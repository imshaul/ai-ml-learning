#include <stdio.h>

int main(){
    int n = 5,i = 0;
    int stack[n];
    char brackets[100];
    printf("Enter brackets : ");
    scanf("%s",brackets);
    for(int j = 0;brackets[j] != '\0' ; j++){
        if(brackets[j] == '('){
            stack[i] = '(';
            i++;
    }
    else if (brackets[j] == ')'){
        if (i == 0){
            printf("Not balanced");
        } i--;
    }
    }
    if(i==0){
        printf("Balanced");
    } else{
        printf("Not Balanced");
    }
        
}
