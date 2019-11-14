import os
import shutil

#entries = os.listdir('noscale.25g.500b.Output/')

#print(entries)



for i in range(20):
	name = 'noscale.25g.500b/R' + str(i+1)
	shutil.copy('run_paup_consensus.pl',name)
	shutil.copy('paup',name)

	os.chdir(name)

	myCmd = 'perl run_paup_consensus.pl -i Best.1 -o output'

	os.system(myCmd)

	os.remove('output.greedy')
	os.remove('output.paup')
	os.remove('output.nexus')
	os.remove('output.majority')
	os.remove('output.majority.tree')
	os.remove('output.strict')
	os.remove('output.strict.tree')
	os.remove('paup')
	os.remove('run_paup_consensus.pl')
	#coying file to SuperFine Folder
	shutil.copy('Best.1','../../SuperFine')
	shutil.copy('output.greedy.tree','../../SuperFine')
	shutil.copy('astral.tre','../../SuperFine')
	myCmd2 = 'python ./runSuperFine.py -r rmrp Best.1 output.greedy.tree -w tre'
	#changing Directory to SuperFine Folder
	os.chdir('../../SuperFine')
	os.system(myCmd2)
	copyTo = '../'+name;
	shutil.copy('Best.SuperFineTree.tre',copyTo)
	#Get the Fp and Fn Rates
	myCmd3= 'getFpFn.py -t true.tree -e Best.SuperFineTree.tre>>FpFnRate.result'
	myCmd4= 'getFpFn.py -t true.tree -e astral.tre>>FpFnRateAstral25g.result'
	os.system(myCmd3)
	os.system(myCmd4)
	#Removing unnecessary Files
	os.remove('output.greedy.tree')
	os.remove('Best.1')
	os.remove('Best.SuperFineTree.tre')
	os.remove('Best.scmTree.tre')
	os.remove('astral.tre')
	
	#for changing to initial directory
	os.chdir('..')
	
	
