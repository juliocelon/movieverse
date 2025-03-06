import csv
 
def main():
   
    student_dic = read_dictionary("students.csv")
 
    i_number = input("Please enter an I-Number (xxxxxxxxx):  ").replace("-", "")
 
    validation = validate_i_number(i_number)

    if validation == 1 :
        if i_number in student_dic:
            print("The student with I-number", i_number, "is", student_dic[i_number])
        else:
            print("no such student")
 
def read_dictionary(students):
 
    student_dict = {}  
   
    with open(students, "rt") as student_file:
        next(student_file)  
       
        for line in student_file:
            line = line.strip()  
            data = line.split(",")  
           
            if len(data) > 1:  
                i_number = data[0]  
                name = data[1]  
                student_dict[i_number] = name  
               
    return student_dict
 
def validate_i_number(i_number):
    validation = 1 # Its a valid number
    
    if len(i_number) < 9:
        print("Invalid I-Number: too few digits")
        validation = -1
    elif len(i_number) > 9:
        print("Invalid I-Number: too many digits")
        validation = -1
    elif not i_number.isdigit():
        print("Invalid I-Number")
        validation = -1

    return validation

if __name__ == "__main__":
    main()