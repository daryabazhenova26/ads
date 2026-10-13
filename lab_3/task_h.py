import sys
from collections import deque


N = int(sys.stdin.readline())
l_dek = deque()
r_dek = deque()


for i in range(N):
    goblin = sys.stdin.readline().split()

    if goblin[0] == '+':
        r_dek.append(int(goblin[1]))
    elif goblin[0] == '-':
        print(l_dek.popleft())

    elif goblin[0] == '*':
        r_dek.appendleft(int(goblin[1]))

    if len(l_dek) < len(r_dek):
        l_dek.append(r_dek.popleft())
    elif len(l_dek) - len(r_dek) > 1:
        r_dek.appendleft(l_dek.pop())


