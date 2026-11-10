# ScreenTime v1 Product Requirements Document

**Document role:** Authoritative location for v1 product requirements and acceptance criteria.
**Review status:** Approved by the project owner on 2026-11-07 as the ScreenTime v1 product requirements baseline, with the Google and email/password authentication scope amendment approved on 2026-11-09. The unresolved policy gates in section 11 remain in force.
**Scope:** The complete agreed MVP is the v1 target. Intermediate milestones do not redefine or reduce that target.

## 1. Authority, sources, and approval boundaries

This PRD translates the following approved sources into requirements:

- [Project context](PROJECT_CONTEXT.md).
- [Discovery decisions D01–D16](DISCOVERY_DECISIONS.md).
- [Delivery milestones M1–M7](MILESTONES.md).
- [Domain glossary](../GLOSSARY.md).
- [ADR 0001: participation without accounts](adr/0001-participation-without-accounts.md).
- [ADR 0002: reservations and completed turns](adr/0002-reserve-turns-until-completion.md).
- [ADR 0003: Google and email/password sign-in](adr/0003-support-google-and-email-password-sign-in.md), recording the approved 2026-11-09 amendment to D02.

The discovery decisions remain the provenance for product policy, the glossary defines terminology, and the ADRs explain consequential domain trade-offs. The coverage matrix in section 12 connects every decision area and milestone to this specification.

No material contradiction was found between the sources. In particular, M4's manual coordination and M5's rotation automation are successive delivery stages; both belong to v1. Participant versus member, reservation versus picker credit, and proxy RSVP versus proxy watchlist permissions are intentional distinctions.

The approved 2026-11-09 amendment supersedes D02's original Google-only sign-in requirement. V1 requires Google sign-in and email/password registration and login. It does not select authentication tooling or resolve the policies in R-007. An **account link** associates an account with an existing group participant; **sign-in method linking** associates multiple sign-in methods with one ScreenTime account. Defining the latter does not approve a linking workflow or change FR-006's participant-linking rules.

Requirements have permanent identifiers. Future revisions must preserve existing identifiers rather than renumber or reuse them. Acceptance criteria are referenced as, for example, FR-001.AC1.

Unspecified policy is recorded in section 11 rather than silently selected. Resolving those items may require approved additions to acceptance criteria. Project-owner approval is required for product scope or policy changes. This document does not select implementation frameworks, storage structures, authentication tooling, metadata providers, or hosting, and does not authorize application implementation or technical architecture work.

## 2. Vision, users, and problems

### Product vision

Help private groups organize movie nights, distribute movie-picking opportunities fairly, share suggestions, and preserve what actually happened. The first release should replace the existing group's spreadsheet while working even when some friends never sign in. ScreenTime should also demonstrate a complete, usable product as a portfolio project.

The longer-term vision is a broader social movie platform. Personalized group recommendations are a high-priority post-MVP feature; v1 must preserve the ability to add them later.

### Target users and stakeholders

| User or stakeholder | Need |
| --- | --- |
| Group owner | Establish and maintain a private group, manage authority, represent friends without accounts, and move existing records into ScreenTime. |
| Group admin | Help with admission, participants, shared suggestions, event coordination, and rotation exceptions within delegated permissions. |
| Member | Join approved groups, schedule movie nights, RSVP, suggest movies, express interest, and view group history. |
| Participant without an account | Remain represented in planning, picker rotation, and attendance through authorized people without being required to sign up. |
| Picker | Choose any movie for their assigned night, using their account when they have one or communicating the choice to an event editor. |
| Project owner and portfolio audience | Evaluate a useful application with demonstrable workflows and traceable requirements. No separate public demo mode is implied. |

These roles overlap. Event editor is an event-specific permission relationship, not an additional group management role.

### Core problems

1. The spreadsheet needs manual maintenance across schedules, assignments, suggestions, attendance, and history.
2. Upcoming picker assignments and completed picker totals need distinct meanings, especially after cancellations.
3. Group membership and actual participation differ when friends do not sign in.
4. Real movie nights include absences, partial attendance, schedule changes, and informal exceptions.
5. Fixed scheduling would not serve groups with different routines or occasional events.
6. Starting with empty history would prevent a satisfactory replacement of the existing spreadsheet.

The current group meets remotely on Thursdays at 8 PM Pacific local time, following seasonal clock changes, and expects to add in-person nights. This is migration context, not a restriction on other groups.

## 3. Goals, evidence, and non-goals

### V1 goals

| Goal | Measurable evidence |
| --- | --- |
| G-01 Coordinate a complete movie night | The planning, RSVP, picker/movie selection, completion, and history flows pass their acceptance criteria on phones and desktops. |
| G-02 Support fair turns and agreed exceptions | A full regular round, cancellation, unavailable picker, manual exception, and round correction produce the outcomes specified in M5. |
| G-03 Work with incomplete signup | Participants without accounts appear in the actual group's planning and records without receiving private app access; later approved account links preserve their records. |
| G-04 Preserve existing information | Every record approved for migration is reconciled against the imported result, with approved corrections and no unexplained omissions or counter differences. |
| G-05 Replace the spreadsheet in actual use | The migrated group uses ScreenTime as its main record and completes the pilot checklist in FR-051. |
| G-06 Preserve the recommendation path | The compatibility review in QR-002 is completed during subsequent technical planning before the initial data model is approved. |

Development planning uses 10 hours per week and a flexible timeline. No release date, implementation estimate, service-level target, or fixed number of pilot nights has been agreed.

### Non-goals and post-MVP boundaries

| Feature or capability | Boundary |
| --- | --- |
| Personalized group recommendations | High-priority post-MVP; retain the compatibility requirement in QR-002. No recommendation algorithm or weighting is approved. |
| Personal watchlists, personal viewing logs, and ratings | Post-MVP. V1 history concerns completed group movie nights. |
| Letterboxd integration | Future possibility subject to feasibility; no v1 dependency or promised integration behavior. |
| Automated reminders and email/push notifications about movie-night and group activity | Post-MVP. Members check ScreenTime or share changes themselves, including pending membership requests. Authentication email requirements depend on the separate unresolved policies in R-007. |
| External calendar integration | Post-MVP. V1 scheduling operates inside ScreenTime. |
| Native mobile applications | Post-MVP; v1 is a responsive website. |
| Week/day calendar time grids and drag-and-drop scheduling | Post-MVP; v1 includes month and upcoming-events views plus event editing. |
| Monthly and more complex recurrence patterns | Post-MVP; v1 supports a selected weekday every week or every few weeks. |
| Ongoing spreadsheet synchronization and a general-purpose importer | Post-MVP; v1 includes the existing group's one-time migration. |
| Double features or multiple movies per event | Outside v1; each event supports one movie. |
| Automatic draws triggered by event dates | Outside v1; an event editor explicitly starts a draw. |
| A separate banning system | Outside v1; former members can request fresh admission. |

Watchlists and interest votes do not become binding movie-selection rules. The full set of approved v1 requirements remains required even when an earlier milestone is usable.

Email/password registration and login are required in v1 under FR-001. Password-recovery availability and behavior remain unresolved under R-007, rather than automatically included or excluded by the authentication scope amendment.

