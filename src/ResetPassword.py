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
        label1 = Label(text='[color=00000]Reset Password[/color]',
                      size_hint=(.25, .25),
                      pos=(193,550),
                      markup = True)
        layout.add_widget(label1)
        label2 = Label(text='[color=00000]Username/E-mail[/color]',
                      size_hint=(.25, .25),
                      pos=(30,500),
                      markup = True)
        layout.add_widget(label2)
        text1 = TextInput(text='Enter username/email',
                      size_hint=(.9,.05),
                      pos=(25,540))
        layout.add_widget(text1)
        btn1 = Button(text='Link boat to account',
                      size_hint = (.4, .05),
                      pos=(153, 470))
        layout.add_widget(btn1)
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()