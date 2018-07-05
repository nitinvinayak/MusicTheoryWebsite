"""Code for creating all the MusicElements in form of Html tags"""

notes=["A ","A#","B ","C ","C#","D ","D#","E ","F ","F#","G ","G#"]
notesnormal=["A ","  ","B ","C ","  ","D ","  ","E ","F ","  ","G ","  "]
strings={7:"E ",2:"B ",10:"G ",5:"D ",0:"A ",7:"E "}                #according to index of list notes

print("Select any option:")
print("1 for CHORDS" )
print("2 for SCALES" )
print("3 for FRETBOARD" )
print("4 for NORMAL FRETBOARD")
print("5 for empty FRETBOARD")
choice=input("Enter your choice: ")
if (choice==1):
    majformula=[4,3]
    minformula=[3,4]

    ofile=open("Chords.txt",'w')
    ofile.write("MAJOR CHORDS\n")
    for scale in range(len(notes)):
                ofile.write("</tr>\n")
                ofile.write("<tr>\n")
                ofile.write("<td>"+notes[scale]+"</td>"+'\n')
                majind=0
                num=scale
                i=1
                while i<=3:
                            i=i+1
                            ofile.write("<td>"+notes[num]+"</td>"+'\n')
                            num=num+majformula[majind]
                            majind=majind+1
                            if (majind>=2):
                                        majind=majind-2
                            if(num>=12):
                                        num=num-12
    ofile.write("</tr>\n")
    ofile.close()

    ofile=open("Chords.txt",'a')
    ofile.write("MINOR CHORDS\n")
    for scale in range(len(notes)):
                ofile.write("</tr>\n")
                ofile.write("<tr>\n")
                ofile.write("<td>"+notes[scale]+"</td>"+'\n')
                minind=0
                num=scale
                i=1
                while i<=3:
                            i=i+1
                            ofile.write("<td>"+notes[num]+"</td>"+'\n')
                            num=num+minformula[minind]
                            minind=minind+1
                            if (minind>=2):
                                        minind=minind-2
                            if(num>=12):
                                        num=num-12
    ofile.write("</tr>\n")
    ofile.close()
elif(choice==2):
    majformula=[2,2,1,2,2,2,1]
    minformula=[2,1,2,2,1,2,2]

    ofile=open("Scales.txt",'w')
    ofile.write("MAJOR SCALES\n")
    for scale in range(len(notes)):
                ofile.write("</tr>\n")
                ofile.write("<tr>\n")
                ofile.write("<td>"+notes[scale]+"</td>"+'\n')
                majind=0
                num=scale
                i=1
                while i<=8:
                            i=i+1
                            ofile.write("<td>"+notes[num]+"</td>"+'\n')
                            num=num+majformula[majind]
                            majind=majind+1
                            if (majind>=7):
                                        majind=majind-7
                            if(num>=12):
                                        num=num-12
    ofile.write("</tr>\n")
    ofile.close()

    ofile=open("Scales.txt",'a')
    ofile.write("MINOR SCALES\n")
    for scale in range(len(notes)):
                ofile.write("</tr>\n")
                ofile.write("<tr>\n")
                ofile.write("<td>"+notes[scale]+"</td>"+'\n')
                minind=0
                num=scale
                i=1
                while i<=8:
                            i=i+1
                            ofile.write("<td>"+notes[num]+"</td>"+'\n')
                            num=num+minformula[majind]
                            minind=minind+1
                            if (minind>=7):
                                        minind=minind-7
                            if(num>=12):
                                        num=num-12
    ofile.write("</tr>\n")
    ofile.close()
elif(choice==3):
    ofile=open("Fretboard.txt",'w')
    ofile.write("FRETBOARD\n")
    for note in [7,2,10,5,0,7]:
                ofile.write("</tr>\n")
                ofile.write("<tr>\n")
                num=note
                i=0
                while i<=22 :
                            i=i+1
                            ofile.write("<td>"+notes[num]+"</td>"+'\n')
                            num=num+1
                            if(num>=12):
                                        num=num-12
    ofile.write("</tr>\n")
    ofile.close()
elif(choice==4):
    ofile=open("FretboardNormal.txt",'w')
    ofile.write("FRETBOARDNORMAL\n")
    for note in [7,2,10,5,0,7]:
                ofile.write("</tr>\n")
                ofile.write("<tr>\n")
                num=note
                i=0
                while i<=22 :
                            i=i+1
                            ofile.write("<td>"+notesnormal[num]+"</td>"+'\n')
                            num=num+1
                            if(num>=12):
                                        num=num-12
    ofile.write("</tr>\n")
    ofile.close()
elif(choice==5):
    ofile=open("FretboardEmpty.txt",'w')
    ofile.write("FRETBOARDEmpty\n")
    for note in [7,2,10,5,0,7]:
                ofile.write("</tr>\n")
                ofile.write("<tr>\n")
                num=note
                i=0
                while i<=22 :
                            i=i+1
                            ofile.write("<td>"+" "+"</td>"+'\n')
                            num=num+1
                            if(num>=12):
                                        num=num-12
    ofile.write("</tr>\n")
    ofile.close()
