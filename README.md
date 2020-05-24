<h2>HandyEnrich Installation and User Manual</h2>


### Overview of HandyEnrich

**HandyEnrich** is a software package for enrichment analysis which enables multiple enrichment tests with a simple command

### Supported Environment

1. HandyEnrich can be executed on Linux OS / Mac

### Software Dependency

<h4>Required</h4>

1. Python3 (version: 3.7.0 or later) with statsmodels/scipy module *required*

### Software installation

Each installation step will take less than ~1 min


#### Installation of HandyEnrich


1. Download HandyEnrich by

   ```shell
    git clone https://github.com/UTNK/handyenrich.git
   ```

2. Add the absolute path of `handyenrich/src` directory to `$PATH`

3. Make `handyenrich/src/*` executable

   ```shell
   chmod u+x handyenrich/src/*
   ```

### Sample Codes

The HandyEnrich package contains an example input file in the `examples` directory so users can check the software functions as follows:

**Example 1**

Test enrichment of metagenome samples in environment ontology terms

```shell
entest -r metagenome/meo_mg.txt -q metagenome/query.txt -a metagenome/mg.txt
```


Input:

[`meo_mg.txt`](https://github.com/UTNK/handyenrich/tree/master/example/metagenome/meo_mg.txt)

[`query.txt`](https://github.com/UTNK/handyenrich/tree/master/example/metagenome/query.txt)

[`mg.txt`](https://github.com/UTNK/handyenrich/tree/master/example/metagenome/mg.txt)

Output:

 Standard output: stats, p values, q values for each environment ontology term ("meo")

### entest usage

```
usage: entest [-h] [-v] [-r REF] [-q QUERY] [-a ALL] [-d DELIM1]
              [--delim2 DELIM2] [--alt ALT] [--cor COR]

entest

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Print version
  -r REF, --ref REF     File path of Class-Term list
  -q QUERY, --query QUERY
                        File path of query term list
  -a ALL, --all ALL     File path of all term list
  -d DELIM1, --delim1 DELIM1
                        delimitter between class and term
  --delim2 DELIM2       delimitter among terms
  --alt ALT             Alternative hypothesis type ("greater" :default,
                        "less", "two-sided")
  --cor COR             Multiple test correction default: fdr_bh (see https://
                        www.statsmodels.org/dev/generated/statsmodels.stats.mu
                        ltitest.multipletests.html)
```


### Contact


Naoki Konno (The University of Tokyo) [naoki@bs.s.u-tokyo.ac.jp](mailto:naoki@bs.s.u-tokyo.ac.jp)
