
import glob
#to import pandas in terminal give "pip install pandas"
import pandas as pd
#give path where all xlsx's exist
path = "D:\\python"
file_list= glob.glob(path+"/*.xlsx")

pd.read_excel(file_list)
excl_list=[]
for file in file_list:
    excl_list.append(pd.read_excel(file))

excl_merge= pd.concat(excl_list,ignore_index=True)
print(type(excl_merge))

# create a new xlsx file & give path below example foods.xlsx
out_file= 'C:\\Users\\VHB\\OneDrive\\Documents\\foods.xlsx'
excl_merge.to_excel(out_file,index=False)

