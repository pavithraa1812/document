s1='aaaa'
s2='bb'
res = "".join(i + j for i, j in zip(s1, s2)) 
      
# print result 
print("The Interleaved string : " + str(res)) 
