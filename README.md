# wai-annotations-adams
wai.annotations module for ADAMS-related formats.

The manual is available here:

https://ufdl.cms.waikato.ac.nz/wai-annotations-manual/

## Format

[ADAMS](https://adams.cms.waikato.ac.nz/) reports are just [Java .properties](https://en.wikipedia.org/wiki/.properties)
files used for storing meta-data. Since these files do not store any type information, 
ADAMS reports store with each key-value pair of data an additional key-value pair that
contains the type information. As data types, the following are supported:

* `B`: boolean
* `N`: numeric (float or integer)
* `S`: string
* `U`: unknown (treated as string)

The data type appends `<TAB>DataType` to the key of the data pair. Here is an example:

```properties
# comments get ignored
A=some_kind_of_string
A\tDataType=S
B=20.0
B\tDataType=N
C=true
C\tDataType=B
```

In case of image classification, a single field in the report will hold the class label.

For object detection (bounding box or shape), each object groups its properties via a
common prefix. This is usually `Object.NNN.` with `NNN` an integer index for the object.

As suffixes the following are common:
* `x`: the left of the top-left corner of the bbox
* `y`: the top of the top-left corner of the bbox
* `width`: the width of the bbox
* `height`: the height of the bbox
* `poly_x` (optional): comma-separated list of x coordinates of the shape
* `poly_y` (optional): comma-separated list of y coordinates of the shape

All other suffixes are considered *meta-data* for an object. Object detection usually
stores the *label* in the `type` suffix.


## Plugins
### FROM-ADAMS-IC
Reads image classification annotations in the ADAMS report-format

#### Domain(s):
- **Image Classification Domain**

#### Options:
```
usage: from-adams-ic [-I FILENAME] [-i FILENAME] [-N FILENAME] [-n FILENAME] [--seed SEED] [-e FORMAT FORMAT FORMAT] -c FIELD

optional arguments:
  -I FILENAME, --inputs-file FILENAME
                        Files containing lists of input files (can use glob syntax)
  -i FILENAME, --input FILENAME
                        Input files (can use glob syntax)
  -N FILENAME, --negatives-file FILENAME
                        Files containing lists of negative files (can use glob syntax)
  -n FILENAME, --negative FILENAME
                        Files that have no annotations (can use glob syntax)
  --seed SEED           the seed to use for randomisation
  -e FORMAT FORMAT FORMAT, --extensions FORMAT FORMAT FORMAT
                        image format extensions in order of preference
  -c FIELD, --class-field FIELD
                        the report field containing the image class
```

### FROM-ADAMS-OD
Reads image object-detection annotations in the ADAMS report-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: from-adams-od [-I FILENAME] [-i FILENAME] [-N FILENAME] [-n FILENAME] [--seed SEED] [-e FORMAT FORMAT FORMAT] [-p PREFIXES [PREFIXES ...]]

optional arguments:
  -I FILENAME, --inputs-file FILENAME
                        Files containing lists of input files (can use glob syntax)
  -i FILENAME, --input FILENAME
                        Input files (can use glob syntax)
  -N FILENAME, --negatives-file FILENAME
                        Files containing lists of negative files (can use glob syntax)
  -n FILENAME, --negative FILENAME
                        Files that have no annotations (can use glob syntax)
  --seed SEED           the seed to use for randomisation
  -e FORMAT FORMAT FORMAT, --extensions FORMAT FORMAT FORMAT
                        image format extensions in order of preference
  -p PREFIXES [PREFIXES ...], --prefixes PREFIXES [PREFIXES ...]
                        prefixes to parse
```

### TO-ADAMS-IC
Writes image classification annotations in the ADAMS report-format

#### Domain(s):
- **Image Classification Domain**

#### Options:
```
usage: to-adams-ic -c FIELD [--annotations-only] -o PATH [--split-names SPLIT NAME [SPLIT NAME ...]] [--split-ratios RATIO [RATIO ...]]

optional arguments:
  -c FIELD, --class-field FIELD
                        the report field containing the image class
  --annotations-only    skip the writing of data files, outputting only the annotation files
  -o PATH, --output PATH
                        output directory to write files to
  --split-names SPLIT NAME [SPLIT NAME ...]
                        the names to use for the splits
  --split-ratios RATIO [RATIO ...]
                        the ratios to use for the splits
```

### TO-ADAMS-OD
Writes image object-detection annotations in the ADAMS report-format

#### Domain(s):
- **Image Object-Detection Domain**

#### Options:
```
usage: to-adams-od [--annotations-only] -o PATH [--split-names SPLIT NAME [SPLIT NAME ...]] [--split-ratios RATIO [RATIO ...]]

optional arguments:
  --annotations-only    skip the writing of data files, outputting only the annotation files
  -o PATH, --output PATH
                        output directory to write files to
  --split-names SPLIT NAME [SPLIT NAME ...]
                        the names to use for the splits
  --split-ratios RATIO [RATIO ...]
                        the ratios to use for the splits
```
