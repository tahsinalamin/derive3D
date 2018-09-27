'''
Program: Find the derivative of a 2D function and compare it with another function
Update:  6/4/18 - Program reads function A, compute the derivatives (Gx & Gy), plot them and normalize the values.
            12/4/18 - Reads function B, plot the axis values and normalize them
            15/4/18 - Resized function B w.r. to function A and compare derivatives of X and Y axis of both function by taking the average of intervals and plotting them
            16/4/18 - Compare A and B by taking the median of intervals and plotting them. Fixed the legend error in plots.
             2/5/18 - Implemented Method 3 to compare A & B and plot them.  Added Component and Angle comparison and plot them.
             9/5/18 - Made everything 3D
'''
#import matplotlib
#import numpy.core._methods
#import numpy.lib.format
import numpy as np
import math
import csv
#from tkinter import *
#matplotlib.use('agg')
#import matplotlib.backends.backend
import matplotlib.pyplot as plt


##read the csv file
A_file_name=input("Enter the name of Function A (like DERIV3D_functionA_XYZ.csv): ")
B_file_name=input("Enter the name of Function B (like DERIV3D_functionB_XYZ.csv): ")
#A_file_name="DERIV3D_functionA_XYZ.csv"
#B_file_name="DERIV3D_functionB_XYZ.csv"

################ Process File A Function ############

index=[] #the index
x=[]  #the x column
y=[]  #the y column
z=[]  #the z column

##open the function A file and store them ###
with open(A_file_name) as csvDataFile:
    csvReader = csv.reader(csvDataFile,delimiter=',')
    for row in csvReader:
        float(row[0].replace(',', ''))
        index.append(float(row[0]))
        float(row[1].replace(',', ''))
        x.append(float(row[1]))
        float(row[2].replace(',', ''))
        y.append(float(row[2]))
        float(row[3].replace(',', ''))
        z.append(float(row[3]))
     
csvDataFile.close()
print("Function A:")
print(len(x))
print(len(y))
print(len(z))

