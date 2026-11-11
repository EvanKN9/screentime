# First vertical slice: sign in, create, and retrieve a private group

**Status:** Approved specification by the project owner on 2026-11-10; not authorization to implement or publish tickets.
**Date:** 2026-11-10.
**Approval boundary:** The project owner approved this specification, including its API contracts, acceptance criteria, database integrity requirements, test seams, and learning/delegation strategy. Supabase session-validation and recovery-session restrictions remain a mandatory feasibility gate before protected endpoint implementation, not a claim of verified provider capability. Explicitly unresolved security policies remain open. This approval does not authorize application code or issue publication.

## Problem Statement

A group organizer needs to sign in, create a private ScreenTime group, and find that same group after reloading. Their group must remain inaccessible to another signed-in person. This establishes a small working path through authentication, application authorization, and persistent storage before adding movie-night features.

## Solution

Use React for the interface, Supabase Auth for email/password sign-in, FastAPI for all application requests and permissions, and Supabase PostgreSQL for group persistence. A signed-in creator becomes the group's owner in the same transaction that creates the group. The interface retrieves saved data from FastAPI after reloading rather than relying on browser state.

Existing email/password test accounts are approved for this first development slice. Self-service registration, password recovery, and Google sign-in remain required follow-up work and must not be marked complete. Google must remain disabled in the Supabase project, not merely hidden in the interface, until its automatic-linking conflict is resolved. This is partial delivery of authentication and M1, not acceptance of FR-001 or M1 as complete. Registration, Google, and recovery remain approved v1 requirements.

### Approved sources and traceability

