#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char *string[] = {"battleship", "boot", "cannon", "iron", "thinkable", "sorry"};

    char *word = NULL;
    printf("Enter a word: ");
    scanf("%ms", &word);

    int found = 0;
    char **ptr = string;
    while (*ptr != NULL)
    {
        if (strcmp(*ptr, word) == 0)
        {
            printf("Found\n");
            found = 1;
            break;
        }
        ptr++;
    }

    if (!found)
    {
        printf("Not found\n");
    }

    free(word);
    return 0;
}
