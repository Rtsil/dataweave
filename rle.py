class RLEHandler:
    """Class for handling Run-Length Encoding operations."""

    @staticmethod
    def encode(data):
        """Encode a binary list using Run-Length Encoding (RLE)."""
        if not data:
            return []

        encoded = []
        count = 1
        current = data[0]

        for element in data[1:]:
            if element == current:
                count += 1
            else:
                encoded.append((current, count))
                current = element
                count = 1
        encoded.append((current, count))
        return encoded

    @staticmethod
    def decode(encoded_data):
        """Decode RLE data back to a binary list."""
        decoded = []
        for value, count in encoded_data:
            decoded.extend([value] * count)
        return decoded