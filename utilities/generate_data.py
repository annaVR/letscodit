__author__ = 'anna'

import random

def generate_invalid_credit_card():

    data = random.sample(range(100), 3)
    print(data)

generate_invalid_credit_card()