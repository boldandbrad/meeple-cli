
# activate venv
venv:
    . .venv/bin/activate

# install bgg-cli
install:
    pip install .

# install editable
dev:
    pip install -e .

# build dist
build:
    python setup.py sdist bdist_wheel

# generate homebrew formula
brew: install
    poet -f bgg-cli >> formula.rb

# lint and format
lint:
    trunk check

# check code and deps for vulns
deps:
    snyk test --file=setup.py

# run all tests
test: install
    pytest

# run all tests with coverage
test-cov: install
    pytest --cov-report=xml --cov=./bgg/

# remove artifacts
cleanup:
    rm -f .coverage
    rm -f coverage.xml
    rm -f formula.rb
    rm -rf .pytest_cache
    rm -rf build
    rm -rf dist
    rm -rf *.egg-info
    rm -rf bgg/__pycache__
    rm -rf tests/__pycache__