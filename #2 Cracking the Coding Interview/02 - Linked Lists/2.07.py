'''
Question: 2.7 Intersection: Given two (singly) linked lists, determine if the two lists intersect. 
Return the intersecting node. Note that the intersection is defined based on reference, not value. 
That is, if the kth node of the first linked list is the exact same node (by reference) as the j t h node of the second linked list, then they are intersecting.

Thoughts:
Try to draw this through:

  1->2->3->4->5

  0->0->3->4->5

If they intersect, the lists would merge and the end will be one. i.e all the values after intersection will be same.

Thoughts.. 
#1: if list are of same length, its easy coz you could traverse and compare, as soon as they collides, nodes will match up.. 
#2: since the list length could be different, how about traversing from back? go till the end and traverse back and find the split, but its not doubly linked list :(

Solution: Run till the end and find out the lengths.. then start the longer one from the place where the smaller is from.. and use the #1 above.


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ptr1 = headA
        ptr2 = headB
        counta = countb = 0
        while(ptr1 or ptr2):
            if ptr1:
                counta+=1
                ptr1 = ptr1.next
            if ptr2:
                countb+=1
                ptr2 = ptr2.next
        # Ran till the end and found the count of both lists


        # Setting up the ptrs in the same spot, specifically jumping for the
        # longer one  
        if counta<countb:
            count = 0
            diff = countb-counta
            while(count<diff):
                count+=1
                headB = headB.next
        elif countb<counta:
            count = 0
            diff = counta-countb
            while(count<diff):
                count+=1
                headA = headA.next
                
        while(headA):
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next
        return None
                
            
            
            