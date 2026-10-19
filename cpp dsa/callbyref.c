#include <stdio.h>

void modifyArray(int *arr[],int *i){
    for(i = 0; i<5;i++){
    if(*arr[i] % 2 == 0){
       printf("0");
    } else {
        printf("1");
    }
   }
}

int main(){
    int arr[5];
    int i;
    for(i = 0; i < 5 ; i++){
        printf("enter %d element : ",i);
        scanf("%d",&arr[i]);
    }
    for(int i = 0 ; i<5;i++){
        printf("%d",&arr[i]);
    }
}