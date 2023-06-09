import argparse
import sys

def main(number,other_number,output):
    result = number / other_number
    print(f'The result is {result}',file=output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1',type=int, help='A number',default=4)
    parser.add_argument('-n2',type=int, help='Another number',default=2)
    parser.add_argument('--o',type=argparse.FileType('w'), help='Output file',default=sys.stdout)

    args = parser.parse_args()

    main(args.n1,args.n2,args.output)