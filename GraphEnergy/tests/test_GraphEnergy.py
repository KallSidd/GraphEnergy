"""
Unit and regression test for the GraphEnergy package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import GraphEnergy


def test_GraphEnergy_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "GraphEnergy" in sys.modules
