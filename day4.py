"""Given a paragraph and a list of banned words, return the most frequent word that 
is not in the list of banned words.  It is guaranteed there is at least one word that 
isn't banned, and that the answer is unique.

Words in the list of banned words are given in lowercase, and free of punctuation.  
Words in the paragraph are not case sensitive.  
The answer is in lowercase.
"""


import re

def mostCommonWord(paragraph, banned):
    """Given a paragraph and a list of banned words, return the most frequent word that 
is not in the list of banned words."""    
    paragraph_items = re.findall(r"[\w']+|[.,!?;]", paragraph)

    dictionary_of_words = {}

    for word in paragraph_items:

        if word in ".,!?;":
            continue
        else:
            word = word.lower()

            if word in banned:
                continue

            if word in dictionary_of_words:
                count = dictionary_of_words[word]
                count += 1
                dictionary_of_words[word] = count
            else:
                dictionary_of_words[word] = 1

    count_max_word = 0
    max_word = None

    for word in dictionary_of_words:

        if count_max_word < dictionary_of_words[word]:
            count_max_word = dictionary_of_words[word]
            max_word = word
            
    return max_word


print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
print(mostCommonWord("FAKE Bob hit a FAKE ball as a event, the hit a fake BALL which was fake and it was hit, fake.", ["hit", "fake"]))
