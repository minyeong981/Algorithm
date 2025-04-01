#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return *(int*)a - *(int*)b;
}

int main() {
    int n = 5, lst[5], sum = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &lst[i]);
        sum += lst[i];
    };

    qsort(lst, n, sizeof(int), compare);
    printf("%d\n%d", sum/n, lst[n/2]);
    return 0;
};