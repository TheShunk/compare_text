# compare_text
compare two texts and determine their similarity between 0 and 1 based on character match. No NLP present.

value is determined by the total number of matches between the two texts and the total number of characters between the texts. 

example:

    text1 = 'abc'
    text2 = 'nmc'

    only the 'c' matches between the two, but 33% of each text matches so we expect a value of .33

-----------------------------------------

usage: python compare_text arg1 arg2

arg1 is path to text1 
arg2 is path to text2

assumption: texts are simple .txt files

-----------------------------------------

references

https://blog.jcoglan.com/2017/02/12/the-myers-diff-algorithm-part-1/
https://medium.com/@adriensieg/text-similarities-da019229c894
http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6048/pdf/imm6048.pdf
https://sites.temple.edu/tudsc/2017/03/30/measuring-similarity-between-texts-in-python/
https://paulbutler.org/2007/a-simple-diff-algorithm-in-php/