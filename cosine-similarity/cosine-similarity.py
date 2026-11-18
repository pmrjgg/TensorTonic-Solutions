import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    an = np.linalg.norm(a, ord=2)
    bn = np.linalg.norm(b, ord=2)
    if an == 0 or bn == 0: return 0.0
    return float(np.dot(a,b) / (an * bn))