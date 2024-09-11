def restaurant():
    
    menu = {
        'Burger': 50,
        'Pizza': 800,
        'Salad': 80,
        'Pasta': 70,
        'Fries': 200,
        'Sandwich': 40,
        'Soup': 300,
        'Steak': 140,
        'Soda': 10,
        'Ice Cream': 30
    }

    print("Welcome to our restaurant! Here is our menu:\n")
    
    for item, price in menu.items():
        print(f"{item}: ₹{price}")
    
    print("\nType 'exit' when you are finished ordering.\n")
    
    total_bill = 0.0
    
    while True:
        order = input("Please enter the item you'd like to order: ").strip().title()
        
        if order == 'Exit':
            break
        elif order in menu:
            total_bill += menu[order]
            print(f"{order} added to your order. Current total: ₹{total_bill:}")
        else:
            print("Sorry, that item is not on the menu. Please choose an item from the menu.")
    
    print(f"\nThank you! Your total bill is: ₹{total_bill:}")


restaurant()