def vaccine_filter(func):
    immunoglobulins[:] = list(filter(func, immunoglobulins))