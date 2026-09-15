#include <iostream>
#include <vector>

using namespace std;

// Функция сортировки выбором
void SelectionSort(vector<int>& A) {
    int n = A.size();

    for (int i = 0; i < n - 1; i++) {
        int maxIndex = i; // индекс максимального элемента

        // Ищем максимальный элемент в оставшейся части списка
        for (int j = i + 1; j < n; j++) {
            if (A[j] > A[maxIndex]) {
                maxIndex = j;
            }
        }

        // Меняем текущий элемент с максимальным
        swap(A[i], A[maxIndex]);
    }
}

int main() {
    vector<int> A;
    int x;

	
    // Считываем числа до конца ввода
    while (cin >> x) {
        A.push_back(x);
    }

    SelectionSort(A);

    // Вывод отсортированного списка
    for (int i = 0; i < A.size(); i++) {
        cout << A[i] << " ";
    }

    return 0;
}