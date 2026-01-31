import math

# Dataset (same as your notebook)
data = [
    ['True','Hot','High','No'],
    ['True','Hot','High','No'],
    ['False','Hot','High','Yes'],
    ['False','Cool','Normal','Yes'],
    ['False','Cool','Normal','Yes'],
    ['True','Cool','High','No'],
    ['True','Hot','High','No'],
    ['True','Hot','Normal','Yes'],
    ['False','Cool','Normal','Yes'],
    ['False','Cool','High','Yes']
]

attributes = ['A1', 'A2', 'A3']

# Entropy function
def entropy(data):
    yes = 0
    no = 0
    for row in data:
        if row[-1] == 'Yes':
            yes += 1
        else:
            no += 1

    total = yes + no
    if yes == 0 or no == 0:
        return 0

    return - (yes/total)*math.log2(yes/total) - (no/total)*math.log2(no/total)

# Information Gain
def information_gain(data, attr_index):
    total_entropy = entropy(data)
    values = set(row[attr_index] for row in data)

    weighted_entropy = 0
    for value in values:
        subset = [row for row in data if row[attr_index] == value]
        weighted_entropy += (len(subset)/len(data)) * entropy(subset)

    return total_entropy - weighted_entropy

# Find best attribute
def best_attribute(data):
    gains = {}
    for i in range(len(attributes)):
        gains[attributes[i]] = information_gain(data, i)
    return max(gains, key=gains.get)

# MAIN
print("Entropy of Class:", entropy(data))
print("\nInformation Gain:")
for i in range(len(attributes)):
    print(attributes[i], "=", information_gain(data, i))

print("\nBest Attribute for Root Node:", best_attribute(data))
