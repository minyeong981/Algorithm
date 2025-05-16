#include <string>
#include <vector>
#include <numeric> // accumulate 함수 사용을 위해 필요

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    
    if (num_list.size() >= 11) {
        answer = accumulate(num_list.begin(), num_list.end(), 0);
    } else {
        answer = 1;
        for (int i = 0; i < num_list.size(); i++) {
            answer *= num_list[i];
        }
    }
    return answer;
}