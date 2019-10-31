# -*- condig:utf-8 -*-

def findTheSame(list_a, list_b):
  list_a = sorted(list_a)
  list_b = sorted(list_b)
  count_a = 0
  count_b = 0
  list_c = []
  while (count_a < len(list_a) and count_b < len(list_b)):
    if list_a[count_a] > list_b[count_b]:
      count_b += 1
    elif list_a[count_a] < list_b[count_b]:
      count_a += 1
    elif list_a[count_a] == list_b[count_b]:
      list_c.append(list_a[count_a])
      count_a += 1
      count_b += 1
  return list_c 
  print(list_c)
if __name__ == '__main__':
list_a = [2, 8, 4, 5, 10]
list_b = [10, 12, 4, 5, 2]
findTheSame(list_a, list_b)
