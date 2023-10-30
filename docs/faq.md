# FAQ

Answers to common `meeple-cli` questions.

Table of Contents:

- [FAQ](#faq)
  - [Why local-only collections?](#why-local-only-collections)
  - [Why does collection import take so long?](#why-does-collection-import-take-so-long)
  - [Why do some items show a weight of `NA` when boardgamegeek.com has a value?](#why-do-some-items-show-a-weight-of-na-when-boardgamegeekcom-has-a-value)
  - [Where does `meeple-cli` store data?](#where-does-meeple-cli-store-data)

## Why local-only collections?

Currently, the
[BoardGameGeek Public API](https://boardgamegeek.com/wiki/page/BGG_XML_API2)
provides limited _read-only_ data about user Collections and GeekLists.

While it is _technically_ feasible to interface with Collections and GeekLists
via webscrapers or spiders, these approaches would be complex and also violate
[BoardGameGeek Terms of Service](https://boardgamegeek.com/terms#toc22).

For now, it is possible to import BGG user collections into `meeple-cli` via
`meeple import`.

## Why does collection import take so long?

Currently, the
[BoardGameGeek Public API](https://boardgamegeek.com/wiki/page/BGG_XML_API2)
relies on queued jobs to create a snapshot of a user's collection on demand.
Depending on the length of the queue or size of your BGG collection, the job may
take several minutes or longer to complete. You can read more about this issue
in [this thread](https://boardgamegeek.com/thread/1188687/export-collections-has-been-updated-xmlapi-develop).

If your request times out, or exceeds the BGG API rate limit, please be patient
and try again later.

## Why do some items show a weight of `NA` when boardgamegeek.com has a value?

This is a known and occasionally recurring bug in the BoardGameGeek database. It
usually resolves itself within a day. For more info or additional support, read
[this thread](https://boardgamegeek.com/thread/3049286/some-games-show-weight-000).

Luckily for us, game weights do not often change drastically. In most cases, we
can assume that the weight from yesterday is _close enough_.
[In the future](https://github.com/boldandbrad/meeple-cli/issues/61),
`meeple-cli` will attempt to compensate for this issue automatically by
displaying the last known value by default, if there is one.

## Where does `meeple-cli` store data?

`meeple-cli` stores collection data locally in `~/.meeple` and only makes network
connections to retrieve data from the BoardGameGeek API.
