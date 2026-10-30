from split_bill import split_bill


def test_shares_add_up_to_total():
    shares = split_bill(10000, 3)
    assert sum(shares) == 10000
