balls =  list(map(int, input().split()))
cnt_same = 1
cnt_destructed = 0
cur = 1
while cur < (len(balls)):
    cur_colour = balls[cur]
    next = cur + 1
    while (next < len(balls)) and (balls[cur] == balls[next]):
        cnt_same += 1
        next += 1
    if cnt_same >= 3:
        cnt_destructed += next - cur
        del balls[cur:next]
        cur = 1
    else:
        cur = next
    cnt_same = 1

print(cnt_destructed)


