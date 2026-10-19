#include <stdio.h>
#define SIZE 5

void enqueue(int arr[],int *front,int *rear,int value){
    if((*rear == SIZE - 1 && *front == 0)||(*front == *rear + 1)){
        printf("queue is full\n");
        return;
    }
    // FIRST ELEMENT
    if(*front == -1){
        *front = 0,*rear = 0;
        arr[*rear] = value;
        printf("Element added %d\n",arr[*rear]);
        return;
    }
    // FOR OTHER ELEMENTS
    *rear = (*rear + 1) % SIZE;
    arr[*rear] = value;
    printf("Element added %d\n",arr[*rear]);

}

int main(){
    int arr[SIZE];
    int front = -1;
    int rear = -1;
    enqueue(arr,&front,&rear,10);
    enqueue(arr,&front,&rear,20);
}