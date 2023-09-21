import argparse

from common.apitester import TestSequence

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="run_api_test")
    parser.add_argument('filename')
    args = parser.parse_args()
    test_seq = TestSequence(args.filename, req_names=[])
    test_seq.run()

