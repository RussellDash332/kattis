#include <stdio.h>
int main() {
    int num;
    scanf("%d", &num);
    if(num % 2 == 0)
        printf("Bob");
    else
        printf("Alice");
    
    return 0;
}