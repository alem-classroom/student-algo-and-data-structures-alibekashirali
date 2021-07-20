def linear_search(lst, to_find):
  # search for the element to_find inside lst
  # if found, return index of element
  # else return -1
  for i in range(0, len(lst)-1):
    if lst[i] == to_find:
      return i
    else:
      return -1
  
