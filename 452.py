def min_arrows(points):
    sorted_points = sorted(points, key=lambda p: p[1])
    a = 1; i = 1; cp = sorted_points[0]; size = len(sorted_points)
    while i < size:
        point = sorted_points[i]
        if point[0] > cp[1]:
            print('Point can\'t burst by prev arrow', point)
            a += 1
            cp = point
        else:
            print('Point can burst by prev arrow', point)
        i += 1
    return a
    


if __name__ == '__main__':
    print(min_arrows([[1,2],[2,3],[3,4],[4,5]]))
    print(min_arrows([[1,2],[3,4],[5,6],[7,8]]))
    print(min_arrows([[10,16],[2,8],[1,6],[7,12]]))
