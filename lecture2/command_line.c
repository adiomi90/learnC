#include <stdio.h>

int main(int argc, char *argv[1])
{
 if (argc == 2)
    printf("Hello, %s\n", argv[1]);
else
    printf("Hellow, world\n");
}