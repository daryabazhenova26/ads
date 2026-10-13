class Dek:
    def __init__(self):
        self.data = []
    def push_front(self, n):
        return self.data.insert(0, n)
    def push_back(self, n):
        return self.data.append(n)
    def pop_front(self):
        if not self.data:
            return 'error'
        return self.data.pop(0)
    def pop_back(self):
        if not self.data:
            return 'error'
        return self.data.pop()
    def front(self):
        if not self.data:
            return 'error'
        return self.data[0]
    def back(self):
        if not self.data:
            return 'error'
        return self.data[-1]
    def size(self):
        return len(self.data)
    def clear(self):
        self.data.clear()


dek = Dek()

while True:
    command = input().split()
    if 'front' in command[0]:
        if 'push' in command[0]:
            dek.push_front(int(command[1]))
            print('ok')
        elif 'pop' in command[0]:
            print(dek.pop_front())
        else:
            print(dek.front())
    elif 'back' in command[0]:
        if 'push' in command[0]:
            dek.push_back(int(command[1]))
            print('ok')
        elif 'pop' in command[0]:
            print(dek.pop_back())
        else:
            print(dek.back())
    elif command[0] == 'size':
        print(dek.size())
    elif command[0] == 'clear':
        dek.clear()
        print('ok')
    elif command[0] == 'exit':
        print('bye')
        break


