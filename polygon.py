
from .utils import polygon_to_mask_cv2, get_polygon_position_as_bbox_from_image, compress_polygon_to_bbox, mask_to_polygon_cv2, decompress_polygon_from_bbox
from .mask import MaskHandler


class PolygonHandler:
    """Class for handling mask-related operations."""

    @staticmethod
    def polygon_to_rle(points):
        """Convert a polygon to RLE format."""
        x, y, w, h = get_polygon_position_as_bbox_from_image(points)

        compressed_points = compress_polygon_to_bbox(points, (x, y, w, h))
        print(compressed_points)
        mask = polygon_to_mask_cv2(polygon_coords=compressed_points, mask_shape=(h, w))
        rle = MaskHandler.mask_to_rle(mask)
        return rle, (x, y, w, h)

    @staticmethod
    def rle_to_polygon(rle, bbox):
        """Convert RLE data back to a polygon."""
        shape = bbox[3], bbox[2]
        mask = MaskHandler.rle_to_mask(rle, shape=shape)
        polygon_points = mask_to_polygon_cv2(mask)
        decompressed_points = decompress_polygon_from_bbox(polygon_points, bbox)
        return decompressed_points


    @staticmethod
    def polygon_to_mask(points, shape):
        """Create a binary mask from a polygon."""
        return polygon_to_mask_cv2(points, shape)

    @staticmethod
    def mask_to_polygon(mask):
        """Create a polygon from mask"""
        return mask_to_polygon_cv2(mask)