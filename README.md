# Number Reader

Lil machine learning implementation that recognizes handwritten numbers

## Files
---
* guess.py
  * Main script for recognizing numbers. Draw a number in pic.jpg (i just use paint), save, and run guess.py
  ```
  C:\> python guess.py
  ```
  * if the guess is incorrect, you can improve the data by giving the actual written number and adding this data to the learning model

* loadpic.py
  * this is only helpful if starting from scratch. you can create some basic data for the model to use by drawing a number and runnning this

* data.csv
  * where the data is at! first column is the number, and all the rest are the pixels of the corresponging image

* pic.jpg
  * input for the thingy. it is 50x50 pixels. simply overwrite this file each time you are running the program
