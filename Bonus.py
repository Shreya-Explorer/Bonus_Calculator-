import sys
if len(sys.argv)== 2:
  script_name=sys.argv[0]
  salary= sys.argv[1]
else:
  script_name=sys.argv[0]
  salary=500000
bonus=(salary)*0.1
total_salary=salary+bonus
print("Salary = ",salary)
print("Bonus =",bonus)
print("Total Salary =",total_salary)
