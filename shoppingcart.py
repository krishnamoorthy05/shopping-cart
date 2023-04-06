class shoppingcart :
    items = {'toys':4,'phones':8,'shirt':6,'pants':10,'shoes':10}
    def __init__(self,c_name,ph_no):
        self.c_name=c_name
        self.ph_no=ph_no
        self.cart={}
    def main(self):
        print()
        op=int(input(' Enter 1 to display all the item : \n Enter 2 to display your details : \n Enter 3 to add items in cart : \n Enter 4 to remove items from cart : \n Enter 5 to exit : '))
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
            print(f'{items} : {shoppingcart.items[items]}')
    def c_display (self):
        print(f'Name : {self.c_name}')
        print (f'Phonenumber : {self.ph_no}')
        if len(self.cart)==0:
            print('Your cart is empty')
        else :
            print("items present in your cart")
            for items in self.cart:
                print(f'{item} : {self.cart[item]}')
    def additems(self):
        item_name = input ("enter the item name :")
        if item_name not in shoppingcart.items:
            prinnt("items not available")
        else :
            count=int(input("Enter the number of items you want to add :"))
            if shoppingcart.items[item_name]<count:
                print(f'stock not available ,only {shoppingcart.items[item_name]} left : ')
            else :
                print("Added successfully")
                if item_name in self.cart:
                    self.cart[item_name]+=count
                else:
                    self.cart[item_name]=count
                shoppingcart.items[item_name]-=count
    def removeitems(self):
        if bool (self.cart):
            item_name=input("Enter the item name :")
            if item_name  in self.cart:
                count=int(input("Enter the number of item to remove "))
                if self.cart[item_name]<count :
                    print("Not possible to remove")
                else:
                    print("remove successfully")
                    self.cart[item_name]-=count
                    shoppingcart.items[item_name]+=count
            else:
                print("This item is not present your cart ")
        else:
            print("your cart is empty you cannot remove ")
c=shoppingcart('krishna',9876543210)
c.main()

                
