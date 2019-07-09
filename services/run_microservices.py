import subprocess


def Main(typeu):
    def UpdateDetail():
        def UpdateRelease():
            day, month, year = 0, 0, 0
            while True:
                day = int(input("enter day"))
                if day >= 1 and day <= 31:
                    break
            while True:
                month = int(input("enter month"))
                if month >= 1 and month <= 12:
                    break
            while True:
                year = int(input("enter year"))
                if year >= 1 and month <= 3000:
                    break
            releasetdate = str(day) + '/' + str(month) + '/' + str(year)
            p4 = subprocess.Popen(
                [r"C:\Users\user\source\repos\ER2019N3\ER2019N3\bin\Debug\ER2019N3.exe", pid, visitdate,
                 "DateRelease", releasetdate])
            out = str(p4.communicate())
        pid=input("enter patient's id")
        p3 = subprocess.Popen([r"C:\Users\user\source\repos\ER2019N2\ER2019N2\bin\Debug\ER2019N2.exe", pid],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = str(p3.communicate())
        if (out.__contains__("Patient exists")):
            day,month,year=0,0,0
            print("Enter visitation date")
            while True:
                day = int(input("enter day"))
                if day>=1 and day<=31:
                    break
            while True:
                month = int(input("enter month"))
                if month>=1 and month<=12:
                    break
            while True:
                year = int(input("enter year"))
                if year>=1 and month<=3000:
                    break
            visitdate=str(day)+'/'+str(month)+'/'+str(year)

            print("Choose the info you want to update")
            print("1-release date")
            print("2-Symptoms")
            print("3-Metrics")
            print("4-Diagnostic")
            print("5-Medication ")
            c=input()
            if(c=='1'):
                UpdateRelease()
            if(c=='2'):
                info=input("Enter Symptoms")
                p4 = subprocess.Popen(
                    [r"C:\Users\user\source\repos\ER2019N3\ER2019N3\bin\Debug\ER2019N3.exe", pid,visitdate , "Symptoms", info])
                out = str(p4.communicate())
            if(c=='3'):
                info = input("Enter Metrics")
                p4 = subprocess.Popen(
                    [r"C:\Users\user\source\repos\ER2019N3\ER2019N3\bin\Debug\ER2019N3.exe", pid,visitdate , "Metrics", info])
                out = str(p4.communicate())
            if(c=='4'):
                info = input("Enter Diagnostic")
                p4 = subprocess.Popen(
                    [r"C:\Users\user\source\repos\ER2019N3\ER2019N3\bin\Debug\ER2019N3.exe", pid,visitdate , "Diagnostic", info])
                out = str(p4.communicate())
            if(c=='5'):
                info = input("Enter Medication")
                p4 = subprocess.Popen(
                    [r"C:\Users\user\source\repos\ER2019N3\ER2019N3\bin\Debug\ER2019N3.exe", pid,visitdate , "Medication", info])
                out = str(p4.communicate())


    def DeleteData():
        print("what data you want to delete? ")
        print("a-medication")
        print("b-Diagnostic")
        print("c-Employee")
        c=input()
        if c=='a':
            p2 = subprocess.Popen(
                ["java", "-jar", r"C:\Users\user\Documents\NetBeansProjects\ER2019N3\dist\ER2019N3.jar", cmd['a'],
                 typeemp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p2.communicate()
            out = str(out)

            if (out.__contains__("permissiom granted")):
                med=input("Enter SSN of medication")
                p7 = subprocess.Popen(
                ["java", "-jar", r"C:\Users\user\Documents\NetBeansProjects\ER2019N2\dist\ER2019N2.jar","Medication", med],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print("Medication deleted")
            else:
                print("Access denied")
        elif c=='b':
            p2 = subprocess.Popen(
                ["java", "-jar", r"C:\Users\user\Documents\NetBeansProjects\ER2019N3\dist\ER2019N3.jar", cmd['b'],
                 typeemp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p2.communicate()
            out = str(out)
            if (out.__contains__("permissiom granted")):
                diag=input("Enter SSN of diagnostic")
                p7 = subprocess.Popen(
                    ["java", "-jar", r"C:\Users\user\Documents\NetBeansProjects\ER2019N2\dist\ER2019N2.jar","Diagnostic" ,diag],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                print("Diagnostic deleted")
            else:
                print("Access denied")
        elif c=='c':
            p2 = subprocess.Popen(
                ["java", "-jar", r"C:\Users\user\Documents\NetBeansProjects\ER2019N3\dist\ER2019N3.jar", cmd['c'],
                 typeemp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p2.communicate()
            out = str(out)
            if (out.__contains__("permissiom granted")):

                eid=input("enter id of employee")
                typee=input("Employee Type ")
                p1 = subprocess.Popen(
                    ["java", "-jar", r"C:\Users\user\Google Drive\Projects\NetBeans\ER2019\dist\ER2019.jar", eid,
                     typee], stdout=subprocess.PIPE, stderr=subprocess.PIPE)


                out, err = p1.communicate()
                out = str(out)

                if (out.__contains__("emp exist")):
                    p7 = subprocess.Popen(
                        ["java", "-jar", r"C:\Users\user\Documents\NetBeansProjects\ER2019N2\dist\ER2019N2.jar","Employee" ,eid],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    print("Employee deleted")
                else:
                    print("Employee doesn't exist")
            else:
                print("Access denied")


    print("Welcome",typeu)
    cmd = { "1": "UPDATE PATIENT DATA", "c": "DELETE EMPLOYEE", "2": "SHOW PATIENT DATA","a":"DELETE MEDICATION","b":"DELETE DIAGNOSTIC "}
    while True:
        print("1-Update details of patient")
        print("2-Show patient")
        print("3-Delete data")
        print("4-Exit")
        c=input()
        if(c=='1'):
            p2 = subprocess.Popen(
                ["java", "-jar", r"C:\Users\user\Documents\NetBeansProjects\ER2019N3\dist\ER2019N3.jar", cmd['1'],
                 typeemp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p2.communicate()
            out = str(out)
            if (out.__contains__("permissiom granted")):
                UpdateDetail()
            else:
                print("Access denied")
        elif(c=='2'):
            p2 = subprocess.Popen(
                ["java", "-jar", r"C:\Users\user\Documents\NetBeansProjects\ER2019N3\dist\ER2019N3.jar", cmd['2'],
                 typeemp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p2.communicate()
            out = str(out)
            if (out.__contains__("permissiom granted")):
                pid=input("enter id of patient")
                p5 = subprocess.Popen([r"C:\Users\user\source\repos\ER2019NEW\ER2019NEW\bin\Debug\ER2019NEW.exe", pid])
            else:
                print("Access denied")
        elif(c=='3'):
                DeleteData()
        elif(c=='4'):
            break
        else:
            print("Try again")

typ={"1":"DR","2":"NURSE","3":"SECRETARY"}
print("WELCOME TO ER 2019")

while True:

    while True:
        print("Enter employee type (DR-1,NURSE-2,Secratary-3) ")
        c=input()
        if (c in ('1','2','3')):
            break
    typeemp=typ[c]
    idDr=input("Enter user's Id ")
    #1 search for employee to see that she/he exists
    p1 = subprocess.Popen(["java", "-jar", r"C:\Users\user\Google Drive\Projects\NetBeans\ER2019\dist\ER2019.jar", idDr,typeemp],stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    out,err=p1.communicate()
    out=str(out)

    if (out.__contains__("emp exist")):
        Main(typeemp)

    else:
        print("Employee does'nt exist")
    c=input("do you want to exit? y/n ")
    if (c=='y'):
        break
print("good bye")
input()






