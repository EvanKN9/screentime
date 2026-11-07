# Approved ScreenTime discovery decisions

Discovery concluded and was approved by the project owner on **2026-11-07**, including the final clarifications recorded below. This document preserves product decisions; it is not a PRD or an architecture specification.

Read [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md) for orientation, [GLOSSARY.md](../GLOSSARY.md) for vocabulary, and [MILESTONES.md](MILESTONES.md) for delivery organization. The full agreed MVP is the **v1 target**. Milestones do not remove or defer any approved v1 requirement.

## D01. Product and delivery

- Build a social movie watch-party planner suitable for actual friend-group use and a portfolio project, with a longer-term social movie platform vision.
- Deliver a responsive website for phones and desktops. Native apps are post-MVP.
- Plan around 10 hours of development per week, with a flexible timeline.
- Replace the existing group's spreadsheet after its one-time migration. The current group meets remotely on Thursdays at 8 PM Pacific local time, following seasonal clock changes, and anticipates in-person nights later.
- Preserve all approved v1 scope while organizing work into smaller, independently testable milestones. Scope reductions require explicit project-owner approval.

## D02. Accounts, participants, and account links

- Google sign-in is the only v1 sign-in option. Separate passwords and password recovery are outside v1.
- A participant can exist without an account. Owners/admins can add and manage such participants, including their inclusion in picker rotation and attendance records.
- Only approved accounts can access a private group and act in the app themselves. A participant record alone grants no access.
- An owner/admin explicitly confirms the link between a newly joining account and an existing participant. A matching display name does not establish that link automatically.
- Linking preserves that participant's history, suggestions, and current rotation state; it does not create a duplicate participant or grant a new turn.
- Terminology distinguishes the participant in group activity from the member with approved account access. See [ADR 0001](adr/0001-participation-without-accounts.md).

## D03. Private groups and admission

- Any signed-in user can create a private group and belong to multiple groups. Group planning, watchlists, history, and rotations remain separate.
- Nonmembers cannot browse a group's membership, schedule, or watchlist.
- Any member can share the group's invitation link. Following the link permits a membership request, not immediate access; an owner/admin must approve admission.
- A forwarded link does not bypass approval.
- Former members may request to rejoin through a link and require fresh approval. A separate banning system is outside v1.

## D04. Group management and ownership

- The group creator is its owner. Owner/admin are ongoing group roles, independent of the person hosting or choosing a particular movie night.
- Only the owner can appoint or remove admins. Owners/admins can approve membership and remove ordinary members. Admins cannot remove the owner or other admins; removing an admin is owner-only.
- Owners/admins manage participants without accounts, as described in D02.
- An owner must transfer ownership before leaving a group that continues with other people.
- Only an approved account holder can receive ownership. A participant without an account cannot inherit group access through an ownership transfer.
- Only the owner can permanently delete the group, including its shared watchlist and movie-night history, after explicit confirmation of the loss. This also provides a way to close a last-member group.

## D05. Flexible calendar

- Each group chooses when to meet; v1 is not restricted to the existing group's weekly routine.
- Support events on arbitrary dates and times and recurring series on a chosen weekday every week or every few weeks, such as every other Saturday. Monthly and more complex recurrence patterns are deferred.
- Each group has a scheduling time zone. Recurring events stay at the intended local time there across seasonal clock changes. Each viewer sees times converted to their current local time zone.
- Require an event start date/time. End time is optional; do not invent an end time from an undecided movie.
- Optional meeting details can hold a call link, address, or joining instructions, supporting remote and future in-person gatherings.
- Provide a month calendar and an upcoming-events list. Week/day time grids and drag-and-drop scheduling are deferred; rescheduling uses event editing.
- Editing or canceling a recurring event supports this occurrence only or this occurrence and future occurrences. Series changes preserve past events.

## D06. Event authority and readiness

