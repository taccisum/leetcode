def frequencySort(s: str) -> str:
    min=ord('0'); max=ord('z')
    max_count = 0; count_bucket = [0 for i in range(max-min+1)]
    for c in s:
        idx=ord(c)-min
        count_bucket[idx]+=1
        max_count=count_bucket[idx] if count_bucket[idx]>max_count else max_count

    new_bucket = [[] for i in range(max_count)]

    for i in range(len(count_bucket)):
        count=count_bucket[i]
        if count == 0: continue
        c=chr(i+min)
        new_bucket[count-1].append(c)
    
    new_str=[]; r=len(new_bucket)-1
    while r>=0:
        for c in new_bucket[r]:
            new_str.append(c*(r+1))     # 字符 c 重复出现了 r+1 次
        r-=1

    # return count_bucket, new_bucket, ''.join(new_str)
    return ''.join(new_str)

if __name__ == '__main__':
    print(frequencySort('tree'))
    print(frequencySort('cccaaa'))
    print(frequencySort('Aabb'))
    print(frequencySort('2a554442f544asfasssffffasss'))
    print(frequencySort('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUVVWWXXYYZZaabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz0011223344556677889'))
    