"""Tests for schema parser."""

from pathlib import Path

import pytest

from nf_docs.schema_parser import (
    SchemaParseError,
    find_schema_file,
    parse_schema,
    validate_schema,
)


class TestParseSchema:
    def test_parse_basic_schema(self, sample_schema_file: Path):
        metadata, inputs = parse_schema(sample_schema_file)

        assert metadata.name == "Test Pipeline"
        assert metadata.description == "A test pipeline for unit tests"

    def test_parse_inputs(self, sample_schema_file: Path):
        _, inputs = parse_schema(sample_schema_file)

        # Check we got all inputs
        input_names = {inp.name for inp in inputs}
        assert "input" in input_names
        assert "outdir" in input_names
        assert "genome" in input_names
        assert "fasta" in input_names

    def test_parse_required_inputs(self, sample_schema_file: Path):
        _, inputs = parse_schema(sample_schema_file)

        input_map = {inp.name: inp for inp in inputs}

        # input should be required
        assert input_map["input"].required is True
        # outdir should be optional
        assert input_map["outdir"].required is False

    def test_parse_input_details(self, sample_schema_file: Path):
        _, inputs = parse_schema(sample_schema_file)

        input_map = {inp.name: inp for inp in inputs}

        # Check input details
        inp = input_map["input"]
        assert inp.type == "string"
        assert inp.format == "file-path"
        assert inp.description == "Path to input samplesheet"
        assert "samplesheet" in inp.help_text.lower()

        # Check outdir default
        outdir = input_map["outdir"]
        assert outdir.default == "./results"

        # Check genome enum
        genome = input_map["genome"]
        assert genome.enum == ["GRCh37", "GRCh38", "GRCm38"]

    def test_parse_input_groups(self, sample_schema_file: Path):
        _, inputs = parse_schema(sample_schema_file)

        input_map = {inp.name: inp for inp in inputs}

        assert input_map["input"].group == "Input/output options"
        assert input_map["genome"].group == "Reference genome options"

    def test_nonexistent_file(self):
        with pytest.raises(SchemaParseError, match="not found"):
            parse_schema("/nonexistent/path/schema.json")

    def test_invalid_json(self, tmp_path: Path):
        bad_file = tmp_path / "bad.json"
        bad_file.write_text("not valid json {{{")

        with pytest.raises(SchemaParseError, match="Invalid JSON"):
            parse_schema(bad_file)


class TestFindSchemaFile:
    def test_find_in_root(self, tmp_path: Path):
        schema_file = tmp_path / "nextflow_schema.json"
        schema_file.write_text("{}")

        found = find_schema_file(tmp_path)
        assert found == schema_file

    def test_find_in_schema_dir(self, tmp_path: Path):
        schema_dir = tmp_path / "schema"
        schema_dir.mkdir()
        schema_file = schema_dir / "nextflow_schema.json"
        schema_file.write_text("{}")

        found = find_schema_file(tmp_path)
        assert found == schema_file

    def test_not_found(self, tmp_path: Path):
        found = find_schema_file(tmp_path)
        assert found is None


class TestValidateSchema:
    def test_valid_schema(self, sample_schema: dict):
        warnings = validate_schema(sample_schema)
        # Our sample schema is valid
        assert len(warnings) == 0

    def test_missing_schema_declaration(self):
        schema = {"title": "Test", "properties": {}}
        warnings = validate_schema(schema)
        assert any("$schema" in w for w in warnings)

    def test_missing_description(self):
        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "properties": {
                "param_without_description": {
                    "type": "string",
                }
            },
        }
        warnings = validate_schema(schema)
        assert any("missing a description" in w for w in warnings)

    def test_missing_type(self):
        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "properties": {
                "param_without_type": {
                    "description": "A parameter",
                }
            },
        }
        warnings = validate_schema(schema)
        assert any("missing a type" in w for w in warnings)
