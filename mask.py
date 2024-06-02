import numpy as np


class MaskHandler:
    """Class for handling mask-related operations."""

    @staticmethod
    def mask_to_rle(mask):
        """Convert a binary mask to RLE format."""
        mask_array = np.array(mask)
        pixels = mask_array.flatten()
        rle = []
        last_pixel = pixels[0]
        count = 1

        for pixel in pixels[1:]:
            if pixel == last_pixel:
                count += 1
            else:
                rle.append((last_pixel, count))
                last_pixel = pixel
                count = 1
        rle.append((last_pixel, count))
        return rle

    @staticmethod
    def rle_to_mask(rle, shape):
        """Convert RLE data back to a binary mask."""

        mask = np.zeros(shape[0] * shape[1], dtype=np.uint8)
        current_pos = 0

        for value, count in rle:
            mask[current_pos:current_pos + count] = value
            current_pos += count

        return mask.reshape(shape)
