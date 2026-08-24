# Changelog

All notable changes to the public MSA taxonomy are recorded here.

Version numbers track the internal knowledge repository this release is drawn
from, so that a published version and an internal one always mean the same
content.

## 0.2.0 — first public release

The taxonomy is published for the first time. Contents: 11 mechanisms, 37
signals, 11 archetypes, 13 attributes, 3 sources. 75 entities in total.

Coverage was expanded in this version to match where older adults actually lose
money, using IC3 2025 loss data rather than how often a scam type is reported.
Seven archetype families were added on that basis:

| Family | Why it was added |
|---|---|
| `arch.investment_grooming` | Investment and crypto fraud, the single largest older-adult loss category in 2025 at $3.52B |
| `arch.phantom_hacker` | Multi-stage impersonation chains, $1B+ drained since 2024 |
| `arch.crypto_atm_direction` | $333–389M in 2025 crypto-ATM losses, 76% from victims aged 60+ |
| `arch.tech_support_popup` | $1.04B loss category |
| `arch.medicare_enrollment` | Open-enrollment-season targeting |
| `arch.bereavement_targeting` | Obituary-mined targeting of newly bereaved older adults |
| `arch.contractor_redflag` | Door-to-door contractor fraud |

Sixteen signals and four attributes were added to support them.

Also in this release:

- `schema/id_subjects.yaml` is not published; the id-subject vocabulary it
  declares is visible in the ids themselves.
- The 8 `sig.detector.*` entities are published without their regular
  expressions, marked `pattern_published: false`.
- Provenance notes were rewritten for a public audience. Internal roadmap
  identifiers and references to the withheld verdict gate were removed. The
  source citations themselves are unchanged.

## Earlier

Version 0.1.0 was an internal seed release and was never published. It migrated
Sahai's hand-coded knowledge out of application code into this structure: the
9-attribute evidence matrix, institution legitimacy rules, and the original 11
mechanisms, 11 behavioral signals, and 4 archetypes.
