print('=====WELCOME TO THE SMART SHOPPING COUNTER=====')
print('Add Items To Your Cart. Type "done" When You Are Finished.')
cart=[]
while True:
    item=input('Enter Item or Type "done" to Finish:')
    if item.lower()=='done':
        print('=====Closing Shopping Counter=====')
        break
    else:
        cart.append(item)
        print("Item Added To Your Cart:", item)
number_of_items=len(cart)
print("Total NUmber Of Items In Your Cart:", number_of_items)
print("Items in Your Cart:", *cart)
item_number=1
for item in cart:
    print(f"{item_number}.{item}")
    item_number+=1
print("=====THANK YOU FOR SHOPPING WITH US=====")

    

