products = {}
cart = {}

while True:
    print("Enter 'add' to add a product or 'products' to see what you have")
    option = input('Enter your option: ')

    if option == 'add':
        product = input('Enter product name: ')
        quantity = int(input('Enter quantity: '))
        products[product] = quantity
    elif option == 'products':
        print(f'All products: {products}')
        print(f'Your cart: {cart}')
        print('1) add product to cart, 2) change product in cart, '
              '3) delete product from cart: ')
        choice = input('Your choice: ')

        if choice == '1':
            cart_product = input('Enter product name to add: ')

            if cart_product in products:
                cart_quantity = int(input('Enter quantity: '))

                if cart_quantity <= products[cart_product]:
                    products[cart_product] -= cart_quantity
                    cart[cart_product] = cart_quantity
                else:
                    print('Check quantity available')
            else:
                print('Does not exist in products dict, add it there')
        elif choice == '2':
            cart_product_to_change = input('Enter product name to change: ')

            if cart_product_to_change in cart:
                new_cart_product = input('Enter new product name: ')

                if new_cart_product in products:
                    new_cart_quantity = int(input('Enter new quantity: '))

                    if new_cart_quantity <= products[new_cart_product]:
                        products[new_cart_product] -= new_cart_quantity
                        cart.pop(cart_product_to_change)
                        cart[new_cart_product] = new_cart_quantity
                    else:
                        print('Check quantity available')
                else:
                    print('Does not exist in products dict, add it there')
            else:
                print('Does not exist in cart, add it there')
        elif choice == '3':
            product_to_delete = input('Enter product name to delete: ')

            if product_to_delete in cart:
                cart.pop(product_to_delete)
            else:
                print('Does not exist in cart')

        print(f'Your cart: {cart}')

    else:
        print('Wrong option')
