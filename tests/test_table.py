from toyro.table import Table


def test_table():
    table = Table(4, 4)
    assert table.is_coord_valid(1,1) == True
    assert table.is_coord_valid(4,4) == False
    assert table.is_coord_valid(0,4) == False
    assert table.is_coord_valid(-1,-1) == False