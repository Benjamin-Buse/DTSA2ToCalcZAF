import pandas as pd
import tkinter
import tkinter.filedialog
urllocation = tkinter.filedialog.askopenfile(title="select dtsa2 html report")
#url = r'file:///C:/Users/glxbb/Documents/DTSA-II%20Reports/2024/September/26-Sep-2024/index1.html'
url = r'file:///'+urllocation.name
tables = pd.read_html(url)
#sp500_table = tables[0]
TableNo = []
ExperimentName = []
#CNo = 0
for z in range(0,len(tables)):
    for x in tables[z].columns:
        #CNo = CNo + 1
        for y in range(0,len(tables[z])):
            #print("z,x,y")
            #print(z)
            #print(x)
            #print(y)
            if ('Sample tilt' in str(tables[z][x][y])) == True:
                print('sample tilt')
                print(z)
                for positiontable in tables[z].itertuples():
                    if positiontable[1].find('Sample tilt') != -1:
                        print(positiontable[2])
                        sampletilt = positiontable[2]
            if ('Result 1' in str(tables[z][x][y])) == True:
                print("z")
                print(z)
                print(len(tables[z]))
                print(tables[z][x][y])
                TableNo.append(z)
                #ExperimentName.append(tables[z][tables[z].columns.__getitem__(CNo)][y])
                ExperimentName.append(tables[z][x+1][y]+" "+sampletilt)
                print(tables[z][x+1][y]+" "+sampletilt)

#for a in TableNo:
#extract to variables the relevant tables of Transition,Generated,Emitted and Ratio
for a in range(0,len(TableNo)):
    for b in range(0,len(tables[TableNo[0]])):
        if 'Characteristic' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['Cht' + str(a)]=tables[TableNo[a]+1]
            vars()['Chn' + str(a)]=ExperimentName[a]
        if 'Characteristic Fluorescence' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['ChFt' + str(a)]=tables[TableNo[a]+2]
            vars()['ChFn' + str(a)]=ExperimentName[a]
        if 'Bremsstrahlung Fluorescence' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['BrFt' + str(a)]=tables[TableNo[a]+3]
            vars()['BrFn' + str(a)]=ExperimentName[a]
        if 'Comparing Characteristic to Characteristic Fluorescence' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['CChChFt' + str(a)]=tables[TableNo[a]+4]
            vars()['CChChFn' + str(a)]=ExperimentName[a]
        if 'Comparing Characteristic to Bremsstrahlung Fluorescence' == str(tables[TableNo[a]][0][b]):
            print(a)
            print(b)
            vars()['CChBrFt' + str(a)]=tables[TableNo[a]+5]
            vars()['CChBrFn' + str(a)]=ExperimentName[a]