## 4. Permissions and business rules

### Permission matrix

All private-group actions require approved membership. Having a participant record, an invitation link, or an assigned picker role alone does not grant access. Event-creator permissions do not override this access boundary.

| Action | Authorized actor |
| --- | --- |
| Create a private group | Any signed-in user; the creator becomes its owner. |
| View private group information or share its invite link | A member of that group. |
| Approve membership and confirm an account link | Group owner or group admin. |
| Add/manage participants without accounts | Group owner or group admin. |
| Appoint/remove admins or remove an admin from the group | Group owner only. |
| Remove an ordinary member | Group owner or group admin. Admins cannot remove the owner or another admin. |
| Create an event or recurring series | Any member, without a scheduling approval workflow. |
| Edit/cancel an event or manage its picker assignment/draw | Event editors: its creator, the group owner, and group admins. |
| Record/change the event movie | Event editors or the assigned picker when that picker has approved account access. |
| Update their own RSVP | Any member. |
| Record/update another participant's RSVP | Event editors, including for participants with accounts. |
| Confirm completion or record actual attendance | Event editors. |
| Add their own suggestion, remove their own suggestion, or express their own interest | Any member. |
| Remove any shared watchlist entry | Group owner or group admin. |
| Record proxy suggestions/interest | Group owner or group admin, only for participants without accounts. |
| Exclude participants from rotation or correct current-round used/unused turns | Group owner or group admin. |
| Transfer ownership or permanently delete the group | Group owner only. Ownership recipients must already have approved account access to the group. |
| Request deletion of their own account | The account holder, after resolving every owned group; deletion semantics remain provisional under FR-043. |

### Business rules

| Rule | Meaning | Requirements |
| --- | --- | --- |
| BR-01 Private access | Approval is group-specific; a participant record or matching display name is insufficient. | FR-002–FR-008 |
| BR-02 Participant continuity | Linking an account preserves the existing participant's attribution and rotation state. | FR-006, FR-036, FR-046 |
| BR-03 Selection freedom | One movie per event; the picker may choose outside the watchlist, including a rewatch. | FR-009, FR-024, FR-028 |
| BR-04 Attendance meaning | RSVP is intended attendance; actual attendance is optional and separate. No response is not Not going. | FR-021–FR-022, FR-026 |
| BR-05 Turn lifecycle | Assignment reserves; confirmed credited completion consumes; cancellation releases an unused reserved turn. | FR-025, FR-032–FR-033 |
| BR-06 Credit and totals | A completed night can have no picker credit. Lifetime totals count credited completed nights, not assignments or manual eligibility corrections. | FR-025, FR-027, FR-038 |
| BR-07 Rotation scope | Each group has one rotation and one active automatic round across all its events. | FR-029, FR-035 |
| BR-08 Exceptions | Absences do not force an early reset. Manual assignments and manager corrections preserve flexibility. | FR-031, FR-034–FR-038 |
| BR-09 Interest meaning | One interest vote per participant per movie; an interest vote is not a rating or movie approval. | FR-012–FR-013 |
| BR-10 Lifecycle distinction | Departure/removal preserves named history; account deletion provisionally anonymizes it and revokes active participation. | FR-039–FR-043 |
| BR-11 Scheduling meaning | Group time zone anchors the schedule; each viewer sees their current local time. Series edits preserve past events. | FR-017, FR-020 |
| BR-12 Complete v1 | All seven milestones and applicable acceptance criteria are required; scope or policy changes need project-owner approval. | Section 9, section 11, QR-001–QR-002 |

## 5. Functional requirements by delivery milestone

Every FR below belongs to v1. Source references identify the corresponding approved discovery decisions. Acceptance criteria describe observable product outcomes rather than implementation choices. Approval-dependent edge cases are tracked in section 11 and must be resolved before the affected milestone receives final sign-off.

### M1. Private groups and participant access

**User story US-001:** As a group organizer, I want private access and an accurate roster even if some friends never sign in, so the planner can represent the actual group.

#### FR-001 — Google sign-in and email/password registration and login

**Source:** D02 as amended on 2026-11-09; ADR 0003.

- AC1: A person can sign in through Google to use account-based features.
- AC2: A person can register using an email address and password and log in using email and password to use account-based features.
- AC3: Signing in alone does not grant access to another person's private group; admission follows FR-004–FR-005.

Authentication policy questions remain subject to R-007 before the affected implementation. Neither this requirement nor FR-006 approves sign-in method linking or automatic matching of sign-in identities.

#### FR-002 — Create and belong to multiple groups

**Source:** D03–D04.

- AC1: A signed-in user can create a private group and becomes that group's owner.
- AC2: The same account can belong to multiple groups and select which group to use without creating another account.
- AC3: Membership in one group does not copy or grant access to another group's calendar, watchlist, history, or picker rotation.

#### FR-003 — Participants without accounts

**Source:** D02, D04; ADR 0001.

- AC1: An owner/admin can add and manage a participant without requiring that person to sign in.
- AC2: That participant can be represented in picker rotation and attendance through the relevant authorized workflows.
- AC3: A participant without an account receives no private app access; an ordinary member cannot use the manager-only roster-management capability.

#### FR-004 — Shareable invitations

**Source:** D03.

- AC1: Any member can share a group invitation link.
- AC2: A recipient can use the link to request membership through an account; following or forwarding it does not grant immediate admission.
- AC3: An account with an unapproved request remains unable to browse private group information.

#### FR-005 — Membership approval

**Source:** D03–D04.

- AC1: Owners/admins can inspect membership requests in ScreenTime and approve admission.
- AC2: An ordinary member cannot approve a request.
- AC3: A former member requesting to return needs fresh approval; their possession of an old link or previous approval is insufficient.

#### FR-006 — Explicit account links

**Source:** D02, D11; ADR 0001.

- AC1: Linking an approved account to an existing participant requires an owner/admin's explicit confirmation; matching display names alone do not create the link.
- AC2: Linking preserves the participant's existing history, suggestions, interest attribution, and current rotation state without creating a duplicate participant.
- AC3: Linking does not grant an additional unused turn or duplicate an existing interest vote.

#### FR-007 — Group management authority

**Source:** D04.

- AC1: Only the owner can grant or remove the group admin role.
- AC2: Owners/admins can remove ordinary members; admins cannot remove the owner or other admins, and only the owner can remove an admin.
- AC3: Admission and role-management actions in one group have no effect on the person's role or membership in another group.
- AC4: Creating an event, hosting a movie night, or being assigned as picker does not itself appoint or remove a group owner/admin; those are ongoing group roles.

#### FR-008 — Private information and action boundaries

**Source:** D02–D04.

- AC1: A nonmember cannot read the group's participant/member roster, calendar, shared watchlist, or history, including by opening a private feature's link directly.
- AC2: A person cannot perform a group action merely by having a participant record, invitation link, matching name, or membership in another group.
- AC3: Members can use only the actions authorized by the permission matrix; creator/picker relationships never bypass membership approval or later access revocation.

### M2. Movies and shared suggestions

**User story US-002:** As a member, I want to suggest identifiable movies and express interest so the picker has useful ideas without losing freedom of choice.

#### FR-009 — Catalog search and manual movie entry

