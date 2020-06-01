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

  