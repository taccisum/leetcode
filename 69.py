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


def sqrt_newton(num):
    # f(x) = x^2 - num = 0
    # f'(x) = 2x
    # 起始点为 x_0，所求目标点为 x_1 = x_0 - f(x_0) / f'(x_0) = (x_0 +　num / x_0) / 2
    x0 = num

    while x0 ** 2 > num:
        x0 = floor(x0 / 2 + num / (2 * x0))

    return x0

if __name__ == '__main__':
    # print(sqrt(0))
    # print(sqrt(1))
    # print(sqrt(4))
    # print(sqrt(9))
    # print(sqrt(18))
    # print(sqrt(36))

    print(sqrt_newton(9))
    print(sqrt_newton(18))
    print(sqrt_newton(36))

