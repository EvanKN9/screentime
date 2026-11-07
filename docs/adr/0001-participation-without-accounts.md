# Represent participation independently from account access

Approved during discovery on 2026-11-07: a group participant may exist without an account, while a member needs an approved account for private group access. Requiring every friend to sign up would prevent the planner and spreadsheet migration from representing the actual group when adoption is incomplete; owners/admins instead confirm links to existing participants so later signup preserves attribution and rotation state. This accepts the extra work of managing and matching participants without accounts; it establishes domain concepts, not a choice of tables, identifiers, or authentication architecture.

See [D02 and D03 in the discovery decisions](../DISCOVERY_DECISIONS.md) and the [glossary](../../GLOSSARY.md). Account deletion remains subject to the provisional policy and technical/privacy review in D13.
