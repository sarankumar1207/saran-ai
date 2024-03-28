class Multiplecodes():
    def subfields():
        print("Sub-fields in AI are:")
        Lists=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for temp in Lists:
            print(temp)
            
    def oddeven():
        num=int(input("enter the number:"))
        if num %2==0:
            print(num,"is Even number")
        else:
                print(num,"is Odd number")
                
    def Elegible():
        gender=(input("Your Gender:"))
        age=int(input("Your Age:"))
        if(gender=="Male"):
            if(age>=21):
                print("Elegible")
        else:
            print("Not Elegible")
        if(gender=="Femle"):
            if(age>=18):
                print("Elegible")
        else:
            print("Not Elegible")
            
    def percentage():
        p1=int(input("subject1="))
        p2=int(input("subject2="))
        p3=int(input("subject3="))
        p4=int(input("subject4="))
        p5=int(input("subject5="))
        total=(p1+p2+p3+p4+p5)
        print("total:",total)
        percentage=(total/5)
        print("percentage:",percentage)
        
    def triangle():
        Height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ",(Height*breadth)/2)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        breadth=int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+breadth)    