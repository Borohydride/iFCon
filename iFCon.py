from iFConFile import iFConFile
import argparse

parser = argparse.ArgumentParser(description='iFCon - A tool for extracting and packing iFCon files.')
parser.add_argument('file', type=str, help='The iFCon file to extract or pack.')
parser.add_argument('-x', '--extract', action='store_true', help='Extract the contents of an iFCon file.')
parser.add_argument('-p', '--pack', type=str, help='Pack the contents of a folder into an iFCon file.')
parser.add_argument('-o', '--output', type=str, default='.\\output\\', help='The output folder for extracting the iFCon file.')

args = parser.parse_args()

if args.extract:
    ifc = iFConFile(args.file,'rb')
    ifc.extractAll(args.output)
    ifc.close()
elif args.pack:
    ifc = iFConFile(args.file,'wb')
    ifc.addfolder(args.pack)
    ifc.close()
else:
    parser.print_help() 