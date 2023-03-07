import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
import dice

class DiceRoller(FloatLayout):
    def __init__(self, **kwargs):
        super(DiceRoller, self).__init__(**kwargs)

        # Dropdown to choose dice type
        dropdown = DropDown()
        for sides in [4, 6, 8, 10, 12, 20, 100]:
            btn = Button(text=str(sides), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: dropdown.select(btn.text))
            dropdown.add_widget(btn)
        self.dice_type = Button(text='4', size_hint=(0.3, 0.1), pos_hint={'x': 0.05, 'y': 0.8})
        self.dice_type.bind(on_release=dropdown.open)
        dropdown.bind(on_select=lambda instance, x: setattr(self.dice_type, 'text', x))
        self.add_widget(self.dice_type)

        # Scroll bar to choose number of dice to roll
        self.num_dice_label = Label(text='Number of Dice: 1', size_hint=(0.3, 0.1), pos_hint={'x': 0.05, 'y': 0.65})
        self.add_widget(self.num_dice_label)
        self.num_dice_slider = Slider(min=1, max=20, value=1, step=1, size_hint=(0.4, 0.1), pos_hint={'x': 0.35, 'y': 0.65})
        self.num_dice_slider.bind(value=self.update_num_dice)
        self.add_widget(self.num_dice_slider)

        # Button to roll dice
        self.roll_button = Button(text='Roll', size_hint=(0.3, 0.1), pos_hint={'x': 0.05, 'y': 0.5})
        self.roll_button.bind(on_release=self.roll_dice)
        self.add_widget(self.roll_button)

        # Field to display dice result
        self.result_label = Label(text='Result: ', size_hint=(0.9, 0.1), pos_hint={'x': 0.05, 'y': 0.3})
        self.add_widget(self.result_label)

    # Function for the number of dice
    def update_num_dice(self, instance, value):
        self.num_dice_label.text = 'Number of Dice: ' + str(int(value))

    # Function to roll the dice
    def roll_dice(self, instance):
        num_dice = int(self.num_dice_slider.value)
        dice_type = int(self.dice_type.text)
        result = str(f'{num_dice}d{dice_type}')
        self.result_label.text = str(dice.roll(result))

class DiceRollerApp(App):
    def build(self):
        return DiceRoller()

if __name__ == '__main__':
    DiceRollerApp().run()
