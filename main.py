from shop import (
    print_menu,
    print_originals,
    print_signatures,
    get_order,
    print_order,
    get_total_price,
    accept_credit_card,
)

print_menu()
print_originals()
print_signatures()
order_list = get_order()
print_order(order_list)
print(get_total_price(order_list))
