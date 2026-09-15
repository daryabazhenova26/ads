#include <iostream>
#include <vector>

using namespace std;

void CountSort(vector<int>& A) {
    int count[101] = {0};

    // —читаем, сколько раз встречаетс€ каждое число
    for (int i = 0; i < A.size(); i++) {
        count[A[i]]++;
    }

    // «аполн€ем исходный вектор в отсортированном пор€дке
    int index = 0;

    for (int value = 0; value <= 100; value++) {
        for (int j = 0; j < count[value]; j++) {
            A[index] = value;
            index++;
        }
    }
}

int main() {
    vector<int> A;
    int x;

    while (cin >> x) {
        A.push_back(x);
    }

    CountSort(A);

    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}