import dice

noppa = int(input("What dice: "))
maara = int(input("How many dice: "))
nopat = str(f'{maara}d{noppa}')

print(dice.roll(nopat))