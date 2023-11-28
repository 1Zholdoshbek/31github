#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
    long long t,n,cnt=0;
    cin>>t;
    
    while(t--){
        cin>>n;
        if(n%2050!=0){
                cout<<-1<<"\n";
            }
        else{
            n=n/2050;
            while(n>0){
                cnt+=n%10;
                n/=10;
                
            }
            cout<<cnt<<"\n";
            cnt=0;
            }
       
    }
 
    return 0;
}