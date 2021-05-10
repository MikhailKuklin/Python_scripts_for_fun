def count_occ(mylist, *letters):
  str = list(' '.join(mylist)) # divide into letter
  mylist_let = ' '.join(str).lower() # make a string ignoring capitalization
  count = 0
  for letter in letters:
    for i in mylist_let:
        if i == letter:
          count += 1
    print(f"Number of occurancies of {letter} is {count}")
