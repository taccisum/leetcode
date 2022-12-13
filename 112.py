

def path_num(root, targetSum):
    """
    这里需要转成 TreeNode，否则类型不匹配原题
    """
    size = len(root)
    def each(tree, ci, sum, num):
        sum += tree[ci]
        if sum == num: return True
        if sum > num: return False
        n_l = ci * 2 + 1; n_r = ci * 2 + 2

        if n_l > size - 1:
            return False
        if each(tree, n_l, sum, num):
            return True

        if n_r > size - 1:
            return False
        if each(tree, n_r, sum, num):
            return True
        return False
    return each(root, 0, 0, targetSum)


if __name__ == '__main__':
    print(path_num([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22))
    print(path_num([1,2,3], 5))
