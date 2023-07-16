#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *string[] = {"battleship", "boot", "cannon", "iron", "thimble", "link"};

    char *word = (char *)malloc(30 * sizeof(char));
    if (word == NULL)
    {
        printf("Memory allocation failed. Exiting...\n");
        return 1;
    }

    printf("Enter a word: ");
    scanf("%s", word);

    for (int i = 0; i < 6; i++)
    {
        if (strcmp(string[i], word) == 0)
        {
            printf("Found\n");
            free(word); // Free dynamically allocated memory
            return 0;
        }
    }

    printf("Not found\n");
    free(word); // Free dynamically allocated memory
    return 1;
}
