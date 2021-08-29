import random

# Variables

ridingIterator = 1
numberOfRidings = int(input("How many riding's exist in this election?"))
title = '===============\n\bFederal Election Simulator 2021:\n===============\n'

federalLPCSUM = 0
federalCPCSUM = 0
federalNDPSUM = 0
federalGRNSUM = 0
federalPPCSUM = 0


class Party:
    def __init__(self, name, weight, votes):
        self.name = name
        self.weight = weight
        self.votes = 0


def popularity_handler(x):
    return "{:.0%}".format(x / population)


def density_bias(party_weight):
    if party_weight == LPC:
        return party_weight.weight / population * 103
    elif party_weight == NDP:
        return party_weight.weight / population * 105
    elif party_weight == GRN:
        return party_weight.weight / population * 101
    elif party_weight == PPC:
        return party_weight.weight
    elif party_weight == PPC and rural:
        return party_weight.weight + 0.5
    elif rural:
        return 2
    else:
        return party_weight.weight


class Riding:
    def __init__(self, name):
        self.name = name


LPC = Party("Liberal Party of Canada", 3, 0)
CPC = Party("Conservative Party of Canada", 3, 0)
NDP = Party("New Democratic Party of Canada", 2, 0)
GRN = Party("Green Party of Canada", .5, 0)
PPC = Party("People's Party of Canada", .7, 0)

partyList = [LPC, CPC, NDP, GRN, PPC]


class Citizen:
    def __init__(self):
        self.preference = random.choices(partyList,
                                         weights=[density_bias(LPC), density_bias(CPC), density_bias(NDP),
                                                  density_bias(GRN), density_bias(PPC)])


print(title)

for i in range(0, numberOfRidings):

    ridingInstance = Riding("Federal Riding " + str(ridingIterator))
    population = int(input(f"What is the population of Federal Riding {str(ridingIterator)}? "))
    isRural = (input("Is this riding rurally based? "))
    if isRural == 'Yes' or 'True' or 'yes' or 'true':
        rural = True
    else:
        rural = False

    # Recording citizen classes choice and then counting it
    voteList = []
    for i in range(0, population):
        voteList.append(Citizen())
    for choices in range(0, population):
        voteList[choices].preference[0].votes += 1

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

    print('\n', victor.name,
          f'has received the majority of the vote ({max(total)} votes) and have won in {ridingInstance.name}.\n')
    ridingIterator += 1

    # Reset voting variables
    for i in range(0, len(partyList)):
        partyList[i].votes = 0

print(f'Liberal vote sum of      ', federalLPCSUM, 'votes | Electoral performance was weighted at a', density_bias(LPC))
print(f'Conservative vote sum of ', federalCPCSUM, 'votes | Electoral performance was weighted at a', density_bias(CPC))
print(f'NDP vote sum of          ', federalNDPSUM, 'votes | Electoral performance was weighted at a', density_bias(NDP))
print(f'Green vote sum of        ', federalGRNSUM, 'votes | Electoral performance was weighted at a', density_bias(GRN))
print(f"People's vote sum of     ", federalPPCSUM, 'votes | Electoral performance was weighted at a', density_bias(PPC))
