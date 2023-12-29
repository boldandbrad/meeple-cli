# Changelog

All notable changes to **meeple-cli** will be documented here.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/ "Keep a Changelog"),
and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html "Semantic Versioning").

## [Unreleased]

## [v1.3.0] - 2023-12-29

### Added

- `meeple campaigns` - List active crowdfunding campaigns.
- `meeple open`: `--campaign` - Open an item's crowdfunding campaign page.

## [v1.2.0] - 2023-10-27

### Added

- `README`: `FAQ` - Add faq statement about slow collection imports.
- `CI` - Add Python 3.12 support. ([#90](https://github.com/boldandbrad/meeple-cli/issues/90))

### Changed

- `meeple import` - Add progress bar to indicate status of collection fetch from
  BGG.
- `meeple info`
  - Show a list of collections the item is contained in. ([#56](https://github.com/boldandbrad/meeple-cli/issues/56))
  - Add designers, artists, and publishers to `-v`/`--verbose` output.
- `README`: `Usage` - Update usage documentation to reflect current help message
  text.
- `CI` - Update `pre-commit` linters.

### Fixed

- `meeple import --verbose` - Fix crash.
- `meeple collections` - Prevent update warning message from printing more than once.
- `meeple collections` - Fix sort order of NA Last Updated values.
- `GENERAL` - Fix justification of numeric values in tables. ([#83](https://github.com/boldandbrad/meeple-cli/issues/83))
- `GENERAL` - Print a more elegant error message when BGG API rate limit is exceeded.

## [v1.1.0] - 2023-10-18

### Changed

- `meeple add`
  - Add multiple items to a collection at once. ([#77](https://github.com/boldandbrad/meeple-cli/issues/77))
  - Update help text wording to be consistent with action.
  - Dim 'already added' message text.
- `meeple drop`
  - Drop multiple items from a collection at once. ([#78](https://github.com/boldandbrad/meeple-cli/issues/78))
  - Update help text wording to be consistent with action.
  - Dim 'already dropped' message text.
- `meeple collections` - Update 'pending update' warning message text.

### Fixed

- `meeple add` - Prevent adding duplicate items in collections when collection
  data has not yet been updated.
- `meeple list`/`meeple find` - Order items with NA rank values last when
  sorting by rank. ([#81](https://github.com/boldandbrad/meeple-cli/issues/81))

## [v1.0.1] - 2023-10-13

### Changed

- `DEPENDENCY` - Update `pyyaml` to v6.0.1.

### Fixed

- Fix homebrew install dependency crash.

## [v1.0.0] - 2023-10-13

### Added

- `meeple add`: `--update` - Automatically update collection data. ([#26](https://github.com/boldandbrad/meeple-cli/issues/26))
- `meeple drop`: `--update` - Automatically update collection data. ([#26](https://github.com/boldandbrad/meeple-cli/issues/26))
- `meeple move`: `--update` - Automatically update collection data. ([#26](https://github.com/boldandbrad/meeple-cli/issues/26))
- `meeple collections`: `--update` - Update collection data before showing results.
- `meeple list`: `--verbose` - Summarize output above table. ([#40](https://github.com/boldandbrad/meeple-cli/issues/40))
- `meeple find`: `--verbose` - Summarize output above table. ([#40](https://github.com/boldandbrad/meeple-cli/issues/40))

### Changed

- `DATA`
  - Migrate collection state files to new location and format (NON-BREAKING - these migrations happen automatically)
    - Move location of collection state files from `.meeple/collections/` to `.meeple/collections/state/`. Automatically migrate existing files.
    - Add `version` attribute to allow for more seamless data changes in the future.
    - Rename `bgg_ids` attribute to `active`.
  - Update collection data storage pattern (**BREAKING** - historical data is no longer tracked)
    - Move _existing_ collection data files from `.meeple/data/` to `.meeple/archives/v0/`
    - Move location of _new_ collection data files from `.meeple/data/` to `.meeple/collections/data/`
    - Only store data for the most recent update
      - Note: Historical data storage _may_ return in the future, but at this time it only increases complexity without benefit.
    - Add `version` attribute to allow for more seamless data changes in the future.
    - Add `date` attribute.
    - Replace `boardgames` and `expansions` attributes with a single `items` attribute.
    - Add `type` attribute to `items` objects.
- `meeple collections` - Update `--sort` option help text.
- `meeple find`
  - Update `-b/--boardgames` option help text.
  - Update `-e/--expansions` option help text.
  - Update `--players` option help text.
  - Update `--max-time` option help text.
  - Update `--weight` option help text.
  - Update `--sort` option help text and move to bottom of options.
- `meeple list`
  - Update `-b/--boardgames` option help text.
  - Update `-e/--expansions` option help text.
  - Update `--sort` option help text.
- `meeple stats`
  - Update output summary message and table format.
  - Update `-b/--boardgames` option help text.
  - Update `-e/--expansions` option help text.
- `GENERAL`
  - Rename `COLLECTION/S` argument `--help` references to `COLLECTION_NAME/S`
  - Rename `ID` argument `--help` references to `BGG_ID`

## [v0.2.0] - 2023-05-22

### Added

- `meeple import` - Import BoardGameGeek user collections. ([#46](https://github.com/boldandbrad/meeple-cli/issues/46))
  - Import as either one large collection or as separate collections based on item status.
  - `--one` - Import as one collection.
  - `--many` - Import as separate collections by status.
  - `--dry-run` - Simulate import operations without persisting.
  - `-v/--verbose` - Output additional details.

### Changed

- `meeple delete` - Delete multiple collections at once. ([#69](https://github.com/boldandbrad/meeple-cli/issues/69))
- `meeple new` - Create multiple collections at once. ([#70](https://github.com/boldandbrad/meeple-cli/issues/70))
- `meeple update` - Update multiple specific collections at once. ([#66](https://github.com/boldandbrad/meeple-cli/issues/66))

### Fixed

- `meeple find` - Fix error message collection name formatting.
- `meeple rename` - Fix help message wording.

## [v0.1.0] - 2023-05-16

### Changed

- `GENERAL` - Code cleanup and increased test coverage.

## [v0.1.0rc1] - 2023-05-15

### Added

- `meeple list` - Show warning message when the collection has pending changes.
- `meeple move`
  - Gracefully handle the re-removal of items slated to be added to the source collection.
  - Gracefully handle the re-addition of items slated to be dropped from the destination collection.

### Changed

- `meeple add`/`meeple drop`/`meeple move`/`meeple update` - Update output message wording.
- `meeple update` - Skipped collection output is now dimmed.
- `GENERAL` - Reduce duplicate code.

### Fixed

- `meeple add`
  - Remove rogue `'` character in output.
  - Properly colorize collection name in output.
- `meeple search` - Properly show error message when no results found matching query.
- `meeple collections` - Properly dim NA _Last Updated_ value.

## [v0.1.0b8] - 2023-05-10

### Fixed

- `meeple stats`: `-b/-e` - Fix output format issue.

## [v0.1.0b7] - 2023-05-10

### Added

- `meeple add`
  - Gracefully handle the re-addition of items slated to be dropped.
  - Recommend `meeple update` in output.
- `meeple collections` - Show pending changes indicators and warning message.
- `meeple drop`
  - Gracefully handle the re-removal of items slated to be added.
  - Recommend `meeple update` in output.
- `meeple find`/`meeple list`/`meeple search`/`meeple stats` - Show warning message when no items match provided filters.
- `meeple move` - Recommend `meeple update` in output.
- `meeple stats` - Show pending changes warning message.
- `meeple update`: `-f/--force` - Force update regardless of collection state.
- `INSTALL` - Install via [Homebrew](https://brew.sh). See project README for details.

### Changed

- `meeple completions` - Simplify output style.
- `meeple delete`/`meeple open` - Confirmation input must now match `y/Y/n/N` or a re-prompt will occur.
- `meeple update`
  - By default, only update collections that are either outdated or have pending changes.
  - Output is more readable.
- `GENERAL`
  - Item names now appear blue and italicized in output messages.
  - Collection names now appear magenta and underlined in output messages.
  - Commands now appear green in output messages.
  - Item Ids and other values now appear yellow in error and warning messages.
  - Output message ontainer borders now appear dimmer.
- `DATA`
  - Update collection yaml file format to accomodate pending changes. (NON-BREAKING - Collection modifying commands such `meeple add/drop/move/update` will automatically convert old files to the new format when possible.)

### Fixed

- `meeple find` - Exit with error when no collections exist to search.
- `GENERAL` - Properly print out messages as Errors instead of Warnings when the
  result is a process termination.

## [v0.1.0b6] - 2023-04-16

### Added

- `GENERAL` - Sortedby column indicator in sorted output.
- `meeple list` - _Type_ column included if output contains both board games and expansions.
- `TESTS` - Increase test coverage.
- `CI` - Report test coverage to [Codecov](https://codecov.io).
- `CI` - Speed up test github action with `pre-commit` caching.

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
