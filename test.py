"""
from english_words import get_english_words_set

web2lowerset = list(get_english_words_set(['web2'], alpha=True,lower=True))

print(len(web2lowerset))
"""

spam = [50, 100, 200]
cheese = spam
cheese[0] = 0
print(spam)
