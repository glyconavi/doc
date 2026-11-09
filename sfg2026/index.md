---
title: "Registered but unreachable — reproducibility record"
---

# Reproducibility record

## Registered but unreachable: what shared glycan identifiers do not resolve

Issaku Yamada, Naoki Kimura, Hinako Terauchi, Masaaki Matsubara
Laboratory of Glycoinformatics, The Noguchi Institute, Tokyo, Japan

Poster Board **BM-16** | Poster Session 1, Starvine Ballroom | Monday, November 9, 2026 | 4:00–5:30 p.m.
2026 Society for Glycobiology Annual Meeting | November 8–11, 2026 | Emory Conference Center Hotel, Atlanta, Georgia, USA
Topic 2: AI, Informatics, and Computational Glycoscience

---

This document records every structure, query and count presented on the
poster, in a form that allows them to be re-executed independently.

**Observation dates.** Case-study counts (sections 2–6) were obtained on
**12 August 2026** unless stated otherwise. The archetype family and the
registry totals were verified on **28 October 2026**. The session
statistics (section 7) were collected between **April 8 and July 16, 2026**. Database contents change; counts
obtained on another date may differ, which is a property of the resources
and not an error in this record.

---

## 1. Resources and interfaces

### 1.1 MCP servers

| Server | Endpoint | Role |
|---|---|---|
| GlycanBuilder-MCP | `https://gb.glyconavi.org/mcp` (web app: https://gb.glyconavi.org) | Structure construction and editing; WURCS to GlyTouCan resolution; PDB search; GlyGen annotation retrieval |
| TogoMCP | `https://togomcp.rdfportal.org/mcp` | SPARQL access to life-science RDF endpoints |
| GlycoNAVI MCP | GlycoNavi service | Glycan-database retrieval; subsumption-graph queries |
| PubMed MCP | — | Literature retrieval (session statistics, section 7) |

Tools were invoked through the Model Context Protocol (MCP), a standard
interface by which software agents call external services.

### 1.2 Underlying resources reached

| Resource | Access route |
|---|---|
| GlyTouCan | GlycanBuilder-MCP (`search_glycan`) |
| RCSB PDB | GlycanBuilder-MCP (`search_pdb_structures`, RCSB Search API) |
| GlyCosmos | TogoMCP (`run_sparql`, `https://ts.glycosmos.org/sparql`) |
| UniProt | TogoMCP (`run_sparql`, `https://sparql.uniprot.org/sparql`) |
| GlyGen | GlycanBuilder-MCP (`get_glycan_annotations`) |

### 1.3 Tools used

**GlycanBuilder-MCP**

| Tool | Use |
|---|---|
| `add_residue` | Attach Glc, Gal, NeuAc, Fuc |
| `set_linkage` | Change anomeric state or parent linkage position |
| `change_residue_type` | NeuAc to NeuGc; Glc to GlcNAc |
| `remove_residue` | Remove terminal NeuAc |
| `search_glycan` | WURCS to GlyTouCan accession |
| `search_pdb_structures` | WURCS matched against PDB branched-entity descriptors |
| `search_glycan_substructure` | Substructure search (unavailable at the time of observation) |
| `get_glycan_annotations` | GlyGen cross-references, motifs, literature |

**TogoMCP**

| Tool | Use |
|---|---|
| `get_MIE_file` | Schema description for GlyCosmos |
| `get_sparql_endpoints` | Endpoint discovery |
| `run_sparql` | Queries against GlyCosmos and UniProt |

### 1.4 Division of labour

| Step | Performed by |
|---|---|
| Interpreting a natural-language request | language model |
| Choosing which tool to call, and in what order | language model |
| Constructing the WURCS string | GlycanBuilder (deterministic) |
| Resolving the GlyTouCan accession | GlyTouCan |
| Returning entry counts | RCSB PDB Search API / SPARQL endpoints |

The language model did not generate WURCS strings or accession numbers.
Query structures were built and edited with GlycanBuilder-MCP; accessions
were resolved in GlyTouCan. Structure construction and identifier
resolution were deterministic: the same input returns the same output,
independently of the model.

**Systems used.** The case study (sections 2–6) was run with Claude
(Anthropic) through claude.ai, calling the MCP servers listed in section
1.1. The session statistics (section 7) come from glyconavi-llm-mcp, the
GlycoNAVI LLM–MCP service, run with locally served open-weight language
models; Claude was not used there.

**Figures.** Glycans on the poster are drawn according to the Symbol
Nomenclature for Glycans (SNFG). The figures were drawn for the poster
following the SNFG guidelines; they were not rendered directly by
GlycanBuilder-MCP.

---

## 2. Structure series

All structures derive from 3'-sialyllactose, Neu5Ac(a2-3)Gal(b1-4)Glc, by
changing exactly one structural element.

### 2.1 WURCS strings

```
3'-sialyllactose, alpha reducing end
WURCS=2.0/3,3,2/[a2122h-1a_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b3-c2

3'-sialyllactose, beta reducing end
WURCS=2.0/3,3,2/[a2122h-1b_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b3-c2

3'-sialyllactose, anomeric configuration unspecified
WURCS=2.0/3,3,2/[a2122h-1x_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b3-c2

3'-sialyllactose, anomeric configuration and sialic acid linkage unspecified
WURCS=2.0/3,3,2/[a2122h-1x_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b?-c2

3'-sialyllactose, beta reducing end, sialic acid linkage unspecified
WURCS=2.0/3,3,2/[a2122h-1b_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b?-c2

6'-sialyllactose, beta reducing end
WURCS=2.0/3,3,2/[a2122h-1b_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b6-c2

6'-sialyllactose, alpha reducing end
WURCS=2.0/3,3,2/[a2122h-1a_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b6-c2

6'-sialyllactose, anomeric configuration unspecified, pyranose
WURCS=2.0/3,3,2/[a2122h-1x_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b6-c2

6'-sialyllactose, anomeric configuration and ring form unspecified
WURCS=2.0/3,3,2/[a2122h-1x_1-?][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b6-c2

6'-sialyllactose, archetype
WURCS=2.0/3,3,2/[u2122h][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3/a4-b1_b6-c2

N-glycolyl form of 3'-sialyllactose, beta reducing end
WURCS=2.0/3,3,2/[a2122h-1b_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCCO/3=O]/1-2-3/a4-b1_b3-c2

3'-sialyl-3-fucosyllactose, beta reducing end
WURCS=2.0/4,4,3/[a2122h-1b_1-5][a1221m-1a_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3-4/a3-b1_a4-c1_c3-d2

Lactose, beta reducing end
WURCS=2.0/2,2,1/[a2122h-1b_1-5][a2112h-1b_1-5]/1-2/a4-b1

Lactose, alpha reducing end
WURCS=2.0/2,2,1/[a2122h-1a_1-5][a2112h-1b_1-5]/1-2/a4-b1

Sialyl Lewis x, beta reducing end
WURCS=2.0/4,4,3/[a2122h-1b_1-5_2*NCC/3=O][a1221m-1a_1-5][a2112h-1b_1-5][Aad21122h-2a_2-6_5*NCC/3=O]/1-2-3-4/a3-b1_a4-c1_c3-d2
```

### 2.2 Editing operations

| Product | Parent | Operation |
|---|---|---|
| 3'-SL alpha / unspecified | 3'-SL beta | `set_linkage` targetIndex=1, anomericState=a / ? |
| linkage-unspecified variants | above | `set_linkage` targetIndex=3, parentPosition=? |
| 6'-SL | 3'-SL beta | `set_linkage` targetIndex=3, parentPosition=6 |
| N-glycolyl form | 3'-SL beta | `change_residue_type` targetIndex=3, NeuAc to NeuGc |
| 3'-sialyl-3-fucosyllactose | 3'-SL beta | `add_residue` Fuc, targetIndex=1, parentPosition=3, anomericState=a |
| Lactose | 3'-SL beta | `remove_residue` targetIndex=3 |
| Sialyl Lewis x | 3'-sialyl-3-fucosyllactose | `change_residue_type` targetIndex=1, Glc to GlcNAc |

Sialyl Lewis x was obtained from 3'-sialyl-3-fucosyllactose by a single
residue-type substitution.

---

## 3. Results

### 3.1 Accessions and entry counts

| Structure | GlyTouCan | PDB entries | Glycoproteins (GlyCosmos) |
|---|---|---|---|
| 3'-SL, alpha reducing end | G92323ZH | 19 | 0 |
| 3'-SL, beta reducing end | G91237TK | 30 | 0 |
| 3'-SL, anomer unspecified | G56516VH | see 3.5 | 0 |
| 3'-SL, anomer and linkage unspecified | G38552LX | 0 | 0 |
| 3'-SL, beta, linkage unspecified | not retrieved | 0 | — |
| 6'-SL, beta reducing end | G28868ZC | 12 | 0 |
| 6'-SL, alpha reducing end | G63717BV | 0 | 0 |
| 6'-SL, anomer unspecified, pyranose | G69893KP | 12 | — |
| 6'-SL, anomer and ring unspecified | G09675VB | 0 | — |
| 6'-SL, archetype | G77019UJ | 12 | — |
| N-glycolyl form of 3'-SL, beta | not retrieved | 1 | — |
| 3'-sialyl-3-fucosyllactose, beta | G84173YM | 0 | 0 |
| Lactose, beta | not retrieved | 146 | — |
| Lactose, alpha | not retrieved | 67 | — |
| Sialyl Lewis x, beta | G00054MO | 10 | 0 |
| beta-GlcNAc (monosaccharide) | G49108TO | not measured | 8,767 |

### 3.2 PDB identifiers

**3'-sialyllactose, alpha reducing end (G92323ZH) — 19 entries**

1QFO, 1S0I, 1Z4X, 2XBO, 3HTT, 3SIT, 4C1W, 4LO5, 4WVW, 4Y20, 4YZ5, 5B2D,
5GLU, 5WHT, 5WHU, 6HKU, 6Y5Y, 7EE4, 9UG5

**3'-sialyllactose, beta reducing end (G91237TK) — 30 entries**

1DBN, 1HGG, 1SE3, 1SID, 1WGC, 1WW4, 2OSX, 2W68, 2WGC, 2ZG3, 3AP7, 3NV4,
3S6X, 3VKM, 4EN6, 4GU4, 4LBL, 4LBO, 4MBY, 4ONT, 4POR, 5IJ1, 5J14, 6TLZ,
6Y5Y, 7ZIL, 7ZIM, 7ZIP, 8BJZ, 8BSO

Overlap: 6Y5Y only. Union: 19 + 30 - 1 = **48 distinct entries**.

**6'-sialyllactose, beta reducing end (G28868ZC) — 12 entries**

2DS0, 3S6Y, 4C1X, 4EN8, 5BNN, 6ER4, 6R43, 6TM0, 7ZIN, 7ZIO, 7ZIQ, 8PBZ

**6'-sialyllactose, alpha reducing end (G63717BV) — 0 entries**

**Sialyl Lewis x (G00054MO) — 10 entries via RCSB WURCS matching**

2KMB, 2R61, 2Z8L, 4RFB, 4UO2, 4UO6, 4USO, 5KIQ, 6Q05, 8X2F

Via GlyGen cross-references, 5 entries: 1g1r, 1g1t, 2kmb, 2r61, 2z8l.
Intersection 3, union 12.

**Lactose**

Beta reducing end: 146 entries. Alpha reducing end: 67 entries.
1BZW appears in both.

### 3.3 Archetype family of 6'-sialyllactose

*The archetype family and the counts in this section were verified on 28 October 2026.*

GlyTouCan groups registrations that differ only in the anomeric
configuration or ring form of the reducing-end residue under a single
archetype accession. Each member keeps its own citable accession; the
archetype carries its own accession as well. The grouping is shown on
the archetype's Structure Detail page as an Archetype Glycan Family
table, and the Browse interface can list archetypes only.

| Member | Reducing end | PDB entries |
|---|---|---|
| G28868ZC | beta, pyranose | 12 |
| G63717BV | alpha, pyranose | 0 |
| G69893KP | unspecified, pyranose | 12 |
| G09675VB | unspecified, ring form unspecified | 0 |
| **G77019UJ** | **archetype** | **12** |

Five accessions denote the same glycan. Three return 12 entries; two
return none. No empty result was accompanied by any indication that the
query could not be satisfied as posed.

Registry-wide scale: the GlyTouCan Browse interface reports the number of
registered accessions and, with the "Archetype Glycans Only" filter
applied, the number of archetype structures. Observed at
https://glytoucan.org on 28 October 2026:

| | Count |
|---|---|
| Registered accessions | 257,041 |
| Archetype structures | 92,970 |
| Difference | 164,071 |

Sixty-four per cent of registered accessions are therefore members rather
than archetypes: they share a topology with at least one other accession
and differ only in the anomeric configuration or ring form of the
reducing-end residue. 6'-sialyllactose is not an unusual case.

### 3.4 Effect of single structural changes

Baseline: 3'-sialyllactose, beta reducing end, 30 PDB entries.

| Change | PDB entries |
|---|---|
| baseline | 30 |
| reducing end beta to alpha | 19 |
| sialic acid linkage a2-3 to a2-6 | 12 |
| Neu5Ac to Neu5Gc | 1 |
| add Fuc(a1-3) to the reducing-end residue | 0 |
| remove sialic acid (lactose) | 146 |

### 3.5 A change in tool behaviour during the study

An anomeric normalization fallback was added to `search_pdb_structures`
in the course of this work.

| Structure with unspecified anomer | Before | After |
|---|---|---|
| 3'-SL (G56516VH) | 0 (`matchedBy: none`) | 30 (`matchedAnomericState: beta`) |

After the change, a query carrying an unspecified anomeric configuration
is rewritten to the beta form. For 3'-sialyllactose this returns the 30
beta entries and omits the 19 alpha entries; the union of 48 is still not
reached.

The fallback applies to the anomeric configuration only. Structures with
an unspecified linkage position or an unspecified ring form are not
rewritten and return nothing.

This is recorded because it illustrates why observation dates are stated
throughout: the behaviour of a tool an agent calls may change between
runs.

---

## 4. Queries

### 4.1 Glycoproteins carrying a given glycan (GlyCosmos)

Endpoint `https://ts.glycosmos.org/sparql`

```sparql
PREFIX glycoconjugate: <http://purl.jp/bio/12/glyco/conjugate#>
PREFIX sio: <http://semanticscience.org/resource/>

SELECT DISTINCT ?protein
FROM <http://rdf.glycosmos.org/glycoprotein>
WHERE {
  ?protein glycoconjugate:glycosylated_at ?site .
  ?site sio:SIO_000255 ?bn .
  ?bn glycoconjugate:has_saccharide <http://rdf.glycoinfo.org/glycan/G49108TO> .
}
```

The path from a glycosylation site to its glycan passes through an
intermediate node. Queries written as
`?site glycoconjugate:has_saccharide ?glycan` return no rows.

Glycoprotein IRIs are of the form
`http://glycosmos.org/glycoprotein/[UniProt accession]`.

### 4.2 WURCS sequence of an accession (GlyCosmos)

```sparql
PREFIX glycan: <http://purl.jp/bio/12/glyco/glycan#>

SELECT ?seq
WHERE {
  <http://rdf.glycoinfo.org/glycan/G28868ZC> glycan:has_glycosequence ?gs .
  ?gs glycan:has_sequence ?seq ;
      glycan:in_carbohydrate_format glycan:carbohydrate_format_wurcs .
}
```

Address the glycan by its IRI. Matching on `dcterms:identifier` can bind
to more than one node and produce spurious rows.

### 4.3 Disease annotations (UniProt)

Endpoint `https://sparql.uniprot.org/sparql`

```sparql
PREFIX up: <http://purl.uniprot.org/core/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX uniprotkb: <http://purl.uniprot.org/uniprot/>

SELECT ?mnemonic (GROUP_CONCAT(DISTINCT ?diseaseName; separator=" | ") AS ?diseases)
FROM <http://sparql.uniprot.org/uniprot>
FROM <http://sparql.uniprot.org/diseases>
WHERE {
  VALUES ?protein { uniprotkb:Q12830 uniprotkb:Q15021 uniprotkb:P12270 }
  ?protein up:mnemonic ?mnemonic .
  OPTIONAL {
    ?protein up:annotation ?annot .
    ?annot a up:Disease_Annotation ;
           up:disease ?disease .
    ?disease skos:prefLabel ?diseaseName .
  }
}
GROUP BY ?mnemonic
```

---

## 5. Traversal to disease annotations

Starting from beta-GlcNAc (G49108TO), GlyCosmos returns 8,767
glycoproteins. The first 60 rows were taken, giving 52 distinct proteins,
and passed to UniProt. Eight carried disease annotations.

| UniProt | Disease |
|---|---|
| BPTF | Neurodevelopmental disorder with dysmorphic facies and distal limb anomalies |
| NCAPD2 | Microcephaly 21, primary, autosomal recessive |
| GGN | Spermatogenic failure 69 |
| INF2 | Charcot-Marie-Tooth disease, dominant intermediate E; Focal segmental glomerulosclerosis 5 |
| MAN1B1 | Rafiq syndrome |
| SPEN | Radio-Tartaglia syndrome |
| SNAP29 | CEDNIK syndrome |
| TPR | Intellectual developmental disorder, autosomal recessive 79 |

**This is a sample, not a rate.** Eight of 52 proteins drawn from the
first rows returned; it is not the proportion of all 8,767 that carry
disease annotations. The sample includes non-human proteins.

G49108TO is a single beta-GlcNAc residue. Whether it constitutes
O-GlcNAc depends on the aglycone, which the glycan accession does not
determine.

---

## 6. Routes that did not return

| Query | Outcome | How the failure appeared |
|---|---|---|
| Substructure search for sialyl Lewis x | unavailable | Stated explicitly: the dataset required was not published on the endpoint, and the question could not be posed |
| Superstructure search for G00054MO | 0 | no indication |
| Glycoproteins carrying sialyl Lewis x (GlyCosmos) | 0 | no indication |
| Glycoproteins carrying sialyl Lewis x (GlyGen) | 0 | no indication |

The substructure search returned the only message distinguishing "no
glycan contains this structure" from "that question cannot currently be
asked".

For sialyl Lewis x, GlyGen recorded 4 motifs (Type 2 LN, Lewis x, Sialyl
Lewis x, 3-Sialyl-LN), 6 species, 106 publications and 193
cross-references, while the structured glycoprotein field was empty.

---

## 7. Session statistics

These statistics come from 237 chat exports of glyconavi-llm-mcp, the
GlycoNAVI LLM–MCP service (in-house), analysed for the 45th Annual Meeting
of the Japanese Society of Carbohydrate Research (September 14–16, 2026),
where they were first presented. All language models were served locally,
and no session switched between models. The script that produces every figure in this
section, `analyze_sessions.py`, is published with this record. The exports
themselves are not published, because they contain internal network
addresses and the full text of the questions.

How the figures are counted:

- one export file is one session;
- structure-started sessions are GlycoCraft session-editing requests (the
  title begins with "GlycoCraft"); all other sessions are question-led;
- a tool call is one timeline event of kind `tool_call`;
- servers and resources are assigned from tool names, as listed in the script.

### 7.1 Question-led sessions

- Sessions: 224, answering 53 kinds of question posed in natural language
- Collection period: April 8 – July 16, 2026
- Tool calls: 4,085, using 67 distinct tools

| Main language model of the session | Sessions |
|---|---|
| Qwen3.6-35B-A3B | 155 |
| Gemma 4 26B-A4B | 32 |
| Gemma 4 31B | 11 |
| Gemma 4 E4B | 10 |
| Qwen3.6-27B | 5 |
| Qwen3-32B | 3 |
| No model call recorded | 8 |

| MCP server | Tool calls | Share (%) |
|---|---|---|
| TogoMCP | 2,386 | 58.4 |
| GlycoNAVI MCP | 1,587 | 38.8 |
| PubMed MCP | 39 | 1.0 |
| GlycanBuilder-MCP | 1 | 0.0 |
| Other | 72 | 1.8 |
| **Total** | **4,085** | **100** |

The JSCR poster reported 1,586 calls for GlycoNAVI MCP and 73 for Other;
one call was assigned to a different group.

| Servers used in the session | Sessions | Share (%) | Median resources reached |
|---|---|---|---|
| GlycoNAVI MCP + TogoMCP | 160 | 71.4 | 5.5 |
| TogoMCP only | 39 | 17.4 | 2 |
| GlycoNAVI MCP only | 10 | 4.5 | 1 |
| GlycoNAVI MCP + TogoMCP + PubMed MCP | 8 | 3.6 | 6 |
| No named tool call | 6 | 2.7 | 0 |
| GlycanBuilder-MCP + GlycoNAVI MCP + TogoMCP | 1 | 0.4 | 7 |

Distinct resources reached per session: median 4, maximum 17; six sessions
reached none.

| Resources reached | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Sessions | 6 | 25 | 39 | 23 | 22 | 24 | 29 | 22 | 12 | 10 | 2 | 3 | 3 | 0 | 0 | 1 | 2 | 1 |

Tool calls to single-database tools: UniProt 836, ChEMBL 621, Reactome 525,
QuickGO 299, PDB 238, GlyGen 98, Rhea 74, TogoID 72.

**Differences from the JSCR poster.** The number of resources reached
depends on how tools are grouped into resources. The JSCR poster used a
different grouping and reported a maximum of 15 and a median of 5 for
sessions using both main servers; the overall median of 4 is the same under
either grouping. Its figure of 76 is the number of distinct tools across all
237 sessions, not the number of resources, and its per-resource counts
(UniProt 840, ChEMBL 622) include the structure-started sessions.

Sessions that combined several servers tended to reach more resources.
Question complexity may drive both the number of servers used and the
number of resources reached, so this is an association, not a causal claim.

### 7.2 Structure-started sessions

- Sessions: 13 GlycoCraft session-editing requests, each asking to remove
  one residue (Gal, Fuc or GlcNAc) from a public GlyTouCan structure
- Date: June 20, 2026
- Language model: Qwen3.6-35B-A3B (all 13 sessions)
- Tool calls: 125

| MCP server | Tool calls | Share (%) |
|---|---|---|
| GlycanBuilder-MCP | 81 | 64.8 |
| TogoMCP | 20 | 16.0 |
| GlycoNAVI MCP | 4 | 3.2 |
| Other (no tool name recorded) | 20 | 16.0 |
| **Total** | **125** | **100** |

### 7.3 The 3′-sialyllactose comparison shown at JSCR

The comparison of anomeric forms reported at the JSCR meeting (there labelled
GM3, meaning its glycan portion without ceramide) was obtained in a separate
claude.ai session, not in the sessions above. A structured record of that
session, `SFG2026_BM16_GM3_session_2026-08-03.json`, is published with this
record.

- Date: August 3, 2026 (last updated August 4, 2026, UTC)
- Interface and model: claude.ai, Claude (Anthropic); the model version is
  not recorded in the transcript
- MCP server: GlycanBuilder-MCP only; 14 tool calls, 13 executed

| Step | Tool | Result |
|---|---|---|
| Build Neu5Ac(α2-3)Gal(β1-4)Glc residue by residue | `add_residue` ×3 | WURCS with the reducing-end anomer unspecified |
| Resolve the accession | `search_glycan` (database = GlyTouCan) | G56516VH |
| Set the reducing end to β, then α | `set_linkage` ×2 | G91237TK (β), G92323ZH (α) |
| Search deposited structures | `search_pdb_structures` ×3 | β 30, α 19, unspecified 0 |

The union of the α and β results is 48 entries; 6Y5Y is the only entry in
both. **The α and β lists are identical to those obtained on August 12, 2026
(section 3.2).** The unspecified form returned 0 because the anomeric
normalization fallback had not yet been added; after it was added, the same
query returned 30 (section 3.5). Both values are correct for the tool
behaviour at the time of the query.

In that session the default `search_glycan` returned only a GlycoNAVI hub
URL; specifying `database = GlyTouCan` was needed to obtain the accession.
Direct conversion from IUPAC condensed notation (`encode_structure`) did not
succeed, so the structure was built residue by residue.

---

## 8. Reproducing these results

1. Construct the WURCS string, or take it from section 2.1.
2. Resolve it to a GlyTouCan accession (`search_glycan`, or the GlyTouCan
   REST API).
3. Search the PDB by WURCS (`search_pdb_structures`, or the RCSB Search
   API against branched-entity descriptors).
4. Query GlyCosmos and UniProt with the SPARQL in section 4.
5. For the session statistics, run `python3 analyze_sessions.py <directory>`
   on glyconavi-llm-mcp chat exports.

Counts may differ from those recorded here. The PDB grows; tool
behaviour changes; archetype coverage is being extended. Each count in
this record is an observation of the date stated for it.

---

## 9. References

**Symbol Nomenclature for Glycans (SNFG)**
- Varki A, et al. Symbol Nomenclature for Graphical Representations of Glycans. *Glycobiology* 25:1323–1324 (2015). https://doi.org/10.1093/glycob/cwv091
- Neelamegham S, et al. Updates to the Symbol Nomenclature for Glycans guidelines. *Glycobiology* 29:620–624 (2019). https://doi.org/10.1093/glycob/cwz045

**WURCS**
- Tanaka K, et al. WURCS: the Web3 unique representation of carbohydrate structures. *J Chem Inf Model* 54:1558–1566 (2014). https://doi.org/10.1021/ci400571e
- Matsubara M, et al. WURCS 2.0 Update To Encapsulate Ambiguous Carbohydrate Structures. *J Chem Inf Model* 57:632–637 (2017). https://doi.org/10.1021/acs.jcim.6b00650

**GlyTouCan**
- Tiemeyer M, et al. GlyTouCan: an accessible glycan structure repository. *Glycobiology* 27:915–919 (2017). https://doi.org/10.1093/glycob/cwx066
- Fujita A, et al. The international glycan repository GlyTouCan version 3.0. *Nucleic Acids Res* 49:D1529–D1533 (2021). https://doi.org/10.1093/nar/gkaa947

**GlyCosmos**
- Yamada I, et al. The GlyCosmos Portal: a unified and comprehensive web resource for the glycosciences. *Nat Methods* 17:649–650 (2020). https://doi.org/10.1038/s41592-020-0879-8

**GlyGen**
- York WS, et al. GlyGen: Computational and Informatics Resources for Glycoscience. *Glycobiology* 30:72–73 (2020). https://doi.org/10.1093/glycob/cwz080

**Software and services**
- GlycanBuilder-MCP: https://gb.glyconavi.org (MCP endpoint: https://gb.glyconavi.org/mcp)
- Session statistics script: [`analyze_sessions.py`](analyze_sessions.py)
- Structured record of the August 3, 2026 session: [`SFG2026_BM16_GM3_session_2026-08-03.json`](SFG2026_BM16_GM3_session_2026-08-03.json)
- Figure sources (scripts and SVG, English and Japanese): [`figure_sources.zip`](figure_sources.zip)
- TogoMCP: https://togomcp.rdfportal.org/mcp
- Model Context Protocol: https://modelcontextprotocol.io

---

## 10. Correspondence and licence

Issaku Yamada — Laboratory of Glycoinformatics, The Noguchi Institute

This record is made available under the Creative Commons Attribution 4.0
International licence (CC BY 4.0). You are free to share and adapt it,
including for commercial purposes, provided you give appropriate credit.

https://creativecommons.org/licenses/by/4.0/

Suggested citation:

> Yamada I, Kimura N, Terauchi H, Matsubara M. Reproducibility record for
> "Registered but unreachable: what shared glycan identifiers do not
> resolve". SFG 2026 Annual Meeting, poster BM-16. Laboratory of
> Glycoinformatics, The Noguchi Institute, 2026. CC BY 4.0.
