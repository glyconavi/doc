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
  
  
  * https://sparqlist.glyconavi.org/TCarp_entry_citation
  * https://sparqlist.glyconavi.org/TCarp_entry_summary
  * https://sparqlist.glyconavi.org/TCarp_exptl_count
  * https://sparqlist.glyconavi.org/TCarp_glycosylated_site
  * https://sparqlist.glyconavi.org/TCarp_GTC
  * https://sparqlist.glyconavi.org/TCarp_id_gtc_Interaction
  * https://sparqlist.glyconavi.org/TCarp_id_model_gtc_mol
  * https://sparqlist.glyconavi.org/TCarp_Interaction
  * https://sparqlist.glyconavi.org/TCarp_Interaction_residue
  * https://sparqlist.glyconavi.org/TCarp_Interaction_residue_pdbid
  * https://sparqlist.glyconavi.org/TCarp_molfiles
  * https://sparqlist.glyconavi.org/TCarp_PDB_glycan_interaction_sheet_helix
  * https://sparqlist.glyconavi.org/TCarp_PDB_Glycosylation_type_Count
  * https://sparqlist.glyconavi.org/TCarp_PDB_helix_info_count
  * https://sparqlist.glyconavi.org/TCarp_PDB_sheet_info_count
  * https://sparqlist.glyconavi.org/TCarp_PDB_WURCS_GTC
  * https://sparqlist.glyconavi.org/TCarp_PDB_WURCS_PDBID
  * https://sparqlist.glyconavi.org/TCarp_PDBID_Search_WURCS
  * https://sparqlist.glyconavi.org/TCarp_PDBiD_WURCS_GTC
  * https://sparqlist.glyconavi.org/TCarp_protein_list
  * https://sparqlist.glyconavi.org/TCarp_proteindb_entry
  * https://sparqlist.glyconavi.org/TCarp_Residues_near_glycans
  * https://sparqlist.glyconavi.org/TCarp_Sequon_count
  * https://sparqlist.glyconavi.org/TCarp_stdWURCS
  * https://sparqlist.glyconavi.org/TCarp_text_Search
  * https://sparqlist.glyconavi.org/TCarp_Uniprot_Glycoprotein_list
  * https://sparqlist.glyconavi.org/TCarp_Uniprot_Lectin_list
  * https://sparqlist.glyconavi.org/TCarp_Validation_atom
  * https://sparqlist.glyconavi.org/TCarp_Validation_bond
  * https://sparqlist.glyconavi.org/TCarp_Validation_sugar



### SPARQL Endpoint

* This is a web interface designed to access RDF-encoded GlycoNAVI-TCarp data.


  * SPARQL Endpoint URL: https://sparql.glyconavi.org/sparql

  * Graph: `http://glyconavi.org/tcarp`

  * Example of SPARQL Query

