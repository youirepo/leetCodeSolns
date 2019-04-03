/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == NULL) return false;
        
        /* Two pointers, one fast and one slow */
        ListNode* fast = head->next;
        ListNode* slow = head;
        
        /* Traverse list until pointers meet */
        while (fast != NULL && fast->next != NULL) {
            if (fast == slow) return true;
            fast = fast->next->next;
            slow = slow->next;
        }
        /* List does not have cycle, pointers don't meet */
        return false;
    }
};