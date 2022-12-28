from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
import dice

class DiceRollerApp(App):
    def build(self):
        self.layout = FloatLayout()

        # create a dropdown menu to choose the number of sides on the dice
        self.sides_dropdown = DropDown()
        for num_sides in (4, 6, 8, 10, 12, 20, 100):
            btn = Button(text=str(num_sides), size_hint_y=None, height=44)
            btn.bind(on_release=lambda btn: self.sides_dropdown.select(btn.text))
            self.sides_dropdown.add_widget(btn)
        self.sides_button = Button(text="4", size_hint=(None, None))
        self.sides_button.bind(on_release=self.sides_dropdown.open)
        self.sides_dropdown.bind(on_select=lambda instance, x: setattr(self.sides_button, 'text', x))
        self.layout.add_widget(self.sides_button)

        # create a label and text input for the number of dice to roll
        dice_label = Label(text="Choose the number of dice to roll:")
        self.dice_input = TextInput(text='1', multiline=False)
        self.layout.add_widget(dice_label)
        self.layout.add_widget(self.dice_input)

        # create a button to roll the dice
        self.roll_button = Button(text="Roll the dice!", font_size=20)
        self.roll_button.bind(on_release=self.roll_dice)
        self.layout.add_widget(self.roll_button)

        # create a label to display the results of the dice roll
        self.results_label = Label(text="", font_size=20)
        self.layout.add_widget(self.results_label)

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
        self.results_label.text = f"Results: {results
