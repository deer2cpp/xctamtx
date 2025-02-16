import sys

def extract_jpeg_from_mtx(mtx_file, output_file):
    """Extracts a JPEG image from an MTX file and saves it."""
    try:
        with open(mtx_file, "rb") as file:
            data = file.read()
        
        # Locate JPEG start and end markers
        jpeg_start = data.find(b'\xFF\xD8')  # Start of Image (SOI)
        jpeg_end = data.rfind(b'\xFF\xD9')  # End of Image (EOI)
        
        if jpeg_start != -1 and jpeg_end != -1:
            jpeg_data = data[jpeg_start:jpeg_end + 2]
            
            with open(output_file, "wb") as img_file:
                img_file.write(jpeg_data)
            
            print(f"XctaMTX: Extracted JPEG saved as: {output_file}")
        else:
            print("XctaMTX: No valid JPEG data found in the MTX file.")
    except Exception as e:
        print(f"XctaMTX Runtime Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python XctaMTX.py <input.mtx> <output.jpg>")
    else:
        extract_jpeg_from_mtx(sys.argv[1], sys.argv[2])
