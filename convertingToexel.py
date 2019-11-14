import xlsxwriter 
##Change the name of the output file here
workbook = xlsxwriter.Workbook('result.xlsx') 

worksheet = workbook.add_worksheet() 
  
cnt = 1
fp_greedy = 0
fn_greedy = 0
##Change the name of the file here
filepath = 'FpFnGreedy.result'
with open(filepath) as fp:
    line = fp.readline()
    line = line.replace('(','')
    line = line.replace(')','')
    mylist = line.split(",")
    print(mylist[0])
    r1='A'+str(cnt)
    cnt+=1
    r2='A'+str(cnt)
    cnt+=1
    worksheet.write(r1, mylist[0]) 
    worksheet.write(r2, mylist[1]) 
    fp_greedy = fp_greedy+float(mylist[0])
    fn_greedy = fn_greedy+float(mylist[1])
    while line:
	if(cnt>40):
		break;
        line = fp.readline()
	line = line.replace('(','')
    	line = line.replace(')','')
	mylist = line.split(",")
    	#print(mylist[0])
	r1='A'+str(cnt)
    	cnt+=1
    	r2='A'+str(cnt)
 	cnt+=1
    	worksheet.write(r1, mylist[0]) 
    	worksheet.write(r2, mylist[1])
	fp_greedy = fp_greedy+float(mylist[0])
    	fn_greedy = fn_greedy+float(mylist[1])
cnt = 1
fp_majority = 0
fn_majority = 0
##Change the name of the file here
filepath = 'FpFnMajority.result'
with open(filepath) as fp:
    line = fp.readline()
    line = line.replace('(','')
    line = line.replace(')','')
    mylist = line.split(",")
    print(mylist[0])
    r1='B'+str(cnt)
    cnt+=1
    r2='B'+str(cnt)
    cnt+=1
    worksheet.write(r1, mylist[0]) 
    worksheet.write(r2, mylist[1]) 
    fp_majority = fp_majority+float(mylist[0])
    fn_majority = fn_majority+float(mylist[1])
    while line:
	if(cnt>40):
		break;
        line = fp.readline()
	line = line.replace('(','')
    	line = line.replace(')','')
	mylist = line.split(",")
    	#print(mylist[0])
	r1='B'+str(cnt)
    	cnt+=1
    	r2='B'+str(cnt)
 	cnt+=1
    	worksheet.write(r1, mylist[0]) 
    	worksheet.write(r2, mylist[1])
	fp_majority = fp_majority+float(mylist[0])
    	fn_majority = fn_majority+float(mylist[1])
cnt = 1
#fp_strict = 0
fn_strict = 0.0
##Change the name of the file here
filepath = 'FpFnStrict.result'
with open(filepath) as fp:
    line = fp.readline()
    line = line.replace('(','')
    line = line.replace(')','')
    mylist = line.split(",")
    print(mylist[0])
    r1='D'+str(cnt)
    cnt+=1
    r2='D'+str(cnt)
    cnt+=1
    worksheet.write(r1, mylist[0]) 
    worksheet.write(r2, mylist[1]) 
    #fp_strict = fp_strict+float(mylist[0])
    fn_strict = fn_strict+float(mylist[1])
    while line:
	if(cnt>40):
		break;
        line = fp.readline()
	line = line.replace('(','')
    	line = line.replace(')','')
	mylist = line.split(",")
    	#print(mylist[0])
	r1='D'+str(cnt)
    	cnt+=1
    	r2='D'+str(cnt)
 	cnt+=1
    	worksheet.write(r1, mylist[0]) 
    	worksheet.write(r2, mylist[1])
        #fp_strict = fp_strict+float(mylist[0])
        fn_strict = fn_strict+float(mylist[1])
workbook.close() 
print(str(fn_strict))
f = open("fpAvg.txt", "a")
f.write("g "+str(fp_greedy/20)+"\nmajo "+str(fp_majority/20))
f.close()

f = open("fnAvg.txt", "a")
f.write("g "+str(fn_greedy/20)+"\nmajo "+str(fn_majority/20)+"\nst "+str(fn_strict/20))
f.close()
