from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
import random

Window.size = (500,700)
Window.clearcolor = (1,1,1,1)

class ScheduleWorker:
    random_number = StringProperty()

    def __init__(self, **kwargs):
        super(ScheduleWorker, self).__init__(**kwargs)
        self.random_number = str(random.randint(1, 100))

    def change_text(self):
        self.random_number = str(random.randint(1, 100))

class MainApp(App):
    def build(self):
        return ScheduleWorker()

if __name__ == '__main__':
    app = MainApp()
    app.run()