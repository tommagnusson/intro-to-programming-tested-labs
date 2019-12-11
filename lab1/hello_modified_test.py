from hello_modified import main

def test_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, instructor!\nGood-bye!\n"
