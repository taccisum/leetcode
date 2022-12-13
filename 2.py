def non_overlay_areas(areas):
    by_end_sorted_areas = sorted(areas, key=lambda a: a[1])
    ca = None
    removed = 0
    for a in by_end_sorted_areas:
        if ca is None:
            print('retain', a)
            ca = a
            continue
        """
        区间交叉的特点: a 的头小于 ca 的尾
        """
        if a[0] < ca[1]:
            print('remove', a)
            removed += 1
        else:
            print('retain', a)
            ca = a
    return removed

if __name__ == '__main__':
    print(non_overlay_areas([[1,2], [2,4], [2,3], [1,5], [3,6], [5,6], [4,5],[1,3]]))


