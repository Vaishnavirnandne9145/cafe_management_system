#define the menu of restuarent
menu ={ 
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'cofee': 80, 
}
print (menu)
#we greet people 
print ( "welcome to restuarent")
print ("pizza : rs 40 \n pasta : 50 \n burger : 60 \n salad :70 \n cofee : 70")

order_total = 0 #user enter prize added on this var suppose salad then cofee 70+80=150
item_1= input("enter the name of item you want to order=")  #check conditions the choice entered by user is available
                                                              #in our restaurent or not if yes then go further if not then 
                                                              #it should display not available  

#membership operator we use here to check users input avalable or not
if item_1 in menu :
    order_total += menu [item_1]     #condition 1
# 0 + pasta (if) 0+50
["order table update for prize"]

print(f"your item { item_1} has been added to your order")
else : ( if user entered  )
 
print (f" ordered item { item_1} is not available yet !")
another_order = input ("do you want to add another item ? (yes/no)")

#condition add
if another_order =="yes" :
item_2 = input ("enter the name of second item if item_2 in menu")
order_total += 

