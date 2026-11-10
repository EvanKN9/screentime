---
status: accepted
date: 2026-11-09
---

# Support Google sign-in and email/password registration and login

Discovery D02 originally restricted v1 to Google sign-in and excluded separate passwords and password recovery. On 2026-11-09, the project owner approved Google sign-in plus email/password registration and login, superseding that original restriction so people can use email/password access while retaining Google as a convenience. The decision accepts additional authentication, recovery, and security design and verification work; it does not choose their policies or technical implementation.

## Consequences

- FR-001 retains its identifier and now covers both approved sign-in methods. The original D02 statement remains explicitly marked as superseded history; unrelated product requirements and existing ADRs remain unchanged.
- **Sign-in method linking** associates multiple sign-in methods with one ScreenTime account. An **account link** associates an account with an existing group participant under FR-006 and ADR 0001. Supporting both sign-in methods does not approve a linking workflow or change participant-linking permissions.
- Password-recovery availability and behavior, method linking/unlinking, proof of control, matching-email conflicts, duplicate-account handling, email verification and changes, and security-related behavior require the targeted review in PRD R-007 before affected implementation. Recovery is not automatically included or excluded.
- Authentication email requirements depend on the unresolved policies and remain separate from deferred movie-night and group-activity notifications. Username login, automatic method linking, security thresholds, authentication tooling, credential storage design, and schema are not selected by this decision.

See [D02 and its dated amendment](../DISCOVERY_DECISIONS.md#d02-accounts-participants-and-account-links), [FR-001](../PRD.md#fr-001--google-sign-in-and-emailpassword-registration-and-login), [R-007](../PRD.md#authentication-policy-questions-r-007), and [ADR 0001](0001-participation-without-accounts.md).
