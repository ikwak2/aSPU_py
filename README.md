Python code for MTaSPUsSet
=========================

IL-YOUP KWAK <ikwak@umn.edu>

python code for MTaSPUsSet (Multiple-trait, gene-level adaptive association testing
  with GWAS summary statistics) test.


Here's a description of the files:

---

[`MTaSPUsSet.py`] - MTaSPUsSet test using python. Need five arguments, Z-score matrix (Zs.txt), correlation matrix among phenotypes (corPhe.txt), correlation matrix among SNPs (corSNP.txt), the number of permutations ( 1000 ) and the file name where result outputs to be saved (out.txt).

[`util.py`] - some useful python functions used in MTaSPUsSet.py.

[`Zs.txt`] - example Z score matrix used for MTaSPUsSet.py. (14 rows (#SNPs) and 6 columns (#Phenotypes) )

[`corPhe.txt`] - example correlation matrix among phenotypes (6 phenotypes, 6 by 6 matrix).

[`corSNP.txt`] - example correlation matrix among SNPs (14 SNPs, 14 by 14 matrix). 

---


How to execute :
```py
./MTaSPUsSet.py Zs.txt corPhe.txt corSNP.txt 1000 out.txt 
```

Results (MTSPUsSet and MTaSPUsSet p-values) are saved in `out.txt`