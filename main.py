# File: main.py
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


class ClockApp(App):
	pass


if __name__ == '__main__':
	Window.clearcolor = get_color_from_hex('#38548a')
	LabelBase.register(name='Roboto',
		fn_regular='Roboto-Light.ttf',
		fn_bold='Roboto-Medium.ttf')
	ClockApp().run()
