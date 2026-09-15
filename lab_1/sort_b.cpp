#include <iostream>
#include <vector>

using namespace std;

void InsertionSort(vector<int>& A) {
    int n = A.size();

    for (int i = 1; i < n; i++) {
        int current = A[i]; // элемент, который нужно поставить на нужное место
        int j = i - 1;

        // Сдвигаем вправо все элементы, которые больше current
        while (j >= 0 && A[j] > current) {
            A[j + 1] = A[j];
            j--;
        }

        // Ставим current на найденное место
        A[j + 1] = current;
    }
}

int main() {
    vector<int> A;
    int x;

    while (cin >> x) {
        A.push_back(x);
    }

    InsertionSort(A);

    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}