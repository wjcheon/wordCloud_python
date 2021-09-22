##
# conda env: naver_kin_crawling
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
        #if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
        print(text)
        if re.match("과연|설마|제발|정말|결코|모름지기|응당|어찌|아마|정녕|아무쪼록|하물며|그리고|그러나|그러므로|즉|곧|및|혹은|또는", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict


def makeImage(text):

    font_path = r"D2CodingBold-Ver1.3.2-20180524-ligature.ttf"
    mask_path = r"단어모음 (jpg)/단어 (png)/소아청소년과_1024.jpg"  # width 와 height가 일정 크기 이상이어야 글자가 많이 들어감
    mask = np.array(Image.open(mask_path))  # powerpoint -> export as jpg format

    wc = WordCloud(font_path=font_path, background_color="white", max_words=20000, mask=mask, min_font_size=2,
                   max_font_size=300, random_state=42)

    wc.generate_from_frequencies(text)
    wc.recolor(color_func=color_func, random_state=3)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    print('working: MakeImage')


def makeImageFromText(text):

    font_path = r"D2CodingBold-Ver1.3.2-20180524-ligature.ttf"
    mask_path = r"단어모음 (jpg)/단어 (png)/소아청소년과.jpg"
    mask = np.array(Image.open(mask_path))  # powerpoint -> export as jpg format


    wc = WordCloud(font_path=font_path, background_color="white", max_words=20000, mask=mask, min_font_size=2, max_font_size=300, random_state=42)
    wc.generate_from_text(text)
    wc.recolor(color_func=color_func, random_state=3)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    print('working: MakeImage')


# TEXT
#f = open(r"poem_YDJ.txt",  'rt', encoding='UTF8')
f = open(r"질문txt/소아청소년과.txt",  'rt', encoding='UTF8')
text = f.read()
print(text)
f.close()

# Frequency mode
word_dict_frequency = getFrequencyDictForText(text)
makeImage(word_dict_frequency)

# text mode
#makeImageFromText(text)
