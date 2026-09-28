#include <iostream>
using namespace std;

bool good_time(long long t, int x, int y, int N){
	if ((N == 1) and (t >= min(x, y))){
		return true;
	}
	if (t < min(x, y)){
		return false;
	}
	if ((1 + (t - min(x,y))/x + (t - min(x,y))/y) >= N){
		return true;
	}
	else {
		return false;
	}
}


int main()
{
    int N, x, y;
    cin >> N >> x >> y;
    long long left = 0;
    long long right = N*min(x,y);
    while ((right-left)>1){
    	long long middle = (right + left)/2;
    	if (!good_time(middle, x, y, N)){
    		left = middle;
		} else {
			right = middle;
		}
	}

    cout << right; 
}