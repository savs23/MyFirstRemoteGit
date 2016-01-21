import optparse, os

VERSION='0.1'

def print_hello(*args):
    for i in args:
        print i

parser=optparse.OptionParser(version='0.1', description='Some test program to show what is optparse module of Python')

parser.add_option('-f','--file', type='string', dest='file', help='Input file for additional data')

parser.add_option('-b','--buffer-size', action='store', choices=['512','4k','1m'], default='4k', help='Set buffer size for IO operations')

parser.add_option('-c','--coefficients', nargs=3, metavar='X Y Z', default=[0, 0, 0], help='User defined coefficients of start')

parser.add_option('-o', action='store_const', const=10, dest='output_level', help='Set output information level to above standart, for see additional information about work of program')
parser.add_option('-O', action='store_const', const=50, dest='output_level', help='Set output information level to maximum')

parser.add_option('-s','--silence', action='store_true', dest='silence', help='No print anything in stdout and stderr')

parser.add_option('-p','--panic', action='store_false', dest='standart_work', help='Abort from program if any working and error occured')

parser.add_option('-e','--exclude', action='append', type='int', dest='exclude_columns', help='Exclude for execution column from input file')

parser.add_option('-n','--nothing', action='append_const', const='Nothing', help='Nothing to do option')

parser.add_option('-P','--priority', action='count', dest='user_priorety', help='Increase priority of execution program on 1 point')

parser.add_option('--hello', action='callback', dest='help_string', nargs=1, callback=print_hello)

parser.add_option('--hidden_option', action='store_true', help=optparse.SUPPRESS_HELP)


options,arguments=parser.parse_args()

for key,value in options.__dict__.items():
    print key,'=',value
for i,item in enumerate(arguments):
    print 'argument #%s = %s'%(i,item)