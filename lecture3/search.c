#include <stdio.h>
#include <string.h>

int main(void)
{
    char *string[] = {"battleship", "boot", "cannon", "iron", "thimble","link"};

    char word[30];
    printf("Enter a word: ");
    scanf("%s", word);

    for (int i = 0; i < 6; i++)
    {
        if(strcmp(string[i], word) == 0)
        {
            printf("Found \n");
            return 0;
        }
    }
    printf("Not found \n");
    return 1;
}