from enum import Enum

class Color(Enum):
    BLURPLE = 0
    GREEN = 1
    YELLOW = 2
    FUSCHIA = 3
    RED = 4
    WHITE = 5
    BLACK = 6
    GRAY = 7


colors = {
    Color.BLURPLE: 0x5865F2,
    Color.GREEN: 0x57F287,
    Color.YELLOW: 0xFEE75C,
    Color.FUSCHIA: 0xEB459E,
    Color.RED: 0xED4245,
    Color.WHITE: 0xFFFFFF,
    Color.BLACK: 0x000000,
    Color.GRAY: 0x2C2F33
}