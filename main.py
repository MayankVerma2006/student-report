import pandas as pd 
import numpy as np

df = pd.read_csv("student.csv")

def grade(Percentage):
    if Percentage >= 90:
        return "A+"
    elif Percentage >=80:
        return "A"
    elif Percentage >=70:
        return "B"
    elif Percentage >=60:
        return "C"
    elif Percentage >=50:
        return "D"
    else:
        return "F"

df["Total Marks"] = df[["Python","Maths","DBMS","English"]].sum(axis=1)
df["Percentage"] = df["Total Marks"]/4
df["Grade"]=df["Percentage"].apply(grade)


total_s = len(df["Name"])
men = len(df[df["Gender"]=="M"])
women = len(df[df["Gender"]=="F"])
hp = df["Percentage"].max()
mp = df["Percentage"].min()
ap = df["Percentage"].mean()
aa = df["Attendance"].mean()
ps = len(df[df["Percentage"]>=50][["Name","Percentage","Grade"]])
fs = len(df[df["Percentage"]<50][["Name","Percentage","Grade"]])
aas = len(df[df["Attendance"]<75][["Name","Attendance"]])
topa = df[df["Percentage"]==df["Percentage"].max()]["Name"]

print("==============================")
print("  STUDENT PERFORMANCE SYSTEM   ")
print("==============================")
print()
print("1. Show all students")
print("2. Search students")
print("3. Show Topper")
print("4. Show Average Marks")
print("5. Show Passed students")
print("6. Show Failed students")
print("7. Show Attendance Shoratge")
print("8. Show class Statistics")
print("9. Exit")


while True:
    
    try:
        
        mkv = int(input(f"\nChoose the option : "))
        
        if mkv == 1:
            print(df)
        
        elif mkv == 2:
            user=input(f"\nEnter the Student Name :")
            student = df[df["Name"].str.lower()==user.lower()]
            if student.empty:
                print("\nSorry Student not found.")
            else:
                print("\n-------STUDENT REPORT--------")
                print(f"\n{student.T.to_string(header=False)}")
                
        elif mkv == 3:
            topper_ji = df["Percentage"].max()
            topper = df[df["Percentage"]==topper_ji]
            print(f"\n------TOPPER REPORT------\n")
            print(topper.T.to_string(header=False))
            
        elif mkv == 4:
            py=df["Python"].mean()
            math=df["Maths"].mean()
            dbsm=df["DBMS"].mean()
            eng=df["English"].mean()

            print("\n------AVERAGE MARKS------")
            print()
            print(f"Python   :{py:.2f}")
            print(f"Maths    :{math:.2f}")
            print(f"DBMS     :{dbsm:.2f}")      
            print(f"English  :{eng:.2f}")
            
        elif mkv == 5:
            pas = df[df["Percentage"]>=50][["Name","Percentage","Grade"]]
            print("\n------PASSED STUDENTS-------")
            print()
            print(pas.to_string(index=False))
            print(f"\n======= Total student passed is : {len(pas)} =======")
            
        elif mkv == 6:
            fail = df[df["Percentage"]<50][["Name","Percentage","Grade"]]
            print("\n------FAILED STUDENTS-------")
            print()
            print(fail.to_string(index=False))
            print(f"\n======= Total student Failed is : {len(fail)} =======")
            
        elif mkv == 7:
            att = df[df["Attendance"]<75][["Name","Attendance"]]
            print("\n------ATTENDANCE SHORTAGE-------")
            print()
            print(att.to_string(index=False))
            print(f"\nTotal Students with Attendance Shortage : {len(att)} ")
            
        elif mkv == 8:
            print("\n====== CLASS STATISTICS ======")
            print(f"\nTotal Students      : {total_s}")
            print(f"Male Students       : {men}")
            print(f"Female Students     : {women}")
            print()
            print(f"Highest Percentage  : {hp}")
            print(f"Lowest Percentage   : {mp}")
            print()
            print(f"Average Percentage  : {ap}")
            print(f"Average Attendance  : {aa}")
            print()
            print(f"Passed Students     : {ps}")
            print(f"Failed Students     : {fs}")
            print()
            print(f"Attendance Shoratge : {aas}")
            print()
            print(f"Topper              :{topa.to_string(index=False)}")
            print("================================")
        elif mkv == 9:
            print("Exit")
            break
        else:
            print("Choose the number btw 1 to 9")
            
    except Exception as e:
        print(f"Enter the integer value here") 