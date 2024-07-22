import sys
import iFConFile

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Usage: python iFConExtractor.py <ifcon file>")
        sys.exit(1)

    ifcon_file = sys.argv[1]

    iFConFile.iFConFile(ifcon_file).extractAll('.')
