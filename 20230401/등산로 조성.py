from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
t = int(input())
for tc in range(1, 1+t):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    height = 0
    h_lst = [] # 최고 높이 봉우리 좌표 저장할 배열
    for h in arr: # 최고높이 봉우리 찾기
        temp = max(h)
        height = max(height, temp)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == height: # 해당 좌표가 최고높이 봉우리라면
                h_lst.append((i,j)) # h_lst에 저장
    for h in h_lst: # 최고높이 봉우리에서 하나씩 좌표 빼오기
        r, c = h
        temp_r = r
        temp_c = c
        for n in range(N):
            for m in range(N):
                if n == temp_r and m == temp_c: # 본인 좌표는 높이를 깎으면 안됨
                    continue
                for k in range(0, K+1): # 0 ~ k깊이까지 높이 깎아보기
                    arr[n][m] -= k
                    cnt = 0
                    q = deque()
                    q.append((temp_r,temp_c)) # 본인 좌표 넣고
                    while q:
                        size = len(q)
                        for _ in range(size):
                            r, c = q.popleft()
                            for d in range(4): # 상하좌우 더 낮은 높이 봉우리 담기
                                nr = r + dr[d]
                                nc = c + dc[d]
                                if 0 <= nr < N and 0 <= nc < N and arr[r][c] > arr[nr][nc]:
                                    q.append((nr, nc))
                        cnt += 1 # 한 칸씩 갈 때 cnt + 1 해주기
                    if cnt > max_num: # 최대 카운트가 최고 길이
                        max_num = cnt
                    arr[n][m] += k # 다시 산 깎은거 복원해주기
    print(f'#{tc} {max_num}')