###plot X,Y and Z values of function A ###
indexVSxy= plt.figure(1,figsize=(12,5))
plt.plot(index,x, color = 'b',label="x")
plt.plot(index,y,'g',label="y")
plt.plot(index,z,'y',label="z")
plt.title("x, y and z values of Function A vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('x, y and z values')
plt.legend(loc="best")
indexVSxy.tight_layout()
#indexVSxy.ioff()
indexVSxy.show()
plt.savefig('plots/Figure_1.pdf')

### Find the new points for index ####
index_m=[]
for i in range(0,len(index)-1,1):
    mid=(index[i]+index[i+1])/2
    index_m.append(mid)

### Find Derivative w.r. to X ####
Gx=[]
for i in range(0,len(x)-1,1):
    dx=(x[i+1]-x[i])/(index[i+1]-index[i])
    Gx.append(dx)

indexVSgx= plt.figure(2,figsize=(12,5))
plt.subplot(3,1,1)
plt.plot(index_m,Gx , 'b')
plt.title("G(x) vs Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('G(x)')
plt.legend()

### Find Derivative w.r. to Y ####
Gy=[]
for i in range(0,len(y)-1,1):
    dy=(y[i+1]-y[i])/(index[i+1]-index[i])
    Gy.append(dy)

plt.subplot(3,1,2)
plt.plot(index_m,Gy , 'g')
plt.title("G(y) vs Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('G(y)')
plt.legend()

### Find Derivative w.r. to Z ####
Gz=[]
for i in range(0,len(z)-1,1):
    dz=(z[i+1]-z[i])/(index[i+1]-index[i])
    Gz.append(dz)

plt.subplot(3,1,3)
plt.plot(index_m,Gz , 'y')
plt.title("G(z) vs Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('G(z)')
plt.legend()
indexVSgx.tight_layout()
indexVSgx.show()
plt.savefig('plots/Figure_2.pdf')

print("Gx[0],Gy[0],Gz[0]")
print(Gx[0],Gy[0],Gz[0])
print(Gx[1],Gy[1],Gz[1])
print(Gx[2],Gy[2],Gz[2])
print(Gx[3],Gy[3],Gz[3])
##### Normalize Gx #####
max_Gx=max(Gx)
for i in range(0,len(Gx)-1,1):
    Gx[i]=Gx[i]/max_Gx

##### Normalize Gy #####
max_Gy=max(Gy)
for i in range(0,len(Gy)-1,1):
    Gy[i]=Gy[i]/max_Gy

##### Normalize Gz #####
max_Gz=max(Gz)
for i in range(0,len(Gz)-1,1):
    Gz[i]=Gz[i]/max_Gz

################# Process File B Function ###############
index_B=[] #the index
x_B=[]  #the x column
y_B=[]  #the y column
z_B=[]  #the z column

##open the function A file and store them ###
with open(B_file_name) as BcsvDataFile:
    csvReader = csv.reader(BcsvDataFile,delimiter=',')
    for row in csvReader:
        float(row[0].replace(',', ''))
        index_B.append(float(row[0]))
        float(row[1].replace(',', ''))
        x_B.append(float(row[1]))
        float(row[2].replace(',', ''))
        y_B.append(float(row[2]))
        float(row[3].replace(',', ''))
        z_B.append(float(row[3]))

BcsvDataFile.close()
print("Function B...")
print(len(x_B))
print(len(y_B))
print(len(z_B))

###plot X and Y values of function B ###
indexVSBxy= plt.figure(3,figsize=(12,5))
plt.plot(index_B,x_B,'b',label="x",linewidth=0.15)
plt.plot(index_B,y_B,'g',label="y",linewidth=0.15)
plt.plot(index_B,z_B,'y',label="z",linewidth=0.15)
plt.title("x, y and z values of Function B vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('x, y and z values')
plt.legend(loc="best")
indexVSBxy.tight_layout()
indexVSBxy.show()
plt.savefig('plots/Figure_3.pdf')

#### Normalize B ####
max_Bx=max(x_B)
for i in range(0,len(x_B)-1,1):
    x_B[i]=x_B[i]/max_Bx

max_By=max(y_B)
for i in range(0,len(y_B)-1,1):
    y_B[i]=y_B[i]/max_By

max_Bz=max(z_B)
for i in range(0,len(z_B)-1,1):
    z_B[i]=z_B[i]/max_Bz

################### Comapre A and B : METHOD-1 (Taking average of intervals) ###################
interval_AB=math.floor(len(x_B)/len(Gx))
print("Interval between A and B= ",interval_AB)
print("\n**METHOD 1 : Taking the average of the intervals**")
##fit Bx w.r. to Gx
resized_Bx=[]
i = 0
while i<len(Gx)*interval_AB:     ##loop to the point where Gx goes
    sum_of_interval_points=0
    for j in range(i,i+interval_AB,1):
        sum_of_interval_points=sum_of_interval_points+x_B[j]   ##sum of all the points
    resized_Bx.append(sum_of_interval_points/interval_AB)  ##inserting the average value
    i=i+interval_AB

print("Checking validity...")
print(resized_Bx[1],  (x_B[5]+x_B[6]+x_B[7]+x_B[8]+x_B[9])/5)

##fit By w.r. to Gy
resized_By=[]
i = 0
while i<len(Gy)*interval_AB:     ##loop to the point where Gy goes
    sum_of_interval_points=0
    for j in range(i,i+interval_AB,1):
        sum_of_interval_points=sum_of_interval_points+y_B[j]   ##sum of all the points
    resized_By.append(sum_of_interval_points/interval_AB)  ##inserting the average value
    i=i+interval_AB

print("Checking validity...")
print(resized_By[1],  (y_B[5]+y_B[6]+y_B[7]+y_B[8]+y_B[9])/5)

##fit Bz w.r. to Gz
resized_Bz=[]
i = 0
while i<len(Gz)*interval_AB:     ##loop to the point where Gz goes
    sum_of_interval_points=0
    for j in range(i,i+interval_AB,1):
        sum_of_interval_points=sum_of_interval_points+z_B[j]   ##sum of all the points
    resized_Bz.append(sum_of_interval_points/interval_AB)  ##inserting the average value
    i=i+interval_AB

print("Checking validity...")
print(resized_Bz[1],  (z_B[5]+z_B[6]+z_B[7]+z_B[8]+z_B[9])/5)

###plot GX and BX values of function A and B ###
GxVSBx= plt.figure(4,figsize=(12,5))
plt.plot(index_m,Gx,'b',label="Function A")
plt.plot(index_m,resized_Bx,'g',label="Function B")
plt.title("Comparison Method 1: Derivatives of Function A with Function B (x axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('x Derivate values for Function A and V')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_4.pdf')

###plot GY and BY values of function A and B ###
GyVSBy= plt.figure(5,figsize=(12,5))
plt.plot(index_m,Gy,'b',label="Function A")
plt.plot(index_m,resized_By,'g',label="Function B")
plt.title("Comparison Method 1: Derivatives of Function A with Function B (y axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('y Derivate values for Function A and V')
plt.legend(loc='best')
GyVSBy.tight_layout()
GyVSBy.show()
plt.savefig('plots/Figure_5.pdf')


###plot GZ and BZ values of function A and B ###
GzVSBz= plt.figure(6,figsize=(12,5))
plt.plot(index_m,Gz,'b',label="Function A")
plt.plot(index_m,resized_Bz,'g',label="Function B")
plt.title("Comparison Method 1: Derivatives of Function A with Function B (z axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('z Derivate values for Function A and V')
plt.legend(loc='best')
GzVSBz.tight_layout()
GzVSBz.show()
plt.savefig('plots/Figure_6.pdf')



################### Comapre A and B : METHOD-2 (Taking median of intervals) ###################
print("\n**METHOD 2 : Taking the median of the intervals**")
##fit Bx w.r. to Gx
resized_Bx=[]
i = 0
while i<len(Gx)*interval_AB:     ##loop to the point where Gx goes
    median_index=0
    for j in range(i,i+interval_AB,1):
        median_index=math.floor((i+(i+interval_AB))/2)  ##get the median index
    resized_Bx.append(x_B[median_index])  ##inserting the average value
    i=i+interval_AB

print("Checking validity...")
print(resized_Bx[1],  x_B[7])

##fit By w.r. to Gx
resized_By=[]
i = 0
while i<len(Gy)*interval_AB:     ##loop to the point where Gx goes
    median_index=0
    for j in range(i,i+interval_AB,1):
        median_index=math.floor((i+(i+interval_AB))/2)  ##get the median index
    resized_By.append(y_B[median_index])  ##inserting the average value
    i=i+interval_AB

print("Checking validity...")
print(resized_By[1],  y_B[7])

##fit Bz w.r. to Gz
resized_Bz=[]
i = 0
while i<len(Gz)*interval_AB:     ##loop to the point where Gx goes
    median_index=0
    for j in range(i,i+interval_AB,1):
        median_index=math.floor((i+(i+interval_AB))/2)  ##get the median index
    resized_Bz.append(z_B[median_index])  ##inserting the average value
    i=i+interval_AB

print("Checking validity...")
print(resized_Bz[1],  z_B[7])


###plot GX and BX values of function A and B ###
GxVSBx= plt.figure(7,figsize=(12,5))
plt.plot(index_m,Gx,'b',label="Function A")
plt.plot(index_m,resized_Bx,'g',label="Function B")
plt.title("Comparison Method 2: Derivatives of Function A with Function B (x axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('x Derivate values for Function A and V')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_7.pdf')

###plot GY and BY values of function A and B ###
GyVSBy= plt.figure(8,figsize=(12,5))
plt.plot(index_m,Gy,'b',label="Function A")
plt.plot(index_m,resized_By,'g',label="Function B")
plt.title("Comparison Method 2: Derivatives of Function A with Function B (y axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('y Derivate values for Function A and V')
plt.legend(loc='best')
GyVSBy.tight_layout()
GyVSBy.show()
plt.savefig('plots/Figure_8.pdf')

###plot GZ and BZ values of function A and B ###
GzVSBz= plt.figure(9,figsize=(12,5))
plt.plot(index_m,Gz,'b',label="Function A")
plt.plot(index_m,resized_Bz,'g',label="Function B")
plt.title("Comparison Method 2: Derivatives of Function A with Function B (z axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('z Derivate values for Function A and V')
plt.legend(loc='best')
GzVSBz.tight_layout()
GzVSBz.show()
plt.savefig('plots/Figure_9.pdf')

################### Comapre A and B : METHOD-3 (Taking Average from 2 intervals) ###################
print("\n**METHOD 3 : Taking Average from two intervals**")
resized_Bx=[]
shift_index=math.floor(interval_AB/2)
i=0
first_index_of_i=0
for j in range(0,shift_index+1,1):
    first_index_of_i=first_index_of_i+x_B[j]
resized_Bx.append(first_index_of_i/(shift_index+1))  ##taking the average of first 3 values
i=i+interval_AB
while i<len(Gx)*interval_AB:     ##loop to the point where Gx goes
    sum_of_points=0
    for j in range(i-shift_index,i+shift_index+1,1):
        sum_of_points=+sum_of_points+x_B[j]
    resized_Bx.append(sum_of_points/interval_AB)
    i=i+interval_AB
    
print("Checking validity...")
print(resized_Bx[1],  (x_B[3]+x_B[4]+x_B[5]+x_B[6]+x_B[7])/5)

##fit By w.r. to Gx
resized_By=[]
shift_index=math.floor(interval_AB/2)
i=0
first_index_of_i=0
for j in range(0,shift_index+1,1):
    first_index_of_i=first_index_of_i+y_B[j]
resized_By.append(first_index_of_i/(shift_index+1))  ##taking the average of first 3 values
i=i+interval_AB
while i<len(Gy)*interval_AB:     ##loop to the point where Gx goes
    sum_of_points=0
    for j in range(i-shift_index,i+shift_index+1,1):
        sum_of_points=+sum_of_points+y_B[j]
    resized_By.append(sum_of_points/interval_AB)
    i=i+interval_AB

##fit Bz w.r. to Gz
resized_Bz=[]
shift_index=math.floor(interval_AB/2)
i=0
first_index_of_i=0
for j in range(0,shift_index+1,1):
    first_index_of_i=first_index_of_i+z_B[j]
resized_Bz.append(first_index_of_i/(shift_index+1))  ##taking the average of first 3 values
i=i+interval_AB
while i<len(Gz)*interval_AB:     ##loop to the point where Gx goes
    sum_of_points=0
    for j in range(i-shift_index,i+shift_index+1,1):
        sum_of_points=+sum_of_points+z_B[j]
    resized_Bz.append(sum_of_points/interval_AB)
    i=i+interval_AB

#HOSEIN
GxBx_comparison = []
GyBy_comparison = []
GzBz_comparison = []
for i in range(0,len(Gx),1):
    GxBx_comparison.append(Gx[i] / resized_Bx[i])
    GyBy_comparison.append(Gy[i] / resized_By[i])
    GzBz_comparison.append(Gz[i] / resized_Bz[i])

print("Checking validity...")
print(resized_Bz[1],  (z_B[3]+z_B[4]+z_B[5]+z_B[6]+z_B[7])/5)

###plot GX and BX values of function A and B ###
GxVSBx= plt.figure(10,figsize=(12,5))
plt.plot(index_m,Gx,'b',label="Function A")
plt.plot(index_m,resized_Bx,'g',label="Function B")
plt.title("Comparison Method 3: Derivatives of Function A with Function B (x axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('x Derivate values for Function A and V')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_10.pdf')

###plot GY and BY values of function A and B ###
GyVSBy= plt.figure(11,figsize=(12,5))
plt.plot(index_m,Gy,'b',label="Function A")
plt.plot(index_m,resized_By,'g',label="Function B")
plt.title("Comparison Method 3: Derivatives of Function A with Function B (y axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('y Derivate values for A and V')
plt.legend(loc='best')
GyVSBy.tight_layout()
GyVSBy.show()
plt.savefig('plots/Figure_11.pdf')

###plot GZ and BZ values of function A and B ###
GzVSBz= plt.figure(12,figsize=(12,5))
plt.plot(index_m,Gz,'b',label="Function A")
plt.plot(index_m,resized_Bz,'g',label="Function B")
plt.title("Comparison Method 3: Derivatives of Function A with Function B (z axis) vs. Index(t)")
plt.xlabel('Index(t)')
plt.ylabel('z Derivate values for A and V')
plt.legend(loc='best')
GzVSBz.tight_layout()
GzVSBz.show()
plt.savefig('plots/Figure_12.pdf')

############################# Component Comparison ############################
CA=[]
CB=[]
for i in range(0,len(Gx),1):
    CAi=(Gx[i])**2+(Gy[i])**2+(Gz[i])**2
    CA.append(math.sqrt(CAi))
    
for i in range(0,len(x_B),1):
    CBi=(x_B[i])**2+(y_B[i])**2+(z_B[i])**2
    CB.append(math.sqrt(CBi))

######## CC::METHOD 1 - Taking Average #####
print("\n**Component Comparsions : Taking the average of the intervals**")
##fit Bx w.r. to Gx
resized_CB=[]
i = 0
while i<len(CA)*interval_AB:     ##loop to the point where Gx goes
    sum_of_interval_points=0
    for j in range(i,i+interval_AB,1):
        sum_of_interval_points=sum_of_interval_points+CB[j]   ##sum of all the points
    resized_CB.append(sum_of_interval_points/interval_AB)  ##inserting the average value
    i=i+interval_AB

print("Checking validity...")
print(resized_CB[1],  (CB[5]+CB[6]+CB[7]+CB[8]+CB[9])/5)

component_comparsion=[]
for i in range(0,len(CA),1):
    component_comparsion.append(resized_CB[i]/CA[i])

##plot component comparison
GxVSBx= plt.figure(13,figsize=(12,5))
plt.plot(index_m, CA,'b', label = "Component A") #HOSEIN
plt.plot(index_m, resized_CB,'g', label = "Component B") #HOSEIN
plt.plot(index_m,component_comparsion,'r',label="Component B/Component A vs. Index(t)")
plt.title("Component Comparsion: C(B) and C(A)")
plt.xlabel('Index(t)')
plt.ylabel('Values of C(A), C(B) and C(B)/C(A)')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_13.pdf')


############################# Angle Comparison #############################
theta_A=[]
theta_B=[]

for i in range(0,len(Gx),1):
    if CA[i]==0:
        CA[i]=1
    theta_A_i=math.acos(Gx[i]/CA[i])
    theta_A.append(theta_A_i)
    
for i in range(0,len(x_B),1):
    if CB[i]==0:
        CB[i]=1
    theta_B_i=math.acos(x_B[i]/CB[i])
    theta_B.append(theta_B_i)
print(len(theta_A),len(theta_B))
    
######## CC::METHOD 1 - Taking Average #####
print("\n**Angle Comparsions (X axis): Taking the average of the intervals**")
##fit Bx w.r. to Gx
resized_theta_B=[]
i = 0
while i<len(theta_A)*interval_AB:     ##loop to the point where Gx goes
    sum_of_interval_points=0
    for j in range(i,i+interval_AB,1):
        sum_of_interval_points=sum_of_interval_points+theta_B[j]   ##sum of all the points
    resized_theta_B.append(sum_of_interval_points/interval_AB)  ##inserting the average value
    i=i+interval_AB

print("Checking validity...")    
print(resized_theta_B[1],  (theta_B[5]+theta_B[6]+theta_B[7]+theta_B[8]+theta_B[9])/5)

theta_comparsion = []
for i in range(0,len(CA),1): #HOSEIN
    theta_comparsion.append(theta_A[i] / resized_theta_B[i])

###plot thetaA/ thetaB values of function A and B ###
GxVSBx= plt.figure(14,figsize=(12,5))
plt.plot(index_m,theta_A,'b',label="Theta(A)")
plt.plot(index_m,resized_theta_B,'g',label="Theta(B)")
plt.title("Angle Comparsion (X axis): Theta(A) and Theta(B)")
plt.xlabel('Index(t)')
plt.ylabel('Theta(A) and Theta(B)')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_14.pdf')


GxVSBx= plt.figure(15,figsize=(12,5)) #HOSEIN
plt.plot(index_m, theta_comparsion, 'r', label = "Theta(A) / Theta(B)")
plt.title("Angle Comparsion with division(X axis): Theta(A) and Theta(B)")
plt.xlabel('Index(t)')
plt.ylabel('Theta(A)/ Theta(B)')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_15.pdf')


##### Angle comparsion:::for y axis #####
theta_Ay=[]
theta_By=[]

for i in range(0,len(Gx),1):
    if CA[i]==0:
        CA[i]=1
    theta_Ay_i=math.acos(Gy[i]/CA[i])
    theta_Ay.append(theta_Ay_i)

for i in range(0,len(x_B),1):
    if CB[i]==0:
        CB[i]=1
    theta_By_i=math.acos(y_B[i]/CB[i])
    theta_By.append(theta_By_i)

print("\n**Angle Comparsions (Y axis): Taking the average of the intervals**")
##fit Bx w.r. to Gx
resized_theta_By=[]
i = 0
while i<len(theta_Ay)*interval_AB:     ##loop to the point where Gx goes
    sum_of_interval_points=0
    for j in range(i,i+interval_AB,1):
        sum_of_interval_points=sum_of_interval_points+theta_By[j]   ##sum of all the points
    resized_theta_By.append(sum_of_interval_points/interval_AB)  ##inserting the average value
    i=i+interval_AB
    
print(resized_theta_By[1],  (theta_By[5]+theta_By[6]+theta_By[7]+theta_By[8]+theta_By[9])/5)

theta_comparsion = []
for i in range(0,len(CA),1): #HOSEIN
    theta_comparsion.append(theta_Ay[i] / resized_theta_By[i])


GxVSBx= plt.figure(16,figsize=(12,5))
plt.plot(index_m,theta_Ay,'b',label="Theta(A)")
plt.plot(index_m,resized_theta_By,'g',label="Theta(B)")
plt.title("Angle Comparsion (Y axis): Theta(A) and Theta(B)")
plt.xlabel('Index(t)')
plt.ylabel('Theta(A) and Theta(B)')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_16.pdf')


GxVSBx= plt.figure(17,figsize=(12,5)) #HOSEIN
plt.plot(index_m, theta_comparsion, 'r', label = "Theta(A) / Theta(B)")
plt.title("Angle Comparsion with division(Y axis): Theta(A) and Theta(B)")
plt.xlabel('Index(t)')
plt.ylabel('Theta(A)/ Theta(B)')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_17.pdf')

##### Angle comparsion:::for z axis #####
theta_Az=[]
theta_Bz=[]

for i in range(0,len(Gx),1):
    if CA[i]==0:
        CA[i]=1
    theta_Az_i=math.acos(Gz[i]/CA[i])
    theta_Az.append(theta_Az_i)

for i in range(0,len(x_B),1):
    if CB[i]==0:
        CB[i]=1
    theta_Bz_i=math.acos(z_B[i]/CB[i])
    theta_Bz.append(theta_Bz_i)


print("\n**Angle Comparsions (Z axis): Taking the average of the intervals**")
resized_theta_Bz=[]
i = 0
while i<len(theta_Az)*interval_AB:     ##loop to the point where Gx goes
    sum_of_interval_points=0
    for j in range(i,i+interval_AB,1):
        sum_of_interval_points=sum_of_interval_points+theta_Bz[j]   ##sum of all the points
    resized_theta_Bz.append(sum_of_interval_points/interval_AB)  ##inserting the average value
    i=i+interval_AB
    
print(resized_theta_Bz[1],  (theta_Bz[5]+theta_Bz[6]+theta_Bz[7]+theta_Bz[8]+theta_Bz[9])/5)

theta_comparsion = []
for i in range(0,len(CA),1): #HOSEIN
    theta_comparsion.append(theta_Az[i] / resized_theta_Bz[i])

GxVSBx= plt.figure(18,figsize=(12,5))
plt.plot(index_m,theta_Az,'b',label="Theta(A)")
plt.plot(index_m,resized_theta_Bz,'g',label="Theta(B)")
plt.title("Angle Comparsion (Z axis): Theta(A) and Theta(B)")
plt.xlabel('Index(t)')
plt.ylabel('Theta(A) and Theta(B)')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_18.pdf')

GxVSBx= plt.figure(19,figsize=(12,5)) #HOSEIN
plt.plot(index_m, theta_comparsion, 'r', label = "Theta(A) / Theta(B)")
plt.title("Angle Comparsion with division(Z axis): Theta(A) and Theta(B)")
plt.xlabel('Index(t)')
plt.ylabel('Theta(A)/ Theta(B)')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_19.pdf')




    

'''
##################################################################

###plot GX and BX values of function A and B ###
GxVSBx= plt.figure(20,figsize=(12,5))
#plt.plot(index_m,Gx,'b',label="Function A")
#plt.plot(index_m,resized_Bx,'g',label="Function B")
plt.plot(index_m,GxBx_comparison,'r', label = "Division of Gx / Bx" )
plt.title("Comparison Section, Division of Gx / Bx")
plt.xlabel('Index(t)')
plt.ylabel('Division of Gx / Bx')
plt.legend(loc='best')
GxVSBx.tight_layout()
GxVSBx.show()
plt.savefig('plots/Figure_20.pdf')

###plot GY and BY values of function A and B ###
GyVSBy= plt.figure(21,figsize=(12,5))
#plt.plot(index_m,Gy,'b',label="Function A")
#plt.plot(index_m,resized_By,'g',label="Function B")
plt.plot(index_m,GyBy_comparison,'r', label = "Division of Gy / By" )
plt.title("Comparison Section, Division of Gy / By")
plt.xlabel('Index')
plt.ylabel('Division of Gy / By')
plt.legend(loc='best')
GyVSBy.tight_layout()
GyVSBy.show()
plt.savefig('plots/Figure_21.pdf')


###plot GZ and BZ values of function A and B ###
GzVSBz= plt.figure(22,figsize=(12,5))
#plt.plot(index_m,Gy,'b',label="Function A")
#plt.plot(index_m,resized_By,'g',label="Function B")
plt.plot(index_m,GzBz_comparison,'r', label = "Division of Gz / Bz" )
plt.title("Comparison Section, Division of Gz / Bz")
plt.xlabel('Index')
plt.ylabel('Division of Gz / Bz')
plt.legend(loc='best')
GzVSBz.tight_layout()
GzVSBz.show()
plt.savefig('plots/Figure_22.pdf')
'''




