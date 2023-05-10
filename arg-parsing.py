import argparse

parser = argparse.ArgumentParser(description="Script to concate string")
parser.add_argument('string',metavar='S', type=str, nargs='+'),
parser.add_argument('--concate',dest='concate',action='store_const',
                     const=sum,default=max,
                     help='sum the integers arguments')

# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.string))
