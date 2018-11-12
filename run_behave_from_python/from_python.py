#!/usr/bin/env python3

from behave.__main__ import main as behave_main

TEST_DIR = "features"
TEST_SUFFIX = ".feature"


def run_behave(testname):
    """Run the Behave machinery, read overall test result, capture log file."""
    test_specification = "{dir}/{test}{suffix}".format(dir=TEST_DIR, test=testname,
                                                       suffix=TEST_SUFFIX)
    result = behave_main([test_specification])
    print("Test result: {result}:".format(result=result))


def main():
    run_behave("adder")


if __name__ == '__main__':
    main()
