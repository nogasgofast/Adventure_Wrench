import sys
import dice

dice_roller = dice.dice()
print dice_roller.roll(sys.argv[1])
