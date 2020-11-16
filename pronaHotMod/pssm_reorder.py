import os
import os.path
import sys
from pronaHotMod.lib_parser import *
from pronaHotMod.lib_featurize import *
import random
import numpy as np

np.random.seed(0)
random.seed( 0 )

def expand_list(nested_list):
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            for sub_item in expand_list(item):
                yield sub_item
        else:
            yield item



def extract_features(pp_path ,feature_file):
	if pp_path[-1] != '/':
		pp_path += '/'

	feature_space = []
	
	fea_win = {}

	for l in open(feature_file):
		l = l.rstrip()
		t = l.split('\t')
		fea_win[t[0]] = int(t[1])	
	#Look which pp features are defined in the config and parse those

	try:
		d_in = open(pp_path+"query.in").read()
		d_fasta = open(pp_path+"query.fasta").read()
		pp_seq,pro = parse_sequence(d_in, d_fasta)
		seq = pp_seq['seq']	
	except IOError:
 		sys.exit("Error!!!ProNAHot can not be done for protein %s.\nFile *.in and/or *.fasta not found...\n" % pro )

	
	#2. blast?
	try: 
		d_blast = open(pp_path+"query.blastPsiMat").read()
	except IOError: 
		f_e.write("%s: query.blastPsiMat not found, skipping...\n" % pro)
		f_e.flush()
		os.exit()
	parsed_blast = parse_blast_reorder(d_blast)
	blast_norm = True
	
	
	
	#Now, handle each sequence position
	for pos in range(len(seq)):
		#for instance in add_features:
		instance_feature_names = {}		#We would need that only once, but this way it's easier
		instance_features = {}

		#2. Blast features
		if parsed_blast:
			featnames_blast, window_blast = feature_blast(parsed_blast, pos, fea_win, norm_raw=blast_norm)
			instance_feature_names.update(featnames_blast)
			instance_features.update(window_blast)	
		
		
	#Finally, append the current instance to the great picture
		temp=[]
		for l in open(feature_file):
			l = l.rstrip()
			x = l.split('\t')[0]
			temp.append(instance_features[x])
		feature_space.append(temp)		

	return feature_space,pro,seq





	
