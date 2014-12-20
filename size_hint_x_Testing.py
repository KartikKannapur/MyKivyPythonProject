import kivy

kivy.require('1.0.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        print "Down"
    def on_touch_up(self, touch):
    	print "Up"

class MyPaintApp(App):
    
    def build(self):
        return MyPaintWidget()

if __name__ == '__main__':
    MyPaintApp().run()