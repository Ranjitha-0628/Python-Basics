#Tuple Operations

house = ("hall", "kitchen", "bathroom")
print(house)
print(house[1])
print(house[1:3])

tree = ("leaves", "branch", "flowers")
print(tree)
combine_tree_house = tree + house
print(combine_tree_house)

#Set operations
ranj = {"watermelon", "banana", "grapes", "peach"}
keer = {"apple", "cherry", "peach", "orange"}

union = ranj | keer
intersect = ranj & keer
difference = ranj ^ keer
print(union)
print(intersect)
print(difference)

ranj.add("avacado")
print(ranj)
ranj.remove("grapes")
ranj.discard("cherry")

#list into tuples and sets

shop = ("chips", "chocolates", "drinks")
s = tuple(shop)
print(type(s))
p = set(shop)
print(type(p))

# s.append("cake") # tuples has no add operations (immutable = unchangeable)
p.add("cake")
print(p)

#Reverse a String (Two pointers)

def reverse_string(s):   
    chars = list(s)
    left,right = 0, len(chars) -1

    while left<right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right += 1
        return "".join(chars)
    
print(reverse_string("Haaai"))
