import math

def find_max_number(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return (num1)
    elif num2 >= num1 and num2 >= num3:
        return (num2)
    else:
        return (num3)

def find_mean(num1, num2, num3):
    return (num1 + num2 + num3)/3

def find_mean_std(num1, num2, num3):
    mean = find_mean(num1, num2, num3)
    std = math.sqrt(((num1 - mean)** 2 + (num2 - mean)**2 + (num3 - mean)** 2) / 3)
    return (mean, std)


#num1, num2, num3 = 3, 8, 4
#funcshin = input("(1)-->find_max_number\n(2)-->find_mean\n(3)-->find_mean_std\n")

#if funcshin == "1":
#    print(find_max_number(num1, num2, num3))
#elif funcshin == "2":
#    print(find_mean(num1, num2, num3))
#elif funcshin == "3":
#    print(find_mean_std(num1, num2, num3))
#else:
#    print("error")
