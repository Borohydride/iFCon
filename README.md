# iFCon
A tool for handling iFAction resource file (iFCon file)

## Usage

You can directly run iFCon.py or install this module with pip:

```bash
git clone https://github.com/Borohydride/iFCon.git
pip install ./iFCon
```

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
python3 iFCon.py <iFCon file> -x -o <output folder>
```
or
```
iFCon <iFCon file> -x -o <output folder>
```

To pack the contents of a folder into an iFCon file, run the following command:

```
python3 iFCon.py <iFCon file> -p <folder>
```
or
```
iFCon <iFCon file> -p <folder>
```