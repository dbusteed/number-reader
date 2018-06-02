# 
# Used for loading initial data (if needed)
#

from PIL import Image
import csv

im = Image.open('pic.jpg')
num = int(input('\nActual number?: '))

pix = im.load()

data_string = [num]

for x in range(im.size[0]):
    for y in range(im.size[1]):
        for p in pix[x,y]:
            data_string.append(p)

big_data = [data_string]

with open('data.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(big_data)
