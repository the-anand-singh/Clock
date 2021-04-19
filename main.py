# File: main.py
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
import time
from datetime import datetime


class ClockApp(App):
	def update_time(self, nap):
		self.root.ids.time.text = datetime.now().strftime('[b]%H[/b]:%M:%S')

	def on_start(self):
		Clock.schedule_interval(self.update_time, 1)


if __name__ == '__main__':
	Window.clearcolor = get_color_from_hex('#38548a')
	LabelBase.register(name='Roboto',
		fn_regular='Roboto-Light.ttf',
		fn_bold='Roboto-Medium.ttf')
	ClockApp().run()
