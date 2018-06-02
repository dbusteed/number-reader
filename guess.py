#
#  Edit pic.jpg (draw a number), then run this
#  to see what the computer recognizes
#

from sklearn import tree
from PIL import Image
import csv

data = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for r in reader:
        data.append(r)

labels, values = [], []

for row in data:
    labels.append(row[0])
    values.append(row[1:])

clf = tree.DecisionTreeClassifier()

clf = clf.fit(values, labels)

im = Image.open('pic.jpg')

pix = im.load()

pixels = []

for x in range(im.size[0]):
    for y in range(im.size[1]):
        for p in pix[x,y]:
            pixels.append(p)

pred = clf.predict([pixels])

pred = int(tuple(pred)[0])

print("\nIs it a {} ?".format(pred))
fb = input('[y/n]: ')

if fb.lower() == 'y':
    print('\nAwesome!')
    guess = True
else:
    print('\nOops!')
    guess = False
    actual = int(input('What is the actual number?: '))

print('\nDo you want to add these results to improve future predictions?')
choice = input('[y/n]: ')

if choice.lower() == 'y':
    print('\nThanks!')

    if guess:
        pixels.insert(0, pred)
    else:
        pixels.insert(0, actual)

    data_string = [pixels]

    with open('data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_string)
else:
    print('\nOkay.')