**Source:** D08.

- AC1: A member can search a movie catalog and select a specific movie entry.
- AC2: When the desired movie is missing, manual title entry remains available for group movie tracking and suggestions.
- AC3: Both catalog and manual entries can be used in the shared watchlist and an event's movie selection; manual entry does not replace the required catalog-search feature.

#### FR-010 — Group suggestions

**Source:** D12.

- AC1: Any member can add their own movie suggestion to their group's shared watchlist.
- AC2: The suggestion is attributed to the relevant participant and remains within that group.
- AC3: Suggesting a movie does not assign it to an event or require a picker to select it.

#### FR-011 — Watchlist removal permissions

**Source:** D12.

- AC1: A member can remove a suggestion attributed to them.
- AC2: An ordinary member cannot remove another participant's suggestion.
- AC3: Owners/admins can remove any entry in their group's shared watchlist. Duplicate/co-contributor cases remain subject to R-005 rather than an invented authorship rule.

#### FR-012 — Interest votes

**Source:** D12.

- AC1: A member can express their own interest in a movie on the group's shared watchlist.
- AC2: Within a group's shared watchlist, a participant can contribute at most one interest vote to the same identified movie; repeating that contribution cannot increase their vote count above one.
- AC3: Interest is presented as a desire to watch, not a rating, binding selection decision, or approval requirement.

#### FR-013 — Proxy watchlist contributions

**Source:** D12, final clarification.

- AC1: An owner/admin can record a suggestion or interest vote for a participant without an account, attributed to that participant.
- AC2: An ordinary member cannot make these proxy contributions, and managers cannot use this capability for participants with accounts.
- AC3: Proxy and imported interest still obey one vote per participant per movie. After an account link, existing attribution is preserved and manager proxy eligibility no longer applies to that participant.

### M3. Flexible group calendars

**User story US-003:** As a member, I want to schedule individual nights or a recurring routine and see the correct local times, so plans work across groups, travel, and schedule exceptions.

#### FR-014 — Flexible event creation

**Source:** D05–D06.

- AC1: Any member can create events and recurring series without an owner/admin scheduling-approval step.
- AC2: Individual movie nights can use group-chosen dates and times; creation is not restricted to Thursday, 8 PM, or a fixed weekly routine.
- AC3: An event can be saved while its picker and movie are undecided.

#### FR-015 — Event time and meeting details

**Source:** D05.

- AC1: Creating an event requires a start date/time.
- AC2: The event can be saved without an end time; the app does not invent an end time from an undecided film.
- AC3: Meeting details are optional and can record a call link, address, or joining instructions for remote or in-person nights.

#### FR-016 — Weekly and multiweek recurring series

**Source:** D05.

- AC1: A member can schedule a series on a chosen weekday every week.
- AC2: The recurrence interval can instead be every few weeks; an every-other-week series repeats on the chosen weekday at that interval.
- AC3: Individual events remain available for arbitrary dates that do not fit the supported repeat patterns. V1 does not depend on monthly or more complex recurrence.

#### FR-017 — Scheduling and viewer time zones

**Source:** D05.

- AC1: Each group has a scheduling time zone that anchors the intended local date/time of its recurring schedule.
- AC2: A recurring night retains its intended local time in that zone across seasonal clock changes.
- AC3: Two viewers in different current local time zones see converted representations of the same event time; a viewer's changed current time zone changes their displayed time, not the group schedule.
- AC4: Converted calendar dates and times remain consistent when a viewer's local date differs from the group's date. Exceptional local-time policy is tracked in R-004.

#### FR-018 — Calendar views and rescheduling access

**Source:** D05.

- AC1: Members can view movie nights in a month calendar and an upcoming-events list.
- AC2: Both views identify the corresponding events and use the viewer-local time meaning in FR-017.
- AC3: An event editor can open an event for rescheduling through editing; a week/day time grid or drag-and-drop action is not required.

#### FR-019 — Event and series editing authority

**Source:** D06.

- AC1: An event's creator, the group owner, and group admins can edit/cancel that event; the same management principle applies to series.
- AC2: Another ordinary member cannot edit/cancel an event they did not create merely because they can view it.
- AC3: Being the assigned picker grants movie-choice authority under FR-024, not general scheduling/cancellation authority.

#### FR-020 — One-occurrence and future-series changes

**Source:** D05.

- AC1: An editor can choose to edit/cancel one occurrence without changing the rest of the series.
- AC2: An editor can instead change/cancel that occurrence and future occurrences, including moving the regular schedule or stopping the series.
- AC3: These series operations preserve past events.
- AC4: Once M5 is integrated, cancellation of an affected upcoming event applies the reservation-release rule in FR-033. The treatment of existing future exceptions and ambiguous local times requires the approvals in R-004.

### M4. Movie-night attendance and history

**User story US-004:** As an event editor, I want to record friends' plans and what actually happened, so the group's history and picker totals remain meaningful even when coordination occurs outside the app.

#### FR-021 — Distinct RSVP states

**Source:** D07.

- AC1: Each event distinguishes Going, Maybe, Not going, and No response for its participants.
- AC2: A member can update their own RSVP.
- AC3: No response is not automatically recorded or treated as Not going, and an RSVP is not recorded as actual attendance.

#### FR-022 — RSVPs on participants' behalf

**Source:** D07.

- AC1: Event editors can record/update another participant's RSVP, including a participant without an account.
- AC2: This proxy RSVP capability also applies to participants with accounts; those members can still update their own responses.
- AC3: An ordinary member without event-editor authority cannot update other participants' RSVPs.

#### FR-023 — Manual picker assignment

**Source:** D06, D11.

- AC1: Event editors can directly assign or replace the event's picker with a current participant without running a random draw.
- AC2: Participants without accounts can be assigned; they do not gain private app access by becoming picker.
- AC3: A member without event-editor authority cannot replace the picker. At full v1, reservation and exception effects follow M5; unresolved multiple-assignment cases are identified in R-003.

#### FR-024 — Record the movie choice

**Source:** D06, D08.

- AC1: An event supports one movie choice, using a catalog or manual entry.
- AC2: An assigned picker with approved membership can record/change the choice even on someone else's event; event editors can record/change it on the picker's behalf.
- AC3: Choosing a film outside the watchlist or choosing a rewatch does not require votes, recommendations, or owner/admin movie approval.
- AC4: A picker without an account communicates their choice through an event editor; their assignment does not create self-service access.

#### FR-025 — Explicit completion and optional picker credit

**Source:** D10.

- AC1: An event editor explicitly confirms that a night happened before it enters completed group history or consumes a regular picker turn. Time passing alone does neither.
- AC2: A completed night can award picker credit or explicitly award none; the uncredited night still enters group history and consumes nobody's turn.
- AC3: A credited completed night contributes one night to the credited participant's lifetime picker total; viewing or repeating confirmation of that same completion does not add another night.
- AC4: An ordinary member without event-editor authority cannot confirm completion. M5 supplies the related round/reservation effects; confirmation while a movie remains undecided and retroactive credit changes require the policy resolution in R-003.

#### FR-026 — Optional actual attendance

**Source:** D07.

