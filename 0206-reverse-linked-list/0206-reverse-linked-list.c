struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode* temp = NULL;
    struct ListNode* current = head;
    struct ListNode* previous = NULL;
    
    while (current != NULL) {
        temp = current->next;  // Store next node
        current->next = previous;  // Reverse current node's pointer
        previous = current;  // Move previous to current node
        current = temp;  // Move to next node
    }
    
    head = previous;  // Head now points to the new first node
    return head;
}
