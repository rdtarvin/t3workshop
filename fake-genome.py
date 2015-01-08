import random
dna = ["A","C","T","G"]
dna=dna*250
random.shuffle(dna)
print '>genome'
print "".join(dna)
