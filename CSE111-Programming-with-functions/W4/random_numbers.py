import random

def append_random_words(words_list, quantity=1):
    possible_words = ["melon", "pear", "peach", "plum", "kiwi"]

    words = random.sample(possible_words, quantity)
    #words_list.append(words)

    for word in words:
       words_list.append(word)

def append_random_numbers(numbers_list, quantity=1):
    for i in range(quantity):
        random_number = random.uniform(0, 100)
        random_number_rounded = round(random_number, 1)
        numbers_list.append(random_number_rounded)

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)
    print(numbers)

    words = ["apple", "banana", "cherry", "orange", "grape"]
    print(words)
    append_random_words(words)
    print(words)
    append_random_words(words, 3)
    print(words)

if __name__ == "__main__":
    main()
