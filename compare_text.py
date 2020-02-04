#current limitations
#case sensitive. while this is not necessarily bad, T and t are only slightly different.
#these could be considered only half different or something arbitrary to capture the smiilarity. 

#TO DO
#modify case sensitivity
#pass dynamic values: DONE
#allow for switching between word and letter

import sys
try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except:
    print("must provide the path of two files as arguments")
    quit()
#print ('list: ' + str(sys.argv))


def compare(t1,t2):
    t1_map = dict()
    #set up a dict of each value and it's corresponding coordinates. so the string 
    #'hello' would return something like h:0 e:1 l:2,3 o:4
    for i, val in enumerate(t1):
        #print('i: ' + str(i))
        #print('val: ' + str(val))
        t1_map.setdefault(val,list()).append(i)

    match = dict()
    #index of start of largest overlap in on t1
    sub_st_t1 = 0
    #index of beginning of same substring in t2 list
    sub_st_t2 = 0
    #length of overlap
    length = 0

    #it2 is the index of each letter and val is the value
    for it2, val in enumerate(t2):
        #t2match used for ht1ing 
        t2match = dict()
        for it1 in t1_map.get(val,list()):
            #t2match at index of it1 is set to match + 1 only if it1 and match.get are non 0
            t2match[it1] = (it1 and match.get(it1 - 1, 0)) + 1
            #set values of length and match starts
            if(t2match[it1] > length):
                length = t2match[it1]
                sub_st_t1 = it1 - length + 1
                sub_st_t2 = it2 - length + 1
        match = t2match


    if length == 0:
        #no common substring returns insert and delete
        return (t1 and [('-', t1)] or []) + (t2 and [('+', t2)] or [])
    else:
        #recursively compare the text before and after the common substring
        #will produce complete list of all matches inserts and deletes
        return compare(t1[ : sub_st_t1], t2[ : sub_st_t2]) + \
                [('=', t2[sub_st_t2 : sub_st_t2 + length])] + \
                compare(t1[sub_st_t1 + length : ],
                        t2[sub_st_t2 + length : ])
        
#text1="""The easiest way to earn points with Fetch Rewards is to just shop for the best products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."""
#text2="""The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."""

#text1 = "abc"
#text2 = "vnc"

#text1 = "the quick brown fox did a thing"
#text2 = "the slow red dog did not do a thing"

#text1 = "this is a test"
#text2 = "this is not a test"

#open and read file
try:
    f1 = open(file1)
    contents1=f1.read()
    f2 = open(file2)
    contents2=f2.read()
except:
    print("cannot open files")
    quit()
text1 = contents1
text2 = contents2

rval = compare(list(text1), list(text2))

total = 0
matches = 0
score = 0.0


for s in rval:
    #op is symbol +,-,= for ins, del, match and arr is the corresponding value
    (op , arr) = s
    #print("s: " + str(s))
    #print("op: " + op)
    #print("arr: " + str(arr))
    total += len(arr)
    if (op == '='):
        matches += len(arr)

print('Total: ' + str(total))
print('Match: ' + str(matches))
if(total > 0):
    score = matches/total
print('Score: ' + str(score))


