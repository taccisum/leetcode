from math import floor
def sqrt(num):
    if num == 0: return 0
    if num == 1: return 1
    l=0; r=num; 

    while r > l:
        mid= floor((l+r)/2)
        if r - l == 1:
            break
        power = mid**2
        if power > num:
            r = mid
        elif power == num:
            break
        else:
            l = mid
    return mid

if __name__ == '__main__':
    print(sqrt(0))
    print(sqrt(1))
    print(sqrt(4))
    print(sqrt(9))
    print(sqrt(18))
    print(sqrt(36))

