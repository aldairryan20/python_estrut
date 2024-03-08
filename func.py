def sumImpar(k):
    if k<10:
        if k%2 == 0:
            return 0
        else:
            return k
    else:
        if k%2 == 0:
            return sumImpar(k//10)
        else:
            return sumImpar(k//10) + k%10
# print(sumImpar(123456789))
# >>> 25

