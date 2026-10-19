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
    for(int i = 0 ; i < n-1 ; i ++){
            int diff = arr[i] - arr[i+1];
            if(diff<0){
                diff = -diff;
            } 
            cout<<diff<<endl;
        }
    }
