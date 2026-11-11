# ScreenTime — Project Context

## Project overview

ScreenTime is a social movie watch-party planner for private groups of friends. Its first release will replace the group's spreadsheet for scheduling, picker rotation, shared movie suggestions, and viewing history. It is both a portfolio project and an application for actual use by the friend group.

The long-term vision is a broader social movie platform, with personalized group recommendations as a high-priority post-MVP feature.

## Current problem

The existing group uses a Google Sheet for movie-night schedules, picker assignments and counts, a shared watchlist, interest votes, and viewing/attendance history. It currently meets remotely every Thursday at 8 PM Pacific local time, following seasonal clock changes. In-person nights are a future use case.

The spreadsheet requires manual maintenance. ScreenTime must bring its existing data across rather than require the group to start with empty history.

## Approved discovery baseline

Product discovery concluded and was approved on **2026-11-07**, including the project owner's final clarifications.

- [Approved discovery decisions](DISCOVERY_DECISIONS.md) contain the full v1 product baseline and approval boundaries.
- [Delivery milestones](MILESTONES.md) organize that full scope into independently testable increments.
- [Shared vocabulary](../GLOSSARY.md) defines domain terminology.
- [Domain decision records](adr/) explain consequential approved trade-offs.

These are approved discovery records that inform the approved ScreenTime v1 PRD (PRD.md). React, FastAPI, Supabase Auth, and Supabase PostgreSQL are selected technical foundations; remaining architecture and policy gates still need review. Preserve the entire agreed MVP as the v1 target. An earlier milestone is an intermediate deliverable; moving an approved requirement out of v1 requires the project owner's approval.

On **2026-11-09**, the project owner approved Google sign-in plus email/password registration and login for v1, superseding the original Google-only discovery requirement. See [ADR 0003](adr/0003-support-google-and-email-password-sign-in.md) and FR-001 in the PRD.

The project owner also approved the limited password-account-to-Google sign-in method linking rule on **2026-11-09**. See [ADR 0004](adr/0004-link-google-to-existing-password-account.md) and FR-001.AC4–AC7; other authentication policies remain open under PRD R-007.

On **2026-11-10**, the project owner approved the password-recovery flow and invalidation of all application sessions after a successful reset. See [ADR 0005](adr/0005-password-recovery-and-session-invalidation.md) and FR-001.AC8–AC11.

On **2026-11-10**, the project owner selected Supabase Auth and Supabase PostgreSQL, retaining React as the frontend and FastAPI as the application backend. See [ADR 0006](adr/0006-select-supabase-auth-and-postgresql.md). This selection does not approve Supabase's automatic same-email identity linking or supersede the product requirements in ADRs 0004 and 0005.

## Established product decisions

### Accounts, participants, and private groups

V1 supports both Google sign-in and email/password registration and login. A participant may exist without an account; an approved member has account access to a private group. Owners/admins manage participants without accounts and explicitly confirm account links when those people join.

Sign-in method linking means associating multiple sign-in methods with one ScreenTime account. It is separate from an account link to an existing group participant. When Google sign-in uses the same email as an existing password account, matching emails alone do not connect the methods: the person must authenticate with Google and to the existing ScreenTime account before Google is connected. After both checks succeed, either method signs into that same account with its existing memberships and history. If the person cannot authenticate to the existing account, that Google sign-in attempt stops without adding a link or creating another account.

Password recovery sends a code to the email address already verified on the account. A valid code permits choosing a new password. A successful reset invalidates every existing ScreenTime application session, including the current browser, while leaving the recovery confirmation screen visible with an option to sign in normally. Recovery does not automatically sign the person in; subsequent email/password login uses the new password.

**Unresolved platform-policy conflict:** Supabase Auth automatically links identities with matching emails, while FR-001.AC4–AC7 require authentication to the existing account before connecting Google. Resolve this conflict before implementing or enabling an affected Google/password authentication path; hiding a manual linking button is not a resolution. Supabase selection does not waive the existing requirement or authorize a policy change. This gate need not block an independently scoped email/password implementation slice that does not enable Google.

Remaining recovery security details, unlinking, Google-first accounts later adding passwords, different-email linking, pre-existing duplicate accounts, email-verification timing, session enforcement, and other security-related behavior remain subject to project-owner approval under PRD R-007. Supabase is selected; its integration and configuration must still satisfy the approved linking and recovery outcomes.

Any signed-in user can create a group and belong to multiple groups. Members can share invite links, but owners/admins approve access. Only the owner appoints/removes admins, transfers ownership, and deletes the group. Ownership can transfer only to an approved account holder.

### Calendar and attendance

Groups control their own meeting dates and times. V1 includes individual events and recurring series on a chosen weekday every week or every few weeks, with changes to one event or that event and future events. Each group has a scheduling time zone; viewers see times converted to their current local time zone.

The responsive website includes a month view and upcoming-events list. Start time is required; end time and meeting details are optional. RSVPs distinguish Going, Maybe, Not going, and No response. Event editors can record RSVPs on participants' behalf and optionally record actual full or partial attendance.

### Movies, picker rotation, and history

Each event supports one movie, selected through catalog search or manual entry. Events can be scheduled before choosing a movie or picker. The picker has complete freedom to choose any movie; watchlists, interest votes, and future recommendations are suggestions.

