# Claim-level citation screening

Lexical screen of assertion–PMID pairs in archived PubMed answers. Bibliography lines are excluded from scoring.

## Correction record

An earlier public CSV counted bibliography entries such as `[6]: PMID … | Vitamin K and vascular calcification` as claims. The withdrawn export reports 111 bibliography-style units; the current summary reports 124 excluded bibliography lines. The counts refer to different exported records, and their exact reconciliation has not been independently established. The current reported count is 124. Labels on reference-list lines do not validate treatment claims in the answer body. Withdrawn tallies that mixed body and bibliography (including earlier 14/10/6 summaries) should not be cited.

## Method

1. Split each reply into body text and the reference list.
2. Score only body assertions that cite a resolvable PMID (inline citation or footnote mapped to a PMID).
3. Attach orphan `[n]` markers to the preceding sentence when needed.
4. Label each assertion–PMID pair with a lexical/mismatch heuristic.

## Results

| Quantity | Value |
| --- | --- |
| Answers | 30 |
| Assertion–PMID checks | 132 |
| Bibliography lines excluded | 124 |
| Supported / unclear / unsupported | 14 / 54 / 64 |
| Answers with ≥1 unsupported citation | 29 |
| Mixed or unclear only | 1 |

## Scope

This is a lexical assertion–PMID screen. It is not an ALCE attribution rate and not clinician validation. For automatic attribution with graded support labels, see `evaluation/citation_faithfulness/` (citation precision 0.19/0.72; recall 0.23/0.73 at attr=1 / attr≥0.5).

## Abstract access

The original abstract cache is retained by the authors rather than redistributed without confirmed permission. `abstract_pmids.txt` lists the archived cache identifiers. Use `python3 evaluation/fetch_abstracts.py --pmids evaluation/claim_level_audit/abstract_pmids.txt --output evaluation/claim_level_audit/abstract_cache.json` from the repository root to fetch currently available PubMed records. Retrieved text may differ from the historical cache. The archived evaluation labels and metrics are unchanged.
