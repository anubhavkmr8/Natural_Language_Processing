import re
import sys
import random
from math import log

# Function to compute the base-2 logarithm of a floating point number.
def log2(number):
    return log(number) / log(2)


# Function to normalise the text.
cleaner = re.compile('[^a-z]+')


def clean(text):
    return cleaner.sub(' ', text)


# Dictionary for letter counts
letter_frequency = {}

# Read and normalise input text
text = ''
for i in range(0, 1000):
    text = text + random.choice('abcdefghijklmnopqrstuvwxyz')

# Count letter frequencies
for letter in text:
    if letter in letter_frequency:
        letter_frequency[letter] += 1
    else:
        letter_frequency[letter] = 1

# Calculate entropy
length_sum = 0.0
for letter in letter_frequency:
    probability = float(letter_frequency[letter]) / len(text)
    length_sum += probability * log2(probability)

# Output
sys.stdout.write('Entropy: %f bits per character\n' % (-length_sum))
