#File name : main.py
import kivy
kivy.require('1.0.1')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

count = 0

class ButtonInc():
    def callback(instance):
        global count 
        count += 1
        print('The button <%s> is being pressed' % instance.text)
        print count
        
class ButtonDec():
    def callback(instance):
        global count
        count -= 1
        print('The button <%s> is being pressed' % instance.text) 
        print count
        
        
class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        btn_1 = Button(text = '+1')
        btn_2 = Button(text = '-1')
        layout.add_widget(btn_1)
        layout.add_widget(btn_2)
        
        btn_1.bind(on_press=ButtonInc.callback)
        btn_2.bind(on_press=ButtonDec.callback)
        print Label(text = 'count')
        return layout
        
if __name__ == '__main__':
    MyApp().run()