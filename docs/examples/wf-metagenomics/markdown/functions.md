# Functions

This page documents helper functions defined in the pipeline.

## Contents

- [is_target_file](#is-target-file)
- [is_excluded](#is-excluded)
- [add_run_IDs_and_basecall_models_to_meta](#add-run-ids-and-basecall-models-to-meta)
- [add_number_of_reads_to_meta](#add-number-of-reads-to-meta)
- [fastq_ingress](#fastq-ingress)
- [xam_ingress](#xam-ingress)
- [parse_arguments](#parse-arguments)
- [get_valid_inputs](#get-valid-inputs)
- [create_metamap](#create-metamap)
- [get_target_files_in_dir](#get-target-files-in-dir)
- [get_sample_sheet](#get-sample-sheet)

## is_target_file {#is-target-file}

_Defined in `lib/ingress.nf:15`_

```groovy
def is_target_file(file, extensions)
```

Check if a file ends with one of the target extensions.

### Parameters

| Name         | Description | Default |
| ------------ | ----------- | ------- |
| `file`       | -           | -       |
| `extensions` | -           | -       |

## is_excluded {#is-excluded}

_Defined in `lib/ingress.nf:27`_

```groovy
def is_excluded(p, margs)
```

Check if a file path is flagged for exclusion.

### Parameters

| Name    | Description | Default |
| ------- | ----------- | ------- |
| `p`     | -           | -       |
| `margs` | -           | -       |

## add_run_IDs_and_basecall_models_to_meta {#add-run-ids-and-basecall-models-to-meta}

_Defined in `lib/ingress.nf:54`_

```groovy
def add_run_IDs_and_basecall_models_to_meta(ch, allow_multiple_basecall_models)
```

Take a channel of the shape `[meta, reads, path-to-stats-dir | null]` (or
`[meta, [reads, index], path-to-stats-dir | null]` in the case of XAM) and extract the run IDs and
basecall model, from the `run_ids` and `basecaller` files in the stats directory, into the metamap.
If the path to the stats dir is `null`, add an empty list.

### Parameters

| Name                             | Description | Default |
| -------------------------------- | ----------- | ------- |
| `ch`                             | -           | -       |
| `allow_multiple_basecall_models` | -           | -       |

## add_number_of_reads_to_meta {#add-number-of-reads-to-meta}

_Defined in `lib/ingress.nf:111`_

```groovy
def add_number_of_reads_to_meta(ch, input_type_format)
```

Take a channel of the shape `[meta, reads, path-to-stats-dir | null]` and do the following:

- For `fastcat`, extract the number of reads from the `n_seqs` file.
- For `bamstats`, extract the number of primary alignments and unmapped reads from the
  `bamstats.flagstat.tsv` file. Then, add add these metrics to the meta map. If the path to the
  stats dir is `null`, set the values to 0 when adding them. If not set to 'fastq', input is assumed
  to be 'bam'.

### Parameters

| Name                | Description | Default |
| ------------------- | ----------- | ------- |
| `ch`                | -           | -       |
| `input_type_format` | -           | -       |

## fastq_ingress {#fastq-ingress}

_Defined in `lib/ingress.nf:179`_

```groovy
def fastq_ingress(arguments)
```

Take a map of input arguments, find valid FASTQ inputs, and return a channel with elements of
`[metamap, seqs.fastq.gz | null, path-to-fastcat-stats | null]`. The second item is `null` for
sample sheet entries without a matching barcode directory. The last item is `null` if `fastcat` was
not run (it is only run on directories containing more than one FASTQ file or when `stats: true`).

- "input": path to either: (i) input FASTQ file, (ii) top-level directory containing FASTQ files,
  (iii) directory containing sub-directories which contain FASTQ files
- "sample": string to name single sample
- "sample_sheet": path to CSV sample sheet
- "analyse_unclassified": boolean. Whether to ingress unclassified (failed to demux) reads
- "analyse_fail": boolean. Whether to ingress any sequence files contained in `*_fail` directories.
- "stats": boolean whether to write the `fastcat` stats
- "fastcat_extra_args": string with extra arguments to pass to `fastcat`
- "required_sample_types": list of zero or more required sample types expected to be present in the
  sample sheet
- "per_read_stats": boolean. If true, output a bgzipped TSV containing a summary of each read to
  fastcat_stats/per-read-stats.tsv.gz.
- "fastq_chunk": null or a number of reads to place into chunked FASTQ files
- "allow_multiple_basecall_models": emit data of samples that had more than one basecall model; if
  this is `false`, such samples will be emitted as `[meta, null, null]` The first element is a map
  with metadata, the second is the path to the `.fastq.gz` file with the (potentially concatenated)
  sequences and the third is the path to the directory with the `fastcat` statistics. The second
  element is `null` for sample sheet entries for which no corresponding barcode directory was found.
  The third element is `null` if `fastcat` was not run.

### Parameters

| Name        | Description | Default |
| ----------- | ----------- | ------- |
| `arguments` | -           | -       |

## xam_ingress {#xam-ingress}

_Defined in `lib/ingress.nf:288`_

```groovy
def xam_ingress(arguments)
```

Take a map of input arguments, find valid (u)BAM inputs, and return a channel with elements of
`[metamap, reads.bam | null, path-to-bamstats-results | null]`. The second item is `null` for sample
sheet entries without a matching barcode directory or samples containing only uBAM files when
`keep_unaligned` is `false`. The last item is `null` if `bamstats` was not run (it is only run when
`stats: true`).

- "input": path to either: (i) input (u)BAM file, (ii) top-level directory containing (u)BAM files,
  (iii) directory containing sub-directories which contain (u)BAM files
- "sample": string to name single sample
- "sample_sheet": path to CSV sample sheet
- "analyse_unclassified": boolean. Whether to ingress unclassified (failed to demux) reads
- "analyse_fail": boolean. Whether to ingress any sequence files contained in `*_fail` directories.
- "stats": boolean whether to run `bamstats`
- "keep_unaligned": boolean whether to include uBAM files
- "return_fastq": boolean whether to convert to FASTQ (this will always run `fastcat`)
- "fastcat_extra_args": string with extra arguments to pass to `fastcat`
- "required_sample_types": list of zero or more required sample types expected to be present in the
  sample sheet
- "per_read_stats": boolean. If true, output a bgzipped TSV containing a summary
- "fastq_chunk": null or a number of reads to place into chunked FASTQ files
- "allow_multiple_basecall_models": boolean. If true, emit data of samples that had more than one
  basecall model; if this is `false`, such samples will be emitted as `[meta, null, null]` The first
  element is a map with metadata, the second is the path to the `.bam` file with the (potentially
  merged) sequences and the third is the path to the directory with the `bamstats` statistics. The
  second element is `null` for sample sheet entries for which no corresponding barcode directory was
  found and for samples with only uBAM files when `keep_unaligned: false`. The third element is
  `null` if `bamstats` was not run.

### Parameters

| Name        | Description | Default |
| ----------- | ----------- | ------- |
| `arguments` | -           | -       |

## parse_arguments {#parse-arguments}

_Defined in `lib/ingress.nf:852`_

```groovy
def parse_arguments(func_name, arguments, extra_kwargs)
```

Parse input arguments for `fastq_ingress` or `xam_ingress`. for details) the argument-parsing to be
tailored to a particular ingress function)

### Parameters

| Name           | Description | Default |
| -------------- | ----------- | ------- |
| `func_name`    | -           | -       |
| `arguments`    | -           | -       |
| `extra_kwargs` | -           | -       |

## get_valid_inputs {#get-valid-inputs}

_Defined in `lib/ingress.nf:886`_

```groovy
def get_valid_inputs(margs, extensions)
```

Find valid inputs based on the target extensions and return a branched channel with branches
`missing`, `files` and `dir`, which are of the shape `[metamap, input_path | null]` (with
`input_path` pointing to a target file or a directory containing target files, respectively).
`missing` contains sample sheet entries for which no corresponding barcodes were found. Checks
whether the input is a single target file, a top-level directory with target files, or a directory
containing sub-directories (usually barcodes) with target files.

### Parameters

| Name         | Description | Default |
| ------------ | ----------- | ------- |
| `margs`      | -           | -       |
| `extensions` | -           | -       |

## create_metamap {#create-metamap}

_Defined in `lib/ingress.nf:1123`_

```groovy
def create_metamap(arguments)
```

Create a map that contains at least these keys: `[alias, barcode, type]`. `alias` is required,
`barcode` and `type` are filled with default values if missing. Additional entries are allowed.

### Parameters

| Name        | Description | Default |
| ----------- | ----------- | ------- |
| `arguments` | -           | -       |

## get_target_files_in_dir {#get-target-files-in-dir}

_Defined in `lib/ingress.nf:1149`_

```groovy
def get_target_files_in_dir(dir, extensions, margs, recursive)
```

Get all target files below this directory.

### Parameters

| Name         | Description | Default |
| ------------ | ----------- | ------- |
| `dir`        | -           | -       |
| `extensions` | -           | -       |
| `margs`      | -           | -       |
| `recursive`  | -           | -       |

## get_sample_sheet {#get-sample-sheet}

_Defined in `lib/ingress.nf:1165`_

```groovy
def get_sample_sheet(sample_sheet, required_sample_types)
```

Check the sample sheet and return a channel with its rows if it is valid. in the sample sheet

### Parameters

| Name                    | Description | Default |
| ----------------------- | ----------- | ------- |
| `sample_sheet`          | -           | -       |
| `required_sample_types` | -           | -       |

---

_This pipeline was built with [Nextflow](https://nextflow.io). Documentation generated by
[nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:27:31 UTC._
