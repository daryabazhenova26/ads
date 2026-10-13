class Stek:
    def __init__(self):
        self.data = []
    def push(self, n):
        self.data.append(n)
    def pop(self):
        if not self.data:
            return 'error'
        return self.data.pop()
    def back(self):
        if not self.data:
            return 'error'
        return self.data[-1]
    def size(self):
        return len(self.data)
    def clear(self):
        self.data.clear()



stek = Stek()

while True:
    command = input().split()
    if command[0] == 'push':
        stek.push(int(command[1]))
        print('ok')
    elif command[0] == 'pop':
        print(stek.pop())
    elif command[0] == 'back':
        print(stek.back())
    elif command[0] == 'size':
        print(stek.size())
    elif command[0] == 'clear':
        stek.clear()
        print('ok')
    elif command[0] == 'exit':
        print('bye')
        break