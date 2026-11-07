# ScreenTime v1 delivery milestones

These milestones organize the complete [approved discovery scope](DISCOVERY_DECISIONS.md). They are delivery increments, not smaller definitions of v1. **V1 is complete only when all approved requirements are delivered**, including account deletion and the existing group's migration.

The working budget is 10 hours per week, with a flexible timeline. No effort estimates, launch dates, architecture, or detailed acceptance-test plan are approved by this document. The PRD should turn these observable outcomes into acceptance criteria; technical planning should then estimate and refine delivery order without dropping scope.

## Planning gates

1. Write and approve the MVP PRD from the discovery decisions and this coverage map.
2. Propose and approve the technical approach, including movie metadata, authentication tooling, and an initial data model reviewed for future personalized recommendations.
3. Begin technical/privacy review of account deletion during planning; resolve its exact semantics before implementing that feature. Keep it inside v1.

Application implementation is not authorized by this documentation update.

## M1. Private groups and participant access

**Outcome:** People can sign in with Google, create/switch between private groups, share invitations, and receive access only after approval. Owners/admins can maintain participants without accounts and explicitly link approved accounts to existing participants. Owner/admin permissions and ordinary-member removal are enforceable.

**Verification:** Exercise two groups with different accounts and roles. Verify private data stays within the approved group, a forwarded link grants no immediate access, a participant without an account has no access, and linking does not duplicate a participant. Verify admin appointment/removal and membership approval/removal permissions.

**Coverage:** D01–D04. Depends on planning approval.

## M2. Movies and shared suggestions

**Outcome:** Members can find catalog movies or enter missing titles manually, maintain each group's watchlist, and record interest. Suggestions and votes can be recorded by managers for participants without accounts, with the approved permission limits.

**Verification:** Add catalog and manual movies, exercise own-entry versus manager removal, and confirm the one-vote-per-participant rule. Verify proxy contributions are available for participants without accounts and do not extend to participants with accounts. Verify suggestions remain separate between groups.

**Coverage:** D08, D12. Depends on M1.

## M3. Flexible group calendars

**Outcome:** Members can create movie nights before choosing their film or picker, enter optional end times and meeting details, and use month/upcoming views. Groups can use arbitrary dates and the approved weekly/every-few-weeks recurrence, with per-occurrence and future-series edits/cancellation.

**Verification:** Create individual and recurring events, compare the same event from different viewer time zones, and verify recurring local times across a seasonal clock change. Move/cancel one occurrence and change/stop future occurrences without changing past records. Verify event-editor permissions, including against an ordinary member who did not create the event.

**Coverage:** D05, D06, D08. Depends on M1–M2.

## M4. Movie-night attendance and history

**Outcome:** Members and event editors can record the agreed RSVPs. An event can have a manually assigned picker; the picker and event editors can record its movie. An event editor can confirm completion, optionally record full/partial attendance, and award picker credit or explicitly award none. Group history, lifetime picker totals, and watchlist cleanup reflect completed nights.

**Verification:** Run a scheduled event through RSVPs, a manually recorded movie choice, and completion. Verify proxy RSVPs, distinct No response, optional partial attendance, and a picker recording a movie on someone else's event. Compare credited and uncredited completions: only the credited night increments a picker total. Verify completed watchlist movies leave the active list and can be re-added.

**Coverage:** D06–D08, D10, D12–D13. Depends on M1–M3. Random draws and round automation arrive in M5; this milestone already supports a complete manually coordinated night.

## M5. Picker rotation and flexible exceptions

**Outcome:** A group can run manual random draws without replacement, reserve upcoming turns, consume turns on confirmed completion, and release canceled reservations. Eligibility reflects rotation status and attendance, with the approved exclusions, manual assignments, corrections, and one-active-round limit.

**Verification:** Run a full round using M4's completion workflow, then verify reset. Cover Not going with an override, participants without accounts, a new participant, a returning participant, an excluded participant, an extra manual pick, and an empty pool. Reserve the remaining turns and verify further random draws wait while later scheduling/manual assignment remain possible. Verify current-round corrections do not rewrite lifetime totals.

**Coverage:** D09–D11. Depends on M1, M3–M4.

## M6. Group and account lifecycle

**Outcome:** Departure, removal, rejoining, ownership transfer, group deletion, and account deletion work with the actual calendar, rotation, history, and watchlist data. Owners can transfer ownership only to approved account holders. Account deletion delivers the provisionally approved outcome using reviewed semantics.

**Verification:** Verify a departure/removal revokes access while preserving named past attribution, and a rejoin requires fresh approval with appropriate retained rotation state. Verify owner transfer and owner-only destructive group deletion. After the technical/privacy review is approved, verify account deletion revokes active participation and anonymizes personal history across every affected feature according to that reviewed policy.

**Coverage:** D03–D04, D11, D13. Depends on M1–M5 and completion of the account-deletion review. This milestone is required for v1.

## M7. Existing-group migration and pilot

**Outcome:** The owner reviews and approves the one-time migration, including movie/title matching, time corrections, participant attribution, existing interest votes, partial attendance, upcoming reservations, and current-round initialization. ScreenTime becomes the group's main record.

**Verification:** Reconcile the approved migration preview with imported history, participants, suggestions, votes, totals, and planned nights. Verify the source workbook is unchanged, completed totals exclude future assignments, and accountless participants can be linked later without losing imported state. Use the migrated group to exercise planning, selection, attendance, completion, and exceptions on both phones and desktops.

**Coverage:** D01–D02, D05, D07–D14. Depends on M1–M6. The PRD should specify pilot acceptance criteria; no fixed number of pilot nights has been agreed.

## Complete scope coverage

Decision IDs refer to [DISCOVERY_DECISIONS.md](DISCOVERY_DECISIONS.md). Features spanning milestones require their final integrated behavior; an early partial slice does not complete the requirement.

| Decision | Delivery or review coverage |
| --- | --- |
| D01 Product and delivery | All milestones; responsive use throughout; real-group pilot in M7 |
| D02 Accounts, participants, links | M1; preservation with history/migration in M4 and M7 |
| D03 Private groups and admission | M1; departure/rejoin integration in M6 |
| D04 Group management and ownership | M1 management; M6 transfer and deletion |
| D05 Flexible calendar | M3; real schedule migration in M7 |
| D06 Event authority and readiness | M3; picker movie permissions in M4 |
| D07 RSVPs and attendance | M4; imported attendance in M7 |
| D08 Movie selection and identification | M2 catalog/manual entry; event use in M3–M4 |
| D09 Group rotation and rounds | M5 |
| D10 Reservations and completed credits | M4 manual credit/history; M5 reservation/round integration |
| D11 Eligibility and exceptions | M5; departure/rejoin in M6; starting state in M7 |
| D12 Watchlists and interest | M2; completion cleanup in M4; existing data in M7 |
| D13 History and lifecycle | M4 history; M6 lifecycle and reviewed account deletion |
| D14 Spreadsheet migration | M7 |
| D15 Recommendation compatibility and approved deferrals | Initial data-model review before implementation; personalized recommendations remain high-priority post-MVP |
| D16 Approval boundaries | PRD/technical planning gates and explicit review of any scope change |

## High-priority follow-up

Personalized group recommendations follow v1 as a high-priority feature. Technical planning must preserve the approved compatibility constraint from D15. Personal watchlists, personal viewing logs, ratings, and other recommendation inputs remain post-MVP work; they are not silently added to a v1 milestone. The other explicitly approved deferrals remain listed in the discovery record.
