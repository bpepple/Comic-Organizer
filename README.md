# Comic Organizer

[![Version](https://img.shields.io/github/tag-pre/Macro303/Comic-Organizer.svg?label=version&style=flat-square)](https://github.com/Macro303/Comic-Organizer/releases)
[![Issues](https://img.shields.io/github/issues/Macro303/Comic-Organizer.svg?style=flat-square)](https://github.com/Macro303/Comic-Organizer/issues)
[![Contributors](https://img.shields.io/github/contributors/Macro303/Comic-Organizer.svg?style=flat-square)](https://github.com/Macro303/Comic-Organizer/graphs/contributors)
[![License](https://img.shields.io/github/license/Macro303/Comic-Organizer.svg?style=flat-square)](https://opensource.org/licenses/MIT)

*TODO*

## Built Using

- [Python: 3.9.2](https://www.python.org/)
- [pip: 21.0.1](https://pypi.org/project/pip/)
- [ruamel.yaml: 0.17.4](https://pypi.org/project/ruamel.yaml)
- [titlecase: 2.0.0](https://pypi.org/project/titlecase)
- [requests: 2.25.1](https://pypi.org/project/requests)
- [beautifulsoup4: 4.9.3](https://pypi.org/project/beautifulsoup4)
- [lxml: 4.6.3](https://pypi.org/project/lxml)
- [patool: 1.12](https://pypi.org/project/patool)

## Arguments

| Argument | Type | Required | Default | Notes |
| -------- | ---- | -------- | ------- | ----- |
| `--debug` | bool | False | False | |

## ComicInfo Json Schema

```json
{
    "Publisher": <String>,
    "Series": {
        "Title": <String>,
        "Volume": <Integer|1>
    },
    "Comic": {
        "Number": <String|1>,
        "Title": <String|null>
    },
    "Variant": <String|null>,
    "Summary": <String|null>,
    "Cover Date": <Date|yyyy-mm-dd|null>,
    "Language": <String|EN>,
    "Format": <ComicFormat|Comic>,
    "Genres": [
        <ComicGenre>
    ],
    "Page Count": <Integer|1>,
    "Creators": {
        <Role>: [
            <String>
        ]
    },
    "Alternative Series": [
        {
            "Title": <String>,
            "Volume": <Integer|1>,
            "Number": <String|1>
        }
    ],
    "Identifiers": {
        <Website>: {
            "Id": <String|null>,
            "Url": <String|null>
        }
    },
    "Notes": <String|null>
}
```

Possible Formats:

- Comic
- Annual
- Digital Chapter
- Trade Paperback
- Hardcover

Possible Genres:

- Superhero

## Socials

[![Discord | The DEV Environment](https://invidget.switchblade.xyz/618581423070117932)](https://discord.gg/nqGMeGg)