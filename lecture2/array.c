#include <stdio.h>

float get_scores(int score_count, int array[]);
int array_size(void);

int main(void)
{
    int const N = array_size();
    int array[N];
    float result =  get_scores(N, array);
    printf("The average of the array is %.2f\n",result);
   
    
}


float get_scores(int score_count, int array[])
{
    int sum = 0;
    
    for (int i = 0; i < score_count; i++)
    {
        printf("Enter your number: ");
        scanf("%d", &array[i]);
        sum += array[i];
    }
return sum/(float)score_count;
}

int array_size(void)
{
    int array_size; 
    printf("Enter the length of your array: ");
    scanf("%d", &array_size);
    
    return array_size;
}