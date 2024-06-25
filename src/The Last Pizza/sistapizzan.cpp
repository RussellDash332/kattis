#include<iostream>
int n,a,x;main(){std::cin>>n;for(int i;i<n;i++){std::cin>>x;a+=(2-n+x)%2;}std::cout<<(a?"Ja":"Nej");}