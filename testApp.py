import kivy

#Replace '1.8' with your current version of kivy
kivy.require('1.8')

#The base class inherits fom the App class and Label class respectively
from kivy.app import App
from kivy.uix.label import Label

#The base class is defined in this function
class MyApp(App):

    def build(self):
        return Label(text='Hello world')

#MyApp() is initialized and the run() method is called on it
if __name__ == '__main__':
    MyApp().run()