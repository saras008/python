import argparse
import configparser

def main(number,other_number):
    result = number * other_number
    print("The result is {}".format(result))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1',type=int, help='A number',default=1)
    parser.add_argument('-n2',type=int, help='Another number',default=1)
    parser.add_argument('--config','-c',type=argparse.FileType('r'),help='config file')

    args = parser.parse_args()

    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        args.n1 =int(config['ARGUE']['n1'])
        args.n2 =int(config['ARGUe']['n2'])
    main(args.n1,args.n2)
