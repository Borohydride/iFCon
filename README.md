# iFCon
A tool for handling iFAction resource file (iFCon file)

## Usage

```
positional arguments:  
  file                  The iFCon file to extract or pack.  

options:  
  -h, --help            show this help message and exit  
  -x, --extract         Extract the contents of an iFCon file.  
  -p PACK, --pack PACK  Pack the contents of a folder into an iFConfile.  
  -o OUTPUT, --output OUTPUT  
                        The output file for extracting the iFCon file.  
```

## Example

To extract the contents of an iFCon file, run the following command:

```
python iFCon.py <iFCon file> -x -o <output folder>
```

To pack the contents of a folder into an iFCon file, run the following command:

```
python iFCon.py <iFCon file> -p <folder>
```