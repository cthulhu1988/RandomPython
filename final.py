# binary search
def main20():

    list1 =[2,7,5,4,6,7,8,9,7,45,3,2,4,455,6,67,8,9,0,43,56,78,55,44,33,22,33,44,567]
    
    list1.sort()
    print(list1)
    x = binary_search(45,list1)
    print(x)

def binary_search(key,lst):
    low = 0
    high = len(lst)-1
    while high >= low:
        mid = (low + high)//2
        if key < lst[mid]:
            high = mid-1
        elif key == lst[mid]:
            return mid
        else:
            low = mid +1
            
main20()    



#algorithm work bench:

def main2():
    #my_string = "This is a string that counts spaces"
    index = 0
    for ch in my_string:
        if ch == ' ':
            index+=1
    print(index)
#main1()

def main3():
    my_nums = "these are numbers 1 2 3 4"
    index = 0
    for ch in my_nums:
        if ch.isdigit():
            index+=1
    print(index)
#main3()

def main4():
    my_string = "THis"
    index = 0
    for ch in my_string:
        if ch.islower():
            index+=1
    print(index)
#main4()

def main5():
    my_string = "back.coom"

    check = check_string(my_string)
    print(check)

    rev = reverse(my_string)
    print(rev)

def check_string(string):
    if string.endswith(".com"):
        return True
    else:
        return False
    
def reverse(string):
    new_string = ''
    begin = 0
    end = len(string)-1
    while end >= begin:
        new_string += string[end]
        end -=1
    return new_string

state = "Tennessee"
end = state[-3:]
#print(end)

#main5()

def main10():
    mystring = "cookies>milk>fudge>cake>ice Cream"
    list1 = mystring.split(">")
    for word in list1:
        print(word)
#main10()

def main11():
    newstr = "aaabbbccc"
    l = newstr.strip('cb')
    print(l)
#main11()





    
