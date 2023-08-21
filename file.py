import csv
import numpy as np
data=[]
with open(r"C:\Users\gaura\Desktop\NumProject\MER.csv",'r') as csvfile:
    file_reader=csv.reader(csvfile, delimiter=',')
    for row in file_reader:
        data.append(row)

data=np.array(data)

# 1. Explore the important attributes like dimension,shape, data type etc, of the array formed above.
def fun1(data):    
    print("Dimensions of the array: ",data.ndim)
    print("Shape of the array: ",data.shape)
    print("Data type of elements of the array: ")
    a=[]
    for i in data[1]:
        a.append(type(i))
    print(a)


# 2. Print the data contained in the first 10 rows of the 4th column.

def fun2(data):
    print("The data contained in the first 10 rows of the 4th column : ")
    print(data[:10,3].reshape(10,1))


# 3. Which row serves as the headers/titles for all the columns.

def fun3(data):
    print("Row 1 with index 0 servers as the header/titles for all the columns: \n")
    print(data[0,:])



# 4. Print the data contained in column 2 and 3 from row 1 till row 20.

def fun4(data):
    print("The data contained in column 2 and 3 from row 1 till row 20 :\n")
    print(data[1:21,2:4])


# 5. Print the data present in only the first three and the last three rows of all the columns in a single output.

def fun5(data):
    print("The data present in only the first three and the last three rows of all the columns in a single output : \n")
    selected_rows = np.concatenate((data[1:4, :], data[-3:, :]))
    print(selected_rows)

# 6. Sort the data on the basis of net amount of electricity generated irrespective of the source.

def fun6(data):
    print("Sorted data on the basis of net amount of electricity generated irrespective of the source : \n")
    data=data[1:,:]
    for row_idx in range(data.shape[0]):
        if data[row_idx, 2] != "Not Available":
            data[row_idx, 2] = float(data[row_idx, 2])
    sorted_indices = np.argsort(data[:, 2])
    sorted_array = data[sorted_indices]

    print(sorted_array)

# 7. Find the total amount of electricity generated using coal and nuclear between 1949-1990.

def fun7(data):
    sum=0
    for i in data:
        if i[4]=="Electricity Net Generation From Coal, All Sectors" or i[4]=="Electricity Net Generation From Nuclear Electric Power, All Sectors":
            if int(i[1]) in range(194913,199014,100):
                sum=sum+float(i[2])
    
    print("The total amount of electricity generated using coal and nuclear between 1949-1990 : ",sum," Million Kilowatthours")

# 8. Print all the unique sources of Energy generation present in the dataset.

def fun8(data):
    print("All the unique sources of Energy generation present in the dataset : \n")
    unique=np.unique(data[1:,4])
    print(unique)   


# 9. Print all the details(annual) where the energy source is Wind Energy. Use the concept of masking to filter the data. 

def fun9(data):
    mask=data[:,4]=="Electricity Net Generation From Wind, All Sectors"
    print("The details(annual) where the energy source is Wind Energy: \n")
    print(data[mask])

# 10. Print the Total Energy generated in the USA till date.

def fun10(data):
    sum=0
    for i in data[1:,:]:
        if int(i[1]) in range(194913,201814,100) or int(i[1]) in range(201901,201913):
            if i[2]!="Not Available":
                sum=sum+float(i[2])

    print("The Total Energy generated in the USA till date : ", round(sum,3)," Million Kilowatthours")


# 11. Print the average annual energy generated from wind in the USA and also the standard deviation present in the energy generation.

def fun11(data):
    sum=0
    arr=data[data[:, 4] == "Electricity Net Generation From Wind, All Sectors"]
    brr=np.array([])
    for i in arr:
        if i[2]!="Not Available":
            np.set_printoptions(precision=2, suppress=True)
            brr=np.concatenate((brr,np.array([float(i[2])])))

    print("Average annual energy generated from wind in the USA is: ",np.mean(brr))
    print("The Standard deviation present in the energy generation: ",np.std(brr))


# 12. What and when was the maximum annual energy generated?

def fun12(data):
    di={}
    for i in range(194913,201814,100):
        sum=0
        for j in data[1:,:]:
            if i==int(j[1]):
                if j[2]!="Not Available":
                    sum=sum+float(j[2])
            
        di[i]=sum
    sum=0
    for i in range(201901,201911,1):
        
        for j in data[1:,:]:
            if i==int(j[1]):
                if j[2]!="Not Available":
                    sum=sum+float(j[2]) 
        di[2019]=sum   
    
    
    listt=list(di.values())
    maxx=np.amax(listt)
    
    year=[val for val in di if di[val]==maxx]
    

    return listt,maxx,year

