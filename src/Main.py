from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.properties import *
import itertools
import heapq
from dbAPI import *

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

class LogInOwnerFailed(Screen):
    pass

class LogInWorker(Screen):
    pass

class LogInWorkerFailed(Screen):
    pass

class NewAccountLinkBoat(Screen):
    pass

class LinkBoat(Screen):
    pass

class LinkConfirm(Screen):
    pass

class ResetPassword(Screen):
    def resetPassword(self, username, email):
        value = changePassword(username, email, 'temp1')
        if(value):
            self.label_wid.text = 'Success! Temporary password is temp1, please change after logging in.'
        else:
            self.label_wid.text = 'Oops! The username and/or email do no match an account in our records. Please try again.'

class HomeScreenOwner(Screen):
    def getStatusBoat(self, username):
        value = getStatus(username)
        if(value == 0):
            self.label_wid.text = 'Your boat is in the dry dock'
        else:
            self.label_wid.text = 'Your boat is in the water'

class HomeScreenWorker(Screen):
    pass

class LogOutConfirmWorker(Screen):
    pass

class LogOutConfirmOwner(Screen):
    pass

class ScheduleTime(Screen):
    pass

class ScheduleWorker(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    loginNextScreen = ''
    createNextScreen = ''
    username = ''
    bid = -1
    def createAccount(self, nameText, emailText, passwordText, confirmPasswordText, isWorker):
        val = createUser(nameText, emailText, passwordText, confirmPasswordText, isWorker)
        if(val):
            self.username = nameText
            if(isWorker):
                self.createNextScreen = 'homeworker'
            else:
                self.createNextScreen = 'newlink'
        else:
            if(isWorker):
                self.createNextScreen = 'createworker'
            else:
                self.createNextScreen = 'createowner'

    def tryLogin(self, nameText, passwordText, isWorker):
        val = login(nameText, passwordText, isWorker)
        if(val):
            self.username = nameText
            if(isWorker):
                self.loginNextScreen = 'homeworker'
            else:
                self.loginNextScreen = 'homeowner'
        else:
            if(isWorker):
                self.loginNextScreen = 'loginworkerfailed'
            else:
                self.loginNextScreen = 'loginownerfailed'

    def linkBoat(self, makeAndModel, year):
        createBoat(makeAndModel, self.username, year, 0)

    priorityQueue = []
    counter = itertools.count()
    def schedule(self, timeValue):
        queueBoat(self.bid, self.username, timeValue)
        timeCalc = timeValue.split(':')
        if timeCalc[1][2] == 'p' and timeCalc[0] != '12':
            time = int(str((int(timeCalc[0])+12)) + timeCalc[1][:2])
        else:
            time = int(timeCalc[0] + timeCalc[1][:2])
        count = next(self.counter)
        heapq.heappush(self.priorityQueue, (time, count, [self.bid, self.username]))

    

    def build(self):
        return presentation

   


MainApp().run()