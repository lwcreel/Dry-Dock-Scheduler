from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
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
    def createAccount(self, nameText, emailText, passwordText, confirmPasswordText, isWorker):
        val = createUser(nameText, emailText, passwordText, confirmPasswordText, isWorker)
        if(val):
            MainApp.username = nameText
            MainApp.createNextScreen = 'newlink'
        else:
            self.label_wid.text = 'Oops! Something went wrong. Please try again.'
            MainApp.createNextScreen = 'createowner'

class CreateAccountWorker(Screen):
    def createAccount(self, nameText, emailText, passwordText, confirmPasswordText, isWorker):
        val = createUser(nameText, emailText, passwordText, confirmPasswordText, isWorker)
        if(val):
            MainApp.username = nameText
            MainApp.createNextScreen = 'homeworker'
        else:
            self.label_wid.text = 'Oops! Something went wrong. Please try again.'
            MainApp.createNextScreen = 'createworker'

class LogInOwner(Screen):
    def tryLogin(self, nameText, passwordText, isWorker):
        val = login(nameText, passwordText, isWorker)
        if(val):
            MainApp.username = nameText
            MainApp.loginNextScreen = 'homeowner'
        else:
            self.label_wid.text = 'Login Failed'
            MainApp.loginNextScreen = 'loginowner'

class LogInWorker(Screen):
    def tryLogin(self, nameText, passwordText, isWorker):
        val = login(nameText, passwordText, isWorker)
        if(val):
            MainApp.username = nameText
            MainApp.loginNextScreen = 'homeworker'
        else:
            self.label_wid.text = 'Login Failed'
            MainApp.loginNextScreen = 'loginworker'

class NewAccountLinkBoat(Screen):
    pass

class LinkBoat(Screen):
    pass

class LinkConfirm(Screen):
    pass

class ResetPassword(Screen):
    def resetPassword(self, username, email):
        value = changePassword(username, email, 'temp1', 'temp1')
        if(value):
            self.label_wid.text = 'Success! Temporary password is temp1, please change after logging in.'
        else:
            self.label_wid.text = 'Oops! Something was wrong with your entries. Please try again.'

class HomeScreenOwner(Screen):
    def getStatusBoat(self, username):
        value = getStatus(username)
        if(value == 0):
            self.label_wid.text = 'Your boat is in the dry dock'
        else:
            self.label_wid.text = 'Your boat is in the water'

class HomeScreenWorker(Screen):
    pass

class LoggedInChangePasswordOwner(Screen):
    def resetPassword(self, username, email, password, cpassword):
        value = changePassword(username, email, password, cpassword)
        if(value):
            self.label_wid.text = 'Success! Your new password has been set!'
        else:
            self.label_wid.text = 'Oops! Something was wrong with your entries. Please try again.'

class LoggedInChangePasswordWorker(Screen):
    def resetPassword(self, username, email, password, cpassword):
        value = changePassword(username, email, password, cpassword)
        if(value):
            self.label_wid.text = 'Success! Your new password has been set!'
        else:
            self.label_wid.text = 'Oops! Something was wrong with your entries. Please try again.'

class LogOutConfirmWorker(Screen):
    pass

class LogOutConfirmOwner(Screen):
    pass

class ScheduleTime(Screen):
    pass

class ScheduleWorker(Screen):
    displayedItems = ['','','','','','','','','','']
    label_value = ListProperty(displayedItems)
    def refresh(self):
        if(len(MainApp.priorityQueue) < 10):
            for i in range(10):
                if(i < len(MainApp.priorityQueue)):
                    self.displayedItems[i] = self.numToTime(MainApp.priorityQueue[i][0]) + '   ' + MainApp.priorityQueue[i][2][1] + '   ' + str(MainApp.priorityQueue[i][2][0])
                else:
                    self.displayedItems[i] = ''
        else:
            for i in range(10):
                self.displayedItems[i] = self.numToTime(MainApp.priorityQueue[i][0]) + '   ' + MainApp.priorityQueue[i][2][1] + '   ' + str(MainApp.priorityQueue[i][2][0])
        self.label_value = self.displayedItems

    def removeFromQueue(self):
        val = heapq.heappop(MainApp.priorityQueue)
        print(val[2][0])
        dequeueBoat(str(val[2][0]))

    def numToTime(self, num):
        min = num % 100
        num = num // 100
        if num < 12:
            time = 'am'
        elif num == 12:
            time = 'pm'
        else:
            num -= 12
            time = 'pm'
        minstr = ''
        if min == 0:
            minstr = '00'
        else:
            minstr = str(min)
        time = str(num) + ':' + minstr + time
        return time

class MoveBoatToDock(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class MainApp(App):
    loginNextScreen = ''
    createNextScreen = ''
    username = ''
    bid = -1

    def linkBoat(self, makeAndModel, year):
        createBoat(makeAndModel, self.username, year, 0)

    priorityQueue = []
    #heapq.heappush(priorityQueue, (915, 0, [-1, 'test']))
    counter = 0
    def schedule(self, timeValue):
        self.bid = getBoatID(self.username)
        queueBoat(self.bid, self.username, timeValue)
        timeCalc = timeValue.split(':')
        if timeCalc[1][2] == 'p' and timeCalc[0] != '12':
            time = int(str((int(timeCalc[0])+12)) + timeCalc[1][:2])
        else:
            time = int(timeCalc[0] + timeCalc[1][:2])
        self.counter+=1
        heapq.heappush(self.priorityQueue, (time, self.counter, [self.bid, self.username]))
        self.priorityQueue.sort()
        print(self.priorityQueue[0])

    def changeLocation(self, boatID):
        moveBoat(boatID, 0)

    def build(self):
        return presentation

   


MainApp().run()