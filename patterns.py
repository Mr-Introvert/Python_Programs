#right triangle
rows = 5 
for i in range(0, rows +1):
    for j in range (0, i):
        print("* ", end = "")
    print()

#inverted right triangle
rows = 5
for i in range (rows, 0, -1):
    for j in range(i, 0, -1):
        print("* ", end ="")
    print()


#right arrow triangle
rows = 5 
for i in range(0, rows +1):
    for j in range (0, i):                  #combining above two patterns 
        print("* ", end = "")
    print()
for i in range (rows-1, 0, -1):               #reduced one row 
    for j in range(i, 0, -1):
        print("* ", end ="")
    print()

