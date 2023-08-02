# Python SVG to G-Code Converter
A fast svg to gcode compiler forked from [vishpat/svg2gcode](https://github.com/vishpat/svg2gcode).

This is CodeMonkey1100001001 fork. Note it is highly optimized for my homebrew Makelangelo polar plotter.

--------------

This library takes an svg file `location/my_file.svg` and outputs the gcode conversion to a folder in the same directory `location/gcode_output/my_file.gcode`.

The file `config.py` contains the configurations for the conversion (printer bed size etc).

## Installation
Simply clone this repo.
```
git clone https://github.com/CodeMonkey1100001001/py-svg2gcode_personal.git
```

## Usage
### As a Python module
To import it into your existing python project:
```python
import py-svg2gcode
```
or
```python
import generate_gcode from py-scvg2gcode
```
### As a Python Command
```
python3 ./svg2gcode.py ./filename.svg

## Details
The compiler is based on the eggbot project and it basically converts all of the SVG shapes into bezier curves. The bezier curves are then recursively sub divided until desired smoothness is achieved. The sub curves are then approximated as lines which are then converted into g-code.

### Usage Notes

```
This works fairly well with vpype. vpype likes to use a viewBox instead of using width and height. So care has to be taken to make sure svg2gcode.py is using the right dimensions.

vpype read infile.svg linesort write outfile.svg 

```