ElCt = 0
#checkdoublecount = 0
#combine each x-ray line intensities (chr,chrfl,brfl) for each experiment into variables
#read from extracted tables the name and emitted intensity for each transition
for i in range(0,len(ExperimentName)):
    #vars()['El' + str(ElCt)]=[]
    vars()['El' + str(i)]=[]
    ElCt = 0
    for ii in range(0,len(eval('Cht'+str(i)))):
        for iii in range(0,len(eval('ChFt'+str(i)))):
            if eval('Cht'+str(i))[eval('Cht'+str(i)).columns.__getitem__(0)][ii] == eval('ChFt'+str(i))[eval('ChFt'+str(i)).columns.__getitem__(0)][iii]:
                print("yes ChFt")
                print(i)
                print(ElCt)
                #print(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0)][ii])
                #print(iii)
                vars()['Eln' + str(i) + '_' + str(ElCt)]=[]
                vars()['ElE' + str(i) + '_' + str(ElCt)]=[]
                #vars()['El' + str(ElCt)].append(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0)][ii])
                vars()['El' + str(i)].append(eval('Cht'+str(i))['Transition'][ii])
                vars()['Eln' + str(i) + '_' + str(ElCt)].append(eval('Cht'+str(i))['Transition'][ii])
                vars()['Eln' + str(i) + '_' + str(ElCt)].append(eval('ChFt'+str(i))[eval('ChFt'+str(0)).columns.__getitem__(0)][iii])
                vars()['ElE' + str(i) + '_' + str(ElCt)]=[]
                #vars()['ElE' + str(ElCt)].append(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0+1)][ii])
                vars()['ElE' + str(i) + '_' + str(ElCt)].append(eval('Cht'+str(i))['Emitted 1/msR'][ii])
                vars()['ElE' + str(i) + '_' + str(ElCt)].append(eval('ChFt'+str(i))[eval('ChFt'+str(0)).columns.__getitem__(0+2)][iii])
                print(eval('Eln' + str(i) + '_' + str(ElCt)))
                ElCt = ElCt + 1
                #checkdoublecount = 1
        for iii in range(0,len(eval('BrFt'+str(i)))):
            if eval('Cht'+str(i))[eval('Cht'+str(i)).columns.__getitem__(0)][ii] == eval('BrFt'+str(i))[eval('BrFt'+str(i)).columns.__getitem__(0)][iii]:
                print("yes BrFt")
                print(i)
                #if checkdoublecount == 1:
                ElCt = ElCt - 1
                #print(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0)][ii])
                #print(iii)
                #vars()['Eln' + str(i) + '_' + str(ElCt)]=[]
                #vars()['ElE' + str(i) + '_' + str(ElCt)]=[]
                #vars()['El' + str(ElCt)].append(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0)][ii])
                #vars()['El' + str(i)].append(eval('Cht'+str(i))['Transition'][ii])
                #vars()['Eln' + str(i) + '_' + str(ElCt)].append(eval('Cht'+str(i))['Transition'][ii])
                print(ElCt)
                print(eval('Eln' + str(i) + '_' + str(ElCt)))
                print((eval('ChFt'+str(i))[eval('BrFt'+str(0)).columns.__getitem__(0)][iii]))
                vars()['Eln' + str(i) + '_' + str(ElCt)].append(eval('BrFt'+str(i))[eval('BrFt'+str(0)).columns.__getitem__(0)][iii])
                print(eval('Eln' + str(i) + '_' + str(ElCt)))
                #vars()['ElE' + str(i) + '_' + str(ElCt)]=[]
                #vars()['ElE' + str(ElCt)].append(eval('Cht'+str(0))[eval('Cht'+str(0)).columns.__getitem__(0+1)][ii])
                #vars()['ElE' + str(i) + '_' + str(ElCt)].append(eval('Cht'+str(i))['Emitted 1/msR'][ii])
                vars()['ElE' + str(i) + '_' + str(ElCt)].append(eval('BrFt'+str(i))[eval('BrFt'+str(0)).columns.__getitem__(0+2)][iii])
                #if checkdoublecount == 0:
                ElCt = ElCt + 1
        #checkdoublecount = 0
                
#print element list for each experiment
for i in range(0,len(ExperimentName)):
    print(eval('El'+str(i)))
#print element values for each experiment
for i in range(0,len(ExperimentName)):
    print(ExperimentName[i])
    for iv in range(0, len(eval('El'+str(i)))):
        print(eval('Eln'+str(i)+'_'+str(iv)))
        print(eval('ElE'+str(i)+'_'+str(iv)))

#user select which experiment is standard
standardselectionname = []
standardselectionnum = []
import tkinter
import tkinter.messagebox
for i in range(0,len(ExperimentName)):
    standardselection = tkinter.messagebox.askquestion(title="experiment selection", message=ExperimentName[i]+'\r'+"Is this a standard")
    if standardselection == 'yes':
        standardselectionname.append(ExperimentName[i])
        standardselectionnum.append(i)

Elelm = []
for i in range(0,len(ExperimentName)):
    #print('i')
    #print(i)
    vars()['El' + str(i) + 'elm']=[]
    for iv in range(0,len(eval('El'+str(i)))):
        #print('iv')
        #print(iv)
        vars()['El' + str(i) + 'elm'].append(eval('El'+str(i)+'['+str(iv)+']'+'[:2]'))
        vars()['El' + 'elm'].append(eval('El'+str(i)+'['+str(iv)+']'+'[:2]'))
    vars()['El' + str(i) + 'elm2'] = list(dict.fromkeys(eval('El' + str(i) + 'elm')))
