def main1():
    word_sep("StopAndSmellTheRoses.")

def word_sep(string):
    new_string=''
    for ch in string:
        if ch.isupper():
            ch = ch.lower()
            new_string+=(" "+ch)
        else:
            new_string+=ch
    new_string = new_string.strip()
    new_string = new_string.capitalize()
    print(new_string)
main1()




'''

def main5():
    binary = [9,4,3,45,6,7,5,4,3,2,1]
    #x = locate_min(binary,0,len(binary)-1)
    #print(x)
    selection_sort(binary)
    print(binary)

def selection_sort(lst):
    top = 0
    end = len(lst)-1
    while top < end:
        min_pos = locate_min(lst,top,end)
        lst[top],lst[min_pos] = lst[min_pos],lst[top]
        top+=1

        
def locate_min(lst, begin, end):
    smallest = lst[begin]
    pos = begin
    k = begin + 1
    while k <= end:
        if lst[k] < smallest:
            smallest = lst[k]
            pos = k
        k+=1
    return pos


main5()





def main4():
    binary = [2,4,5,6,4,3,2,45,6,7,8,98,6,4,4,6,7,87,8,5,4,3,3,4,5,4,67,8,9,9,9,8,8,7,77,6,65]
    new_lst = [6,4,3,5,6,4,3,2]
    length1 = len(binary)
    length = len(new_lst)
    yes = locate_min(binary,0,length1 - 1)
    print(yes)

def locate_min(lst, begin, end):
    
    smallest = lst[begin]
    pos = begin

    k = begin+1
    while k <= end:
        if lst[k] < smallest:
            smallest = lst[k]
            pos = k
        k+=1
    return pos

main4()

def main3():
    binary = [2,1,4,5,6,4,3,2,45,6,7,8,98,6,4,4,6,7,87,8,5,4,3,3,4,5,4,67,8,9,9,9,8,8,7,77,6,65]
    #binary.sort()

    x = binary_search(binary,9)
    print(x)
    
def binary_search(lst,key):
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (high+low)//2
        if key == mid:
            return mid
        elif key < mid:
            high = mid -1
        else:
            low = mid + 1
    return -1

#main3()



def main2():
    numbers = [1,2,3,4,5,6,7]

    outfile = open("text.txt","w")

    for item in numbers:
        outfile.write(str(item)+"\n")
    outfile.close()

#main2()







def main():
    infile = open("text.txt","r")

    numbers = infile.readlines()
    
    infile.close()

    index = 0

    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index+=1

    print(numbers)
    



#main()


'''
