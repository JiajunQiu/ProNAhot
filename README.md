# ProNAHot
ProNAhot: Predicting protein-DNA, protein-RNA and protein-protein binding hot-spots from sequence
ProNAhot can distinguish between the binding hotspots and binding non-hotspots based on only sequence information,
which means you need to label the binding residues on the input protein before running ProNAhot.
In case you don't have any binding information for your input protein, 
we suggest you run ProNA2020 from predictprotein.org to get predicted protein-, DNA- and RNA-binding residues for your input protein.
And you can submit the output of ProNA2020 directly to ProNAhot.

## How to install
git clone https://github.com/JiajunQiu/ProNAhot.git
cd ProNAhot
python3 setup.py install

or you can install the following dependency manually：

pybrain (>=0.3.3)

scikit-learn (=0.19.1-2)

botocore (>=1.10.33)

smart-open (>=1.5.7)

#### Software:

ncbi-blast+

fastprofkernel (>=1.0.24)

## How to run

Usage: prona2020 [options]

Options:

* -h:show this help message and exit
  
* -p:PATH,Directory containing the PredictProtein output files with the
               suffixes .chk .in .fasta .blastPsiMat .profbval .mdisorder and
               .profRdb.
               
* -o:FILENAME,Output file. If not specified, the output is written to STDOUT.
  
* -l:LABEL,Turn off protein level prediction by inputting binding label,
               e.g. "-l  Protein_DNA", which means the input protein is already known as a Protein- and DNA-binding protein.
               
* -d:DATABASE,Use your own local database for PSI-BLAST (homology based
               inference), default is using the profile (.chk) from big_80
               database(rostlab) which is a comprehensive blast database at
               80% sequence identity redundancy level
               
* -v:Print verbose or not (True/False), default is False

