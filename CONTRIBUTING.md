## Contribution guide

1. Fork the assigned repository. Use Code → Local to copy your fork URL. Run `git clone YOUR_FORK_URL`, enter the cloned folder and run `git switch -c evaluation/YOUR_HANDLE`.
2. Read this README. Run its demo and tests. Pick one failure and explain its user impact. Read the three issue files.
3. Fix all three issues. Implement one additional feature that helps a user make a decision. Add regression tests for each fix and your feature. Preserve supplied tests and input data.
4. Copy the root Markdown templates into `submissions/YOUR_HANDLE/`. Complete **approach.md**, **challenges.md** and **optimizations.md**. All three are compulsory. Record decisions as you work. Include an unsuccessful attempt or an honest account of what you checked, and distinguish measured improvements from ideas. Disclose any AI assistance in ai-usage.md.
5. Commit focused changes, push with `git push -u origin HEAD`, and open a PR against the organiser’s main branch. Reference the three assigned issues, give the exact demo command, before/after test results and one example output. Respond to review on the same branch. Submit the PR URL.
6. Demo the user problem, run one boundary case, explain a design decision and show the original feature. A local CLI demo is sufficient. A deployed preview is optional.

## Assessment

| Criterion | Marks | Evidence |
|---|---:|---|
| Codebase understanding | 15 | Trace an input from fixture through demo to result |
| Problem solving | 25 | Three issue fixes (15), reasoning and edge cases (5), useful original feature (5) |
| Working prototype | 25 | Reproducible setup (5), three workflows (15), feature demo (5) |
| Code quality | 15 | Readability (5), maintainability (5), focused Git changes (5) |
| Testing | 10 | Regression coverage (6), boundary cases and reproducible results (4) |
| Demo and communication | 10 | Clear demonstration (4), technical viva (3), documentation evidence (3) |

Code-only submissions are incomplete. Mentors check the three files before scoring.