Each group has one picker rotation. Assignment reserves a turn; confirmed completion consumes it. Cancellation releases the reservation. Lifetime picker totals come from completed nights with picker credit and are distinct from current-round eligibility. Manual assignments, attendance overrides, rotation exclusions, and manager corrections preserve the group's flexibility. Automatic draws manage one active round at a time.

Event editors explicitly confirm completion. A completed night can have no picker credit. Group history preserves attribution when someone leaves or is removed.

### Shared watchlist

Members can add suggestions, remove their own suggestions, and express interest, with one vote per participant per movie. Owners/admins can remove any entry and record suggestions and votes for participants **without accounts**. Proxy watchlist contributions for participants with accounts were not approved.

A completed movie leaves the active group watchlist and can be re-added for a rewatch.

### Migration and account deletion

V1 includes a one-time migration of the existing group's spreadsheet, with owner review of corrections, movie matches, participant mappings, and starting rotation. ScreenTime then becomes the main record. The source workbook remains unchanged.

Account deletion is in v1. Its provisionally accepted outcome is to revoke active participation and anonymize personal history after owned groups have been transferred or deleted. Exact data-handling semantics require technical and privacy review before implementation; see the review items in the approved discovery decisions. This review does not defer account deletion out of v1.

## High-priority post-MVP recommendations

Personalized group recommendations remain a high-priority follow-up. Desired signals include predicted group enjoyment, movies members have not watched, overlap between personal watchlists, and the current picker's preferences. Algorithms and weighting remain undecided.

Initial data-model planning must demonstrate that v1 participant/account relationships, movie identities, group history, attendance, suggestions, and interest records can accommodate later personalization. Personal watchlists, personal viewing logs, and ratings will supply additional signals after MVP. This is a compatibility constraint for technical review, not approval of a schema, recommendation architecture, or extra v1 features.

Other approved deferrals include automated reminders and email/push notifications about movie-night and group activity, external calendar integration, native mobile apps, advanced calendar views and drag-and-drop scheduling, ongoing spreadsheet synchronization, and a general-purpose importer. Letterboxd integration remains a future goal subject to feasibility. Recovery-code email delivery is required by FR-001.AC8; other authentication email requirements depend on the remaining policies in PRD R-007. Authentication emails are separate from these product-notification deferrals.

## Selected technical foundations and remaining choices

- Frontend: React
- Backend: Python / FastAPI
- Authentication: Supabase Auth
- Database: Supabase PostgreSQL
- Movie metadata: Potentially TMDB
- Version control: Git / GitHub
- Development assistance: Codex and GitHub Copilot

React, FastAPI, Supabase Auth, and Supabase PostgreSQL are selected by the project owner. Application authorization remains FastAPI's responsibility; selecting Supabase does not grant authenticated users access to private groups or move business permissions to the frontend. Database exposure and access controls, session enforcement, application schema, metadata provider, frontend/backend hosting, and remaining security policies still require the relevant technical planning and approval. Initial authentication must use free-tier or open-source capabilities without a recurring authentication subscription.

## Development philosophy and delivery

Plan around **10 hours per week**. The approved **December 31, 2026 intermediate checkpoint** demonstrates authentication, private group creation, adding participants without accounts, an individual movie-night event, manual picker assignment, catalog/manual movie recording, and completion/history with picker credit. The full v1 timeline remains flexible; this checkpoint does not replace any approved v1 requirement or milestone.

Limit remaining architecture planning to **2–3 focused sessions, at most four hours**, prioritizing decisions that block the first implementation slice. Classify decisions as blocking before the affected implementation, deferrable to implementation, or post-release. Recommend established tools and reasonable defaults for minor details; explore additional scenarios only when they materially affect security, data integrity, or the first release. Initial model approval still requires the QR-002 recommendation-compatibility review, without designing a recommender.

Implementation specifications may be drafted once the first slice is sufficiently defined, even if later December-release decisions remain open. Preserve the unresolved gates before implementing affected behavior. After the slice's blockers are resolved, recommend moving to specifications and tickets rather than continuing broad architecture exploration. Application code and publication of implementation tickets still require explicit project-owner approval.

The project serves two purposes: build something useful for real people and develop practical engineering skills through AI-assisted work.

- **Learning:** I implement important fundamentals myself with AI guidance.
- **Collaborate:** I work alongside AI agents on moderately complex features.
- **Delegate:** AI agents implement well-defined tasks that I can review and verify.

Prioritize maintainability, testability, clear architecture, and practical learning.

## Current project status

Discovery and the ScreenTime v1 PRD were approved on 2026-11-07, with authentication scope and limited sign-in method linking approved on 2026-11-09, and password recovery, session invalidation, and Supabase platform selection approved on 2026-11-10. The December checkpoint and architecture-planning timebox are approved. Remaining architecture is scoped to the initial slice, and application implementation has not begun. The remaining PRD policy gates, including Supabase's linking conflict under R-007, remain in force.

The next planning step is to define the first implementation slice using the selected foundations and approved requirements, close only its blocking decisions, and move to implementation specifications. Obtain approval before changing established product requirements, publishing implementation tickets, or implementing application code.
