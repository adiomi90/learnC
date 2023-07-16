#include <stdio.h>
#include <string.h>


int main(void)
{
    char *word[] = {"particles", "molecular", "since", "day", "one"};

    char *typed_word;
    printf("Enter a word");
    scanf("%s", typed_word);

    for (int i = 0; i < 5; i++)
    {
        if(strcmp(word[i], typed_word) == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not in the list\n");
    return 1;

}