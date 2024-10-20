# print("Chai aur Python")

# def chai(n):
#     print(n)

# chai("Lemon Tea")

# chai_one = "Lemon Tea"
# chai_two = "Ginger Tea"
# chai_three = "Masala Chai"


# chai_types = {"Masala": "Spicy",  "Ginger": "Zesty", "Lemon": "Sour", "Green": "Mild"}
# print(chai_types)

# for chai_type, description in chai_types.items():
#     print(f"{chai_type} chai tests like {description}") # Output:  Masala chai tests like Spicy


# if "Masala" in chai_types:
#     print("Masala chai is available") # Output: Masala chai is available
# print(chai_types)
# chai_types["Earl Grey"] =  "Bergamot"
# print(chai_types)
# chai_types.pop("Earl Grey")
# print(chai_types)

# tea_shop = {
#     "chai": {
#         "Masala": "Spicy",
#         "Ginger": "Zesty"
#     },
#     "tea": {
#         "Green": "Mild",
#         "Earl Grey": "Bergamot",
#         "Black Tea":  "Strong"
#     }
# }

# print(f"{tea_shop["chai"]} and {tea_shop["tea"]}")

squared_num = {x: x **2 for x in range(10)}
print(squared_num) # Output: {0: 0, 1: 1, 2: 4,  3: 9, 4: 16, 5: 25}

keys = ["Masala", "Ginger", "Lemon", "Green"]
default_value = "Delicious"

new_dict = dict.fromkeys(keys, default_value)
print(new_dict)

