#include <iostream>
using namespace std;

int main(){
    int n;
    cout<<"enter the size of array : ";
    cin>>n;
    int arr[n];
    for(int i = 0;i<n;i++){
        cout<<"enter "<<i+1<<" number array : "; 
        cin>>arr[i];
    }
    for(int i = 0 ; i < n ; i++){
        int flag = 0;
        int count = 1;
        for (int j = 0 ; j < i ;  j++) {
            
            if (arr[i] == arr[j]){
                flag = 1;
                break;
                
            }
        }
        if (flag == 0){
            for(int j = i+1 ; j < n ; j ++){
                if(arr[i]==arr[j]){
                    count++;
                }
            }
                cout << arr[i] <<" occurs " <<count <<" times"<<endl;
            }
         }
     }

