#ifndef LISTS_H
#define LISTS_

#include <stdlib.h>

/**
 * structs LISTS_H - linked list
 * @n: integer
 * next: point to the next node 
 *
 * Description: linked list node structure
 */

/*structure definition of a node in a linked list*/
typedef struct Node {
    int data;
    struct Node* next;
} Node;

/*prototypes functions*/
Node* createNode(int data);
void appendNode(Node** head, int data);
void printList(Node* head);

endif /*LISTS_H*/
