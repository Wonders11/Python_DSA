
from common import *

headOdd = createLLFromList([1,2,3,4,5])
headEven = createLLFromList([1,2,3,4,5,6])

print_LL(headOdd)
print_LL(headEven)

def middleOfLL(head):
    if(head is None or head.next is None): # LL is empty or has only one node
        return head
    
    length = lenthOfLL(head)
    middle = length//2

    temp = head
    count = 0

    while(count<middle):
        temp = temp.next
        count+=1
    
    return temp


# 2 pointer method (slow and fast pointer)
def middleOfLLUsingSlowAndFast(head):
    if(head is None or head.next is None):
        return head
    
    slow = head
    fast = head

    # concept is as fast reaches the end of the linked list, slow will be at the middle of the linked list
    # since the speed of fast is 2X of slow
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast = fast.next.next
    
    return slow # When fast reaches end, slow will be at middle


headOddMid = middleOfLLUsingSlowAndFast(headOdd)
headEvenMid = middleOfLLUsingSlowAndFast(headEven)

print(headOddMid.data)
print(headEvenMid.data)