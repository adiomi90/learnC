#include <stdio.h>
#include <string.h>

typedef struct 
{
    char *name;
    char  *number;
}
person;

int main(void)
{
    person people[2];
    people[0].name = "Particles";
    people[1].number = "7-977-278-2794";

    people[1].name = "Tikils";
    people[1].number = "233-246-07-29-07";

    char name[100];
    printf("Enter a name: ");
    scanf("%s",name);
    for (int i = 0; i < 2; i++)
    {
        if(strcmp(people[i].name, name) == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found");
    return 1;
}