- AC1: During completion, an event editor can optionally record full or partial actual attendance, including for participants without accounts.
- AC2: Actual attendance remains distinct from the RSVP and does not require exact arrival or departure times.
- AC3: A night can be completed without an actual-attendance record; an unrecorded attendance result is not silently inferred from Going or No response.

#### FR-027 — Group history and lifetime picker totals

**Source:** D10, D13.

- AC1: Members can view completed group nights with their recorded movie, picker credit when present, and actual attendance when recorded.
- AC2: Lifetime picker totals are group-specific and count credited completed nights, excluding planned assignments and uncredited completions.
- AC3: Group history remains a record of group nights rather than a personal viewing log. Lifecycle attribution changes follow M6, not an automatic rewrite of past nights.

#### FR-028 — Completion-driven watchlist cleanup

**Source:** D12.

- AC1: Completing a night removes its identified movie from that group's active watchlist when present.
- AC2: The completed movie remains in group history, and a member can add it to the watchlist again for a rewatch.
- AC3: Cleanup in one group does not remove another group's suggestions or rewrite prior viewing history. Uncertain manual/catalog identity matches are governed by R-005.

### M5. Picker rotation and flexible exceptions

**User story US-005:** As a group, we want fair random turns with explicit exceptions, so absences, cancellations, and advance planning do not distort completed picker credit.

#### FR-029 — One group rotation without replacement

**Source:** D09.

- AC1: Individual events and recurring-series occurrences in the same group draw from one shared rotation.
- AC2: Regular random draws select from eligible rotation participants without replacement within a round, respecting used turns and reservations.
- AC3: Another group's rounds, picker assignments, and completion history do not change this group's rotation.

#### FR-030 — Explicit draw initiation and permission

**Source:** D06, D09.

- AC1: A draw runs only when an event editor explicitly starts it.
- AC2: Event creation or reaching a scheduled date/time does not automatically select a picker.
- AC3: Another ordinary member cannot run the draw, and an unavailable draw does not silently become an automatic assignment.

#### FR-031 — Attendance-aware default eligibility

**Source:** D07, D11.

- AC1: Regular eligibility considers rotation inclusion, current-round unused status, and the absence of a conflicting regular reservation.
- AC2: Not going excludes a participant from that event's draw by default. Going, Maybe, and No response do not by themselves exclude an otherwise eligible participant.
- AC3: An event editor can override attendance eligibility for an exception; direct assignments outside the regular pool remain available under FR-034.

#### FR-032 — Picker reservations

**Source:** D10; ADR 0002.

- AC1: Assigning an unused regular turn creates a picker reservation for that event.
- AC2: Before completion, the reservation does not create a used turn or increase the lifetime picker total.
- AC3: That regular reservation excludes the participant from regular draws for other upcoming events in the same group. Multiple manual exceptions require the explicit policy review in R-003.

#### FR-033 — Consume on completion and release on cancellation

**Source:** D10; ADR 0002.

- AC1: Confirming a regular credited night changes its reserved turn to used and counts the completed picker credit.
- AC2: Canceling an upcoming night releases its unused regular reservation without consuming the turn or increasing the lifetime picker total; eligibility then follows the other applicable rules.
- AC3: Merely selecting a movie does not count the reservation as a completed turn.
- AC4: Completing without picker credit does not consume a turn. Handling pre-existing assignments, retroactive corrections, and multiple manual reservations must follow an approved R-003 policy before those edge cases are signed off.

#### FR-034 — Manual exceptions and an empty eligible pool

**Source:** D11.

- AC1: An event editor can manually select any current participant, including someone outside the regular eligible pool, instead of rerolling.
- AC2: If the only unused rotation participant is not attending, the app keeps the round open and requires a manual exception rather than resetting everyone's eligibility.
- AC3: A credited extra manual pick enters lifetime totals as a completed night but does not erase another participant's unused regular turn.

#### FR-035 — Round completion and advance planning

**Source:** D09–D11.

- AC1: A regular round resets after its included rotation participants have used their turns; excluded participants do not prevent reset.
- AC2: When remaining unused turns are reserved for upcoming nights, regular draws wait for the current round to finish instead of opening overlapping automatic rounds.
- AC3: Temporarily unavailable unused participants do not cause an early reset. Groups can still schedule further events and make manual assignments while regular draws wait.

#### FR-036 — First-time, returning, and newly linked participants

**Source:** D02, D11.

- AC1: A first-time participant enters the active round with an unused turn.
- AC2: A returning participant retains their used/unused status when the same round is still active; leaving and rejoining does not grant another regular turn.
- AC3: Linking an account to an existing participant retains that participant's state rather than treating the person as first-time.

#### FR-037 — Exclude a participant without removing them

**Source:** D11.

- AC1: Owners/admins can keep a participant in the group but exclude them from rotation.
- AC2: The participant can still be represented in attendance and event activity; exclusion alone is not removal from the group.
- AC3: Excluded participants are omitted from regular draws and do not hold the round open. An ordinary member cannot change this manager-only rotation setting.

#### FR-038 — Current-round corrections

**Source:** D11.

- AC1: Owners/admins can manually adjust current-round used/unused turns after initial setup.
- AC2: An eligibility correction alone does not rewrite movie-night history or change lifetime picker totals.
- AC3: An event creator who is not an owner/admin does not receive this group-wide correction authority merely from being an event editor.

### M6. Group and account lifecycle

**User story US-006:** As a member or owner, I want clear departure and ownership rules and an account-deletion path, so access and historical attribution follow the group's approved policies.

#### FR-039 — Departure and removal

**Source:** D04, D13.

- AC1: A non-owner member can leave, and an authorized manager can remove a member within FR-007's role limits.
- AC2: Leaving/removal revokes that account's private access to the group, including access through old event links.
- AC3: Named attribution for past picks and understandable lifetime totals remain in group history.
- AC4: The effect on a linked participant's ongoing roster status and pending assignments must be approved under R-002 before final lifecycle verification; revoking access does not silently decide those separate outcomes.

#### FR-040 — Fresh admission on rejoin

**Source:** D03, D11.

- AC1: A former member may use an invitation link to request to return.
- AC2: Access is restored only after fresh owner/admin approval, without requiring a separate banning system.
- AC3: Returning identity and current-round status follow FR-006 and FR-036; rejoining does not create duplicate history or an extra regular turn.

#### FR-041 — Ownership transfer and owner departure

**Source:** D04, D13.

- AC1: The owner can transfer ownership only to an existing member with approved account access to that group; a participant without an account cannot receive it.
- AC2: An owner cannot leave a continuing group without first transferring ownership. After a successful transfer, the approved recipient owns the group and the previous owner can proceed to leave.
- AC3: Account deletion cannot proceed while the person still owns groups; each must be transferred or deleted. Having only accountless participants does not satisfy the transfer precondition.

#### FR-042 — Owner-only group deletion

**Source:** D04.

- AC1: Only the owner can permanently delete the group; admins and ordinary members cannot.
- AC2: Deletion requires explicit confirmation explaining that the group's shared watchlist and movie-night history will be lost.
- AC3: After confirmed deletion, the group's shared records are no longer available through the product, and other groups remain unaffected. A last-member group can be closed through this workflow.

