# Workflows

This page documents all workflows in the pipeline.

## Contents

- [NFCORE_RNAVAR](#nfcore-rnavar)
- [(entry)](#entry) _(entry point)_
- [RNAVAR](#rnavar)
- [BAM_STATS_SAMTOOLS](#bam-stats-samtools)
- [FASTQ_ALIGN_STAR](#fastq-align-star)
- [VCF_ANNOTATE_SNPEFF](#vcf-annotate-snpeff)
- [VCF_ANNOTATE_ENSEMBLVEP](#vcf-annotate-ensemblvep)
- [BAM_MARKDUPLICATES_PICARD](#bam-markduplicates-picard)
- [BAM_SORT_STATS_SAMTOOLS](#bam-sort-stats-samtools)
- [PREPARE_ALIGNMENT](#prepare-alignment)
- [SPLITNCIGAR](#splitncigar)
- [RECALIBRATE](#recalibrate)
- [DOWNLOAD_CACHE_SNPEFF_VEP](#download-cache-snpeff-vep)
- [PIPELINE_INITIALISATION](#pipeline-initialisation)
- [PIPELINE_COMPLETION](#pipeline-completion)
- [ANNOTATION_CACHE_INITIALISATION](#annotation-cache-initialisation)
- [PREPARE_GENOME](#prepare-genome)
- [VCF_ANNOTATE_ALL](#vcf-annotate-all)

## NFCORE_RNAVAR {#nfcore-rnavar}

_Defined in `main.nf:63`_

### Inputs

| Name          | Description |
| ------------- | ----------- |
| `samplesheet` | -           |
| `align`       | -           |

### Outputs

| Name | Description |
| ---- | ----------- |
| `?`  | -           |
| `?`  | -           |

## (entry) {#entry}

**Entry workflow**

_Defined in `main.nf:211`_

## RNAVAR {#rnavar}

_Defined in `workflows/rnavar.nf:83`_

Main workflow for RNA variant calling analysis. This workflow performs end-to-end RNA-seq variant
calling including:

- Quality control with FastQC
- Read alignment with STAR
- Duplicate marking with Picard
- Split N CIGAR reads for RNA-seq data
- Base quality score recalibration (BQSR)
- Variant calling with GATK HaplotypeCaller
- Variant filtering
- Variant annotation with SnpEff and VEP
- HLA typing with seq2HLA (optional) The workflow supports multiple input types including FASTQ,
  BAM, CRAM, and VCF files.

### Inputs

| Name                       | Description |
| -------------------------- | ----------- |
| `input`                    | -           |
| `bcftools_annotations`     | -           |
| `bcftools_annotations_tbi` | -           |
| `bcftools_columns`         | -           |
| `bcftools_header_lines`    | -           |
| `dbsnp`                    | -           |
| `dbsnp_tbi`                | -           |
| `dict`                     | -           |
| `exon_bed`                 | -           |
| `fasta`                    | -           |
| `fasta_fai`                | -           |
| `gtf`                      | -           |
| `known_sites`              | -           |
| `known_sites_tbi`          | -           |
| `star_index`               | -           |
| `snpeff_cache`             | -           |
| `snpeff_db`                | -           |
| `vep_genome`               | -           |
| `vep_species`              | -           |
| `vep_cache_version`        | -           |
| `vep_include_fasta`        | -           |
| `vep_cache`                | -           |
| `vep_extra_files`          | -           |
| `seq_center`               | -           |
| `seq_platform`             | -           |
| `aligner`                  | -           |
| `bam_csi_index`            | -           |
| `extract_umi`              | -           |
| `generate_gvcf`            | -           |
| `skip_multiqc`             | -           |
| `skip_baserecalibration`   | -           |
| `skip_intervallisttools`   | -           |
| `skip_variantannotation`   | -           |
| `skip_variantfiltration`   | -           |
| `star_ignore_sjdbgtf`      | -           |
| `tools`                    | -           |

### Outputs

| Name | Description |
| ---- | ----------- |
| `?`  | -           |
| `?`  | -           |

## BAM_STATS_SAMTOOLS {#bam-stats-samtools}

_Defined in `subworkflows/nf-core/bam_stats_samtools/main.nf:9`_

**Keywords:** `statistics`, `counts`, `bam`, `sam`, `cram`

Produces comprehensive statistics from SAM/BAM/CRAM file

### Components

This workflow uses the following modules/subworkflows:

- `samtools/stats`
- `samtools/idxstats`
- `samtools/flagstat`

### Inputs

| Name         | Description                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------- |
| `ch_bam_bai` | The input channel containing the BAM/CRAM and it's index Structure: [ val(meta), path(bam), path(bai) ] |
| `ch_fasta`   | Reference genome fasta file Structure: [ path(fasta) ]                                                  |

### Outputs

| Name       | Description                                                                       |
| ---------- | --------------------------------------------------------------------------------- |
| `stats`    | File containing samtools stats output Structure: [ val(meta), path(stats) ]       |
| `flagstat` | File containing samtools flagstat output Structure: [ val(meta), path(flagstat) ] |
| `idxstats` | File containing samtools idxstats output Structure: [ val(meta), path(idxstats)]  |
| `versions` | Files containing software versions Structure: [ path(versions.yml) ]              |

**Authors:** [@drpatelh](https://github.com/drpatelh) **Maintainers:**
[@drpatelh](https://github.com/drpatelh)

## FASTQ_ALIGN_STAR {#fastq-align-star}

_Defined in `subworkflows/nf-core/fastq_align_star/main.nf:6`_

**Keywords:** `align`, `fasta`, `genome`, `reference`

Align reads to a reference genome using bowtie2 then sort with samtools

### Components

This workflow uses the following modules/subworkflows:

- `star/align`
- `samtools/sort`
- `samtools/index`
- `samtools/stats`
- `samtools/idxstats`
- `samtools/flagstat`
- `bam_sort_stats_samtools`

### Inputs

| Name                      | Description                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| `ch_reads`                | List of input FastQ files of size 1 and 2 for single-end and paired-end data, respectively. Structure: [ val(meta), [ path(reads) ] ] |
| `ch_index`                | STAR genome index                                                                                                                     |
| `ch_gtf`                  | GTF file used to set the splice junctions with the --sjdbGTFfile flag                                                                 |
| `val_star_ignore_sjdbgtf` | If true the --sjdbGTFfile flag is set                                                                                                 |
| `val_seq_platform`        | Sequencing platform to be added to the bam header using the --outSAMattrRGline flag                                                   |
| `val_seq_center`          | Sequencing center to be added to the bam header using the --outSAMattrRGline flag                                                     |
| `ch_fasta`                | Reference genome fasta file                                                                                                           |
| `ch_transcripts_fasta`    | Optional reference genome fasta file                                                                                                  |

### Outputs

| Name                  | Description                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `orig_bam`            | Output BAM file containing read alignments Structure: [ val(meta), path(bam) ]                                   |
| `log_final`           | STAR final log file Structure: [ val(meta), path(log_final) ]                                                    |
| `log_out`             | STAR log out file Structure: [ val(meta), path(log_out) ]                                                        |
| `log_progress`        | STAR log progress file Structure: [ val(meta), path(log_progress) ]                                              |
| `bam_sorted`          | Sorted BAM file of read alignments (optional) Structure: [ val(meta), path(bam) ]                                |
| `orig_bam_transcript` | Output BAM file of transcriptome alignment (optional) Structure: [ val(meta), path(bam) ]                        |
| `fastq`               | Unmapped FastQ files (optional) Structure: [ val(meta), path(fastq) ]                                            |
| `tab`                 | STAR output tab file(s) (optional) Structure: [ val(meta), path(tab) ]                                           |
| `bam`                 | BAM file ordered by samtools Structure: [ val(meta), path(bam) ]                                                 |
| `bai`                 | BAI index of the ordered BAM file Structure: [ val(meta), path(bai) ]                                            |
| `stats`               | File containing samtools stats output Structure: [ val(meta), path(stats) ]                                      |
| `flagstat`            | File containing samtools flagstat output Structure: [ val(meta), path(flagstat) ]                                |
| `idxstats`            | File containing samtools idxstats output Structure: [ val(meta), path(idxstats) ]                                |
| `bam_transcript`      | Transcriptome-level BAM file ordered by samtools (optional) Structure: [ val(meta), path(bam) ]                  |
| `bai_transcript`      | Transcriptome-level BAI index of the ordered BAM file (optional) Structure: [ val(meta), path(bai) ]             |
| `stats_transcript`    | Transcriptome-level file containing samtools stats output (optional) Structure: [ val(meta), path(stats) ]       |
| `flagstat_transcript` | Transcriptome-level file containing samtools flagstat output (optional) Structure: [ val(meta), path(flagstat) ] |
| `idxstats_transcript` | Transcriptome-level file containing samtools idxstats output (optional) Structure: [ val(meta), path(idxstats) ] |
| `versions`            | File containing software versions                                                                                |

**Authors:** [@JoseEspinosa](https://github.com/JoseEspinosa) **Maintainers:**
[@JoseEspinosa](https://github.com/JoseEspinosa)

## VCF_ANNOTATE_SNPEFF {#vcf-annotate-snpeff}

_Defined in `subworkflows/nf-core/vcf_annotate_snpeff/main.nf:8`_

**Keywords:** `vcf`, `annotation`, `snpeff`

Perform annotation with snpEff and bgzip + tabix index the resulting VCF file

### Components

This workflow uses the following modules/subworkflows:

- `snpeff`
- `snpeff/snpeff`
- `tabix/bgziptabix`

### Inputs

| Name              | Description                                                                |
| ----------------- | -------------------------------------------------------------------------- |
| `ch_vcf`          | vcf file Structure: [ val(meta), path(vcf) ]                               |
| `val_snpeff_db`   | db version to use                                                          |
| `ch_snpeff_cache` | path to root cache folder for snpEff (optional) Structure: [ path(cache) ] |

### Outputs

| Name        | Description                                                                      |
| ----------- | -------------------------------------------------------------------------------- |
| `vcf_tbi`   | Compressed vcf file + tabix index Structure: [ val(meta), path(vcf), path(tbi) ] |
| `reports`   | html reports Structure: [ path(html) ]                                           |
| `summary`   | html reports Structure: [ path(csv) ]                                            |
| `genes_txt` | html reports Structure: [ path(txt) ]                                            |
| `versions`  | Files containing software versions Structure: [ path(versions.yml) ]             |

**Authors:** [@maxulysse](https://github.com/maxulysse) **Maintainers:**
[@maxulysse](https://github.com/maxulysse)

## VCF_ANNOTATE_ENSEMBLVEP {#vcf-annotate-ensemblvep}

_Defined in `subworkflows/nf-core/vcf_annotate_ensemblvep/main.nf:8`_

**Keywords:** `vcf`, `annotation`, `ensemblvep`

Perform annotation with ensemblvep and bgzip + tabix index the resulting VCF file

### Components

This workflow uses the following modules/subworkflows:

- `ensemblvep/vep`
- `tabix/tabix`

### Inputs

| Name                | Description                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `ch_vcf`            | vcf file to annotate Structure: [ val(meta), path(vcf), [path(custom_file1), path(custom_file2)... (optional)] ] |
| `ch_fasta`          | Reference genome fasta file (optional) Structure: [ val(meta2), path(fasta) ]                                    |
| `val_genome`        | genome to use                                                                                                    |
| `val_species`       | species to use                                                                                                   |
| `val_cache_version` | cache version to use                                                                                             |
| `ch_cache`          | the root cache folder for ensemblvep (optional) Structure: [ val(meta3), path(cache) ]                           |
| `ch_extra_files`    | any extra files needed by plugins for ensemblvep (optional) Structure: [ path(file1), path(file2)... ]           |

### Outputs

| Name       | Description                                                                      |
| ---------- | -------------------------------------------------------------------------------- |
| `vcf_tbi`  | Compressed vcf file + tabix index Structure: [ val(meta), path(vcf), path(tbi) ] |
| `json`     | json file Structure: [ val(meta), path(json) ]                                   |
| `tab`      | tab file Structure: [ val(meta), path(tab) ]                                     |
| `reports`  | html reports                                                                     |
| `versions` | File containing software versions                                                |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm),
[@nvnieuwk](https://github.com/nvnieuwk) **Maintainers:**
[@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm),
[@nvnieuwk](https://github.com/nvnieuwk)

## BAM_MARKDUPLICATES_PICARD {#bam-markduplicates-picard}

_Defined in `subworkflows/nf-core/bam_markduplicates_picard/main.nf:9`_

**Keywords:** `markduplicates`, `bam`, `sam`, `cram`

Picard MarkDuplicates, index BAM file and run samtools stats, flagstat and idxstats

### Components

This workflow uses the following modules/subworkflows:

- `picard/markduplicates`
- `samtools/index`
- `samtools/stats`
- `samtools/idxstats`
- `samtools/flagstat`
- `bam_stats_samtools`

### Inputs

| Name       | Description                                                                    |
| ---------- | ------------------------------------------------------------------------------ |
| `ch_reads` | Sequence reads in BAM/CRAM/SAM format Structure: [ val(meta), path(reads) ]    |
| `ch_fasta` | Reference genome fasta file required for CRAM input Structure: [ path(fasta) ] |
| `ch_fasta` | Index of the reference genome fasta file Structure: [ path(fai) ]              |

### Outputs

| Name       | Description                                                                       |
| ---------- | --------------------------------------------------------------------------------- |
| `bam`      | processed BAM/SAM file Structure: [ val(meta), path(bam) ]                        |
| `bai`      | BAM/SAM samtools index Structure: [ val(meta), path(bai) ]                        |
| `cram`     | processed CRAM file Structure: [ val(meta), path(cram) ]                          |
| `crai`     | CRAM samtools index Structure: [ val(meta), path(crai) ]                          |
| `csi`      | CSI samtools index Structure: [ val(meta), path(csi) ]                            |
| `stats`    | File containing samtools stats output Structure: [ val(meta), path(stats) ]       |
| `flagstat` | File containing samtools flagstat output Structure: [ val(meta), path(flagstat) ] |
| `idxstats` | File containing samtools idxstats output Structure: [ val(meta), path(idxstats) ] |
| `versions` | Files containing software versions Structure: [ path(versions.yml) ]              |

**Authors:** [@dmarron](https://github.com/dmarron), [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@dmarron](https://github.com/dmarron), [@drpatelh](https://github.com/drpatelh)

## BAM_SORT_STATS_SAMTOOLS {#bam-sort-stats-samtools}

_Defined in `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:9`_

**Keywords:** `sort`, `bam`, `sam`, `cram`

Sort SAM/BAM/CRAM file

### Components

This workflow uses the following modules/subworkflows:

- `samtools/sort`
- `samtools/index`
- `samtools/stats`
- `samtools/idxstats`
- `samtools/flagstat`
- `bam_stats_samtools`

### Inputs

| Name    | Description                                                                   |
| ------- | ----------------------------------------------------------------------------- |
| `meta`  | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam`   | BAM/CRAM/SAM file                                                             |
| `fasta` | Reference genome fasta file                                                   |

### Outputs

| Name       | Description                                                                   |
| ---------- | ----------------------------------------------------------------------------- |
| `meta`     | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam`      | Sorted BAM/CRAM/SAM file                                                      |
| `bai`      | BAM/CRAM/SAM index file                                                       |
| `crai`     | BAM/CRAM/SAM index file                                                       |
| `stats`    | File containing samtools stats output                                         |
| `flagstat` | File containing samtools flagstat output                                      |
| `idxstats` | File containing samtools idxstats output                                      |
| `versions` | File containing software versions                                             |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels)

## PREPARE_ALIGNMENT {#prepare-alignment}

_Defined in `subworkflows/local/prepare_alignment/main.nf:7`_

### Inputs

| Name   | Description |
| ------ | ----------- |
| `cram` | -           |
| `bam`  | -           |

### Outputs

| Name       | Description |
| ---------- | ----------- |
| `bam`      | -           |
| `versions` | -           |

## SPLITNCIGAR {#splitncigar}

_Defined in `subworkflows/local/splitncigar/main.nf:25`_

Split reads that contain N CIGAR operations for RNA-seq variant calling. This subworkflow handles
the GATK SplitNCigarReads step which is essential for RNA-seq variant calling. It splits reads that
span introns (N in CIGAR) and reassigns mapping qualities to meet GATK requirements. The workflow
processes BAM files in parallel across genomic intervals, then merges and indexes the results for
efficient downstream processing.

### Inputs

| Name        | Description |
| ----------- | ----------- |
| `bam`       | -           |
| `fasta`     | -           |
| `fai`       | -           |
| `dict`      | -           |
| `intervals` | -           |

### Outputs

| Name       | Description |
| ---------- | ----------- |
| `bam_bai`  | -           |
| `versions` | -           |

## RECALIBRATE {#recalibrate}

_Defined in `subworkflows/local/recalibrate/main.nf:27`_

Apply base quality score recalibration (BQSR) to BAM files. This subworkflow applies the BQSR model
generated by GATK BaseRecalibrator to adjust base quality scores in BAM files. Recalibrated quality
scores improve the accuracy of variant calling by correcting systematic errors in the original
quality scores assigned by the sequencing machine. Optionally generates alignment statistics using
samtools stats for QC.

### Inputs

| Name            | Description |
| --------------- | ----------- |
| `skip_samtools` | -           |
| `bam`           | -           |
| `dict`          | -           |
| `fai`           | -           |
| `fasta`         | -           |

### Outputs

| Name       | Description |
| ---------- | ----------- |
| `bam`      | -           |
| `qc`       | -           |
| `versions` | -           |

## DOWNLOAD_CACHE_SNPEFF_VEP {#download-cache-snpeff-vep}

_Defined in `subworkflows/local/download_cache_snpeff_vep/main.nf:14`_

### Inputs

| Name              | Description |
| ----------------- | ----------- |
| `ensemblvep_info` | -           |
| `snpeff_info`     | -           |

### Outputs

| Name               | Description |
| ------------------ | ----------- |
| `ensemblvep_cache` | -           |
| `snpeff_cache`     | -           |

## PIPELINE_INITIALISATION {#pipeline-initialisation}

_Defined in `subworkflows/local/utils_nfcore_rnavar_pipeline/main.nf:51`_

Initialize the nf-core/rnavar pipeline. Performs all setup tasks required before running the main
workflow:

- Display version information if requested
- Validate parameters against the schema
- Check Conda channel configuration
- Parse and validate the input samplesheet
- Generate parameter summary for logging

### Inputs

| Name                | Description |
| ------------------- | ----------- |
| `version`           | -           |
| `validate_params`   | -           |
| `nextflow_cli_args` | -           |
| `outdir`            | -           |
| `input`             | -           |
| `help`              | -           |
| `help_full`         | -           |
| `show_hidden`       | -           |

### Outputs

| Name          | Description |
| ------------- | ----------- |
| `samplesheet` | -           |
| `align`       | -           |
| `versions`    | -           |

## PIPELINE_COMPLETION {#pipeline-completion}

_Defined in `subworkflows/local/utils_nfcore_rnavar_pipeline/main.nf:198`_

Handle pipeline completion tasks. Executes cleanup and notification tasks when the pipeline
finishes:

- Send completion email with run summary
- Generate completion summary to stdout
- Send notifications to messaging platforms (Slack, Teams, etc.)
- Log error messages for failed runs

### Inputs

| Name              | Description |
| ----------------- | ----------- |
| `email`           | -           |
| `email_on_fail`   | -           |
| `plaintext_email` | -           |
| `outdir`          | -           |
| `monochrome_logs` | -           |
| `hook_url`        | -           |
| `multiqc_report`  | -           |

### Outputs

| Name     | Description |
| -------- | ----------- |
| `<none>` | -           |

## ANNOTATION_CACHE_INITIALISATION {#annotation-cache-initialisation}

_Defined in `subworkflows/local/annotation_cache_initialisation/main.nf:11`_

### Inputs

| Name                | Description |
| ------------------- | ----------- |
| `snpeff_enabled`    | -           |
| `snpeff_cache`      | -           |
| `snpeff_db`         | -           |
| `vep_enabled`       | -           |
| `vep_cache`         | -           |
| `vep_species`       | -           |
| `vep_cache_version` | -           |
| `vep_genome`        | -           |
| `vep_custom_args`   | -           |
| `help_message`      | -           |

### Outputs

| Name | Description |
| ---- | ----------- |
| `?`  | -           |
| `?`  | -           |

## PREPARE_GENOME {#prepare-genome}

_Defined in `subworkflows/local/prepare_genome/main.nf:22`_

### Inputs

| Name                       | Description |
| -------------------------- | ----------- |
| `bcftools_annotations`     | -           |
| `bcftools_annotations_tbi` | -           |
| `dbsnp`                    | -           |
| `dbsnp_tbi`                | -           |
| `dict`                     | -           |
| `exon_bed`                 | -           |
| `fasta`                    | -           |
| `fasta_fai`                | -           |
| `gff`                      | -           |
| `gtf`                      | -           |
| `known_indels`             | -           |
| `known_indels_tbi`         | -           |
| `star_index`               | -           |
| `feature_type`             | -           |
| `skip_exon_bed_check`      | -           |
| `align`                    | -           |

### Outputs

| Name               | Description |
| ------------------ | ----------- |
| `bcfann`           | -           |
| `bcfann_tbi`       | -           |
| `dbsnp`            | -           |
| `dbsnp_tbi`        | -           |
| `dict`             | -           |
| `exon_bed`         | -           |
| `fasta`            | -           |
| `fasta_fai`        | -           |
| `gtf`              | -           |
| `known_indels`     | -           |
| `known_indels_tbi` | -           |
| `known_sites`      | -           |
| `known_sites_tbi`  | -           |
| `star_index`       | -           |
| `versions`         | -           |

## VCF_ANNOTATE_ALL {#vcf-annotate-all}

_Defined in `subworkflows/local/vcf_annotate_all/main.nf:37`_

Annotate variants using multiple annotation tools. This subworkflow provides flexible variant
annotation using one or more tools:

- **SnpEff**: Functional annotation and effect prediction
- **VEP (Ensembl Variant Effect Predictor)**: Comprehensive variant annotation
- **BCFtools annotate**: Add custom annotations from external files
- **Merge**: Combined SnpEff + VEP annotation The tools to use are specified via the `tools`
  parameter as a comma-separated list (e.g., "snpeff,vep" or "merge").

### Inputs

| Name                         | Description |
| ---------------------------- | ----------- |
| `vcf`                        | -           |
| `fasta`                      | -           |
| `tools`                      | -           |
| `snpeff_db`                  | -           |
| `snpeff_cache`               | -           |
| `vep_genome`                 | -           |
| `vep_species`                | -           |
| `vep_cache_version`          | -           |
| `vep_cache`                  | -           |
| `vep_extra_files`            | -           |
| `bcftools_annotations`       | -           |
| `bcftools_annotations_index` | -           |
| `bcftools_columns`           | -           |
| `bcftools_header_lines`      | -           |

### Outputs

| Name | Description |
| ---- | ----------- |
| `?`  | -           |
| `?`  | -           |
| `?`  | -           |
| `?`  | -           |

---

_This pipeline was built with [Nextflow](https://nextflow.io). Documentation generated by
[nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:23:12 UTC._
