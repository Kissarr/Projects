def kaprekar_step(L):
    z = sorted(L)
    min = (str(z[0])+str(z[1])+str(z[2])+str(z[3]))
    max = (str(z[3]) + str(z[2]) + str(z[1]) + str(z[0]))
    print(max)
    print(min)
    return int(max) - int(min)


kaprekar_step([8, 6, 5, 4])