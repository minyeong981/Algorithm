#include <stdio.h>
#include <string.h>

int queue[10000];  // 큐 저장 배열
int front = 0, back = 0;  // 큐의 앞/뒤 포인터

int main() {
    int n;
    scanf("%d", &n);

    while (n--) {
        char cmd[10];  // 명령어 문자열 저장
        scanf("%s", cmd);

        if (strcmp(cmd, "push") == 0) {
            int x;
            scanf("%d", &x);
            queue[back++] = x;  // 뒤에 값을 추가하고 back 증가
        } else if (strcmp(cmd, "pop") == 0) {
            if (front == back) printf("-1\n");  // 비어 있음
            else printf("%d\n", queue[front++]);  // 앞에서 꺼냄
        } else if (strcmp(cmd, "size") == 0) {
            printf("%d\n", back - front);  // 큐에 있는 요소 수
        } else if (strcmp(cmd, "empty") == 0) {
            printf("%d\n", front == back ? 1 : 0);  // 비어 있으면 1
        } else if (strcmp(cmd, "front") == 0) {
            if (front == back) printf("-1\n");
            else printf("%d\n", queue[front]);
        } else if (strcmp(cmd, "back") == 0) {
            if (front == back) printf("-1\n");
            else printf("%d\n", queue[back - 1]);
        }
    }

    return 0;
}
