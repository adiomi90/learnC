#include <stdio.h>

int draw(int n);

int main(void)
{
    int num;
    printf("Enter the height of your pyramid: ");
    scanf("%d", &num);
    draw(num);
}

int draw(int n)
{
    if(n == 0)
        return;

    draw(n -1);

    for (int i = 0; i < n; i++)
    {
        printf("#");
    }
    printf("\n");
}