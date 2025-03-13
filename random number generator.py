import random
number = []
for i in range (0,10):
    number.append(i)


randomValue = []
for i in range(0, 10): 
    randomValue+=(random.randint(0,10))
    
print(randomValue)