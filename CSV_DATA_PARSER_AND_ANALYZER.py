n=int(input("Enter The Number Of Employees:"))
employee_dataset = []
for i in range(n):
    NAME=input("Enter The Name Of Employee:")
    DEPARTMENT=input("Enter The Department Of The Employee:")
    SALARY=int(input("Enter The Salary Of The Employee:"))
    EXPERIENCE=int(input("Enter The Experience Of The Employee:"))
    employee_dataset.append({"NAME":NAME,"DEPARTMENT":DEPARTMENT,"SALARY":SALARY,"EXPERIENCE":EXPERIENCE})
total_salary = 0
max_salary = 0
min_salary =float('inf')
ds_dept_count = 0
for employee in employee_dataset:
    current_salary = employee["SALARY"]
    total_salary += current_salary
    if current_salary > max_salary:
        max_salary = current_salary
    elif current_salary < min_salary:
        min_salary = current_salary
    if employee["DEPARTMENT"] == "Data Science":
        ds_dept_count += 1
num_records = len(employee_dataset)
if num_records>0:
    average_salary = total_salary / num_records
else:
    average_salary=0.0
    min_salary=0
print(" DATASET SUMMARY STATISTICS ")
print("=" * 40)
print(f"Total Records Analysed: {num_records}")
print(f"Average Salary       : {average_salary:.2f}")
print(f"Highest Salary       : {max_salary}")
print(f"Lowest Salary        : {min_salary}")
print(f"Data Science Team Size: {ds_dept_count} employees")
print("=" * 40)
