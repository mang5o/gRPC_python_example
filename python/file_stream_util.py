from python.proto.test_pb2 import FileChunk
CHUNK_SIZE = 1024 * 1024  # 1MB

def get_file_chunks(filename):
    with open(filename, 'rb') as f:
        while True:
            piece = f.read(CHUNK_SIZE);
            if len(piece) == 0:
                return
            yield FileChunk(file_bytes=piece)


def save_chunks_to_file(chunks, filename):
    print("Saved file in output -> " + filename)
    with open(filename, 'wb') as f:
        for chunk in chunks:
            f.write(chunk.file_bytes)