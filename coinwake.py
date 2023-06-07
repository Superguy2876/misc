from random import randint as ri

monday0 = 0
monday1 = 0
tuesday1 = 0

for i in range(1000):
    coin = ri(1)
    if coin:
        monday0 += 1
    else:
        
