# Workflows

This page documents all workflows in the pipeline.

## Contents

- [NFCORE_RNAVAR](#nfcore-rnavar)
- [(entry)](#entry) *(entry point)*
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

*Defined in `main.nf:63`*

### Inputs

| Name | Description |
|------|-------------|
| `samplesheet` | - |
| `align` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


## (entry) {#entry}

**Entry workflow**

*Defined in `main.nf:211`*


## RNAVAR {#rnavar}

*Defined in `workflows/rnavar.nf:83`*

Main workflow for RNA variant calling analysis.
This workflow performs end-to-end RNA-seq variant calling including:
- Quality control with FastQC
- Read alignment with STAR
- Duplicate marking with Picard
- Split N CIGAR reads for RNA-seq data
- Base quality score recalibration (BQSR)
- Variant calling with GATK HaplotypeCaller
- Variant filtering
- Variant annotation with SnpEff and VEP
- HLA typing with seq2HLA (optional)
The workflow supports multiple input types including FASTQ, BAM, CRAM, and VCF files.

### Inputs

| Name | Description |
|------|-------------|
| `input` | - |
| `bcftools_annotations` | - |
| `bcftools_annotations_tbi` | - |
| `bcftools_columns` | - |
| `bcftools_header_lines` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dict` | - |
| `exon_bed` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `gtf` | - |
| `known_sites` | - |
| `known_sites_tbi` | - |
| `star_index` | - |
| `snpeff_cache` | - |
| `snpeff_db` | - |
| `vep_genome` | - |
| `vep_species` | - |
| `vep_cache_version` | - |
| `vep_include_fasta` | - |
| `vep_cache` | - |
| `vep_extra_files` | - |
| `seq_center` | - |
| `seq_platform` | - |
| `aligner` | - |
| `bam_csi_index` | - |
| `extract_umi` | - |
| `generate_gvcf` | - |
| `skip_multiqc` | - |
| `skip_baserecalibration` | - |
| `skip_intervallisttools` | - |
| `skip_variantannotation` | - |
| `skip_variantfiltration` | - |
| `star_ignore_sjdbgtf` | - |
| `tools` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


## BAM_STATS_SAMTOOLS {#bam-stats-samtools}

*Defined in `subworkflows/nf-core/bam_stats_samtools/main.nf:9`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_bam_bai` | - |
| `ch_fasta` | - |

### Outputs

| Name | Description |
|------|-------------|
| `stats` | - |
| `flagstat` | - |
| `idxstats` | - |
| `versions` | - |


## FASTQ_ALIGN_STAR {#fastq-align-star}

*Defined in `subworkflows/nf-core/fastq_align_star/main.nf:6`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_reads` | - |
| `ch_index` | - |
| `ch_gtf` | - |
| `val_star_ignore_sjdbgtf` | - |
| `val_seq_platform` | - |
| `val_seq_center` | - |
| `ch_fasta` | - |
| `ch_transcripts_fasta` | - |

### Outputs

| Name | Description |
|------|-------------|
| `orig_bam` | - |
| `log_final` | - |
| `log_out` | - |
| `log_progress` | - |
| `bam_sorted` | - |
| `fastq` | - |
| `tab` | - |
| `orig_bam_transcript` | - |
| `bam` | - |
| `bai` | - |
| `stats` | - |
| `flagstat` | - |
| `idxstats` | - |
| `bam_transcript` | - |
| `bai_transcript` | - |
| `stats_transcript` | - |
| `flagstat_transcript` | - |
| `idxstats_transcript` | - |
| `versions` | - |


## VCF_ANNOTATE_SNPEFF {#vcf-annotate-snpeff}

*Defined in `subworkflows/nf-core/vcf_annotate_snpeff/main.nf:8`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_vcf` | - |
| `val_snpeff_db` | - |
| `ch_snpeff_cache` | - |

### Outputs

| Name | Description |
|------|-------------|
| `vcf_tbi` | - |
| `reports` | - |
| `summary` | - |
| `genes_txt` | - |
| `versions` | - |


## VCF_ANNOTATE_ENSEMBLVEP {#vcf-annotate-ensemblvep}

*Defined in `subworkflows/nf-core/vcf_annotate_ensemblvep/main.nf:8`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_vcf` | - |
| `ch_fasta` | - |
| `val_genome` | - |
| `val_species` | - |
| `val_cache_version` | - |
| `ch_cache` | - |
| `ch_extra_files` | - |

### Outputs

| Name | Description |
|------|-------------|
| `vcf_tbi` | - |
| `json` | - |
| `tab` | - |
| `reports` | - |


## BAM_MARKDUPLICATES_PICARD {#bam-markduplicates-picard}

*Defined in `subworkflows/nf-core/bam_markduplicates_picard/main.nf:9`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_reads` | - |
| `ch_fasta` | - |
| `ch_fai` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `cram` | - |
| `metrics` | - |
| `bai` | - |
| `crai` | - |
| `csi` | - |
| `stats` | - |
| `flagstat` | - |
| `idxstats` | - |
| `versions` | - |


## BAM_SORT_STATS_SAMTOOLS {#bam-sort-stats-samtools}

*Defined in `subworkflows/nf-core/bam_sort_stats_samtools/main.nf:9`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_bam` | - |
| `ch_fasta` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `bai` | - |
| `csi` | - |
| `stats` | - |
| `flagstat` | - |
| `idxstats` | - |
| `versions` | - |


## PREPARE_ALIGNMENT {#prepare-alignment}

*Defined in `subworkflows/local/prepare_alignment/main.nf:7`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `bam` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `versions` | - |


## SPLITNCIGAR {#splitncigar}

*Defined in `subworkflows/local/splitncigar/main.nf:25`*

Split reads that contain N CIGAR operations for RNA-seq variant calling.
This subworkflow handles the GATK SplitNCigarReads step which is essential
for RNA-seq variant calling. It splits reads that span introns (N in CIGAR)
and reassigns mapping qualities to meet GATK requirements.
The workflow processes BAM files in parallel across genomic intervals,
then merges and indexes the results for efficient downstream processing.

### Inputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `fasta` | - |
| `fai` | - |
| `dict` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bam_bai` | - |
| `versions` | - |


## RECALIBRATE {#recalibrate}

*Defined in `subworkflows/local/recalibrate/main.nf:27`*

Apply base quality score recalibration (BQSR) to BAM files.
This subworkflow applies the BQSR model generated by GATK BaseRecalibrator
to adjust base quality scores in BAM files. Recalibrated quality scores
improve the accuracy of variant calling by correcting systematic errors
in the original quality scores assigned by the sequencing machine.
Optionally generates alignment statistics using samtools stats for QC.

### Inputs

| Name | Description |
|------|-------------|
| `skip_samtools` | - |
| `bam` | - |
| `dict` | - |
| `fai` | - |
| `fasta` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `qc` | - |
| `versions` | - |


## DOWNLOAD_CACHE_SNPEFF_VEP {#download-cache-snpeff-vep}

*Defined in `subworkflows/local/download_cache_snpeff_vep/main.nf:14`*

### Inputs

| Name | Description |
|------|-------------|
| `ensemblvep_info` | - |
| `snpeff_info` | - |

### Outputs

| Name | Description |
|------|-------------|
| `ensemblvep_cache` | - |
| `snpeff_cache` | - |


## PIPELINE_INITIALISATION {#pipeline-initialisation}

*Defined in `subworkflows/local/utils_nfcore_rnavar_pipeline/main.nf:51`*

Initialize the nf-core/rnavar pipeline.
Performs all setup tasks required before running the main workflow:
- Display version information if requested
- Validate parameters against the schema
- Check Conda channel configuration
- Parse and validate the input samplesheet
- Generate parameter summary for logging

### Inputs

| Name | Description |
|------|-------------|
| `version` | - |
| `validate_params` | - |
| `nextflow_cli_args` | - |
| `outdir` | - |
| `input` | - |
| `help` | - |
| `help_full` | - |
| `show_hidden` | - |

### Outputs

| Name | Description |
|------|-------------|
| `samplesheet` | - |
| `align` | - |
| `versions` | - |


## PIPELINE_COMPLETION {#pipeline-completion}

*Defined in `subworkflows/local/utils_nfcore_rnavar_pipeline/main.nf:198`*

Handle pipeline completion tasks.
Executes cleanup and notification tasks when the pipeline finishes:
- Send completion email with run summary
- Generate completion summary to stdout
- Send notifications to messaging platforms (Slack, Teams, etc.)
- Log error messages for failed runs

### Inputs

| Name | Description |
|------|-------------|
| `email` | - |
| `email_on_fail` | - |
| `plaintext_email` | - |
| `outdir` | - |
| `monochrome_logs` | - |
| `hook_url` | - |
| `multiqc_report` | - |

### Outputs

| Name | Description |
|------|-------------|
| `<none>` | - |


## ANNOTATION_CACHE_INITIALISATION {#annotation-cache-initialisation}

*Defined in `subworkflows/local/annotation_cache_initialisation/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `snpeff_enabled` | - |
| `snpeff_cache` | - |
| `snpeff_db` | - |
| `vep_enabled` | - |
| `vep_cache` | - |
| `vep_species` | - |
| `vep_cache_version` | - |
| `vep_genome` | - |
| `vep_custom_args` | - |
| `help_message` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


## PREPARE_GENOME {#prepare-genome}

*Defined in `subworkflows/local/prepare_genome/main.nf:22`*

### Inputs

| Name | Description |
|------|-------------|
| `bcftools_annotations` | - |
| `bcftools_annotations_tbi` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dict` | - |
| `exon_bed` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `gff` | - |
| `gtf` | - |
| `known_indels` | - |
| `known_indels_tbi` | - |
| `star_index` | - |
| `feature_type` | - |
| `skip_exon_bed_check` | - |
| `align` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bcfann` | - |
| `bcfann_tbi` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dict` | - |
| `exon_bed` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `gtf` | - |
| `known_indels` | - |
| `known_indels_tbi` | - |
| `known_sites` | - |
| `known_sites_tbi` | - |
| `star_index` | - |
| `versions` | - |


## VCF_ANNOTATE_ALL {#vcf-annotate-all}

*Defined in `subworkflows/local/vcf_annotate_all/main.nf:37`*

Annotate variants using multiple annotation tools.
This subworkflow provides flexible variant annotation using one or more tools:
- **SnpEff**: Functional annotation and effect prediction
- **VEP (Ensembl Variant Effect Predictor)**: Comprehensive variant annotation
- **BCFtools annotate**: Add custom annotations from external files
- **Merge**: Combined SnpEff + VEP annotation
The tools to use are specified via the `tools` parameter as a
comma-separated list (e.g., "snpeff,vep" or "merge").

### Inputs

| Name | Description |
|------|-------------|
| `vcf` | - |
| `fasta` | - |
| `tools` | - |
| `snpeff_db` | - |
| `snpeff_cache` | - |
| `vep_genome` | - |
| `vep_species` | - |
| `vep_cache_version` | - |
| `vep_cache` | - |
| `vep_extra_files` | - |
| `bcftools_annotations` | - |
| `bcftools_annotations_index` | - |
| `bcftools_columns` | - |
| `bcftools_header_lines` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


---

*This pipeline was built with [Nextflow](https://nextflow.io).
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:02:57 UTC.*