# 13. Find from the above data if the energy production in the USA has increased in the last 10 years

def fun13(data):
    listt,x,y=fun12(data)
    print("This is the energy consumption of last  10 years from 2008 to 2018:\n")
    print(listt[-11:-1])
    print("Energy production has slightly increased in last 10 years from ",listt[-11],'Million Kilowatthours to',listt[-2],'Million Kilowatthours')

# 14. What is the trend in the energy generated from wind over the years? Which source of energy has been the largest contributor to the annual electricity production over the years.

def fun14(data):
    di={}
    for i in range(194913,201814,100):
        sum=0
        for j in data[1:,:]:
            if i==int(j[1]) and j[4]=="Electricity Net Generation From Wind, All Sectors":
                if j[2]!="Not Available":
                    sum=sum+float(j[2])
        if sum!=0:    
            di[i]=sum

    sum=0
    for i in range(201901,201911,1):
        
        for j in data[1:,:]:
            if i==int(j[1]) and j[4]=="Electricity Net Generation From Wind, All Sectors":
                if j[2]!="Not Available":
                    sum=sum+float(j[2]) 
        di[2019]=sum   
    
    np.set_printoptions(precision=2, suppress=True)
    listt=list(di.values())
    arr=np.array(listt)
    print("This is the trend in the energy generated from wind over the years :")
    print(listt)
    print("Energy production from the wind is incresing at a great pace.....")


def fun15(data):
    print
    



def fun16(data):
    print







# Main()............

ch=1
while ch==1:
    print("Enter 1 to Explore the important attributes like dimension,shape, data type etc, of the array formed.")
    print("Enter 2 to Print the data contained in the first 10 rows of the 4th column")
    print("Enter 3 to see Which row serves as the headers/titles for all the columns.")
    print("Enter 4 to Print the data contained in column 2 and 3 from row 1 till row 20")
    print("Enter 5 to Print the data present in only the first three and the last three rows of all the columns in a single output.")
    print("Enter 6 to sort the data on the basis of net amount of electricity generated irrespective of the source.")
    print("Enter 7 to find the total amount of electricity generated using coal and nuclear between 1949-1990.")
    print("Enter 8 to print all the unique sources of Energy generation present in the dataset.")
    print("Enter 9 to print all the details(annual) where the energy source is Wind Energy. Use the concept of masking to filter the data.")
    print("Enter 10 to print the Total Energy generated in the USA till date")
    print("Enter 11 to  print the average annual energy generated from wind in the USA and also the standard deviation present in the energy generation.")
    print("Enter 12 to see What and when was the maximum annual energy generated")
    print("Enter 13 to Find from the above data if the energy production in the USA has increased in the last 10 years")
    print("Enter 14 to find What is the trend in the energy generated from wind over the years? Which source of energy has been the largest contributor to the annual electricity production over the years.")
    print("Enter 15 to Which renewable source of energy is expected to meet the major demand of energy in the coming years. Can we predict an estimate for the same.")
    print("Enter 16 to Compute the contribution of wind, solar, and their combined contribution compared to the total energy generation in the USA, and answer whether the national grid is fundamentally shifting toward wind energy")
    choice=int(input("\nEnter your choice:\n"))

    if choice==1:
        fun1(data)
    elif choice==2:
        fun2(data)
    elif choice==3:
        fun3(data)
    elif choice==4:
        fun4(data)
    elif choice==5:
        fun5(data)
    elif choice==6:
        fun6(data)
    elif choice==7:
        fun7(data)
    elif choice==8:
        fun8(data)
    elif choice==9:
        fun9(data)
    elif choice==10:
        fun10(data)
    elif choice==11:
        fun11(data)
    elif choice==12:
        x,y,z=fun12(data)
        print("The maximum annual energy generated is: ",y,"Million Kilowatthours in the year ",z[0]//100)
        
    elif choice==13:
        fun13(data)
    elif choice==14:
        fun14(data)
    elif choice==15:
        fun15(data)
    elif choice==16:
        fun16(data)
    else:
        print("You have entered a wrong choice")
    ch=int(input("\n Enter 1 to continuee... and Enter 0 to exit : "))
    
    









