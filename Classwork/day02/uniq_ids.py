EMP = {}

emp_id = 1
temp = '000000'
const = '9999'

while True:

    name = input('Enter employee name: ')
    if(name == 'quit'):
        break

    temp_id = temp + str(emp_id)
    real_id = const + temp_id[len(temp_id)-4:]

    EMP.setdefault(real_id, name)
    emp_id += 1

print('EMPLOYEES')
for key in EMP.keys():
    print(EMP[key] + ' ---------> ' + key)

    