#### FR-043 — Account deletion, provisionally specified

**Source:** D13; provisionally accepted final clarification.
**Status:** Required in v1; detailed acceptance is gated by R-001.

- AC1: An account holder has an account-deletion path once all owned groups have been transferred to approved account holders or deleted.
- AC2: Under the provisionally accepted outcome, deletion revokes active participation and anonymizes personal history, for example with Deleted member attribution in retained group history.
- AC3: Deletion does not substitute conversion into a named participant without an account for the approved revocation/anonymization outcome.
- AC4: Before implementation, the project owner approves exact data-handling semantics after technical/privacy review covering all categories listed in R-001.
- AC5: M6 and v1 cannot be signed off until that reviewed policy has testable detailed criteria and verified behavior. A placeholder workflow or moving deletion to post-MVP does not satisfy this requirement.

### M7. Existing-group migration and pilot

**User story US-007:** As the existing group's organizer, I want our current records transferred with reviewed corrections, so ScreenTime can become the main record without requiring everyone to sign up or losing our history.

#### FR-044 — One-time migration scope

**Source:** D01, D14.

- AC1: Migration covers the existing group's movie-night history and attendance, planned nights and assignments, watchlist suggestions and existing votes, participants, and picker information.
- AC2: The migration is for this group once; neither ongoing spreadsheet synchronization nor a general-purpose importer is required.
- AC3: After reviewed import and pilot acceptance, ScreenTime becomes the group's main record.

#### FR-045 — Review before import and source preservation

**Source:** D14.

- AC1: Before import, the group owner reviews and approves proposed movie matches, corrections, participant mappings, and starting rotation.
- AC2: Uncertain entries are flagged for confirmation rather than silently guessed; missing catalog matches can retain manual movie entries.
- AC3: Import uses the approved review outcome and leaves the source workbook unchanged. No particular migration interface or execution mechanism is mandated.

#### FR-046 — Migration without universal signup

**Source:** D02, D14.

- AC1: People named in the spreadsheet do not all need accounts before migration; their records can be represented by participants without accounts.
- AC2: Approved participant mappings preserve attribution for history, suggestions, existing votes, and picker information.
- AC3: A later approved account link retains imported records and rotation state without duplicating the participant or their contributions.

#### FR-047 — Schedule correction review

**Source:** D01, D05, D14.

- AC1: Review of inconsistent planned dates/times uses the clarified Thursday-at-8-PM Pacific local routine and its seasonal-clock meaning as context.
- AC2: The owner confirms proposed corrections rather than the migration blindly replacing dates with a fixed schedule.
- AC3: Imported approved event times display consistently under the group/viewer time-zone rules in FR-017.

#### FR-048 — Historical attendance interpretation

**Source:** D07, D14.

- AC1: An attendance asterisk in the existing sheet is interpreted as partial attendance.
- AC2: Approved historical attendance is preserved separately from RSVP intention without inventing exact arrival/departure times.
- AC3: Attendance attribution follows reviewed participant mappings, including people who have not signed in.

#### FR-049 — Imported credits, reservations, and starting round

**Source:** D10–D11, D14.

- AC1: Completed/watched nights determine imported lifetime picker totals; upcoming assignments are imported as reservations rather than completed credit.
- AC2: A night's picker can remain undecided where appropriate; a placeholder is not silently treated as a new real participant.
- AC3: An owner/admin explicitly confirms used/unused turns for the current round. Migration does not infer round boundaries solely from lifetime totals.

#### FR-050 — Migration reconciliation

**Source:** D14; M7 verification.

- AC1: Every record approved for import is accounted for in the resulting history, attendance, planned nights, suggestions, votes, participant attribution, and picker state.
- AC2: Every correction or difference from source counters is explained by the approved review, including the distinction between planned assignments and completed nights.
- AC3: There are no unexplained omissions, duplicated participant contributions, or attribution/count discrepancies when the owner accepts the migration result.

#### FR-051 — Actual-group pilot

**Source:** D01, D14; M7 verification.

- AC1: Using the migrated group, the pilot exercises planning, picker/movie selection, RSVP, completion, optional attendance recording, and an agreed exception, checking the expected resulting records.
- AC2: The pilot checklist records pass/fail evidence for the relevant workflows on phones and desktops and confirms later account linking preserves imported state.
- AC3: The owner accepts the reconciled result and the group uses ScreenTime as its main record. No fixed pilot duration or number of movie nights is imposed by this PRD.

## 6. Cross-milestone product constraints

### QR-001 — Responsive web workflows

**Source:** D01; M1–M7.

- AC1: The applicable workflows in each milestone can be completed through the website on phones and desktops, including forms, calendar/list views, and required confirmations.
- AC2: Verification covers completing the workflow, not only opening its initial screen.
- AC3: No native app installation is required for an invitation recipient or an approved member to use v1.

No specific device dimensions, accessibility conformance target, latency, uptime, or user-capacity commitment was approved in discovery. Such targets must not be reported as agreed requirements without review.

### QR-002 — Future recommendation compatibility

**Source:** D15.

- AC1: Before approving the initial data model in subsequent technical planning, a documented review explains how future personalization can preserve participant/account attribution, movie identity, group history and attendance, suggestions, and interest.
- AC2: The review explicitly covers participants without accounts, later approved account links, and manually entered movies that may later be matched to catalog entries.
- AC3: The review demonstrates that later personal watchlists, personal watched status, ratings, and preferences can be accommodated without discarding the meaning of v1 records.
- AC4: Completing this review does not require implementing recommendations or those additional personal features in v1 and does not approve a particular schema or algorithm.

## 7. Important user flows

### UF-01 — Create a group or join an existing one

1. A person uses Google sign-in or email/password registration and login.
2. They either create a private group and become its owner, or follow a shared invite link to request admission to an existing group.
3. For admission, an owner/admin approves access and explicitly confirms any link to an existing participant.
4. The member can use that group's authorized features. A participant without an account remains represented without receiving access.

**Requirements:** FR-001–FR-008.

### UF-02 — Collect suggestions and interest

1. A member selects a catalog movie or enters a missing title manually and adds their suggestion.
2. Members express their own interest. Owners/admins may record suggestions or interest only for participants without accounts.
3. Each participant has at most one interest vote per movie.
4. Own-entry and manager removal rights apply; no suggestion or vote binds the picker.

**Requirements:** FR-009–FR-013, FR-024.

### UF-03 — Schedule and adjust movie nights

1. A member creates an individual event or the supported recurring series, with a start time and optional end time/meeting details.
2. Picker and movie may remain undecided. Members see month/upcoming views in their own current local time.
3. An event editor reschedules or cancels one occurrence or that occurrence and future occurrences.
4. Past events remain unchanged by series operations. Cancellation integrates with reservation release when M5 is delivered.

**Requirements:** FR-014–FR-020, FR-033.

### UF-04 — Run a movie night and record the result

1. Members RSVP, or an event editor records responses received outside the app.
2. An event editor reviews eligibility, starts a random draw when available, or makes a manual assignment.
3. The picker records the movie if they have access; otherwise an event editor records their choice.
4. After the night, an event editor confirms completion, optionally records full/partial attendance, and records picker credit or none.
5. History, lifetime totals, regular used turns/reservations, and watchlist cleanup reflect that outcome.

