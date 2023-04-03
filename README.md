# meeple-cli

[![build status](https://img.shields.io/github/actions/workflow/status/boldandbrad/meeple-cli/python-test.yml?branch=main&logo=github)](https://github.com/boldandbrad/meeple-cli/actions/workflows/python-test.yml?query=branch%3Amain)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![pypi](https://img.shields.io/pypi/v/meeple-cli)](https://pypi.org/project/meeple-cli/)
![downloads](https://img.shields.io/pypi/dm/meeple-cli)

<!-- [![codecov](https://codecov.io/gh/boldandbrad/meeple-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/meeple-cli) -->
<!-- [![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fmeeple-cli%2F)](https://boldandbrad.github.io/meeple-cli/) -->

**Local board game collection manager. Powered by [BoardGameGeek](https://boardgamegeek.com).**

> `meeple-cli` allows you to create and manage _local_ board game collections
> stored on your system. At this time the [BoardGameGeek API](https://boardgamegeek.com/wiki/page/BGG_XML_API2)
> does not allow for creation nor modification of GeekLists directly. Nor is
> `meeple-cli` affiliated with BoardGameGeek.

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

<!-- > For more details, read the **meeple-cli** [install guide](https://boldandbrad.github.io/meeple-cli/#/install). -->

## Usage

```sh
$ meeple --help
Usage: meeple [OPTIONS] COMMAND [ARGS]...

  Local board game collection manager. Powered by BoardGameGeek.

Options:
  -h, --help     Show this message and exit.
  -v, --version  Show the version and exit.

Commands:
  add          Add a board game/extension to a collection.
  collections  List all local collections.
  delete       Delete a local collection.
  drop         Remove a board game/extension from a collection.
  hot          Retrieve the current BoardGameGeek hotness list.
  info         Print out the details of a board game or expansion.
  list         List all board games/extensions in a collection.
  move         Move a board game/extension from one collection to another.
  new          Create a new local collection.
  open         Open a board game or expansion on the BoardGameGeek website.
  rename       Rename a local collection.
  search       Search BoardGameGeek for a board game or expansion.
  stats        Print out the details of a local collection.
  update       Update local collection data.
```

<!-- > For more usage details, read the **meeple-cli** [usage guide](https://boldandbrad.github.io/meeple-cli/#/usage). -->

## Roadmap

See a list of already implemented features/changes in the [Changelog](docs/changelog.md).

### Planned Features

- [ ] Find board games/expansions across local collections by attributes ->
      `meeple find`
- [ ] Verbose option on `meeple info` that includes additional info such as
      description, publishers, etc
- [ ] Copy a local collection -> `meeple copy`
- [ ] Export a local collection to csv or another format -> `meeple export`
- [ ] Import a local collection from a variety of formats -> `meeple import`
- [ ] Ability to assign and manage personal ratings of board games/expansions

### Potential Features (May or may not happen)

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
- [ ] Shell completions for common shells? For finding/searching.

### Other Todos

- [ ] Unit tests
- [ ] Documentation site (via vitepress?)
- [ ] Homebrew formula (will be available [here](https://github.com/boldandbrad/homebrew-tap))
- [ ] Implement simple logging for debugging (local, not telemetry) (via
      loguru?)

## License

Copyright (c) 2023 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
