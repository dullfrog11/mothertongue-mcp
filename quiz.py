import pandas as pd

# CSV 읽기
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent
CSV_PATH = BASE_DIR / "words.csv"

words = pd.read_csv(CSV_PATH)

# 단어장 가져오기
def get_word_list(list_num):
    start = (list_num - 1) * 100 + 1
    end = list_num * 100

    return words[(words["number"] >= start) & (words["number"] <= end)]


def create_quiz(list_num):
    word_list = get_word_list(list_num)

    quiz = ""

    for i, row in enumerate(word_list.itertuples(), start=1):
        quiz += f"{i}. {row.word}\n"
        quiz += "____________________\n\n"

    return quiz

print(create_quiz(1))