s = 'abba'

'''The generic binomial formula is: n! / k! * (n-k)! If you use the generic formula, 
you're gonna get integer overflow, even with u128 integers (35!). But because the k is fixed:

n! / (2! * (n-2)!)
(1 / 2!) * (n! / (n-2)!)
And by definition of factorial n! => (n-2)! * (n-1) * n, so
(1/2) * ( ((n-2)! * (n-1) * n) / (n-2)! )
And the (n-2)! factorial cancels out, so we have:
(n * (n-1)) / 2'''


from collections import Counter
def sherlockAndAnagrams(s):
    count = 0
    for i in range(1,len(s)+1):
        a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        #print(a)
        b = Counter(a)
        print(b)
        for j in b:
            print("j:",j,b[j],b[j] - 1)
            count+=b[j]*(b[j]-1)/2
            print("count", count)
            
    return int(count)

print(sherlockAndAnagrams(s))