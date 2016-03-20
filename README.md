Python codes for aSPU
=========================

IL-YOUP KWAK <kwaki@umn.edu>

python codes for MTaSPUsSet (Multiple-trait, gene-level adaptive association testing
  with GWAS summary statistics) test.


Here's a description of the files:

---

[`MTaSPUsSet.py`] - MTaSPUsSet test using python. Need four arguments, Z-score matrix (Zs.txt), correlation matrix among phenotypes (corPhe.txt), correlation matrix among SNPs (corSNP.txt) and the number of permutations ( 1000 )

[`util.py`] - some useful python functions used in MTaSPUsSet.py.

[`Zs.txt`] - example Z score matrix used for MTaSPUsSet.py. (14 rows (#SNPs) and 6 columns (#Phenotypes) )

[`corPhe.txt`] - example correlation matrix among phenotypes (6 phenotypes, 6 by 6 matrix).

[`corSNP.txt`] - example correlation matrix among SNPs (14 SNPs, 14 by 14 matrix). 

---


How to execute :
```py
./MTaSPUsSet.py Zs.txt corPhe.txt corSNP.txt 1000
```

