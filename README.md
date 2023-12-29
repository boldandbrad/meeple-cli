# meeple-cli

[![build status](https://img.shields.io/github/actions/workflow/status/boldandbrad/meeple-cli/python-test.yml?branch=main&logo=github)](https://github.com/boldandbrad/meeple-cli/actions/workflows/python-test.yml?query=branch%3Amain)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![codecov](https://codecov.io/gh/boldandbrad/meeple-cli/branch/main/graph/badge.svg)](https://codecov.io/gh/boldandbrad/meeple-cli)
[![pypi](https://img.shields.io/pypi/v/meeple-cli)](https://pypi.org/project/meeple-cli/)
[![downloads](https://img.shields.io/pypi/dm/meeple-cli)](https://pypistats.org/packages/meeple-cli)

<!-- [![Docs](https://img.shields.io/website?down_message=down&label=docs&up_message=online&url=https%3A%2F%2Fboldandbrad.github.io%2Fmeeple-cli%2F)](https://boldandbrad.github.io/meeple-cli/) -->

**meeple-cli** is a local board game collection manager. Powered by
[BoardGameGeek](https://boardgamegeek.com).

**Jump to:**
[Installation](#install) |
[Usage](#usage) |
[Completions](#completions) |
[Changelog](#changelog) |
[Roadmap](#roadmap) |
[FAQ](#faq) |
[Legal](#legal)

## Install

Via [Homebrew](https://brew.sh) (Recommended on macOS/Linux)

```zsh
brew tap boldandbrad/tap
brew install meeple-cli
```

Via [pipx](https://pypa.github.io/pipx/) (Recommended on Windows):

```sh
pipx install meeple-cli
```

Via `pip`:

```sh
pip install meeple-cli
```

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
  add          Add items to a collection.
  collections  List all collections.
  delete       Delete collections.
  drop         Drop items from a collection.
  find         Search collections for items.
  list         List contents of a collection.
  move         Move an item from one collection to another.
  new          Create new collections.
  rename       Rename a collection.
  stats        View collection statistics.
  update       Update collection data.

BoardGameGeek Commands:
  campaigns  List active crowdfunding campaigns.
  hot        List current BoardGameGeek trending items.
  import     Import BoardGameGeek user collections.
  info       View item details.
  open       Open items in the browser.
  search     Search BoardGameGeek for items.

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

## Changelog

See a history of implemented features/changes in the
[Changelog](docs/changelog.md).

## Roadmap

See a list of planned features and milestones
[here](https://github.com/boldandbrad/meeple-cli/milestones).

## FAQ

### Why local only collections?

Currently, the
[BoardGameGeek Public API](https://boardgamegeek.com/wiki/page/BGG_XML_API2)
provides limited _read-only_ data about user Collections and GeekLists.

While it is _technically_ feasible to interface with Collections and GeekLists
via webscrapers or spiders, these approaches would be complex and also violate
[BoardGameGeek Terms of Service](https://boardgamegeek.com/terms#toc22).

For now, it is possible to import BGG user collections into `meeple-cli` via
`meeple import`.

### Why does collection import take so long?

Currently, the
[BoardGameGeek Public API](https://boardgamegeek.com/wiki/page/BGG_XML_API2)
relies on queued jobs to create a snapshot of a user's collection on demand.
Depending on the length of the queue or size of your BGG collection, the job may
take several minutes or longer to complete. You can read more about this issue
in [this thread](https://boardgamegeek.com/thread/1188687/export-collections-has-been-updated-xmlapi-develop).

If your request times out, or exceeds the BGG API rate limit, please be patient
and try again later.

### Why do some items show a weight of `NA` when boardgamegeek.com has a value?

This is a known and occasionally recurring bug in the BoardGameGeek database. It
usually resolves itself within a day. For more info or additional support, read
[this thread](https://boardgamegeek.com/thread/3049286/some-games-show-weight-000).

Luckily for us, game weights do not often change drastically. In most cases, we
can assume that the weight from yesterday is _close enough_.
[In the future](https://github.com/boldandbrad/meeple-cli/issues/61),
`meeple-cli` will attempt to compensate for this issue automatically by
displaying the last known value by default, if there is one.

### Where does `meeple-cli` store data?

`meeple-cli` stores collection data in `~/.meeple` and only makes network
connections to retrieve data from the BoardGameGeek API.

## Legal

### Disclaimers

- Neither `meeple-cli` nor its maintainers are affiliated with
  [BoardGameGeek](https://boardgamegeek.com).
- Neither `meeple-cli` nor its maintainers are affiliated with
  [Kickstarter](https://www.kickstarter.com/),
  [Gamefound](https://gamefound.com/en), or any other crowdfunding site or
  campaign. Links to crowdfunding campaigns surfaced by `meeple-cli` are
  sourced from Boardgamegeek and are provided for convenience purposes only.
  Back campaigns at your own risk.

### License

Copyright (c) 2023 Bradley Wojcik. Released under the MIT License. See
[LICENSE](LICENSE) for details.
