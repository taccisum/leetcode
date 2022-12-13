

def assign_cookies(childs, cookies):
    pair = []
    sorted_childs = sorted(childs)
    sorted_cookies = sorted(cookies)
    print('sort childs & cookies:', sorted_childs, sorted_cookies)
    for cookie in sorted_cookies:
        print('try assign cookie: ', cookie)
        child = sorted_childs[0] if len(sorted_childs) > 0 else None
        if child is None:
            print('All child have had cookie.')
            break

        if cookie >= child:
            print('assign cookie to childe: ', cookie, child)
            pair.append([child, cookie])
            sorted_childs.remove(child)
        else:
            print('drop cookie:', cookie)
        print(cookie, pair, sorted_childs, sorted_cookies)
        
    return pair, len(pair)

def assign_cookies_max(childs, cookies):
    i = 0
    c = 0
    sorted_childs = sorted(childs)
    for cookie in sorted(cookies):
        if cookie >= sorted_childs[i]:
            c += 1; i += 1
    return c




if __name__ == '__main__':
    # print('assign result:', assign_cookies([1,2], [1,2,3]))
    print('assign result:', assign_cookies([3,6,1,2], [5,9,1,2,3]))
    print('assign result max:', assign_cookies_max([3,6,1,2], [5,9,1,2,3]))




