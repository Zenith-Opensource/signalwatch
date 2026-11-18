# SignalWatch

Checkout sometimes times out, yet the status report says healthy. Help the on-call developer distinguish a slow successful call from an outage and see how many incidents occurred.

Run these commands inside this folder (Python 3.9+, standard library only).

```sh
python3 demo.py
python3 -m unittest -v
```

The demo reads 6,000 synthetic JSONL records. Each record names an operation and its positional inputs. Edit the existing workflow module, keep passing cases green, and add a useful report of your choice. Demonstrate one record before and after your fix.

## Issue 1 · Classify check results

A missing status means timeout. A non-2xx response means error. A 2xx response over 500 ms is slow. Other successes are healthy.

## Issue 2 · Report recent latency

Return maximum valid latency among the last three checks in chronological input order. Negative latency is invalid. Return None for an empty valid window.

## Issue 3 · Group failed checks

Given ordered booleans for a single endpoint (True means healthy), count distinct incidents. Open on the second consecutive failure, stay open until the next success.

## How to contribute

See [CONTRIBUTING.md](CONTRIBUTING.md) for the fork, branch and pull request workflow.

Complete [approach.md](approach.md), [challenges.md](challenges.md) and [optimizations.md](optimizations.md).
