# OLA112 BY Isaac Callison,  CSCI 1170-sec007,  Due: 11/30/2016
# PROGRAM ID: bakery.py / Calculates & prints Monthly Cost of Products Forecast
# AUTHOR:  Isaac Callison
# INSTALLATION:  MTSU
# REMARKS:  This program calculates and prints the Monthly Cost of Bakery
# Products Forecast table. The program obtains all input from three data
# files. The products file contains the number of products and a list of
# the names. The ingredients file contains the number of ingredients and a
# list of the amount of ingredient used in each product. The prices file
# contains values representing the beginning and ending months of the report
# and a list containing the price of each ingredient for each month. The
# program reads in this data, processes it, and prints a formatted table. 
#
#   .    1    .    2    .    3    .    4    .    5    .    6    .    7    .    8
#2345678901234567890123456789012345678901234567890123456789012345678901234567890

import os.path

# Main routine
# --- Do not change this function; use as-is -----------------------------------
def main():
    # --- File name constants:
    PRODUCTS_FILE    = "products.dat"     # Products filename
    INGREDIENTS_FILE = "ingredients.dat"  # Ingredients filename
    PRICES_FILE      = "prices.dat"       # Prices filename
    # --- Local variables:
    # num_products        (int)    # Number of products
    # num_ingredients     (int)    # Number of ingredients
    # first_month         (int)    # Beginning month of report
    # last_month          (int)    # Ending month of report
    # product[]           (str)    # Names of products
    # recipe[][]          (int)    # Ingredient quantities
    # price[][]           (int)    # Ingredient prices
    # forecast_cost[][]   (int)    # Forecast Product costs

    # Get product names
    num_products,product_name = get_products(PRODUCTS_FILE)
    
    # Get recipe ingredient quantities
    num_ingredients,recipe = get_recipes(INGREDIENTS_FILE, num_products)

    # Get monthly prices of ingredients
    first_month,last_month,price = get_prices(PRICES_FILE, num_ingredients)
    num_months = span_of_months(first_month,last_month)

    # Calculate forecast product costs, by product by month
    forecast_cost = forecast_monthly_product_costs(           \
                    num_products, num_months, num_ingredients, recipe, price)

    # Print the forecast table of costs
    print_table(product_name,forecast_cost,num_products,first_month,last_month)
     


# --- Do not change this function; use as-is -----------------------------------
def get_products(products_file):
# Read in the number of products and the product names from the products file.
# Pre:  The 'products_file' is the name of the input file.
# Post: 'num_products' contains the total number of products and
#       'products' list contains the product names.
    
    # Open the input 
    if not os.path.isfile(products_file):
        print("ERROR: Could not open", products_file)
        sys.exit()   # stop the program
    prodfile = open(products_file,'r')

    # Read in number of products contained in file
    num_products = int( prodfile.readline() )
    
    # Read and store the product names
    product_name = [ None for p in range(num_products)]
    for prod in range(num_products):
        product_name[prod] = prodfile.readline().strip()
        
    # Close the input PRODUCTS_FILE
    prodfile.close()

    return num_products,product_name



# ??? COMPLETE THIS FUNCTION - [Hint: Use get_prices() logic as an example] ----
# ------------------------------------------------------------------------------
def get_recipes(ingredients_file, num_products):
# Store amounts of ingredients used in each product from the ingredients file.
# Pre:  'ingredients_file' has been set and 'num_products' contains the the
#        total number of products.
# Post: 'num_ingredients' contains the total number of ingredients
#       and 'num_products' rows of 'recipe' contain
#       'num_ingredients' elements with the ingredient amounts.
    
    # Open the input ingredients_file
    # ???
    ingredients_file_object = open(ingredients_file,"r")

    # Read in number of ingredients contained in file
    # ???
    num_ingredients = int(ingredients_file_object.readline())
   
    # Read in the quantity of each ingredient per product
    recipe = [[0]*num_ingredients for p in range(num_products)]
    for row in range(num_products):
        row_line = (ingredients_file_object.readline())
        row_line = row_line.split()
        index = 0
        for column in range(num_ingredients):
            row = int(row)
            column = int(column)
            recipe[row][column] = row_line[index]
            index+=1
    print(recipe)
            
            #print("row: {} and char {}".format(row,column))
        

    # creates 7 num_product rows, with 6 columns in each row. 
    # ???  Hint: there will be two for loops in the code you supply
        

    # Close the input ingredients_file
    # ???
    ingredients_file_object.close()

    return num_ingredients,recipe

    

