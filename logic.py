import random
from CitizenClass import Citizen

population = 10

def popularity_handler(x):
    x = "{:.0%}".format(x)
    return x


def decimalize(x):
    return x / population


groupC = 0
groupA = 0
groupB = 0

# Make a random number to multiply by turnout to simulate turnout number percentage




voteList = []
for i in range(0, population):
    voteList.append(Citizen().preference)
for i in range(0, population):
    if voteList[i] == 1:
        groupA += 1
    elif voteList[i] == 2:
        groupB += 1
    elif voteList[i] == 3:
        groupC += 1

print("GroupA: ", groupA, "votes,", str(popularity_handler(decimalize(groupA))))
print("GroupB: ", groupB, "votes,", str(popularity_handler(decimalize(groupB))))
print("GroupC: ", groupC, "votes,", str(popularity_handler(decimalize(groupC))))
total = groupA + groupB + groupC
print("Total Votes:", total, "|", popularity_handler(total/population) + " Turnout")