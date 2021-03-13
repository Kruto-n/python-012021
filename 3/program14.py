class Employee:
  def get_info(self):
    return f"{self.name} pracuje na pozici {self.position}."
  def __init__(self, name, position, salary, children):
    self.name = name
    self.position = position
    self.salary = salary
    self.children = children
  def get_tax(self):
    tax = self.salary * 0.15 - self.children * 1500
    return tax
  def get_net_salary(self):
    netsalary = self.salary - self.get_tax()
    return f"Cista mzda je {netsalary}"
Alena = Employee("Horakova", "chemik", 40000, 2)
print(Alena.get_info())
print(Alena.get_net_salary())