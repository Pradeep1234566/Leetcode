#include<stdio.h>

int main()
{
    int n;
    scanf("%d", &n); // Reading the number of rows and columns
    for(int i = 0; i < n; i++) // Outer loop for rows
    {
        for(int j = 0; j < n; j++) // Inner loop for columns
        {
            printf("*");
        }
        printf("\n"); // Move to the next line after each row
    }
    return 0;
}
