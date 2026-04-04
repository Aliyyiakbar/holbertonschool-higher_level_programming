#!/usr/bin/python3
"""Multiply 2 matrices using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the product of 2 matrices."""
    a = np.array(m_a)
    b = np.array(m_b)

    return np.matmul(a, b)
