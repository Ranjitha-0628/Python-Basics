#List Manipulation Exercise

bag = ["books", "pen", "bottle", "id", "pods"]
print("Initial list: " , bag)
bag.append("box")
bag.insert(1, "laptop")
print("After adding: " , bag)

bag.remove("pen")
print("After removing: ", bag)

#Reverse and Sort

numbers = [23, 56, 8, 11, 76, 90]
numbers.sort(reverse=True) #No direct method to covert into descending so we use reverse = true
print("After sort: " , numbers)
numbers.reverse()
print("After reverse: " , numbers)