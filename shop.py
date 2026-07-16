
#append
items = ["minecraft","uncharted","counter strike","valorant"]
soorat_hesab = 0
while True:
    user_item = input("What Game Do You Want? ")
    if user_item in items:
        print("Sefaresh Sabt Shod")
        if user_item == "minecraft":
            soorat_hesab+=100
            print(soorat_hesab)
            
    elif user_item == "exit":
        break
    else:
        print("item Not Found")