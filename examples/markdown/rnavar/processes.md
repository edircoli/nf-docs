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

**Keywords:** `QC`, `bioinformatics tools`, `Beautiful stand-alone HTML report`

Aggregate results from bioinformatics analyses across many samples into a single report

### Code Documentation

Aggregate results from multiple analysis tools into a single report.
MultiQC searches a given directory for analysis logs and compiles them
into a single HTML report. It supports output from many common
bioinformatics tools including FastQC, STAR, Picard, GATK, and more.
The report provides:
- Summary statistics across all samples
- Interactive plots for QC metrics
- Data tables for detailed metrics
- Export functionality for plots and data

### Tools

#### [multiqc](https://multiqc.info/)

MultiQC searches a given directory for analysis logs and compiles a HTML report.
It's a general use tool, perfect for summarising the output from numerous bioinformatics tools.

[Homepage](https://multiqc.info/) | [Documentation](https://multiqc.info/docs/) | [biotools:multiqc](https://bio.tools/multiqc) | License: GPL-3.0-or-later

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `report` | `-` | `-` | - |
| `data` | `-` | `-` | - |
| `plots` | `-` | `-` | - |

**Authors:** [@abhi18av](https://github.com/abhi18av), [@bunop](https://github.com/bunop), [@drpatelh](https://github.com/drpatelh), [@jfy133](https://github.com/jfy133)
**Maintainers:** [@abhi18av](https://github.com/abhi18av), [@bunop](https://github.com/bunop), [@drpatelh](https://github.com/drpatelh), [@jfy133](https://github.com/jfy133)


## UNTAR {#untar}

*Defined in `modules/nf-core/untar/main.nf:1`*

**Keywords:** `untar`, `uncompress`, `extract`

Extract files from tar, tar.gz, tar.bz2, tar.xz archives

### Tools

#### [untar](https://www.gnu.org/software/tar/manual/)

Extract tar, tar.gz, tar.bz2, tar.xz files.

[Documentation](https://www.gnu.org/software/tar/manual/) | License: GPL-3.0-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `archive` | `file` | File to be untarred |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `untar` | `map` | `*/` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@matthdsm](https://github.com/matthdsm), [@jfy133](https://github.com/jfy133)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@matthdsm](https://github.com/matthdsm), [@jfy133](https://github.com/jfy133)


## MOSDEPTH {#mosdepth}

*Defined in `modules/nf-core/mosdepth/main.nf:1`*

**Keywords:** `mosdepth`, `bam`, `cram`, `coverage`

Calculates genome-wide sequencing coverage.

### Tools

#### [mosdepth](https://github.com/brentp/mosdepth)

Fast BAM/CRAM depth calculation for WGS, exome, or targeted sequencing.

[Documentation](https://github.com/brentp/mosdepth) | [biotools:mosdepth](https://bio.tools/mosdepth) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | Input BAM/CRAM file |
| `bai` | `file` | Index for BAM/CRAM file |
| `bed` | `file` | BED file with intersected intervals |
| `meta2` | `map` | Groovy Map containing bed information e.g. [ id:'test' ] |
| `fasta` | `file` | Reference genome FASTA file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `global_txt` | `file` | `*.{global.dist.txt}` | Text file with global cumulative coverage distribution |
| `summary_txt` | `file` | `*.{summary.txt}` | Text file with summary mean depths per chromosome and regions |
| `regions_txt` | `file` | `*.{region.dist.txt}` | Text file with region cumulative coverage distribution |
| `per_base_d4` | `file` | `*.{per-base.d4}` | D4 file with per-base coverage |
| `per_base_bed` | `file` | `*.{per-base.bed.gz}` | BED file with per-base coverage |
| `per_base_csi` | `file` | `*.{per-base.bed.gz.csi}` | Index file for BED file with per-base coverage |
| `regions_bed` | `file` | `*.{regions.bed.gz}` | BED file with per-region coverage |
| `regions_csi` | `file` | `*.{regions.bed.gz.csi}` | Index file for BED file with per-region coverage |
| `quantized_bed` | `file` | `*.{quantized.bed.gz}` | BED file with binned coverage |
| `quantized_csi` | `file` | `*.{quantized.bed.gz.csi}` | Index file for BED file with binned coverage |
| `thresholds_bed` | `file` | `*.{thresholds.bed.gz}` | BED file with the number of bases in each region that are covered at or above each threshold |
| `thresholds_csi` | `file` | `*.{thresholds.bed.gz.csi}` | Index file for BED file with threshold coverage |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@ramprasadn](https://github.com/ramprasadn), [@matthdsm](https://github.com/matthdsm)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@ramprasadn](https://github.com/ramprasadn), [@matthdsm](https://github.com/matthdsm)


## SEQ2HLA {#seq2hla}

*Defined in `modules/nf-core/seq2hla/main.nf:20`*

**Keywords:** `hla`, `typing`, `rna-seq`, `genomics`, `immunogenetics`

Precision HLA typing and expression from RNA-seq data using seq2HLA

### Code Documentation

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

### Tools

#### [seq2hla](https://github.com/TRON-Bioinformatics/seq2HLA)

Precision HLA typing and expression from next-generation RNA sequencing data

[Homepage](https://github.com/TRON-Bioinformatics/seq2HLA) | [Documentation](https://github.com/TRON-Bioinformatics/seq2HLA#readme) | [biotools:seq2HLA](https://bio.tools/seq2HLA) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. `[ id:'sample1', single_end:false ]` |
| `reads` | `file` | Paired-end FASTQ files for RNA-seq data |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `class1_genotype_2d` | `file` | `*ClassI-class.HLAgenotype2digits` | HLA Class I 2-digit genotype results |
| `class2_genotype_2d` | `file` | `*ClassII.HLAgenotype2digits` | HLA Class II 2-digit genotype results |
| `class1_genotype_4d` | `file` | `*ClassI-class.HLAgenotype4digits` | HLA Class I 4-digit genotype results |
| `class2_genotype_4d` | `file` | `*ClassII.HLAgenotype4digits` | HLA Class II 4-digit genotype results |
| `class1_bowtielog` | `file` | `*ClassI-class.bowtielog` | HLA Class I Bowtie alignment log |
| `class2_bowtielog` | `file` | `*ClassII.bowtielog` | HLA Class II Bowtie alignment log |
| `class1_expression` | `file` | `*ClassI-class.expression` | HLA Class I expression results |
| `class2_expression` | `file` | `*ClassII.expression` | HLA Class II expression results |
| `class1_nonclass_genotype_2d` | `file` | `*ClassI-nonclass.HLAgenotype2digits` | HLA Class I non-classical 2-digit genotype results |
| `ambiguity` | `file` | `*.ambiguity` | HLA typing ambiguity results |
| `class1_nonclass_genotype_4d` | `file` | `*ClassI-nonclass.HLAgenotype4digits` | HLA Class I non-classical 4-digit genotype results |
| `class1_nonclass_bowtielog` | `file` | `*ClassI-nonclass.bowtielog` | HLA Class I non-classical Bowtie alignment log |
| `class1_nonclass_expression` | `file` | `*ClassI-nonclass.expression` | HLA Class I non-classical expression results |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## FASTQC {#fastqc}

*Defined in `modules/nf-core/fastqc/main.nf:19`*

**Keywords:** `quality control`, `qc`, `adapters`, `fastq`

Run FastQC on sequenced reads

### Code Documentation

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

### Tools

#### [fastqc](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)

FastQC gives general quality metrics about your reads.
It provides information about the quality score distribution
across your reads, the per base sequence content (%A/C/G/T).

You get information about adapter contamination and other
overrepresented sequences.

[Homepage](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) | [Documentation](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/Help/) | [biotools:fastqc](https://bio.tools/fastqc) | License: GPL-2.0-only

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | List of input FastQ files of size 1 and 2 for single-end and paired-end data, respectively. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `html` | `file` | `*_{fastqc.html}` | FastQC report |
| `zip` | `file` | `*_{fastqc.zip}` | FastQC report archive |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@grst](https://github.com/grst), [@ewels](https://github.com/ewels), [@FelixKrueger](https://github.com/FelixKrueger)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@grst](https://github.com/grst), [@ewels](https://github.com/ewels), [@FelixKrueger](https://github.com/FelixKrueger)


## GFFREAD {#gffread}

*Defined in `modules/nf-core/gffread/main.nf:1`*

**Keywords:** `gff`, `conversion`, `validation`

Validate, filter, convert and perform various other operations on GFF files

### Tools

#### [gffread](http://ccb.jhu.edu/software/stringtie/gff.shtml#gffread)

GFF/GTF utility providing format conversions, region filtering, FASTA sequence extraction and more.

[Homepage](http://ccb.jhu.edu/software/stringtie/gff.shtml#gffread) | [Documentation](http://ccb.jhu.edu/software/stringtie/gff.shtml#gffread) | [biotools:gffread](https://bio.tools/gffread) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing meta data e.g. [ id:'test' ] |
| `gff` | `file` | A reference file in either the GFF3, GFF2 or GTF format. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `gtf` | `file` | `*.{gtf}` | GTF file resulting from the conversion of the GFF input file if '-T' argument is present |
| `gffread_gff` | `file` | `*.gff3` | GFF3 file resulting from the conversion of the GFF input file if '-T' argument is absent |
| `gffread_fasta` | `file` | `*.fasta` | Fasta file produced when either of '-w', '-x', '-y' parameters is present |

**Authors:** [@edmundmiller](https://github.com/edmundmiller)
**Maintainers:** [@edmundmiller](https://github.com/edmundmiller), [@gallvp](https://github.com/gallvp)


## GUNZIP {#gunzip}

*Defined in `modules/nf-core/gunzip/main.nf:16`*

**Keywords:** `gunzip`, `compression`, `decompression`

Compresses and decompresses files.

### Tools

#### [gunzip](https://www.gnu.org/software/gzip/manual/gzip.html)

gzip is a file format and a software application used for file compression and decompression.

[Documentation](https://www.gnu.org/software/gzip/manual/gzip.html) | License: GPL-3.0-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Optional groovy Map containing meta information e.g. [ id:'test', single_end:false ] |
| `archive` | `file` | File to be compressed/uncompressed |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `gunzip` | `file` | `*.*` | Compressed/uncompressed file |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@jfy133](https://github.com/jfy133)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@jfy133](https://github.com/jfy133), [@gallvp](https://github.com/gallvp)


## GATK4_COMBINEGVCFS {#gatk4-combinegvcfs}

*Defined in `modules/nf-core/gatk4/combinegvcfs/main.nf:1`*

**Keywords:** `gvcf`, `gatk4`, `vcf`, `combinegvcfs`, `short variant discovery`

Combine per-sample gVCF files produced by HaplotypeCaller into a multi-sample gVCF file

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Genome Analysis Toolkit (GATK4). Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools with a primary focus on variant discovery and genotyping. Its powerful processing engine and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360037593911-CombineGVCFs) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `vcf` | `file` | Compressed VCF files |
| `vcf_idx` | `file` | VCF Index file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `combined_gvcf` | `file` | `*.combined.g.vcf.gz` | Compressed Combined GVCF file |

**Authors:** [@sateeshperi](https://github.com/sateeshperi), [@mjcipriano](https://github.com/mjcipriano), [@hseabolt](https://github.com/hseabolt), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@sateeshperi](https://github.com/sateeshperi), [@mjcipriano](https://github.com/mjcipriano), [@hseabolt](https://github.com/hseabolt), [@maxulysse](https://github.com/maxulysse)


## GATK4_INDEXFEATUREFILE {#gatk4-indexfeaturefile}

*Defined in `modules/nf-core/gatk4/indexfeaturefile/main.nf:1`*

**Keywords:** `feature`, `gatk4`, `index`, `indexfeaturefile`

Creates an index for a feature file, e.g. VCF or BED file.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Genome Analysis Toolkit (GATK4)

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: BSD-3-clause

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `feature_file` | `file` | VCF/BED file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `index` | `file` | `*.{tbi,idx}` | Index for VCF/BED file |

**Authors:** [@santiagorevale](https://github.com/santiagorevale)
**Maintainers:** [@santiagorevale](https://github.com/santiagorevale)


## GATK4_VARIANTFILTRATION {#gatk4-variantfiltration}

*Defined in `modules/nf-core/gatk4/variantfiltration/main.nf:1`*

**Keywords:** `filter`, `gatk4`, `variantfiltration`, `vcf`

Filter variants

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `vcf` | `list` | List of VCF(.gz) files |
| `tbi` | `list` | List of VCF file indexes |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Fasta file of reference genome |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Index of fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `dict` | `file` | Sequence dictionary of fastea file |
| `meta5` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `gzi` | `file` | Genome index file only needed when the genome file was compressed with the BGZF algorithm. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.vcf.gz` | Compressed VCF file |
| `tbi` | `file` | `*.vcf.gz.tbi` | Index of VCF file |

**Authors:** [@kevinmenden](https://github.com/kevinmenden), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@kevinmenden](https://github.com/kevinmenden), [@ramprasadn](https://github.com/ramprasadn)


## GATK4_CREATESEQUENCEDICTIONARY {#gatk4-createsequencedictionary}

*Defined in `modules/nf-core/gatk4/createsequencedictionary/main.nf:1`*

**Keywords:** `createsequencedictionary`, `dictionary`, `fasta`, `gatk4`

Creates a sequence dictionary for a reference sequence

### Tools

#### [gatk](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Input fasta file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `dict` | `file` | `*.{dict}` | gatk dictionary file |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@ramprasadn](https://github.com/ramprasadn)


## GATK4_SPLITNCIGARREADS {#gatk4-splitncigarreads}

*Defined in `modules/nf-core/gatk4/splitncigarreads/main.nf:1`*

**Keywords:** `gatk4`, `merge`, `vcf`

Splits reads that contain Ns in their cigar string

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `bam` | `list` | BAM/SAM/CRAM file containing reads |
| `bai` | `list` | BAI/SAI/CRAI index file (optional) |
| `intervals` | `file` | Bed file with the genomic regions included in the library (optional) |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'reference' ] |
| `fasta` | `file` | The reference fasta file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'reference' ] |
| `fai` | `file` | Index of reference fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'reference' ] |
| `dict` | `file` | GATK sequence dictionary |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam` | `file` | `*.{bam,sam,cram}` | Output file with split reads (BAM/SAM/CRAM) |

**Authors:** [@kevinmenden](https://github.com/kevinmenden)
**Maintainers:** [@kevinmenden](https://github.com/kevinmenden)


## GATK4_HAPLOTYPECALLER {#gatk4-haplotypecaller}

*Defined in `modules/nf-core/gatk4/haplotypecaller/main.nf:25`*

**Keywords:** `gatk4`, `haplotype`, `haplotypecaller`

Call germline SNPs and indels via local re-assembly of haplotypes

### Code Documentation

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

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM file from alignment |
| `input_index` | `file` | BAI/CRAI file from alignment |
| `intervals` | `file` | Bed file with the genomic regions included in the library (optional) |
| `dragstr_model` | `file` | Text file containing the DragSTR model of the used BAM/CRAM file (optional) |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test_reference' ] |
| `fasta` | `file` | The reference fasta file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'test_reference' ] |
| `fai` | `file` | Index of reference fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'test_reference' ] |
| `dict` | `file` | GATK sequence dictionary |
| `meta5` | `map` | Groovy Map containing dbsnp information e.g. [ id:'test_dbsnp' ] |
| `dbsnp` | `file` | VCF file containing known sites (optional) |
| `meta6` | `map` | Groovy Map containing dbsnp information e.g. [ id:'test_dbsnp' ] |
| `dbsnp_tbi` | `file` | VCF index of dbsnp (optional) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.vcf.gz` | Compressed VCF file |
| `tbi` | `file` | `*.vcf.gz.tbi` | Index of VCF file |
| `bam` | `file` | `*.realigned.bam` | Assembled haplotypes and locally realigned reads |

**Authors:** [@suzannejin](https://github.com/suzannejin), [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@suzannejin](https://github.com/suzannejin), [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## GATK4_INTERVALLISTTOOLS {#gatk4-intervallisttools}

*Defined in `modules/nf-core/gatk4/intervallisttools/main.nf:1`*

**Keywords:** `bed`, `gatk4`, `interval_list`, `sort`

Splits the interval list file into unique, equally-sized interval files and place it under a directory

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `intervals` | `file` | Interval file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `interval_list` | `file` | `*.interval_list` | Interval list files |

**Authors:** [@praveenraj2018](https://github.com/praveenraj2018)
**Maintainers:** [@praveenraj2018](https://github.com/praveenraj2018)


## GATK4_BASERECALIBRATOR {#gatk4-baserecalibrator}

*Defined in `modules/nf-core/gatk4/baserecalibrator/main.nf:1`*

**Keywords:** `base quality score recalibration`, `table`, `bqsr`, `gatk4`, `sort`

Generate recalibration table for Base Quality Score Recalibration (BQSR)

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM file from alignment |
| `input_index` | `file` | BAI/CRAI file from alignment |
| `intervals` | `file` | Bed file with the genomic regions included in the library (optional) |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome'] |
| `fasta` | `file` | The reference fasta file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome'] |
| `fai` | `file` | Index of reference fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'genome'] |
| `dict` | `file` | GATK sequence dictionary |
| `meta5` | `map` | Groovy Map containing reference information e.g. [ id:'genome'] |
| `known_sites` | `file` | VCF files with known sites for indels / snps |
| `meta6` | `map` | Groovy Map containing reference information e.g. [ id:'genome'] |
| `known_sites_tbi` | `file` | Tabix index of the known_sites |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `table` | `file` | `*.{table}` | Recalibration table from BaseRecalibrator |

**Authors:** [@yocra3](https://github.com/yocra3), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@yocra3](https://github.com/yocra3), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)


## GATK4_APPLYBQSR {#gatk4-applybqsr}

*Defined in `modules/nf-core/gatk4/applybqsr/main.nf:1`*

**Keywords:** `bam`, `base quality score recalibration`, `bqsr`, `cram`, `gatk4`

Apply base quality score recalibration (BQSR) to a bam file

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM file from alignment |
| `input_index` | `file` | BAI/CRAI file from alignment |
| `bqsr_table` | `file` | Recalibration table from gatk4_baserecalibrator |
| `intervals` | `file` | Bed file with the genomic regions included in the library (optional) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam` | `file` | `${prefix}.bam` | Recalibrated BAM file |
| `bai` | `file` | `${prefix}*bai` | Recalibrated BAM index file |
| `cram` | `file` | `${prefix}.cram` | Recalibrated CRAM file |

**Authors:** [@yocra3](https://github.com/yocra3), [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@yocra3](https://github.com/yocra3), [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## GATK4_BEDTOINTERVALLIST {#gatk4-bedtointervallist}

*Defined in `modules/nf-core/gatk4/bedtointervallist/main.nf:1`*

**Keywords:** `bed`, `bedtointervallist`, `gatk4`, `interval list`

Creates an interval list from a bed file and a reference dict

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `bed` | `file` | Input bed file |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `dict` | `file` | Sequence dictionary |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `interval_list` | `file` | `*.interval_list` | gatk interval list file |

**Authors:** [@kevinmenden](https://github.com/kevinmenden), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@kevinmenden](https://github.com/kevinmenden), [@ramprasadn](https://github.com/ramprasadn)


## GATK4_MERGEVCFS {#gatk4-mergevcfs}

*Defined in `modules/nf-core/gatk4/mergevcfs/main.nf:1`*

**Keywords:** `gatk4`, `merge`, `vcf`

Merges several vcf files

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `vcf` | `list` | Two or more VCF files |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome'] |
| `dict` | `file` | Optional Sequence Dictionary as input |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.vcf.gz` | merged vcf file |
| `tbi` | `file` | `*.tbi` | index files for the merged vcf files |

**Authors:** [@kevinmenden](https://github.com/kevinmenden)
**Maintainers:** [@kevinmenden](https://github.com/kevinmenden)


## UMITOOLS_EXTRACT {#umitools-extract}

*Defined in `modules/nf-core/umitools/extract/main.nf:1`*

**Keywords:** `UMI`, `barcode`, `extract`, `umitools`

Extracts UMI barcode from a read and add it to the read name, leaving any sample barcode in place

### Tools

#### [umi_tools](https://umi-tools.readthedocs.io/en/latest/)

UMI-tools contains tools for dealing with Unique Molecular Identifiers (UMIs)/Random Molecular Tags (RMTs) and single cell RNA-Seq cell barcodes

[Documentation](https://umi-tools.readthedocs.io/en/latest/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `list` | List of input FASTQ files whose UMIs will be extracted. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `reads` | `file` | `*.{fastq.gz}` | Extracted FASTQ files. | For single-end reads, pattern is \${prefix}.umi_extract.fastq.gz. | For paired-end reads, pattern is \${prefix}.umi_extract_{1,2}.fastq.gz. |
| `log` | `file` | `*.{log}` | Logfile for umi_tools |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@grst](https://github.com/grst)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@grst](https://github.com/grst)


## SAMTOOLS_SORT {#samtools-sort}

*Defined in `modules/nf-core/samtools/sort/main.nf:1`*

**Keywords:** `sort`, `bam`, `sam`, `cram`

Sort SAM/BAM/CRAM file

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | BAM/CRAM/SAM file(s) |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Reference genome FASTA file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam` | `file` | `*.{bam}` | Sorted BAM file |
| `cram` | `file` | `*.{cram}` | Sorted CRAM file |
| `sam` | `file` | `*.{sam}` | Sorted SAM file |
| `crai` | `file` | `*.crai` | CRAM index file (optional) |
| `csi` | `file` | `*.csi` | BAM index file (optional) |
| `bai` | `file` | `*.bai` | BAM index file (optional) |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels), [@matthdsm](https://github.com/matthdsm)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels), [@matthdsm](https://github.com/matthdsm)


## SAMTOOLS_MERGE {#samtools-merge}

*Defined in `modules/nf-core/samtools/merge/main.nf:1`*

**Keywords:** `merge`, `bam`, `sam`, `cram`

Merge BAM or CRAM file

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input_files` | `file` | BAM/CRAM file |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Reference file the CRAM was created with (optional) |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Index of the reference file the CRAM was created with (optional) |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `gzi` | `file` | Index of the compressed reference file the CRAM was created with (optional) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam` | `file` | `*.{bam}` | BAM file |
| `cram` | `file` | `*.{cram}` | CRAM file |
| `csi` | `file` | `*.csi` | BAM index file (optional) |
| `crai` | `file` | `*.crai` | CRAM index file (optional) |

**Authors:** [@yuukiiwa](https://github.com/yuukiiwa), [@maxulysse](https://github.com/maxulysse), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@yuukiiwa](https://github.com/yuukiiwa), [@maxulysse](https://github.com/maxulysse), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@ramprasadn](https://github.com/ramprasadn)


## SAMTOOLS_IDXSTATS {#samtools-idxstats}

*Defined in `modules/nf-core/samtools/idxstats/main.nf:1`*

**Keywords:** `stats`, `mapping`, `counts`, `chromosome`, `bam`, `sam`, `cram`

Reports alignment summary statistics for a BAM/CRAM/SAM file

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | BAM/CRAM/SAM file |
| `bai` | `file` | Index for BAM/CRAM/SAM file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `idxstats` | `file` | `*.{idxstats}` | File containing samtools idxstats output |

**Authors:** [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@drpatelh](https://github.com/drpatelh)


## SAMTOOLS_FAIDX {#samtools-faidx}

*Defined in `modules/nf-core/samtools/faidx/main.nf:1`*

**Keywords:** `index`, `fasta`, `faidx`, `chromosome`

Index FASTA file, and optionally generate a file of chromosome sizes

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `fasta` | `file` | FASTA file |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `fai` | `file` | FASTA index file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `fa` | `file` | `*.{fa}` | FASTA file |
| `sizes` | `file` | `*.{sizes}` | File containing chromosome lengths |
| `fai` | `file` | `*.{fai}` | FASTA index file |
| `gzi` | `file` | `*.gzi` | Optional gzip index file for compressed inputs |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels), [@phue](https://github.com/phue)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@phue](https://github.com/phue)


## SAMTOOLS_INDEX {#samtools-index}

*Defined in `modules/nf-core/samtools/index/main.nf:1`*

**Keywords:** `index`, `bam`, `sam`, `cram`

Index SAM/BAM/CRAM file

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | input file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bai` | `file` | `*.{bai,crai,sai}` | BAM/CRAM/SAM index file |
| `csi` | `file` | `*.{csi}` | CSI index file |
| `crai` | `file` | `*.{bai,crai,sai}` | BAM/CRAM/SAM index file |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels), [@maxulysse](https://github.com/maxulysse)


## SAMTOOLS_FLAGSTAT {#samtools-flagstat}

*Defined in `modules/nf-core/samtools/flagstat/main.nf:1`*

**Keywords:** `stats`, `mapping`, `counts`, `bam`, `sam`, `cram`

Counts the number of alignments in a BAM/CRAM/SAM file for each FLAG type

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | BAM/CRAM/SAM file |
| `bai` | `file` | Index for BAM/CRAM/SAM file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `flagstat` | `file` | `*.{flagstat}` | File containing samtools flagstat output |

**Authors:** [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@drpatelh](https://github.com/drpatelh)


## SAMTOOLS_STATS {#samtools-stats}

*Defined in `modules/nf-core/samtools/stats/main.nf:1`*

**Keywords:** `statistics`, `counts`, `bam`, `sam`, `cram`

Produces comprehensive statistics from SAM/BAM/CRAM file

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM file from alignment |
| `input_index` | `file` | BAI/CRAI file from alignment |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Reference file the CRAM was created with (optional) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `stats` | `file` | `*.{stats}` | File containing samtools stats output |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@ramprasadn](https://github.com/ramprasadn)


## SAMTOOLS_CONVERT {#samtools-convert}

*Defined in `modules/nf-core/samtools/convert/main.nf:1`*

**Keywords:** `view`, `index`, `bam`, `cram`

convert and then index CRAM -> BAM or BAM -> CRAM file

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM file |
| `index` | `file` | BAM/CRAM index file |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Reference file to create the CRAM file |
| `meta3` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fai` | `file` | Reference index file to create the CRAM file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam` | `file` | `*{.bam}` | filtered/converted BAM file |
| `cram` | `file` | `*{cram}` | filtered/converted CRAM file |
| `bai` | `file` | `*{.bai}` | filtered/converted BAM index |
| `crai` | `file` | `*{.crai}` | filtered/converted CRAM index |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm)


## BEDTOOLS_SORT {#bedtools-sort}

*Defined in `modules/nf-core/bedtools/sort/main.nf:1`*

**Keywords:** `bed`, `sort`, `bedtools`, `chromosome`

Sorts a feature file by chromosome and other criteria.

### Tools

#### [bedtools](https://bedtools.readthedocs.io/en/latest/content/tools/sort.html)

A set of tools for genomic analysis tasks, specifically enabling genome arithmetic (merge, count, complement) on various file types.

[Documentation](https://bedtools.readthedocs.io/en/latest/content/tools/sort.html) | [biotools:bedtools](https://bio.tools/bedtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `intervals` | `file` | BED/BEDGRAPH |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `sorted` | `file` | `*.${extension}` | Sorted output file |

**Authors:** [@edmundmiller](https://github.com/edmundmiller), [@sruthipsuresh](https://github.com/sruthipsuresh), [@drpatelh](https://github.com/drpatelh), [@chris-cheshire](https://github.com/chris-cheshire), [@adamrtalbot](https://github.com/adamrtalbot)
**Maintainers:** [@edmundmiller](https://github.com/edmundmiller), [@sruthipsuresh](https://github.com/sruthipsuresh), [@drpatelh](https://github.com/drpatelh), [@chris-cheshire](https://github.com/chris-cheshire), [@adamrtalbot](https://github.com/adamrtalbot)


## BEDTOOLS_MERGE {#bedtools-merge}

*Defined in `modules/nf-core/bedtools/merge/main.nf:1`*

**Keywords:** `bed`, `merge`, `bedtools`, `overlapped bed`

combines overlapping or “book-ended” features in an interval file into a single feature which spans all of the combined features.

### Tools

#### [bedtools](https://bedtools.readthedocs.io/en/latest/content/tools/merge.html)

A set of tools for genomic analysis tasks, specifically enabling genome arithmetic (merge, count, complement) on various file types.

[Documentation](https://bedtools.readthedocs.io/en/latest/content/tools/merge.html) | [biotools:bedtools](https://bio.tools/bedtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bed` | `file` | Input BED file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bed` | `file` | `*.{bed}` | Overlapped bed file with combined features |

**Authors:** [@edmundmiller](https://github.com/edmundmiller), [@sruthipsuresh](https://github.com/sruthipsuresh), [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@edmundmiller](https://github.com/edmundmiller), [@sruthipsuresh](https://github.com/sruthipsuresh), [@drpatelh](https://github.com/drpatelh)


## STAR_GENOMEGENERATE {#star-genomegenerate}

*Defined in `modules/nf-core/star/genomegenerate/main.nf:1`*

**Keywords:** `index`, `fasta`, `genome`, `reference`

Create index for STAR

### Tools

#### [star](https://github.com/alexdobin/STAR)

STAR is a software package for mapping DNA sequences against
a large reference genome, such as the human genome.

[Homepage](https://github.com/alexdobin/STAR) | [biotools:star](https://bio.tools/star) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Fasta file of the reference genome |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `gtf` | `file` | GTF file of the reference genome |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `index` | `directory` | `star` | Folder containing the star index files |

**Authors:** [@kevinmenden](https://github.com/kevinmenden), [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@kevinmenden](https://github.com/kevinmenden), [@drpatelh](https://github.com/drpatelh)


## STAR_ALIGN {#star-align}

*Defined in `modules/nf-core/star/align/main.nf:1`*

**Keywords:** `align`, `fasta`, `genome`, `reference`

Align reads to a reference genome using STAR

### Tools

#### [star](https://github.com/alexdobin/STAR)

STAR is a software package for mapping DNA sequences against
a large reference genome, such as the human genome.

[Homepage](https://github.com/alexdobin/STAR) | [biotools:star](https://bio.tools/star) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | List of input FastQ files of size 1 and 2 for single-end and paired-end data, respectively. |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `index` | `directory` | STAR genome index |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `gtf` | `file` | Annotation GTF file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `log_final` | `file` | `*Log.final.out` | STAR final log file |
| `log_out` | `file` | `*Log.out` | STAR lot out file |
| `log_progress` | `file` | `*Log.progress.out` | STAR log progress file |
| `bam` | `file` | `*.{bam}` | Output BAM file containing read alignments |
| `bam_sorted` | `file` | `*sortedByCoord.out.bam` | Sorted BAM file of read alignments (optional) |
| `bam_sorted_aligned` | `file` | `*.Aligned.sortedByCoord.out.bam` | Sorted BAM file of read alignments (optional) |
| `bam_transcript` | `file` | `*toTranscriptome.out.bam` | Output BAM file of transcriptome alignment (optional) |
| `bam_unsorted` | `file` | `*Aligned.unsort.out.bam` | Unsorted BAM file of read alignments (optional) |
| `fastq` | `file` | `*fastq.gz` | Unmapped FastQ files (optional) |
| `tab` | `file` | `*.tab` | STAR output tab file(s) (optional) |
| `spl_junc_tab` | `file` | `*.SJ.out.tab` | STAR output splice junction tab file |
| `read_per_gene_tab` | `file` | `*.ReadsPerGene.out.tab` | STAR output read per gene tab file |
| `junction` | `file` | `*.out.junction` | STAR chimeric junction output file (optional) |
| `sam` | `file` | `*.out.sam` | STAR output SAM file(s) (optional) |
| `wig` | `file` | `*.wig` | STAR output wiggle format file(s) (optional) |
| `bedgraph` | `file` | `*.bg` | STAR output bedGraph format file(s) (optional) |

**Authors:** [@kevinmenden](https://github.com/kevinmenden), [@drpatelh](https://github.com/drpatelh), [@praveenraj2018](https://github.com/praveenraj2018)
**Maintainers:** [@kevinmenden](https://github.com/kevinmenden), [@drpatelh](https://github.com/drpatelh), [@praveenraj2018](https://github.com/praveenraj2018)


## STAR_INDEXVERSION {#star-indexversion}

*Defined in `modules/nf-core/star/indexversion/main.nf:1`*

**Keywords:** `index`, `version`, `rna`

Get the minimal allowed index version from STAR

### Tools

#### [star](https://github.com/alexdobin/STAR)

STAR is a software package for mapping DNA sequences against
a large reference genome, such as the human genome.

[Homepage](https://github.com/alexdobin/STAR) | [biotools:star](https://bio.tools/star) | License: MIT

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `index_version` | `-` | `-` | - |

**Authors:** [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@nvnieuwk](https://github.com/nvnieuwk)


## SNPEFF_SNPEFF {#snpeff-snpeff}

*Defined in `modules/nf-core/snpeff/snpeff/main.nf:1`*

**Keywords:** `annotation`, `effect prediction`, `snpeff`, `variant`, `vcf`

Genetic variant annotation and functional effect prediction toolbox

### Tools

#### [snpeff](https://pcingola.github.io/SnpEff/)

SnpEff is a variant annotation and effect prediction tool.
It annotates and predicts the effects of genetic variants on genes and proteins (such as amino acid changes).

[Homepage](https://pcingola.github.io/SnpEff/) | [Documentation](https://pcingola.github.io/SnpEff/se_introduction/) | [biotools:snpeff](https://bio.tools/snpeff) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcf` | `file` | vcf to annotate |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `cache` | `file` | path to snpEff cache (optional) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.ann.vcf` | annotated vcf |
| `report` | `string` | `*.csv` | The process The tool name snpEff report csv file |
| `summary_html` | `string` | `*.html` | The process The tool name snpEff summary statistics in html file |
| `genes_txt` | `string` | `*.genes.txt` | The process The tool name txt (tab separated) file having counts of the number of variants affecting each transcript and gene |

**Authors:** [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@maxulysse](https://github.com/maxulysse)


## SNPEFF_DOWNLOAD {#snpeff-download}

*Defined in `modules/nf-core/snpeff/download/main.nf:1`*

**Keywords:** `annotation`, `effect prediction`, `snpeff`, `variant`, `vcf`

Genetic variant annotation and functional effect prediction toolbox

### Tools

#### [snpeff](https://pcingola.github.io/SnpEff/)

SnpEff is a variant annotation and effect prediction tool.
It annotates and predicts the effects of genetic variants on genes and proteins (such as amino acid changes).

[Homepage](https://pcingola.github.io/SnpEff/) | [Documentation](https://pcingola.github.io/SnpEff/se_introduction/) | [biotools:snpeff](https://bio.tools/snpeff) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `snpeff_db` | `string` | SnpEff database name |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `cache` | `file` | `-` | snpEff cache |

**Authors:** [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@maxulysse](https://github.com/maxulysse)


## ENSEMBLVEP_VEP {#ensemblvep-vep}

*Defined in `modules/nf-core/ensemblvep/vep/main.nf:1`*

**Keywords:** `annotation`, `vcf`, `json`, `tab`

Ensembl Variant Effect Predictor (VEP). The output-file-format is controlled through `task.ext.args`.

### Tools

#### [ensemblvep](https://www.ensembl.org/info/docs/tools/vep/index.html)

VEP determines the effect of your variants (SNPs, insertions, deletions, CNVs
or structural variants) on genes, transcripts, and protein sequence, as well as regulatory regions.

[Homepage](https://www.ensembl.org/info/docs/tools/vep/index.html) | [Documentation](https://www.ensembl.org/info/docs/tools/vep/script/index.html) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcf` | `file` | vcf to annotate |
| `custom_extra_files` | `file` | extra sample-specific files to be used with the `--custom` flag to be configured with ext.args (optional) |
| `meta2` | `map` | Groovy Map containing fasta reference information e.g. [ id:'test' ] |
| `fasta` | `file` | reference FASTA file (optional) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.vcf.gz` | annotated vcf (optional) |
| `tbi` | `file` | `*.vcf.gz.tbi` | annotated vcf index (optional) |
| `tab` | `file` | `*.ann.tab.gz` | tab file with annotated variants (optional) |
| `json` | `file` | `*.ann.json.gz` | json file with annotated variants (optional) |
| `report` | `string` | `*.html` | The process The tool name VEP report file |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm), [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm), [@nvnieuwk](https://github.com/nvnieuwk)


## ENSEMBLVEP_DOWNLOAD {#ensemblvep-download}

*Defined in `modules/nf-core/ensemblvep/download/main.nf:1`*

**Keywords:** `annotation`, `cache`, `download`

Ensembl Variant Effect Predictor (VEP). The cache downloading options are controlled through `task.ext.args`.

### Tools

#### [ensemblvep](https://www.ensembl.org/info/docs/tools/vep/index.html)

VEP determines the effect of your variants (SNPs, insertions, deletions, CNVs
or structural variants) on genes, transcripts, and protein sequence, as well as regulatory regions.

[Homepage](https://www.ensembl.org/info/docs/tools/vep/index.html) | [Documentation](https://www.ensembl.org/info/docs/tools/vep/script/index.html) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `assembly` | `string` | Genome assembly |
| `species` | `string` | Specie |
| `cache_version` | `string` | cache version |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `cache` | `file` | `*` | cache |

**Authors:** [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@maxulysse](https://github.com/maxulysse)


## BCFTOOLS_ANNOTATE {#bcftools-annotate}

*Defined in `modules/nf-core/bcftools/annotate/main.nf:1`*

**Keywords:** `bcftools`, `annotate`, `vcf`, `remove`, `add`

Add or remove annotations.

### Tools

#### [annotate](http://samtools.github.io/bcftools/bcftools.html)

Add or remove annotations.

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](https://samtools.github.io/bcftools/bcftools.html#annotate) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | Query VCF or BCF file, can be either uncompressed or compressed |
| `index` | `file` | Index of the query VCF or BCF file |
| `annotations` | `file` | Bgzip-compressed file with annotations |
| `annotations_index` | `file` | Index of the annotations file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*{vcf,vcf.gz,bcf,bcf.gz}` | Compressed annotated VCF file |
| `tbi` | `file` | `*.tbi` | Alternative VCF file index |
| `csi` | `file` | `*.csi` | Default VCF file index |

**Authors:** [@projectoriented](https://github.com/projectoriented), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@projectoriented](https://github.com/projectoriented), [@ramprasadn](https://github.com/ramprasadn)


## PICARD_MARKDUPLICATES {#picard-markduplicates}

*Defined in `modules/nf-core/picard/markduplicates/main.nf:1`*

**Keywords:** `markduplicates`, `pcr`, `duplicates`, `bam`, `sam`, `cram`

Locate and tag duplicate reads in a BAM file

### Tools

#### [picard](https://broadinstitute.github.io/picard/)

A set of command line tools (in Java) for manipulating high-throughput sequencing (HTS)
data and formats such as SAM/BAM/CRAM and VCF.

[Homepage](https://broadinstitute.github.io/picard/) | [Documentation](https://broadinstitute.github.io/picard/) | [biotools:picard_tools](https://bio.tools/picard_tools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | Sequence reads file, can be SAM/BAM/CRAM format |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Reference genome fasta file, required for CRAM input |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Reference genome fasta index |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam` | `file` | `*.{bam}` | BAM file with duplicate reads marked/removed |
| `bai` | `file` | `*.{bai}` | An optional BAM index file. If desired, --CREATE_INDEX must be passed as a flag |
| `cram` | `file` | `*.{cram}` | Output CRAM file |
| `metrics` | `file` | `*.{metrics.txt}` | Duplicate metrics file generated by picard |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@projectoriented](https://github.com/projectoriented), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@projectoriented](https://github.com/projectoriented), [@ramprasadn](https://github.com/ramprasadn)


## TABIX_TABIX {#tabix-tabix}

*Defined in `modules/nf-core/tabix/tabix/main.nf:1`*

**Keywords:** `index`, `tabix`, `vcf`

create tabix index from a sorted bgzip tab-delimited genome file

### Tools

#### [tabix](https://www.htslib.org/doc/tabix.html)

Generic indexer for TAB-delimited genome position files.

[Homepage](https://www.htslib.org/doc/tabix.html) | [Documentation](https://www.htslib.org/doc/tabix.1.html) | [biotools:tabix](https://bio.tools/tabix) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `tab` | `file` | TAB-delimited genome position file compressed with bgzip |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `index` | `file` | `*.{tbi,csi}` | Tabix index file (either tbi or csi) |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@maxulysse](https://github.com/maxulysse)


## TABIX_BGZIPTABIX {#tabix-bgziptabix}

*Defined in `modules/nf-core/tabix/bgziptabix/main.nf:1`*

**Keywords:** `bgzip`, `compress`, `index`, `tabix`, `vcf`

bgzip a sorted tab-delimited genome file and then create tabix index

### Tools

#### [tabix](https://www.htslib.org/doc/tabix.html)

Generic indexer for TAB-delimited genome position files.

[Homepage](https://www.htslib.org/doc/tabix.html) | [Documentation](https://www.htslib.org/doc/tabix.1.html) | [biotools:tabix](https://bio.tools/tabix) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | Sorted tab-delimited genome file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `gz_index` | `file` | `*.gz, *.{tbi,csi}` | bgzipped tab-delimited genome file Tabix index file (either tbi or csi) |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@DLBPointon](https://github.com/DLBPointon)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@DLBPointon](https://github.com/DLBPointon)


## CAT_FASTQ {#cat-fastq}

*Defined in `modules/nf-core/cat/fastq/main.nf:1`*

**Keywords:** `cat`, `fastq`, `concatenate`

Concatenates fastq files

### Tools

#### [cat](https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html)

The cat utility reads files sequentially, writing them to the standard output.

[Documentation](https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html) | License: GPL-3.0-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | List of input FastQ files to be concatenated. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `reads` | `file` | `*.{merged.fastq.gz}` | Merged fastq file |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh)


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
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 14:11:19 UTC.*
