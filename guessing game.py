import random
while True:
    try:
        level = int(input("level: "))
        if level < 0:
            continue
        else:
            level = random.randint(0, level)
            break
    except ValueError:
        continue
while True: 
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
    except ValueError:
        continue   
    if guess > level:
        print("Too large!")
        continue
    elif guess < level:
        print("Too small!")
        continue
    elif guess == level:
        print("Just right!")
    break
        
        
 