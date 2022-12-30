from typing import List


def find_max_min(nums):
    """
    同时寻找到最大值和最小值
    """
    max = -9999; min = 9999
    for n in nums:
        if n > max: max = n
        if n < min: min = n
    return max, min


def topKFrequentWithoutSorted(nums: List[int], k: int):
    """
    计算排序变种，不使用原生的 sorted 方法
    """
    max, min = find_max_min(nums)
    bucket = [0 for i in range(max - min + 1)]
    for n in nums: idx = n - min; bucket[idx]+=1

    new_bucket = [[] for i in range(find_max_min(bucket)[0])]
    for i in range(len(bucket)):
        v = i + min     # 原先数的值
        c = bucket[i]   # 该数出现的次数
        # 仅计出现次数不为 0 的数
        if c > 0: new_bucket[c-1].append(v)

    r = len(new_bucket)-1; res = []
    while len(res) < k:
        # 从右边开始取，取够 k 个数为止
        for i in new_bucket[r]:
            res.append(i)
            if len(res) == k: break
        r-=1

    return res



def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    计算排序变种
    """
    buckets = []
    max, min = find_max_min(nums)
    for i in range(max-min+1):
        buckets.append({
            'val': min+i,
            'count': 0
        })

    for n in nums:
        idx = n - min
        buckets[idx]['count']+=1

    return list(map(
            lambda obj: obj['val'],
            sorted(buckets, key=lambda obj: obj['count'], reverse=True)[0:k]
        ))


if __name__ == '__main__':
    print(topKFrequentWithoutSorted([4,1,-1,2,-1,2,3], 2))       # print -1, 2
    print(topKFrequentWithoutSorted([1,1,1,2,2,3], 2))       # print 1, 2
    print(topKFrequentWithoutSorted([7,7,7,7,2,2,3,4,4,4], 2))       # print 7, 4
    print(topKFrequentWithoutSorted([-1,-1], 2))       # print -1, -1
    # print(topKFrequent([1,1,1,2,2,3], 2))       # print 1, 2
    # print(topKFrequent([7,7,7,7,2,2,3,4,4,4], 2))       # print 7, 4
    # print(topKFrequent([-1,-1], 2))       # print 1, 2
