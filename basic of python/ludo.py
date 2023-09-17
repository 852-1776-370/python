try:
  a=int(input(" inter the number which you want to write the table"))
  print(a)
except ValueError:
    print("value error")
finally:
    print("try exp finished")
