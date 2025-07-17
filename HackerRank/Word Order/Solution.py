# Enter your code here. Read input from STDIN. Print output to STDOUT

occurance = dict()

n = int (input())
words = [ input() for _ in range(n) ]

for word in words:
    if occurance.get(word):
        occurance[word] +=1 ;
    else:
        occurance[word] = 1

print (len(occurance))

occurance_counts = list( map (str, occurance.values()) )
print(' '.join( occurance_counts ))
