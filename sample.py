import os
import re

# Match files like 'args_kwargs_99.py'
pattern = re.compile(r"^(.+?)_(\d+)\.py$")

for filename in os.listdir():
    match = pattern.match(filename)
    if match:
        name = match.group(1)    # name part
        number = match.group(2)  # number part
        new_filename = f"{number}_{name}.py"  # number first, underscore, then name

        if os.path.exists(new_filename):
            print(f"Skipping {filename}, {new_filename} exists.")
        else:
            os.rename(filename, new_filename)
            print(f"Renamed: {filename} --> {new_filename}")