**Requirements:** FR-021–FR-038.

### UF-05 — Handle an absence or canceled plan

1. Not going excludes a participant from the default draw; an event editor can make an explicit exception.
2. An empty available pool does not reset a round early; the editor may select a substitute manually.
3. Canceling an upcoming regular assignment releases its reservation without completed credit.
4. Owners/admins can make current-round corrections independently of lifetime totals.
5. Cases involving repeated manual reservations, already completed nights, or post-assignment RSVP changes use the approved resolution of R-003; this flow does not assume an automatic redraw.

**Requirements:** FR-030–FR-038.

### UF-06 — Leave, transfer, or delete

1. A non-owner leaves, or a permitted manager removes a member; access ends and named past attribution remains.
2. A returning member requests fresh approval and retains the appropriate existing participant/round identity.
3. An owner who wants to leave transfers to another approved member, or uses confirmed group deletion to close the group.
4. Account deletion requires resolving owned groups and then applies the reviewed revocation/anonymization policy. R-001 and R-002 govern unresolved lifecycle details.

**Requirements:** FR-039–FR-043.

### UF-07 — Move the existing spreadsheet into actual use

1. Prepare the one-time migration proposal without requiring universal signup.
2. The owner reviews data corrections, movie and participant matches, upcoming reservations, and starting round.
3. Import the reviewed result without altering the source workbook.
4. Reconcile all approved records and exercise the real-group pilot checklist.
5. Accept the reconciled result and use ScreenTime as the main record.

**Requirements:** FR-044–FR-051, QR-001.

## 8. Required edge-case coverage

These are required verification scenarios for the referenced behavior. Open policies remain explicit gates; this table does not choose their outcomes.

| Scenario | Expected rule or approval gate |
| --- | --- |
| A link is forwarded to someone outside the group | Fresh approval is still required; no private access from the link alone. FR-004–FR-005. |
| Two people have the same display name | No automatic account link; a manager confirms the correct participant. FR-006. |
| A later signup matches an imported participant | Preserve records, interest, and current turn; no duplicate person or bonus turn. FR-006, FR-036, FR-046. |
| A picker has no account | An event editor records their choice; the picker gains no app access. FR-023–FR-024. |
| A participant with an account asks a manager to enter a vote | Proxy watchlist capability is unavailable for that person, unlike proxy RSVPs. FR-013, FR-022. |
| No RSVP has been recorded | Keep No response distinct from Not going and actual attendance. FR-021, FR-031. |
| The picker attends only briefly | Partial attendance can be recorded independently; picker credit is explicitly recorded rather than inferred from RSVP. FR-025–FR-026. |
| The only unused participant is absent | Keep the round open; permit a manual exception. FR-034. |
| All remaining regular turns are reserved | Wait for the active round to finish; allow later scheduling/manual assignment. FR-035. |
| A new participant joins mid-round | Give an unused current-round turn; an account link to an existing person is not a new entry. FR-036. |
| A person leaves and rejoins within the same round | Fresh access approval; retain prior turn status. FR-036, FR-040. |
| A participant opts out of rotation | Manager exclusion preserves participation and removes the round-reset dependency. FR-037. |
| An owner wants to leave with no other approved account holder available | Accountless participants cannot receive ownership; transfer conditions or explicit group closure must be satisfied. FR-041–FR-042. |
| An upcoming regular assigned event is canceled | Release its unused reservation without credit. FR-033. |
| A completed night is jointly chosen | Record the movie in history without consuming anyone's turn. FR-025. |
| A completed movie is suggested for a rewatch | Permit re-adding it without deleting the old history. FR-028. |
| A recurring night crosses a seasonal clock change or a viewer travels | Preserve the group-local schedule and convert the viewer's time. Exceptional local times require R-004. |
| A series is changed after earlier nights occurred | Preserve past events; future exceptions/assignments require R-004. |
| Manual exceptions overlap, or history is corrected after a round advances | No invented turn-allocation or rollback policy; resolve R-003 before final sign-off. |
| A catalog title is ambiguous or a manual movie may duplicate an entry | Flag migration uncertainty for review; ongoing identity/merge rules require R-005. |
| A member leaves versus deletes their account | Preserve named departure history versus reviewed deletion anonymization. FR-039, FR-043; R-001–R-002. |

## 9. Dependencies and measurable milestone completion

The milestones preserve [MILESTONES.md](MILESTONES.md). They are testable increments with dependencies, not isolated applications. A feature split across milestones requires its final integrated behavior before v1 completion.

| Milestone | Dependencies | Functional requirements | Completion evidence |
| --- | --- | --- | --- |
| M1 Private groups and participant access | Approved PRD and subsequent technical approach | FR-001–FR-008 | All listed criteria pass for Google sign-in and email/password registration and login, with two groups, multiple roles, an unapproved requester, a participant without an account, and an account explicitly linked to a group participant; private information and permissions remain separated. Applicable R-007 policies are approved and verified. |
| M2 Movies and shared suggestions | M1 | FR-009–FR-013 | Catalog and manual entries, own/manager removal, interest limits, and the restricted proxy policy all pass in separate groups. |
| M3 Flexible group calendars | M1–M2 | FR-014–FR-020 | Individual and recurring nights, both calendar views, multiple viewer zones, seasonal-clock behavior, single/future operations, and editing permissions pass; relevant R-004 policies are approved and verified. |
| M4 Movie-night attendance and history | M1–M3 | FR-021–FR-028 | A manually coordinated event completes the RSVP/movie/attendance/history flow; credited and uncredited nights give the expected totals and watchlist result. Relevant completion-validation criteria in R-003 are approved and verified. Required behavior works before random draw automation is added. |
| M5 Picker rotation and flexible exceptions | M1, M3–M4 | FR-029–FR-038 | A full regular round resets correctly; reservations, cancellation, empty pool, membership/attendance exceptions, exclusions, and corrections pass; relevant R-003 cases have approved criteria and verified outcomes. |
| M6 Group and account lifecycle | M1–M5 and resolved account-deletion review | FR-039–FR-043 | Departure/removal/rejoin, retained attribution, owner-only transfer/deletion, and approved account-deletion semantics pass across existing group records; R-001–R-002 are resolved. |
| M7 Existing-group migration and pilot | M1–M6 | FR-044–FR-051 | Owner-approved data reconcile without unexplained loss/duplication, original workbook remains unchanged, and the phone/desktop pilot checklist passes with the migrated group as the main record. |

QR-001 applies throughout. QR-002 is a review gate during subsequent technical planning before the initial data model is approved. Relevant identity/matching policies in R-005 must be resolved before the affected requirement is signed off.

R-007 applies to authentication behavior across milestones, including any applicable effects on account lifecycle in M6. Approve the relevant policies before implementing the affected behavior; existing R-001 and R-002 lifecycle gates remain in force.

V1 completion requires:

1. Every FR and applicable acceptance criterion has recorded passing evidence, including integrated behavior spanning milestones.
2. Both cross-milestone constraints have passing verification/review evidence.
3. Every approval-dependent v1 policy affecting completion has an approved resolution and corresponding verified criteria; a provisional feature is not counted as done merely because its review is documented.
4. Every source decision is accounted for as v1 behavior, an explicit post-MVP boundary, a review constraint, or an approval rule in section 12.
5. The migration and actual-group pilot are accepted. No approved feature has been silently dropped or moved out of v1.