vars()['El' + 'elm2'] = list(dict.fromkeys(eval('El' + 'elm')))

elementstandard = []
standardelement = []
standardelementname = []
standardexperimentnum = []
for i in range(0,len(Elelm2)):
    #for iv in range(0,len(eval('El'+str(i)+'elm2'))):
    checkelementselected=0
    for ii in range(0,len(standardselectionname)):
        #standardselection = tkinter.messagebox.askquestion(title="standard selection", message=standardselectionname[ii]+'\r'+"Is this the standard for"+'\r'+eval('El'+str(i)+'elm2'+'['+str(iv)+']'))
        if checkelementselected == 0:
            standardselection = tkinter.messagebox.askquestion(title="standard selection", message=standardselectionname[ii]+'\r'+"Is this the standard for"+'\r'+Elelm2[i])
            if standardselection == 'yes':
                print(i)
                elementstandard.append(Elelm2[i])
                print(Elelm2[i])
                print(ii)
                print(standardselectionname[ii])
                standardelement.append(ii)
                standardelementname.append(standardselectionname[ii])
                standardexperimentnum.append(standardselectionnum[ii])
                checkelementselected=1

#calculate kratio
#f = open("C:/Users/glxbb/Documents/DTSA-II Reports/2024/September/26-Sep-2024/PythonKratios.txt","a")
f = open(urllocation.name.split('index1.html')[0]+'PythonKratios.txt',"a")

for i in range(0,len(ExperimentName)):
    #for each x-ray line in first one experiment then next etc
    for ii in range(0,len(eval('El'+str(i)))):
        try:
            #find standard
            print(elementstandard.index(eval('El'+str(i))[ii][:2]))
            #so experiment no is
            print(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])
            #so kratio is
            #unknown/
            #eval('ElE'+str(i)+'_'+str(ii))/
            print(eval('ElE'+str(i)+'_'+str(ii)))
            #standard intensity is - but ii needs to be determined
            #eval('ElE'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(ii))
            #standard list of elements is
            print(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])))
            #position of element for standard is
            print(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii]))
            #standard intensity is
            print(eval('ElE'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii]))))
            #so kratio is
            sum(eval('ElE'+str(i)+'_'+str(ii)))/sum(eval('ElE'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii]))))
            print(sum(eval('ElE'+str(i)+'_'+str(ii)))/sum(eval('ElE'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii])))))
            f.write(str(ExperimentName[i])+','+str(eval('El'+str(i))[ii])+','+str(sum(eval('ElE'+str(i)+'_'+str(ii)))/sum(eval('ElE'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii])))))+'\n')
        except ValueError:
            print("Element not in standard list")
            print(eval('El'+str(i))[ii][:2])
        except:
            print("Something else went wrong")
f.close()

#Read element - oxide valancies
import chemlib
df = pd.read_csv(r'C:\Users\glxbb\OneDrive - University of Bristol\element to oxidev2.csv')
#TestEle='H'
#cationsoxygens('H')

#function to return number of cations and number of oxygens
def cationsoxygens(TestEle):
    g=chemlib.Element(TestEle).AtomicNumber-1
    cat = 0
    oxy = 0
    if 'O' in str(df['oxide'][g]):
        print("yes")
        if df['oxide'][g] == 'O':
            print('oxygen as cation 1')
            print('oxygen for oxygen 0')
            cat = 1
            oxy = 0
        else:
            if df['oxide'][g].split('O')[0].split(df['element'][g])[1] == '':
                #element = 1
                print('element 1')
                cat = 1
            else:
                #element = df['oxide'][g].split('O')[0].split(df['element'][g])[1]
                print(df['oxide'][g].split('O')[0].split(df['element'][g])[1])
                cat = df['oxide'][g].split('O')[0].split(df['element'][g])[1]
            if df['oxide'][g].split('O')[1] == '':
                #oxide = 1
                print('oxide 1')
                oxy = 1
            else:
                #oxide = df['oxide'][g].split('O')[1]
                print(df['oxide'][g].split('O')[1])
                oxy = df['oxide'][g].split('O')[1]
    else:
        #element = 1
        print('element 1')
        cat = 1
        # oxide = 0
        print('oxide 0')
        oxy = 0
    return cat, oxy
            
