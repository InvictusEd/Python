# 随机选择饮品

import random
menu = ["milk", "water", "cola", "tea", "coffee"]
print("Menu:", menu)
name = input("Please enter your name:")
drink = random.choice(menu)
print("Hello", name + "!" + " Please enjoy your", drink)
