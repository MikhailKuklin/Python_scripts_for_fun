This folder contains simple Python scripts.

1) guess_word.py - simple game where you have to guess the word. Letters in the word is randomly rearranged and player has five attempts.

2) get_neg_index.py - simple function that extracts negative index of an item(s) in the list without limitation on the number of items. Example usage:

waitlist = ["Jane", "Adam", "Alex", "Mike"]

get_index(waitlist, "Jane", "Mike")

Result:

String Jane has -4 index in the list

String Mike has -1 index in the list

(3) uniqie_items.py - function creates a list with unique items only. Example usage:

new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]

print(unique(new_store_order_list))

Result:

['Orange', 'Apple', 'Mango', 'Broccoli']

(4) count_occ.py - function counts number of occurancies of letters and words in a string

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
count_occ(order_list, 'a')

Result:

Number of occurancies of a is 4

Number of occurancies of b is 5
