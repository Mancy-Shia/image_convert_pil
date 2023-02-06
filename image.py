from PIL import Image
import os


for file in os.listdir('orig'):
    if file.endswith('.jfif'):
        img = Image.open('orig/' + file)
        img = img.convert('L') # convert to L (Grayscale)
        img.save(os.path.join('conv', file[:-5] + '_grey.jpg')) 