1. Glycosylation site information

  * [RUN](https://sparql.glyconavi.org/sparql/?default-graph-uri=&query=DEFINE+sql%3Aselect-option+%22order%22%0D%0Aprefix+xsd%3A+++++%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E%0D%0Aprefix+rdfs%3A++++%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0Aprefix+glycan%3A++%3Chttp%3A%2F%2Fpurl.jp%2Fbio%2F12%2Fglyco%2Fglycan%23%3E%0D%0Aprefix+pdbo%3A++++%3Chttps%3A%2F%2Frdf.wwpdb.org%2Fschema%2Fpdbx-v50.owl%23%3E%0D%0Aprefix+dcterms%3A++%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E%0D%0Aprefix+glyconavi%3A++%3Chttp%3A%2F%2Fglyconavi.org%2Fontology%2Fpdb%23%3E%0D%0ASELECT+DISTINCT+%3Fid+%3Fmodel_num+%3Fprotein_db+%3Fdb_name%0D%0A+%3Fstrand_id+as+%3Fmod_chain+%3Fmod_comp_id+as+%3Fmod_aa+%3Fsequon+%3Fneighboring_sequence%0D%0A+%3Fglycan_type_label+as+%3Fgtype+%3Fmod_pos+%3Fgtc+%3Fwurcs+%23%3Fctfile%0D%0AFROM+%3Chttp%3A%2F%2Fglyconavi.org%2Ftcarp%3E%0D%0AWHERE+%7B%0D%0A++%3FTcarpEntry+a+glyconavi%3ATCarpEntry+%3B%0D%0A++++++++++++++dcterms%3Aidentifier+%3Fid+.%0D%0A++FILTER+%28+%3Fid+%3D+%221CKL%22+%29+%0D%0A++%23+Strand%0D%0A++%3FTcarpEntry+glyconavi%3Ahas_strand+%3Fstrand+.%0D%0A++%3Fstrand+dcterms%3Aidentifier+%3Fprotein_db+%3B%0D%0A++++++++++a+%3Fstrand_type+%3B%0D%0A++++++++++glyconavi%3Ahas_strand_id+%3Fstrand_id+%3B%0D%0A++++++++++glyconavi%3Ahas_db_name+%3Fdb_name+%3B%0D%0A++++++++++glyconavi%3Ahas_entity_id+%3Fentity_id+%3B%0D%0A++++++++++glyconavi%3Ahas_sequence+%3Faa_seq+.%0D%0A++%23+PDBModel%0D%0A++%3FTcarpEntry+glyconavi%3Ahas_PDB_model_glycan+%3Fmodel_glycan+.%0D%0A++%3Fmodel_glycan++glyconavi%3Ahas_model+%3Fmodel+.%0D%0A++%3Fmodel+a+glyconavi%3APDBModel+%3B%0D%0A++++++++%23glyconavi%3Ahas_ctfile+%3Fctfile+%3B%0D%0A++++++++glyconavi%3Ahas_pdbx_PDB_model_num+%3Fmodel_num+.%0D%0A++%23+Interaction+%28optional%29%0D%0A+%23+OPTIONAL+%7B+%3Fmodel+glyconavi%3Ahas_interaction+%3Finteraction+.+%7D%0D%0A++%23+Glycan+and+Glycosequence%0D%0A++%3Fmodel+glycan%3Ahas_glycan+%3Fglycan+.%0D%0A++%3Fglycan+%3Fa+glyconavi%3AWURCSStandard+%3B%0D%0A+++++++++++glycan%3Ahas_glycosequence+%3Fglycosequence+.%0D%0A++%3Fglycosequence+a+glycan%3AGlycosequence+%3B%0D%0A+++++++++++++++++glycan%3Ahas_sequence+%3Fwurcs+%3B%0D%0A+++++++++++++++++glycan%3Ain_carbohydrate_format+glycan%3Acarbohydrate_format_wurcs+.%0D%0A++OPTIONAL+%7B+%3Fglycan+glyconavi%3Ahas_glytoucan_id+%3Fgtc+.+%7D%0D%0A++%23+GlycosylationSite%0D%0A++%3Fmodel_glycan+glyconavi%3Ahas_glycosylation_site+%3Fptm_site+.%0D%0A++%3Fptm_site+a+glyconavi%3AGlycosylationSite+%3B%0D%0A++++++++++++glyconavi%3Ais_on_strand+%3Fstrand+%3B%0D%0A++++++++++++glyconavi%3Ahas_one_letter_code+%3Fone_letter_code+%3B%0D%0A++++++++++++glyconavi%3Ahas_sequence_before+%3Fsequence_before+%3B%0D%0A++++++++++++glyconavi%3Ahas_sequence_after+%3Fsequence_after+%3B%0D%0A++++++++++++glyconavi%3Ahas_asym_id+%3Fmod_asym_id+%3B%0D%0A++++++++++++glyconavi%3Ahas_entity_id+%3Fmod_entity_id+%3B%0D%0A++++++++++++glyconavi%3Ahas_seq_id+%3Fmod_pos+%3B%0D%0A++++++++++++glyconavi%3Ahas_asym_id+%3Fmod_asym_id+%3B%0D%0A++++++++++++glyconavi%3Ahas_comp_id+%3Fmod_comp_id+%3B%0D%0A++++++++++++glyconavi%3Ahas_atom_id+%3Fmod_atom_id+%3B%0D%0A++++++++++++glyconavi%3Ahas_glycan_type+%3Fglycan_type+.%0D%0A++%23+URI+for+pdbx_struct_mod_residue+%28optional%29%0D%0A++OPTIONAL+%7B+%3Fptm_site+glyconavi%3Ais_mod_residue+%3Fmod_residue+.+%7D%0D%0A+++FILTER+%28STRLEN%28%3Fsequence_after%29+%3D+3%29%0D%0A++BIND+%28CONCAT%28%3Fone_letter_code%2C+substr%28%3Fsequence_after%2C+1%2C+2%29%29+as+%3Fsequon%29%0D%0A++BIND+%28CONCAT%28%3Fsequence_before%2C%3Fsequon%29+as+%3Fneighboring_sequence%29++%0D%0A++OPTIONAL+%7B+%3Fptm_site+glyconavi%3Ahas_helix_info+%3Fhelix_info+.+%7D%0D%0A++OPTIONAL+%7B+%3Fptm_site+glyconavi%3Ahas_sheet_info+%3Fsheet_info+.+%7D%0D%0A++%3Fglycan_type+a+glyconavi%3AGlycanType%3B%0D%0A+++++++++++++++rdfs%3Alabel+%3Fglycan_type_label+.%0D%0A%7D%0D%0AORDER+BY+%3Fprotein_db+%3Fdb_name+%3Fmod_chain+%3Fmod_pos&format=text%2Fhtml&timeout=0&debug=on)

```
DEFINE sql:select-option "order"
prefix xsd:     <http://www.w3.org/2001/XMLSchema#>
prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
prefix glycan:  <http://purl.jp/bio/12/glyco/glycan#>
prefix pdbo:    <https://rdf.wwpdb.org/schema/pdbx-v50.owl#>
prefix dcterms:  <http://purl.org/dc/terms/>
prefix glyconavi:  <http://glyconavi.org/ontology/pdb#>
SELECT DISTINCT ?id ?model_num ?protein_db ?db_name
 ?strand_id as ?mod_chain ?mod_comp_id as ?mod_aa ?sequon ?neighboring_sequence
 ?glycan_type_label as ?gtype ?mod_pos ?gtc ?wurcs #?ctfile
FROM <http://glyconavi.org/tcarp>
WHERE {
  ?TcarpEntry a glyconavi:TCarpEntry ;
              dcterms:identifier ?id .
  FILTER ( ?id = "1CKL" ) 
  # Strand
  ?TcarpEntry glyconavi:has_strand ?strand .
  ?strand dcterms:identifier ?protein_db ;
          a ?strand_type ;
          glyconavi:has_strand_id ?strand_id ;
          glyconavi:has_db_name ?db_name ;
          glyconavi:has_entity_id ?entity_id ;
          glyconavi:has_sequence ?aa_seq .
  # PDBModel
  ?TcarpEntry glyconavi:has_PDB_model_glycan ?model_glycan .
  ?model_glycan  glyconavi:has_model ?model .
  ?model a glyconavi:PDBModel ;
        #glyconavi:has_ctfile ?ctfile ;
        glyconavi:has_pdbx_PDB_model_num ?model_num .
  # Interaction (optional)
 # OPTIONAL { ?model glyconavi:has_interaction ?interaction . }
  # Glycan and Glycosequence
  ?model glycan:has_glycan ?glycan .
  ?glycan ?a glyconavi:WURCSStandard ;
           glycan:has_glycosequence ?glycosequence .
  ?glycosequence a glycan:Glycosequence ;
                 glycan:has_sequence ?wurcs ;
                 glycan:in_carbohydrate_format glycan:carbohydrate_format_wurcs .
  OPTIONAL { ?glycan glyconavi:has_glytoucan_id ?gtc . }
  # GlycosylationSite
  ?model_glycan glyconavi:has_glycosylation_site ?ptm_site .
  ?ptm_site a glyconavi:GlycosylationSite ;
            glyconavi:is_on_strand ?strand ;
            glyconavi:has_one_letter_code ?one_letter_code ;
            glyconavi:has_sequence_before ?sequence_before ;
            glyconavi:has_sequence_after ?sequence_after ;
            glyconavi:has_asym_id ?mod_asym_id ;
            glyconavi:has_entity_id ?mod_entity_id ;
            glyconavi:has_seq_id ?mod_pos ;
            glyconavi:has_asym_id ?mod_asym_id ;
            glyconavi:has_comp_id ?mod_comp_id ;
            glyconavi:has_atom_id ?mod_atom_id ;
            glyconavi:has_glycan_type ?glycan_type .
  # URI for pdbx_struct_mod_residue (optional)
  OPTIONAL { ?ptm_site glyconavi:is_mod_residue ?mod_residue . }
   FILTER (STRLEN(?sequence_after) = 3)
  BIND (CONCAT(?one_letter_code, substr(?sequence_after, 1, 2)) as ?sequon)
  BIND (CONCAT(?sequence_before,?sequon) as ?neighboring_sequence)  
  OPTIONAL { ?ptm_site glyconavi:has_helix_info ?helix_info . }
  OPTIONAL { ?ptm_site glyconavi:has_sheet_info ?sheet_info . }
  ?glycan_type a glyconavi:GlycanType;
               rdfs:label ?glycan_type_label .
}
ORDER BY ?protein_db ?db_name ?mod_chain ?mod_pos
```

### RDF Data

  * RDF Schema
  
    * e.g. [RDF structure of TCarp:1A39](https://raw.githubusercontent.com/glyconavi/doc/master/tcarp/TCarp-1A39.svg)
  
  * [RDF Data](https://gitlab.com/glyconavi/resources/-/tree/master/TCarp)

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


