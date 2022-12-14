import dice

noppa = int(input("What dice: "))
amount = int(input("How many dice: "))
nopat = str(f'{amount}d{noppa}')

print(dice.roll(nopat))