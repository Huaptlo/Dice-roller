import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
kivy.require('2.1.0')
Config.set('graphics', 'resizable', True)

class MyApp(App):
  
    def build(self):
        Fl = FloatLayout()
        dropdown = DropDown()

        for index in range(7):
            btn1 = Button(text ='Value % d' % index, size_hint_y = None, height = 40)
            btn1.bind(on_release = lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn1)

        mainbutton = Button(text ='Dice', size_hint =(.3, .3),
                            background_color =(.3, .6, .7, 1), pos_hint ={'x':.1, 'y':.6})
        mainbutton.bind(on_release = dropdown.open)
        dropdown.bind(on_select = lambda instance, x: setattr(mainbutton, 'text', x))
        
        btn2 = Button(text ='Amount', size_hint =(.3, .3),
                     background_color =(.3, .6, .7, 1),
                    pos_hint ={'x':.6, 'y':.6 })

        Fl.add_widget(mainbutton) 
        Fl.add_widget(btn2)

        return Fl

if __name__ == "__main__":
    MyApp().run()