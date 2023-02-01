import argparse
import re
from pathlib import Path

TAB = " " * 4


def make_kebab_case(text):
    text = text.lower()
    text = re.sub(r"\W", "-", text)
    text = text.replace("--", "-").strip("-")
    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automatically generates an index based on markdown headers."
    )
    parser.add_argument("file", type=Path, help="The file to generate the index for.")
    parser.add_argument(
        "--numbering",
        action="store_true",
        help="Optional: Activate this flag to use numbering in the index instead of bullet points.",
    )

    args = parser.parse_args()

    index = []
    with open(args.file) as f:
        for line in f:
            if line.startswith("#"):
                level = len(line.split()[0])
                index.append(
                    {
                        "name": line.split(" ", 1)[-1].split(":")[0].strip(),
                        "level": level,
                    }
                )

    for item in index:
        level = item["level"]
        name = item["name"]
        print(f"{TAB * (level - 1)}- [{name}](#{make_kebab_case(name)})")
