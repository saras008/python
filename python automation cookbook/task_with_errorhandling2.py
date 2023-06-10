import argparse
import sys
import logging

LOG_FORMAT = '%(ascitime)s %(name)s %(levelname)s %(message)s'
LOG_LEVEL = logging.DEBUG

def main(number,other_number,output):
    result = number * other_number
    print(f'The result is {result}', file=output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1',type=int, help='A number',default=2)
    parser.add_argument('-n2',type=int,help='Another number',default=2)
    parser.add_argument('-o',type=argparse.FileType('w'),help='The output',default=sys.stdout)
    parser.add_argument('-l',dest='log',type=str,help='log file',default=None)

    args = parser.parse_args()

    if args.log:
        logging.basicConfig(format=LOG_FORMAT,filename=args.log,loglevel=LOG_LEVEL)
    else:
        logging.basicConfig(format=LOG_FORMAT,loglevel=LOG_LEVEL)
    try:
        main(args.n1,args.n2,args.output)
    except Exception as exc:
        logging.exception('Error running task')
        exit(1)
