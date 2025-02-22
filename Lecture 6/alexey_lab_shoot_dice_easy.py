from random import randint as r

user_result = int(input('Put 1 2 or 3 to play the dice -->'))
comp_result = r(1, 4)

win_or_not = 'are you winning son' if user_result == comp_result \
            else 'are you loser son?'
print(win_or_not)
