School Management System

This is a basic implementation of a School Management System using Python classes. The School class has methods to manage school's students and staff information.
Features

    Add and remove students
    Add and remove staff members
    Display student and staff lists

Getting started

To use the code, you need to instantiate a School object and pass the name of the school as an argument. Then, you can use the available methods to manage the students and staff information.

scss

ps_118 = School('PS 118')
ps_118.add_student('Arnold')
ps_118.add_student('Gerald')

ps_118.add_staff('Mr.Wartz', 'principal')
ps_118.add_staff('Mr. Robert Simmons', '4th grade teacher')

print(ps_118.display_student_list())
print(ps_118.display_staff_list())

Contributing

Feel free to suggest improvements and make contributions to the code.
