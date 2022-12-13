def detect_cycle(head):
    fast = head; slow = head
    while fast != slow:
        fast = fast.next.next
        slow = slow.next
    begin = head; meet = fast
    while begin != meet:
        begin = begin.next
        meet = meet.next
    return meet


    


if __name__ == '__main__':
    detect_cycle(None)