
# activate venv
venv:
    . .venv/bin/activate

# install meeple-cli
install:
    pip install flit
    flit install

# install editable
dev-install:
    pip install -e .

# lint and format
lint:
    pre-commit run --all-files

# run all tests
test: install
    pytest

# run all tests with coverage
test-cov: install
    pytest --cov-report=xml --cov=./src/meeple/

# build dist
build:
    flit build

# generate homebrew formula
brew: install
    poet -f meeple-cli >> formula.rb

# check code and deps for vulns
# snyk doesn't currently support flit project with pyproject.toml
# deps:
#     snyk test --file=pyproject.toml

# remove artifacts
# TODO: remove __pycache__ dirs from src/ and tests/
cleanup:
    rm -f .coverage
    rm -f coverage.xml
    rm -f formula.rb
    rm -rf .pytest_cache
    rm -rf build
    rm -rf dist
    rm -rf *.egg-info
    rm -rf .ruff_cache
