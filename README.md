# The MSA Taxonomy

**Mechanism–Signal–Archetype: a structured vocabulary for elder-fraud manipulation tactics.**

Version 0.2.0 · Licensed CC BY 4.0 · Published by Sahai LLC

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22085666.svg)](https://doi.org/10.5281/zenodo.22085666)

---

## What this is

Fraud advice for older adults is usually written as prose. "Watch out for
gift-card requests." "Hang up if someone claims to be the IRS." Prose is fine
for a pamphlet. It is not something two researchers can code against, an
engineer can implement, or a paper can cite by identifier.

The MSA is that same knowledge written down as data. Every entity has a stable
id, a version, a severity, and a citation to where the claim comes from. There
are three levels:

| Level | Directory | What it answers |
|---|---|---|
| **Mechanism** | `mechanisms/` | *Why* did the person comply? The persuasion lever. |
| **Signal** | `signals/` | *What* can actually be observed in the contact? |
| **Archetype** | `archetypes/` | *Which* scam family do these signals compose into? |

Two supporting sets sit alongside them:

- `attributes/` — the case-file evidence matrix. What a triage conversation
  tries to establish, and the plain-language question it asks to establish it.
- `sources/` — necessary-for-legitimacy rules for commonly impersonated
  institutions. The IRS does not open contact by phone demanding payment. That
  is a rule, not an opinion, and it is written here as one.

`schema/` holds JSON Schemas that are authoritative for validation. If a file
and the prose disagree, the schema wins.

## What is in version 0.2.0

| Kind | Count |
|---|---|
| Mechanisms | 11 |
| Signals | 37 |
| Archetypes | 11 |
| Attributes | 13 |
| Sources | 3 |
| **Total entities** | **75** |

Of the 37 signals, 29 are behavioral signals observable in conversation, and 8
are `sig.detector.*` artifact screeners that match message text. See
"What is not here" below regarding those 8.

## Design commitments

**Deprecate, never delete.** An entity is retired by setting
`version_deprecated`. The file stays and its id stays resolvable forever. Ids
are never reused. Anything you cite here will still resolve.

**Every entity carries provenance.** The `provenance` block names the source
that grounds the entity and when it was retrieved. Sources include the FBI,
IC3, the FTC, Medicare, AARP, and published research. Entities migrated from
Sahai's own earlier hand-coded knowledge are marked `sahai-seed`.

**Grounding is declared, not assumed.** Each signal states whether it is
`theory`-grounded (it manifests one or more named persuasion mechanisms),
`operational` (it is a working detector with no theoretical claim), or
`ungrounded_pending_review`. Coercion signals such as threat of arrest are
marked `ungrounded_pending_review` on purpose: threat is not influence, and the
Cialdini and Stajano–Wilson frameworks model influence. Forcing them into a
mechanism would be a false claim, so they are flagged instead.

**Verbal and artifact signals stay separate.** An older adult's spoken
description of a pop-up and a forensic check on a screenshot of that pop-up are
two different observations with two different failure modes. They are two
entities, never one.

## Stability

**Version 0.2.0 does not yet guarantee stable identifiers.** Ids may still be
renamed before 1.0.0. If you are building on this, pin to a tagged release and
a DOI rather than tracking the default branch.

Version 1.0.0 is when the stable-id guarantee turns on. It is also when the
taxonomy will have been validated by coders outside the authoring team, with
inter-coder agreement reported. That validation work is planned, not done. It
would be dishonest to call this 1.0 before it happens.

## What is not here

This repository is the open part of a larger internal knowledge repository. The
following are deliberately withheld:

- the Sahai Fraud Verdict Engine and its source code
- the verdict gate: its rules, their ordering, and its response tables
- the regular expressions backing the `sig.detector.*` signals
- the regression and adversarial test corpora

The reasoning is a safety judgment, not a commercial one. The tactics described
here are already public through the FTC, AARP, and IC3, so publishing the
vocabulary tells a bad actor nothing new. Publishing the decision logic would
let them test messages against the exact conditions that protect an older adult
and rewrite around them.

The 8 `sig.detector.*` entities are published without their patterns, so that
archetype references resolve and so that others can write their own detector for
the same signal. They carry `pattern_published: false`.

## Using it

Every file is YAML with a stable `id`. To load the whole library:

```python
import glob, yaml

entities = {}
for path in glob.glob("*/*.yaml"):
    entity = yaml.safe_load(open(path, encoding="utf-8"))
    entities[entity["id"]] = entity

print(len(entities), "entities")
print(entities["arch.phantom_hacker"]["canonical_signals"])
```

To validate a copy you have modified:

```bash
pip install pyyaml jsonschema
python validate.py
```

## Citing it

Please cite the release, not the branch. See `CITATION.cff`. Both the archived
release and the accompanying paper should be cited where both are relevant.

## A word on what this is for

This vocabulary exists because a scam is a conversation, and conversations have
structure. Naming that structure precisely enough that two people can agree on
what they saw is the prerequisite for measuring whether anything we build
actually helps. That is the whole reason to publish it rather than keep it.

Corrections, disagreements, and additions are welcome. If a signal is wrong, or
a mechanism attribution is a stretch, that is worth knowing.

## License

CC BY 4.0. See `LICENSE` for the full text and `NOTICE.md` for the patent
reservation and the list of withheld material.

Copyright (c) 2026 Sahai LLC.
