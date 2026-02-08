# #Dictionary Operations & methods 
# state_food = {
#     "Bengaluru": "Bisi bele bath",
#     "Mysore":"Mysore pak",
#     "Mangaluru":"Mangalur buns",
#     "Udupi":"Neer Dose",
#     "Dharwad":"Peda"
# }
# #Adding new item
# print(state_food)
# state_food["Davangere"] = "Benne Dose"
# print("After adding new element: ", state_food)

# #Updating the item
# state_food["Bengaluru"] = "Masala Dose"
# print("After updating: ", state_food)

# #Removing item
# dharwad_food = state_food.pop("Dharwad") #using pop
# print(dharwad_food)

# del state_food["Mangaluru"] #using del
# print(state_food)

# state_food.clear() #using clear to empty the dictionary
# print(state_food)


friends = {
    "friend1" : {
        "name" : "keer",
        "fav_subject" : "Maths",
        "fav_food" : "Masala Dose"
    },
    "friend2" : {
        "name" : "Monisha",
        "fav_subject" : "Social",
        "fav_food" : "Biryani"
    }
}

print("favorite food of", friends ["friend1"] ["name"] ,"is", friends ["friend1"] ["fav_food"] )

print("Favorite subject of" , friends ["friend2"] ["name"], "is", friends ["friend2"] ["fav_subject"])
