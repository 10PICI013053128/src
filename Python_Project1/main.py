import getopt,sys
import csv
import time
from Random_Database import randomDB

def names(n):
	'''Displays names of freedom fighters'''
	z=0
	while z!=n:
                print dt['name'][z]
                z=z+1

def gender1(gen):
	'''Checks the gender given in command line'''
	i=0
	j=-1
        if gen=='Female' or gen=='female':
                for i in dt['gender']:
                        j=j+1
                        if i==gen:
                                print dt['name'][j],"\t\t\t"
				print dt['gender'][j],"\n"
	else:
		print "No female freedom fighters"

def achieve(ach,num1):
	'''Displays the name and achievements of freedom fighters'''
	p=0
	for q in dt['region']:
		while p!=num1:
			if q=='india' or q=="southindia" or q=="northindia" or q=='india':				
				print dt['name'][p],"\t\t\t"
				print dt['achievements'][p],"\n"
				p=p+1
			
def region1(reg):
	'''Checks if the region given in command line argument is same as in the dictionary and displays only those names'''
	x=-1
	if reg=='southindia' or reg=='SouthIndia' or reg=='southIndia':
		for k in dt['region']:
			x=x+1
			if k==reg or k=="southindia" or k=="SouthIndia" or k=="southIndia":
				print dt['name'][x],"\t\t\t"
				print dt['region'][x],"\n"
	else:
		print "No freedom fighters from Southern India"
def det(num):
	"""Displays the details of freedom fighters"""
	y=0
	while y!=num:
		print "Name: ",dt['name'][y],"\n",
		print "Gender: ",dt['gender'][y],"\n",
		print "Birth Date: ",dt['birth_date'][y],"\n",
		print "Death Date: ",dt['death_date'][y],"\n",
		print "Region: ",dt['region'][y],"\n",
		print "Achievements: ",dt['achievements'][y],"\n",
		print "Other Names: ",dt['other_names'][y],"\n",
		print "\n"
		y=y+1


flagn=0
flagg=0
flagr=0
flagd=0
flagt=0
flagf=0
flaga=0

rec=0
gen=0
reg=0
num=0
n=0
ach=0 

ls=[]
name=[]
gender=[]
bd=[]
dd=[]
region=[]
ac=[]
on=[]

starttime=time.clock()

#reading comma seperated values from a file
q=0
f=open("database.txt","r")
reader = csv.reader(f)
for line in reader:
	rec=rec+1
        ls.extend(line) 

#taking the input from a file into seperate lists
for q in range(0,len(ls),7):
	name.append(ls[q])

for q in range(1,len(ls),7):
	gender.append(ls[q])

for q in range(2,len(ls),7):
	bd.append(ls[q])

for q in range(3,len(ls),7):
	dd.append(ls[q])

for q in range(4,len(ls),7):
	region.append(ls[q])

for q in range(5,len(ls),7):
	ac.append(ls[q])

for q in range(6,len(ls),7):
	on.append(ls[q])
	        
#creating a dictionary
dt={'name':name,'gender':gender,'birth_date':bd,'death_date':dd,'region':region,'achievements':ac,'other_names':on}

#taking command line arguments
optlist,args=getopt.getopt(sys.argv,'ngdtarf:')

#checking using flags which command line arguments have been given
for arg in sys.argv:
        if arg=='-n':
                flagn=1
        if arg=='-g':
                flagg=1
        if arg=='-r':
                flagr=1
        if arg=='-d':
                flagd=1
        if arg=='-t':
                flagt=1
        if arg=='-f':
                flagf=1
        if arg=='-a':
                flaga=1

#accepting the command line arguments for futher computation
if flagn==1 and flagg==1 and flagf==1 and flagr==0 and flagd==0 and flagt==0 and flaga==0:
        if sys.argv[2]=='name' and sys.argv[6]=='freedomfighters':
                if sys.argv[4]=='female'or sys.argv[4]=='Female'or sys.argv[4]=='Male' or sys.argv[4]=='male':
                        gen=sys.argv[4]
                else:
                        print "Usage: -g female or -g male"
                        gen=0
                        exit(0)
        else:
                print "Usage -n name -g <female or male> -f freedomfighters"
                exit(0)

