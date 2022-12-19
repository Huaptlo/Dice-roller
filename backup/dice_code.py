import dice

dice_value = int(input("What dice: "))
dice_amount = int(input("How many dice: "))
dice_roll = str(f'{dice_amount}d{dice_value}')

print(dice.roll(dice_roll))