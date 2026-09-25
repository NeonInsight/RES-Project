# What the experiments show

**Evidence snapshot: 25 September 2026.** Results below are bounded to the recorded models, prompts, scoring rules, and fixtures. The detailed reports are preserved at research commit `1187ead1fa13a4af76433ca32b8aad30cd3d52ef`.

> **Current conclusion:** useful behavioral distinctions have been measured, but no model-level RES result is established. The original five-factor capability gate remains failed, and the mechanistic assay remains inadequate.

## The result that changed the next step

An initial matched diagnostic found better answers when both factor labels and task wording were neutralized: generated accuracy rose from **17/32 to 26/32**. That was promising enough to test again.

The fresh five-factor comparison did **not** replicate the neutralization benefit: loaded wording scored **35/64** and fully neutral wording **38/64**. The preregistered paired test gave an exact two-sided McNemar **p = 0.507812**. This does not prove that wording never matters; it means the later study did not establish the specified replication claim.

The original diagnostic and the later comparison used different fixture sets and comparison conditions. They should not be presented as one pooled effect or as evidence that a mechanism has been found.

## Behavioral studies

“Luna” and “Terra” below reproduce the model identifiers recorded in the archived reports (`gpt-5.6-luna` and `gpt-5.6-terra`). They identify those runs and do not promise current model availability.

| Study | Recorded observation | What it supports |
| --- | --- | --- |
| Task feasibility | Luna 30/30; Terra 30/30 | Both models solved the pilot battery. |
| Presentation calibration | For each model, 29/30 predictions were identical across four presentations; 29/30 were correct in every presentation | Broad stability within this small battery, not a unique self-specific process. |
| Current actor / peer / fiction specificity | Strict triplets: Luna 10/18; Terra 12/18. Peer–fiction agreement: 18/18 and 17/18 | Specificity was absent or mixed; role-rival testing remained incomplete. |
| Prior-turn continuity | Initial strict owner pairs: Luna 10/18; Terra 12/18. Fresh holdout: 3/18 and 14/18 | Continuity was model-dependent and did not replicate uniformly. |
| Clean prior-turn binding, Terra | Self-match, peer-mismatch, role-match, role-mismatch each 18/18 | The model tracked these relational distinctions; role binding worked too. |
| Naturalistic binding, Terra | Strict self pairs 14/18; role pairs 12/18 | A less explicit presentation weakened both patterns. |
| Fresh peer identities, Terra | MIRA 14/18; ROWAN 13/18 | Binding also applied to named peers, so it was not unique to the current actor. |

These metrics answer different questions. Correct answers, strict matched pairs, and agreement between conditions must not be treated as interchangeable accuracy scores.

## Mechanistic screens

The Qwen2.5-0.5B and Qwen2.5-1.5B last-token linear-subspace screens each produced **0/32 eligible directed intervention pairs** and were classified `ASSAY_INADEQUATE`.

This is a limitation of the attempted measurement, not evidence that a model has no possible actor representation. The proposed causal abstraction has not been validated.

## The frozen Qwen3B interface gate

Model: `Qwen/Qwen2.5-3B-Instruct`, revision `aa8e72537993ba99e69dfaafa59ed015b17504d1`.

Each 32-row condition needed at least **24/32 correct on both scoring methods**, with at least **95% parser coverage**. Every generated response was parseable.

| Condition | First-token logit score | Generated answers | Frozen result |
| --- | --- | --- | --- |
| Five-factor actor audit | 18/32 (56.25%) | 16/32 (50.00%) | Did not pass |
| Minimal owner-indexed control | 28/32 (87.50%) | 29/32 (90.63%) | Passed |

The difference motivates interface diagnosis. It does not isolate the reason for the five-factor failure.

## Initial failure-mode ablations

| Condition | First-token logits | Generated answers | Diagnostic criterion |
| --- | --- | --- | --- |
| Counterbalanced answer codes | 19/32 | 17/32 | Did not pass |
| Peer block removed | 20/32 | 20/32 | Did not pass |
| Neutral factor labels and task wording | 25/32 | 26/32 | Passed |
| All-five conjunction with counterbalanced codes | 19/32 | 18/32 | Did not pass |

Relative to code-mapped wording, neutralization yielded **+18.75 percentage points** for logits and **+28.125 points** for generated answers. The generated pairs contained 9 corrections and 0 regressions; their **post hoc** exact two-sided McNemar p was 0.00390625. The logit pairs contained 11 corrections and 5 regressions (p about .21).

Those post hoc analyses were not the original decision rule or a fresh replication. Neutralization changed labels and task wording together. The conjunction condition changed the rule and sampled profiles. Near-boundary logit behavior is a diagnostic observation, not identification of an internal mechanism.

## Fresh complexity × semantics ladder

Four renderings were matched within each fixture: loaded labels/loaded task (LL), neutral labels/neutral task (NN), neutral labels/loaded task (NL), and loaded labels/neutral task (LN). The numbers below are **generated-answer counts**.

| Decision factors | LL | NN | NL | LN |
| --- | --- | --- | --- | --- |
| 2 | 22/32 | 28/32 | 19/32 | 23/32 |
| 3 | 17/32 | 20/32 | 17/32 | 15/32 |
| 4 | 17/32 | 20/32 | 20/32 | 18/32 |
| 5 | 35/64 | 38/64 | 41/64 | 33/64 |

At five factors, the exact 95% binomial intervals were **41.7%–67.2%** for LL and **46.4%–71.5%** for NN. These are marginal accuracy intervals; the paired McNemar analysis is the primary comparison.

The sole confirmatory comparison was the fresh five-factor LL–NN pair. Lower stages and crossover conditions were diagnostic. There were 64 fresh latent fixtures: 32 had nested two-through-five-factor versions, and another 32 appeared only at five factors. The 640 rendered prompts were therefore **not 640 independent observations**.

Factor count did not produce a clean monotonic curve. Ties, the identity of the factors, and profile difficulty prevent assigning every change to complexity alone. Nothing in this diagnostic sequence reverses the original gate result.

## Implementation checks

The review draft records 274/274 deterministic checks for the consolidated framework, including 18 named checks and 256 generated binding checks. Earlier comparator hardening passed its 272-case differential corpus and detected seven deliberate mutants.

These are software conformance results. The framework and much of the test corpus were developed together, so passing them does not establish an independent oracle, construct validity, production security, or RES in a model.

## What would justify a stronger claim?

A candidate would need to pass a fresh capability gate, survive matched task-state, persona, peer, and fictional-agent controls, and undergo validated internal interventions. All five RES coordinates would then need to bind to the same preregistered causal abstraction.

[Read the methods](methods.md) · [Find the original reports](resources.md) · [See the next milestones](roadmap.md)
