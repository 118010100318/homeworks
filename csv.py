import csv
fr=open("score.csv","r+")
ls=[]
for line in fr:
     line = line.replace("\n","")
     ls.append(line.split(","))
a,b,c=0,0,0
for i in range(1,6):
         a=int(ls[i][1])+a
         b=int(ls[i][2])+b
         c=int(ls[i][3])+c
def cc(x):
     lt=[]
     for i in range(1,6):
       lt.append(ls[i][x])
     return max(lt)
def cg(x):
     lt=[]
     for i in range(1,6):
       lt.append(ls[i][x])
     return min(lt)
print("语文的最高分是:{0}最低分是:{1}平均分是:{2}".format(cc(1),cg(1),a/5))
print("数学的最高分是:{0}最低分是:{1}平均分是:{2}".format(cc(2),cg(2),b/5))
print("英语的最高分是:{0}最低分是:{1}平均分是:{2}".format(cc(3),cg(3),c/5))
ls[0].append("总分")
for i in range(1,6):
    ls[i].append(int(ls[i][1])+int(ls[i][2])+int(ls[i][3]))
fr.close()
with open("score.csv","w") as csvfile: 
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(ls)
