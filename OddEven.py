def OddEven(num):
    if num%2 == 0 :
        print(f"{num} is a even number")
    else:
        print(f"{num} is a odd number")

while True:
    number = int(input("Enter a number:"))
    OddEven(number)