### Early end-to-end demonstrable release checkpoint

An early demonstrable release should show one complete journey using selected existing M1–M4 behaviors. It is a development checkpoint, not a new milestone, a smaller definition of v1, or a replacement for any milestone's completion evidence. The seven milestone definitions, dependencies, functional requirements, and acceptance criteria remain unchanged.

Demonstrate the following sequence through the website using the existing permission rules:

1. Sign in and create a private group (FR-001–FR-002), with a current participant available for selection; use the existing participant-management behavior if needed (FR-003).
2. Schedule a single, individual movie night with its start date/time (FR-014–FR-015).
3. As an event editor, assign its picker manually (FR-023).
4. Record one movie using the approved catalog/manual-entry behavior (FR-009, FR-024).
5. Explicitly confirm completion with picker credit, then verify the movie and picker credit in group history and the corresponding lifetime picker total (FR-025, FR-027).

Checkpoint evidence is a successful end-to-end demonstration of that sequence, with the completed night visible in history and credited once under the existing acceptance criteria. It does not mark M1–M4 complete or change their approved delivery dependencies. Requirements outside this demonstration remain required in their existing milestones; random rotation, lifecycle, migration, and all other v1 requirements are still part of the full release.

The checkpoint can be demonstrated when its necessary behaviors are available under the normal planning approvals and the affected-policy gates in section 11. It does not resolve an open policy, authorize architecture or implementation work, or change the post-MVP recommendation boundary.

## 10. Post-MVP recommendation direction

Personalized group recommendations remain a high-priority feature after v1. Desired signals are predicted enjoyment across the group, movies participants have not watched, overlap between personal watchlists, and the current picker's preferences. Algorithms, relative weights, evaluation methods, and additional preference collection remain undecided.

The initial compatibility review must preserve the meaning of v1 data while leaving room for future personal watchlists, viewing logs, ratings, and preferences. It must handle participants who later link accounts and manually entered movies that may later be identified in a catalog. QR-002 states the reviewable constraint without selecting a data model.

Letterboxd integration remains a separate future possibility subject to feasibility. Neither its availability nor the future recommender is a prerequisite for v1. The other explicit post-MVP boundaries remain in section 3.

## 11. Unresolved policies, risks, and approval needs

No unresolved item below is permission to remove an approved v1 requirement. Where discovery establishes an outcome but not every interaction, this PRD records the established criteria and marks the remaining policy gate.

### Approval timing for R-001 through R-005 and R-007

R-001 through R-005 and R-007 are approval gates **before implementation of the behaviors they affect**. Resolve the relevant unresolved choices and obtain project-owner approval before that affected work begins. Already approved requirements are not reopened, and these gates do not block unrelated work that has its normal planning approvals.

Targeted policy reviews at the point of need are sufficient; another comprehensive discovery interview is not required now. References elsewhere to milestone acceptance or sign-off remain verification gates for the approved outcomes, not permission to postpone policy approval until after implementation. This refinement does not select answers to any open policy.

