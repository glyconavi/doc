![GlycoNAVI Logo](https://glyconavi.org/img/GlycoNAVI.png)
<img src="https://glyconavi.org/img/TCarp.png" width="150px">


# GlycoNAVI TCarp Documantation

* [GlycoNAVI documantation](https://glyconavi.github.io/doc/)

## About GlycoNAVI TCarp

* [GlycoNAVI TCarp](https://glyconavi.org/TCarp/) is a database that provides information on glycan structures, and can access to data of  glycans and proteins using Semantic Web technology, that is a secondary database of PDB to provide extracted and annotated glycan structures and their surrounding environment. Users can access to the data not only from a browser but also through our SPARQL endpoint and APIs.


## How to use

### Search

*  Text Search

    * TCarp Text Search is a text search for proteins using strings such as Title, Descriptor, PDB ID, Uniprot ID, and common name.

    1. Typing your search query into the text box and pushing the search button.
    
    2. The results of the text search will be displayed in a table.

    3. You can refine your search by using the search box on the upper right.

    4. Browse the table and click on the TCarp ID link to go to the details page of TCarp.

<img width="500" alt="text_serch" src="https://user-images.githubusercontent.com/2530360/86117713-7a0d9900-bb0a-11ea-81c7-913f5b2cab4c.png">


![image](https://user-images.githubusercontent.com/2530360/86117908-d7a1e580-bb0a-11ea-8358-6f1778c70bed.png)



* Glycan Structure

  * Drawing and searching glycan structures using SugarDrawer.
  
  1. Go to the search site of [SugarDrawer](https://glyconavi.org/Draw/index.php).
  
  2. Drawing the glycan structures to be searched for using SugarDrawer.
  
  3. pushing the search button.
  
  4. The searched glycan structure and the accession number of GlyTouCan are displayed below the search button.
  
  5. A list of entries containing glycan structures will be displayed.
  
  6. Browse the table and click on the TCarp ID link to go to the details page of TCarp.

  
![image](https://user-images.githubusercontent.com/2530360/86119782-11282000-bb0e-11ea-83af-b61b37abe5f5.png)


![image](https://user-images.githubusercontent.com/2530360/86120288-fe621b00-bb0e-11ea-8017-ea450f33d202.png)


![image](https://user-images.githubusercontent.com/2530360/86120510-657fcf80-bb0f-11ea-80d5-261e3ae89b51.png)

![image](https://user-images.githubusercontent.com/2530360/86120758-d921dc80-bb0f-11ea-9d64-84e82c0233f1.png)



  * [Common Name Search](https://glyconavi.org/CAN/can-tcarp.php) is a search that utilizes trivial names, synonyms, abbreviations and other carbohydrate names based on CAN resource of GlycoNAVI.
  
  1. Click the [Common Name Search](https://glyconavi.org/CAN/can-tcarp.php) image.
  
  2. Typing your search query into the text box.
  
  3. Clicking on CommonName or WURCS will display a list of entries containing that glycan structure. (If no entry is found, "No data available in table" is displayed.)

  4. Browse the table and click on the TCarp ID link to go to the details page of TCarp.
  
  ![image](https://user-images.githubusercontent.com/2530360/86121077-5e0cf600-bb10-11ea-823a-5878636700a3.png)


  ![image](https://user-images.githubusercontent.com/2530360/86121278-ba701580-bb10-11ea-87e6-860902c4e6b1.png)


  ![image](https://user-images.githubusercontent.com/2530360/86121761-8f39f600-bb11-11ea-9693-3db849616325.png)


  * [Motif Search](https://glyconavi.org/Glycans/motif-tcarp-table.php) is a search that utilizes glycan motif structures.

  1. Click the [Motif Search](https://glyconavi.org/Glycans/motif-tcarp-table.php) image.
  
  2. Enter your search query in the text box or browse the table to find the motif structure.
  
  3. Clicking on Motif or WURCS will display a list of entries containing that glycan structure. (If no entry is found, "No data available in table" is displayed.)

  4. Browse the table and click on the TCarp ID link to go to the details page of TCarp.


![image](https://user-images.githubusercontent.com/2530360/86121936-df18bd00-bb11-11ea-966c-d3f96ff7c016.png)


![image](https://user-images.githubusercontent.com/2530360/86122163-4b93bc00-bb12-11ea-94d0-d3c6ac6a49e7.png)



* Structural Categoly

　1. Click on an image of the categories and search using the displayed table.
 
 ![image](https://user-images.githubusercontent.com/2530360/86122683-33706c80-bb13-11ea-8dfb-73eebcacaa3f.png)


  * Table of [carbohydrates structures in the Protein Data Bank](https://glyconavi.org/Glycans/pdb-saccharide_table.php)
  
  ![image](https://user-images.githubusercontent.com/2530360/86122397-bcd36f00-bb12-11ea-9445-ae3fee43a304.png)

  * Table of [proteins containing carbohydrate in the Protein Data Bank](https://glyconavi.org/Proteins/db_table.php)
  
  ![image](https://user-images.githubusercontent.com/2530360/86122507-ebe9e080-bb12-11ea-8679-37a0f2aa64f0.png)

  * Table of [glycoproteins containing carbohydrate in the Protein Data Bank](https://glyconavi.org/Glycoproteins/db_table.php)
  
  ![image](https://user-images.githubusercontent.com/2530360/86122569-02903780-bb13-11ea-8ef2-4d2ec19e8913.png)

  * Table of [lectins containing carbohydrate in the Protein Data Bank](https://glyconavi.org/Lectins/db_table.php)
  
  ![image](https://user-images.githubusercontent.com/2530360/86122614-16d43480-bb13-11ea-98f7-771e58012ef4.png)


### Entry Page

* The TCarp entry page contains information on the three-dimensional structure of the glycans and proteins, structural information near the glycans, information on the glycosylation sites of the glycoproteins, citation information, and a structure validation report.


  * Protein Information: e.g. [TCarp:1CKL](https://glyconavi.org/Proteins/entry.php?id=1CKL)

![image](https://user-images.githubusercontent.com/2530360/86125588-e216ac00-bb17-11ea-92e1-9ff638e8c09e.png)

  * Saccharide Information: e.g. [TCarp:1CKL](https://glyconavi.org/Proteins/entry.php?id=1CKL)

![image](https://user-images.githubusercontent.com/2530360/86125630-f5297c00-bb17-11ea-81f8-a1d1cc9ea574.png)

  * Residues near the glycans: e.g. [TCarp:1CKL](https://glyconavi.org/Proteins/entry.php?id=1CKL)

![image](https://user-images.githubusercontent.com/2530360/86125704-10948700-bb18-11ea-84ec-a0613baa42e2.png)

  * Glycosylation Information: e.g. [TCarp:1CKL](https://glyconavi.org/Proteins/entry.php?id=1CKL) 
  
![image](https://user-images.githubusercontent.com/2530360/86125755-230ec080-bb18-11ea-9c0d-dd500a7cb0e6.png)

  * Citation: e.g. [TCarp:1CKL](https://glyconavi.org/Proteins/entry.php?id=1CKL)

![image](https://user-images.githubusercontent.com/2530360/86125792-31f57300-bb18-11ea-94dd-e75b050cdd46.png)

  * Validation Report: e.g. [TCarp:4PEZ](https://glyconavi.org/Proteins/entry.php?id=4PEZ)

![image](https://user-images.githubusercontent.com/2530360/86126107-b6e08c80-bb18-11ea-9a21-458818accfe1.png)



## Programmatic Access

* GlycoNAVI provides several ways for programmatic access to its data, including:

### Web Service Interface

* GlycoNAVI-SPARQList

  * [SPARQList](https://github.com/dbcls/sparqlist) is a REST API server which executes a SPARQL query,



### SPARQL Endpoint

* This is a web interface designed to access RDF-encoded GlycoNAVI-TCarp data.


  * SPARQL Endpoint URL: https://sparql.glyconavi.org/sparql

  * Graph: `http://glyconavi.org/tcarp`

  * SPARQL Queries

1. Glycosylation site information

```
PREFIX 
```


## Statistics

* Statistics related to glycans in the Protein Data Bank

* Statistics on glycan-containing proteins in the Protein Data Bank

* Statistics of protein structures around carbohydrates in the Protein Data Bank

  * Helix structures of proteins around glycan structures
  
  * Sheet structures of proteins around glycan structures

* Statistics of the sequon

* Statistics of amino acid residues

  * Statistics of residues around glycans in the Protein Data Bank

* Statistics of the paired structure of glycans and amino acid residues

  * Statistics of the paired structure of glycans and amino acid residues around carbohydrates in the Protein Data Bank

* Statistics of the experimental methods



## Feedback

* We are always open to questions, comments and suggestions about the Feedback site and the information we provide in general.
  
  * [Feedback](https://glyconavi.org/Feedback/)


