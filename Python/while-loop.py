# name=input("enter the name:")
# while name=="ram":
#     print("hello ram")
#     break


name=input("enter the name:")
list=["ram","shyam","hari"]
while (name in list):
    print(f"hello {name}")
    break

while True:
    name=input("Enter your name:")
    list=["ram","shyam","hari"]
    if name in list:
        print(f"hello {name}")
        break
    else:
        print("hello stranger")
    