def reverseLinkedList(head):
    prev,curr=None,head
    while curr:
        nxt=curr.next
        curr.next=prev
        prev=curr
        curr=nxt
    return prev
head=[1,2,3,4,5]
print(reverseLinkedList(head))