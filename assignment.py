     #Assignment
#Given a sample list,student_names =["Sandra","Patricia","Phionah","Anitah"]
#and student_marks = [80,56,78,90]
#(a) Print Patricia,faith,phionah and anitah
#(b) Add masha at the forth position
# (c) Update the name Phionah to Phionah Aladinah
# (d) Display the length of the student's list
# (e) Print all the student names using a for loop
# (f) Calculate the total marks for the student marks variable and the answer is 304

 #solution
student_names =["Sandra","Patricia","Phionah","Anitah"]
student_marks = [80,56,78,90]


# (a)Print Patricia,faith,phionah and anitah
print(student_names[1])
print("Faith")
print(student_names[2])
print(student_names[3])

#(b) Add masha at the forth position
student_names.insert(3,'Masha')
print(f"\nThe updated list is {student_names}"'\n\n')

# (c) Update the name Phionah to Phionah Aladinah
student_names[2] = "Phionah Aladina"
print(f"\nThe updated list of names is {student_names}"'\n\n')

# (d) Display the length of the student's list
print(f"The number of students is :",len(student_names)) 

# (e) Print all the student names using a for loop
for name in student_names:
     print(name)

#total marks
total_marks = sum(student_marks)
print(f"\nThe total marks for student's marks is : {total_marks}"'\n\n')

