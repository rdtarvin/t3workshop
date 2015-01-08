#when I want to build these files, run this command

#targets of makefile
all: genome.fa reads.fa

#force rebuild everything, use rm -f to say don't complain if it doesn't exist or -rm to force ignore errors 
clean:
	-rm genome.fa

#depends on fake-genome.py, so if genome.fa is older than fake-genome, it will remake genome.fa
genome.fa: fake-genome.py
	python fake-genome.py > genome.fa

#dependent on genome.fa and make-reads.py
reads.fa: genome.fa fake-genome.py
	python make-reads.py genome.fa > reads.fa
