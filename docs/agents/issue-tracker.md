# Issue tracker: GitHub

Issues and specs live in GitHub Issues for `EvanKN9/screentime`.
Use the `gh` CLI with `--repo EvanKN9/screentime`.

## Conventions

- Before creating the first issue of a session, verify the target with
  `gh repo view --json nameWithOwner`.
- Create issues with `gh issue create --title "..." --body-file <path>`.
  Write multiline bodies to a temporary file.
- Read issues with `gh issue view <number> --json number,title,body,labels,comments`.
- List issues with `gh issue list`, adding state and label filters as needed.
- Apply or remove labels with `gh issue edit`.
- Add comments with `gh issue comment`; use `--body-file` for multiline text.
- Before closing an issue, post the resolution, then run `gh issue close`.
  Post the explanation separately even when the issue is already closed.
- Use native GitHub sub-issues and issue dependencies where available.
  Otherwise, place `Part of #<parent>` and `Blocked by: #<number>` references
  at the top of the child issue body.
- An issue is unblocked when every blocker is closed.

File issues only in the user's repo.

## Pull requests as a triage surface

**PRs as a request surface: no.**

## Skill operations

- “Publish to the issue tracker” means create a GitHub issue.
- “Fetch the relevant ticket” means read its GitHub issue and comments.
