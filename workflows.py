def health(status, latency):
    return "healthy" if status == 200 else "error"

def peak(samples):
    return max(samples, default=None)

def incidents(checks):
    return checks.count(False)
