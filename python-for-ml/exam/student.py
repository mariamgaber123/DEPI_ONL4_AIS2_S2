class Student:
   _id_counter =1

   def __init__(self,name):
      self.student_id=Student._id_counter
      Student._id_counter+=1
      self.name=name
      self.grades={}
      self.enroolled_courses=[]


   def __str__(self):
       return f"Student ID: {student_id} ,Name :{self.name} , Grades : {(self.grades)}"
   
   def add_grade(self,course_id,grade):
      self.grades[course_id]=grade

   def enrolled_in_course(self,course):
      self.enroolled_courses.append(course)  
