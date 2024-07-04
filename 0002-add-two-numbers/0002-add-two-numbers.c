struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) 
{   
    struct ListNode* result = (struct ListNode*)malloc(sizeof(struct ListNode));
    result= NULL;
    struct ListNode* cur = result;
    int c = 0, sum = 0, k;

    while (l1 != NULL || l2 != NULL || c != 0) {
        sum = c;
        
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }
        
        c = sum / 10;
        k = sum % 10;
        
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = k;
        newNode->next = NULL;
        
        if (result == NULL) {
            result = newNode;
            cur = result;
        } else {
            cur->next = newNode;
            cur = cur->next;
        }
    }
    return result; // Skip the dummy node and return the actual result list
}