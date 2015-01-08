
import sys
import screed
import random
import argparse

N=1000
L=100

def main():
#	parser = argparse.ArgumentParser()
	genomefile = sys.argv[1]

	for record in screed.open(genomefile):
		genome = record.sequence

	for i in range(N):
		start = random.randint(0, len(genome) - 1 - L)
		end = start + L
		read = genome[start:end]

		for j in range(L):
			if random.randint(0, L -1) == 0:
				position = random.randint(0, L - 1)
				newbase = random.choice(["a","c","g","t"])
				read = read[:position] + newbase + \
					read[position+1:]
		
	
		if random.choice([0,1]):
			read = screed.rc(read)
	
		assert len(read) == L #make sure the length of the reads is what I want
		print '>read%d\n%s' %(i, read)


if __name__ == '__main__':
	main()
