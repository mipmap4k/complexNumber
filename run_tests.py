import unittest
import coverage

from unit_tests import TestComplexNum 
from rational import RationalNum

cov = coverage.Coverage()
cov.start()

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestComplexNum))

cov.stop()
cov.save()

cov.report()
