"""Split the Bill: split a restaurant bill fairly between friends.

Money is always stored as whole cents (int), never float.
Example: $100.00 is 10000.
"""


def split_bill(total_cents: int, people: int) -> list[int]:
    """Split total_cents equally between people.

    If the total does not divide evenly, the first people
    pay one extra cent each, so every cent is paid.
    """
    base, leftover = divmod(total_cents, people)
    # The first `leftover` people pay one extra cent
    return [base + 1 if i < leftover else base for i in range(people)]


if __name__ == "__main__":
    shares = split_bill(10000, 3)  # $100.00 in cents
    print("Shares (cents):", shares)
    print("Total paid (cents):", sum(shares))
