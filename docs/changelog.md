# Changelog

All notable changes to **meeple-cli** will be documented here.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/ "Keep a Changelog"),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html "Semantic Versioning").

## [v0.1.0-beta-2] - 2023-03-28

### Added

#### Collection Management

- Rename a local collection via `meeple rename`

### Changed

- Most commands now output tabulated data and info
- `meeple search` now includes year published in output
- `meeple search` results are now sorted by ID by default
- `meeple info` now includes min age in output
- Replaced tabulate dependency with rich

### Fixed

- `meeple stats` no longer crashes when the collection only contains unrated,
  unranked, or un_weighted items

## [v0.1.0-beta-1] - 2023-03-26

### Added

#### Boardgamegeek.com

- Search BoardGameGeek for a board game or expansion via `meeple search`
- Get and display detailed info for a board game or expansion via `meeple info`
- Open a board game or expansion on BoardGameGeek in browser via `meeple open`
- Get and display the current BoardGameGeek hotness list via `meeple hot`

#### Collection Management

- Create a new local collection via `meeple new`
- List all local collections via `meeple collections`
- Delete a local collection via `meeple delete`
- Add a board game/expansion to a local collection via `meeple add`
- List all board games/expansions in a local collection via `meeple list`
- Drop a board game/expansion from a local collection via `meeple drop`
- Display average board game stats for a collection via `meeple stats`
- Update local collection data with snapshot from BoardGameGeek via `meeple update`
- Move a board game/expansion from one collection to another via `meeple move`
