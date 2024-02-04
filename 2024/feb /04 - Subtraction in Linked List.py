class Solution:
    def list_to_int(self,head):
        result = 0
        while head:
            result = result*10 + head.data
            head = head.next
        return result
            
    def subLinkedList(self, l1, l2): 
        list1 = self.list_to_int(l1)
        list2 = self.list_to_int(l2)
        
        ans = list1 - list2
        
        if(ans<0):
            ans = -(ans)
        
        ans_head = Node(0)
        ans_tail = ans_head
        
        for digit in str(ans):
            ans_tail.next = Node(int(digit))
            ans_tail = ans_tail.next
        return ans_head.next
        
