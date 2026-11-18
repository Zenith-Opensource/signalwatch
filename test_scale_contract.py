"""Additional contract cases with passing controls for each tagged workflow."""

import unittest

import workflows


def scenarios(i):
    status = 201 + i % 45 if i >= 5 else 503
    latency = 501 + i if i % 2 else 500
    yield "health", (status, latency), "error" if i < 5 else ("slow" if latency > 500 else "healthy")
    recent = [i, i + 1, i + 2]
    yield "peak", (recent if i < 5 else [900 + i, -1, *recent],), i + 2
    checks = [True] * (i + 1)
    if i >= 5:
        checks += [False] * (i % 9 + 3) + [True, False, False]
    yield "incidents", (checks,), 0 if i < 5 else 2

def load_tests(loader, standard_tests, pattern):
    suite = unittest.TestSuite()
    for index in range(50):
        for operation, arguments, expected in scenarios(index):
            def check(operation=operation, arguments=arguments, expected=expected):
                actual = getattr(workflows, operation)(*arguments)
                unittest.TestCase().assertEqual(actual, expected, f"{operation}{arguments!r}")

            suite.addTest(unittest.FunctionTestCase(check, description=f"{operation}_scale_{index + 1:02d}"))
    return suite
