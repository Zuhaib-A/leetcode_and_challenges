def solution(arr):
    
    lengths=[]
    for x in arr:
        
        lengths.append(int(len(list(x))))
        
    index_len=[]
    for n in range(0, len(arr)):
        index_len.append([lengths[n], n])
        
    length = (sorted(index_len))[-1][0]
    
   
    final=[]
    remaining=length
    count=0

    
    checked=[]
    for x in arr:
        checked.append(x)
            
    while remaining != 0:
        

        found = False
        while found == False:

            for i in range(0, len(arr)):
                
                if count < len(list(arr[i])):
                    checked.append(arr[i])
                    if checked[-1]==checked[-2]:
                        temp=list(arr[i])

                        for n in range(count+1,len(arr[i])):
                            final.append(temp[n])
                        
                        remaining=0
                        found = True
                        break


                    else:
                        temp=list(arr[i])
                        final.append(temp[count])
                        found = True
                    
                else:
                    found = False
        if remaining == 0:
            break

        count=count+1
        remaining=remaining-1
        
    return "".join(final)
