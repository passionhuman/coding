# N = 10
# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             print(i, j, k)

a = "112"
ans = 0
len_a = len(a)

for i in range(len(a)):
    cnt = 3 ** (len_a - 1)
    if cnt == 0:
        cnt = 1
    a_temp = int(a[i])
    ans += cnt * a_temp
    len_a -= 1
    print(cnt)
print(ans)