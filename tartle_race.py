import random
import time

a = 0
b = 0
goal = 10

ans = input("a,bどちらの亀が勝つと思いますか？")

while (a < goal) and (b < goal):
  a += random.randint(1,3)
  b += random.randint(1,3)
  print("a:" + "->" * a + "@")
  print("b:" + "->" * b + "@")
  time.sleep(1)

if a == b:
  print("draw")
  winner = "draw"
elif a > b:
  print("winner is a")
  winner = "a"
else:
  print("winner is b")
  winner = "b"

if ans == winner:
  print("you wiiiiiiin")
else:
  print("you lost....")
