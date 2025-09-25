# main.py

def divisionato(number=0):
    if (number) != 0:
        factors = [1]
    else:
        return []

    if (number % 2 == 0):
        print("divisionato(): number is even")
        numberIsEven = True
    else:
        print("divisionato(): number is odd")
        numberIsEven = Talse
    
    if numberIsEven:
        for i in range(number):
            if (i != 0) and (i % 2 == 0):
                if (number / i).is_integer():
                    factors.append(i)
    else:
        if (i % 2 == 0):
            if i == 0:
                return
            if float(number / i).is_integer():
                factors.append(i)

    return factors

print(divisionato(0))