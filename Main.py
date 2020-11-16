from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

Window.size = (500, 700)

class WelcomeScreen(Screen):
    pass

class WorkerQuestionCreate(Screen):
    pass

class WorkerQuestionLogIn(Screen):
    pass

class CreateAccountOwner(Screen):
    pass

class CreateAccountWorker(Screen):
    pass

class LogInOwner(Screen):
    pass

class LogInWorker(Screen):
    pass

class NewAccountLinkBoat(Screen):
    pass

class LinkBoat(Screen):
    pass

class ResetPassword(Screen):
    pass

class HomeScreenOwner(Screen):
    pass

class HomeScreenWorker(Screen):
    pass

class LogOutConfirmWorker(Screen):
    pass

class LogOutConfirmOwner(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        return presentation

MainApp().run()