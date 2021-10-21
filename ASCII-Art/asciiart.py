# cli-games/asciiart.py
#Called Libraries
import requests
import random

text = input('ASCII Art Text > ')
font = input('ASCII Art Font > ')

data = requests.get('http://artii.herokuapp.com/fonts_list')
fontsArray = data.text.split('\n')

def getAsciiArt(text, font):
    r = requests.get(f'http://artii.herokuapp.com/make?text={text}&font={font}')
    print("Font:", font)
    print(r.text)

#If you type something it will type random 3 fonts
if font == "random":
    for i in range(3):
        font = random.choice(fontsArray)
        getAsciiArt(text, font)

 #If I type the font name, then it will print out
elif font in fontsArray:
    getAsciiArt(text, font)
   

 #If I dont type the font name, it will print random font
elif font == '':
    font = random.choice(fontsArray)
    getAsciiArt(text, font)
   