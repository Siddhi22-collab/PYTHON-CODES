#"1
# 21
# 321
# 4321
# 54321"
for i in range(1, 6):  # Outer loop for rows
    for j in range(i,0,-1):  # Loop for spaces
        print(j, end=" ")
    print()