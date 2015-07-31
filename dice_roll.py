import random

 #NUM_DICE_ROLLS =

print "Rolling the dice."



def timesRolled():

    i = True
    NUM_DICE_ROLLS = 0

    while i == True:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        NUM_DICE_ROLLS = NUM_DICE_ROLLS + 1
        if roll1 == roll2 == 6:
            i = False
    return NUM_DICE_ROLLS

print timesRolled()

sum1 = 0

for num_times_rolled in range(1, 3):
    sum1 += timesRolled()
    print sum1

a = sum1 / (2.0)

print a
