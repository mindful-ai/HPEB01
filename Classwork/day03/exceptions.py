try:
    f = open(r"C:\Users\Purushotham\Desktop\Clients\HPE\B01\day03\ipconfig2.py","r")
    c = f.read()
    print(c)
    f.close()
except Exception as var:
    print('File not found')
    print(var)
finally:
    print('Operation completed!!')
