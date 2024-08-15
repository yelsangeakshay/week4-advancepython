#Write FIles
# l = ["\nakshay\n","Mallinath\n","Yelsange\n"]
# f = open("Sample.txt",'w')
# f.writelines(l)
# # for word in l:
# #     f.write(word)
# f.close()
#Read FIles
# with open("Sample.txt",'r') as f:
#     print(f.read(10))
#     print(f.read(10))
    # for content in f:
    #     print(content,end='')

# with open("Sample.txt",'a') as f:
#     f.write("\nSolmon bhai")

#Create A Big FIle
big_l = [ str(i) + 'hello world' for i in range(1000)]

with open("bigfile.txt",'w') as f:
    f.writelines(big_l)

with open("bigfile.txt",'r') as f:
    size = 10
    while len(f.read(size))>0:
        print(f.read(size),end="")
        f.read(size)
        print("\n",f.tell())