/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    struct compare {
    bool operator()(const ListNode* l, const ListNode* r) {
            return l->val > r->val;
        }
    };
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        priority_queue<ListNode *, vector<ListNode *>, compare> q;
        if(list1==NULL) return list2;
        if(list2==NULL) return list1;
        q.push(list1);
        q.push(list2);
        ListNode *ans = new ListNode(1000);
        ListNode *temp=ans;
        while(!q.empty())
        {
            ListNode *k = q.top();
            temp->next=k;
            temp=temp->next;
            q.pop();
            if(k->next!=NULL)
            {
                q.push(k->next);
            }
        }
        return ans->next;
        
    }
};