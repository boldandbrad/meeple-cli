# bgg-cli

[![Build Status](https://api.travis-ci.com/boldandbrad/bgg-cli.svg?branch=main)](https://travis-ci.com/github/boldandbrad/bgg-cli)

<!-- [![codecov](https://codecov.io/gh/boldandbrad/bgg-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/bgg-cli) -->
<!-- [![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fbgg-cli%2F)](https://boldandbrad.github.io/bgg-cli/) -->
<!-- [![PyPI](https://img.shields.io/pypi/v/bgg-cli)](https://pypi.org/project/bgg-cli/) -->
<!-- ![PyPI - Downloads](https://img.shields.io/pypi/dm/bgg-cli) -->

> search [BoardGameGeek](https://boardgamegeek.com) and manage local board game collections from your terminal.

## Install

> Coming soon.

<!-- ```zsh
brew tap boldandbrad/homebrew-tap
brew install bgg-cli
```

or

```zsh
pipx install bgg-cli
```

or

```zsh
pip install bgg-cli
``` -->

<!-- > For more details, read the **bgg-cli** [install guide](https://boldandbrad.github.io/bgg-cli/#/install). -->

## Usage

```zsh
bgg
```

<!-- > For more usage details, read the **bgg-cli** [usage guide](https://boldandbrad.github.io/bgg-cli/#/usage). -->

## Roadmap

<!-- TODO: add link to changelog here -->

### Features

- [x] Search boardgamegeek for a game or expansion -> `bgg search`
- [x] Get and display detailed info for a boardgame or expansion -> `bgg info`
- [x] Open a game or expansion on boardgamegeek.com in browser -> `bgg open`
- [x] Display current boardgamegeek hotness list -> `bgg hot`
- [x] Create a new local collection -> `bgg new`
- [x] Add a game/expansion to a local collection -> `bgg add`
- [x] List all local collections -> `bgg collections`
- [x] List all games/expansions in a local collection -> `bgg list`
- [x] Drop a game/expansion from a local collection -> `bgg drop`
- [x] Delete a local collection -> `bgg delete`
- [x] Update local collection data with snapshot from bgg -> `bgg update`
- [x] Display average game stats for a collection -> `bgg stats`
- [x] Store local collection data in user's home directory
- [ ] Find games/expansions across local collections by attributes -> `bgg find`
- [ ] Rename a local collection -> `bgg rename`
- [ ] Copy a local collection -> `bgg copy`
- [x] Move a game/expansion from one local collection to another -> `bgg move`
- [ ] Export a local collection to csv or another format -> `bgg export`
- [ ] Import a local collection from a variety of formats -> `bgg import`
- [ ] Ability to sort listed outputs by a particular column
- [ ] Ability to display only a given number of rows
- [ ] Manage user preferences/configs -> `bgg config` stored at `~/.bgg/config.json` or something
  - [ ] Toggle colorized output
  - [ ] Set custom default output sorts
  - [ ] Set custom data location
- [ ] Show elegant data diffs on `bgg update` (individual game stat changes/collection stat changes)
- [ ] Output pagination for long lists?
- [ ] Identify when changes have been made to a collection and an update has not occurred yet

#### Long Shot Ideas (May or may not happen)

- [ ] Ability to assign and manage personal ratings to games/expansions
- [ ] Ability to record and manage plays of games - would be nuts.
  - [ ] Ability to calculate and surface play statistics for a game
- [ ] Ability to interact with discord services to show that you are currently playing a boardgame?
- [ ] Ability to actually interact with BGG.com user profile/settings/collections (not all currently possible via the API)

### Technical

- [ ] Implement simple logging for debugging (local, not telemetry) (via loguru?)
- [ ] Unit tests
- [ ] Documentation site (via vitepress?)
- [x] Linting (via [trunk](trunk.io))
- [ ] Convert to pyproject.toml build system (via flit?)
- [ ] CI/CD pipeline (via [travis](travis-ci.com))
- [ ] Deployed to pypi
- [ ] Pre-releases deployed to pypi-test
- [ ] Homebrew formula (will be available [here](https://github.com/boldandbrad/homebrew-tap))

## License

Copyright (c) 2022 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
