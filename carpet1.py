# ola105 BY Isaac Callison, CSCI 1170-007, Due: 9/20/2016
#
# PROGRAM ID: carpet.py / The Carpet Bill Problem
# AUTHOR: Isaac Callison
# INSTALLATION: MTSU
# REMARKS: This program calculates the amount a customer of the
# Maripot Carpet Store should be charged. Input includes the
# amount of carpet purchased plus various cost factors. Output
# inlcudes a cost breakdown and total charge to the customer.
# Refer to the "ola105 Exercise" handout for more details.

STATE_TAX = 0.0975


def main():

    
    # Read in data for calculation of carpet yardage, cost, labor, floor prep, discount.
    sq_yards_purchased = int(input("Enter number of square yards purchased: "))
    cost_per_sq_yard = float(input("Enter cost per square yard: $"))
    labor_cost_per_sq_yard = float(input("Enter cost of labor per square yard: $"))
    floor_prep_charge = float(input("Enter floor preparation cost: $"))
    customer_discount = float(input("Enter customer discount rate: $"))

    # Calculate relevant data based on data read in from above.
    carpet_charge = (sq_yards_purchased * cost_per_sq_yard)
    labor_charge = (sq_yards_purchased * labor_cost_per_sq_yard + floor_prep_charge)
    calculated_customer_discount = (customer_discount * carpet_charge)
    tax_is_theft = (STATE_TAX * (carpet_charge - calculated_customer_discount))
    total_customer_charge = (carpet_charge
                             + labor_charge
                             - calculated_customer_discount
                             + tax_is_theft)
    
    # reiterate user input.
    print("Square yards purchased:     ",format(sq_yards_purchased,'>8d'))
    print("Cost per square yard:      $",format(cost_per_sq_yard,'>8.2f'))
    print("Labor per square yard:     $",format(labor_cost_per_sq_yard,'>8.2f'))
    print("Floor preparation cost:    $",format(floor_prep_charge,'>8.2f'))
  
    # print formated calculations.
    print("Cost for carpet:           $",format(carpet_charge,'>8.2f'))
    print("Cost for labor:            $",format(labor_charge,'>8.2f'))
    print("Discount on carpet:        $",format(calculated_customer_discount,'>8.2f'))
    print("Tax on carpet:             $",format(tax_is_theft,'>8.2f'))
    print("Charge to customer:        $",format(total_customer_charge,'>8.2f'))

#call main
main()

