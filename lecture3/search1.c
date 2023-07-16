#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char *string[] = {"battleship", "boot", "cannon", "iron", "thimble","link"};

    char *word = malloc(30 * sizeof(char));
    printf("Enter a word: ");
    scanf("%s", word);

    char **ptr = string; // Pointer to the first element of the array
    while (*ptr != NULL) // Iterate until reaching the end of the array (marked by a NULL pointer)
    {
        if(strcmp(*ptr, word) == 0)
        {
            printf("Found\n");
            free(word); // Free the dynamically allocated memory
            return 0;
        }
        ptr++; // Move to the next element in the array
    }
    printf("Not found\n");
    free(word); // Free the dynamically allocated memory
    return 1;
}
