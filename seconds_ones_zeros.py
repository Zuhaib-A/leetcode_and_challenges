def solution(numbers, zerosToOne):
    seconds=0
    continuing=True
    while continuing==True:
        length=len(numbers)
        current_zeros=0
        current_ones=0
        list_index_zeros=[]
        list_index_ones=[]
        
        for i in numbers:
            index=numbers.index(i)
            
            if i==0:
                current_zeros=current_zeros+1
                list_index_zeros.append(index)
                
            elif i==1:
                current_ones=current_ones+1
                list_index_ones.append(index)
            

        if zerosToOne <= current_zeros:
            for i in range(zerosToOne):
                numbers.pop(index+len(list_index_zeros)-1-i)
            new_list=[1]
            for i in range(0, len(numbers)):
                new_list.append(numbers[i])
                
            numbers=new_list
            seconds=seconds+1
        
        elif current_ones >= 1:
            numbers[current_ones-1]=0
            seconds=seconds+1
            
        else:
            continuing=False
    return seconds