#get from variable
#eval('k'+str(5))
#eval('k'+str(14))
#eval('k'+str(i))
f = open(urllocation.name.split('index1.html')[0]+'SimulationStandardsX.dat',"a")
#stdnum=[]
#stdelm=[]
for q in range(0,len(standardselectionname)):
    for z in range(0,len(tables)):
        for x in tables[z].columns:
            #CNo = CNo + 1
            for y in range(0,len(tables[z])):
                #print("z,x,y")
                #print(z)
                #print(x)
                #print(y)
                if ('Sample tilt' in str(tables[z][x][y])) == True:
                    print('sample tilt')
                    print(z)
                    for positiontable in tables[z].itertuples():
                        if positiontable[1].find('Sample tilt') != -1:
                            print(positiontable[2])
                            sampletilt = positiontable[2]
                if standardselectionname[q] == (str(tables[z][x][y])+' '+sampletilt):
                    print("z")
                    print(z)
                    print('q')
                    print(q)
                    print('x')
                    print(x)
                    print('y')
                    print(y)
                    #print(len(tables[z]))
                    print(tables[z][x][y])
                    f.write(str(q+1)+'         '+str(tables[z-1].columns.__getitem__(0))+'\n')
                    #stdnum.append(q+1)
                    f.write('""'+'\n')
                    f.write('-1'+'             '+str(len(tables[z-1])-2)+'\n')
                    #write density
                    f.write(tables[z-1][tables[z-1].columns.__getitem__(1)][0].split('\xa0g')[0]+'\n')
                    stdelm=[]
                    stdwtpct=[]
                    stdcations = []
                    stdoxygens = []
                    stdcations2 = []
                    stdoxygens2 = []
                    for w in range(0,len(tables[z-1])):
                        if len(tables[z-1][tables[z-1].columns.__getitem__(0)][w]) < 3:
                            #print(len(tables[z-1][tables[z-1].columns.__getitem__(0)][w]))
                            #print(tables[z-1][tables[z-1].columns.__getitem__(0)][w])
                            #f.write('"'+str(tables[z-1][tables[z-1].columns.__getitem__(0)][w])+'"')
                            stdelm.append(tables[z-1][tables[z-1].columns.__getitem__(0)][w])
                            stdwtpct.append(float(tables[z-1][tables[z-1].columns.__getitem__(1)][w])*100)
                            #print("element call")
                            #print(tables[z-1][tables[z-1].columns.__getitem__(0)][w])
                            stdcations, stdoxygens = cationsoxygens(tables[z-1][tables[z-1].columns.__getitem__(0)][w])
                            stdcations2.append(int(stdcations))
                            stdoxygens2.append(int(stdoxygens))
                            #print("return cations oxygens")
                            #print(stdcations)
                            #print(stdoxygens)
                            #print(stdcations2)
                            #print(stdoxygens2)
                            #have variable appending number of cations - calculated from code below
                            #have variable appending number of oxygens
                    #f.write('\n')
                    #f.write('   '+str(stdelm).replace("[","").replace("]","").replace(",","    "))
                    f.write('   '+str(stdelm).replace("[","").replace("]","").replace(",","    ").replace("'",'"'))
                    f.write('\n')
                    f.write('    '+str(stdcations2).replace("[","").replace("]","").replace(",","    "))
                    f.write('\n')
                    f.write('    '+str(stdoxygens2).replace("[","").replace("]","").replace(",","    "))
                    f.write('\n')
                    f.write('   '+str(stdwtpct).replace("[","").replace("]","").replace(",","    "))
                    f.write('\n')
                    f.write('"'+'"'+'             0             0            '+'"'+'"'+'            '+'"'+'"'+' ')
                    f.write('\n')
                    print("cations, oxygens")
                    #print(stdcations2)
                    #print(stdoxygens2)
                    #write line with number of cations for all elements
                    #write line with number of oxygens for all elements
f.close()                            

