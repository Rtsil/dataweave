# DATAWEAVE 


A Python package for handling various data encoding and manipulation tasks, including run-length encoding (RLE), mask operations, and polygon manipulations.

## Installation

Install the package using pip:

```bash
pip install dataweave
```

## USAGE

###  Run-Length Encoding (RLE)

Use RLEHandler for encoding and decoding sequences of data using run-length encoding.


```python 
from dataweave import RLEHandler

# Example data
data = [0, 0, 1, 1, 1, 0, 0, 0, 1]

# Encode data using RLE
encoded = RLEHandler.encode(data)
print(encoded)  # Output: [(0, 2), (1, 3), (0, 3), (1, 1)]

# Decode the RLE encoded data
decoded = RLEHandler.decode(encoded)
print(decoded)  # Output: [0, 0, 1, 1, 1, 0, 0, 0, 1]
```


### Mask Operations
Use MaskHandler for converting between mask data and RLE encoding.
```python
from dataweave import MaskHandler

# Example mask data
mask_data = [[0, 0, 1], 
             [1, 1, 0], 
             [0, 0, 1]]

# Convert mask data to RLE
rle_encoded = MaskHandler.mask_to_rle(mask_data)
print(rle_encoded)
shape = (3, 3) # The shape of the mask data (height, width)
# Convert RLE back to mask data
decoded_mask = MaskHandler.rle_to_mask(rle_encoded, shape)
print(decoded_mask)
```
### Polygon Operations
Use PolygonHandler for converting between polygon vertices and RLE encoding as well as masks.

```python 
from dataweave import PolygonHandler

# Example polygon data (list of vertices)
data = [(100, 100),  # Vertex 1
        (200, 150),  # Vertex 2
        (250, 300),  # Vertex 3
        (180, 400),  # Vertex 4
        (120, 350)]  # Vertex 5

polyhandler = PolygonHandler()

# Convert polygon vertices to RLE and bounding box
rle, bbox = polyhandler.polygon_to_rle(data)
print(rle)

# Convert RLE and bounding box back to polygon vertices
polygon = polyhandler.rle_to_polygon(rle, bbox)
print(polygon)

mask = polyhandler.polygon_to_mask(data, shape=(height, width), color=(255,255,255))
print(mask)

# Convert mask back to polygon vertices
polygon_from_mask = polyhandler.mask_to_polygon(mask)
print(polygon_from_mask)
```
  
## License
This project is licensed under the MIT License - see the LICENSE file for details. 

## Additional Notes:

- Ensure the package is named appropriately, in this case, `dataweave`.
- If the package is to be published on PyPI, make sure to include all necessary files such as `setup.py`, `LICENSE`, and any other metadata files.
- Adjust the package name and module imports according to your actual package structure.


## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# Authors

**Tsilavo Tahina R.**

- Mail: rtsilavotahina@gmail.com
- Github: https://github.com/Rtsil
- Gitlab: https://gitlab.com/tsilavotahina