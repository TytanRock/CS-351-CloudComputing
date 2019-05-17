# From http://mrjob.readthedocs.org/en/latest/guides/quickstart.html#writing-your-first-job

from mrjob.job import MRJob
from mrjob.step import MRStep
from itertools import tee
import re
import sys

WORD_RE = re.compile(r"[\w']+")

# Legacy class to remember how jobs work
class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        yield "chars", len(line)
        yield "words", len(line.split())
        yield "lines", 1

    def reducer(self, key, values):
        yield key, sum(values)

# New class for MRJob Word Probability
class MRWordProbability(MRJob):
    
    # All the steps taken to produce probabilities and most common occurences
    def steps(self):
        return [
            # Pull strings out of the csv
            MRStep(mapper=self.mapper_pull_csv),
            # Produce bigrams from the string
            MRStep(mapper=self.mapper_get_bigrams,
                   combiner=self.combiner_count_bigrams,
                   reducer=self.reducer_count_bigrams),
            # Calculate percents and most common occurences
            MRStep(reducer=self.reducer_calculate_percents)
        ]
    
    # Just get the string from the csv
    def mapper_pull_csv(self, _, line):
        if(line[0] != '"'):
            yield (None, line[line.find(","):].lower())
    
    # Pull words from the string and make a bigram for every instance of each word following each other
    def mapper_get_bigrams(self, _, line):
        prevWord = ""
        # Use regex to find words
        for word in WORD_RE.findall(line):
            if(prevWord != ""):
                yield ((prevWord, word), 1)
            prevWord = word
    
    # Combine all like bigrams
    def combiner_count_bigrams(self, word, counts):
        yield (word, sum(counts))
    
    # Combine all like bigrams
    def reducer_count_bigrams(self, word, counts):
        first_word, second_word = word
        yield first_word, (sum(counts), second_word)
        
    # Function used to sort based on probability
    def mostUsed(self, x):
        num, word = x
        return num
    
    # Calculate percentage of each word showing up
    def reducer_calculate_percents(self, word, pairs):
        
        total = 0
        
        # Tee off the iterator so we can have 3 total runs through the data
        pairs, secondPairs = tee(pairs)
        pairs, sortedPairs = tee(pairs)
        
        # First calculate the total number of occurences of each bigram
        for pair in pairs:
            tmpCnt, _ = pair
            
            total = total + tmpCnt
        
        # Then print out all the rest of the words based on most common occurence
        probabilityList = sorted(secondPairs, key=self.mostUsed, reverse = True)
        for anotherPair in probabilityList:
            word_count, word_key = anotherPair
            
            yield (word, word_key), ((float(word_count) / total), word_count)
        
        # If the first word is "my", print the most used pairs
        if (word == "my"):
            for i in range(10):
                if i == len(probabilityList): 
                    break
                word_count, word_key = probabilityList[i]
                yield 'Most used number ' + str(i+1), ((word, word_key), word_count / total, word_count)
        
        

# Run the program
if __name__ == '__main__':
    MRWordProbability.run()
