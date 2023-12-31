#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main(int argc, char *argv[])
{

    node *list = NULL;

    for (int i = 1; i < argc; i++)
    {
    int number = atoi(argv[i]);

    node *num = malloc(sizeof(node));
    if(num == NULL){
        return 1;
    }

    num->number = number;
    num->next = NULL;

    num->next = list;
    list = num;
    }
    node *ptr = list;
    while(ptr != NULL)
    {
        printf("%i\n", ptr->number);
        ptr = ptr ->next;
    }
}