#include <iostream>
 
using namespace std;
 
int main()
{
    int n,a,b,sum1=0,sum2=0;
    cin>>n;
    while(n--){
        cin>>a>>b;
        if(a>b)sum1++;
        if(b>a)sum2++;
    }
    if(sum1==sum2){
            cout<<"Friendship is magic!^^";
        }
        else if(sum1>sum2){
            cout<<"Mishka";
        }
        else{
            cout<<"Chris";
        }
    return 0;
}