#create calczaf input file
f = open(urllocation.name.split('index1.html')[0]+'SimulationForCalcZAFQuant.dat',"a")
voltage = tkinter.simpledialog.askinteger('voltage','what voltage was used')
for i in range(0,len(ExperimentName)):
    #for each x-ray line in first one experiment then next etc
    #write first line
    #2 for raw -ratios, number of elements, voltage, takeoff angle, description
    #number of elements given by
    #len(eval('El'+str(i)+'elm2'))
    #next is the voltage
    f.write('2'+','+str(len(eval('El'+str(i)+'elm2')))+','+str(voltage)+','+'40.'+','+ExperimentName[i])
    f.write('\n')
    f.write('2'+','+'"'+'"'+','+'"'+'"'+',0.0,'+'"'+'"'+','+'"'+'"'+',0.0')
    f.write('\n')
    for ii in range(0,len(eval('El'+str(i)))):
        try:
            #find standard
            print(eval('El'+str(i))[ii][2:])
            #if k-line present and atomic number < 35 use k-line for quantification
            if eval('El'+str(i))[ii][2:].replace(" ","") == 'K-L3' and int(chemlib.Element(str(eval('El'+str(i))[ii][:2]).replace(" ","")).AtomicNumber) < 35:
                #Ka line
                print("Ka line")
                #find number of cations and oxygens
                print(str(eval('El'+str(i))[ii][:2]))
                testinput=(str(eval('El'+str(i))[ii][:2]))
                stdcations, stdoxygens = cationsoxygens(str(eval('El'+str(i))[ii][:2]).replace(" ",""))
                print("cations and oxygens")
                print(stdcations)
                print(stdoxygens)
                stdkratio=(sum(eval('ElE'+str(i)+'_'+str(ii)))/sum(eval('ElE'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii])))))
                print(stdkratio)
                #f.write('"'+str(eval('El'+str(i))[ii][:2]).replace(" ","")+'"'+','+'"'+'ka'+'"'+','+str(stdcations)+','+str(stdoxygens)+','+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+',0.0,'+str(stdkratio)+',0.') # kratio, zero
                f.write('"'+str(eval('El'+str(i))[ii][:2]).replace(" ","")+'"'+','+'"'+'ka'+'"'+','+str(stdcations)+','+str(stdoxygens)+','+str(int(standardelement[elementstandard.index(eval('El'+str(i))[ii][:2])])+1)+',0.0,'+str(stdkratio)+',0.') # kratio, zero
                f.write('\n')
            else:
                if eval('El'+str(i))[ii][2:].replace(" ","") == 'L3-M5':
                    #La Line
                    print("La Line")
                    #find number of cations and oxygens
                    print(str(eval('El'+str(i))[ii][:2]))
                    testinput=(str(eval('El'+str(i))[ii][:2]))
                    stdcations, stdoxygens = cationsoxygens(str(eval('El'+str(i))[ii][:2]).replace(" ",""))
                    print("cations and oxygens")
                    print(stdcations)
                    print(stdoxygens)
                    stdkratio=(sum(eval('ElE'+str(i)+'_'+str(ii)))/sum(eval('ElE'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+'_'+str(eval('El'+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])).index(eval('El'+str(i))[ii])))))
                    print(stdkratio)
                    #f.write('"'+str(eval('El'+str(i))[ii][:2]).replace(" ","")+'"'+','+'"'+'ka'+'"'+','+str(stdcations)+','+str(stdoxygens)+','+str(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])+',0.0,'+str(stdkratio)+',0.') # kratio, zero
                    f.write('"'+str(eval('El'+str(i))[ii][:2]).replace(" ","")+'"'+','+'"'+'la'+'"'+','+str(stdcations)+','+str(stdoxygens)+','+str(int(standardelement[elementstandard.index(eval('El'+str(i))[ii][:2])])+1)+',0.0,'+str(stdkratio)+',0.') # kratio, zero
                    f.write('\n')
            print(elementstandard.index(eval('El'+str(i))[ii][:2]))
            #so experiment no is
            print(standardexperimentnum[elementstandard.index(eval('El'+str(i))[ii][:2])])
        except ValueError:
            print("Element not in standard list")
            print(eval('El'+str(i))[ii][:2])
        except:
            print("Something else went wrong")
f.close()