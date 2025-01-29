import numpy as np
from generate_data import normal_distribution
import pytest
import sys


def test_normal_distribtion():
    rng = np.random.default_rng(seed=42)
    data = normal_distribution(rng, 0.0, 1.0, 10, 0)

    assert len(data) == 10


def test_that_fails():
    assert False


# Run the test
if __name__ == "__main__":
    n_failed = pytest.main(["-v", "tests.py"])
    sys.exit(n_failed)