# --- Do not change this function; use as-is -----------------------------------
def get_prices(prices_file, num_ingredients):
# Read in the monthly prices of the ingredients and the date range.
# Pre:  'prices_file' and 'num_ingredients' properly set.
# Post: 'first_month' and 'last_month' are set
#       and 'price' has 'num_ingredients'rows by 'num_months' elements
#       with the corresponding ingredient costs.

    # Open the input prices_file
    if not os.path.isfile(prices_file):
        print("ERROR: Could not open", prices_file)
        sys.exit()   # stop the program
    prices = open(prices_file,'r')

    # Read in what the 'first_month' and 'last_month' are.
    first_month,last_month = map(int,prices.readline().split())
    months = span_of_months(first_month,last_month)
     
    # Read in the monthly prices for each ingredient
    price = [[0]*months for i in range(num_ingredients)]
    for i in range(num_ingredients):
        spot_price = prices.readline().split()
        for month in range(months):
            price[i][month] = int(spot_price[month])
        
    # Close the input prices_file
    prices.close()

    return first_month,last_month,price



# --- Do not change this function; use as-is -----------------------------------
def span_of_months(first_month, last_month):
# Ascertain span of months; that is, how many months between first and last.
# Pre:  'first_month' and 'last_month' have valid values.
# Post: Returns the span of months between first and last month.
    if last_month > first_month:
        return (last_month-first_month)+1
    else:
        return (13 -(first_month-last_month))
    


# ??? COMPLETE THIS FUNCTION - [Hint: Think about how you'd do it by hand.] ----
# ------------------------------------------------------------------------------
def forecast_monthly_product_costs(           \
                    num_products, num_months, num_ingredients, recipe, price):
# Calculate forecast product costs, by month.
# Pre:  All "IN" parameters have correct values.
# Post: The appropriate elements of the 'forecast_cost' table will
#       contain the predicted product cost.

    # Initialize matrix of costs to zero
    forecast_cost=[ [0]*num_months for p in range(num_products)]

    for prod in range(num_products):
        for month in range(num_months):
            for ingred in range(num_ingredients):
                # forecast_cost for product by month = SUM ( amount of ingredient * price of ingredient(monthly) )
                pass    # ??? get rid of this stub "pass" statement
                #         ??? ...replace this comment with YOUR code...

    return forecast_cost



# --- Do not change this function; use as-is -----------------------------------
def print_table(product, forecast_cost, num_products, first_month, last_month):
# Print nicely formatted forecast of product costs, by product, by month.
# Pre:  All "IN" parameters have correct values.
# Post: A table will be printed to stdout.  Long lines are not wrapped.
    num_months = span_of_months(first_month,last_month)

    # Print the forecast table heading
    print_table_heading(first_month, last_month)
    
    # print each row of the forecast table
    for prod in range(num_products):
        print_table_row(num_months, product[prod], forecast_cost[prod]) 
        


# --- Do not change this function; use as-is -----------------------------------
def print_table_heading(first_month, last_month):
# Print the heading for the table.
# Pre:  All "IN" parameters have correct values.
# Post: The table title, title of each column, and a separator line
#       will be printed to stdout.
    MO=["", "Jan","Feb","Mar","Apr","May","Jun",        \
            "Jul","Aug","Sep","Oct","Nov", "Dec"]
    num_months = span_of_months(first_month,last_month)

    
    # print table title and title of product column
    print("Monthly Cost of Bakery Products Forecast\n")
    print("Product      ", end='')
    
    # Print out the Months by name
    month = first_month        # Current month to be printed
    for column in range( num_months ):
        print('   ' + MO[month] + ' ', end='')
        month += 1
        if month > 12:  # When we get to December wrap back to January
            month = 1
    print()
    
    #  This section creates the header line
    
    print('-'*12, '+', sep='', end='')  # Prime the pump.  Add the first +
    for column in range( num_months ):
        print('-'*6, '+', sep='', end='')
    print()
    
    return



# --- Do not change this function; use as-is -----------------------------------
def print_table_row(num_months, product, monthly_cost):
# Print the product name and the costs per month for that product.
# Pre:  All "IN" parameters have correct values.
# Post: The product name and cost for each month will be printed
#       to stdout.

    # print product name
    print( format(product,'13s')[:13], end='')
    
    # print cost to produce product during each month
    for month in range(num_months):
        print( format(monthly_cost[month],'6d'), end=' ')
    print()
    
    return



# -- Invoke main function --
main()

