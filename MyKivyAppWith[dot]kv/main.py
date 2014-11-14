#File name : main.py
#NOTE : The Initial Part of the 'App's subclass must coincide with the name of the kivy file
#Contd. : Example - If the name of the subclass is FooApp(), then the kivy file must be foo.kv
import kivy

#Replace '1.8' with your current version of kivy
kivy.require('1.0.1')

#The base classes are - App class and Label class respectively
from kivy.app import App
from kivy.uix.label import Label

#The base class inheritance is defined in this function
class MyApp(App):

    def build(self):
        return Label()

#MyApp() is initialized and the run() method is called on it
if __name__ == '__main__':
    MyApp().run()