#current limitations
#case sensitive. while this is not necessarily bad, T and t are only slightly different.
#these could be considered only half different or something arbitrary to capture the smiilarity. 

#TO DO
#modify case sensitivity
#pass dynamic values: DONE
#allow for switching between word and letter


#print ('list: ' + str(sys.argv))


def compare(old,new):
    old_map = dict()
    #set up a dict of each value and it's corresponding coordinates. so the string 
    #'hello' would return something like h:0 e:1 l:2,3 o:4
    for i, val in enumerate(old):
        #print('i: ' + str(i))
        #print('val: ' + str(val))
        old_map.setdefault(val,list()).append(i)

    match = dict()

    sold = 0
    snew = 0
    length = 0

    #inew is the index of each letter and val is the value
    
    for inew, val in enumerate(new):
        newmatch = dict()
        #print("inew: " + str(inew))
        #print("val: " + str(val))
        #for each match of value in old_map
        for iold in old_map.get(val,list()):
         #   print("iold: " + str(iold))
            #set value of newmatch at index of iold to iold and the index of the match dictionary defaulted to 1
            #number of matches
            newmatch[iold] = (iold and match.get(iold - 1, 0)) + 1
          #  print("weird amtch: " + str(match.get(iold - 1, 0)))
            #print("newmatch[iold]: " + str(newmatch[iold]))
           # print("newmatch: " + str(newmatch))
            if(newmatch[iold] > length):


                length = newmatch[iold]
                sold = iold - length + 1
                snew = inew - length + 1
             #   print("length: " + str(length) + " sold: " + str(sold) + " snew: " + str(snew))
        match = newmatch
        #print("match: " + str(match))
    #quit()


    if length == 0:
        #no common substring returns insert and delete
        return (old and [('-', old)] or []) + (new and [('+', new)] or [])
    else:
        #recursively compare the text before and after the common substring
        return compare(old[ : sold], new[ : snew]) + \
                [('=', new[snew : snew + length])] + \
                compare(old[sold + length : ],
                        new[snew + length : ])
        
text1="""The easiest way to earn points with Fetch Rewards is to just shop for the best products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."""
text2="""The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."""

#text1 = "abc"
#text2 = "vnc"

#text1 = "the quick brown fox did a thing"
#text2 = "the slow red dog did not do a thing"

text1 = "abc"
text2 = "abcde"



rval = compare(list(text1), list(text2))

total = 0
matches = 0
score = 0.0


for s in rval:
    print(str(s))
    (op , arr) = s
    #print(arr)
    total += len(arr)
    if (op == '='):
        matches += (2*len(arr)) 
        total += len(arr)

print('Total: ' + str(total))
print('Match: ' + str(matches))
if(total > 0):
    score = (matches)/total
print('Score: ' + str(score))


