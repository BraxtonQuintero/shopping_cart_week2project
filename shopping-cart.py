from IPython.display import clear_output
class shopping_cart:

    def __init__(self, add, remove, show, clear, quit, shop):
        self.add_to_cart = add
        self.remove_from_cart = remove
        self.show_cart = show
        self.clear_cart = clear
        self.quit_cart = quit
        self.shop_cart = shop
        

    def main():     
        my_cart = shopping_cart()
        correct_answer = ('Add', 'Remove', 'Show', 'Clear', 'Quit')

        while True:
            answer = input('Welcome to Braxton Shoppe What would you like to do? Add/Remove/Show/Clear/Quit ').title()
    
            while answer not in correct_answer:
                answer = 'That is not an option. What would you like to do? Add/Remove/Show/Clear/Quit '.title()
            if answer == 'quit':
                clear_output()
                break
            elif answer == 'add':
                my_cart.add_to_cart()
            elif answer == 'remove':
                my_cart.remove_from_cart()
            elif answer == 'clear':
                my_cart.clear_cart(my_cart)

    def add_to_cart(self):
        item = input('What would you like to add to your cart? ').title()
        if item in self.shop_cart:
            amount = int(input(f'How many {item} would you like to add to your cart? '))
            self.cart[item]['amount'] += amount 
        else:
            price = float(input(f'What is the price of {item}'))
            amount = int(input(f'How many {item} would you like to add to your cart? '))
            self.cart[item] = {'price': price, 'amount': amount}
        clear_output()
        print(f'{amount} {item} have been added to your cart! ')

    def remove_from_cart(self):
        item = input('What would you like to remove from your cart? ').title()
        if item in self.shop_cart:
            amount = int(input(f'How many {item} would you like to remove from your cart? '))
            self.cart[item]['amount'] -= amount 
        print(f'{amount} {item} have been removed from your cart! ')
        pass
    def show_cart():
        print(my_cart)
        pass

    def clear_cart(self):
        my_cart.clear()
        pass
