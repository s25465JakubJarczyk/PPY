listaLiczb = input("Podaj kilka liczb rozdnielonych przecinkiem: ")
x = listaLiczb.split(",")
print(x)
max = 0
min = int(x[0])
for i in x:
    numb = int(i)
    if max < numb:
      max = numb
    if min > numb:
      min = numb
print(min)
print(max)