# ALCE/MedCite-style citation faithfulness (machine eval)

Automatic attribution of ECHO-AI literature answers against PubMed abstracts, following [ALCE](https://github.com/princeton-nlp/ALCE) **citation precision** / **citation recall**.

## Named metrics

| Name (ALCE) | Definition |
|-------------|------------|
| **Citation precision** | Fraction of (statement, PMID) instances whose abstract supports the statement |
| **Citation recall** | Fraction of statements with ≥1 supporting cited PMID |

Both metrics are reported at attr=1 and at attr≥0.5 (partial support counts only in the latter).

## Method

1. Extract answer-body assertions with resolvable PMIDs (bibliography excluded).
2. Fetch title+abstract via NCBI E-utilities (`abstract_cache.json`).
3. Local judge `Qwen/Qwen3-4B-Instruct-2507` (temp 0; **same family** as the reply formatter) → {0, 0.5, 1}.
4. Aggregate precision over citation instances; recall over statements.

## Reproduce

The archived runner is provided for methodological inspection. It expects a historical answer corpus (`heldout_qa_set.csv` and lab Q&A logs) that is not fully included in this release, as well as vLLM at `http://127.0.0.1:8001` to re-judge. Full historical re-judging is therefore not supported by this snapshot alone. Offline rate check (no GPU):

```bash
python3 evaluation/verify_results.py   # public layout
```

## Headline results (2026-11-24)

| ALCE metric | Value |
|-------------|-------|
| Citation precision (attr=1 / attr≥0.5) | **0.19 / 0.72** |
| Citation recall (attr=1 / attr≥0.5) | **0.23 / 0.73** |

28 answers · 86 statements · 114 citation instances · 60 scores are 0.5 · 0 parse failures.

**Veterinary PMID 29314873** (AAHA dogs/cats) appears in 8 historical diabetes citation instances and receives 3 attr=1 judgments on human-diabetes claims—judge leniency across species. Not used as a positive appendix example.

Lexical claim audit (14/132 supported) is not the attr≥0.5 precision 0.72.

Not clinician validation.

## Abstract access

The original abstract cache is retained by the authors rather than redistributed without confirmed permission. `abstract_pmids.txt` lists the archived cache identifiers. Use `python3 evaluation/fetch_abstracts.py --pmids evaluation/citation_faithfulness/abstract_pmids.txt --output evaluation/citation_faithfulness/abstract_cache.json` from the repository root to fetch currently available PubMed records. Retrieved text may differ from the historical cache. The archived evaluation labels and metrics are unchanged.
