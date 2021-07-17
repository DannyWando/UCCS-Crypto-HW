# Code implementation of the Euclidean algorithm
# Daniel Wandeler CS4920 HW2 Problem 4 and 5

def euclidean(num1, num2):
    while num2:
        tmp = num1
        num1 = num2
        num2 = tmp % num2
    return num1

def multInvextendedEuclid(num1, num2):
        if (euclidean(num1, num2) != 1):
            return 'DNE'
        initialMod = num2
        y = 0
        x = 1
        if (num2 == 1):
            return 0
        while (num1 > 1):
            quotient = num1 // num2
            tmp = num2
            num2 = num1 % num2
            num1 = tmp
            tmp = y
            y = x - quotient * y
            x = tmp
        if (x < 0):
            x = x + initialMod
        return x

if __name__ == '__main__':
    print('The GCD of 1005 and 425 is', euclidean(1005, 425)) #4A
    print('The GCD of 3555 and 12075 is', euclidean(3555, 12075)) #4B
    print('The GCD of 3278 and 9602 is', euclidean(3278, 9602)) #4C
    print('The GCD of 24142 and 16762 is', euclidean(24142, 16762)) #4D

    print('The multiplicative inverse of 650 mod 1869 is', multInvextendedEuclid(650, 1869)) #5A
    print('The multiplicative inverse of 1035 mod 3321 is', multInvextendedEuclid(1035, 3321)) #5B
    print('The multiplicative inverse of 9141 mod 39902 is', multInvextendedEuclid(9141, 39902)) #5C
    