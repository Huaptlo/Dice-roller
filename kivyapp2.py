import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
kivy.require('2.1.0')
from kivy.uix.dropdown import DropDown
Config.set('graphics', 'resizable', True)

class MyApp(App):
  
    def build(self):
        Fl = FloatLayout()
        btn1 = Button(text ='Dice', size_hint =(.3, .3),
                     background_color =(.3, .6, .7, 1),
                    pos_hint ={'x':.1, 'y':.6 })
        
        btn2 = Button(text ='Amount', size_hint =(.3, .3),
                     background_color =(.3, .6, .7, 1),
                    pos_hint ={'x':.1, 'y':.1 })
        
        Fl.add_widget(btn1,btn2)
        return Fl

if __name__ == "__main__":
    MyApp().run()