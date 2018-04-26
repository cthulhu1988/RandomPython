def main():
    num_students = int(input("How many students do you have: "))
    num_scores = int(input("How many test scores/student?: "))

    for student in range(num_students):
        total = 0.0
        print("student number", student +1)
        for test_num in range(num_scores):
            print("Test number", test_num+1, end='')
            score = float(input(": "))
            total += score
        avg = total/num_scores
        print("The average for student number", student+1, "is:", avg)
        
    

main()
