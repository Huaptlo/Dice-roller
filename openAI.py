from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import dice

class DiceRollerApp(App):
    def build(self):
        self.layout = FloatLayout()

        # create a dropdown menu to choose the number of sides on the dice
        self.sides_dropdown = DropDown()
        for num_sides in (4, 6, 8, 10, 12, 20, 100):
            btn = Button(text ='Dice', size_hint =(.3, .2), background_color =(.3, .6, .7, 1), pos_hint ={'x':.1, 'y':.5})
            btn.bind(on_release=lambda btn: self.sides_dropdown.select(btn.text))
            self.sides_dropdown.add_widget(btn)
        self.sides_button = Button(text="4", size_hint=(None, None))
        self.sides_button.bind(on_release=self.sides_dropdown.open)
        self.sides_dropdown.bind(on_select=lambda instance, x: setattr(self.sides_button, 'text', x))
        self.layout.add_widget(self.sides_button)

        # create a dropdown menu to choose the number of dice to roll
        self.dice_dropdown = DropDown()
        for num_dice in range(1, 11):
            btn = Button(text ='Amount', size_hint =(.3, .2), background_color =(.3, .6, .7, 1), pos_hint ={'x':.6, 'y':.5 })
            btn.bind(on_release=lambda btn: self.dice_dropdown.select(btn.text))
            self.dice_dropdown.add_widget(btn)
        self.dice_button = Button(text="1", size_hint=(None, None))
        self.dice_button.bind(on_release=self.dice_dropdown.open)
        self.dice_dropdown.bind(on_select=lambda instance, x: setattr(self.dice_button, 'text', x))
        self.layout.add_widget(self.dice_button)

        # create a button to roll the dice
        self.roll_button = Button(text ='Roll', size_hint =(.5, .2), background_color =(.3, .6, .7, 1),pos_hint ={'x':.25, 'y':.2 })
        self.roll_button.bind(on_release=self.roll_dice)
        self.layout.add_widget(self.roll_button)

        # create a label to display the results of the dice roll
        self.results_label = TextInput(text = "0", pos_hint = {'x':.1, 'y':.75}, font_size = 45, size_hint = (.8,.15))
        self.layout.add_widget(self.results_label)

        # create a button to close the app
        self.close_button = Button(text="X", size_hint=(None, None), size=(40, 40), pos_hint={'top': 1, 'right': 1})
        self.close_button.bind(on_release=self.close_app)
        self.layout.add_widget(self.close_button)

        return self.layout

    def roll_dice(self, instance):
        # get the user-specified number of sides and dice
        try:
            num_sides = int(self.sides_button.text)
            num_dice = int(self.dice_input.text)
        except ValueError:
            self.results_label.text = "Invalid input. Please enter valid integers."
            return

        # make sure the number of dice is positive
        if num_dice <= 0:
            self.results_label.text = "Invalid number of dice. Please enter a positive integer."
            return

        # roll the dice and display the results
        results = []
        for i in range(num_dice):
            result = dice.roll(num_sides)
            results.append(result)
        self.results_label.text = (f"Results: {results}")

    def close_app(self, instance):
        App.get_running_app().stop()

if __name__ == "__main__":
    DiceRollerApp().run()
