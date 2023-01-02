def safe_direction4(i, j, height, width):
    """
    返回上下左右四个方向的坐标（自动剔除越界坐标）
    """
    d=[]
    if i > 0: d.append((i-1, j))    # up i-1, j
    if i < height-1: d.append((i+1, j))     # down i+1, j
    if j > 0: d.append((i, j-1))    # left i, j-1
    if j < width-1: d.append((i, j+1))      # right i, j+1
    return d