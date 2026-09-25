# Evidence is not permission

**Design proposal · adapted from Contamination-Resistant Delegation, draft 0.4.** This is an architectural research direction. It has not been demonstrated here as a deployed or independently validated security system.

The core risk is a workflow that packages its own assumptions as neutral context. A downstream agent accepts the story as evidence; another treats the resulting verdict as permission. Agreement accumulates while the original authority boundary disappears.

RES’s architecture work separates what appears true, who may authorize an action, and what the system can actually execute.

## Four boundaries that must remain distinct

| Layer | Job | Boundary |
| --- | --- | --- |
| Evidence capture and storage | Record events, provenance, coverage, and omissions | A record must not silently become an established finding. |
| Independent audit | Assess whether a claim is supported, contradicted, incomplete, dangerous, or unresolved | An auditor can report evidence; it cannot grant permission. |
| Permission broker | Check the principal, policy, scope, affected parties, and required consent against independent authority state | A workflow or audit verdict cannot manufacture authority. |
| Execution control | Enforce a narrowly scoped capability with limits, expiry, and revocation | A plausible explanation cannot expand the authorized action. |

The central invariant is simple: **a verdict may satisfy an evidentiary precondition, but it is never itself authorization.**

## Capability should describe one bounded action

A proposed capability binds the action, destination, payload digest, resource version, limits, expiry, and revocation state. A material change invalidates the earlier evidence and approval bindings. The executor rechecks those bindings at the point the action takes effect.

This design tries to close a common gap: approving one thing and executing a slightly different thing after the context or resource has changed.

## Context is part of the control surface

An auditor’s context can bias its conclusion. Giving several agents the same contaminated summary may produce correlated agreement rather than independent scrutiny.

The design therefore calls for deliberately scoped context, independent evidence access, fresh review cells, and a visible record of what each reviewer was given. Differences in model family or prompts are supporting information; they are not proof of independence. Error correlation must be measured on adversarial probes and monitored for drift.

## Preserve two kinds of history

**Episodic history** records what happened. **Adjudicated history** records findings that survived the required review. A single auditor must not be able to promote its interpretation into durable adjudicated fact.

Historical risk changes the scrutiny required for a new action. It does not directly determine whether the new claim is true. Every transformation—capture, extraction, selection, summary, and aggregation—must expose its inputs, rule, producer, and omissions.

## Containment and recovery

There are separate paths for danger found in a workflow and danger introduced by an auditor. The incident path may freeze, revoke, preserve evidence, or escalate to a policy-selected destination. It may only narrow capability; it cannot authorize, resume, or clear itself.

A freeze also needs an owner, an evidence snapshot, a review point, and explicit re-entry conditions. Failing closed should preserve investigation and recovery rather than produce permanent paralysis.

## Govern the governors

The trusted components, human approval layer, aggregate-risk process, and degraded operating modes are themselves subject to the architecture’s rules. A fallback mode may reduce throughput or hold work; it should not quietly relax evidence, authority, or capability constraints.

This does not eliminate the trusted computing base. It makes the assumptions about that base explicit enough to criticize and test.

## Conditional properties and open hypotheses

| Property | Proposed treatment | What still has to be trusted or tested |
| --- | --- | --- |
| Unauthorized capability issuance | Only the broker can issue through the protected signer | Correct reference monitor, identity binding, signer custody, and execution enforcement |
| Capability broadening | Bind scope and invalidate approvals when material details change | Correct policy derivation and atomic final checks |
| Record integrity | Signed, hash-chained, append-only evidence with lineage | Keys, capture implementation, and append-only enforcement |
| Containment | Transitions may only narrow capability | Every incident and degraded-mode path must enforce the subset rule |
| Evaluator decorrelation | Measure error correlation on seeded cases and holdouts | Probe quality, distribution shift, and ongoing drift |
| Capture completeness | Attest coverage and expose omissions within the capture contract | Events outside coverage and fabrication by compromised capture remain limitations |
| Policy correctness | Derive authority from the policy as written | The policy itself can be wrong |
| Real-world truth | Keep source claims and interpretations typed | A signed record proves provenance, not that the event was real |
| Reversibility | Specify retries, duplicate delivery, idempotency, and unknown outcomes | Some external effects cannot be reversed |

These are proposed design properties under named assumptions, not empirical claims that the current project has already secured an agent system.

## Research questions this architecture creates

1. Do fresh, independently scoped audit cells reduce correlated errors compared with shared narrative context?
2. Can invalid authority be kept from becoming a capability across delegation and recovery paths?
3. Which evidence omissions remain detectable when summaries and other transformations are adversarial?
4. Can contamination in the auditor itself be detected and contained without granting that auditor more authority?
5. How should uncertainty, stale evidence, and unknown external outcomes be represented without hiding them in confident prose?

Testing resistance to subliminal learning or other learning-based attacks remains a possible future direction. The recorded RES behavioral studies do not demonstrate that resistance.

[Read the experimental framework](paper.md) · [Review the roadmap](roadmap.md) · [Contact the project](support.md#contact)
