#include <iostream>
#include <vector>
#include <string>
#include <utility>
 
 using namespace std;
 
 class MinHeap {
 	private:
 		vector<int> heap;
 	
 	public:
 		
 		void insert(int x) {
 			heap.push_back(x);
 			int i = heap.size() - 1;
 			
 			while (i > 0) {
 				int parent = (i-1)/2;
 				if (heap[i] < heap[parent]) {
 					swap(heap[i], heap[parent]);
 					i = parent;
				}
				 else {
				 	break;
				}
			}
		}
		 
		int extract() {
		 	int minimum = heap[0];
		 	
		 	if (heap.size() == 1) {
		 		heap.pop_back();
		 		return minimum;
			}
			 
			heap[0] = heap.back();
			heap.pop_back();
			 
			int i = 0;
			 
			while (true) {
			 	int left = 2*i + 1;
			 	int right = 2*i + 2;
			 	int smallest = i;
			 	
			 	if (left < heap.size() && heap[left] < heap[smallest]){
			 		smallest = left;
			 	}
			 	if (right < heap.size() && heap[right] < heap[smallest]){
			 		smallest = right;
				}
			 	if (smallest == i) {
			 		break;
				}
				
				swap(heap[i], heap[smallest]);
				i = smallest;
			}
			
			return minimum;
		}
		
		void clear() {
			heap.clear();
		}
		
		bool isEmpty() {
			return heap.empty();
		}
};


int main() {
	MinHeap heap;
	string command;
	
	while (cin >> command) {
		if (command == "ADD") {
			int n;
			cin >> n;
			heap.insert(n);
		} else if (command == "EXTRACT"){
			if (heap.isEmpty()) {
				cout << "CANNOT\n";
			} else {
				cout << heap.extract() << '\n';
			}
		}
		else if (command == "CLEAR") {
			heap.clear();
		}
	}
	return 0;
}