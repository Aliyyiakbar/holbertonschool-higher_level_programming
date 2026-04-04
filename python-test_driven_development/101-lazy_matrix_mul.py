#!/usr/bin/python3
"""Multiply 2 matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the product of 2 matrices."""
    try:
        a = np.array(m_a)
        b = np.array(m_b)
    except ValueError as e:
        if str(e).startswith("setting an array element with a sequence"):
            raise ValueError("setting an array element with a sequence.")
        raise

    if a.ndim == 0 or b.ndim == 0:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if a.dtype.kind in "OUS" or b.dtype.kind in "OUS":
        return np.einsum('ij,jk->ik', a, b)

    return np.dot(a, b)
