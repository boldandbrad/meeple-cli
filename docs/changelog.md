# Changelog

All notable changes to **meeple-cli** will be documented here.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/ "Keep a Changelog"),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html "Semantic Versioning").

## [Unreleased]

## [v0.1.0b5] - 2023-04-10

### Added

- `meeple info`: `-v/--verbose` - Output additional details.
- `meeple open`: `-y/--yes` - Bypass confirmation.
- `meeple find`/`meeple list`: `--sort` - Sort output by _time_.

### Changed

- `GENERAL` - Output _Play Time_ values as expected duration instead of a range.
- `GENERAL` - Update _Time_ column header text to _Play Time_.

### Removed

- `ROADMAP` - Remove roadmap from README. Move to GitHub issues.

## [v0.1.0b4] - 2023-04-07

### Added

- `meeple find` - Search collections for board games and expansions.
  - Search in just one, multiple, or all collections at once.
  - `-b/--boardgames` - Output only board games.
  - `-e/--expansions` - Output only expansions.
  - `--players` - Output only board games/expansions that support the provided player count.
  - `--max-time` - Output only board games/expansions that fit the provided play time (Min).
  - `--weight` - Output only board games/expansions that match the provided weight range.
  - `--sort` - Sort output by _id_, _name_, _year_, _rank_, _rating_, or _weight_.
- `GENERAL` - Shell tab completion support for `bash`, `zsh`, and `fish`.
  - Tab completion support for all commands.
  - Tab completion support for all command `COLLECTION` arguments.
  - Tab completion support for all command options.
- `meeple completions` - Setup shell tab completions.
- `README`
  - Disclaimer section.
  - FAQ section.

### Changed

- `meeple`: `-h/--help` - Group like commands in output.
- `GENERAL`: `-h/--help` - Standardize help messages.
- `GENERAL`: `ID` arg - Improve argument type checking and error handling.
- `CHANGELOG`: Standardize release notes format.

### Fixed

- `meeple search` - Fix data serialization crash.
- `GENERAL` - Properly format missing board game or expansion data as "NA".

## [v0.1.0b3] - 2023-04-03

### Added

- `meeple collections`: `--sort` - Sort output by _name_, _board game count_, _expansion count_, or _updated date_.
- `meeple list`: `--sort` - Sort output by _id_, _name_, _year_, _rank_, _rating_, or _weight_.

### Changed

- `GENERAL` - **Update minimum supported python version from `3.8` to `3.10`.**
- `GENERAL` - _play time_ outputs display with their appropriate unit (Min).
- `GENERAL` - _weight_ outputs no longer display with scale ("/ 5").
- `meeple update` - Update output format.
- `meeple collections`: `-h/--help` - Update help message.
- `meeple list`: `-h/--help` - Update help message.
- `meeple stats` - _Avg. Max Players_ output now calculates items with a max player count greater than 10 as 10 to avoid skewed results from outliers.
- `CI` - Replace `trunk` code lint manager with `pre-commit`.
  - Various code lint fixes and improvements.

### Fixed

- `meeple list` - Fix format of _rank_ output when value is "NA".

## [v0.1.0b2] - 2023-03-28

### Added

- `meeple rename` - Rename a collection.
- `DEPENDENCY` - `rich`.

### Changed

- `meeple search`
  - Include _year_ published column in output.
  - Sort results by ID by default.
- `meeple info` - Include _min age_ in output.
- `GENERAL` - Standardize and tabulate command output formats.

### Removed

- `DEPENDENCY` - `tabulate`.

### Fixed

- `meeple stats` - no longer crash when the collection only contains unrated,
  unranked, or unweighted items.

## [v0.1.0b1] - 2023-03-26

### Added

- `meeple search` - Search BoardGameGeek for a board game or expansion.
- `meeple info` - Get and display detailed info for a board game or expansion.
- `meeple open` - Open a board game or expansion on BoardGameGeek.
- `meeple hot` - Ability to get and display the current BoardGameGeek hotness list.
- `meeple new` - Create a new collection.
- `meeple collections` - List all collections.
  - `-v/--verbose` - Output additional details.
- `meeple delete` - Delete a collection.
  - `-y/--yes` - Bypass confirmation.
- `meeple add` - Add a board game/expansion to a collection.
- `meeple list` - List all board games/expansions in a collection.
  - `-b/--boardgames` - Output only board games.
  - `-e/--expansions` - Output only expansions.
  - `-v/--verbose` - Output additional details.
- `meeple drop` - Remove a board game/expansion from a collection.
- `meeple stats` - Calculate and display average board game stats for a collection.
  - `-b/--boardgames` - Output only board games.
  - `-e/--expansions` - Output only expansions.
- `meeple update` - Update local collection data with snapshot from BoardGameGeek.
- `meeple move` - Move a board game/expansion from one collection to another.
