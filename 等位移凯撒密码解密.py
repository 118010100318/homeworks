ks=input("请输入暗文:")
a=len(ks)
for i in range(0,a):
     b=ord(ks[i])-i-1
     if 65<=ord(ks[i])<=90 and b<65:
          b=b+26
     elif 97<=ord(ks[i])<=122 and b<97:
          b=b-26
     print(chr(b),end='')
