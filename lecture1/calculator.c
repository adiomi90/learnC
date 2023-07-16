#include <stdio.h>

int main(void)
{
    int n, y;
    printf("Enter the number to add");
    scanf("%d %d", &n, &y);

    float z = (float)n / (float)y;
    printf("%d", n + y);
    printf("float : %.2f", z);

    return 0;
}