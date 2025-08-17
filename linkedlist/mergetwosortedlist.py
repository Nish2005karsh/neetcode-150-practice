def mergeTwoLists(list1,list2):
    dummy=ListNode()
    tail=dummy
    while list1 and list2:
        if(list1.val<list2.val):
            tail.next=list1
            list1=list1.next
        else:
            tail.next=list2
            list2=list2.next
        tail=tail.next
        if list1:
            tail.next=list1
        elif list2:
            tail.next=list2
    return dummy.next
list1=[1,2,4]
list2=[1,3,4]
print(mergeTwoLists(list1,list2))
    