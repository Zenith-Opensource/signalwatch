# Start here · SignalWatch

**Difficulty** · Intermediate · upper. HTTP classification, a rolling window, and incident transitions.

1. Read [README.md](README.md) for the problem and [ISSUES.md](ISSUES.md) for the three assigned bugs.
2. Fork this repository, clone your fork, and create a solution branch. Open the cloned repository root in your terminal.
3. Use Python 3.9 or newer. No packages need to be installed.

```sh
python3 demo.py
python3 -m unittest discover -v
```

On Windows, use `py -3` in place of `python3` if needed. The demo processes 6,000 synthetic records. The initial test run should report **300 tests, 250 intentional assertion failures, and 50 passes**. An import error or zero discovered tests indicates a setup problem. Confirm that your terminal is in the folder containing `demo.py` and all three test modules.

4. Investigate the failures in `test_contract.py`, `test_extended_contract.py`, and `test_scale_contract.py`. Trace failures to the responsible functions in `workflows.py`. Keep the supplied tests and dataset intact. Fix the three assigned bugs, implement one useful feature, and add regression tests.
5. Follow [CONTRIBUTING.md](CONTRIBUTING.md). Complete the three required Markdown templates in your submission folder, include before/after test results, and open a pull request from your fork into this repository's `main` branch. Reference the corresponding sections in [ISSUES.md](ISSUES.md).
