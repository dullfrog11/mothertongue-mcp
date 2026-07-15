from fastmcp import FastMCP
from quiz import create_quiz

mcp = FastMCP("MotherTong")


@mcp.tool()
def create_word_quiz(list_num: int) -> str:
    """단어장 시험 생성"""
    return create_quiz(list_num)


if __name__ == "__main__":
    mcp.run()