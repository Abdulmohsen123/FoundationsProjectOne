####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate",
                    "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Best Shop"
signature_flavors = "Vanilla"
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print(menu)


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    # for flavor in original_flavors:
    #     print(flavor)
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    print(original_flavors)


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    print(signature_flavors)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    #print (True if order_list else "Sorry we don't have that, please check our menu ", menu)
    if order in original_flavors:
        return True
    elif order in order_list:
        return True
    elif order in menu:
        return True
    else:
        return False


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    customer_order = getUserInput()
    while customer_order != "Exit":
        if is_valid_order(customer_order):
            order_list.append(customer_order)
        else:
            print("Not valid order")
        customer_order = getUserInput()
    print("Exiting")
    return order_list
    
def getUserInput():
    return input("What's you order? or 'Exit' to complete \n")

def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total == 0:
        return False
    return total


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for value in order_list:
        item_price = menu[value]
        total = total + item_price
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    print(order_list)
