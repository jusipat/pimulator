import random

class Party:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.votes = 0

# Establishing variables
LIBERAL_PARTY = Party("Liberal", 3)
CONSERVATIVE_PARTY = Party("Conservative", 2)
NDP_PARTY = Party("NDP", 1)

partyList = [LIBERAL_PARTY, CONSERVATIVE_PARTY, NDP_PARTY]

class Citizen:
    def __init__(self):
        self.preference = random.choices(partyList, weights=[LIBERAL_PARTY.weight, CONSERVATIVE_PARTY.weight, NDP_PARTY.weight])

# Population who may vote
population = 100

def popularity_handler(x):
    x = "{:.0%}".format(x)
    return x


def decimalize(x):
    return x / population

# Recording citizen classes choice and then counting it

voteList = []
for i in range(0, population):
    voteList.append(Citizen())
for i in range(0, population):
    voteList[i].preference[0].votes += 1

# Debug

# print(voteList)
# print(LIBERAL_PARTY, CONSERVATIVE_PARTY, NDP_PARTY)

for i in range(0, len(partyList)):
    print(partyList[i].name, partyList[i].votes)


# Printing results + percentages and totals
# print("Liberal Party of Canada:", LIBERAL_PARTY, "votes,", str(popularity_handler(decimalize(LIBERAL_PARTY))))
# print("Conservative Party of Canada:", CONSERVATIVE_PARTY, "votes,", str(popularity_handler(decimalize(CONSERVATIVE_PARTY))))
# print("New Democratic Party of Canada:", NDP_PARTY, "votes,", str(popularity_handler(decimalize(NDP_PARTY))))
# total = LIBERAL_PARTY + CONSERVATIVE_PARTY + NDP_PARTY
# print("Total Votes:", total, "|", popularity_handler(total/population) + " Turnout")
