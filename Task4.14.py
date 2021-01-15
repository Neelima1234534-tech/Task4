li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
  
final_list = list(filter(lambda x: (x%3!=0)  and (x%7==0), li)) 
print(final_list) 