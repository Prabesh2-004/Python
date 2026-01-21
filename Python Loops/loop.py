# score = [100, 200, 300, 101, 202, 303, 607, 506, 980, 56]

# max_score = 0
# for scores in score:
#     if scores > max_score:
#         max_score = scores
# print(max_score)

# range function

# for number in range(1, 100):
#     print(number)

# print(int(10)/5)
numbers = 0
for number in range(1, 101):
    if number%3 == 0 and number%5 == 0:
        print("fizzbuzz")
    elif number%3 == 0:
        print("fizz")
    elif number%5 == 0:
        print("buzz")
    else:
        print(number)
