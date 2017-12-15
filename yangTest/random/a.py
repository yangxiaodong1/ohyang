import random
random_int = random.randint(1, 9)
random_uniform = random.uniform(1.0, 9.0)
# print(random_int)

list_test = [1, 2, 3]
str_test = "ajfsfdh"
random_choice_list = random.choice(list_test)
random_choice_str = random.choice(str_test)
# print(random_choice_list)
# print(random_choice_str)

list_test2 = [1, 2, 3, 4, 5]
str_test2 = "ajfsfdh"
tuple_test2 = (1, 2, 3, 4, 5)

test_list = random.sample(list_test2, 2)
test_str = random.sample(str_test2, 2)
test_tuple = random.sample(tuple_test2, 2)
# print(test_list)
# print(test_str)
# print(test_tuple)

test_random = random.random()
# print(test_random)
items = [1, 2, 3, 4, 5, 6]
print(items)
random.shuffle(items)
print(items)