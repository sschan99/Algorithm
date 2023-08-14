n = int(input())

result = 0

is_used_1 = [False] * n
is_used_2 = [False] * (2 * n - 1)
is_used_3 = [False] * (2 * n - 1)

def dfs(row):
  global result
  
  if row == n:
    result += 1
    return

  for col in range(n):
    if is_used_1[col] or is_used_2[row + col] or is_used_3[row - col + n - 1]:
      continue
    is_used_1[col] = True
    is_used_2[row + col] = True
    is_used_3[row - col + n - 1] = True
    dfs(row + 1)
    is_used_1[col] = False
    is_used_2[row + col] = False
    is_used_3[row - col + n - 1] = False

dfs(0)
print(result)
