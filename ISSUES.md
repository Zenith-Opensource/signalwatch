# Assigned issues

# Classify check results

Checkout sometimes times out, yet the status report says healthy. Help the on-call developer distinguish a slow successful call from an outage and see how many incidents occurred.

Expected behavior: A missing status means timeout. A non-2xx response means error. A 2xx response over 500 ms is slow. Other successes are healthy.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing health examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


# Report recent latency

Checkout sometimes times out, yet the status report says healthy. Help the on-call developer distinguish a slow successful call from an outage and see how many incidents occurred.

Expected behavior: Return maximum valid latency among the last three checks in chronological input order. Negative latency is invalid. Return None for an empty valid window.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing peak examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


# Group failed checks

Checkout sometimes times out, yet the status report says healthy. Help the on-call developer distinguish a slow successful call from an outage and see how many incidents occurred.

Expected behavior: Given ordered booleans for a single endpoint (True means healthy), count distinct incidents. Open on the second consecutive failure, stay open until the next success.

Reproduce with python3 -m unittest -v from the track directory. Inspect the failing incidents examples and trace one input through demo.py. Add one fresh boundary regression and demonstrate the corrected output.


