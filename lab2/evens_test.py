from evens import main

def test_evens(capsys):
    main()
    captured = capsys.readouterr()
    expected = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert captured.out == '\n'.join(map(str, expected)) + '\n'
