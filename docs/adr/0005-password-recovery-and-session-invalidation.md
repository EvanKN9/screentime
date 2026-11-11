---
status: accepted
date: 2026-11-10
---

# Recover passwords by email code and invalidate all application sessions

The project owner approved recovery for email/password accounts through a code sent to the email address already verified on the account. After a valid code, the person chooses a new password; a successful reset invalidates every existing ScreenTime application session, including any session in the current browser. The recovery confirmation screen remains visible and offers normal sign-in, preserving the completed flow without keeping an authenticated application session or automatically signing the person in.

## Rationale and consequences

- Recovery proves access through an email address previously associated with and verified for the account. It resets the password rather than revealing the previous password.
- Invalidating all existing application sessions prevents a previously authenticated device from retaining access after the reset. Retaining the confirmation screen is a presentation choice and does not require retaining authenticated access.
- The trade-off is requiring normal sign-in again on every previously signed-in device, including the reset browser. The project owner explicitly chose this policy over preserving the current browser's authenticated session.
- [OWASP's password-recovery guidance](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html#user-resets-password) supports choosing a new password after recovery proof, returning to ordinary login, and addressing existing sessions. ScreenTime's decision is to invalidate all application sessions while retaining the confirmation flow.
- FR-001.AC8–AC11 record the approved outcomes. R-007 remains open for code expiration, retry/resend controls, delivery failures, loss of access to the verified email, email-verification timing, and other unresolved security policies. Established library/service defaults should be reviewed together for the remaining implementation settings.
- Authentication provider, code generation/storage, session mechanism, schema, and concrete security thresholds remain unselected. This decision does not change sign-in method linking, group-participant account links, group permissions, or the full v1 scope, and does not authorize application implementation.

See [FR-001](../PRD.md#fr-001--google-sign-in-and-emailpassword-registration-and-login), [R-007](../PRD.md#authentication-policy-questions-r-007), and [ADR 0004](0004-link-google-to-existing-password-account.md).
