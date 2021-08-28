import random

# Variables
population = 1000
ridingIterator = 1
numberOfRidings = int(input("How many ridings exist in this election?"))
title = '===============\n\bFederal Election Simulator 2021:\n===============\n'

federalLPCSUM = 0
federalCPCSUM = 0
federalNDPSUM = 0
federalGRNSUM = 0
federalPPCSUM = 0


class Party:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.votes = 0


def popularity_handler(x):
    return "{:.0%}".format(x / population)


class Riding:
    def __init__(self, name):
        self.name = name



LPC = Party("Liberal Party of Canada", 4, )
CPC = Party("Conservative Party of Canada", 3)
NDP = Party("New Democratic Party of Canada", 2)
GRN = Party("Green Party of Canada", 1)
PPC = Party("People's Party of Canada", 1)

partyList = [LPC, CPC, NDP, GRN, PPC]


class Citizen:
    def __init__(self):
        self.preference = random.choices(partyList,
                                         weights=[LPC.weight, CPC.weight, NDP.weight, GRN.weight, PPC.weight])


print(title)

for i in range(0, numberOfRidings):
    for i in range(0, numberOfRidings):
        ridingInstance = Riding("Federal Riding " + str(ridingIterator))

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

    federalLPCSUM += partyList[0].votes
    federalCPCSUM += partyList[1].votes
    federalNDPSUM += partyList[2].votes
    federalGRNSUM += partyList[3].votes
    federalPPCSUM += partyList[4].votes

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

    print(victor.name,
          f'has received the majority of the vote ({max(total)} votes) and have won in {ridingInstance.name}.\n')
    ridingIterator += 1

    # Reset voting variables
    partyList[0].votes = 0
    partyList[1].votes = 0
    partyList[2].votes = 0
    partyList[3].votes = 0
    partyList[4].votes = 0

print('Liberal vote sum of ', federalLPCSUM)
print('Conservative vote sum of ', federalCPCSUM)
print('Progressive vote sum of ', federalNDPSUM)
print('Green vote sum of ', federalGRNSUM)
print("People's vote sum of", federalPPCSUM)
