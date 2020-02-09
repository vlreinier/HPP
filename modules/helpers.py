import random

def generate_random_int_list(r):
    return [random.randint(1, r) for i in range(r)]

def generate_random_float_list(r):
    return [random.uniform(0, r) for i in range(r)]