# File: main.py
from kivy.app import App
from kivy.core.text import LabelBase


class ClockApp(App):
	pass


if __name__ == '__main__':
	LabelBase.register(name='Roboto',
		fn_regular='Roboto-Light.ttf',
		fn_bold='Roboto-Medium.ttf')
	ClockApp().run()
