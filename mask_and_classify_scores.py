import numpy as np


def mask_and_classify_scores(arr):
    if not isinstance(arr, np.ndarray):
        return None
    if arr.ndim != 2:
        return None
    n_rows, n_cols = arr.shape
    if n_rows != n_cols:
        return None
    if n_rows < 4:
        return None

    # done w vectorizing here and summarizing later
    # the tests were greeeeen so why not
    cleaned = arr.copy()
    cleaned[cleaned < 0] = 0
    cleaned[cleaned > 100] = 100

    levels = np.zeros_like(cleaned, dtype=int)
    levels[(cleaned >= 40) & (cleaned < 70)] = 1
    levels[cleaned >= 70] = 2

    row_pass_counts = np.zeros(n_rows, dtype=int)
    for i in range(n_rows):
        cound = 0
        for value in cleaned[i]:
            if value >= 50:
                cound += 1
        row_pass_counts[i] = cound

    return cleaned, levels, row_pass_counts
