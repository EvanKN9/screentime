---
status: accepted
date: 2026-11-09
---

# Authenticate both methods before connecting Google to an existing password account

On 2026-11-09, the project owner approved the following rule for a person who first registered a password account and later uses Google sign-in with the same email. Connecting Google requires successful authentication with Google and to the existing ScreenTime account; after connection, either method can sign into that same account. If the person cannot authenticate to the existing account, stop that Google sign-in attempt without connecting Google or creating another account, leaving the existing account unchanged.

## Security rationale

Matching email addresses alone do not demonstrate control of the existing ScreenTime account. Connecting a sign-in method adds another way to access that account, so requiring both authentication checks reduces the risk of attaching an identity to an account its user does not control. [Auth0's account-linking precautions](https://auth0.com/docs/manage-users/user-accounts/user-account-linking#precautions) recommend authenticating both identities before linking; this source supports the rationale and does not select Auth0 as ScreenTime's provider.

Stopping the failed attempt prevents that flow from bypassing the required proof or silently creating a duplicate account. The trade-off is an additional authentication step when connecting Google and an inability to finish that connection without access to the existing account; password-recovery policy remains undecided.

## Consequences and boundaries

- The approved outcomes are FR-001.AC4–AC7. Existing requirement and acceptance-criterion identifiers are preserved.
- Both methods reach the same account with its existing memberships and history. Ordinary sign-in after connection does not require both methods every time; sensitive-action reauthentication remains open under R-007.
- **Sign-in method linking** connects methods to one account. An **account link** connects an account to an existing group participant under FR-006 and ADR 0001. This decision does not change participant linking, membership approval, or group permissions.
- R-007 is partially resolved. Recovery, unlinking, Google-first accounts later adding passwords, different-email linking, pre-existing duplicate accounts, email verification, and other security-related behavior still require approval.
- Authentication-proof implementation, provider, credential storage design, schema, and security thresholds remain unselected. This decision authorizes documentation of the approved behavior, not application implementation.

See [FR-001](../PRD.md#fr-001--google-sign-in-and-emailpassword-registration-and-login), [R-007](../PRD.md#authentication-policy-questions-r-007), [ADR 0001](0001-participation-without-accounts.md), and [ADR 0003](0003-support-google-and-email-password-sign-in.md).
