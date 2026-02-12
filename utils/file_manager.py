
import os
import uuid

def save_photo(file_bytes: bytes) -> str:
    filename = f"media/{uuid.uuid4()}.jpg"
    with open(filename, "wb") as f:
        f.write(file_bytes)
    return filename

def generate_output_path() -> str:
    return f"media/{uuid.uuid4()}_output.jpg"
