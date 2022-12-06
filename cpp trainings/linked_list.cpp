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
        printf("Ilk. if calisti \n");

    }
    
    else{
        struct node *temp = (struct node *)malloc(sizeof(struct node));
        temp -> data = data;
        temp -> next = NULL;
        
        tail -> next = temp;
        tail = temp;
        printf("Ikinci. if calisti \n");
          
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
        printf("Ilk. if calisti \n");
    }

    else{
        node * temp = (node *)malloc(sizeof(node));
        temp -> data = data;
        temp -> next = head;

        head = temp;
        printf("ikinci . if calisti \n");
    }
    
}

int arayaEkle(int data){
    node *iter = head;
    int i = 0;
    for (i= 0; i < 3; i++)
    {
        iter = iter -> next;
    }  
    node *temp = (node *)malloc(sizeof(node));
    temp -> data = data;
    temp -> next = iter -> next;
    iter -> next = temp;
   
    return 1;

}

int sirali(int data){


    if (head == NULL)
    {
        node *temp = (node *)malloc(sizeof(node));
        temp -> next = NULL;
        temp -> data = data;
        printf("1. if calisti \n");
        return 1;
        
    }

    if (head -> data > data)
    {
        node *t = (node *)malloc(sizeof(node));
        t -> data = data;
        t -> next = head;
        head = t;
        printf("2. if calisti \n");
        return 1;
        

    }

    node *iter = head;
    
    while (iter -> next != NULL && iter -> next -> data < data)
    {
        iter = iter ->next;
    }
    node * temp = (node *) malloc(sizeof(node));
    temp -> next = iter -> next;
    iter -> next = temp;
    temp -> data = data;
    printf("normal calisti \n");
    return 1;
   
}

int yazdir(){

    node *index = head;
    while (index != NULL)
    {
        printf("%d - " , index->data);
        index = index -> next;
    }
    printf("\n");
    return 1;
}

//delete node

int deleted(int data){
    node *prev = NULL;
    node *temp = head;
    // linked list is empty
    if (head == NULL)
    {
        printf("Linked list is empty");
        printf("\n");
        return 1;
    }
    
    //delete process
    if (head -> data == data)
    {
        node *t = head;
        head = head -> next;
        free(t);
        printf("The requested data has been deleted.");
        printf("\n");
        return 1;
    }

    while (temp != NULL && temp ->data != data)
    {
        prev = temp;
        temp = temp -> next;
    }

    if (temp == NULL)
    {
        printf("data was not found");
        printf("\n");
        return 1;
    }
    
    prev -> next = temp ->next;

    if (tail -> data == data)
    {
        tail = prev;
    }
    
    free (temp);
    return 1;

    
    
       
    
}


int main(){
    addHeadList(35);
    addHeadList(542);
    addHeadList(24);
    addHeadList(52);
    addHeadList(15);
    addHeadList(48);
    sirali(45);
    sirali(6);
    sirali(54);
    sirali(455);
    sirali(450);
    sirali(41);
    yazdir();

    printf("bol\n");
    addEndList(100);
    addEndList(101);
    addEndList(99);
    addEndList(110);
    addEndList(105);
    sirali(200);
    sirali(201);
    sirali(198);
    sirali(204);
    yazdir();
    // addHeadList(1254);

    // arayaEkle(4512);
    // yazdir();
    // deleted(0);
    // yazdir();
}
