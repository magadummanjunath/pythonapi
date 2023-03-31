cart = []
def addToCart(item): #Function declaration
  cart.append(item)
  print("empty cart")


print(cart)

addToCart("apple")  #function calling and passing value
addToCart("pineapple")  

print(cart)

def removeFromCart(item):  ##function declaration
  cart.remove(item)

removeFromCart("apple")
print(cart)  



items={"apple":100,"orange":10,"banana":20}

# print(len(items))

for fruit in items:
  print(fruit)

print(items["apple"]) #prints value of apple key



kart = []
def addToKart(item):
  kart.append(item)

addToKart("Hi") 
addToKart("hello")

print(kart)

def removeFromkart(item):
   kart.remove(item)

removeFromkart("hello")
print(kart)
#-------------------------------------------------------------------------------------
