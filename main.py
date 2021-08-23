##
import numpy as np
import random
import re
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
from palettable.colorbrewer.qualitative import Dark2_8
import matplotlib.pyplot as plt
import multidict as multidict

def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Dark2_8.colors[random.randint(0,7)])

def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict


def makeImage(text):

    font_path = r"D2CodingBold-Ver1.3.2-20180524-ligature.ttf"
    mask_path = r"diabetes.jpg"
    mask = np.array(Image.open(mask_path))  # powerpoint -> export as jpg format

    wc = WordCloud(font_path=font_path, background_color="white", max_words=1000, mask=mask)
    wc.generate_from_frequencies(text)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    print('working: MakeImage')


# TEXT
#f = open(r"poem_YDJ.txt",  'rt', encoding='UTF8')
f = open(r"diabetes.txt",  'rt', encoding='UTF8')
text = f.read()
print(text)
f.close()

word_dict_frequency = getFrequencyDictForText(text)
makeImage(word_dict_frequency)
