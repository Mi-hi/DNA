from DNAToolkit import *
import random


def generate_random_dna(length):
    nucleotides = ['A', 'C', 'G', 'T']
    dna_sequence = ''.join(random.choice(nucleotides) for _ in range(length))
    return dna_sequence


# Generate a random DNA sequence of
# length 10
random_dna = generate_random_dna(50)

print(random_dna)
print(countNucFreq(random_dna))



