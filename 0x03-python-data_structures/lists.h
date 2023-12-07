#ifndef LISTS_H
#define LISTS_H

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data);
void insertNode(struct Node** head, int data);
void deleteNode(struct Node** head, int data);
void printList(struct Node* head);
void freeList(struct Node* head);

#endif // LISTS_H

