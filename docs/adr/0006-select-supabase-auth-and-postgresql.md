---
status: accepted
date: 2026-11-10
---

# Select Supabase Auth and Supabase PostgreSQL with React and FastAPI

The project owner selected Supabase Auth and Supabase PostgreSQL for ScreenTime, retaining React as the frontend and FastAPI as the application backend. This establishes the platform foundation for the first working vertical slice toward the December 31, 2026 checkpoint, with a preference for free-tier or open-source authentication capabilities rather than a recurring authentication subscription. It preserves the complete approved v1 scope and records, rather than resolves, the compatibility conflict with the approved sign-in method linking rule.

## Consequences and unresolved conflict

- Supabase is the selected authentication and PostgreSQL platform. Application authorization remains in FastAPI; authentication alone does not grant membership, group permissions, or access to private application data.
- [Supabase documents automatic linking of identities with matching emails](https://supabase.com/docs/guides/auth/auth-identity-linking#automatic-linking). FR-001.AC4–AC7 and ADR 0004 instead require authentication to the existing account before connecting Google. The platform choice does not supersede those requirements.
- R-007 records this as a blocking policy conflict before implementing or enabling an affected Google/password authentication path. The conflict includes automatic linking during Google sign-in; merely hiding a linking button or enabling manual linking is not a resolution. A policy change requires explicit project-owner approval.
- The approved recovery flow and invalidation of every application session under ADR 0005 remain requirements. Supabase configuration and FastAPI integration must enforce those outcomes, rather than assuming JWT signature validation alone establishes an active application session.
- Database exposure and access controls, the application schema and QR-002 compatibility review, session enforcement, recovery integration, and remaining security policies still require the relevant planning and approval. This ADR does not select their implementation details.
- A separately scoped first slice may proceed through implementation specifications without resolving every later December-release decision. That does not complete the Google/linking requirements, waive affected policy gates, reduce full v1 scope, or authorize application code or ticket publication.

See the [project context](../PROJECT_CONTEXT.md), [PRD R-007](../PRD.md#authentication-policy-questions-r-007), [ADR 0004](0004-link-google-to-existing-password-account.md), and [ADR 0005](0005-password-recovery-and-session-invalidation.md).
