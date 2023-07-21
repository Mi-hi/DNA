#DNAToolkit file
import collections
Nucleotides = ['A', 'C', 'G', 'T']


def validate_seq(dna_seq):
    Nucleotides = ['A', 'C', 'G', 'T']
    for char in dna_seq:
        if char.upper() not in Nucleotides:
            return False
    return dna_seq

def countNucFreq(seq):
    #tmpFreqDict = {"A" : 0, "C" : 0, "G" : 0 , "T" : 0 }
    #for nuc in seq :
    #    tmpFreqDict[nuc] += 1
    #return tmpFreqDict
    return dict(collections.Counter(seq))
