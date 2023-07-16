#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    char word[100];
    printf("Before: ");
    scanf("%s", word);

    for (int i = 0; i < strlen(word); i++)
    {
        printf("%c",toupper(word[i]));
    }
    printf("\n");
}