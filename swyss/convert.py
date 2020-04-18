import logging
from os.path import splitext, exists

import pandas as pd
import yaml
import json


class Converter:
    def __init__(self,
                 input_file: str,
                 from_format: str,
                 to_format: str,
                 force: bool
                 ):
        self.input_file = input_file
        self.from_format = from_format
        self.to_format = to_format
        self.force = force
        self.data = None
        self.output_file = None

    def _file_without_ext(self):
        return splitext(self.input_file)[0]

    def run(self):
        self.output_file = f"{self._file_without_ext()}_out.{self.to_format}"
        if exists(self.output_file) and not self.force:
            raise FileExistsError(
                f"Output file '{self.output_file}' already exists, exiting...")

        if self.from_format == "csv":
            data = self._from_csv()
        elif self.from_format == "html":
            data = self._from_html()
        elif self.from_format == "json":
            data = self._from_json()
        elif self.from_format == "ods":
            data = self._from_ods()
        elif self.from_format == "tsv":
            data = self._from_tsv()
        elif self.from_format in ["xls", "xlsx"]:
            data = self._from_excel()
        elif self.from_format == "yaml":
            data = self._from_yaml()

        self.data = data

        return self._convert_to()

    def _from_csv(self) -> dict:
        return pd.read_csv(self.input_file).to_dict(orient="records")

    def _from_html(self) -> dict:
        return pd.read_html(self.input_file)[0].to_dict(orient="records")

    def _from_json(self) -> dict:
        with open(self.input_file) as f:
            data = json.load(f)
        return data

    def _from_ods(self) -> dict:
        return pd.read_excel(
            self.input_file, engine="odf").to_dict(orient="records")

    def _from_tsv(self) -> dict:
        return pd.read_table(self.input_file).to_dict(orient="records")

    def _from_excel(self) -> dict:
        return pd.read_excel(self.input_file).to_dict(orient="records")

    def _from_yaml(self) -> dict:
        with open(self.input_file) as f:
            data = yaml.safe_load(f)
        return data

    def _convert_to(self) -> str:
        if self.to_format == "csv":
            self._to_csv()
        elif self.to_format == "html":
            self._to_html()
        elif self.to_format == "json":
            self._to_json()
        elif self.to_format == "tsv":
            self._to_tsv()
        elif self.to_format in ["xls", "xlsx"]:
            self._to_excel()
        elif self.to_format == "yaml":
            self._to_yaml()

        logging.info(f"Saved to {self.output_file}")
        return self.output_file

    def _to_csv(self) -> None:
        pd.DataFrame(self.data).to_csv(self.output_file, index=False)

    def _to_html(self) -> None:
        pd.DataFrame(self.data).to_html(self.output_file, index=False)

    def _to_json(self) -> None:
        with open(self.output_file, "w") as f:
            json.dump(self.data, f)

    def _to_tsv(self) -> None:
        pd.DataFrame(self.data).to_csv(self.output_file, sep="\t", index=False)

    def _to_excel(self) -> None:
        pd.DataFrame(self.data).to_excel(self.output_file, index=False)

    def _to_yaml(self) -> None:
        with open(self.output_file, "w") as f:
            yaml.safe_dump(self.data, f, sort_keys=False)
