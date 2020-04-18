# Swyss

Multiconverter file tool written in Python.

## Usage

```bash
swyss -i path/to/file1.xlsx path/to/file2.xlsx -t json
swyss -i path/to/file1.xlsx path/to/file2.xlsx -t yaml
swyss -i path/to/file1.xlsx path/to/file2.xlsx -t csv
# add -f (--force) option to overwrite existing files
swyss -i path/to/file1.xlsx path/to/file2.xlsx -t csv -f
```

## TODO

* Implement tox tests.
* Design a logo.
* Add `xml` support.
* Add `-v/--verbose` option.
* Add `-o/--out-dir` option.
* Support multiple `--to` arguments.

## Changelog

### 0.0.1 (2020-04-18)

Initial working version.