if flagn==1 and flagr==1 and flagf==1 and flagg==0 and flagd==0 and flagt==0 and flaga==0:
        if sys.argv[2]=='name' and sys.argv[6]=='freedomfighters':
                if sys.argv[4]=='SouthIndia' or sys.argv[4]=='southindia' or sys.argv[4]=='southIndia':
                        reg=sys.argv[4]
                else:
                        print "This is not supported"
                        reg=0
                        exit(0)
        else:
                print "Usage -n name -r <SouthIndia or southindia or southIndia> -f freedomfighters"

if flagd==1 and flagt==1 and flagf==1 and flagg==0 and flagr==0 and flagn==0 and flaga==0:
        if sys.argv[2]=='details' and sys.argv[6]=='freedomfighters':
		if int(sys.argv[4])<=rec:
                        if sys.argv[4].isdigit():
                                num=int(sys.argv[4])
                        else:
                                print "Usage: -t <number>"
                                num=0
                                exit(0)
		else:
			print "Number of names asked exceeds the number of database records"
			exit(0)
        else:
                print "Usage -d details -t <number> -f freedomfighters"
                exit(0)

if flagn==1 and flagt==1 and flagf==1 and flagr==1 and flagg==0 and flagd==0 and flaga==0:
        if sys.argv[2]=='name' and sys.argv[8]=='freedomfighters':
		if sys.argv[6]=='india' or sys.argv[6]=='India' or sys.argv[6]=='SouthIndia' or sys.argv[6]=='southindia' or sys.argv[6]=='southIndia' or sys.argv[6]=='NorthIndia' or sys.argv[6]=='northindia' or sys.argv[6]=='northIndia':
			if int(sys.argv[4])<=rec:
                        	if sys.argv[4].isdigit():
                        	        n=int(sys.argv[4])
                        	else:
                                	print "Usage: -t <number>"
                                	n=0
                               		exit(0)
			else:
				print "Number of names asked exceeds the number of database records"
				exit(0)
		else:
			print "This country ",sys.argv[6]," is not supported"
			exit(0)         
	else:
                print "Usage -n name -t <number> -r <india or southindia or north india> -f freedomfighters"
                exit(0)

if flagn==1 and flagr==1 and flaga==1 and flagf==1 and flagt==1 and flagg==0 and flagd==0:
        if sys.argv[2]=='name' and sys.argv[10]=='freedomfighters':
		if sys.argv[8]=='india' or sys.argv[8]=='India':
			if int(sys.argv[6])<=rec:
                        	if sys.argv[4] and sys.argv[6]:
                                	ach=sys.argv[4]
					num1=int(sys.argv[6])
                        	else:
                                	print "Usage: -a achievements -t <number>"
                               		ach=0
                                	exit(0)
			else:
				print "Number of names asked exceeds the number of database records"
				exit(0)
		else:
			print "This country ",sys.argv[8]," is not supported"
			exit(0)        
	else:
 		print "Usage -n name -a achievements -t <number> -r india  -f freedomfighters"
                exit(0)


#names of n number of freedom fighters
if n:
        print "List of names of ",n," freedom fighters:"
	print "NAMES:"
	print
	names(n)

#names of all female freedom fighters
elif gen:
        print "The names of the female freedom fighters are:"
	print "NAMES & GENDER:"
	print
	gender1(gen)

#names and achievements of all freedom fighters
elif ach:
	print "List of freedom fighters of India and their achievements are:"
	print "NAMES & ACHIEVEMENTS:"
	print
	achieve(ach,num1)
	
#names of all freedom fighters of southern india
elif reg:
	print "The names of all freedom fighters of Southern india are:"
	print "NAMES & Region:\n"	
	region1(reg)
	
#details of alteast t number of freedom fighters
elif num:
	print "The details of ",num," number of freedom fighters are:"
	det(num)
	
else:
	print "Invalid input entered.Please enter valid arguments."
endtime=time.clock()
time_elapsed=endtime-starttime;

print "Time taken for the query to be executed:",time_elapsed," seconds"
