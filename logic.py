import random

class Party:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.votes = 0

# Console text
print("\bModel of Canadian 2019 General Election:\n")
# Establishing variables

LP= Party("Liberal Party of Canada", 4)
CP = Party("Conservative Party of Canada", 3)
NDP = Party("New Democratic Party of Canada", 2)
GRN = Party("Green Party of Canada", 1)
PPC = Party("People's Party of Canada", 1)
X = Party("Refused Ballots", 1)

partyList = [LP, CP, NDP, GRN, PPC, X]


class Citizen:
    def __init__(self):
        self.preference = random.choices(partyList, weights=[LP.weight, CP.weight, NDP.weight, GRN.weight, PPC.weight, X.weight])

# Population who may vote
population = 30

def popularity_handler(x):
    return "{:.0%}".format(x/population)


#def decimalize(x):
    #return x / population

# Recording citizen classes choice and then counting it

voteList = []
for i in range(0, population):
    voteList.append(Citizen())
for i in range(0, population):
    voteList[i].preference[0].votes += 1

# Printing results + percentages and totals

for i in range(0, len(partyList)):
    print(f"{partyList[i].name}, {popularity_handler(partyList[i].votes)} | {partyList[i].votes} votes cast")
# print("Total Votes:", total, "|", popularity_handler(total/population) + " Turnout")

total = LP.votes + CP.votes + NDP.votes + GRN.votes + PPC.votes

print(f"Total Votes Cast: {total}")


# print("Liberal Party of Canada:", LIBERAL_PARTY, "votes,", str(popularity_handler(decimalize(LIBERAL_PARTY))))
# print("Conservative Party of Canada:", CONSERVATIVE_PARTY, "votes,", str(popularity_handler(decimalize(CONSERVATIVE_PARTY))))
# print("New Democratic Party of Canada:", NDP_PARTY, "votes,", str(popularity_handler(decimalize(NDP_PARTY))))
# total = LIBERAL_PARTY + CONSERVATIVE_PARTY + NDP_PARTY
# print("Total Votes:", total, "|", popularity_handler(total/population) + " Turnout")
