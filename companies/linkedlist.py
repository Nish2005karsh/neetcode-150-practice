# Reverse a linked lisst
# def reverseList(head):
#     prev=None
#     curr=head
#     while curr:
#         nxt=curr.next
#         curr.next=prev
#         prev=curr
#         curr=nxt
#         head=prev
#     return head
# head=[1,2,3,4,5]
# print(reverseList(head))
# class ListNode:
#     def __init__(self):
#         self.val=val
#         self.next=next
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         fast,slow=head,head
#         while fast and fast.next:
#             slow=slow.next
#             fast=fast.next.next
#             if slow==fast:
#                 return True
#             return False

# Find the middle element of linked list
# def getLength(head):
#     # Count nodes in a linked list
#     length=0
#     while head:
#         length+=1
#         head=head.next
#     return length
#     def getMiddle(head):
#         length=getLength(head)
#         midIndex=length//2
#         while midIndex:
#             head=head.next
#             midIndex-=1
#         return head.data
