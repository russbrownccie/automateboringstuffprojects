# this program attempts to calculate the odds of getting 6 heads or tails in a coinflip done 100 times -
# (it does this 10k times for a final sample)
# note the math is around 80.68% which is what we come up with in this simulation
# see https://www.quora.com/What-is-the-probability-in-percent-of-getting-six-heads-in-a-row-or-six-tails-in-a-row-
# if-you-flip-a-coin-100-times-this-is-not-a-homework-problem


import random
numberOfStreaks = 0

for experimentNumber in range(10000):

    possibleStreak = ""  # This will be the string of heads or tails - we'll do 100 flips before verifying

    for i in range(100):

        flip = random.randint(1, 2)
        if flip == 1:
            possibleStreak = possibleStreak + "H"
            i += 1
        else:
            possibleStreak = possibleStreak + "T"
            i += 1
    # now we'll examine the possibleStreak string in slices of 6 each - if we get a hit we end the search and start over
    start_streak = 0
    end_streak = 6

    while end_streak <= 100:
        if possibleStreak[start_streak:end_streak] == "HHHHHH" or possibleStreak[start_streak:end_streak] == "TTTTTT":
            numberOfStreaks += 1
            end_streak = 101
        else:
            start_streak += 1
            end_streak += 1

print('chance of streak: %s%%' % (numberOfStreaks / 100))
