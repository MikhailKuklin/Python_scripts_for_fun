import random
import urllib2

# take random word from database of English valid words found in GitHub. Change the link to another source if you want
dictionary = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"
source = urllib2.urlopen(dictionary)
txt = source.read()
WORDS = txt.splitlines()

# to simplify the game, take words with 4  letters
def writeshort(WORDS):
    WORDSs = []
    for item in WORDS:
        if len(item) >= 5 or len(item) <= 3:
            continue
        WORDSs += [item] # or wordlist.append(item) as in your first snippet
    return WORDSs
    #word = random.choice(WORDSs)

word = random.choice(writeshort(WORDS))
#print word
correct = word
guess = ""
title = '\033[95m'
guess_word = '\033[32m'
answer = '\033[1;m'
nope = '\x1b[6;30;41m'
right = '\x1b[6;30;43m'
quit = '\033[91m'
end =  '\x1b[0m'

# randomly rearrange letters in the word
while word:
      position = random.randrange(len(word))
      guess += word[position]
      word = word[:position] + word[(position + 1):]

print(
title +
"""
      Guess the word!
      You have 5 attempts!
"""
+ title)
print (guess_word + "The word is: " + guess + end)

# five attempts to guess the word
guesses_left = 5
while guesses_left > 0:
  guess = raw_input(answer + 'Type your answer: ' + end)
  if guess == correct:
    print ('\x1b[6;30;43m' + 'Success!' + end)
    print ('\x1b[6;30;43m' + "Thanks for playing" + end)
    break
  guesses_left -= 1
else:
    print ('\x1b[6;30;43m' + "You lose...Maybe next time!" + '\x1b[0m')

raw_input(quit + 'Press "Enter" to quit' + end)
