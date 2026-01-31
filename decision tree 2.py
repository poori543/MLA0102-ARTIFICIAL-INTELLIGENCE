import math

# Play Tennis Dataset (same as notebook)
data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']

# Entropy calculation
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

# Find Best Attribute
def best_attribute(data):
    gains = {}
    for i in range(len(attributes)):
        gains[attributes[i]] = information_gain(data, i)
    return gains

# MAIN
print("Entropy of PlayTennis:", round(entropy(data), 3))
print("\nInformation Gain for each attribute:")

gains = best_attribute(data)
for attr in gains:
    print(attr, "=", round(gains[attr], 3))

print("\nBest Attribute (Root Node):", max(gains, key=gains.get))
