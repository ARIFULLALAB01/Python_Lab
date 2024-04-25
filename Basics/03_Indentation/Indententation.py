number = 10
remainder = number % 2
if remainder == 0:
    print("even")
else:
    print("odd")

--
num = 15
if num >= 0:     
    print("im in if")
    if num == 0:         
        print("Zero")         
        print("im in if => if")
    else:         
        print("Positive number")         
        print("im in if => else")
else:     
    print("Negative number")    
    print("im in else")
    print("im outside")

---
number = 10
remainder = number % 2
if remainder == 0:    
    print("even")
else:    
    print("odd")
print("finished executing")