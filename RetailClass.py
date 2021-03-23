# Retail Class
# Due 03/23/2021

class Account:

    def __init__(self, name, accNum):
        self.account = {}
        self.account.update({name: accNum})
        self.shopList = {}

    def printShopList(self):
        print("Item", "      ", "Price")
        for x, y in self.shopList.items():
            print(x, '       ', "$", y)

        print()

    def addItem(self, name, price):
        self.shopList.update({name: price})

    def removeItem(self, itemName):
        for x in self.shopList.keys():
            if x == itemName:
                del self.shopList[itemName]
                break

    def purchase(self):
        total = int(0)
        for x in self.shopList.values():
            total += x

        self.printShopList()
        print("Total Price: $", total)


class Store:

    def __init__(self):
        self.storeItems = {
            "Fortnite Gift Card": 19,
            "Disney x Gucci Donald Duck small backpack": 1980,
            "GG canvas bucket hat":590,
            "Men's Ultrapace R sneaker": 890,
            "Disney x Gucci Donald Duck striped wool sweater":1250,
            "Disney x Gucci Donald Duck eco washed denim vest":1980,
            "Ken Scott print jogging pant":1250,
            "Ken Scott print cotton shorts":520,
            "Men's thong sandal with Web":590,
            "GG canvas jacket":3500,
            "Eco washed organic denim bomber jacket":3900,
            "Eco washed GG denim shorts":980,
            "Eco washed GG denim pant":1400,
            "G Square stripe fil coupé cotton shirt":680,
            "Double G jacquard wool V-neck sweater":890,
            "Velvet flare pant":1250,
            "Gucci jacquard striped cotton polo":690,
            "Alpaca wool jacquard cardigan":2500,
            "Cotton pant with Interlocking G patch":980,
            "GG stretch cotton polo":1150,
            "'Fake/Not' print GG nylon jacket":1800,
            "'Fake/Not' print sweatshirt":1100,
            "The North Face logo x Gucci Web print silk shorts":980,
            "The North Face x Gucci Web print silk shirt":1250,
            "The North Face x Gucci Web print cotton sweatshirt":1400,
            "The North Face x Gucci print cotton T-shirt":650,
            "Online Exclusive The North Face x Gucci jersey jogging pant":1300,
            "Online Exclusive The North Face x Gucci jersey jacket":1800,
            "The North Face x Gucci nylon shorts":830,
            "Doraemon x Gucci cotton sweatshirt":1250,
            "Doraemon x Gucci oversize T-shirt":650,
            "Doraemon x Gucci cotton sweatshirt":1450,
            "Padded nylon zip-up jacket":1800,
            "Disney x Gucci Donald Duck T-shirt":890,
            "Disney x Gucci Donald Duck crop sweatshirt":1200,
            "Gucci Prodige d'Amour print sweatshirt":1250,
            "Double G stripe wool jacket":3200,
            "Check wool coat with Gucci label":2800,
            "GG jacquard nylon padded coat":2800
        }

    def printStore(self):
        print("#", "Item", "      ", "Price")
        count = int(1)
        for x, y in self.storeItems.items():
            print(count, x, '       ', "$", y)
            count += 1


def buy(acc, num):
    if num == 1:
        acc.addItem("Fortnite Gift Card", 19)
    elif num == 2:
        acc.addItem("Disney x Gucci Donald Duck small backpack", 1980)
    elif num == 3:
        acc.addItem("GG canvas bucket hat", 590)
    elif num == 4:
        acc.addItem("Men's Ultrapace R sneaker", 890)
    elif num == 5:
        acc.addItem("Disney x Gucci Donald Duck striped wool sweater", 1250)
    elif num == 6:
        acc.addItem("Disney x Gucci Donald Duck eco washed denim vest", 1980)
    elif num == 7:
        acc.addItem("Ken Scott print jogging pantt", 1250)
    elif num == 8:
        acc.addItem("Ken Scott print cotton shorts ", 520)
    elif num == 9:
        acc.addItem("Men's thong sandal with Web", 590)
    elif num == 10:
        acc.addItem("GG canvas jacket", 3500)
    elif num == 11:
        acc.addItem("Eco washed organic denim bomber jacket", 3900)
    elif num == 12:
        acc.addItem("Eco washed GG denim shorts", 980)
    elif num == 13:
        acc.addItem("Eco washed GG denim pant", 1400)
    elif num == 14:
        acc.addItem("G Square stripe fil coupé cotton shirt", 680)
    elif num == 15:
        acc.addItem("Double G jacquard wool V-neck sweater ", 890)
    elif num == 16:
        acc.addItem("Velvet flare pant", 1250)
    elif num == 17:
        acc.addItem("Gucci jacquard striped cotton polo ", 690)
    elif num == 18:
        acc.addItem("Alpaca wool jacquard cardigan", 2500)
    elif num == 19:
        acc.addItem("Cotton pant with Interlocking G patch", 980)
    elif num == 20:
        acc.addItem("GG stretch cotton polo", 1150)
    elif num == 21:
        acc.addItem("'Fake/Not' print GG nylon jacket", 1800)
    elif num == 22:
        acc.addItem("'Fake/Not' print sweatshirt", 1110)
    elif num == 23:
        acc.addItem("The North Face logo x Gucci Web print silk shorts", 980)
    elif num == 24:
        acc.addItem("The North Face x Gucci Web print silk shirt", 1250)
    elif num == 25:
        acc.addItem("The North Face x Gucci Web print cotton sweatshirt", 1400)
    elif num == 26:
        acc.addItem("The North Face x Gucci print cotton T-shirt", 650)
    elif num == 27:
        acc.addItem("Online Exclusive The North Face x Gucci jersey jogging pant  ", 1300)
    elif num == 28:
        acc.addItem("Online Exclusive The North Face x Gucci jersey jacket", 1800)
    elif num == 29:
        acc.addItem("The North Face x Gucci nylon shorts", 830)
    elif num == 30:
        acc.addItem("Doraemon x Gucci cotton sweatshirt", 1450)
    elif num == 31:
        acc.addItem("Doraemon x Gucci oversize T-shirt ", 650)
    elif num == 32:
        acc.addItem("Padded nylon zip-up jacket", 1800)
    elif num == 33:
        acc.addItem("Disney x Gucci Donald Duck T-shirt", 890)
    elif num == 34:
        acc.addItem("Disney x Gucci Donald Duck crop sweatshirt", 1200)
    elif num == 35:
        acc.addItem("Gucci Prodige d'Amour print sweatshirt", 1250)
    elif num == 36:
        acc.addItem("Double G stripe wool jacket", 3200)
    elif num == 37:
        acc.addItem("Check wool coat with Gucci label", 2800)
    elif num == 38:
        acc.addItem("GG jacquard nylon padded coat ", 2800)


# This is the main driver

print("Welcome new customer!")
gucci = Store()
user = input("Enter your name to enter the store : ")
account = Account(user, "00001")

intent = int(0)
print("Welcome to the Gucci Store!")

gucci.printStore()
intent = int(input("Enter Item # you want to buy (0 exit): "))
while intent != 0:
    buy(account, intent)
    intent = int(input("Enter Item # you want to buy (0 exit): "))

print("Your Shopping Cart:")
account.printShopList()


intent = int(input("Would You like to remove an item(1 for yes, 0 for no): "))

while intent != 0:
    item = input("Enter Item Name you wish to remove: ")
    account.removeItem(item)
    intent = int(input("Would You like to remove an item(1 for yes, 0 for no): "))

print("Time to complete your purchase.")
account.purchase()
