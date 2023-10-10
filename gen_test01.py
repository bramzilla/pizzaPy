import random

def generate_random_integers(min_value, max_value, num_values):
    random_integers = []
    for _ in range(num_values):
        random_integers.append(random.randint(min_value, max_value))
    return random_integers

if __name__ == "__main__":
    min_value = 1
    max_value = 100
    num_values = 10
    random_integers = generate_random_integers(min_value, max_value, num_values)
    print(random_integers)
