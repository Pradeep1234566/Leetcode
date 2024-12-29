#include <stdio.h>

void sum(int n)
{
    int sum;
    sum = (n * (n + 1)) / 2;
    printf("Sum of first %d natural numbers is %d\n", n, sum);
}
int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    sum(n);
}