- Any member can create events and recurring series without a separate approval workflow.
- The event creator and group owner/admins are its event editors. They can edit/cancel the event and manage its picker selection. Apply the same management principle to series.
- An event can be created before either its picker or movie is known.
- The assigned picker can record/change the movie choice even when they did not create the event. Event editors can record/change it on the picker's behalf. No movie-approval workflow is required.

## D07. RSVPs and attendance

- Each event distinguishes Going, Maybe, Not going, and No response. Silence is not a confirmed absence.
- Members can update their own RSVPs. Event editors can record/update RSVPs on any participant's behalf, including participants without accounts.
- Actual attendance is separate from an RSVP. Event editors can optionally record who attended fully or partially when confirming completion, without tracking exact arrival/departure times.

## D08. Movie selection and identification

- Support one movie per event; double features/multiple movies per event are outside v1.
- Use a searchable movie catalog with manual title entry when a movie is missing. The metadata provider is undecided.
- The picker is free to choose any movie, including one outside the watchlist. Suggestions, interest votes, and future recommendations are not restrictions.
- Manual tracking is supported. Letterboxd integration remains a future goal subject to feasibility.

## D09. Group rotation and rounds

- All events in a group share one picker rotation, including individual events and recurring series. Separate groups have separate rotations.
- Random draws operate without replacement within a round. A regular round resets once its rotation participants have used their turns; temporarily unavailable participants do not cause an early reset.
- Draws start only when an event editor explicitly initiates them. Automatic draws based on event dates are outside v1.
- Automatic picker selection manages one active round. If every turn is used or reserved, further random draws wait for that round to finish; scheduling and manual assignments can continue further ahead.

## D10. Assignments, reservations, and completed credits

- A picker assignment reserves the participant's turn and excludes that reservation from regular draws for other upcoming nights.
- An event editor explicitly confirms completion before a turn is counted as used and the night enters group viewing history. Passing the scheduled time is not confirmation.
- Canceling an event releases its reservation without costing the participant a turn.
- A completed night can have no picker credit, for example when the group chose jointly. It still enters movie history and consumes nobody's turn.
- Lifetime picker totals come from completed nights with picker credit, not planned assignments. Current-round eligibility is a separate concept.
- See [ADR 0002](adr/0002-reserve-turns-until-completion.md) for the reservation/completion trade-off.

## D11. Rotation eligibility and exceptions

- Participants marked Not going are excluded from that event's draw by default. Going, Maybe, and No response remain eligible subject to rotation rules. Event editors can override eligibility for exceptions.
- Event editors can directly assign/replace the picker with any current participant rather than repeatedly rerolling, including manual exceptions outside the regular eligible pool.
- If only unused participants are unavailable, keep the round open and require a manual exception. An extra pick need not erase another person's unused regular turn.
- First-time participants enter the current round with an unused turn. Returning participants retain their status if the same round is still active. Linking an account to an existing participant is not a first-time entry.
- Owners/admins can exclude a participant from rotation without removing them from the group. Excluded participants do not prevent the round from resetting.
- Owners/admins can adjust the current round's used/unused turns after setup without rewriting viewing history. Lifetime totals continue to derive from credited completed nights.

## D12. Shared watchlists and interest

- Each group has a shared watchlist. Members can add suggestions and remove their own suggestions; owners/admins can remove any entry.
- Interest votes indicate a desire to watch a movie, not a rating or a binding selection decision. Limit interest to one vote per participant per movie.
- **Final clarification:** owners/admins may record suggestions and interest votes on behalf of participants **without accounts**. Proxy watchlist contributions for participants with accounts were not approved. This is narrower than the proxy RSVP policy in D07.
- When a night is completed, remove its movie from the group's active watchlist if present, retaining viewing history. It can be added again for a rewatch.

## D13. History, departure, and account deletion

