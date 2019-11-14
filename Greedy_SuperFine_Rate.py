import os
import shutil
import time
#entries = os.listdir('noscale.25g.500b.Output/')

#print(entries)



for i in range(20):
	##Change the name of the folder here
	name = 'noscale.200g.1500b/R' + str(i+1)
	shutil.copy('run_paup_consensus.pl',name)
	shutil.copy('paup',name)

	os.chdir(name)
	start=time.time()
	myCmd = 'perl run_paup_consensus.pl -i Best.1 -o output'
	
	os.system(myCmd)
	print(time.time()-start)
	os.remove('output.greedy')
	os.remove('output.paup')
	os.remove('output.nexus')
	os.remove('output.majority')
	#os.remove('output.majority.tree')
	os.remove('output.strict')
	#os.remove('output.strict.tree')
	os.remove('paup')
	os.remove('run_paup_consensus.pl')
	#coying file to initial Folder
	shutil.copy('output.majority.tree','../..')
	shutil.copy('output.greedy.tree','../..')
	shutil.copy('output.strict.tree','../..')
	#changing Directory to initial Folder
	os.chdir('../..')
	#Get the Fp and Fn Rates
	##Change the name of the OutputFiles
	myCmd3= 'getFpFn.py -t true.tree -e output.majority.tree>>FpFnMajority.result'
	myCmd4= 'getFpFn.py -t true.tree -e output.strict.tree>>FpFnStrict.result'
	myCmd5= 'getFpFn.py -t true.tree -e output.greedy.tree>>FpFnGreedy.result'
	os.system(myCmd3)
	os.system(myCmd4)
	os.system(myCmd5)
	os.remove('output.greedy.tree')
	os.remove('output.strict.tree')
	os.remove('output.majority.tree')
	#for changing to initial directory
	#os.chdir('..')




	
	
