def count_letters(mylist, *letters):
  str = list(' '.join(mylist)) # divide into letter
  mylist_let = ' '.join(str).lower() # make a string ignoring capitalization
  count = 0
  for letter in letters:
    for i in mylist_let:
        if i == letter:
          count += 1
    print(f"Number of occurancies of {letter} is {count}")
    
 def count_words(mylist, *words):
  str = ' '.join(mylist).lower().split() # make a string ignoring capitalization
  count = 0
  for word in words:
    for i in str:
        if i == word:
          count += 1
    print(f"Number of occurancies of {word} is {count}")