| Source | Application to this slice |
| --- | --- |
| [PRD FR-001](../PRD.md#fr-001--google-sign-in-and-emailpassword-registration-and-login), AC2–AC3 | Email/password login portion only; authentication does not confer another group's access. Registration is not completed here. |
| [PRD FR-002](../PRD.md#fr-002--create-and-belong-to-multiple-groups), AC1–AC3 | Creator ownership, multiple groups per account, isolated group retrieval. |
| [PRD FR-008](../PRD.md#fr-008--private-information-and-action-boundaries), AC1–AC3 | Server-enforced membership and private-information boundaries; this slice exposes only group summaries. Other private features remain unimplemented. |
| [PRD QR-001 and QR-002](../PRD.md#6-cross-milestone-product-constraints) | Responsive interface and documented initial-model compatibility review; no new device or service-level commitments. |
| [ADR 0001](../adr/0001-participation-without-accounts.md), [glossary](../../GLOSSARY.md) | Account access and participation remain distinct. No implicit linking to existing participants. |
| [ADR 0003](../adr/0003-support-google-and-email-password-sign-in.md), [ADR 0004](../adr/0004-link-google-to-existing-password-account.md) | Both methods remain in v1; matching-email linking policy is preserved. |
| [ADR 0005](../adr/0005-password-recovery-and-session-invalidation.md) | Recovery is follow-up work; protected endpoints must not assume an unexpired JWT always represents an active application session. |
| [ADR 0006](../adr/0006-select-supabase-auth-and-postgresql.md) | Selected platform and FastAPI authorization responsibility; linking conflict remains a gate. |
| [PRD section 11](../PRD.md#11-unresolved-policies-risks-and-approval-needs), [project context](../PROJECT_CONTEXT.md) | Preserve policy approvals, December checkpoint, timebox, and learning ownership. |

## User Stories

1. As an account holder, I want to sign in using email and password, so that I can use account-based features.
2. As an account holder, I want failed sign-in to leave private features unavailable, so that incorrect credentials do not grant access.
3. As a signed-in organizer, I want to name and create a private group, so that my friends' future planning has a home.
4. As a group creator, I want to become its owner automatically, so that ownership is established without a separate permission request.
5. As a group owner, I want to reload and retrieve the saved group, so that my work survives browser state changes.
6. As a signed-in organizer, I want to create and select multiple groups, so that separate groups remain independent.
7. As a group owner, I want other accounts excluded from my private group, so that knowing its identifier does not reveal its information.
8. As an unauthenticated visitor, I want a sign-in prompt instead of private content, so that access has a clear boundary.
9. As a signed-in user, I want clear loading and failure states, so that a network error is not mistaken for successful persistence.
10. As the developer, I want observable authorization and persistence tests, so that I can understand and verify the boundary I build.

## Implementation Decisions

The decisions in this section are approved for this slice, subject to the explicit feasibility and unresolved-policy gates below. Descriptions of proposed defaults do not resolve policies explicitly left open.

### Authentication and group authorization

- React uses the maintained Supabase JavaScript client for password sign-in and session refresh. Passwords are submitted to Supabase Auth, never stored or hashed by ScreenTime application code. FastAPI receives access tokens, not passwords or refresh tokens.
- Use HTTPS when deployed. React sends the access token as a bearer token to FastAPI. Proposed default: SDK-managed browser session persistence so reload can restore sign-in. Its exposure to malicious browser scripts must be accepted during security review; avoid unsafe HTML rendering and token-bearing logs. No custom cookie/session system in this slice.
- FastAPI verifies the signature using the project's supported signing-key mechanism and an established JWT library, with fixed allowed algorithms, expected issuer/audience, expiry, and required subject/session claims. Never trust a decoded but unverified payload or browser-supplied account identifier.
- On each protected request, verify that the token's session belongs to its subject and still exists in Supabase's session store, through a narrowly privileged server-only lookup. Fail closed if verification or its dependency fails. Do not cache positive session results across requests in this slice. Supabase documents correlating `session_id` with `auth.sessions` to reject signed-out tokens; this is additional to JWT validation. [Official session guidance](https://supabase.com/docs/guides/auth/sessions).
- Accept ordinary password-authenticated sessions and their legitimate refreshes. Reject recovery-only sessions for application access; a JWT with a valid signature is insufficient proof of ordinary sign-in. Implement and test this distinction against actual Supabase-issued claims, including refreshed sessions, before enabling the slice. Recovery implementation and all-session reset revocation remain separate delivery work; this guard alone does not complete ADR 0005.
- After authentication, FastAPI resolves an application account by the immutable Supabase user ID. It checks database membership for each requested group. Never derive group roles from email, frontend state, a group identifier, or a participant record. Never accept ownership or membership assignments from request bodies.
- Read authorization is an approved membership in that group. Initially the only creation workflow establishes owner membership; invitations/admissions are absent. Test fixtures can represent another account's membership without implementing admission UI.
- Application tables live in a non-exposed schema. Disable the unused Supabase Data API and do not grant browser roles application-table access. FastAPI uses a dedicated least-privilege SQL role; migrations use separate credentials. Keep any session lookup privileges narrowly scoped and separate from ordinary application-data privileges. Do not give the application unrestricted Auth-table access or distribute database/service credentials to the browser. [Official Data API security guidance](https://supabase.com/docs/guides/api/securing-your-api).

### Minimal entities and invariants

| Entity | Minimal data and constraints |
| --- | --- |
| Supabase Auth user/session (managed) | Provider-owned identity, email, credentials, verification, and session data; no application-owned password table. |
| Application account | UUID equal to verified Supabase subject; creation timestamp. Unique identity, not keyed by email. No copied email needed for this slice; Supabase PostgreSQL already holds the managed account email. This does not decide future profile synchronization or deletion semantics. |
| Group | Generated UUID, name, creation timestamp. Names need not be globally unique. |
| Group membership | Group/account foreign keys and group role; unique group/account pair. Creation inserts the creator's owner membership. Exactly one owner per created group, with ownership represented by membership rather than a conflicting second owner field. |

Use a database transaction for application-account creation if needed, group creation, and owner membership. A failure rolls back the operation without an ownerless group; concurrent first requests cannot duplicate the account. Database constraints enforce identity, foreign-key, membership uniqueness, and ownership invariants. No cascade choice should predetermine unresolved account-deletion behavior.

No participant entity is needed to authorize or retrieve a group in this slice. Do not treat membership as participation or automatically create/link a participant. A later participant can exist without an account and have a separately confirmed account association. Participant management is the next checkpoint capability, not an accidental dependency of group creation.

**Approved slice validation:** trim surrounding whitespace, require a nonempty group name, and cap it at 100 Unicode characters consistently in UI, API, and database validation. This is a slice implementation constraint, not a pre-existing PRD requirement. Do not impose a one-group-per-account restriction.

### API contracts

All routes below are authenticated FastAPI application endpoints. JSON errors have a stable code and safe message without tokens, SQL details, or private group data.

| Request | Contract |
| --- | --- |
| POST /groups | Body contains only `name`. Return 201 after commit with `id`, normalized `name`, `created_at` (UTC timestamp), and `my_role` = owner. Ignore no security-sensitive fields: reject unknown ownership/account/role fields with 422. |
| GET /groups | Return 200 with an `items` array of group summaries (`id`, `name`, `created_at`, `my_role`) for this account's approved memberships only. Empty array for no memberships. Deterministic creation-time/ID ordering; no pagination requirement for this initial slice. |
| GET /groups/{group_id} | Return 200 with the same summary only after membership authorization. A valid UUID for a nonexistent or inaccessible group returns the same generic 404 without confirming existence. Malformed UUID returns 422 without a group lookup. |

- Missing, invalid, expired, revoked, or recovery-only authentication returns 401 and no private data or writes.
- Valid authentication with no membership receives the 404 above on detail retrieval; lists never reveal other groups. CORS is not an authorization control.
- Invalid body/name returns 422 without partial writes. Dependency failure returns a safe 503 without failing open. Unexpected failures return a safe 500.
- No member roster, email addresses, participant details, admin tooling, or mutation beyond creation is exposed. Creation time and ID remain stable on reads.
- A repeated POST is a new creation, not an idempotent request. Disable duplicate submission while pending. On an ambiguous network failure, refresh the group list before inviting a retry; do not automatically repeat a creation request. An idempotency subsystem is outside this slice.

### Frontend interactions

1. Display email/password sign-in for an existing account; show generic credential failure without private data. Do not add Google, signup, recovery, or participant-linking workflows to this slice.
2. Restore the SDK session on load before requesting protected data. On failed/expired authentication, clear private screen state and offer sign-in; never display another session's cached group content.
3. Show the authorized group list and a create-group form with name validation, pending state, and safe errors.
4. After a committed creation, show the returned group and owner role. The group has a directly reloadable URL whose identifier is used to retrieve it from FastAPI.
5. On reload, retrieve persisted data from the backend. Render a generic unavailable view for a 404; render no protected fields before authorization succeeds.
6. Render group names as text. Clear private query state when the authenticated subject changes or authentication is lost. Provide usable phone and desktop layouts without inventing new conformance targets.

### Initial-model compatibility review (QR-002 draft evidence)

- Immutable account IDs plus separate group memberships preserve account access without using email as identity. Future participant records can remain group-scoped, exist without accounts, and gain explicitly confirmed account links without replacing historical participant identifiers.
- Future movie records can have stable application IDs with optional catalog references, preserving manually entered movies when catalog matches are approved. No movie tables are introduced now; merge semantics remain R-005 decisions.
- Future group history, attendance, suggestions, interest, and picker credit can refer to stable group/participant/movie IDs rather than current membership rows or names. Access revocation need not erase attribution. Exact lifecycle semantics remain R-001/R-002 gates.
- Later personal watchlists, watched status, ratings, and preferences can attach to account/movie identities while group activity preserves its original participant attribution. This allows future signals without implementing personal features or selecting a recommendation algorithm.
- The first schema neither equates accounts with participants nor encodes email as a permanent cross-feature identifier. Review this compatibility argument before approving the initial model; it is proposed evidence for QR-002, not a claim that its approval gate is already passed.

## Testing Decisions

**Approved test seams:** primarily the FastAPI HTTP boundary against isolated real PostgreSQL, plus one browser smoke flow covering React, real Supabase Auth, FastAPI, and persistence. This is the highest practical boundary for exhaustive authorization checks without making every negative case a slow browser test. The repository currently contains no application or test harness to reuse.

- Recommend pytest with an ASGI HTTP client for API integration tests and Playwright for the smoke test. Test observable responses and persisted outcomes, not internal helper calls, ORM structure, component implementation, or SDK internals.
- Use real database transactions/constraints and real application routes. Controlled identity/session fixtures may represent expiry, bad signatures, recovery claims, and revocation for deterministic tests; do not mock the membership query or replace PostgreSQL with an in-memory database.
- Supplement fixtures with real Supabase-issued password and refreshed tokens in a disposable integration environment. Verify real session revocation rejects an otherwise unexpired token and real recovery-session claims cannot enter application endpoints. Do not call the authentication guard verified solely because mocked claims pass.
- Use at least two accounts and disjoint groups; include an account with multiple groups. Keep test credentials outside source control and tests isolated from personal/production data.
- Verify database exposure separately using anonymous and authenticated browser credentials against the Data API; API tests alone cannot demonstrate that bypass paths are closed.

### Testable acceptance criteria

| ID | Observable passing result |
| --- | --- |
| S1 | An existing email/password account can sign in. Incorrect credentials produce no application access. |
| S2 | Authenticated creation returns 201, persists the normalized group, and grants the verified creator owner membership atomically. Spoofed identity/role fields are rejected and cannot appoint another owner. |
| S3 | Reloading the group URL retrieves the same ID/name/time/owner role from PostgreSQL through FastAPI, including after a backend restart; no browser-only mock data passes this test. |
| S4 | One account can create two groups and retrieve both through its list and detail routes. Another account's list contains neither group. |
| S5 | A second signed-in account requesting the first account's group ID receives the same generic 404 as for a missing valid UUID, with no name, owner identity, or other private content. Membership in its own group does not change this outcome. |
| S6 | All three routes reject missing, malformed, wrongly signed, wrong-issuer/audience, expired, and revoked tokens with 401; rejected POSTs create no rows. A valid real password token and legitimate refresh succeed. |
| S7 | Recovery-only tokens, including tested refreshed recovery sessions, cannot list, read, or create groups. Session-verification outages return safe failure and never authorize access. |
| S8 | Losing group membership in a test fixture prevents subsequent detail retrieval and removes it from subsequent lists, even while the authentication session stays valid. No removal endpoint or departure policy is implemented by this test. |
| S9 | Empty/whitespace/over-limit names and unknown security-sensitive fields return 422 without a group. Valid duplicate names across groups are allowed. A forced membership-insert failure leaves no group or orphan creation state. |
| S10 | Anonymous and authenticated browser credentials cannot read or write application tables through Supabase's Data API. Frontend assets and logs expose no privileged keys, passwords, refresh tokens, or database credentials. |
| S11 | The browser smoke flow signs in, creates a group, reloads, and sees it. A separate account/browser cannot reveal it via a direct URL. Authentication loss clears private screen state; failures do not display success. |
| S12 | Source traceability, unresolved gates, and the QR-002 compatibility review are reviewed; no test result is reported as completion of all authentication, M1, full v1, or the December checkpoint. |

## Out of Scope

- Google sign-in and advanced sign-in method linking until the ADR 0004/0006 conflict is explicitly resolved; no implicit policy amendment.
- Self-service registration and password recovery UI/orchestration, including reset-driven global session invalidation. These remain required follow-up work, not removed from v1. Authentication guards in this slice must accommodate the approved outcomes.
- Invitations, admission requests, admin appointment, participant creation, participant account links, owner transfer, group editing/deletion, and account deletion. No direct SQL fixture becomes a product admission workflow.
- Events, recurrence, attendance, manual/automatic picker assignment, rotation, catalog integration, movie recording, history, recommendations, migration, and unrelated v1 capabilities.
- Infrastructure automation, performance targets, extensive design-system work, and implementation tickets or application code without separate explicit authorization.

## Further Notes

### Dependencies, assumptions, and approval gates

| Timing | Item |
| --- | --- |
| Specification approval — completed 2026-11-10 | Owner approved the existing-account-only boundary, schema/contracts, validation limit, test seams, acceptance criteria, integrity requirements, and learning strategy, subject to the gates retained here. Explicitly unresolved policies are not approved by this status change. |
| Before protected endpoint implementation — blocking | Verify the proposed session-validation and recovery-session restrictions using supported Supabase APIs/access mechanisms and actual Supabase-issued tokens. Record official support references and observed results for ordinary password sign-in, legitimate refresh, revoked sessions with unexpired tokens, and recovery-only sessions including refresh. Confirm signing configuration, narrowly privileged session lookup, and fail-closed behavior. Do not assume an SDK method, Auth-table access pattern, or token claim provides guarantees that have not been verified. If supported behavior cannot enforce these outcomes, stop the affected endpoint work and return the conflict for owner review; do not invent a custom security mechanism or silently weaken approved policies. |
| Before model approval | Review the QR-002 compatibility evidence and account/participant separation. Do not select deletion cascades that resolve R-001 implicitly. |
| Before real-account testing | Provision a development Supabase environment with Google and unused authentication methods disabled and verified email/password test accounts through supported administrative tooling. Do not manually insert password hashes or require participants to receive project-admin access. |
| Before accepting authentication configuration | Review R-007 as a small configuration bundle: recommended email confirmation enabled; SDK browser storage/refresh; provider password/rate-limit settings recorded as configured; JWT expiry and session/logout behavior. These are proposed defaults, not approved numerical thresholds or completed policies. No paid session feature is required by this draft. |
| Before external deployment/testing | Select free-tier hosting, explicit allowed frontend origins and redirect URLs, HTTPS, server secret handling, database connectivity/migrations, and any required authentication email delivery. SMTP is not needed merely to sign in with already provisioned verified test accounts; it is needed for applicable verification/recovery delivery. |
| Before later affected work | R-007 linking conflict, registration verification UX, recovery security/enforcement, unlinking and other auth policies remain open. R-001–R-005 retain their existing scope and gates. |

Recommend SQLAlchemy with Alembic for application persistence/migrations and maintained JWT tooling with JWKS support; exact package versions, module layout, loading copy, and ordinary form styling can be settled during implementation within this contract. No custom password hashing, cryptography, or auth provider is needed. Provider defaults must be inspected and recorded, not assumed to satisfy unresolved policies automatically.

### Learning, collaboration, and delegation

- **Evan implements:** the group creation and retrieval/list FastAPI endpoints, membership authorization query, transaction boundaries, initial SQL schema/migration and constraints. Evan explains how a verified subject becomes an owner and why another account cannot retrieve the group before considering those tasks complete.
- **Collaborate:** walk through the authentication dependency, JWT/session/recovery checks, database privileges, model review, and negative integration tests. Use `/teach` only when an unfamiliar concept blocks understanding, with learning files kept in the separate personal learning workspace.
- **Delegate after explicit implementation approval:** bounded scaffolding, routine frontend states, test fixture setup, documentation, and security/code review. AI should not pre-implement Evan's endpoints or database fundamentals. Evan reviews delegated results against the acceptance criteria.
- Keep a reviewable first implementation increment rather than building all foundations at once. No estimate here changes the roughly 10-hour weekly budget or the approved seven-capability December checkpoint.

### Review and transition

The project owner approved this specification on 2026-11-10 with the existing-test-account scope and mandatory Supabase feasibility verification clarified above. Broad architecture planning for this slice can conclude; it is ready for `/to-tickets` backlog planning. The backlog must place supported session/recovery verification before any protected endpoint implementation and preserve Evan's ownership of the endpoints and database fundamentals. Specification approval does not mean that verification has passed. Publishing issues or starting application implementation requires separate explicit authorization. Later December-release decisions can be handled before their affected slices rather than delaying backlog planning.
