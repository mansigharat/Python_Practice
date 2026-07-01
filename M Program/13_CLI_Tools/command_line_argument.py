import argparse

parser = argparse.ArgumentParser(description="Run an agent task")
parser.add_argument("prompt", type=str, help="The task for the agent")
parser.add_argument("--model", type=str, default="claude-sonnet-4-6")
parser.add_argument("--max-steps", type=int, default=10)
parser.add_argument("--verbose", action="store_true")

args = parser.parse_args()

print(f"Running: {args.prompt}")
print(f"Model: {args.model}, Max steps: {args.max_steps}")
if args.verbose:
    print("Verbose mode on")