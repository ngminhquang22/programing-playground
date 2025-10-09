import random
high = 100
low = 1
options = ("Scissor", "Rock", "Paper")
jack = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A" ]

print(random.randint(low,high))
print(random.random())
print(random.choice(options))
random.shuffle(jack)
print(jack)