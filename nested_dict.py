# Nested Dictionary Practice - Friend Details

# Create a nested dictionary with details of two friends
friends = {
    "Friend1": {
        "name": "Alice",
        "favorite_subject": "Mathematics",
        "favorite_food": "Pizza"
    },
    "Friend2": {
        "name": "Bob",
        "favorite_subject": "Physics",
        "favorite_food": "Biryani"
    }
}

# Access and print the favorite food of Friend1
print("Favorite food of", friends["Friend1"]["name"], "is:", friends["Friend1"]["favorite_food"])

# You can also access Friend2's favorite food
print("Favorite food of", friends["Friend2"]["name"], "is:", friends["Friend2"]["favorite_food"])
