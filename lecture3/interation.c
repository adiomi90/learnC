#include <stdio.h>

int draw(int n);

int main(void)
{
    int num;
    printf("Enter the height of the pyramid: ");
    scanf("%d", &num);

    draw(num);
}


int draw(int n)
{
    for (int i = 0; i < n; i++){
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");  
        }
        printf("\n");
    }

}