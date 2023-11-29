#include<bits/stdc++.h>
using namespace std;
int Check(int a,int b){
    if(a%b==0) return b;
    if(b%a==0) return a;
    if(a>b)
        return Check(a%b,b);
    return Check(a,b%a);
    
}
int main (){
    int a,b;
    cin>>a>>b;
    a=max(a,b);
    int m = 6-a+1;
    cout<<m/Check(m,6)<<"/"<<6/Check(6,m);
    
}