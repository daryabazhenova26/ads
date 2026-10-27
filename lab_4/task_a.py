class Heap:
    def __init__(self):
        self.heap = []
    # добавить в Heap число k (1 ≤  k ≤ 1000000) ;
    def Insert(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
        while i > 0:
            parent = (i-1)//2
            if self.heap[i] > self.heap[parent]:
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break
    # достать из Heap наибольшее число (удалив его при этом).
    def Extract(self):
        maximum = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
            return maximum

        self.heap[0] = self.heap.pop()
        i = 0
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == i:
                break
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            i = largest
        return maximum



heap = Heap()
N = int(input())
for i in range(N):
    command = list(map(int, input().split()))
    if command[0] == 0:
        heap.Insert(command[1])
    if command[0] == 1:
        maximum = heap.Extract()
        print(maximum)