# Processes

This page documents all processes in the pipeline.

## Contents

- [MULTIQC](#multiqc)
- [UNTAR](#untar)
- [MOSDEPTH](#mosdepth)
- [SEQ2HLA](#seq2hla)
- [FASTQC](#fastqc)
- [GFFREAD](#gffread)
- [GUNZIP](#gunzip)
- [GATK4_COMBINEGVCFS](#gatk4-combinegvcfs)
- [GATK4_INDEXFEATUREFILE](#gatk4-indexfeaturefile)
- [GATK4_VARIANTFILTRATION](#gatk4-variantfiltration)
- [GATK4_CREATESEQUENCEDICTIONARY](#gatk4-createsequencedictionary)
- [GATK4_SPLITNCIGARREADS](#gatk4-splitncigarreads)
- [GATK4_HAPLOTYPECALLER](#gatk4-haplotypecaller)
- [GATK4_INTERVALLISTTOOLS](#gatk4-intervallisttools)
- [GATK4_BASERECALIBRATOR](#gatk4-baserecalibrator)
- [GATK4_APPLYBQSR](#gatk4-applybqsr)
- [GATK4_BEDTOINTERVALLIST](#gatk4-bedtointervallist)
- [GATK4_MERGEVCFS](#gatk4-mergevcfs)
- [UMITOOLS_EXTRACT](#umitools-extract)
- [SAMTOOLS_SORT](#samtools-sort)
- [SAMTOOLS_MERGE](#samtools-merge)
- [SAMTOOLS_IDXSTATS](#samtools-idxstats)
- [SAMTOOLS_FAIDX](#samtools-faidx)
- [SAMTOOLS_INDEX](#samtools-index)
- [SAMTOOLS_FLAGSTAT](#samtools-flagstat)
- [SAMTOOLS_STATS](#samtools-stats)
- [SAMTOOLS_CONVERT](#samtools-convert)
- [BEDTOOLS_SORT](#bedtools-sort)
- [BEDTOOLS_MERGE](#bedtools-merge)
- [STAR_GENOMEGENERATE](#star-genomegenerate)
- [STAR_ALIGN](#star-align)
- [STAR_INDEXVERSION](#star-indexversion)
- [SNPEFF_SNPEFF](#snpeff-snpeff)
- [SNPEFF_DOWNLOAD](#snpeff-download)
- [ENSEMBLVEP_VEP](#ensemblvep-vep)
- [ENSEMBLVEP_DOWNLOAD](#ensemblvep-download)
- [BCFTOOLS_ANNOTATE](#bcftools-annotate)
- [PICARD_MARKDUPLICATES](#picard-markduplicates)
- [TABIX_TABIX](#tabix-tabix)
- [TABIX_BGZIPTABIX](#tabix-bgziptabix)
- [CAT_FASTQ](#cat-fastq)
- [REMOVE_UNKNOWN_REGIONS](#remove-unknown-regions)
- [GTF2BED](#gtf2bed)

## MULTIQC {#multiqc}

*Defined in `modules/nf-core/multiqc/main.nf:21`*

Aggregate results from multiple analysis tools into a single report.
MultiQC searches a given directory for analysis logs and compiles them
into a single HTML report. It supports output from many common
bioinformatics tools including FastQC, STAR, Picard, GATK, and more.
The report provides:
- Summary statistics across all samples
- Interactive plots for QC metrics
- Data tables for detailed metrics
- Export functionality for plots and data

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `*.html` | `path` | `report` | - |
| `*_data` | `path` | `data` | - |
| `*_plots` | `path` | `plots` | - |


## UNTAR {#untar}

*Defined in `modules/nf-core/untar/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(archive)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## MOSDEPTH {#mosdepth}

*Defined in `modules/nf-core/mosdepth/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai), path(bed)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.global.dist.txt')` | `tuple` | `global_txt` | - |
| `val(meta), path('*.summary.txt')` | `tuple` | `summary_txt` | - |
| `val(meta), path('*.region.dist.txt')` | `tuple` | `regions_txt` | - |
| `val(meta), path('*.per-base.d4')` | `tuple` | `per_base_d4` | - |
| `val(meta), path('*.per-base.bed.gz')` | `tuple` | `per_base_bed` | - |
| `val(meta), path('*.per-base.bed.gz.csi')` | `tuple` | `per_base_csi` | - |
| `val(meta), path('*.regions.bed.gz')` | `tuple` | `regions_bed` | - |
| `val(meta), path('*.regions.bed.gz.csi')` | `tuple` | `regions_csi` | - |
| `val(meta), path('*.quantized.bed.gz')` | `tuple` | `quantized_bed` | - |
| `val(meta), path('*.quantized.bed.gz.csi')` | `tuple` | `quantized_csi` | - |
| `val(meta), path('*.thresholds.bed.gz')` | `tuple` | `thresholds_bed` | - |
| `val(meta), path('*.thresholds.bed.gz.csi')` | `tuple` | `thresholds_csi` | - |


## SEQ2HLA {#seq2hla}

*Defined in `modules/nf-core/seq2hla/main.nf:20`*

Perform HLA typing from RNA-seq data using seq2HLA.
seq2HLA determines HLA class I and class II genotypes from RNA-seq reads
by mapping to a reference database of HLA alleles. It provides:
- 2-digit resolution typing (e.g., HLA-A*02)
- 4-digit resolution typing (e.g., HLA-A*02:01)
- Expression levels of HLA alleles
- Ambiguity reports when alleles cannot be distinguished
Supports both classical HLA genes (HLA-A, -B, -C, -DRB1, -DQB1, -DQA1)
and non-classical genes.
Requires paired-end RNA-seq reads as input.

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*ClassI-class.bowtielog")` | `tuple` | `class1_bowtielog` | - |
| `val(meta), path("*ClassI-class.expression")` | `tuple` | `class1_expression` | - |
| `val(meta), path("*ClassI-class.HLAgenotype2digits")` | `tuple` | `class1_genotype_2d` | - |
| `val(meta), path("*ClassI-class.HLAgenotype4digits")` | `tuple` | `class1_genotype_4d` | - |
| `val(meta), path("*ClassI-nonclass.bowtielog")` | `tuple` | `class1_nonclass_bowtielog` | - |
| `val(meta), path("*ClassI-nonclass.expression")` | `tuple` | `class1_nonclass_expression` | - |
| `val(meta), path("*ClassI-nonclass.HLAgenotype2digits")` | `tuple` | `class1_nonclass_genotype_2d` | - |
| `val(meta), path("*ClassI-nonclass.HLAgenotype4digits")` | `tuple` | `class1_nonclass_genotype_4d` | - |
| `val(meta), path("*ClassII.bowtielog")` | `tuple` | `class2_bowtielog` | - |
| `val(meta), path("*ClassII.expression")` | `tuple` | `class2_expression` | - |
| `val(meta), path("*ClassII.HLAgenotype2digits")` | `tuple` | `class2_genotype_2d` | - |
| `val(meta), path("*ClassII.HLAgenotype4digits")` | `tuple` | `class2_genotype_4d` | - |
| `val(meta), path("*.ambiguity")` | `tuple` | `ambiguity` | - |
| `versions.yml` | `path` | `versions` | - |


## FASTQC {#fastqc}

*Defined in `modules/nf-core/fastqc/main.nf:19`*

Run FastQC quality control on sequencing reads.
FastQC provides a comprehensive quality control report for high-throughput
sequencing data. It generates an HTML report and a ZIP archive containing
detailed metrics including:
- Basic statistics (total sequences, sequence length, GC content)
- Per-base sequence quality scores
- Per-sequence quality scores
- Per-base sequence content
- Sequence duplication levels
- Overrepresented sequences
- Adapter content

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.html")` | `tuple` | `html` | - |
| `val(meta), path("*.zip")` | `tuple` | `zip` | - |


## GFFREAD {#gffread}

*Defined in `modules/nf-core/gffread/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(gff)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.gtf")` | `tuple` | `gtf` | - |
| `val(meta), path("*.gff3")` | `tuple` | `gffread_gff` | - |
| `val(meta), path("*.fasta")` | `tuple` | `gffread_fasta` | - |
| `versions.yml` | `path` | `versions` | - |


## GUNZIP {#gunzip}

*Defined in `modules/nf-core/gunzip/main.nf:16`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(archive)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## GATK4_COMBINEGVCFS {#gatk4-combinegvcfs}

*Defined in `modules/nf-core/gatk4/combinegvcfs/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(vcf_idx)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.combined.g.vcf.gz")` | `tuple` | `combined_gvcf` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_INDEXFEATUREFILE {#gatk4-indexfeaturefile}

*Defined in `modules/nf-core/gatk4/indexfeaturefile/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(feature_file)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## GATK4_VARIANTFILTRATION {#gatk4-variantfiltration}

*Defined in `modules/nf-core/gatk4/variantfiltration/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dict)` | `tuple` | - |
| `val(meta5), path(gzi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_CREATESEQUENCEDICTIONARY {#gatk4-createsequencedictionary}

*Defined in `modules/nf-core/gatk4/createsequencedictionary/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.dict')` | `tuple` | `dict` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_SPLITNCIGARREADS {#gatk4-splitncigarreads}

*Defined in `modules/nf-core/gatk4/splitncigarreads/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dict)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.bam')` | `tuple` | `bam` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_HAPLOTYPECALLER {#gatk4-haplotypecaller}

*Defined in `modules/nf-core/gatk4/haplotypecaller/main.nf:25`*

Call germline SNPs and indels using GATK HaplotypeCaller.
HaplotypeCaller is GATK's flagship variant caller, performing local
de-novo assembly of haplotypes in regions showing variation. It can
produce either standard VCF output or GVCF output for joint calling.
Key features:
- Local re-assembly for accurate indel calling
- Population-aware calling using dbSNP
- Support for GVCF output mode for cohort analysis
- DRAGstr model support for improved STR calling
For RNA-seq data, this should be run after SplitNCigarReads processing.

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(intervals), path(dragstr_model)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dict)` | `tuple` | - |
| `val(meta5), path(dbsnp)` | `tuple` | - |
| `val(meta6), path(dbsnp_tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*.realigned.bam")` | `tuple` | `bam` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_INTERVALLISTTOOLS {#gatk4-intervallisttools}

*Defined in `modules/nf-core/gatk4/intervallisttools/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(intervals)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*_split/*/*.interval_list")` | `tuple` | `interval_list` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_BASERECALIBRATOR {#gatk4-baserecalibrator}

*Defined in `modules/nf-core/gatk4/baserecalibrator/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dict)` | `tuple` | - |
| `val(meta5), path(known_sites)` | `tuple` | - |
| `val(meta6), path(known_sites_tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.table")` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_APPLYBQSR {#gatk4-applybqsr}

*Defined in `modules/nf-core/gatk4/applybqsr/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(bqsr_table), path(intervals)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## GATK4_BEDTOINTERVALLIST {#gatk4-bedtointervallist}

*Defined in `modules/nf-core/gatk4/bedtointervallist/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bed)` | `tuple` | - |
| `val(meta2), path(dict)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.interval_list')` | `tuple` | `interval_list` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_MERGEVCFS {#gatk4-mergevcfs}

*Defined in `modules/nf-core/gatk4/mergevcfs/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf)` | `tuple` | - |
| `val(meta2), path(dict)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.vcf.gz')` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## UMITOOLS_EXTRACT {#umitools-extract}

*Defined in `modules/nf-core/umitools/extract/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.fastq.gz")` | `tuple` | `reads` | - |
| `val(meta), path("*.log")` | `tuple` | `log` | - |
| `versions.yml` | `path` | `versions` | - |


## SAMTOOLS_SORT {#samtools-sort}

*Defined in `modules/nf-core/samtools/sort/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## SAMTOOLS_MERGE {#samtools-merge}

*Defined in `modules/nf-core/samtools/merge/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input_files, stageAs: "?/*")` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(gzi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## SAMTOOLS_IDXSTATS {#samtools-idxstats}

*Defined in `modules/nf-core/samtools/idxstats/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.idxstats")` | `tuple` | `idxstats` | - |
| `versions.yml` | `path` | `versions` | - |


## SAMTOOLS_FAIDX {#samtools-faidx}

*Defined in `modules/nf-core/samtools/faidx/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(fasta)` | `tuple` | - |
| `val(meta2), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## SAMTOOLS_INDEX {#samtools-index}

*Defined in `modules/nf-core/samtools/index/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.csi")` | `tuple` | `csi` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `versions.yml` | `path` | `versions` | - |


## SAMTOOLS_FLAGSTAT {#samtools-flagstat}

*Defined in `modules/nf-core/samtools/flagstat/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.flagstat")` | `tuple` | `flagstat` | - |
| `versions.yml` | `path` | `versions` | - |


## SAMTOOLS_STATS {#samtools-stats}

*Defined in `modules/nf-core/samtools/stats/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.stats")` | `tuple` | `stats` | - |


## SAMTOOLS_CONVERT {#samtools-convert}

*Defined in `modules/nf-core/samtools/convert/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(index)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `versions.yml` | `path` | `versions` | - |


## BEDTOOLS_SORT {#bedtools-sort}

*Defined in `modules/nf-core/bedtools/sort/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(intervals)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## BEDTOOLS_MERGE {#bedtools-merge}

*Defined in `modules/nf-core/bedtools/merge/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bed)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.bed')` | `tuple` | `bed` | - |
| `versions.yml` | `path` | `versions` | - |


## STAR_GENOMEGENERATE {#star-genomegenerate}

*Defined in `modules/nf-core/star/genomegenerate/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(fasta)` | `tuple` | - |
| `val(meta2), path(gtf)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("star")` | `tuple` | `index` | - |
| `versions.yml` | `path` | `versions` | - |


## STAR_ALIGN {#star-align}

*Defined in `modules/nf-core/star/align/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads, stageAs: "input*/*")` | `tuple` | - |
| `val(meta2), path(index)` | `tuple` | - |
| `val(meta3), path(gtf)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*Log.final.out')` | `tuple` | `log_final` | - |
| `val(meta), path('*Log.out')` | `tuple` | `log_out` | - |
| `val(meta), path('*Log.progress.out')` | `tuple` | `log_progress` | - |
| `versions.yml` | `path` | `versions` | - |
| `val(meta), path('*d.out.bam')` | `tuple` | `bam` | - |
| `val(meta)` | `tuple` | - | - |


## STAR_INDEXVERSION {#star-indexversion}

*Defined in `modules/nf-core/star/indexversion/main.nf:1`*

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `*.txt` | `path` | `index_version` | - |
| `versions.yml` | `path` | `versions` | - |


## SNPEFF_SNPEFF {#snpeff-snpeff}

*Defined in `modules/nf-core/snpeff/snpeff/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf)` | `tuple` | - |
| `val(meta2), path(cache)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.ann.vcf")` | `tuple` | `vcf` | - |
| `val(meta)` | `tuple` | - | - |


## SNPEFF_DOWNLOAD {#snpeff-download}

*Defined in `modules/nf-core/snpeff/download/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), val(snpeff_db)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('snpeff_cache')` | `tuple` | `cache` | - |


## ENSEMBLVEP_VEP {#ensemblvep-vep}

*Defined in `modules/nf-core/ensemblvep/vep/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(custom_extra_files)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*.tab.gz")` | `tuple` | `tab` | - |
| `val(meta), path("*.json.gz")` | `tuple` | `json` | - |
| `val(meta)` | `tuple` | - | - |


## ENSEMBLVEP_DOWNLOAD {#ensemblvep-download}

*Defined in `modules/nf-core/ensemblvep/download/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), val(assembly), val(species), val(cache_version)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path(prefix)` | `tuple` | `cache` | - |


## BCFTOOLS_ANNOTATE {#bcftools-annotate}

*Defined in `modules/nf-core/bcftools/annotate/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(index), path(annotations), path(annotations_index)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## PICARD_MARKDUPLICATES {#picard-markduplicates}

*Defined in `modules/nf-core/picard/markduplicates/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.metrics.txt")` | `tuple` | `metrics` | - |
| `versions.yml` | `path` | `versions` | - |


## TABIX_TABIX {#tabix-tabix}

*Defined in `modules/nf-core/tabix/tabix/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(tab)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## TABIX_BGZIPTABIX {#tabix-bgziptabix}

*Defined in `modules/nf-core/tabix/bgziptabix/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.gz")` | `tuple` | - | - |


## CAT_FASTQ {#cat-fastq}

*Defined in `modules/nf-core/cat/fastq/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads, stageAs: "input*/*")` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.merged.fastq.gz")` | `tuple` | `reads` | - |


## REMOVE_UNKNOWN_REGIONS {#remove-unknown-regions}

*Defined in `modules/local/remove_unknown_regions/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bed)` | `tuple` | - |
| `val(meta2), path(dict)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.bed')` | `tuple` | `bed` | - |


## GTF2BED {#gtf2bed}

*Defined in `modules/local/gtf2bed/main.nf:13`*

Convert GTF annotation file to BED format.
Extracts genomic features (exons, transcripts, or genes) from a GTF file
and outputs them in BED format for use with interval-based tools.
The output BED file uses 0-based coordinates (BED standard) converted
from the 1-based GTF coordinates.

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(gtf)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.bed')` | `tuple` | `bed` | - |


---

*This pipeline was built with [Nextflow](https://nextflow.io).
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:02:57 UTC.*
