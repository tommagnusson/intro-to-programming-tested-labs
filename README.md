# Introduction to Programming - Abridged Labs with Testing

This repository implements at least partial solutions to most of the labs in introduction to programming, as well as [`pytest`](https://docs.pytest.org/en/latest/) unit tests.

Dependencies:
 - Python 3
 - [`pytest`](https://docs.pytest.org/en/latest/getting-started.html)

Included in each lab folder is a `README.md` which explains how my testing contributes to the labs, or an explanation of why there are not tests if that is the case.

## Running Tests

Run `program.py`'s test in `labN` folder:
```
pytest labN/program_test.py
```

Run all tests:
```
pytest
```

## Most testing-friendly labs

Lab 4 (account generator) and Lab 7 (tic tac toe) are two excellent candidates for testing.

Lab 4's `README.md` explains a recommended testing paradigm called Given-When-Then.

Lab 7 include lots of tests that clearly demonstrate why manual testing would be way slower than writing unit tests.

## Pytest resources

 - [Official Documentation](https://docs.pytest.org/en/latest/getting-started.html)
 - Excellent two part series on Pytest and good unit testing practices
    - [Python Testing 101 with pytest](https://youtu.be/etosV2IWBF0)
    - [Python Testing 201 with pytest](https://youtu.be/fv259R38gqc)