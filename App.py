import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import ButtonBehavior

Window.size = (500,700)
Window.clearcolor = (1,1,1,1)


class MainApp(App):
    def build(self):
        layout = FloatLayout(size=(500, 700))
        label1 = Label(text='[color=00000]Sea Scheduler[/color]',
                      size_hint=(.25, .25),
                      pos=(193,550),
                      markup = True)
        layout.add_widget(label1)
        label2 = Label(text='[color=00000]Welcome to the Sea Scheduler![/color]',
                      size_hint=(.25, .25),
                      pos=(192, 400),
                      markup = True)
        layout.add_widget(label2)
        label3 = Label(text='[color=00000]To get started, log in to begin scheduling[/color]',
                      size_hint=(.25,.25),
                      pos=(192,380),
                      markup = True)
        layout.add_widget(label3)
        btn1 = Button(text='Log In',
                      size_hint = (.4, .05),
                      pos=(153, 340))
        btn2 = Button(text='Create Account',
                      size_hint = (.4, .05),
                      pos=(153, 280))
        btn3 = Button(text='Contact Dock',
                      size_hint = (.4, .05),
                      pos=(153, 220))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout
        
if __name__ == '__main__':
    app = MainApp()
    app.run()