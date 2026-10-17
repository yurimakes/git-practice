# words.txt에 저장한 단어를 번호와 함께 출력한다.
from pathlib import Path

file_path = Path(__file__).parent / "words.txt"
words = file_path.read_text(encoding="utf-8").splitlines()

for number, word in enumerate(words, start=1):
    print(f"{number}. {word}")
