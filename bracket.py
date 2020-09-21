# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here

            return stack.append(next)
            pass

        if next in ")]}":
            pos = )]}.index(next)
            # Process closing bracket, write your code here
            return stack.pop()

            pass


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
