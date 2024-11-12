import pandas as pd
import pyperclip
import pyautogui
import time
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.resources import resource_add_path
from kivy.uix.slider import Slider
from kivy.graphics import Color, RoundedRectangle
from kivy.config import Config

# 设置窗口为可调整大小
Config.set('graphics', 'resizable', '1')
Config.write()

# 添加字体文件路径
resource_add_path(r'C:\Users\Public\Documents\CLO\Assets\Font')
# 注册字体
LabelBase.register(name='SourceHanSansSC', fn_regular='SourceHanSansSC-Regular-2.otf')

class RoundedButton(Button):
    def __init__(self, bg_color=(1, 0.84, 0, 1), **kwargs):
        super().__init__(**kwargs)
        self.bg_color = bg_color
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
        self.color = (0.11, 0.11, 0.11, 1)
        self.bind(size=self.update_canvas, pos=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[20,])

class RoundedTextInput(TextInput):
    def __init__(self, bg_color=(0.2, 0.2, 0.2, 1), **kwargs):
        super().__init__(**kwargs)
        self.bg_color = bg_color
        self.background_color = (0, 0, 0, 0)
        self.foreground_color = (1, 1, 1, 1)
        self.cursor_color = (1, 0.84, 0, 1)
        self.bind(size=self.update_canvas, pos=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=[20,])

class MJOutputTool(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        file_layout = BoxLayout(size_hint_y=None, height=50, spacing=15)
        self.file_input = RoundedTextInput(multiline=False, font_name='SourceHanSansSC', padding=[15, 15, 0, 0], font_size=16)
        file_layout.add_widget(self.file_input)
        browse_button = RoundedButton(text="浏览", on_press=self.browse_file, size_hint_x=None, width=120, 
                              font_name='SourceHanSansSC', font_size=16)
        file_layout.add_widget(browse_button)
        self.add_widget(file_layout)

        slider_layout = BoxLayout(size_hint_y=None, height=50, spacing=15)
        slider_layout.add_widget(Label(text="输出间隔(秒):", font_name='SourceHanSansSC', size_hint_x=None, width=140, color=(1, 1, 1, 1), font_size=16))
        self.interval_slider = Slider(min=1, max=10, value=3, step=0.5)
        slider_layout.add_widget(self.interval_slider)
        self.interval_label = Label(text="3", font_name='SourceHanSansSC', size_hint_x=None, width=40, color=(1, 1, 1, 1), font_size=16)
        slider_layout.add_widget(self.interval_label)
        self.add_widget(slider_layout)
        self.interval_slider.bind(value=self.on_slider_value)

        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=15)
        self.start_button = RoundedButton(text="启动", on_press=self.start, font_name='SourceHanSansSC', font_size=18)
        self.pause_button = RoundedButton(text="暂停", on_press=self.pause, disabled=True, bg_color=(0.9, 0.3, 0.1, 1), font_name='SourceHanSansSC', font_size=18)
        button_layout.add_widget(self.start_button)
        button_layout.add_widget(self.pause_button)
        self.add_widget(button_layout)

        self.status_label = Label(text="      ", font_name='SourceHanSansSC', color=(1, 1, 1, 1), font_size=16)
        self.add_widget(self.status_label)

        self.running = False

    def on_slider_value(self, instance, value):
        self.interval_label.text = str(round(value, 1))

    def browse_file(self, instance):
        from plyer import filechooser
        result = filechooser.open_file(filters=[("Excel files", "*.xlsx")])
        if result:
            self.file_input.text = result[0]
        else:
            self.status_label.text = "未选择文件"

    def start(self, instance):
        self.running = True
        self.start_button.disabled = True
        self.pause_button.disabled = False
        threading.Thread(target=self.merge_and_copy_excel).start()

    def pause(self, instance):
        self.running = False
        self.start_button.disabled = False
        self.pause_button.disabled = True

    def merge_and_copy_excel(self):
        file_path = self.file_input.text
        if not file_path:
            Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', "请先选择文件"))
            return

        try:
            df = pd.read_excel(file_path, engine='openpyxl')
        except Exception as e:
            Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', f"读取文件错误: {str(e)}"))
            return

        merged_rows = [' '.join(row.astype(str)) for _, row in df.iterrows()]

        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', 
                            "内容已复制到剪贴板，将按顺序输出每一行..."))

        for merged_row in merged_rows:
            if not self.running:
                break
            pyperclip.copy(merged_row)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(self.interval_slider.value)

        Clock.schedule_once(lambda dt: setattr(self.status_label, 'text', "完成!"))
        Clock.schedule_once(lambda dt: setattr(self.start_button, 'disabled', False))
        Clock.schedule_once(lambda dt: setattr(self.pause_button, 'disabled', True))

class MJOutputApp(App):
    def build(self):
        Window.clearcolor = (0.11, 0.11, 0.11, 1)  # 设置窗口背景颜色为深灰色
        Window.size = (500, 270)  # 设置初始窗口大小
        Window.minimum_width, Window.minimum_height = 400, 300  # 设置最小窗口大小
        Window.borderless = False  # 确保窗口有边框
        Window.fullscreen = False  # 确保不是全屏模式
        self.title = 'MJ Output Tool'  # 设置窗口标题
        return MJOutputTool()
    
if __name__ == '__main__':
    MJOutputApp().run()
