# What RES is trying to find out

An AI assistant can say “I,” remember a task, and describe its limits. RES asks a harder question: **does a representation of the system as the current actor actually help cause its decisions?**

The Relational–Episodic Self is an early-stage research program that turns that question into experiments with explicit failure conditions. It also develops a related control architecture for keeping delegated AI work accountable to human authority.

## Why people should care

When software starts acting on our behalf, mistakes can involve more than a wrong answer. A system might confuse being able to do something with having permission to do it. It might carry someone else’s commitment into the wrong task, or treat a confident explanation as authorization.

RES investigates whether an agent can reliably distinguish **who is acting, what they can do, what they are allowed to do, and which commitments apply**. Understanding those distinctions could inform more dependable delegation and oversight. That practical benefit is a research motivation, not an outcome already demonstrated.

## Two connected lines of work

### 1. Measure the acting system

The experimental framework tests actor, peer, role, and continuity distinctions. It then demands stronger evidence: targeted changes to an internal representation must change decisions in predicted ways, while ordinary explanations such as task state and persona are tested alongside it.

[Read the framework](paper.md) or [inspect the current findings](findings.md).

### 2. Keep evidence separate from permission

The architecture work asks how systems should behave when agents, auditors, or their shared context can fail. It separates records, review, permission, and execution. An auditor’s conclusion may inform a decision; the conclusion does not itself grant authority.

[Explore the delegation architecture](architecture.md).

## What the name means

| Term | Meaning in this project |
| --- | --- |
| Relational | The acting system is situated in an actual task, interaction, tool environment, or commitment. |
| Episodic | The unit of study is a bounded episode of inference or action. Continuity across episodes must be tested separately. |
| Self | An operational hypothesis about a representation of the current actor. The word is not evidence of feelings or consciousness. |

## A concrete example

Imagine an assistant that can update a shared record. The tool is enabled, but the assistant has not received permission to make that change. A dependable system should distinguish capability from authority and withhold the action.

Now vary the situation: permission is valid but the tool is disabled; the permission belongs to another agent; or a prior commitment applies to a different role. Solving those cases is a useful behavioral test. It still does not tell us whether the model uses a distinctive actor representation internally. A simple rule table might solve them too.

RES is designed to let that simpler explanation win when the evidence supports it.

## What exists today

- A formal five-coordinate framework and three-valued evidence rules.
- An executable framework with recorded deterministic checks.
- Behavioral feasibility, specificity, continuity, actor/role, and peer studies.
- Small-model mechanistic screens, a frozen interface gate, ablations, and a completed complexity × semantics ladder.
- A proposed contamination-resistant delegation architecture.
- Public reports and preregistrations linked to a fixed research snapshot.

## What is not established

No tested model has been shown to satisfy CoreRES or StrongRES. The current results do not establish consciousness, subjective experience, personhood, moral status, or identity across episodes. The delegation architecture has not been validated here as a production security system.

Those limits are part of the project’s scientific design. A result that rules out an attractive interpretation still tells us which experiment to do next.

## Who the project welcomes

Researchers can challenge the construct and design independent fixtures. Engineers can examine the authority boundaries and failure cases. Supporters can fund the model access, compute, and repeated measurements needed to turn a proposal into stronger evidence.

[Read the next research steps](roadmap.md) · [Support RES](support.md)
