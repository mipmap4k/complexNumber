import unittest
import coverage

cov = coverage.Coverage()
cov.start()

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='unit_tests.py')  # 
    runner = unittest.TextTestRunner()
    runner.run(suite)

cov.stop()
cov.save()

cov.report()
