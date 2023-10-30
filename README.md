# meeple-cli

[![build status](https://img.shields.io/github/actions/workflow/status/boldandbrad/meeple-cli/python-test.yml?branch=main&logo=github)](https://github.com/boldandbrad/meeple-cli/actions/workflows/python-test.yml?query=branch%3Amain)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![codecov](https://codecov.io/gh/boldandbrad/meeple-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/meeple-cli)
[![pypi](https://img.shields.io/pypi/v/meeple-cli)](https://pypi.org/project/meeple-cli/)
[![downloads](https://img.shields.io/pypi/dm/meeple-cli)](https://pypistats.org/packages/meeple-cli)

<!-- [![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fmeeple-cli%2F)](https://boldandbrad.github.io/meeple-cli/) -->

**Local board game collection manager. Powered by
[BoardGameGeek](https://boardgamegeek.com).**

> Disclaimer: Neither `meeple-cli` nor its maintainers are affiliated with
> [BoardGameGeek](https://boardgamegeek.com).

## Install

Via [Homebrew](https://brew.sh) (Recommended on macOS/Linux)

```zsh
brew tap boldandbrad/tap
brew install meeple-cli
```

Via [pipx](https://pypa.github.io/pipx/) (Recommended on Windows):

```sh
pipx install meeple-cli
```

Via `pip`:

```sh
pip install meeple-cli
```

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
  add          Add items to a collection.
  collections  List all collections.
  delete       Delete collections.
  drop         Drop items from a collection.
  find         Search collections for items.
  list         List contents of a collection.
  move         Move an item from one collection to another.
  new          Create new collections.
  rename       Rename a collection.
  stats        View collection statistics.
  update       Update collection data.

BoardGameGeek Commands:
  hot     List current BoardGameGeek trending items.
  import  Import BoardGameGeek user collections.
  info    View item details.
  open    Open an item on BoardGameGeek.
  search  Search BoardGameGeek for items.

Other Commands:
  completions  Setup meeple shell completions.
```

<!-- > For more usage details, read the **meeple-cli**
> [usage guide](https://boldandbrad.github.io/meeple-cli/#/usage). -->

### Completions

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

## Resources

- [Changelog](docs/changelog.md) - See a history of implemented features/changes.
- [Roadmap](https://github.com/boldandbrad/meeple-cli/milestones) - See a list of planned features and milestones.
- [FAQ](docs/faq.md) - Find answers to common questions.
- [Contributor Guide](docs/contributing.md) - Find out how to get involved.

## License

Copyright (c) 2023 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
