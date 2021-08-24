def is_year_leap(Year):
    if Year % 4 == 0:
        print("True")
    else:
        print("False")


Year = int(input())
is_year_leap(Year)
