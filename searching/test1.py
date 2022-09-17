def climbingLeaderboard(ranked, player):
  scores = sorted(list(set(ranked)), reverse = True)
  print(scores)
  result =[]
  for s in player:
    if s > scores[0]:
      result.append(1)
    elif s < scores[-1]:
      result.append(len(scores)+1)
    else:
      index = binsearch(scores, 0, len(scores),s)
      result.append(index)
  return result

  
def binsearch(arr, start, end, x):
  mid = 0
  while start <= end:
      mid = start + (end - start) // 2

      # if exist
      if arr[mid] == x:
          return mid + 1

      elif arr[mid] < x:
          end = mid - 1

      else:
          start = mid + 1

  return start + 1

ranked =[100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
print(climbingLeaderboard(ranked,player))