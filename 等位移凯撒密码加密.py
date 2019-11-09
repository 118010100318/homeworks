ks=input("请输入明文:")
a=len(ks)
for i in range(0,a):
     b=ord(ks[i])+i+1
     if 65<=ord(ks[i])<=90 and b>90:
          b=b-26
     elif 97<=ord(ks[i])<=122 and b>122:
          b=b-26
     print(chr(b),end='')
     


