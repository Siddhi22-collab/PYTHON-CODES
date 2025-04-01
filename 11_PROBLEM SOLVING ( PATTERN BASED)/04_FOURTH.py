for i in range(1, 6):  # Outer loop for rows
    for j in range(5, i, -1):  # Loop for spaces
        print(" ", end=" ")
    
    for k in range(i):  # Loop for stars
        print("*", end=" ")
    
    print()  # Move to the next line