# Changelog

All notable changes to **euchre-cli** will be documented here.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/ "Keep a Changelog"),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html "Semantic Versioning").

## Unreleased

### Added

#### Boardgamegeek.com

- Search boardgamegeek for a game or expansion via `bgg search`
- Get and display detailed info for a boardgame or expansion via `bgg info`
- Open a game or expansion on boardgamegeek.com in browser via `bgg open`
- Get and display the current boardgamegeek hotness list via `bgg hot`

#### Local Collection Management

- Create a new local collection via `bgg new`
- List all local collections via `bgg collections`
- Delete a local collection via `bgg delete`
- Add a game/expansion to a local collection via `bgg add`
- List all games/expansions in a local collection via `bgg list`
- Drop a game/expansion from a local collection via `bgg drop`
- Display average game stats for a collection via `bgg stats`
- Update local collection data with snapshot from bgg via `bgg update`
