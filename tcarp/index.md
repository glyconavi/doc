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



  * Common Name Search is a search that utilizes trivial names, synonyms, abbreviations and other carbohydrate names based on CAN resource of GlycoNAVI.

  * Motif Search is a search that utilizes glycan motif structures.



* Structural Categoly

  * Table of carbohydrates structures in the Protein Data Bank

  * Table of proteins containing carbohydrate in the Protein Data Bank

  * Table of glycoproteins containing carbohydrate in the Protein Data Bank

  * Table of lectins containing carbohydrate in the Protein Data Bank


### Entry Page

* 

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


