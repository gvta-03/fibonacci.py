n=int(input("no. of terms"))
n1,n2=0,1
c=0
if n<=0:
  print("enter pos num")
  elif n==1:
  print("f s",n,":")
  print(n1)
  else:
  print("series")
  while c<n:
  print(n1)
  n=n1+n2
  n1=n2
  n2=n
  c+=1
