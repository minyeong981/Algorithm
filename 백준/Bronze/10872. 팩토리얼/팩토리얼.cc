#include <stdio.h>

int func(int x) {
    if (x == 0)
        return 1;
    else
        return x * func(x-1);
};

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d", func(n));
    return 0;
};