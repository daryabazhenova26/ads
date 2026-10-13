class Queue:
    def __init__(self):
        self.data = []
    def push(self, n):
        self.data.append(n)
    def pop(self):
        if not self.data:
            return 'error'
        return self.data.pop(0)
    def front(self):
        if not self.data:
            return 'error'
        return self.data[0]
    def size(self):
        return len(self.data)
    def clear(self):
        self.data.clear()


queue = Queue()

while True:
    command = input().split()
    if command[0] == 'push':
        queue.push(int(command[1]))
        print('ok')
    elif command[0] == 'pop':
        print(queue.pop())
    elif command[0] == 'front':
        print(queue.front())
    elif command[0] == 'size':
        print(queue.size())
    elif command[0] == 'clear':
        queue.clear()
        print('ok')
    elif command[0] == 'exit':
        print('bye')
        break