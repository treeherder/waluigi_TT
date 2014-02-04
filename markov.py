# mostly taken from  Kernighan and Pike 'The Practice of Programming'

import random

stop = "\n" #EoL marker is the limit
sen_lim = (".", "!", "?",) # figure out punctuation errors
sen_sep  = "\n" #output limit


# Gcreate lookups
first_stop = stop
second_stop = stop
table = {}


for line in src_txt:
    for word in line.split():
        if word[-1] in sen_lim:
            table.setdefault( (first_stop, second_stop), [] ).append(word[0:-1])
            first_stop, second_stop = second_stop, word[0:-1]
            word = word[-1]
        table.setdefault( (first_stop, second_stop), [] ).append(word)
        first_stop, second_stop = second_stop, word
# indicate EoP
table.setdefault( (first_stop, second_stop), [] ).append(stop)

#sentence structure
max_groups  = 5

first_stop = stop
second_stop = stop
sen_count = 0
sentence = []


while sen_count < max_groups:
    new_word = random.choice(table[(first_stop, second_stop)])
    if new_word == stop: sys.exit()
    if new_word in sen_lim:
        print "%s%s%s" % (" ".join(sentence), new_word, sen_sep)
        sentence = []
        sen_count += 1
    else:
        sentence.append(new_word)
    first_stop, second_stop = second_stop, new_word
