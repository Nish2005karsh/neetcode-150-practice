def cycle(head):
    # Using flyod tortoise and hare algorithm
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
        return False
head=[3,2,0,-4]
print(cycle(head))
    