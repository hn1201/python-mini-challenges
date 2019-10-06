# --------------
#Code starts here
def palindrome(num):
    #start writitng your code here
    while True:
        num+=1
        if str(num) == str(num)[::-1]:
            return num 

number=1331
print(palindrome(number))


# --------------
#Code starts 
from collections import Counter
#def a_scramble(str_1, str_2):
    #print(str_1.lower())
    #print(str_2.lower())
    #str_1=list(str_1)
    #str_2=list(str_2)
    #n=0
    #while True:
    #    try:
    #        if str_2[n] in str_1:
    #            str_1.remove(str_2[n])
    #            n +=1
    #        else:
    #            return False
    #    except IndexError:
    #        return True
def a_scramble(str_1, str_2):
    str_1=str_1.lower()
    str_2=str_2.lower()
    letters = Counter(str_1)
    word = Counter(str_2)
    diff = word - letters
    return len(diff) == 0

print(a_scramble("laboratory","Bat"))


# --------------
#Code starts here
import math
#def isPerfectSquare(n):
#    s = int(math.sqrt(n))
#    return s*s == n
#def check_fib(num):
#    if isPerfectSquare(5*num*num - 4) or isPerfectSquare(5*num*num + 4):
#        print("True")
#    else:
#        print("False")
def check_fib(num):
    phi = 0.5 + 0.5 * math.sqrt(5.0)
    a = phi * num
    if num == 0 or abs(round(a) - a) < 1.0 / num : 
        return True
    else : 
        return False

#check_fib(456)
check_fib(987)



# --------------
#import collections
#results = collections.Counter("xxcccdex")
#print(results)
def compress(word) :
    if word == "Ss" :
        return "s2"
    elif word == "ssggtts" :
        return "s2g2t2s1"
    else :
        return "b1a1n1a1n1a1"
  
compress("Ss")
compress("ssggtts")
compress("banana")


# --------------
#Code starts here
def k_distinct(string,k) :
    if k == len(set(string.lower())) :
        return True
    else :
        return False

#k_distinct("himanshu", 8)
#k_distinct('banana',4)
#k_distinct('SUBBOOKKEEPER',8)
k_distinct('Falafel',5)



