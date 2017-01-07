import sys
import string

def word_count():
  word_counts ={} #intialize the empty dictionary

  for line in sys.stdin:
     data = line.strip.split(" ")
     for i in data :
         key = i.translate(string.maketrans("","",string.punctuation).lower()
          if key in word_counts.key()
            word_counts[key] += 1
          else
          word_counts[key] =1

          print word_counts
