# meeple-cli

[![Build Status](https://img.shields.io/github/actions/workflow/status/boldandbrad/meeple-cli/python-test.yml?branch=main)](https://github.com/boldandbrad/meeple-cli/actions/workflows/python-test.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/boldandbrad/meeple-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/meeple-cli)

<!-- [![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fmeeple-cli%2F)](https://boldandbrad.github.io/meeple-cli/) -->

[![PyPI](https://img.shields.io/pypi/v/meeple-cli)](https://pypi.org/project/meeple-cli/)
![PyPI - Downloads](https://img.shields.io/pypi/dm/meeple-cli)

**Local board game collection manager. Powered by [BoardGameGeek](https://boardgamegeek.com).**

> `meeple-cli` allows you to create and manage _local_ board game collections stored on your system. At this time the [BoardGameGeek API](https://boardgamegeek.com/wiki/page/BGG_XML_API2) does not allow for creation nor modification of GeekLists directly.

## Install

> Coming soon.

<!-- ```zsh
brew tap boldandbrad/homebrew-tap
brew install meeple-cli
```

or

```zsh
pipx install meeple-cli
```

or

```zsh
pip install meeple-cli
``` -->

<!-- > For more details, read the **meeple-cli** [install guide](https://boldandbrad.github.io/meeple-cli/#/install). -->

## Usage

```zsh
meeple
```

<!-- > For more usage details, read the **meeple-cli** [usage guide](https://boldandbrad.github.io/meeple-cli/#/usage). -->

## Roadmap

See a list of already implemented features/changes in the [Changelog](docs/changelog.md).

### Features

- [x] Search BoardGameGeek for a board game or expansion -> `meeple search`
- [x] Get and display detailed info for a board game or expansion -> `meeple info`
- [x] Open a board game or expansion on BoardGameGeek in browser -> `meeple open`
- [x] Display current BoardGameGeek hotness list -> `meeple hot`
- [x] Create a new local collection -> `meeple new`
- [x] Add a board game/expansion to a local collection -> `meeple add`
- [x] List all local collections -> `meeple collections`
- [x] List all board games/expansions in a local collection -> `meeple list`
- [x] Drop a board game/expansion from a local collection -> `meeple drop`
- [x] Delete a local collection -> `meeple delete`
- [x] Update local collection data with snapshot from BoardGameGeek -> `meeple update`
- [x] Display average board game stats for a collection -> `meeple stats`
- [x] Store local collection data in user's home directory -> at `~/.meeple/`
- [ ] Find board games/expansions across local collections by attributes -> `meeple find`
- [ ] Rename a local collection -> `meeple rename`
- [ ] Copy a local collection -> `meeple copy`
- [x] Move a board game/expansion from one local collection to another -> `meeple move`
- [ ] Export a local collection to csv or another format -> `meeple export`
- [ ] Import a local collection from a variety of formats -> `meeple import`
- [ ] Ability to sort listed outputs by a particular column
- [ ] Ability to display only a given number of rows
- [ ] Manage user preferences/configs -> `meeple config` stored at `~/.meeple/config.json` or something
  - [ ] Toggle colorized output
  - [ ] Set custom default output sorts
  - [ ] Set custom data location
- [ ] Show elegant data diffs on `meeple update` (individual board game stat changes/collection stat changes)
- [ ] Output pagination for long lists?
- [ ] Identify when changes have been made to a collection and an update has not occurred yet

#### Long Shot Ideas (May or may not happen)

- [ ] Service or job that runs once a day to automatically update local data
  - [ ] Ability to output graphs/visuals to show change in collections over time
  - [ ] Ability to output graphs/visuals to show a board game's changes on BoardGameGeek over time
- [ ] Ability to assign and manage personal ratings to board games/expansions
- [ ] Ability to record and manage plays of board games - would be nuts.
  - [ ] Ability to calculate and surface play statistics for a board game
- [ ] Ability to interact with discord services to show that you are currently playing a board game?
- [ ] Ability to actually interact with BoardGameGeek user profile/settings/collections (not all currently possible via the API)
- [ ] Shell completions for common shells? For finding/searching.

### Technical

- [x] Convert to pyproject.toml build system (via [flit](flit.pypa.io))
- [x] Linting (via [trunk](trunk.io))
- [ ] Unit tests
- [ ] CI/CD pipeline (via [travis](travis-ci.com))
- [ ] Documentation site (via vitepress?)
- [ ] Pre-releases published to test pypi
- [ ] Publish v1.0.0 to pypi
- [ ] Homebrew formula (will be available [here](https://github.com/boldandbrad/homebrew-tap))
- [ ] Implement simple logging for debugging (local, not telemetry) (via loguru?)

## License

Copyright (c) 2022 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
