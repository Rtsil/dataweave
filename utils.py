import cv2
import numpy as np


def polygon_to_mask_cv2(polygon_coords, mask_shape):
    """
    Convert a polygon defined by its coordinates to a binary mask using OpenCV (cv2).

    Parameters:
    - polygon_coords: List of (x, y) coordinates defining the polygon.
    - mask_shape: Tuple defining the shape of the mask (height, width).

    Returns:
    - A binary mask with the same shape as mask_shape.
    """
    # Create an empty mask
    mask = np.zeros(mask_shape, dtype=np.uint8)

    # Convert the polygon coordinates to a format accepted by cv2
    pts = np.array(polygon_coords, dtype=np.int32)

    # Fill the polygon in the mask
    cv2.fillPoly(mask, [pts], color=1)

    return mask


def get_polygon_position_as_bbox_from_image(points):
    """
    Get polygons points and locate the polygon using bbox

    Parameters:
    - points: List of tuples representing points [(x1, y1), (x2, y2), ...]

    Returns:
    - Tuple representing the bounding box (x, y, w, h)
    """
    # Convert the list of tuples to a NumPy array for efficient operations
    points_array = np.array(points)

    # Use NumPy's min and max functions to compute the bounding box
    min_x, min_y = np.min(points_array, axis=0)
    max_x, max_y = np.max(points_array, axis=0)

    # Calculate width and height of the bounding box
    width = max_x - min_x
    height = max_y - min_y

    # Return bounding box coordinates as (x, y, w, h)
    return min_x, min_y, width, height


def compress_polygon_to_bbox(poly_points, bbox):
    # Convert the polygon points to a NumPy array for efficient operations
    poly_points_array = np.array(poly_points)

    # Get the bounding box coordinates
    min_x, min_y, width, height = bbox
    # Calculate the width and height of the bounding box

    # Compress each point relative to the bounding box
    compressed_points = [(point[0] - min_x, point[1] - min_y) for point in poly_points_array]

    return compressed_points


def mask_to_polygon_cv2(mask):
    """
    Convert a binary mask to a polygon using OpenCV (cv2).

    Parameters:
    - mask: Binary mask (numpy array) where 1 represents the foreground and 0 represents the background.

    Returns:
    - List of tuples representing the polygon vertices [(x1, y1), (x2, y2), ...]
    """
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Extract the polygon vertices from the first contour (assuming there's only one contour)
    if contours:
        contour = contours[0]
        polygon = [tuple(point[0]) for point in contour]
        return polygon
    else:
        return None


def decompress_polygon_from_bbox(compressed_points, bbox):
    """
    Decompresses polygon points from their bounding box relative coordinates.

    Parameters:
    - compressed_points: List of tuples representing compressed points [(x1', y1'), (x2', y2'), ...]
    - bbox: Bounding box coordinates (min_x, min_y, max_x, max_y)

    Returns:
    - List of tuples representing decompressed points [(x1, y1), (x2, y2), ...]
    """
    # Unpack the bounding box coordinates
    min_x, min_y, max_x, max_y = bbox

    # Decompress each point by adding the minimum x and y values of the bounding box
    decompressed_points = [(point[0] + min_x, point[1] + min_y) for point in compressed_points]

    return decompressed_points