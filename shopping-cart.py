from IPython.display import clear_output

store = {}

shop_cart = store()

only_answer = {'Add', 'Remove', 'Show', 'Clear', 'Quit'}

def shopping_cart():     
    while True:
        answer = input('Welcome to Braxton Shoppe What would you like to do? Add/Remove/Show/Clear/Quit ').title()
        
        while answer not in only_answer:
            answer = 'That is not an option. What would you like to do? Add/Remove/Show/Clear/Quit '.title()
        if answer == 'quit':
            clear_output()
        elif answer == 'add':
            add_to_cart(shop_cart)
        elif answer == 'remove':
            remove_from_cart(shop_cart)
        #elif answer == 'clear':
            #clear_cart(shop_cart)


    # add to cart
def add_to_cart():
    item = input('What would you like to add to your cart? ').title()
    if item in shop_cart:
        amount = int(input(f'How many {item} would you like to add to your cart? '))
        cart[item]['amount'] += amount 
    else:
        price = float(input(f'What is the price of {item}'))
        amount = int(input(f'How many {item} would you like to add to your cart? '))
        cart[item] = {'price': price, 'amount': amount}
    clear_output()
    print(f'{amount} {item} have been added to your cart! ')

    # Remove from cart
def remove_from_cart():
    item = input('What would you like to add to your cart? ').title()
    if item in self.cart:
        amount = int(input(f'How many {item} would you like to add to your cart? '))
        cart[item]['amount'] += amount 
    else:
        price = float(input(f'What is the price of {item}'))
        amount = int(input(f'How many {item} would you like to add to your cart? '))
        cart[item] = {'price': price, 'amount': amount}
    clear_output()
    print(f'{amount} {item} have been added to your cart! ')

    # Show in cart
def item_to_cart():
    item = input('What would you like to add to your cart? ').title()
    if item in self.cart:
        amount = int(input(f'How many {item} would you like to add to your cart? '))
        cart[item]['amount'] += amount 
    else:
        price = float(input(f'What is the price of {item}'))
        amount = int(input(f'How many {item} would you like to add to your cart? '))
        cart[item] = {'price': price, 'amount': amount}
    clear_output()
    print(f'{amount} {item} have been added to your cart! ')
    
    # Clear the cart
def item_to_cart():
    item = input('What would you like to add to your cart? ').title()
    if item in self.cart:
        amount = int(input(f'How many {item} would you like to add to your cart? '))
        cart[item]['amount'] += amount 
    else:
        price = float(input(f'What is the price of {item}'))
        amount = int(input(f'How many {item} would you like to add to your cart? '))
        cart[item] = {'price': price, 'amount': amount}
    clear_output()
    print(f'{amount} {item} have been added to your cart! ')

print('Thank you for shopping at Braxton/"s Store')
#print(shop_cart, True)        
