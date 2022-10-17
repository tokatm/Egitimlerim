#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node * next;
};

struct node * head = NULL;
struct node * tail = NULL;

// add to list a member

int addEndList(int data){

    if (head == NULL)
    {
        struct node *temp = (struct node *)malloc(sizeof(struct node));
        temp -> data = data;
        temp -> next = NULL;
        head = tail = temp;

    }
    
    else{
        struct node *temp = (struct node *)malloc(sizeof(struct node));
        temp -> data = data;
        temp -> next = NULL;
        
         tail -> next = temp;
         tail = temp;
          
    }
    return 1;
}

int addHeadList(int data){

    if (head == NULL)
    {
        node * temp = (node *)malloc(sizeof(node));
        temp -> data = data;
        temp -> next = NULL;
        head = tail = temp;
    }

    else{
        node * temp = (node *)malloc(sizeof(node));
        temp -> data = data;
        temp -> next = head;

        head = temp;
    }
    
}

int yazdir(){

    node *index = head;
    while (index != NULL)
    {
        printf("%d - ", index->data);
        index = index -> next;
    }
    return 1;
}

int sirala(data)
{
    
    node * iter = (node *)malloc(sizeof(node));
    while (iter -> next != NULL && iter -> next -> data < data)
    {
        iter = iter -> next;
    }

    node *temp = (node*) malloc(sizeof(node));
    temp -> next = iter -> next;
    iter -> next = temp;
    temp -> data = data ;


    
}


int main(){

    addEndList(35);
    addEndList(5);
    addEndList(24);
    addEndList(52);
    addEndList(15);
    addEndList(48);

    addHeadList(1254);
    yazdir();
    
    return 1;
}
