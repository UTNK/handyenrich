<h2>HandyEnrich example reference files</h2>

### Description files

####KEGG various lists

- Download date: June 1st, 2020

  ```shell
  $ curl http://rest.kegg.jp/list/pathway > pathway.kegg.txt
  $ curl http://rest.kegg.jp/list/module > module.kegg.txt
  $ curl http://rest.kegg.jp/list/reaction > reaction.kegg.txt
  $ curl http://rest.kegg.jp/list/rclass > rclass.kegg.txt
  $ curl http://rest.kegg.jp/list/compound > compound.kegg.txt
  $ curl http://rest.kegg.jp/list/ko > ko.kegg.txt
  ```

  - **pathway.kegg.txt**
  - **module.kegg.txt**
  - **reaction.kegg.txt**
  - **rclass.kegg.txt**
  - **compound.kegg.txt**
  - **ko.kegg.txt**
  
- Downloaded date: July 12th, 2020

  ```shell
  $ curl http://rest.kegg.jp/list/glycan > glycan.kegg.txt
  ```

  - **glycan.kegg.txt**

###Link files

####KEGG Module - KEGG Orthology

- Download date: June 1st, 2020

  ```shell
  $ curl http://rest.kegg.jp/link/md/ko | awk '{ print $2"\t"$1 }' > md_ko.txt
  ```

  - **md_ko.txt**

####EC Number - KEGG Orthology

- Download date: June 1st, 2020

  ```shell
  $ curl http://rest.kegg.jp/link/ko/ec | awk '{ print $2"\t"$1 }' | cut -d"." -f1,2,3 | awk '{ print $2"\t"$1 }' | sort | uniq > ec3_ko.txt
  $ curl http://rest.kegg.jp/link/ko/ec | awk '{ print $2"\t"$1 }' | cut -d"." -f1,2 | awk '{ print $2"\t"$1 }' | sort | uniq > ec2_ko.txt
  $ curl http://rest.kegg.jp/link/ko/ec | awk '{ print $2"\t"$1 }' | cut -d"." -f1 | awk '{ print $2"\t"$1 }' | sort | uniq > ec1_ko.txt
  $ cat ec* > ec_ko.txt
  ```

  - **ec1_ko.txt**
  - **ec2_ko.txt**
  - **ec3_ko.txt**
  - **ec_ko.txt**

#### Reaction Class - KEGG Orthology

- Download date: June 1st, 2020

  ```shell
  $ curl http://rest.kegg.jp/link/ko/rclass > rc_ko.txt
  ```

  - **rn_ko.txt**

####KEGG Pathway - KEGG Orthology

- Download date: June 1st, 2020

  ```shell
  $ curl http://rest.kegg.jp/link/ko/pathway | grep map > pathway_ko.txt
  ```

  - **pathway_ko.txt**

#### EC Number - KEGG Reaction

- Download date: June 27th, 2020

  ```shell
  $ curl http://rest.kegg.jp/link/reaction/ec | awk '{ print $2"\t"$1 }' | cut -d"." -f1 | awk '{ print $2"\t"$1 }' | sort | uniq > ec1_rn.txt
  $ curl http://rest.kegg.jp/link/reaction/ec | awk '{ print $2"\t"$1 }' | cut -d"." -f1,2 | awk '{ print $2"\t"$1 }' | sort | uniq > ec2_rn.tx
  $ curl http://rest.kegg.jp/link/reaction/ec | awk '{ print $2"\t"$1 }' | cut -d"." -f1,2,3 | awk '{ print $2"\t"$1 }' | sort | uniq > ec3_rn.txt
  $ cat ec*_rn.txt > ec_rn.txt
  ```


####KEGG Pathway - KEGG Module

- Download date: June 28th, 2020

  ```shell
  $ (base) enukenoMacBook-puro:class_elem nk$ curl http://rest.kegg.jp/link/pathway/module | awk '{ print $2 "\t" $1 }' > pathway_md.txt
  ```

#### KEGG Module - KEGG Reaction

- Download date: June 28th, 2020

  ```shell
  $ curl http://rest.kegg.jp/link/reaction/module > md_rn.txt
  ```

#### KEGG Pathway - KEGG Reaction

- Download date: June 28th, 2020

  ```shell
  $ curl http://rest.kegg.jp/link/reaction/pathway | grep map > pathway_rn.txt
  ```

  