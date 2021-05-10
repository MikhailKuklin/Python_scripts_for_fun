def unique(mylist):
  uniq_list = []
  for name in mylist:
    if name in uniq_list:
      continue
    else:
      uniq_list.append(name)
  return uniq_list
