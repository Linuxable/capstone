import numpy as np
import matplotlib.pyplot as plt
import os

# Classes can be found in the README file of OT&Sien Dataset
classes = ['acorn', 'axe', 'backpack', 'badger', 'bag', 'barrel', 'basket', 'bear', 'bed', 'bee', 'bell', 'bench', 'bird', 'birdcage', 'boar', 'boat', 'book', 'bottle', 'bow', 'bowl', 'box', 'bridge', 'broom', 'brush', 'bucket', 'building', 'butterfly', 'camel', 'campfire', 'candle', 'cane', 'cannon', 'car', 'cat', 'cello', 'chair', 'clock', 'couch', 'cow', 'cradle', 'crown', 'cup', 'curtain', 'deer', 'diningTable', 'dog', 'doghouse', 'donkey', 'door', 'dragon', 'drum', 'egg', 'elephant', 'ermine', 'feather', 'female', 'fence', 'fireplace', 'fish', 'fishingRod', 'flag', 'flower', 'flute', 'fox', 'frog', 'glasses', 'globe', 'goat', 'gun', 'hammer', 'hat', 'hedgehog', 'helmet', 'horse', 'hotAirBalloon', 'inkpot', 'insect', 'jackal', 'jar', 'jug', 'kettle', 'kite', 'knife', 'ladder', 'lamp', 'lifebuoy', 'lion', 'lizard', 'lobster', 'male', 'map', 'marmot', 'melon', 'monkey', 'moon', 'musicSheet', 'nest', 'net', 'painting', 'paintingStand', 'pan', 'pear', 'pen', 'penguin', 'piano', 'pickaxe', 'pig', 'pineapple', 'pipe', 'plant', 'plate', 'pot', 'pottedPlant', 'rabbit', 'rake', 'rat', 'rhino', 'sausage', 'saw', 'scale', 'scissors', 'scorpion', 'seal', 'shark', 'sheep', 'shield', 'shovel', 'sieve', 'skate', 'snail', 'snake', 'spear', 'spoon', 'sportsBall', 'squirrel', 'star', 'stool', 'stroller', 'suitcase', 'sun', 'sunflower', 'sword', 'teachingBoard', 'teapot', 'tent', 'tie', 'tiger', 'train', 'tree', 'trumpet', 'tub', 'turtle', 'umbrella', 'vase', 'violin', 'wagon', 'walnut', 'weight', 'whip', 'windmill', 'window', 'wineGlass', 'wolf', 'zebra']

# Change the 'train' into 'test' or 'valid' to check for the other datasets
# This assumes that you have a folder in the same directory with the same "Ot&Sien++" containing the dataset
dataset = 'train'
directory = os.fsencode("./Ot&Sien++/1.0_Children_Books/1.0_Children_Books/" + dataset + "/labels")
files = os.listdir(directory)
print("Amount of images in " + dataset + " dataset: ", len(files))

used_classes = []
for filename in files:
    with open(os.path.join(directory, filename)) as f:
        split1 = f.read().split('\n')
        for s in split1:
            used_classes.append(int(s.split()[0]))

# Create a dictionary with the frequency of each object class
amount_per_class = dict()
for i in range(len(classes)):
    amount_per_class[classes[i]] = used_classes.count(i)

# Print list of object classes that do not occur
not_occuring = []
for k in amount_per_class.keys():
    if amount_per_class[k] == 0:
        not_occuring.append(k)
print("Objects that do not occur: ", not_occuring)


# Sort(large to small) the dictionary based on the frequency in the training data
sorted_dict = dict(reversed(sorted(amount_per_class.items(), key=lambda item: item[1])))
print("Frequency per object: ", sorted_dict)

# Bar plot for 20 most frequent objects
x, y = [], []
for i in range(20):
    key = list(sorted_dict.keys())[i]
    x.append(sorted_dict[key])
    y.append(key)
fig, ax = plt.subplots()
bars = ax.barh(y, x)
ax.bar_label(bars)
plt.xlim([0,2000])
plt.title("Most frequent objects")
plt.show()

