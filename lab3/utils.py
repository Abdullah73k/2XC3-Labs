import random

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]