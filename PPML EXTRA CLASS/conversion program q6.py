#write a pandas program to split the following dataframe into groups based on school code.also check the type 

import pandas as pd
pd.set_option('display.max_rows',None)
student_data=pd.DataFrame({
    'School_code':['S001','S002','S001','S003','S002','S001','S003'],
    'class':['V','V','VI','VI','V','VI','VI'],
    'name':['Alok','Bina','Chitra','Dinesh','Esha','Firoz','Gita'],
    'date_of_birth':['2005-01-15','2006-02-20','2005-03-10','2006-04-25','2005-05-30','2006-06-15','2005-07-20'],
    'age':[18,17,18,17,18,17,18],
    'height':[150,160,155,165,158,152,168],
    'weight':[45,50,48,55,52,47,60],
    'address':['Delhi','Mumbai','Delhi','Kolkata','Mumbai','Delhi','Kolkata'],
    'name':['Alok','Bina','Chitra','Dinesh','Esha','Firoz','Gita']
})
print("original dataframe:")
print(student_data)
print('\nsplit dataframe based on school code wise:')
result=student_data.groupby('School_code')
for name,group in result:
        print(f"\nGroup: {name}")
        print(name)
        print(group)
        print("\ntype of the object:")
        print(type(group))
