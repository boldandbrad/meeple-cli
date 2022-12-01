# meeple-cli

[![Build Status](https://api.travis-ci.com/boldandbrad/meeple-cli.svg?branch=main)](https://travis-ci.com/github/boldandbrad/meeple-cli)
[![codecov](https://codecov.io/gh/boldandbrad/meeple-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/meeple-cli)

<!-- [![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fmeeple-cli%2F)](https://boldandbrad.github.io/meeple-cli/) -->
<!-- [![PyPI](https://img.shields.io/pypi/v/meeple-cli)](https://pypi.org/project/meeple-cli/) -->
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/meeple-cli) -->

> manage your boardgame collection(s) from your terminal. powered by [BoardGameGeek](https://boardgamegeek.com).

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

<!-- TODO: add link to changelog here -->

### Features

- [x] Search boardgamegeek for a game or expansion -> `meeple search`
- [x] Get and display detailed info for a boardgame or expansion -> `meeple info`
- [x] Open a game or expansion on boardgamegeek.com in browser -> `meeple open`
- [x] Display current boardgamegeek hotness list -> `meeple hot`
- [x] Create a new local collection -> `meeple new`
- [x] Add a game/expansion to a local collection -> `meeple add`
- [x] List all local collections -> `meeple collections`
- [x] List all games/expansions in a local collection -> `meeple list`
- [x] Drop a game/expansion from a local collection -> `meeple drop`
- [x] Delete a local collection -> `meeple delete`
- [x] Update local collection data with snapshot from boardgamegeek -> `meeple update`
- [x] Display average game stats for a collection -> `meeple stats`
- [x] Store local collection data in user's home directory -> at `~/.meeple/`
- [ ] Find games/expansions across local collections by attributes -> `meeple find`
- [ ] Rename a local collection -> `meeple rename`
- [ ] Copy a local collection -> `meeple copy`
- [x] Move a game/expansion from one local collection to another -> `meeple move`
- [ ] Export a local collection to csv or another format -> `meeple export`
- [ ] Import a local collection from a variety of formats -> `meeple import`
- [ ] Ability to sort listed outputs by a particular column
- [ ] Ability to display only a given number of rows
- [ ] Manage user preferences/configs -> `meeple config` stored at `~/.meeple/config.json` or something
  - [ ] Toggle colorized output
  - [ ] Set custom default output sorts
  - [ ] Set custom data location
- [ ] Show elegant data diffs on `meeple update` (individual game stat changes/collection stat changes)
- [ ] Output pagination for long lists?
- [ ] Identify when changes have been made to a collection and an update has not occurred yet

#### Long Shot Ideas (May or may not happen)

- [ ] Ability to assign and manage personal ratings to games/expansions
- [ ] Ability to record and manage plays of games - would be nuts.
  - [ ] Ability to calculate and surface play statistics for a game
- [ ] Ability to interact with discord services to show that you are currently playing a boardgame?
- [ ] Ability to actually interact with boardgamegeek.com user profile/settings/collections (not all currently possible via the API)

### Technical

- [ ] Implement simple logging for debugging (local, not telemetry) (via loguru?)
- [ ] Unit tests
- [ ] Documentation site (via vitepress?)
- [x] Linting (via [trunk](trunk.io))
- [x] Convert to pyproject.toml build system (via [flit](flit.pypa.io))
- [ ] CI/CD pipeline (via [travis](travis-ci.com))
- [ ] Pre-releases deployed to test pypi
- [ ] Deploy v1.0.0 to pypi
- [ ] Homebrew formula (will be available [here](https://github.com/boldandbrad/homebrew-tap))

## License

Copyright (c) 2022 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
