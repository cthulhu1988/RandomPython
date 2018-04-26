import circle	
import rectangle

def main():

	choice = 0

	AREA_CIRCLE_CHOICE = 1
	CIRCUM_CHOICE = 2
	AREA_RECT_CHOICE = 3
	PERIMETER_CHOICE = 4
	QUIT_CHOICE = 5

	while choice !=5:
		display_menu()
		print()
		choice = int(input("Enter the number selection: "))
		if choice == 1:
			area_of_circle()
		elif choice == 2:
			circumference_circle()
		elif choice == 3:
			area_rectangle()
		elif choice == 4:
			user_perimeter()
		elif choice == 5:
			print("exiting")

def user_perimeter():
	length = float(input("Enter the Length: "))
	width = float(input("Enter the width: "))
	user_perimeter = rectangle.perimeter(length, width)
	print("The perimeter of your rectangle is",user_perimeter)
			
def area_rectangle():
	length = float(input("Enter the Length: "))
	width = float(input("Enter the width: "))
	user_area_rect = rectangle.area_rectangle(length, width)
	print("The area of your rectangle is",user_area_rect)

def area_of_circle():
	num = float(input("Enter the radius of the circle to be evaluated: "))
	user_area = circle.area(num)
	print("Your area is {} ".format(user_area))

def circumference_circle():
	num = float(input("Enter the radius of the circle to be evaluated: "))
	circumference = circle.circumference(num)
	print("The circumference of the circle is",circumference)

def display_menu():
	print("MENU --->")
	print("Area of a circle = enter 1")
	print("Circum choice = enter 2")
	print("Area of a rectangle = enter 3")
	print("perimeter choice = enter 4")
	print("Quit program = enter 5")
	print()
	
main()