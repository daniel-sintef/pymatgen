"""Created on Jan 24, 2012."""

from __future__ import annotations

from pymatgen.core.structure import Structure
from pymatgen.io.cssr import Cssr
from pymatgen.util.testing import TEST_FILES_DIR, VASP_IN_DIR

__author__ = "Shyue Ping Ong"
__copyright__ = "Copyright 2012, The Materials Project"
__version__ = "0.1"
__maintainer__ = "Shyue Ping Ong"
__email__ = "shyuep@gmail.com"
__date__ = "Jan 24, 2012"

TEST_DIR = f"{TEST_FILES_DIR}/io/cssr"


class TestCssr:
    def setup_method(self):
        filepath = f"{VASP_IN_DIR}/POSCAR"
        self.cssr = Cssr(Structure.from_file(filepath))

    def test_str(self):
        expected_string = """10.4118 6.0672 4.7595
90.00 90.00 90.00 SPGR =  1 P 1    OPT = 1
24 0
0 Fe4 P4 O16
1 Fe 0.2187 0.7500 0.4749
2 Fe 0.2813 0.2500 0.9749
3 Fe 0.7187 0.7500 0.0251
4 Fe 0.7813 0.2500 0.5251
5 P 0.0946 0.2500 0.4182
6 P 0.4054 0.7500 0.9182
7 P 0.5946 0.2500 0.0818
8 P 0.9054 0.7500 0.5818
9 O 0.0434 0.7500 0.7071
10 O 0.0966 0.2500 0.7413
11 O 0.1657 0.0461 0.2854
12 O 0.1657 0.4539 0.2854
13 O 0.3343 0.5461 0.7854
14 O 0.3343 0.9539 0.7854
15 O 0.4034 0.7500 0.2413
16 O 0.4566 0.2500 0.2071
17 O 0.5434 0.7500 0.7929
18 O 0.5966 0.2500 0.7587
19 O 0.6657 0.0461 0.2146
20 O 0.6657 0.4539 0.2146
21 O 0.8343 0.5461 0.7146
22 O 0.8343 0.9539 0.7146
23 O 0.9034 0.7500 0.2587
24 O 0.9566 0.2500 0.2929"""
        assert str(self.cssr) == expected_string

    def test_from_file(self):
        filename = f"{TEST_DIR}/Si.cssr"
        cssr = Cssr.from_file(filename)
        assert isinstance(cssr.structure, Structure)
