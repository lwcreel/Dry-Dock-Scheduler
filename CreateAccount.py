from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

Window.size = (500,700)
Window.clearcolor = (1,1,1,1)

class MainApp(App):
    def build(self):
        layout = FloatLayout(size=(500, 700))
        label1 = Label(text='[color=00000]Create Account[/color]',
                      size_hint=(.25, .25),
                      pos=(193,550),
                      markup = True)
        layout.add_widget(label1)
        label2 = Label(text='[color=00000]E-mail[/color]',
                      size_hint=(.25, .25),
                      pos=(0,500),
                      markup = True)
        layout.add_widget(label2)
        text1 = TextInput(text='Enter email',
                      size_hint=(.9,.05),
                      pos=(25,540))
        layout.add_widget(text1)
        label3 = Label(text='[color=00000]Username[/color]',
                      size_hint=(.25, .25),
                      pos=(10,420),
                      markup = True)
        layout.add_widget(label3)
        text2 = TextInput(text='Enter username',
                      size_hint=(.9,.05),
                      pos=(25,460))
        layout.add_widget(text2)
        label4 = Label(text='[color=00000]Password[/color]',
                      size_hint=(.25, .25),
                      pos=(10,340),
                      markup = True)
        layout.add_widget(label4)
        text3 = TextInput(text='Enter password',
                      size_hint=(.9,.05),
                      pos=(25,380))
        layout.add_widget(text3)
        label5 = Label(text='[color=00000]Confirm Password[/color]',
                      size_hint=(.25, .25),
                      pos=(35,260),
                      markup = True)
        layout.add_widget(label5)
        text4 = TextInput(text='Enter password',
                      size_hint=(.9,.05),
                      pos=(25,300))
        layout.add_widget(text4)
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()
        