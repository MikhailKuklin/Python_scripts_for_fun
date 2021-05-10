def get_index(mylist, *names):
  for name in names:
    for i in mylist:
      if i == name:
        neg_ind = ~mylist[::-1].index(i)
        print(f"String {name} has {neg_ind} index in the list")
