filename = "theguardian.txt"

with open(filename, encoding="utf-8") as file_object:
    lines = file_object.readlines() # create a list of lines.
    # Since I cannot use maketrans on list I will convert the list in a string.

contents = " ".join(lines)

mydict = contents.maketrans("", "", "./\£%&\"")
clean_message = contents.translate(mydict)

wordlist_raw = clean_message.lower().split()

# proper wordlist with no numbers or .,!$
wordlist= []
for word in wordlist_raw:
    if word.isalpha() == True:
        wordlist.append(word)
    else:
        continue
# make a dictionary to remove dupes. Don't use set because the order is not fixed
thedict = dict.fromkeys(wordlist)
#transform the dict in a list
no_dupe_list = list(thedict)
wordfreq = [wordlist.count(word) for word in no_dupe_list]

pairs = list(zip(no_dupe_list, wordfreq))
pairs.sort(key = lambda x: x[1], reverse=True)

for pair in pairs:
    print(pair)
