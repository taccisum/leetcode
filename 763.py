
def partition_labels(s):
    i = 0; last = {}
    for c in s:
        last[c] = i; i += 1

    i = 0; left = 0; right = 0; p = []
    for c in s:
        if last[c] > right:
            right = last[c]

        if i == right:
            p.append(right - left + 1)
            left = right + 1
        i += 1
    return p


if __name__ == '__main__':
    print(partition_labels('ababcbacadefegdehijhklij'))
    print(partition_labels('eccbbbbdec'))
