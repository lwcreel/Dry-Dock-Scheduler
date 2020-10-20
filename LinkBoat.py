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
        label1 = Label(text='[color=00000]Enter your boat information[/color]',
                      size_hint=(.25, .25),
                      pos=(193,550),
                      markup = True)
        layout.add_widget(label1)
        label2 = Label(text='[color=00000]Marina Name[/color]',
                      size_hint=(.25, .25),
                      pos=(10,500),
                      markup = True)
        layout.add_widget(label2)
        text1 = TextInput(text='Enter marina name',
                      size_hint=(.9,.05),
                      pos=(25,540))
        layout.add_widget(text1)
        label3 = Label(text='[color=00000]Boat tag[/color]',
                      size_hint=(.25, .25),
                      pos=(10,420),
                      markup = True)
        layout.add_widget(label3)
        text2 = TextInput(text='Enter boat tag',
                      size_hint=(.9,.05),
                      pos=(25,460))
        layout.add_widget(text2)
        btn1 = Button(text='Link boat to account',
                      size_hint = (.4, .05),
                      pos=(153, 390))
        layout.add_widget(btn1)
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()