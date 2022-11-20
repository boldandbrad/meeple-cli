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
- [ ] Store local collection data in user's home directory
- [ ] Find a game/expansion in a collection by attributes -> `bgg find`
- [ ] Rename a local collection -> `bgg rename`
- [ ] Copy a local collection -> `bgg copy`
- [ ] Move a game/expansion from one local collection to another -> `bgg move`
- [ ] Export a local collection to csv or another format -> `bgg export`
- [ ] Ability to sort listed outputs by a particular column
- [ ] Manage user preferences/configs -> `bgg config`

### Technical

- [ ] Implement simple logging for debugging (local, not telemetry)
- [ ] Unit tests
- [ ] Documentation site
- [ ] CI/CD pipeline
- [ ] Deployed to pypi
- [ ] Homebrew formula (will be available [here](https://github.com/boldandbrad/homebrew-tap))

## License

Copyright (c) 2022 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
