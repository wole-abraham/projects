def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
         sum = 3 * number + 1
         print(sum)
         return sum
    
def usingcollatz():
    try:
        user = int(input("Enter a interger: "))
    except ValueError:
        print("Enter a Valid interger! not a string ")
        usingcollatz()
    else:
     
        while True:
            user = collatz(user)
            if user == 1:
                 break

usingcollatz()
