# meeple-cli

[![build status](https://img.shields.io/github/actions/workflow/status/boldandbrad/meeple-cli/python-test.yml?branch=main&logo=github)](https://github.com/boldandbrad/meeple-cli/actions/workflows/python-test.yml?query=branch%3Amain)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pypi](https://img.shields.io/pypi/v/meeple-cli)](https://pypi.org/project/meeple-cli/)
[![downloads](https://img.shields.io/pypi/dm/meeple-cli)](https://pypistats.org/packages/meeple-cli)

<!-- [![codecov](https://codecov.io/gh/boldandbrad/meeple-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/meeple-cli) -->
<!-- [![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fmeeple-cli%2F)](https://boldandbrad.github.io/meeple-cli/) -->

**Local board game collection manager. Powered by
[BoardGameGeek](https://boardgamegeek.com).**

> Disclaimer: Neither `meeple-cli` nor its maintainers are affiliated with
> [BoardGameGeek](https://boardgamegeek.com).

## Install

Global isolated install via [pipx](https://pypa.github.io/pipx/) (recommended):

```sh
pipx install meeple-cli
```

Local python environment install:

```sh
pip install meeple-cli
```

<!-- Homebrew install: -->

<!-- ```zsh
brew tap boldandbrad/homebrew-tap
brew install meeple-cli
```-->

<!-- > For more details, read the **meeple-cli**
> [install guide](https://boldandbrad.github.io/meeple-cli/#/install). -->

## Usage

```txt
$ meeple --help
Usage: meeple [OPTIONS] COMMAND [ARGS]...

  Local board game collection manager. Powered by BoardGameGeek.

Options:
  -h, --help     Show this message and exit.
  -v, --version  Show the version and exit.

Collection Commands:
  add          Add an item to a collection.
  collections  List all collections.
  delete       Delete a collection.
  drop         Remove an item from a collection.
  find         Search collections for items.
  list         List contents of a collection.
  move         Move an item from one collection to another.
  new          Create a new collection.
  rename       Rename a local collection.
  stats        Print out the details of a collection.
  update       Update local collection data.

BoardGameGeek Commands:
  hot     List current BoardGameGeek trending items.
  info    Print out the details of an item.
  open    Open an item on BoardGameGeek.
  search  Search BoardGameGeek for items.

Other Commands:
  completions  Setup meeple shell completions.
```

<!-- > For more usage details, read the **meeple-cli**
> [usage guide](https://boldandbrad.github.io/meeple-cli/#/usage). -->

## Completions

`meeple-cli` supports shell completions for `bash`, `zsh`, and `fish`. For
setup, use `meeple completions <SHELL>`, or the following instructions:

<details>
<summary>bash</summary>

Add the following to `~/.bashrc`:

```sh
eval "$(_MEEPLE_COMPLETE=bash_source meeple)"
```

</details>

<details>
<summary>zsh</summary>

Add the following to `~/.zshrc`:

```sh
eval "$(_MEEPLE_COMPLETE=zsh_source meeple)"
```

</details>

<details>
<summary>fish</summary>

Save the script to `~/.config/fish/completions/meeple.fish`:

```sh
_MEEPLE_COMPLETE=fish_source meeple > ~/.config/fish/completions/meeple.fish
```

</details>

## Changelog

See a history of implemented features/changes in the
[Changelog](docs/changelog.md).

## Roadmap

See a list of planned features and milestones
[here](https://github.com/boldandbrad/meeple-cli/milestones).

## FAQ

### Why local only collections?

Currently, the
[BoardGameGeek Public API](https://boardgamegeek.com/wiki/page/BGG_XML_API2)
provides limited _read-only_ data about user collections/GeekLists.

While it is _technically_ feasible to interface with GeekLists via
webscrapers/spiders, this kind of practice would be both complex and also
violate [BoardGameGeek Terms of Service](https://boardgamegeek.com/terms#toc22).

### Where does `meeple-cli` store data?

`meeple-cli` stores collection data in `~/.meeple` and only makes network
connections to retrieve data from the BoardGameGeek API.

## License

Copyright (c) 2023 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
