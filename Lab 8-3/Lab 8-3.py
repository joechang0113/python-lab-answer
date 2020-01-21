name= []
score= []
total= []
stdev= 0
with open("Lab 8-3/工程電腦程式Lab成績.txt", 'r', encoding='UTF-8') as file:
    for line in file:
        name.append(line.strip().split(' ')[0])
        score.append(line.strip().split(' ')[1:])

for i in range(len(name)):
    print("{0}: ".format(name[i]),end='')
    total.append(0)
    for t in score[i]:
        total[i]+= int(t)
    print(total[i])
print("\nthe highest: %d" %max(total))
print("the lowest: %d" %min(total))
avg= sum(total)/len(score)/len(score[0])
print("avg: %d" %avg)
for i in range(len(score)):
    for t in score[i]:
        stdev+= pow(int(t)-avg, 2)
        
stdev = (stdev/len(score)/len(score[0]))**0.5
print("stdev: %.2f" %stdev)
