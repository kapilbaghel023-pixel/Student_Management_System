# student management system
class Student:
    def new_addmision(self):
        try:    
            print("-------------------------------------------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------------------------------------------")
            roll_no=input("enter student roll number").strip()
            name=input(str("enter student name")).strip().lower()
            print("-------------------------------------------------------------------------------------------------------------")
            clss=input("enter i whichi class in addit in student")
            print("-------------------------------------------------------------------------------------------------------------")
            previose_colifiication=input("enter student prives qulification")
            print("-------------------------------------------------------------------------------------------------------------")
            prives_instritute_name=input("enter stutent prives instrute daitails")
            print("-------------------------------------------------------------------------------------------------------------")
            addhar_no=input("emter student addhar number")
            print("-------------------------------------------------------------------------------------------------------------")
            father_name=input(str("enter student father's name"))
            print("-------------------------------------------------------------------------------------------------------------")
            mother_name=input(str("enter student mother's name"))
            print("-------------------------------------------------------------------------------------------------------------")
            print("-------------------------------------------------------------------------------------------------------------")
            student={"roll_number":roll_no,
                "name": name,
            "class":clss,
            "previose_colifiication":previose_colifiication,
            "prives_instritute_name":prives_instritute_name,
            "student_detaile":{
                "addhar_no":addhar_no,
                "father_name":father_name,
                "mother_name":mother_name}} 
            with open(roll_no,"w") as f:
                  data = f.write(str(student))
            return "student sucssefully admit in your form"
        except Exception as e:
            print("pleace cheak your input",e)
    
    def add(self):
        try:
            roll_no=input("enter student roll_no").lower().strip()
            add=input("enter deatels please click for next line\n")
            with open(roll_no,"a") as f:
                data = f.write(add)
            return "sucsefully add your detail"
        except Exception as e:
            print("pleace cheak your input",e)
         
    def show_detail(self):
        try:
            roll_no=input("enter student roll_no").strip().lower()
            print("-------------------------------------------------------------------------------------------------------")
            with open(roll_no,"r") as f:
                data = f.read()
                return data

        except Exception as e:
            print("pleace cheak your input",e)
    print("-------------------------------------------------------------------------------------------------------")
    
    def update(self):
        try:
            roll_no=input("enter student roll_no")
            print("-------------------------------------------------------------------------------------------------------")
            with open(roll_no,"r") as f:
                lines = f.readlines()
                print(lines)
            line=int(input("enter which line are update "))
            old_word=input("enter which word are update")
            new_word=input("entr updated word ")
            lines[line] = lines[line].replace(old_word,new_word)
            with open(roll_no,"w") as f:
                f.writelines(lines)
        except Exception as e:
            print("pleace cheak your input",e)    
            
        
    def deliet(self):
        import os
        try:
            roll_no=input("enter student roll_no").strip().lower()
            print("-------------------------------------------------------------------------------------------------------")
            with open(roll_no,"r") as f:
                data = f.read()
                os.remove(roll_no)
        except Exception as e:
            print("pleace cheak your input",e)            

    def add_result(self):
        try:
            roll_no=input("enter student roll_no").strip().lower()
            ns1=input("enter first subject name").strip().lower()
            sub1=int(input("enter first subject number"))
            ns2=input("enter second subject name").strip().lower()
            sub2= int(input("enter second subject nuber"))
            ns3=input("enter third subject name").strip().lower()
            sub3=int(input("enter thired subject number"))
            r=((sub1+sub2+sub3)*100)/300
        
            with open(roll_no,"a") as f:
               
               data = f.write("\nTHE STUDENT REPORT CARD IS\n ")
               data =f.write(ns1)
               data=f.write(" = ")
               data = f.write(str(sub1))
               data = f.write("\n ")
               data = f.write(ns2)
               data = f.write(" = ")
               data = f.write(str(sub2))
               data  = f.write("\n ")
               data =f.write(ns3)
               data= f.write(" = ")
               data = f.write(str(sub3))
               data=f.write("\n student achived a : ")
               data =f.write(str(r))
               data = f.write("%")
               return data
        except Exception as e:
            print("pleace check your input details",e)




r1 = Student()

while True:
    print("\n--- Student Management System ---")
    print("1. New Admission")
    print("2. Show Details")
    print("3. Add Extra Detail")
    print("4. Update Detail")
    print("5. Delete Student")
    print("6. Add Result")
    print("7. Exit")

    choice = input("Enter choice: ")
    try:

        if choice == "1":
            print(r1.new_addmision())
        elif choice == "2":
            print(r1.show_detail())
        elif choice == "3":
            print(r1.add())
        elif choice == "4":
            r1.update()
        elif choice == "5":
            r1.deliet()
        elif choice == "6":
            r1.add_result()
        elif choice == "7":
            print("Thank you for using Student Management System ✅")
            break
    except FileNotFoundError as e:    
        print("Invalid choice ❌",e)
