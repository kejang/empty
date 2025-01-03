from empty.subpackage import sub_function1


def test_sub_function1(capsys):
    sub_function1()
    captured = capsys.readouterr()
    assert "Hello from submodule1!" in captured.out
