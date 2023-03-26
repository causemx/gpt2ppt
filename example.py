from gpt2ppt.gpt2ppt import generate
from argparse import ArgumentParser as ap

if __name__ == "__main__":
    parser = ap(description="gpt2ppt commands")
    parser.add_argument("input_file", help=".txt, format:[question],[topic]")
    parser.add_argument("-o", "--output_file", help="output destination path (folder)")
    args = parser.parse_args()
    error_code = generate(args)
    if error_code != 0:
        print("exit...")
        exit(error_code)