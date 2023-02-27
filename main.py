def info(request):
    if request == 'Help': # Help menu for new users
        print("""\nHere at Food-R-Us we want to help people
we do this by offering food at discount rates.

You may view our menu by entering 'menu'.
In your cart you may 'add', 'remove' or 'see cart' items, 
When you are all finished, say 'checkout'.\n""")
    elif request == 'Menu': # Menu which could change perodically 
        print("""\n
____________________________________________
|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|
|******************  Menu  *****************|
|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|
|---------                         ---------|
|---------     Pineapple: $1.99    ---------|
|---------       Banana: $0.59     ---------|
|---------  Hamburger Buns: $1.99  ---------|
|---------       Bacon: $3.99      ---------|
|---------      Avocado: $0.99     ---------|
|---------       Ranch: $2.59      ---------|
|---------  Sliced Cheese: $2.99   ---------|
|---------   Ground Beef: $4.99    ---------|
|---------                         ---------|
|-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|
____________________________________________\n""")
        
def price(item):
    # Price list - could change periodically as supply changes
    price_dict = {
        'Pineapple': '1.99',
        'Banana': '0.59',
        'Bacon': '3.99',
        'Ranch': '2.59',
        'Ground Beef': '4.99',
        'Hamburger Buns': '1.99',
        'Sliced Cheese': '2.99',
        'Avocado': '0.99'}
    if item not in price_dict:
        return -1
    return price_dict[item]

def view_cart(cart, cart_total):
    # Used to print the items in the cart, the count of the items, and the total cost for all of the items
    unique_list = []
    # Creates unique list of items 
    for item in cart:
        if item not in unique_list:
            unique_list.append(item)
    # Prints count of each item, item's name, item's price
    print("\n__________________")
    for item in unique_list:
        print(f"\n{cart.count(item)}x {item} - ${price(item)}")
    print(f"__________________\nGrand Total: ${cart_total:.2f}\n")




def shopping_cart():
    cart = []
    request = ''
    flag = True # Flag for error checking in 'add' 
    cart_total = float(0)
    print("\n\nHello, welcome to your digital shopping cart, what would you like to do (enter 'help' if you don't know)?\n")
    while request != 'Checkout':
        request = input("Enter request(or 'help'): ").title().strip()
        if request == 'Help':
            info(request)
        elif request == 'Add':
            # Adds items to the user's cart based upon inputs
            print("\033c") # Clears output
            info('Menu') # Prints menu
            # Adds items to the user's cart from the menu based upon inputs
            while request.title().strip() != 'N':
                # For first loop, to continue to input, ensures that the user will be prompted as long as add is not input
                # Flag determines if input should be stored in the cart and the total should be updated 
                if (request != 'Add') and (flag == True):
                    if price(request) == -1:
                          print("That's not on the menu!")
                          flag = False
                          continue
                    cart_total += float(price(request)) # running total, price of what is in cart
                    cart.append(request) # list of everything added to cart
                    print(f"{request.title()} has been added to cart.")
                request = input("What would you like to add('n' if done)? ").title().strip()
                flag = True
            print("\033c") # Clears output
        elif request == 'Remove':
            # Removes items to the user's cart based upon inputs
            print("\033c") # Clears output
            while request.title() != 'N':
                view_cart(cart, cart_total) # Prints cart
                request = input("What would you like to remove? ").title().strip()
                print("\033c") # Clears output
                # Error checking if input is does not exit in cart
                if request not in cart:
                    print(f"{request} is not in your cart, buddy.")
                    continue
                cart_total -= float(price(request)) # running total, price of what is in cart
                cart.remove(request) # list of everything removed to cart
                print(f"{request.title()} has been removed from cart.\n\nUpdated Cart:")
                view_cart(cart, cart_total) # Prints cart
                request = input("Remove another 'y'/'n': ")
            print("\033c") # Clears output
        elif request == 'See Cart':
            print("\033c") # Clears output
            view_cart(cart, cart_total) # Prints cart
        elif request == 'Menu':
            print("\033c") # Clears output
            info('Menu') # Prints Menu
        elif request != 'Checkout':
            print("\033c") # Clears output
            print("Try using 'help' if you are unsure what to enter!\n")
    # Checkout Process
    print("\033c") # Clears output
    if cart_total == 0:
        print("\nSad, you didn't buy anything :(")
    else:
        print("\nHere is a receipt of your purchases with us today:")
        # Prints Receipt
        view_cart(cart, cart_total)
    print("\nHave a great day!")
    
        
shopping_cart()
