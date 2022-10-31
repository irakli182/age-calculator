
import random
num = random.randint(1000, 2000)
while True:
    guess = input("guess: ")
    if len(guess) != 4:
        continue
    elif guess.isalpha():
        continue
    else:
        break
print()
b = -1
c = -1
listGuess = []
listFarm = [*str(num)]
for i in range(4):
    increasingGuess = guess[b + 1]
    increasingFarm = str(num)[c + 1]
    b = b + 1
    c = c + 1
    listGuess.append(increasingGuess)
b = -1
c = -1
list_cow = []
list_bull = []
for i in range(4):
    increasingGuess = guess[b + 1]
    increasingFarm = str(num)[c + 1]
    b = b + 1
    c = c + 1
    if increasingGuess == increasingFarm:
        list_cow.append("1")
    else:
        list_bull.append('2')
print("number: " + str(num))
print()
print("guess: " + str(guess))
print()
print("cows: " + str(len(list_cow)))
print("bulls: " + str(len(list_bull)))