- Group history covers completed group movie nights. Personal viewing logs and ratings are post-MVP.
- Leaving or being removed from a group ends access but preserves named attribution for past picks and understandable picker totals.
- Account deletion remains a v1 requirement. Owned groups must first be transferred to approved account holders or deleted.
- **Provisionally accepted outcome:** revoke active participation and anonymize personal history, using a label such as Deleted member in retained group history. Do not automatically revert a linked account into a named participant without an account as a substitute for this outcome.
- Exact deletion/anonymization semantics require technical and privacy review. No retention periods, deletion mechanism, identity storage design, or compliance conclusion have been selected.

The review must define the treatment of account links and identifiers; memberships and active participant records; history and attendance attribution; suggestions and votes; pending requests, assignments, and reservations; retained operational data; and a later return by the same person. Begin this review in technical planning and resolve the semantics before implementing account deletion. Review work is not permission to remove the feature from v1.

## D14. One-time spreadsheet migration

- Bring across the existing group's spreadsheet data, including movie-night history and attendance, planned events and picker assignments, watchlist suggestions and existing votes, participants, and picker information.
- Do not require everyone in the sheet to sign in before migration. Preserve participant attribution and link approved accounts explicitly as people join.
- The owner reviews proposed movie matches, date/time corrections, participant mappings, and starting rotation before import. Flag uncertain entries for confirmation rather than guessing; manual movie entries remain available.
- Use the clarified current schedule of Thursday at 8 PM Pacific local time when reviewing inconsistent planned dates/times. The migration review, rather than silent source edits, confirms corrections.
- Interpret the attendance asterisk in the existing sheet as partial attendance.
- Derive historical picker totals from completed/watched nights. Import upcoming assignments as reservations rather than copying assignment-based counters into completed totals.
- An owner/admin explicitly confirms used/unused turns in the current round. Lifetime totals alone do not establish round boundaries.
- This is a one-time migration for this group, after which ScreenTime becomes the main record. Preserve the original workbook. Ongoing Google Sheets synchronization and a general-purpose importer are deferred.

## D15. Post-MVP scope and recommendation compatibility

Personalized group recommendations are a **high-priority post-MVP feature**. Desired signals remain:

- Predicted enjoyment across the group.
- Movies participants have not watched.
- Overlap between personal watchlists.
- The current picker's preferences.

The algorithm, weights, evaluation method, and additional preference collection are undecided. V1 does not need to implement recommendations, personal watchlists, personal viewing logs, or ratings.

Initial data-model review must explain how the proposed v1 design can accommodate future personalization while preserving participant/account attribution, movie identity, group viewing and attendance history, suggestions, and interest. It must account for participants who have not signed up and manually entered movies that may later be matched to catalog entries. Existing v1 records should not prevent adding future personal watchlists, watched status, ratings, or preferences. This is an approved compatibility requirement; no schema or recommendation architecture is selected here.

Other approved post-MVP deferrals are automated reminders and email/push notifications; external calendar integration; native apps; advanced calendar views, drag-and-drop scheduling, and more complex recurrence; ongoing spreadsheet synchronization and a general-purpose importer; and possible Letterboxd integration. V1 users check the app or share updates themselves, including schedule changes, picker assignments, and pending membership requests.

## D16. Approval boundaries and superseded assumptions

- The approved summary and final clarifications conclude discovery. A PRD and its detailed acceptance criteria are the next planning deliverable; neither the PRD nor a technical architecture has been approved yet.
- React, Python/FastAPI, PostgreSQL, and potentially TMDB remain preferences. Authentication tooling, metadata provider, hosting, schema, and other technical decisions need proposals and approval.
- The earlier requirement that every participant have an account is superseded by D02. Private app access still requires approved membership.
- The earlier fixed-weekly-only scheduling proposal was rejected. D05 permits arbitrary events with the agreed limited recurrence automation.
- Removing a turn when a movie is selected is superseded by the reservation/completion distinction in D10. Imported counters must follow that distinction too.
- Do not silently cut approved v1 requirements while refining milestones or resolving implementation questions. Obtain project-owner approval for changes to established context or architecture.
