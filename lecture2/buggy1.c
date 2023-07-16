#include <stdio.h>


int get_negative_int(void);

int main(void)
{
    int i = get_negative_int();
    printf("you entered %i\n",i);
}


int get_negative_int(void)
{
    int n;
    do
    {
        printf("Enter a negative integer");
        scanf("%d",&n);
    }
    while (n >= 0);
    return n;
}