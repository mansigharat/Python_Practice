employee = {
    'name': 'Riya',
    'dept': 'HR',
    'salary': 50000,
}
employee['bonus'] = 5000
del employee['dept']
employee.pop('bonus')

print(employee)
