import sys
import os
from jinja2 import Environment, FileSystemLoader

teaser_number = sys.argv[1]
os.makedirs(teaser_number, exist_ok=True)

loader = FileSystemLoader("templates")
env = Environment(loader=loader)

with open(f"{teaser_number}/guess.md", "w") as f:
    f.write(env.get_template("guess.md").render())

with open(f"{teaser_number}/results.md", "w") as f:
    f.write(env.get_template("guess.md").render())
