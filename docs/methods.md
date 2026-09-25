# How the work is tested

RES separates software correctness, behavioral performance, and mechanistic evidence. A success at one level does not substitute for a missing result at another.

## Start with an alternative explanation

A model may solve an actor task using ordinary instruction following, a rule table, task state, generic agent modeling, persona, or external scaffolding. A RES experiment must give those explanations a fair opportunity to account for the behavior.

Matched controls compare the current actor with peers, fictional agents, and role identities. Other controls vary capability independently of authority, and separate factor labels from task wording.

## Behavioral gates come before mechanism claims

An internal intervention is hard to interpret when the model cannot perform the underlying task. The completed Qwen3B gate therefore required both first-token logit accuracy and generated-answer accuracy of at least 24/32 in each condition, alongside 95% parser coverage.

Passing a diagnostic variant does not retroactively change that gate. A replacement gate would need a new prospective protocol and fresh fixtures.

## Preregister before looking

Preregistration specifies the question, fixtures or generation procedure, model revision, scoring, exclusions, thresholds, primary comparison, and interpretation rule before the relevant inference.

The complexity ladder fixed its two-through-five-factor sequence before running. It advanced on completion rather than favorable accuracy. Only the fresh five-factor generated-output LL–NN comparison was confirmatory. Lower stages, crossovers, logit behavior, and secondary modeling were diagnostic.

## Preserve the experimental unit

Multiple renderings of one logical fixture are matched observations. Nested versions of the same fixture across factor counts are also related. Repeated prompts must not be counted as independent samples merely because each made an API call.

The completed ladder contained 64 fresh latent fixtures and 640 prompts. Half the fixtures contributed nested lower-factor views. The reports retain the distinction between those counts.

## Report paired changes and uncertainty

For matched binary outcomes, record corrections, regressions, and unchanged pairs. The completed five-factor primary comparison used the exact two-sided McNemar test. Exact binomial intervals describe accuracy within each condition; they do not replace the paired comparison.

Report effect size, sample size, parser coverage, and the declared decision rule alongside a p-value. Preserve null results and conflicts. Do not promote a favorable post hoc analysis into a preregistered success.

## Step 0: validate the internal variable

The proposed mechanism study would identify a candidate actor representation and explicit task-state and persona rivals, then test them through interchange interventions or comparable causal-abstraction methods. Discovery and held-out validation must be separated.

The candidate’s identity, version, semantic interface, scope, and intervention meaning must be frozen before the five-coordinate confirmatory assay. API-only outputs normally cannot establish this step.

## Bind every claim to the same object

Evidence for all five coordinates must name the same validated abstraction, episode, branch family, and scope. Combining one mechanism’s cognition, another’s integration, and a third’s actor sensitivity does not establish one coherent RES profile.

Unvalidated measurements become `UNKNOWN` before aggregation. Missing access, incomplete rival tests, broken blinding, and inadequate provenance are assay limitations, not convenient positive or negative results.

## Reproducibility record

The experiment repository preserves runners, preregistrations, generated fixtures, model responses, summaries, and execution records. This public site pins its source links to research commit `1187ead1fa13a4af76433ca32b8aad30cd3d52ef` and archives human-readable reports and protocols.

The source manifest records upstream Git blob identities and local SHA-256 hashes. Hashes establish byte identity; they are not independent timestamps or proof that an interpretation is correct.

Model access and hosted execution conditions can change. Reproducing an archived run requires the recorded model revision, fixture and runner versions, sampling parameters, token budget, answer mapping, and execution state. A local report build does not rerun the models.

## Independent review needed

The framework and much of its test corpus were developed together. The next useful review should derive fixtures and expected outcomes independently, challenge the strongest rival explanations, and check raw-response completeness before interpreting a result.

[Open the evidence index](resources.md) · [Read the complete framework](paper.md)
