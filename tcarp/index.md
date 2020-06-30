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

    * Typing your search query into the text box and pushing the search button.

    * You can refine your search by using the search box on the upper right.

    * Browse the table and click on the TCarp ID link to go to the details page of TCarp.

<img width="500" alt="text_serch" src="https://user-images.githubusercontent.com/2530360/86117713-7a0d9900-bb0a-11ea-81c7-913f5b2cab4c.png">




![image](https://user-images.githubusercontent.com/2530360/86117908-d7a1e580-bb0a-11ea-8358-6f1778c70bed.png)


  


* Glycan Structure

  * Drawing and searching glycan structures using SugarDrawer.

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


