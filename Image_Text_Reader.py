#..........................................................................................................................
# Dependencies and Libraries 
import easyocr
import os
from textblob import Word
#..........................................................................................................................
#Creating a list of image paths by joining folder to individual file name ....
raw_image_path = 'Enter root folder where all your images lie'
data_folder = os.listdir(raw_image_path)
individual_image_path = []

for i in data_folder:
    individual_image_path.append(os.path.join(raw_image_path,i))

#..........................................................................................................................
#Reader to read text from images ....
reader = easyocr.Reader(['en'])
final_data = []

for i in individual_image_path:
    text = reader.readtext(i,detail=0)
    final_data.append(text)

#...........................................................................................................................
#Replace tne faulty spellings with the correct ones using textblob module ....
i = 0
while i < len(final_data):
    j = 0
    while j < len(final_data[i]):
        data = final_data[i][j]
        word = Word(data)
        output = word.correct()
        final_data[i][j] = output
        j+=1
    i+=1
#...........................................................................................................................

print(final_data) #output

#...........................................................................................................................