

def plant_flowers(flowerbed, n):
    def _print(*args, **kv):
        # print(*args, **kv)
        pass

    a = 0; i = 0; size = len(flowerbed)
    _print('The flower bed:', flowerbed)
    while i < size:
        slot = flowerbed[i]
        if i == (size - 1):
            if slot == 0:
                _print('Last Slot %d can plant flower, shut down' % i)
                a += 1
            break
        if slot == 1:
            _print('Slot is 1, Skip index', i, '+2')
            i += 2
        elif flowerbed[i+1] != 1:
            _print('Slot %d can plant flower, +2' % i)
            a += 1; i += 2
        else:
            _print('Next is %d, Skip index' % flowerbed[i+1], i, '+1')
            i += 1
    return a >= n


if __name__ == '__main__':
    print(plant_flowers([1,0,0,0,1], 1))
    print(plant_flowers([1,0,0,0,1], 2))
    print(plant_flowers([1,0,0,0,1,0,0], 2))