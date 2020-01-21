name=[]
height=[]
weight=[]

with open("./Lab 8-1/read.txt", "r", encoding= "UTF-8") as file:
    for line in file:
        name.append(line.strip().split(' ')[0])
        height.append(eval(line.strip().split(' ')[1]))
        weight.append(eval(line.strip().split(' ')[2]))

print("\nheight avg: %.2f" %(sum(height)/len(height)))
print("weight avg: %.2f" %(sum(weight)/len(weight)))
print("the tallest one: {0}".format(name[height.index(max(height))]))
print("the heaviest one: {0}\n".format(name[weight.index(max(weight))]))
