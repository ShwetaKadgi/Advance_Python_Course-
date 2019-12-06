# Introduction to python modules
"""def make_pizza(*toppings):

    #print list of toppings that have been requested
    print(toppings)

make_pizza('Pepperoni')
make_pizza('onions','olives','cheeze')
"""

def make_pizza(size,*toppings):
    """Summarize the pizzas we are about to make """
    print(f"\n Making a {size}-inch pizza with the following toppings :")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(12,'corn','onion','cheeze')
make_pizza(16,'corn')

