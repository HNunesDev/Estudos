""""
Generator = Tuple Comprehension
"""

gen = (x * 10 for x in range(1000))
print(list(gen))