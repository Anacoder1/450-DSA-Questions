#Approach 1  - O(N)

def reverseString(mystr):
  mychars=list(mystr)
  start=0
  end=len(mychars)-1
  while(start<end):
    mychars[start],mychars[end]=mychars[end],mychars[start]
    start+=1
    end-=1
  return "".join(mychars)


#Approach 2  - python list slicing method

def revString(mystr):
  return mystr[::-1]






  

