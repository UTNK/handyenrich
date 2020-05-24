<h2>HandyEnrich Installation and User Manual</h2>


### Overview of HandyEnrich

**HandyEnrich** is a software for enrichment analysis which enables multiple enrichment tests with a simple command

### Supported Environment

1. HandyEnrich can be executed on Linux OS / Mac

### Software Dependency

<h4>Required</h4>

1. Python3 (version: 3.7.0 or later) with statsmodels/scipy module *required*

### Software installation

Each installation step will take less than ~1 min


#### Installation of HandyEnrich


1. Download FRACTAL by

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

	[`meo_mg.txt`](https://github.com/yachielab/FRACTAL/blob/master/example/)(FASTA format)

Output:

	 [`FRACTALout.nwk`](https://github.com/yachielab/FRACTAL/blob/master/example/output/FRACTALout.nwk) (Newick format) will be created in your current working directory

**Example 2**

Lineage estimation by NJ using RapidNJ with distributed computing where the maximum number of computing nodes is set to 100. The output file name is set to `FRACTAL_NJ`. The computation will take several minutes.

```shell
FRACTAL.sh -i test.fa -f FRACTAL_NJ -m rapidnjNJ -d 100
```

Input:

	 [`test.fa`](https://github.com/yachielab/FRACTAL/blob/master/example/test.fa) (FASTA format)

Output:

	 [`FRACTAL_NJ.nwk`](https://github.com/yachielab/FRACTAL/blob/master/example/output/FRACTAL_NJ.nwk) (Newick format) for intermediate files will be created in your working directory.

**Example 3**

Lineage estimation by ML using FastTreeMP with its option `-fastest -quiet` without distributed computing. The number of threads required for the phylogenetic placement and the sample tree reconstruction procedures is set to be 16. The output file name is set to `FRACTAL_ML`.  The computation will take ~5 min.

```shell
FRACTAL.sh -i test.fa -f FRACTAL_ML -m fasttreeML -p "-fastest -quiet" -c 16
```

Input:    

	 [`test.fa`](https://github.com/yachielab/FRACTAL/blob/master/example/test.fa) (FASTA format)

Output:  

	 [`FRACTAL_ML.nwk`](https://github.com/yachielab/FRACTAL/blob/master/example/output/FRACTAL_ML.nwk) (Newick format) 

**Example 4**

Lineage estimation with a software tool of choice and user defined parameters.

1. Prepare a shell script that takes a FASTA file as an input file, calculate a lineage of the input sequences, and output it to a Newick format file whose name is inherited from the input FASTA file, like from `foo.fa` to `foo.fa.tree`.

2. Add the absolute path of the shell script to `$PATH`

3. Make the shell script executable

4. Execute FRACTAL as follows. The example shell script file [`ml_raxml.sh`](https://github.com/yachielab/FRACTAL/blob/hotfix/example/script/ml_raxml.sh) below is prepared and provided in the installation package for ML method with GTR-Gamma model by RAxML. The maximum number of computing nodes is set to 100 in the following command. The computation will take 20~30 min.

   ```shell
   FRACTAL.sh -i test.fa -f FRACTAL_raxml -s ml_raxml.sh -d 100
   ```

### FRACTAL Usage

```
Usage:
    FRACTAL.sh
    [-v] [-h] [-i input_file] [-o output_file_path] [-f output_file_name]
    [-m method] [-p "options"] [-k sequence_number] [-b model_name]
    [-x iteration_number] [-t sequence_number]
    [-d job_number] [-c thread_number] [-e]
    [-r integer] [-O qsub_option] [-I first_qsub_option] [-j job_name]

Options:
    -v
      Print FRACTAL version; ignore all the other parameters
    -h
      Print the usage of FRACTAL; ignore all the other parameters
    -i <String>
      Input FASTA file
    -o <String>
      Output directory path. Default: current working directory
    -f <String>
      Output file name. Default: FRACTALout
    -m <String, Permissible values: ‘raxmlMP’, ‘rapidnjNJ’ and ‘fasttreeML’>
      Method to reconstruct lineage tree in each iteration cycle. Default: raxmlMP
        When you specify -s option, this option will be ignored.
    -p "<String>"
      Options for the software corresponding to the method selected by -m
    -s <String>
      File name of a shell script used to reconstruct lineage tree in each iteration cycle.
        See sample codes (example 4).
    -k <Integer>
      Number of sequences for the subsampling procedure. Default: 100
    -b <String>
      Substitution model of RAxML for phylogenetic placement. Default: GTRCAT
    -x <Integer>
      Threshold for the maximum number of retrial iterations in the subsampling process
    -t <Integer>
      Threshold number of input sequences to switch to direct lineage tree reconstruction 
        in each iteration cycle. Default: 500
    -d <Integer>
      Maximum number of jobs permissible for distributed computing.
        Default: 1 (no distributed computing)
    -c <Integer>
      Number of threads for the subsample tree reconstruction and the phylogenetic placement
        in each iteration cycle. Default: 1
    -e
      Output intermediate files
    -r <Integer>
      Seed number for generation of random values. Default: 0
    -O "<String>"
      Options for qsub. Default: ""
      example:  -O "-pe def_slot 4 -l s_vmem=16G -l mem_req=16G" 
    -I "<String>"
      Options especially for the first qsub. Default: the string specified by -O
    -j "<String>"
      Name of the jobs distributed by FRACTAL. Default: "FRACTAL"
```


### Contact


Naoki Konno (The University of Tokyo) [naoki@bs.s.u-tokyo.ac.jp](mailto:naoki@bs.s.u-tokyo.ac.jp)

Nozomu Yachie (The University of Tokyo) [nzmyachie@gmail.com](mailto:yachie@synbiol.rcast.u-tokyo.ac.jp)