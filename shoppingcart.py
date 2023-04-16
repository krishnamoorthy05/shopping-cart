class shoppingcart :
    items = {'toys':4,'phones':8,'shirt':6,'pants':10,'shoes':10}
    prices= {'toys':100,'phones':2500,'shirt':1000,'pants':700,'shoes':550}
    def __init__(self,c_name,ph_no):
        self.c_name=c_name
        self.ph_no=ph_no
        self.cart={}
        self.price=0
    def main(self):
        print()
        op=int(input(" Enter 1 to display all the item : \n Enter 2 to display your details : \n Enter 3 to add items in cart : \n Enter 4 to remove items from cart : \n Enter 5 to exit : "))
        if op==1:
            self.display()
            self.main()
        elif op==2:
            self.c_display()
            self.main()
        elif op==3:
            self.additems()
            self.main()
        elif op==4:
            self.removeitems()
            self.main()
        elif op==5:
            print('Thank You for shopping !!')
            return
        else:
            print('invalid Input')
            self.main()
    @classmethod
    def display(cls):
        print('Items available are : ')
        for items in shoppingcart.items:
            print(f'{items} : {shoppingcart.items[items]} ,price per unit : {shoppingcart.prices[items]}')
    def c_display (self):
        print(f'Name : {self.c_name}')
        print (f'Phonenumber : {self.ph_no}')
        if len(self.cart)==0:
            print('Your cart is empty ,The value of cart is 0')
        else :
            print("items present in your cart")
            for items in self.cart:
                print(f'{items} : {self.cart[items]}')
    def additems(self):
        item_name = input ("enter the item name :")
        if item_name not in shoppingcart.items:
            print("items not available")
        else :
            count=int(input(f'Tne number of {item_name} left is {shoppingcart.items[item_name]} \nEnter the number of {item_name} you want to add :'))
            if shoppingcart.items[item_name]<count:
                print(f'stock not available ,only {shoppingcart.items[item_name]} left : ')
            else :
                print("Added successfully")
                self.price+=(shoppingcart.prices[item_name]*count)
                print(f'your cart value is :Rs {self.price}')
                if item_name in self.cart:
                    self.cart[item_name]+=count
                else:
                    self.cart[item_name]=count
                shoppingcart.items[item_name]-=count
    def removeitems(self):
        if bool (self.cart):
            item_name=input("Enter the item name :")
            if item_name  in self.cart:
                count=int(input("Enter the number of item to remove:"))
                
                if self.cart[item_name]<count :
                    print(f'Not possible to remove {count}-{item_name} since You have only {self.cart[item_name]} {item_name} in Your cart ')
                else:
                    print("remove successfully")
                    self.price-=(shoppingcart.prices[item_name]*count)
                    print(f'your cart value is :Rs {self.price} ')
                    self.cart[item_name]-=count
                    shoppingcart.items[item_name]+=count
            else:
                print("This item is not present your cart ")
        else:
            print("your cart is empty you cannot remove ")
c=shoppingcart('krishna',9876543210)
c.main()

                
