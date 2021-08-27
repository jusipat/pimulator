import random

# Variables
population = 30
ridingIterator = 1
numberOfRidings = int(input("How many ridings exist in this election?"))
title = '\bModel of Canadian 2019 General Election:\n'


class Party:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.votes = 0


def popularity_handler(x):
    return "{:.0%}".format(x / population)


class Riding:
    def __init__(self, name, result):
        self.name = name
        self.result = result


LPC = Party("Liberal Party of Canada", 4, )
CPC = Party("Conservative Party of Canada", 3)
NDP = Party("New Democratic Party of Canada", 2)
GRN = Party("Green Party of Canada", 1)
PPC = Party("People's Party of Canada", 1)
X = Party("Refused Ballots", 1)

partyList = [LPC, CPC, NDP, GRN, PPC, X]

for i in range(0, numberOfRidings):
    ridingInstance = Riding("Federal Riding " + str(ridingIterator), popularity_handler(partyList[i].votes))
    ridingIterator += 1
    print(ridingInstance.name, "has elected", ridingInstance.result)

# Console text

print(title)


# Establishing variables
class Citizen:
    def __init__(self):
        self.preference = random.choices(partyList,
                                         weights=[LPC.weight, CPC.weight, NDP.weight, GRN.weight, PPC.weight, X.weight])


# Recording citizen classes choice and then counting it
voteList = []
for i in range(0, population):
    voteList.append(Citizen())
for i in range(0, population):
    voteList[i].preference[0].votes += 1

# Printing results + percentages and totals
for i in range(0, len(partyList)):
    print(f"{partyList[i].name}, {popularity_handler(partyList[i].votes)} | {partyList[i].votes} votes cast")
total = [LPC.votes, CPC.votes, NDP.votes, GRN.votes, PPC.votes]
print(f"Total Votes Cast: {sum(total)}")

if max(total) == LPC.votes:
    victor = LPC
elif max(total) == CPC.votes:
    victor = CPC
elif max(total) == NDP.votes:
    victor = NDP
elif max(total) == GRN.votes:
    victor = GRN
elif max(total) == PPC.votes:
    victor = PPC

print(victor.name, f'has received the majority of the vote ({max(total)} votes) and has won in {ridingInstance.name}.')
ridingIterator += 1
