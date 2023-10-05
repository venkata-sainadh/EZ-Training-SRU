Input="Hello, how is your family?!"
Output=""
for i in range(len(Input)):
    if(Input[i].isalpha()):
        Output+="X"
    else:
        Output+=Input[i]
j=0
Input=list(Input)
Output=list(Output)
for i in range(len(Input)-1,-1,-1):
    while(Output[j]!="X"):
        j+=1
    if(Input[i].isalpha()):
        Output[j]=Input[i]
        j+=1
print("".join(Output))