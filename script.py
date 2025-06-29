import os

path = 'assets'
files = os.listdir(path)


for file in files:
    print("![" + file + "](https://github.com/utoprey/KateAntipushina/tree/master/assets/" + file + ")")
