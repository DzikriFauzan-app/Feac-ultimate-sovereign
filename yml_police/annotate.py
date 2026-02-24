import sys
from pathlib import Path

def annotate(file, notes):
    ann = Path(file).with_suffix(".police.txt")
    with open(ann, "w") as f:
        f.write("YML POLICE NOTES\n")
        f.write("=================\n")
        for n in notes:
            f.write(f"- {n}\n")
    print(f"[ANNOTATION] {ann}")

if __name__ == "__main__":
    annotate(sys.argv[1], sys.argv[2:])
