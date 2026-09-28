#include <iostream>
#include <vector>
using namespace std;

bool good_size(long long size, int n, long long w, long long h){
	if ((size/w) * (size/h) >= n){
		return true;
	}
	return false;
}


int main()
{
	long long w, h, n;
	cin >> w >> h >> n;
	
	long long left = 1;
	long long right = n*max(w, h);
	
	while ((right - left) > 1){
		long long middle = (right + left) / 2;
		if (good_size(middle, n, w, h)){
			right = middle;
		} else {
			left = middle;
		}
	}
	cout << right;
	return 0;
}