#include <iostream>
#include <vector>

using namespace std;

int BubbleSort(vector<long long>& A) {
    int n = A.size();
    int count = 0;

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {

            if (A[j] > A[j + 1]) {
                swap(A[j], A[j + 1]);
                count++;
            }
        }
    }

    return count;
}

int main() {
    int N;
    cin >> N;

    vector<long long> A(N);

    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }

    cout << BubbleSort(A);

    return 0;
}