# Evaluation package (public, sanitized)

Supports the manuscript tables for:

1. **Paired zero-frame ablation** (33/35 vs 3/35)
2. **ECHO-content packet** (M=13; pooled human mean 4.26)
3. **Model-graded check** (Spearman ρ≈0.34; not clinician ratings)

## Offline verify (no GPUs)

```bash
python3 evaluation/verify_results.py
```

## Files

| File | Role |
|---|---|
| `paired_zero_frame.csv` | Per-arm labels for 35 paired asks |
| `paired_zero_frame_summary.md` | Count summary matching the paper |
| `packet_qa.csv` | Archived M=13 questions/answers for inspection |
| `heldout_qa_set_echo_only.csv` | Same packet ids with metadata |
| `packet_scores.csv` | Per-item human vs model means |
| `packet_scores_summary.json` | Anonymized pooled/per-rater means |
| `llm_judge_m13.csv` / `llm_judge_m13_summary.json` | Model-graded pass artifacts |
| `RUBRIC.md` | Scoring rubric |
| `verify_results.py` | Stdlib verification |

| `recorded_replay/` | GPU-free no-frame paired outputs (`paired_runs_n35.jsonl`, `paired_cases.json`) + HTML verifier |

| `routing_comparison/` | Focus and retrieval-intent comparisons, category-derived labels and predictions |
| `speech_recall_ablation/` | Paired speech/slide conflict runs, synthetic fixtures and controls |
| `citation_faithfulness/` | Archived citation attribution scores at both thresholds |
| `claim_level_audit/` | Archived lexical citation screen and correction record |

The offline verifier recomputes selected metrics from released labels and checks stored summary values. It does not rerun models or independently validate human ratings. The citation and lexical audit caches are not distributed; PMID lists and a fetch utility are provided. The original historical answer corpus is not fully public, so the full historical citation study cannot be regenerated from this release alone.

**Not included:** individual identifiable rater sheets, institutional indexes, credentials or private session media.
