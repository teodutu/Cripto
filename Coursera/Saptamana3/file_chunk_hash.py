import argparse
from hashlib import sha256
from os import path


TEST_FILE_NAME = "test_video.mp4"
TEST_BLOCK_SIZE = 1024
TEST_FILE_HASH = "03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8"


def _get_args():
	parser = argparse.ArgumentParser(
		description="This script is used to calculate the hash of a file by "
			"splitting it into blocks of a given size.")
	parser.add_argument("-f", "--file", dest="file_name", type=str, nargs="?",
		default="assignment_video.mp4",
		help="the file whose hash will be computed")
	parser.add_argument("-b", "--block-size", dest="block_size", type=int,
		nargs="?", default=TEST_BLOCK_SIZE,
		help="the size of the block in which the file will be split")

	return parser.parse_args()


def _get_chunked_file_hash(file_chunks, block_size):
	hash = b""

	for chunk in reversed(file_chunks):
		hash = sha256(chunk + hash).digest()

	return hash

def get_file_hash(file_name, block_size):
	with open(path.expanduser(file_name), "rb") as file:
		file_data = file.read()
		chunks = [file_data[i : i + block_size]
			for i in range(0, len(file_data), block_size)]
		return _get_chunked_file_hash(chunks, block_size)


if __name__ == "__main__":
	test_hash = get_file_hash(TEST_FILE_NAME, TEST_BLOCK_SIZE).hex()
	if test_hash == TEST_FILE_HASH:
		args = _get_args()
		print(f"The rolling block hash of file '{args.file_name}' with block "
			f"size {args.block_size} is:\n\t",
			get_file_hash(args.file_name, args.block_size).hex())
	else:
		print(f"ERROR: The hash of the test file '{TEST_FILE_NAME}' with block"
			f" size {TEST_BLOCK_SIZE} is incorrect:\n\t{test_hash} "
			f"instead of {TEST_FILE_HASH}.")
