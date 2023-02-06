class School:

  def __init__(self, school_name):
    self.school_name = school_name
    self.__students = {}
    self.__staff = {}

  def add_student(self, name, description='student'):
    self.__students[name] = description

  def remove_student(self, name):
    self.__students.pop(name)
    return f'{name} has been removed from the school student list.'

  def display_student_list(self):
    result = f'Here is the list of {self.school_name} students:\n\n'
    for name, desc in self.__students.items():
      result += f'{name}\n'
    return result

  def add_staff(self, name, position):
    self.__staff[name] = position

  def remove_staff(self, name):
    self.__staff.pop(name)
    return f'{name} has been removed from the school staff list.'

  def display_staff_list(self):
    result = f"Here's the list of {self.school_name} staff members with their position:\n\n"
    for name, position in self.__staff.items():
      result += f'{name}, {position}\n'
    return result


ps_118 = School('PS 118')
ps_118.add_student('Arnold')
ps_118.add_student('Gerald')
ps_118.add_student('Helga')
ps_118.add_student('Phoeby')
ps_118.add_student('Stinky')

ps_118.add_staff('Mr.Wartz', 'principal')
ps_118.add_staff('Mr. Robert Simmons', '4th grade teacher')
ps_118.add_staff('Miss Slovak', '4th grade teacher')

print(ps_118.display_student_list())

print(ps_118.remove_student('Stinky'))

print(ps_118.display_student_list())

print(ps_118.display_staff_list())

print(ps_118.remove_staff('Miss Slovak'))
