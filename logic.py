import random

# Variables

ridingIterator = 1
numberOfRidings = int(input("How many ridings exist in this election?"))
title = '===============\n\bFederal Election Simulator 2021:\n===============\n'

federalLPCSUM = 0
federalCPCSUM = 0
federalNDPSUM = 0
federalGRNSUM = 0
federalPPCSUM = 0

dynamicLPC = 5
dynamicCPC = 5
dynamicNDP = 3
dynamicGRN = 1
dynamicPPC = 2


class Party:
    def __init__(self, name, weight, votes):
        self.name = name
        self.weight = weight
        self.votes = 0


def popularity_handler(x):
    return "{:.0%}".format(x / population)


def density_bias(x):
    p = population / 10000
    return x*p



class Riding:
    def __init__(self, name):
        self.name = name
        ridingWeight = 0


LPC = Party("Liberal Party of Canada", dynamicLPC, 0)
CPC = Party("Conservative Party of Canada", dynamicCPC, 0)
NDP = Party("New Democratic Party of Canada", dynamicNDP, 0)
GRN = Party("Green Party of Canada", dynamicGRN, 0)
PPC = Party("People's Party of Canada", dynamicPPC, 0)

partyList = [LPC, CPC, NDP, GRN, PPC]


class Citizen:
    def __init__(self):
        self.preference = random.choices(partyList,
                                         weights=[density_bias(LPC.weight), density_bias(CPC.weight), density_bias(NDP.weight), density_bias(GRN.weight), density_bias(PPC.weight)])


print(title)

for i in range(0, numberOfRidings):
    ridingInstance = Riding("Federal Riding " + str(ridingIterator))
    population = int(input(f"What is the population of Federal Riding {str(ridingIterator)}? "))

    # Recording citizen classes choice and then counting it
    voteList = []
    for i in range(0, population):
        voteList.append(Citizen())
    for i in range(0, population):
        voteList[i].preference[0].votes += 1

    # Printing results + percentages and totals
    print('\n')
    for i in range(0, len(partyList)):
        print(f"{partyList[i].name}, {popularity_handler(partyList[i].votes)} | {partyList[i].votes} votes cast")
    total = [LPC.votes, CPC.votes, NDP.votes, GRN.votes, PPC.votes]
    sortedTotal = [(sorted(total, reverse=True))]

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

    print('\n',victor.name,
          f'has received the majority of the vote ({max(total)} votes) and have won in {ridingInstance.name}.\n')
    ridingIterator += 1

    # Reset voting variables
    for i in range(0, len(partyList)):
        partyList[i].votes = 0

print(f'Liberal vote sum of      ', federalLPCSUM, 'votes | Electoral performance was weighted at a',LPC.weight)
print(f'Conservative vote sum of ', federalCPCSUM, 'votes | Electoral performance was weighted at a',CPC.weight)
print(f'NDP vote sum of          ', federalNDPSUM, 'votes | Electoral performance was weighted at a',NDP.weight)
print(f'Green vote sum of        ', federalGRNSUM, 'votes | Electoral performance was weighted at a',GRN.weight)
print(f"People's vote sum of     ", federalPPCSUM, 'votes | Electoral performance was weighted at a',PPC.weight)
