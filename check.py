import argparse

parser = argparse.ArgumentParser(description="Check files in a folder")
parser.add_argument("folder", help="which folder to check")
parser.add_argument("--extension", default=".py", help="which file type")

args = parser.parse_args()

print(f"Checking {args.folder} for {args.extension} files")