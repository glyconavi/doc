#!/usr/bin/env python3
"""Session statistics for SFG 2026 poster BM-16.

Reads glyconavi-llm-mcp chat exports (schema "glyconavi-chat-export",
format 1.1) and reports the figures given in section 7 of the
reproducibility record.

Usage:  python3 analyze_sessions.py <directory-of-json-exports>

Counting rules
- A session is one export file.
- Structure-started sessions are GlycoCraft session-editing requests
  (the title begins with "GlycoCraft"); all others are question-led.
- A tool call is one timeline event with kind == "tool_call".
- Servers are assigned from tool names (SERVER below). Calls with no
  tool name are counted as "Other".
- Resources are assigned from tool names (RESOURCE below). This grouping
  is a choice: a different grouping changes per-session resource counts.
"""
import json, glob, os, sys, statistics, collections, datetime

PUBMED = {"search_articles", "get_article_metadata", "find_related_articles",
          "lookup_article_by_citation", "get_full_text_article",
          "get_copyright_status", "convert_article_ids"}
TOGO = {"get_MIE_file", "run_sparql", "search_uniprot_entity", "search_chembl_molecule",
        "search_chembl_target", "search_mesh_descriptor", "search_pdb_entity",
        "search_reactome_entity", "search_rhea_entity", "togoid_convertId"}
OTHER = {"ncbi_ncbi_esearch", "ncbi_esearch", "ncbi_esummary", "ncbi_efetch",
         "get_pubchem_compound_id", "get_compound_attributes_from_pubchem",
         "search_chembl_id_lookup"}

def server(tool):
    if tool is None: return "Other"
    if tool.startswith("glycan_"): return "GlycanBuilder-MCP"
    if tool in PUBMED: return "PubMed MCP"
    if tool in TOGO: return "TogoMCP"
    if tool in OTHER: return "Other"
    return "GlycoNAVI MCP"

RESOURCE = [("uniprot", "UniProt"), ("chembl", "ChEMBL"), ("reactome", "Reactome"),
    ("quickgo", "QuickGO"), ("pdb", "PDB"), ("glygen", "GlyGen"), ("rhea", "Rhea"),
    ("togoid", "TogoID"), ("mesh", "MeSH"), ("ggdonto", "GGDonto"), ("alphafold", "AlphaFold DB"),
    ("protein_atlas", "Human Protein Atlas"), ("kegg", "KEGG"), ("interpro", "InterPro"),
    ("ensembl", "Ensembl"), ("string", "STRING"), ("gwas", "GWAS Catalog"), ("gtex", "GTEx"),
    ("bindingdb", "BindingDB"), ("pubchem", "PubChem"), ("ols", "OLS"), ("glytoucan", "GlyTouCan"),
    ("lectin", "lectin data"), ("paconto", "PAConto"), ("clinical_trials", "ClinicalTrials.gov"),
    ("ncbi", "NCBI"), ("glycoepitope", "GlycoEpitope"), ("mie", "RDF Portal"),
    ("run_sparql", "RDF Portal"), ("enzyme_substrates", "glycosyltransferase data"),
    ("protein_glycosylation", "glycosylation sites"), ("glycan_by_name", "glycan names"),
    ("glycans_by_organism", "glycan names"), ("article", "PubMed"), ("copyright", "PubMed"),
    ("glycan_", "GlycanBuilder")]

def resource(tool):
    if tool is None: return None
    t = tool.lower()
    for key, name in RESOURCE:
        if key in t: return name
    return None

def model_name(m):
    m = m.lower().replace("google/", "").replace("qwen/", "")
    return {"qwen3.6-35b-a3b": "Qwen3.6-35B-A3B", "qwen3.6-27b": "Qwen3.6-27B",
            "qwen3-32b": "Qwen3-32B", "gemma-4-26b-a4b": "Gemma 4 26B-A4B",
            "gemma-4-e4b-it": "Gemma 4 E4B", "gemma-4-31b-it": "Gemma 4 31B",
            "gemma4-31b": "Gemma 4 31B"}.get(m, m)

def load(directory):
    out = []
    for path in sorted(glob.glob(os.path.join(directory, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            d = json.load(fh)
        if d.get("schema") != "glyconavi-chat-export": continue
        events = [e for b in d["bubbles"] for e in (b.get("timelineEvents") or [])]
        models = collections.Counter(model_name(e["model"]) for e in events
                    if e.get("kind") in ("llm_dispatch", "llm_call") and e.get("model"))
        start = min(b["timestamp"] for b in d["bubbles"] if "timestamp" in b)
        out.append({"title": d["metadata"]["title"].strip(),
                    "date": datetime.datetime.fromtimestamp(start / 1000, datetime.timezone.utc).date(),
                    "model": models.most_common(1)[0][0] if models else None,
                    "tools": [e.get("toolName") for e in events if e.get("kind") == "tool_call"]})
    return out

def report(name, sessions):
    calls = [t for s in sessions for t in s["tools"]]
    print(f"\n== {name}: {len(sessions)} sessions, {len(calls)} tool calls")
    print("period:", min(s["date"] for s in sessions), "to", max(s["date"] for s in sessions))
    print("question types:", len({s["title"].rstrip("？?").strip() for s in sessions}))
    print("sessions by model:", dict(collections.Counter(s["model"] for s in sessions).most_common()))
    print("calls by server:", dict(collections.Counter(server(t) for t in calls).most_common()))
    print("distinct tools:", len({t for t in calls if t}))
    per = [len({resource(t) for t in s["tools"] if resource(t)}) for s in sessions]
    print("resources per session: median", statistics.median(per), "max", max(per),
          "| sessions with none:", per.count(0))
    print("distribution:", [per.count(i) for i in range(max(per) + 1)])
    combos = collections.defaultdict(list)
    for s, n in zip(sessions, per):
        combos[" + ".join(sorted({server(t) for t in s["tools"]} - {"Other"})) or "(no named tool call)"].append(n)
    for k, v in sorted(combos.items(), key=lambda x: -len(x[1])):
        print(f"  {len(v):4d} sessions  median resources {statistics.median(v):>4}  {k}")
    print("calls by resource:", dict(collections.Counter(resource(t) for t in calls if resource(t)).most_common(10)))

if __name__ == "__main__":
    S = load(sys.argv[1] if len(sys.argv) > 1 else ".")
    report("question-led", [s for s in S if not s["title"].startswith("GlycoCraft")])
    report("structure-started", [s for s in S if s["title"].startswith("GlycoCraft")])
    report("all sessions", S)
