#utf-8
with open('./mvsform.log') as fp:
    log_ori = fp.readlines()

acc_all = []
comp_all = []

for i in log_ori:
    if(len(i)>5):
        acc_i = i.split(' ')[3].split("/")[0]
        acc_all.append(float(acc_i))
        # comp_i = i.split(' ')[1].split("/")[1]
acc = 0.0
comp = 0.0
for j,k in enumerate(acc_all):
    if(j%2==0):
        acc += k
    else:
        comp +=k

acc =  acc/(len(acc_all)//2)
comp = comp/(len(acc_all)//2)
print("所有场景的acc:",acc,",comp:",comp)