| Item | Established boundary | Unresolved question or risk | Required resolution |
| --- | --- | --- | --- |
| R-001 Account-deletion semantics — provisional | Revoke active participation, anonymize personal history, resolve owned groups first, keep deletion in v1. | Exact treatment of account links/identifiers, memberships/participant records, history/attendance, suggestions/votes, requests, future assignments/reservations, retained operational data, and a later return is unspecified. No retention period, deletion mechanism, or compliance conclusion is approved. | Technical/privacy review and project-owner approval before implementing FR-043; add detailed testable semantics before M6 sign-off. |
| R-002 Departure versus ongoing participation | Leaving/removal revokes app access and preserves named past attribution. Accountless participation exists separately. | Sources do not state whether a departing linked member's participant remains active without access, leaves the active roster, or how pending assignments/reservations are handled. Account deletion must not be treated as a named accountless conversion. | Approve unresolved participant/assignment transition rules before implementing those transitions, then verify them during lifecycle integration and M6 acceptance. Do not infer the answer solely from access revocation. |
| R-003 Completion, reservation, and correction interactions | Manual assignment may select any current participant; one active automatic round; completed credit determines lifetime totals; corrections can change current eligibility without rewriting history. | Confirmation while the movie is still undecided, repeated far-future manual assignments for one person, assignment replacement, completion without credit after a reservation, post-assignment attendance changes, and correcting completed credit after round advancement need precise rules. | Approve the unresolved product outcomes before implementing the affected completion, reservation, or correction behavior, then verify the relevant M4/M5 cases against the approved criteria. Preserve all existing regular-turn and manual-exception rules. |
| R-004 Recurrence and local-time exceptions | Group-local recurrence, viewer-local display, single/future changes, past-event preservation. | Nonexistent/ambiguous local times, changing the scheduling time zone, and bulk future edits interacting with existing occurrence exceptions, RSVPs, picker assignments, and movie choices are not specified. | Approve unresolved user-visible policies before implementing the affected recurrence or local-time behavior, then verify the M3/integrated scenarios. Time-zone detection tooling and UI presentation remain implementation choices. |
| R-005 Movie identity and shared-entry semantics | Catalog search plus manual fallback; one interest vote per participant per movie; owner-reviewed migration matches. | The metadata source is unselected. Ongoing manual-to-catalog matching, duplicate suggestions with multiple contributors, vote retraction, and merges affecting ownership/interest/history are not defined. | Select tooling only in later approved technical planning; obtain approval for unresolved product policies affecting attribution, permissions, or counts before implementing their affected behavior, then verify the M2/M7 cases. Keep catalog search and fallback in scope. |
| R-006 Delivery and adoption risk | 10 hours per week, flexible timeline, full seven-milestone v1, participants without accounts, pilot using migrated records. | Calendar exceptions and participant/account continuity make this a substantial project. No estimates, fixed pilot duration, or number of nights have been agreed. | Estimate after technical planning, preserve scope unless the project owner approves a change, and evaluate progress using milestone evidence and FR-051 rather than an invented deadline. |
| R-007 Authentication policies | Google sign-in and email/password registration and login are required in v1; sign-in does not bypass private-group membership approval. | Sign-in method linking, password recovery, verification, and security-related behavior remain unresolved; see the [authentication policy questions](#authentication-policy-questions-r-007). | Obtain project-owner approval for the relevant product behavior and technical/security design before affected implementation. Record approved outcomes as testable criteria and verify applicable policies before M1 acceptance and affected later milestone acceptance. |

### Authentication policy questions (R-007)

- **Sign-in method linking:** whether it is available, how methods may be linked or unlinked, required proof of control, matching-email conflicts, and duplicate-account handling. This is separate from FR-006's owner/admin-confirmed account link to a group participant.
- **Password recovery:** availability, identity checks, recovery flow, and effects on existing sessions. The approved registration/login requirement does not settle recovery scope or behavior.
- **Email ownership:** verification requirements and timing, and the handling of email changes.
- **Security-related behavior:** password rules, failed-attempt responses, throttling or lockouts, session duration, logout, and sensitive-action reauthentication.

No automatic sign-in method linking, username login, recovery mechanism, security thresholds, authentication provider, or schema is approved by this amendment. Authentication email requirements depend on the decisions above; they are separate from the existing deferral of movie-night and group-activity notifications. Authentication tooling and credential storage design still require technical planning and approval.

The following can be refined during implementation within the approved outcomes: wording and form arrangement, sorting/presentation, responsive layout details, and how review evidence is presented. Specific validation limits, new permissions, retention rules, automatic identity matching, or changed business outcomes are not merely presentation details and must not be introduced as already approved.

No comprehensive discovery interview is required to resolve the remaining policy gates. The project owner can approve or amend the listed policy gaps as part of planning; unresolved gaps remain visible gates rather than assumed defaults.

## 12. Coverage check against approved discovery and milestones

This matrix records a section-by-section coverage review. A mapped provisional requirement is covered in scope, but it remains conditional until its policy and acceptance criteria are approved. Coverage does not resolve the remaining policy gates or claim that the software is complete.

| Source | Preserved requirements or constraint | PRD coverage |
| --- | --- | --- |
| D01 Product and delivery | Actual-group and portfolio purpose; responsive web; 10-hour budget/flexible timeline; current remote routine/future in-person use; full v1 and spreadsheet replacement. | Sections 2–3 and 9; FR-014–FR-015, FR-044, FR-047, FR-051; QR-001. |
| D02 Accounts, participants, links | Google sign-in and email/password registration and login under the approved 2026-11-09 amendment; accountless participation; approved app access; explicit participant matching; continuity without duplicate identities or turns. | FR-001, FR-003, FR-005–FR-006, FR-008, FR-036, FR-046; R-007. |
| D03 Private groups and admission | Creation/multiple groups; isolation; shared/forwarded invite approval; fresh rejoin; no separate ban system. | FR-002, FR-004–FR-005, FR-008, FR-040; section 3. |
| D04 Management and ownership | Creator owner; ongoing roles; admin/member authority; participant management; owner departure, approved-account transfer, confirmed owner-only deletion. | FR-002–FR-003, FR-007, FR-039, FR-041–FR-042; permission matrix. |
| D05 Flexible calendar | Arbitrary nights; weekly/multiweek recurrence; group/viewer zones; start/end/details; month/upcoming; single/future changes; deferred advanced functions. | FR-014–FR-020; section 3; R-004. |
| D06 Event authority/readiness | Any member creates; editors control event/series; missing film/picker allowed; picker/editor movie entry without approval. | FR-014, FR-019, FR-023–FR-024, FR-030. |
| D07 RSVPs/attendance | Four RSVP states; own and proxy responses for anyone; optional full/partial actual attendance without exact times. | FR-021–FR-022, FR-026, FR-048. |
| D08 Movie selection/identification | One film; catalog/manual entry; unrestricted picker choice; manual tracking; possible future Letterboxd integration. | FR-009, FR-024, FR-027–FR-028; sections 3 and 10. |
| D09 Rotation/rounds | One rotation per group; without replacement; completion-based reset; explicit draw; one active automatic round with later manual scheduling allowed. | FR-029–FR-030, FR-032, FR-034–FR-035. |
| D10 Reservations/credits | Reserve on assignment; explicit completion; cancellation release; optional credit; completed-only totals distinct from eligibility. | FR-025, FR-027, FR-032–FR-035, FR-038, FR-049; R-003. |
| D11 Eligibility/exceptions | Attendance default/override; manual any-current assignment; no premature reset; first-time/return/link continuity; opt-out; independent current-round corrections. | FR-006, FR-023, FR-031, FR-034–FR-038, FR-040, FR-049. |
| D12 Shared watchlists/interest | Suggestions/removal permissions; one interest vote; proxy only for participants without accounts; completed cleanup and rewatch. | FR-010–FR-013, FR-028; R-005. |
| D13 History/lifecycle/deletion | Group-only history; named departure; revoked access; ownership precondition; provisional deletion with technical/privacy review and no deferral. | FR-025–FR-027, FR-039–FR-043; sections 3 and 11; R-001–R-002. |
| D14 Migration | All existing datasets; no universal signup; reviewed matching/corrections; partial-attendance marker; completed totals/future reservations; explicit current-round setup; one-time only; original unchanged. | FR-044–FR-051; FR-006; R-005. |
| D15 Post-MVP and compatibility | High-priority recommendations and desired signals; future personal features; compatibility constraint; explicit other deferrals and manual communication. | Sections 3, 6, and 10; QR-002. |
| D16 Approval boundaries | Discovery concluded; no approved architecture; superseded signup/fixed-schedule/selection-consumes-turn assumptions; explicit scope-change approval. | Sections 1, 4, 9, and 11; FR-003, FR-014, FR-032–FR-033. |
| M1 Private groups/participant access | Complete M1 outcome, both approved sign-in methods, and role/isolation/participant-link verification. | FR-001–FR-008; US-001; UF-01; section 9; R-007. |
| M2 Movies/shared suggestions | Complete M2 outcome including restricted proxy permission tests. | FR-009–FR-013; US-002; UF-02; section 9. |
| M3 Flexible calendars | Complete M3 outcome including editor rights, zones, recurrence exceptions, and past preservation. | FR-014–FR-020; US-003; UF-03; section 9. |
| M4 Attendance/history | Complete manual coordination, movie permissions, optional attendance/credit, totals, and cleanup. | FR-021–FR-028; US-004; UF-04; section 9. |
| M5 Rotation/exceptions | Complete draw, reservation, round, absence, membership, opt-out, and correction behavior. | FR-029–FR-038; US-005; UF-04–UF-05; section 9. |
| M6 Group/account lifecycle | Complete access, history, rejoin, approved ownership, deletion, and reviewed anonymization behavior. | FR-039–FR-043; US-006; UF-06; section 9. |
| M7 Migration/pilot | Complete reviewed migration, source preservation, reconciliation, later links, and phone/desktop actual-group pilot. | FR-044–FR-051; US-007; UF-07; section 9. |
| ADR 0001 | Distinct participation/access and manager-confirmed continuity. | FR-003, FR-006, FR-008, FR-036, FR-046; BR-01–BR-02. |
| ADR 0002 | Reservation/completion distinction, cancellation release, independent eligibility, and one active round. | FR-025, FR-027, FR-032–FR-035, FR-038, FR-049; BR-05–BR-07. |
| ADR 0003 | Approved Google and email/password authentication scope; superseded discovery history; distinction between sign-in method linking and participant account links; unresolved authentication policies. | FR-001, FR-006; sections 1, 3, 7, 9, and 11; R-007. |
| Glossary | Participant/member distinction; event editor; scheduling zone; RSVP/actual attendance; rotation/reservation/credit/total; shared watchlist/interest/history. | Used throughout sections 2–12 and the permission/business-rule tables. |

**Coverage result:** All 16 discovery decision areas and all seven milestone outcomes are represented. No approved requirement is intentionally omitted or moved to post-MVP. The unresolved policy/feasibility items are explicitly listed in section 11 and are not reported as already settled.
