import pymorphy2
import collections

morph = pymorphy2.MorphAnalyzer()
words = []
morph_list = []
words_unique = set()
words_dic = dict()

with open("text.txt", encoding="utf-8") as f:
    for i in f:
        line = i.replace(",", " ").replace("—", " ").replace(".", " ") \
            .replace("«", " ").replace("-", " ").replace("»", " ") \
            .replace("(", " ").replace(")", " ").replace("!", " ") \
            .replace("?", " ").replace(";", " ").replace(":", " ")
        words += line.split()
print(words)

lower_words = list(map(str.lower, words))
print(lower_words)

for i in lower_words:
    word = morph.parse(i)[0]
    morph_list.append(word.normal_form)
print(morph_list)

c = collections.Counter(lower_words)
for key, value in c.items():
    words_dic[key] = value
print(words_dic)
print(len(set(lower_words)))
print(c.most_common(5))