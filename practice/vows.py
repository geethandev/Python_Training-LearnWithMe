#Define the find_Novowels function here
def find_Novowels(inp_str):
    out=[]
    l_inp_str = list(map(lambda x:x.lower(),inp_str))
    for i in l_inp_str:
        if i not in ('a','e','i','o','u'):
            out.append(i)
    return out
   
 

 
#Sample main section. 
#Do not remove the below portion of code. 
if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
            inp_str.append(input())
    output=find_Novowels(inp_str)
    if len(output)!=0:
            print('Strings without vowels:')
            for i in output:
                    print(i)
    else:
            print('No string found')
            