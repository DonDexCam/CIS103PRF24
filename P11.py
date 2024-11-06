import datetime
def writerr(emsg,filept,line):
    line = line.strip()
    outline = line+','+emsg+'\n'
    filept.write(outline)
def writegd(letter,filept,line):
    line = line.strip()
    outline = line+','+letter+'\n'
    filept.write(outline)



# Get the current date and time
now = datetime.datetime.now()

# Print the current date and time
print("Current date and time:", now)

def Points_to_Grades(fpoints):
    if (fpoints>=900) and (fpoints<1000):
        Grades='A'
        print('Grade is',Grades)
    else:
        if (fpoints>=800) and (fpoints<899):
            Grades='B'
            print('Grade is',Grades)
        else:
            if (fpoints>=700) and (fpoints<799):
                Grades='C'
                print('Grade is,',Grades)
            else:
                if (fpoints>=600) and (fpoints<699):
                    Grades='D'
                    print('Grade is,',Grades)
                else:
                    Grades='F'
                    print('Grade is,',Grades)
        
       

            
    return Grades             


def main():
    filenamein = 'c:/temp/points.txt'
    filenameout1 = 'c:/temp/grades.txt'
    filenameout2 = 'c:/temp/error.txt'
    rcdcnt = 0
    Goodcnt = 0
    Errcnt = 0

    Acount=0
    Bcount=0
    Ccount=0
    Dcount=0
    Fcount=0

    
    infile = open(filenamein, 'r')
    out1 = open(filenameout1, 'w')   #goodfile
    out2 = open(filenameout2, 'w')   #errorfile
    line = infile.readline()
    while(line !=""):
        rcdcnt = rcdcnt + 1
        #print(line)
        (ID,Name,Points) = line.split(',')
        Points=Points.strip()
        #print('Id number:' +ID)
        #print('Name is:' +Name)
        #print('points are:' +Points)   
        #print('line before split:'+line)
        try:
            fpoints=float(Points)
            if(fpoints)<0:
                #print('points less than zero',fpoints)
                errmsg = 'points less than zero'
                writerr(errmsg,out2,line)
                Errcnt = Errcnt + 1
    
            else:
                if(fpoints)>1000:
                    #print('points must be between 0-1000',fpoints)
                    errmsg = 'points must be between 0-1000'
                    writerr(errmsg,out2,line)
                    Errcnt = Errcnt + 1
                    
                else:
                    letter=Points_to_Grades(fpoints)
                    writegd(letter,out1,line)
                    Goodcnt = Goodcnt+1
                    if letter == 'A':
                        Acount= Acount+1
                    elif letter == 'B':
                        Bcount=Bcount+1
                    elif letter == 'C':
                        Ccount = Ccount+1
                    elif letter == 'D':
                        Dcount = Dcount+1
                    elif letter == 'F':
                        Fcount=Fcount+1
        except:
            #print("Points are in error",Points)
            errmsg = 'Points are in error'
            writerr(errmsg,out2,line)
            Errcnt = Errcnt + 1
       

        line = infile.readline()
           
    infile.close()
    infile.close()
    out1.close()
    out2.close()
    print('\n'+'Records read ',rcdcnt)
    print('\n'+ 'Number of good grades ',Goodcnt)
    print('\n'+ 'Number of errors ',Errcnt)

    print('Grade Counts')
    print('number of A:',Acount)
    print('number of B:',Bcount)
    print('number of C:',Ccount)
    print('number of D:',Dcount)
    print('number of F:',Fcount)
    
    
    now = datetime.datetime.now()
    print("Current date and time:", now)
main()


