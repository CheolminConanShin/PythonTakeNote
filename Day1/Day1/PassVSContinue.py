list = [1,2,3,4,5,6,7]
for item in list:
    print("inside for loop : " + str(item))
    if item > 3:
        pass
    print("inside if statement : " + str(item))

# pass는 if문 안에있는 처리문만 skip, continue는 for문 한 스텝을 skip