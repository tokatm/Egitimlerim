#include <stdio.h>
#include <stdlib.h>

//Eleman alma ve elem an silme
/*  eleman alirke listeyi kontrol etmeli;
    -bos ise hem kuyrugun basi hem sonu bu elemani gostermeli.
    -dolu ise yeni elemani ekleyip kuyrugun sonunu guncellemeli. (FIFO geregi)

    eleman silerken, parametre almiyor cunku FIFO geregi.
    -bos mu kontrol etmeli. bos ise uyari versin.
    -dolu ise yeni kuyrugun ilk elemanini guncellesin.   
*/

struct node{
    int data;
    struct node *next;
};

struct node *front = NULL;
struct node *rear = NULL;

int enqueue(int data){
    
    
    
    if (front == NULL)
    {
        node *news = (node*)malloc(sizeof(node));
        news -> data = data;
        news -> next = NULL;
        front = rear = news;
        
    }

    else{
        node *news = (node*)malloc(sizeof(node));
        news -> data = data;
        news -> next = NULL;
        rear -> next= news;
        rear = news;
    }
    
}

int yazdir(){
    
    if (front == NULL)
    {
        printf("Queue is empty \n");
        return 1;
    }
    
    node *temp = front;

    while (temp != NULL)
    {
        printf("%d - ", temp->data);
        temp = temp -> next;
    }

    printf("\n");
    return 1;
    
}

//for delete

int dequeue(){

    if (front == NULL)
    {
        printf("Queue is empty");
        return 1;
    }

    node *t = front;
    front = front -> next;
    free(t);
    
}



int main(){
    enqueue(4);
    enqueue(45);
    enqueue(145);
    enqueue(5);
    yazdir();

    dequeue();
    yazdir();

    enqueue(26);
    yazdir();

    dequeue();
    yazdir();    

    dequeue();
    dequeue();
    dequeue();
    dequeue();

    return 1;
}