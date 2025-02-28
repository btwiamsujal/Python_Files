class Calc:
  def __init__(self,num1,num2):
    self.num1 = num1
    self.num2 = num2
    self.menu()
    
  def menu(self):
    user_input = input("""
    Hi how can I help you?
    1. Press 1 to addition
    2. Press 2 to substraction
    3. Press 3 to multipilcation
    4. press 4 to division
    5. Anything else to exit
    """)
    
    if user_input == '1':
      self.addition()
    elif user_input == '2':
      self.substraction()
    elif user_input == '3':
      self.multipilcation()
    elif user_input == '4':
      self.division()
    else:
      exit()
      
  def addition(self):
    print("Addition of two number is: ", self.num1 + self.num2) 
    self.menu()
    
  def substraction(self):
    print("substraction of two number is: ", self.num1 - self.num2)
    self.menu()
    
  def multipilcation(self):
    print("multipilcation of two number is: ", self.num1 * self.num2)
    self.menu()
    
  def division(self):
    if(self.num2 != 0):
      print("division of two number is: ", self.num1 / self.num2)
    else:
      print("Number 2 is 0 so division can't done")
    self.menu()
    
x = int(input())
y = int(input())
a = Calc(x, y)


