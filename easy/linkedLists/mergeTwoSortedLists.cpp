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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        /* Return if at least one list is empty */
        if (l1 == NULL) {
            return l2;
        } else if (l2 == NULL) {
            return l1;
        }
        
        /* Initialize dummy node */
        ListNode head(0);

        /* Pointer cur points to tail of sorting list */
        ListNode* cur = &head;
        
        /* Point dummy node to node with smallest value.
         * If same value, point node to either.
         */
        ListNode* greater;
        if (l1->val <= l2->val) {
            head.next = l1;
            l1 = l1->next;
            greater = l2;
        } else {
            head.next = l2;
            l2 = l2->next;
            greater = l1;
        }
        cur = cur->next;
        
        /* Repeat above process to finding smallest node
         * value of the two lists until you exhaust either
         * list.
         */
        while (cur->next != NULL) {
            if (l1->val <= l2->val) {
                cur->next = l1;
                l1 = l1->next;
                greater = l2;
            } else {
                cur->next = l2;
                l2 = l2->next;
                greater = l1;
            }
            cur = cur->next;
        }
        cur->next = greater;
        return head.next;
    }
};