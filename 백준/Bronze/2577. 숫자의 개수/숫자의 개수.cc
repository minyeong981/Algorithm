#include <stdio.h>

int main() {
    int num = 1;
    int lst[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    for (int i = 0; i < 3; i++) {
        int temp;
        scanf("%d", &temp);
        num *= temp;
    };
    
    while (num != 0) {
        lst[num % 10] += 1;
        num /= 10;
    };
    
    for (int j = 0; j < 10; j++) {
        printf("%d\n", lst[j]);
    };

    return 0;
}