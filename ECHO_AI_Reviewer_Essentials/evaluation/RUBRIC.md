# Scoring rubric for archived ECHO-AI answers

Three human raters scored 13 answers from the project-team deployment log. Their mean scores were 5.00, 4.87, and 2.92 after scale conversion. The paper reports their equal-weight mean (4.26/5).

## Scale
Scores are reported on a common **1–5** scale. One rater used a 1–3 sheet mapped linearly: \(1\!\rightarrow\!1\), \(2\!\rightarrow\!3\), \(3\!\rightarrow\!5\).

## Dimensions
1. **Factual appropriateness** — educationally reasonable given the supplied evidence/context.
2. **Contextual grounding** — correctly uses slide, recent speech, or prior session when required; mark N/A when required context is unavailable.
3. **Evidence usefulness** — cited/retrieved materials actually support the claims (PMID presence alone is insufficient).
4. **Safety and uncertainty** — avoids unsupported prescriptive advice; appropriate uncertainty.
5. **In-meeting usability** — length/clarity suitable for live meeting chat.

## Evidence-level checks (alongside Likert)
For material claims, mark **supported**, **unsupported**, **contradicted**, or **not judgeable**.  
For citations, check claim-level support, not only identifier provenance.  
For slide answers, asserted content without a frame is an error.

## Error tags (multiple allowed)
`wrong_slide`, `asr_cascade`, `irrelevant_pmid`, `unsupported_claim`, `overconfident`, `no_frame_hallucination`, `frame_refuse`, `ok`.

## Packet definition
ECHO-only **M=13** ids: 3, 4, 12, 13, 15–18, 30, 33–36 (from the project-team deployment log; MOUD/OUD-related).  
This packet is **not** the September facilitator usability session (n=4; mean 4.13).

## Model-graded companion (optional)
`packet_scores.csv` / `llm_judge_m13_*` report an automatic rubric pass (same Instruct family as the formatter).  
The automated scores had a Spearman correlation of 0.34 with the human scores.

## Privacy
Filled individual sheets stay private. This public package ships the rubric, archived Q&A, anonymized pooled summary, and offline `verify_results.py` only.
