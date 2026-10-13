from collections import deque

player_1 = deque(map(int, input().split()))
player_2 = deque(map(int, input().split()))

cnt_moves = 0

while player_1 and player_2 and cnt_moves <= 10**6:
    f = player_1.popleft()
    s = player_2.popleft()
    if (f == 0) and (s == 9):
        player_1.append(f)
        player_1.append(s)
    elif (f == 9) and (s == 0):
        player_2.append(f)
        player_2.append(s)
    elif f > s:
        player_1.append(f)
        player_1.append(s)
    elif f < s:
        player_2.append(f)
        player_2.append(s)
    cnt_moves += 1
if cnt_moves > 10**6:
    print('botva')
elif player_1:
    print('first', cnt_moves)
else:
    print('second', cnt_moves)