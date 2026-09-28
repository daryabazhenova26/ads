#include <iostream>
#include <vector>
using namespace std;

bool good_lenght(long long lenght, int N, int K, vector<int>&A){
	
	long long count_strings = 0;
	
	int n = A.size();
	
    for (int i = 0; i < n; i++) {
    	count_strings += A[i]/lenght;
	}
	return count_strings >= K;
}


int main()
{
	int N, K;
	cin >> N >> K;
	
	vector<int> A;
    int x;
    for (int i = 0; i < N; i++) {
    	cin >> x;
        A.push_back(x);
    }
	
	long long left = 0;
	long long right = 1e7+1;
	
	while ((right-left)>1){
    	long long middle = (right + left)/2;
    	if (good_lenght(middle, N, K, A)){
    		left = middle;
		} else {
			right = middle;
		}
	}
	cout << left << "\n";
	return 0;
}