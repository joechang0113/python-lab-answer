import re

text = "昔汝雖拒吾於千里之外，傷吾心，然吾怪之罪何有於汝乎？\
反，吾思與日俱增，吾情與時俱進。於汝，情痴㇐片，思濃于海，\
山不可動，海不可淹，火不可滅。愛慕之情，時時加之，\
豈有他人可吾及乎？"

punctuation = '!,;:?，。"\''  # filter symbol what u need


def removePunctuation(text):

    text = re.sub(r'[{}]+'.format(punctuation), '', text)
    return text.strip().lower()  # filter and return


text = tuple(removePunctuation(text))  # storage tuple and forward to text
mode = 0
for i in text:
    if(text.count(i) > text.count(text[mode])):
        mode = text.index(i)
print("\nmode: {0} for {1} times".format(text[mode], text.count(text[mode])))
