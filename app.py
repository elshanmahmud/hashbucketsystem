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

    if(n<0 or s<0):
        print("n or s cannot be less that 0")
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

def save_word_into_bucket(word:str,target_file:str):
    bucket_file = Path(target_file)
    content = bucket_file.read_text(encoding="utf-8")
    # not ready yet
    if(len(content)+len(word)>s):
        ...
    with bucket_file.open("a", encoding="utf-8") as f:
        f.write(word)
    content = bucket_file.read_text(encoding="utf-8")
    

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
                print(word + " added to "+target_file)
                save_word_into_bucket(word,target_file)
        except KeyboardInterrupt:
            print("\nSee you again")
            break

def main():
    checkargs()
    create_bucket_files()
    get_inputs()

main()