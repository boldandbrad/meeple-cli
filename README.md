# meeple-cli

[![build status](https://img.shields.io/github/actions/workflow/status/boldandbrad/meeple-cli/python-test.yml?branch=main&logo=github)](https://github.com/boldandbrad/meeple-cli/actions/workflows/python-test.yml?query=branch%3Amain)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pypi](https://img.shields.io/pypi/v/meeple-cli)](https://pypi.org/project/meeple-cli/)
[![downloads](https://img.shields.io/pypi/dm/meeple-cli)](https://pypistats.org/packages/meeple-cli)

<!-- [![codecov](https://codecov.io/gh/boldandbrad/meeple-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/meeple-cli) -->
<!-- [![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fmeeple-cli%2F)](https://boldandbrad.github.io/meeple-cli/) -->

**Local board game collection manager. Powered by
[BoardGameGeek](https://boardgamegeek.com).**

## Disclaimer

> Neither `meeple-cli` nor its maintainers are affiliated with
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

## Roadmap

See a list of already implemented features/changes in the
[Changelog](docs/changelog.md).

### Planned Features

- [ ] Verbose option on `meeple info` that includes additional info such as
      description, publishers, etc
- [ ] Export a collection to csv or another format -> `meeple export`
- [ ] Import a collection from a variety of formats -> `meeple import`

### Potential Features (May or may not happen)

- [ ] Ability to assign and manage personal ratings of board games/expansions
- [ ] Copy a collection -> `meeple copy`
- [ ] Copy option `-c` on most commands that allows you to interactively select
      and copy text from the command output (for grabbing IDs) - similar to yank
- [ ] Manage user preferences/configs -> `meeple config` stored at
      `~/.meeple/config.json` or something
  - [ ] Toggle colorized output
  - [ ] Set custom default output sorts
  - [ ] Set custom data location
- [ ] Show elegant data diffs on `meeple update` (individual board game stat
      changes/collection stat changes)
- [ ] Output pagination for long lists?
  - [ ] Ability to display only a given number of output rows
- [ ] Identify when changes have been made to a collection and an update has not
      occurred yet
- [ ] Service or job that runs once a day to automatically update local data
  - [ ] Ability to output graphs/visuals to show change in collections over time
  - [ ] Ability to output graphs/visuals to show a board game's changes on
        BoardGameGeek over time
- [ ] Ability to record and manage plays of board games - would be nuts.
  - [ ] Ability to calculate and surface play statistics for a board game
- [ ] Ability to interact with discord services to show that you are currently
      playing a board game?
- [ ] Ability to actually interact with BoardGameGeek user
      profile/settings/collections (not all currently possible via the API)

### Other Todos

- [ ] Unit tests
- [ ] Documentation site (via vitepress?)
- [ ] Homebrew formula (will be available
      [here](https://github.com/boldandbrad/homebrew-tap))
- [ ] Implement simple logging for debugging (local, not telemetry) (via
      loguru?)

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
