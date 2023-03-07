import kivy
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.base import runTouchApp
kivy.require('2.1.0')
Config.set('graphics', 'resizable', True)

class DiceRoller(App):
  
    def build(self):
        Fl = FloatLayout()
        dropdown = DropDown()

        for index in range(7):
            btn1 = Button(text ='D4', size_hint_y = None, height = 30,
                    background_color =(.3, .6, .7, 1))
            btn1.bind(on_release = lambda btn: dropdown.select(btn.text))

            btn2 = Button(text ='D6', size_hint_y = None, height = 30,
                    background_color =(.3, .6, .7, 1))
            btn2.bind(on_release = lambda btn: dropdown.select(btn.text))

            btn3 = Button(text ='D8', size_hint_y = None, height = 30,
                    background_color =(.3, .6, .7, 1))
            btn3.bind(on_release = lambda btn: dropdown.select(btn.text))

            btn4 = Button(text ='D10', size_hint_y = None, height = 30,
                    background_color =(.3, .6, .7, 1))
            btn4.bind(on_release = lambda btn: dropdown.select(btn.text))

            btn5 = Button(text ='D12', size_hint_y = None, height = 30,
                    background_color =(.3, .6, .7, 1))
            btn5.bind(on_release = lambda btn: dropdown.select(btn.text))

            btn6 = Button(text ='D20', size_hint_y = None, height = 30,
                    background_color =(.3, .6, .7, 1))
            btn6.bind(on_release = lambda btn: dropdown.select(btn.text))

            btn7 = Button(text ='D100', size_hint_y = None, height = 30,
                    background_color =(.3, .6, .7, 1))
            btn7.bind(on_release = lambda btn: dropdown.select(btn.text))

            dropdown.add_widget(btn1)
            dropdown.add_widget(btn2)
            dropdown.add_widget(btn3)
            dropdown.add_widget(btn4)
            dropdown.add_widget(btn5)
            dropdown.add_widget(btn6)
            dropdown.add_widget(btn7)

            break

        main_btn = Button(text ='Dice', size_hint =(.3, .2),
                            background_color =(.3, .6, .7, 1), pos_hint ={'x':.1, 'y':.5})
        main_btn.bind(on_release = dropdown.open)
        dropdown.bind(on_select = lambda instance, x: setattr(main_btn, 'text', x))

        for i in range(1,11):
            btn8 = Button(text ='%d' % i, size_hint_y = None, height = 30,
                    background_color =(.3, .6, .7, 1))
            btn8.bind(on_release = lambda btn: dropdown.select(btn.text))

            dropdown.add_widget(btn8)

        dice_amount_btn = Button(text ='Amount', size_hint =(.3, .2),
                            background_color =(.3, .6, .7, 1), pos_hint ={'x':.6, 'y':.5})
        dice_amount_btn.bind(on_release = dropdown.open)
        dropdown.bind(on_select = lambda instance, x: setattr(dice_amount_btn, 'text', x))
        
        # dice_amount_btn = Button(text ='Amount', size_hint =(.3, .2),
        #             background_color =(.3, .6, .7, 1),
        #             pos_hint ={'x':.6, 'y':.5 })

        roll_btn = Button(text ='Roll', size_hint =(.5, .2),
                    background_color =(.3, .6, .7, 1),
                    pos_hint ={'x':.25, 'y':.2 })

        result_box = TextInput(text = "0",
                    pos_hint = {'x':.1, 'y':.75},
                    font_size = 45,
                    size_hint = (.8,.15))

        self.close_btn = Button(text = 'X', size_hint =(.05, .05),
                    background_color =(.3, .6, .7, 1),
                    pos_hint ={'x':.9, 'y':.9})
        self.close_btn.bind(on_release=self.close_app)

        Fl.add_widget(main_btn) 
        Fl.add_widget(dice_amount_btn)
        Fl.add_widget(roll_btn)
        Fl.add_widget(result_box)
        Fl.add_widget(self.close_btn)

        return Fl

    def close_app(self, instance):
        App.get_running_app().stop()

# Window.fullscreen = 'auto'

if __name__ == "__main__":
    DiceRoller().run()