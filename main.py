
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--number", type=str, required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    print("answer is")
    print(args.number+1)
