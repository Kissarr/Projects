def season(number_mount):
    if number_mount == "1" or number_mount == '2' or number_mount == '3':
        print("Zima")
    elif number_mount == '4' or number_mount == '5' or number_mount == '6':
        print("Vesna")
    elif number_mount == '7' or number_mount == '8' or number_mount == '9':
        print("Leto")
    elif number_mount == '10' or number_mount == '11' or number_mount == '12':
        print ("Osen")
    else:
        print ("ERROR")

number = input("Enter number of month ")
season(number)