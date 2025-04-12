class allclasses():
    def Subfields():
        l1 = ("Machine Learning","Neural Networks","Vision,Robotics","Speech Processing","Natural Language Processing")
        for l in l1:
            print(l)
            
    def OddEven():
        num = int(input("Enter a number : "))
        if num % 2 == 0:
            print(num, "is Even number")
        else:
            print(num, "is Odd number")      

    def Elegible():
        age = int (input("Enter your age :"))
        gender = input("Enter your gender (Male/Female) :")
        print("Your Gender : ", gender)
        print("Your Age : ", age)
        if gender == "Male" and age < 21:
            print("Not Eligible")
        elif gender == "Female" and age < 18:
            print("Not Eligible")
        else:
            print("Eligible")

    def percentage():
        tot = 0
        m = 0
        marks = (98, 87, 95, 95, 93)
        for i in marks:
            m += 1
            tot += i
            print("Subject" + str(m) + " = " + str(i))
        print("Total:", tot)
        print("Percentage:", (tot / len(marks)))

    def triangle():
        # Area calculation
        height = 32
        breadth = 34
        print("Height:", height)
        print("Breadth:", breadth)
        print("Area formula: (Height*Breadth)/2")
        area = (height * breadth) / 2
        print("Area of Triangle:", area)

        # Perimeter calculation
        height1 = 2
        height2 = 4
        breadth = 4
        print("Height1:", height1)
        print("Height2:", height2)
        print("Breadth:", breadth)
        print("Perimeter formula: Height1+Height2+Breadth")
        perimeter = height1 + height2 + breadth
        print("Perimeter of Triangle:", perimeter)


