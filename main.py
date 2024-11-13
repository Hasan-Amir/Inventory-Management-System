class Product:
    def __init__(self, product_id, name, category, price, stock_quantity ):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity
    def show_product(self):
        print(f"Product id: {self.product_id}, Product name: {self.name}, Price: {self.price}, Stock: {self.stock_quantity}")

class Inventory:
    
    def __init__(self):
        self.products = []
    def _add_product(self):
        print("\nKindly enter product details to add the product: ")
        product_id = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")
        price = float(input("Enter Product Price: "))  # Convert price to float
        stock_quantity = int(input("Enter Stock Quantity: "))  # Convert stock quantity to int
        self.products.append(Product(product_id, name, category, price, stock_quantity))
        print("Product successfully added")
    def _edit_product(self):
        id = input("\nEnter the id of the product to be edited: ")
        for item in self.products:
            if item.product_id == id:
                item.name = input("Enter the name of the product: ")
                item.category = input("Enter the category of the product: ")
                item.price = float(input("Enter the price of the product: "))
                item.stock_quantity = int(input("Enter the stock quantity of the product: "))
                print(f"Product with id {id} successfully updated.")
        print(f"Product with id {id} not found.")
    def _delete_product(self):
        id= input("\nEnter the id of the product to be deleted: ")
        for item in self.products:
            if item.product_id == id:
                self.products.remove(item)
                print(f"Product with id {id} successfully deleted")
                return
        print(f"Product with id {id} not found.")

    def show_products(self):
        if self.products:
            print("\nInventory List: ")
            for product in self.products:
                product.show_product()
        else:
            print("Inventory is empty")
class User(Inventory):
    def __init__(self,name,password):
        self.name = name
        self.password = password
        super().__init__()
    def add_product(self):
        return super()._add_product()
    def edit_product(self):
        return super()._edit_product()
    def delete_product(self):
        return super()._delete_product()
    def show_products(self):
        return super().show_products()
    
u1 = User("admin", 0000)

def login(): 
    user = {"admin":"0000","ali":"1111", "nauman":"2222", "asif":"3333"}   
    print("Inventory Management System")
    print(f"(For Program checking Purposes the registered users are: {user})\n(and no products have been added, so add products first to check the functionality of the program!)")
    
    user_name = input("Enter User Name:  ")
    
    if user_name.lower() == "admin":
        password = input("Enter the password for the Admin: ")
        if password == user["admin"]:
            print("Login successful.\nWellcome to the inventory Management System, Admin.")
            while True:
                choice = input("\nWhat you want to do:\nEnter 1 to add product\nEnter 2 to update product\nEnter 3 to delete product\nEnter 4 to check inventory status\nEnter q to quit the program\nEnter here: ")
                if choice == "1":
                    u1.add_product()
                    continue
                elif choice == "2":
                    u1.edit_product()
                    continue
                elif choice == "3":
                    u1.delete_product()
                    continue
                elif choice == "4":
                    u1.show_products()
                    continue
                elif choice == "q":
                    quit()
                else:
                    print("invalid input")
        else:
            print("Invalid password")
    elif user_name in user:
        password = input("Enter your password: ")
        if user[user_name] == password:
            print(f"Login successful.\nWelcome {user_name}")
            choice = input("Press 1 to show inventory status or any other key to quit: ")
            if choice == "1":
                u1.show_products()
            else:
                quit()
        else:
            print("Incorrect Password.")
    else:
        print("Incorrect username.")    
login()
