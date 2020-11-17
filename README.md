# ProNAhot
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

numpy == 1.14.*

scipy == 0.14.0

scikit-learn == 0.19.1

PyWavelets >= 0.5.2

## External programs
ProNAhot need PredictProtein output files with the suffixes .in .fasta .blastPsiMat .profbval .mdisorder .consurf.grades and .profRdb.
And all these files can be created by running PredictProtein from predictprotein.org


## How to run
Example：

If you known the binding residues on your input protein, please label them as the same format as that in file ./test/binding_label.example, and run:

./pronahot -p ./test/ -l ./test/binding_label.example

If you do not known any binding information, please run ProNA2020 from predictprotein.org and submit the ProNA2020 ouput as:

./pronahot -p ./test/ -l ./test/query.prona

Usage: pronahot [options]

ProNAhot: Predicting protein-DNA, protein-RNA and protein-protein binding hot-
spots from sequence

Options:

  -h, --help   show this help message and exit
  
  -p PATH      Directory containing the PredictProtein output files with the
               suffixes .in .fasta .blastPsiMat .profbval .mdisorder
               .consurf.grades and .profRdb.
               
  -l LABEL     Please label the binding residues for your input protein and
               the format can be found in file ./test/binding_label.example.
               ProNAHot can only distinguish between binding hotspots and
               binding non-hotspots.If you do not known the binding
               information of your input protein, you can run ProNA2020 from
               predictprotein.org and submit the output here with the suffixe
               .prona.
               
  -o FILENAME  Output file. If not specified, the output is written to STDOUT
