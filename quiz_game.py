from random import randint
import random

print("\nPrepare yourself for the quiz of all quizzes!\n")

begin = input("Shall we begin?\n\nA) Yes. B) No. [A/B]? : ")

if (begin == "B"):
    quit()

praises = ["\nGreat Job!", "\nThat's Right!", "\nThat Is Correct!", "\nKeep It Up!", "\nNice Work!"]
sorry = ["\nIncorrect...", "\nThat's Not Right...", "\nWrong Answer..."]
determine = None
score = 0

def condition():
    if(determine == True):
        print(praises[randint(0, len(praises) - 1)])
    if(determine == False):
        print(sorry[randint(0, len(sorry) - 1)])

print("\nLet's begin!")

answer = input("\nIn school, Albert Einstein failed most of the subjects, except for physics and math.\n\nA) Yes. B) No. [A/B] ? : ")
a1 = "A"
if (answer == a1):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nThe first song ever sung in space was “Happy Birthday”.\n\nA) Yes. B) No. [A/B] ? : ")
a2 = "A"
if (answer == a2):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nThe first country in the world to use postcards was the United States of America.\n\nA) Yes. B) No. [A/B] ? : ")
a3 = "B"
if (answer == a3):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nThe first product with a bar code was chewing gum.\n\nA) Yes. B) No. [A/B] ? : ")
a4 = "A"
if (answer == a4):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nJohn F. Kennedy is one of the four U.S. President who is on Mount Rushmore.\n\nA) Yes. B) No. [A/B] ? : ")
a5 = "B"
if (answer == a5):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nMice have more bones than humans.\n\nA) Yes. B) No. [A/B] ? : ")
a6 = "A"
if (answer == a6):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nThe capital of Australia is Sydney.\n\nA) Yes. B) No. [A/B] ? : ")
a7 = "B"
if (answer == a7):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nThe World War II began in 1939 when Germany invaded Poland.\n\nA) Yes. B) No. [A/B] ? : ")
a8 = "A"
if (answer == a8):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nThe FIFA World Cup 2022 will take place in Iran.\n\nA) Yes. B) No. [A/B] ? : ")
a9 = "B"
if (answer == a9):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

answer = input("\nAB- is the rarest type of blood in humans.\n\nA) Yes. B) No. [A/B] ? : ")
a10 = "A"
if (answer == a10):
    determine = True
    score += 1
    condition()
else:
    determine = False
    condition()

print("\nYour final score is " + str(score) + "!\n")