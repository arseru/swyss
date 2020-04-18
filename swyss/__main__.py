import argparse
import logging
from mimetypes import guess_type
from os.path import splitext

from swyss.convert import Converter


def detect_format(file: str):
    """https://www.iana.org/assignments/media-types/media-types.xhtml
    """
    valid_mimetypes = {
        "text/csv": "csv",
        "text/html": "html",
        "application/json": "json",
        "application/vnd.oasis.opendocument.spreadsheet": "ods",
        "text/tab-separated-values": "tsv",
        "application/vnd.ms-excel": "xls",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "xlsx",
        # YAML does not have an official mimetype
        "yaml": "yaml",
        "yml": "yaml",
    }
    f = guess_type(file)[0]
    # If file does not have a mimetype, get directly its file extension
    if f is None:
        f = splitext(file)[1][1:]  # file extension without the dot ('.')
    match = f in valid_mimetypes.keys()
    if match:
        return valid_mimetypes[f]
    else:
        raise ValueError(
            f"Input file '{file}' does not have a valid extension. Valid "
            f"extensions are: {', '.join(valid_mimetypes.values())}")


def convert(file: str, from_format: str, to_format: str, force: bool) -> str:
    c = Converter(
        input_file=file,
        from_format=from_format,
        to_format=to_format,
        force=force)
    return c.run()


def detect_and_convert(file: str, output_fmt: str, force: bool) -> str:
    input_fmt = detect_format(file)
    return convert(
        file=file, from_format=input_fmt, to_format=output_fmt, force=force)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] -- %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    p = argparse.ArgumentParser(
        allow_abbrev=False,
        description="Multiconverter file tool written in Python")
    p.add_argument(
        "-i", "--input", required=True, nargs="+", type=str,
        metavar="input_files", help="Input files to convert")
    p.add_argument(
        "-t", "--to", required=True, help="Output format",
        choices=["csv", "html", "json", "tsv", "xls", "xlsx", "yaml"])
    p.add_argument(
        "-f", "--force", default=False, action='store_true',
        help="Overwrite output file if it already exists in filesystem")
    args = p.parse_args()

    # Identify each input format, and convert to the desired output format
    for f in args.input:
        detect_and_convert(file=f, output_fmt=args.to, force=args.force)


if __name__ == "__main__":
    main()
