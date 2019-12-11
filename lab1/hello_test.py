from hello import main

# capsys is a test fixture, which allows modular importing of common testing utilities
# see https://docs.pytest.org/en/latest/fixture.html for more information
def test_hello(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, instructor!\n"
