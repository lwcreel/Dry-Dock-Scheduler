from kivy.app import App
from kivy.uix.label import Label

# main app subclass for ui
class MainApp(App):

    # defines how the UI is initially built
    def build(self):
        label = Label(text='Hello from Kivy',
                      size_hint=(.5, .5),
                      pos_hint={'center_x': .5, 'center_y': .5})

        return label

# framework run stuff
if __name__ == '__main__':
    app = MainApp()
    app.run()