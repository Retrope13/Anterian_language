import sys
from PIL import Image

imageVector = []
WordtoCode = ""

def findIMGV(phrase):
    phrase = phrase.upper()
    i=0
    im = ""
    letterChosen = False
    while i<len(phrase):
        if i < len(phrase)-2:
            if phrase[i] == "I" and phrase[i+1] == "N" and phrase[i+2] == "G":
                im = Image.open(str(phrase[i]+phrase[i+1]+phrase[i+2]+".png"))
                i+=3
                letterChosen = True
        if i < len(phrase)-1 and letterChosen==False:
            if phrase[i] == "C" and phrase[i+1] == "H":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "P" and phrase[i+1] == "H":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "S" and phrase[i+1] == "H":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "T" and phrase[i+1] == "H":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "E" and phrase[i+1] == "E":
                im = Image.open("EE.png")
                i+=2
                letterChosen = True
            elif phrase[i] == "O" and phrase[i+1] == "O":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "C" and phrase[i+1] == "R":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "P" and phrase[i+1] == "R":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "S" and phrase[i+1] == "R":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "T" and phrase[i+1] == "R":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "B" and phrase[i+1] == "R":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "D" and phrase[i+1] == "R":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "F" and phrase[i+1] == "R":
                im = Image.open(str(phrase[i] + phrase[i+1])+".png")
                i+=2
                letterChosen = True
            elif phrase[i] == "G" and phrase[i+1] == "R":
                im = Image.open(str(phrase[i]) + str(phrase[i+1])+".png")
                i+=2
                letterChosen = True
        if i < len(phrase) and letterChosen==False:
            if phrase[i] == " ":
                im = Image.open("space.png")
                i+=1
            elif phrase[i] ==".":
                im = Image.open("period.png")
                i+=1
            else:
                im = Image.open(str(phrase[i]) + ".png")
                i+=1
        imageVector.append(im)
        letterChosen=False
    print(imageVector)
    im = get_concat_h_multi_blank(imageVector).save('Coded_message.png')
    
def get_concat_h_blank(im1, im2, color=(1000, 1000, 1000)):
    dst = Image.new('RGB', (im1.width+im2.width+15, max(im1.height, im2.height)), color)
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0)) ##if you modify the height of the box parameter you can get partial messages like the sign has been cut in half
    return dst

def get_concat_h_multi_blank(im_list):
    _im = im_list.pop(0)
    for im in im_list:
        _im = get_concat_h_blank(_im, im)
    return _im

 
try:
    WordtoCode = sys.argv[1]
    findIMGV(WordtoCode)
except OSError:
    pass