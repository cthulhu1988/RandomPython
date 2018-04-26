def main():
    palin = 12345678876754321
    is_palindrome(palin)
   

def is_palindrome(num):
    num = str(num)
    index = 0
    end = len(num)-1
    while index <= end:
        if num[index] == num[end]:
            index+=1
            end-= 1
            print(num[index],num[end])
        else:
            print("no")
            return False
    
main()
        
        
