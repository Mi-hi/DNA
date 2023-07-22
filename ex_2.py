rna_string = ['A', 'C', 'G', 'U']
dna_string = ['A', 'C', 'G', 'T']


def transcription(string):
    rna_string = ['A', 'C', 'G', 'U']
    dna_string = ['A', 'C', 'G', 'T']
    trans = []
    for char in string:
        if char in dna_string:
            if char == 'T':
                trans.append('U')
            else:
                trans.append(char)
        else:
            raise ValueError(f" Invalid '{char}' not in the DNA string")
    return ' '.join(trans)


string_1 = "GATCGATCGA"
print(transcription(string_1))
