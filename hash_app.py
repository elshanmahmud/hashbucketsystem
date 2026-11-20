import sys 
from pathlib import Path
import mmh3

n = 0
s = 0

def checkargs():
    global n,s
    if len(sys.argv)!=3:
        print("Enter arguements n and s correctly pls")
        sys.exit()

    try:
        n = int(sys.argv[1])
        s = int(sys.argv[2])
    except ValueError:
        print("n and s must be numbers")
        sys.exit()
    if n <= 0 or s < 0:
        print("n must be greater than 0 and s cannot be less than 0")
        sys.exit()

def create_bucket_files():
    buckets_dir = Path("buckets")
    buckets_dir.mkdir(parents=True, exist_ok=True)

    for i in range(1,1+n):
        bucket_path = buckets_dir / f"{i}.txt"
        with open(bucket_path, "w") as file:
            file.write(f"")


def mark_full(target_file: str):
    path = Path(target_file)
    content = path.read_text(encoding="utf-8")
    if not content.endswith("+"):
        path.write_text(content + "+", encoding="utf-8")

def is_full(target_file: str, extra_len: int = 0) -> bool:
    bucket_file = Path(target_file)
    if not bucket_file.exists():
        return False
    content = bucket_file.read_text(encoding="utf-8").rstrip("+")
    return len(content) + extra_len > s

def create_overflow(target_file: str, index: int) -> str:
    base_path = Path(target_file)
    overflow_path = base_path.parent / f"{base_path.stem}_{index}.txt"
    if not overflow_path.exists():
        overflow_path.write_text("", encoding="utf-8")
    return str(overflow_path)


def save_word_into_bucket(word: str, target_file: str):
    idx = 1
    current_file = target_file

    while is_full(current_file, len(word)):
        mark_full(current_file)
        current_file = create_overflow(target_file, idx)
        idx += 1

    bucket_file = Path(current_file)
    content = bucket_file.read_text(encoding="utf-8").rstrip("+")
    updated = content + word
    bucket_file.write_text(updated, encoding="utf-8")

    if len(updated) == s:
        mark_full(current_file)

    print(f"{word} added to {current_file}")


def get_inputs():
    global n,s
    while(True):
        try:
            word = input("Please enter the string: ")
            if len(word) > s:
                print("The word you enter cannot be bigger than than the bucket size")
            else:
                hashed = mmh3.hash(word)
                target_file = "buckets/"+str((hashed % n)+1)+".txt"
                save_word_into_bucket(word,target_file)
        except KeyboardInterrupt:
            print("\nSee you again")
            break

def main():
    checkargs()
    create_bucket_files()
    get_inputs()

main()