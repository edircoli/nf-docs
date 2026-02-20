# Processes

This page documents all processes in the pipeline.

## Contents

- [minimap](#minimap)
- [minimapTaxonomy](#minimaptaxonomy)
- [extractMinimap2Reads](#extractminimap2reads)
- [getAlignmentStats](#getalignmentstats)
- [run_kraken2](#run-kraken2)
- [run_bracken](#run-bracken)
- [output_kraken2_read_assignments](#output-kraken2-read-assignments)
- [exclude_host_reads](#exclude-host-reads)
- [fastcat](#fastcat)
- [checkBamHeaders](#checkbamheaders)
- [validateIndex](#validateindex)
- [mergeBams](#mergebams)
- [catSortBams](#catsortbams)
- [sortBam](#sortbam)
- [bamstats](#bamstats)
- [move_or_compress_fq_file](#move-or-compress-fq-file)
- [split_fq_file](#split-fq-file)
- [validate_sample_sheet](#validate-sample-sheet)
- [samtools_index](#samtools-index)
- [getParams](#getparams)
- [configure_igv](#configure-igv)
- [abricate](#abricate)
- [abricate_json](#abricate-json)
- [filter_references](#filter-references)
- [abricateVersion](#abricateversion)
- [getVersions](#getversions)
- [getVersionsCommon](#getversionscommon)
- [createAbundanceTables](#createabundancetables)
- [publishReads](#publishreads)
- [publish](#publish)
- [makeReport](#makereport)

## minimap {#minimap}

_Defined in `subworkflows/minimap_pipeline.nf:11`_

### Inputs

| Name                                        | Type    | Description |
| ------------------------------------------- | ------- | ----------- |
| `val(meta), path(concat_seqs), path(stats)` | `tuple` | -           |

### Outputs

| Name        | Type    | Emit | Description |
| ----------- | ------- | ---- | ----------- |
| `val(meta)` | `tuple` | -    | -           |

## minimapTaxonomy {#minimaptaxonomy}

_Defined in `subworkflows/minimap_pipeline.nf:89`_

### Inputs

| Name                           | Type    | Description |
| ------------------------------ | ------- | ----------- |
| `val(meta), path(assignments)` | `tuple` | -           |

### Outputs

| Name        | Type    | Emit | Description |
| ----------- | ------- | ---- | ----------- |
| `val(meta)` | `tuple` | -    | -           |

## extractMinimap2Reads {#extractminimap2reads}

_Defined in `subworkflows/minimap_pipeline.nf:141`_

### Inputs

| Name                                                                                         | Type    | Description |
| -------------------------------------------------------------------------------------------- | ------- | ----------- |
| `val(meta), path("alignment.bam"), path("alignment.bai"), path("bamstats"), val(n_unmapped)` | `tuple` | -           |

### Outputs

| Name        | Type    | Emit | Description |
| ----------- | ------- | ---- | ----------- |
| `val(meta)` | `tuple` | -    | -           |

## getAlignmentStats {#getalignmentstats}

_Defined in `subworkflows/minimap_pipeline.nf:181`_

### Inputs

| Name                                                                    | Type    | Description |
| ----------------------------------------------------------------------- | ------- | ----------- |
| `val(meta), path("input.bam"), path("input.bam.bai"), path("bamstats")` | `tuple` | -           |

### Outputs

| Name           | Type   | Emit | Description |
| -------------- | ------ | ---- | ----------- |
| `${meta.alias` | `path` | -    | -           |

## run_kraken2 {#run-kraken2}

_Defined in `subworkflows/kraken_pipeline.nf:8`_

### Inputs

| Name                                                | Type    | Description |
| --------------------------------------------------- | ------- | ----------- |
| `val(meta), path("reads.fq.gz"), path(fastq_stats)` | `tuple` | -           |

### Outputs

| Name        | Type    | Emit | Description |
| ----------- | ------- | ---- | ----------- |
| `val(meta)` | `tuple` | -    | -           |

## run_bracken {#run-bracken}

_Defined in `subworkflows/kraken_pipeline.nf:72`_

### Inputs

| Name                                                                 | Type    | Description |
| -------------------------------------------------------------------- | ------- | ----------- |
| `val(meta), path("kraken2.report"), path("kraken2.assignments.tsv")` | `tuple` | -           |
| `bracken_length.txt`                                                 | `path`  | -           |

### Outputs

| Name        | Type    | Emit | Description |
| ----------- | ------- | ---- | ----------- |
| `val(meta)` | `tuple` | -    | -           |

## output_kraken2_read_assignments {#output-kraken2-read-assignments}

_Defined in `subworkflows/kraken_pipeline.nf:129`_

### Inputs

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| `val(meta)` | `tuple` | -           |

### Outputs

| Name                                                    | Type    | Emit | Description |
| ------------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("*_lineages.kraken2.assignments.tsv")` | `tuple` | -    | -           |

## exclude_host_reads {#exclude-host-reads}

_Defined in `subworkflows/common_pipeline.nf:1`_

### Inputs

| Name                                                | Type    | Description |
| --------------------------------------------------- | ------- | ----------- |
| `val(meta), path(concat_seqs), path(fastcat_stats)` | `tuple` | -           |

### Outputs

| Name                                                                                                | Type    | Emit          | Description |
| --------------------------------------------------------------------------------------------------- | ------- | ------------- | ----------- |
| `val(meta), path("*.unmapped.fastq.gz"), path("stats_unmapped"), env(n_seqs_passed_host_depletion)` | `tuple` | `fastq`       | -           |
| `val(meta), path("*.host.bam"), path("*.host.bam.bai")`                                             | `tuple` | `host_bam`    | -           |
| `val(meta), path("*.unmapped.bam"), path("*.unmapped.bam.bai")`                                     | `tuple` | `no_host_bam` | -           |

## fastcat {#fastcat}

_Defined in `lib/ingress.nf:587`_

### Inputs

| Name                                               | Type    | Description |
| -------------------------------------------------- | ------- | ----------- |
| `val(meta), path(input_src, stageAs: "input_src")` | `tuple` | -           |

### Outputs

| Name                                                                | Type    | Emit | Description |
| ------------------------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("fastq_chunks/*.fastq.gz"), path("fastcat_stats")` | `tuple` | -    | -           |

## checkBamHeaders {#checkbamheaders}

_Defined in `lib/ingress.nf:650`_

### Inputs

| Name                                      | Type    | Description |
| ----------------------------------------- | ------- | ----------- |
| `val(meta), path("input_dir/reads*.bam")` | `tuple` | -           |

### Outputs

| Name                                                                                                                  | Type    | Emit | Description |
| --------------------------------------------------------------------------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("input_dir/reads*.bam", includeInputs: true), env(IS_UNALIGNED), env(MIXED_HEADERS), env(IS_SORTED)` | `tuple` | -    | -           |

## validateIndex {#validateindex}

_Defined in `lib/ingress.nf:672`_

### Inputs

| Name                                                  | Type    | Description |
| ----------------------------------------------------- | ------- | ----------- |
| `val(meta), path("reads.bam"), path("reads.bam.bai")` | `tuple` | -           |

### Outputs

| Name                                                                                                                  | Type    | Emit | Description |
| --------------------------------------------------------------------------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("reads.bam", includeInputs: true), path("reads.bam.bai", includeInputs: true), env(HAS_VALID_INDEX)` | `tuple` | -    | -           |

## mergeBams {#mergebams}

_Defined in `lib/ingress.nf:698`_

### Inputs

| Name                                       | Type    | Description |
| ------------------------------------------ | ------- | ----------- |
| `val(meta), path("input_bams/reads*.bam")` | `tuple` | -           |

### Outputs

| Name                                                  | Type    | Emit | Description |
| ----------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("reads.bam"), path("reads.bam.bai")` | `tuple` | -    | -           |

## catSortBams {#catsortbams}

_Defined in `lib/ingress.nf:715`_

### Inputs

| Name                                       | Type    | Description |
| ------------------------------------------ | ------- | ----------- |
| `val(meta), path("input_bams/reads*.bam")` | `tuple` | -           |

### Outputs

| Name                                                  | Type    | Emit | Description |
| ----------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("reads.bam"), path("reads.bam.bai")` | `tuple` | -    | -           |

## sortBam {#sortbam}

_Defined in `lib/ingress.nf:731`_

### Inputs

| Name                           | Type    | Description |
| ------------------------------ | ------- | ----------- |
| `val(meta), path("reads.bam")` | `tuple` | -           |

### Outputs

| Name                                                                | Type    | Emit | Description |
| ------------------------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("reads.sorted.bam"), path("reads.sorted.bam.bai")` | `tuple` | -    | -           |

## bamstats {#bamstats}

_Defined in `lib/ingress.nf:746`_

### Inputs

| Name                                                  | Type    | Description |
| ----------------------------------------------------- | ------- | ----------- |
| `val(meta), path("reads.bam"), path("reads.bam.bai")` | `tuple` | -           |

### Outputs

| Name                                                                            | Type    | Emit | Description |
| ------------------------------------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("reads.bam"), path("reads.bam.bai"), path("bamstats_results")` | `tuple` | -    | -           |

## move_or_compress_fq_file {#move-or-compress-fq-file}

_Defined in `lib/ingress.nf:792`_

### Inputs

| Name                     | Type    | Description |
| ------------------------ | ------- | ----------- |
| `val(meta), path(input)` | `tuple` | -           |

### Outputs

| Name                               | Type    | Emit | Description |
| ---------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("seqs.fastq.gz")` | `tuple` | -    | -           |

## split_fq_file {#split-fq-file}

_Defined in `lib/ingress.nf:818`_

### Inputs

| Name                     | Type    | Description |
| ------------------------ | ------- | ----------- |
| `val(meta), path(input)` | `tuple` | -           |

### Outputs

| Name                                         | Type    | Emit | Description |
| -------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("fastq_chunks/*.fastq.gz")` | `tuple` | -    | -           |

## validate_sample_sheet {#validate-sample-sheet}

_Defined in `lib/ingress.nf:1219`_

Python script for validating a sample sheet. The script will write messages to STDOUT if the sample
sheet is invalid. In case there are no issues, no message is emitted. The sample sheet will be
published to the output dir.

### Inputs

| Name               | Type   | Description |
| ------------------ | ------ | ----------- |
| `sample_sheet.csv` | `path` | -           |

### Outputs

| Name                       | Type    | Emit | Description |
| -------------------------- | ------- | ---- | ----------- |
| `path("sample_sheet.csv")` | `tuple` | -    | -           |

## samtools_index {#samtools-index}

_Defined in `lib/ingress.nf:1238`_

### Inputs

| Name                           | Type    | Description |
| ------------------------------ | ------- | ----------- |
| `val(meta), path("reads.bam")` | `tuple` | -           |

### Outputs

| Name                                                  | Type    | Emit | Description |
| ----------------------------------------------------- | ------- | ---- | ----------- |
| `val(meta), path("reads.bam"), path("reads.bam.bai")` | `tuple` | -    | -           |

## getParams {#getparams}

_Defined in `lib/common.nf:3`_

### Outputs

| Name          | Type   | Emit | Description |
| ------------- | ------ | ---- | ----------- |
| `params.json` | `path` | -    | -           |

## configure_igv {#configure-igv}

_Defined in `lib/common.nf:19`_

### Inputs

| Name             | Type   | Description |
| ---------------- | ------ | ----------- |
| `file-names.txt` | `path` | -           |

### Outputs

| Name       | Type   | Emit | Description |
| ---------- | ------ | ---- | ----------- |
| `igv.json` | `path` | -    | -           |

## abricate {#abricate}

_Defined in `modules/local/amr.nf:1`_

### Inputs

| Name                                                      | Type    | Description |
| --------------------------------------------------------- | ------- | ----------- |
| `val(meta), path("input_reads.fastq.gz"), path("stats/")` | `tuple` | -           |

### Outputs

| Name        | Type    | Emit | Description |
| ----------- | ------- | ---- | ----------- |
| `val(meta)` | `tuple` | -    | -           |

## abricate_json {#abricate-json}

_Defined in `modules/local/amr.nf:24`_

### Inputs

| Name        | Type    | Description |
| ----------- | ------- | ----------- |
| `val(meta)` | `tuple` | -           |

### Outputs

| Name        | Type    | Emit | Description |
| ----------- | ------- | ---- | ----------- |
| `val(meta)` | `tuple` | -    | -           |

## filter_references {#filter-references}

_Defined in `modules/local/igv_related.nf:6`_

### Inputs

| Name              | Type   | Description |
| ----------------- | ------ | ----------- |
| `bam_flagstats/*` | `path` | -           |

### Outputs

| Name                                                                                                                 | Type    | Emit | Description |
| -------------------------------------------------------------------------------------------------------------------- | ------- | ---- | ----------- |
| `path("reduced_reference.fasta.gz"), path("reduced_reference.fasta.gz.fai"), path("reduced_reference.fasta.gz.gzi")` | `tuple` | -    | -           |

## abricateVersion {#abricateversion}

_Defined in `modules/local/common.nf:3`_

### Inputs

| Name                 | Type   | Description |
| -------------------- | ------ | ----------- |
| `input_versions.txt` | `path` | -           |

### Outputs

| Name           | Type   | Emit | Description |
| -------------- | ------ | ---- | ----------- |
| `versions.txt` | `path` | -    | -           |

## getVersions {#getversions}

_Defined in `modules/local/common.nf:19`_

### Outputs

| Name           | Type   | Emit | Description |
| -------------- | ------ | ---- | ----------- |
| `versions.txt` | `path` | -    | -           |

## getVersionsCommon {#getversionscommon}

_Defined in `modules/local/common.nf:41`_

### Inputs

| Name           | Type   | Description |
| -------------- | ------ | ----------- |
| `versions.txt` | `path` | -           |

### Outputs

| Name               | Type   | Emit | Description |
| ------------------ | ------ | ---- | ----------- |
| `versions_all.txt` | `path` | -    | -           |

## createAbundanceTables {#createabundancetables}

_Defined in `modules/local/common.nf:62`_

### Inputs

| Name         | Type   | Description |
| ------------ | ------ | ----------- |
| `lineages/*` | `path` | -           |

### Outputs

| Name                    | Type   | Emit            | Description |
| ----------------------- | ------ | --------------- | ----------- |
| `abundance_table_*.tsv` | `path` | `abundance_tsv` | -           |

## publishReads {#publishreads}

_Defined in `modules/local/common.nf:84`_

### Inputs

| Name                                              | Type    | Description |
| ------------------------------------------------- | ------- | ----------- |
| `val(meta), path("reads.fq.gz"), path("ids.txt")` | `tuple` | -           |

### Outputs

| Name           | Type   | Emit | Description |
| -------------- | ------ | ---- | ----------- |
| `${meta.alias` | `path` | -    | -           |

## publish {#publish}

_Defined in `modules/local/common.nf:104`_

### Inputs

| Name                        | Type    | Description |
| --------------------------- | ------- | ----------- |
| `path(fname), val(dirname)` | `tuple` | -           |

### Outputs

| Name    | Type   | Emit | Description |
| ------- | ------ | ---- | ----------- |
| `fname` | `path` | -    | -           |

## makeReport {#makereport}

_Defined in `modules/local/common.nf:124`_

### Inputs

| Name                  | Type   | Description |
| --------------------- | ------ | ----------- |
| `abundance_table.tsv` | `path` | -           |
| `alignment_stats/*`   | `path` | -           |
| `lineages/*`          | `path` | -           |
| `versions/*`          | `path` | -           |
| `params.json`         | `path` | -           |
| `amr/*`               | `path` | -           |

### Outputs

| Name            | Type   | Emit | Description |
| --------------- | ------ | ---- | ----------- |
| `${report_name` | `path` | -    | -           |

---

_This pipeline was built with [Nextflow](https://nextflow.io). Documentation generated by
[nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:27:31 UTC._
