# Processes

This page documents all processes in the pipeline.

## Contents

- [MULTIQC](#multiqc)
- [UNTAR](#untar)
- [MOSDEPTH](#mosdepth)
- [VCFTOOLS](#vcftools)
- [UNZIP](#unzip)
- [YTE](#yte)
- [GAWK](#gawk)
- [FASTQC](#fastqc)
- [ASCAT](#ascat)
- [FREEBAYES](#freebayes)
- [FASTP](#fastp)
- [GUNZIP](#gunzip)
- [SPRING_DECOMPRESS](#spring-decompress)
- [LOFREQ_CALLPARALLEL](#lofreq-callparallel)
- [GATK4_INTERVALLISTTOBED](#gatk4-intervallisttobed)
- [GATK4_CALCULATECONTAMINATION](#gatk4-calculatecontamination)
- [GATK4_FILTERMUTECTCALLS](#gatk4-filtermutectcalls)
- [GATK4_APPLYVQSR](#gatk4-applyvqsr)
- [GATK4_GENOMICSDBIMPORT](#gatk4-genomicsdbimport)
- [GATK4_LEARNREADORIENTATIONMODEL](#gatk4-learnreadorientationmodel)
- [GATK4_VARIANTRECALIBRATOR](#gatk4-variantrecalibrator)
- [GATK4_GATHERBQSRREPORTS](#gatk4-gatherbqsrreports)
- [GATK4_GETPILEUPSUMMARIES](#gatk4-getpileupsummaries)
- [GATK4_GENOTYPEGVCFS](#gatk4-genotypegvcfs)
- [GATK4_CREATESEQUENCEDICTIONARY](#gatk4-createsequencedictionary)
- [GATK4_GATHERPILEUPSUMMARIES](#gatk4-gatherpileupsummaries)
- [GATK4_ESTIMATELIBRARYCOMPLEXITY](#gatk4-estimatelibrarycomplexity)
- [GATK4_HAPLOTYPECALLER](#gatk4-haplotypecaller)
- [GATK4_CNNSCOREVARIANTS](#gatk4-cnnscorevariants)
- [GATK4_BASERECALIBRATOR](#gatk4-baserecalibrator)
- [GATK4_APPLYBQSR](#gatk4-applybqsr)
- [GATK4_MERGEVCFS](#gatk4-mergevcfs)
- [GATK4_FILTERVARIANTTRANCHES](#gatk4-filtervarianttranches)
- [GATK4_MARKDUPLICATES](#gatk4-markduplicates)
- [GATK4_MUTECT2](#gatk4-mutect2)
- [GATK4_MERGEMUTECTSTATS](#gatk4-mergemutectstats)
- [GATK4SPARK_BASERECALIBRATOR](#gatk4spark-baserecalibrator)
- [GATK4SPARK_APPLYBQSR](#gatk4spark-applybqsr)
- [GATK4SPARK_MARKDUPLICATES](#gatk4spark-markduplicates)
- [DEEPVARIANT_RUNDEEPVARIANT](#deepvariant-rundeepvariant)
- [SENTIEON_GVCFTYPER](#sentieon-gvcftyper)
- [SENTIEON_TNSCOPE](#sentieon-tnscope)
- [SENTIEON_DNAMODELAPPLY](#sentieon-dnamodelapply)
- [SENTIEON_BWAMEM](#sentieon-bwamem)
- [SENTIEON_APPLYVARCAL](#sentieon-applyvarcal)
- [SENTIEON_VARCAL](#sentieon-varcal)
- [SENTIEON_DNASCOPE](#sentieon-dnascope)
- [SENTIEON_HAPLOTYPER](#sentieon-haplotyper)
- [SENTIEON_DEDUP](#sentieon-dedup)
- [SAMTOOLS_BAM2FQ](#samtools-bam2fq)
- [SAMTOOLS_MERGE](#samtools-merge)
- [SAMTOOLS_MPILEUP](#samtools-mpileup)
- [SAMTOOLS_FAIDX](#samtools-faidx)
- [SAMTOOLS_VIEW](#samtools-view)
- [SAMTOOLS_INDEX](#samtools-index)
- [SAMTOOLS_COLLATEFASTQ](#samtools-collatefastq)
- [SAMTOOLS_STATS](#samtools-stats)
- [SAMTOOLS_CONVERT](#samtools-convert)
- [VCFLIB_VCFFILTER](#vcflib-vcffilter)
- [BBMAP_BBSPLIT](#bbmap-bbsplit)
- [MSISENSOR2_MSI](#msisensor2-msi)
- [CONTROLFREEC_FREEC2BED](#controlfreec-freec2bed)
- [CONTROLFREEC_MAKEGRAPH2](#controlfreec-makegraph2)
- [CONTROLFREEC_FREEC2CIRCOS](#controlfreec-freec2circos)
- [CONTROLFREEC_FREEC](#controlfreec-freec)
- [CONTROLFREEC_ASSESSSIGNIFICANCE](#controlfreec-assesssignificance)
- [GOLEFT_INDEXCOV](#goleft-indexcov)
- [DRAGMAP_ALIGN](#dragmap-align)
- [DRAGMAP_HASHTABLE](#dragmap-hashtable)
- [STRELKA_GERMLINE](#strelka-germline)
- [STRELKA_SOMATIC](#strelka-somatic)
- [BWA_INDEX](#bwa-index)
- [BWA_MEM](#bwa-mem)
- [SNPEFF_SNPEFF](#snpeff-snpeff)
- [SNPEFF_DOWNLOAD](#snpeff-download)
- [NGSCHECKMATE_NCM](#ngscheckmate-ncm)
- [ENSEMBLVEP_VEP](#ensemblvep-vep)
- [ENSEMBLVEP_DOWNLOAD](#ensemblvep-download)
- [VARLOCIRAPTOR_CALLVARIANTS](#varlociraptor-callvariants)
- [VARLOCIRAPTOR_PREPROCESS](#varlociraptor-preprocess)
- [VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES](#varlociraptor-estimatealignmentproperties)
- [CNVKIT_GENEMETRICS](#cnvkit-genemetrics)
- [CNVKIT_CALL](#cnvkit-call)
- [CNVKIT_BATCH](#cnvkit-batch)
- [CNVKIT_ANTITARGET](#cnvkit-antitarget)
- [CNVKIT_EXPORT](#cnvkit-export)
- [CNVKIT_REFERENCE](#cnvkit-reference)
- [RBT_VCFSPLIT](#rbt-vcfsplit)
- [FGBIO_FASTQTOBAM](#fgbio-fastqtobam)
- [FGBIO_COPYUMIFROMREADNAME](#fgbio-copyumifromreadname)
- [FGBIO_CALLMOLECULARCONSENSUSREADS](#fgbio-callmolecularconsensusreads)
- [FGBIO_GROUPREADSBYUMI](#fgbio-groupreadsbyumi)
- [BWAMEM2_INDEX](#bwamem2-index)
- [BWAMEM2_MEM](#bwamem2-mem)
- [MANTA_TUMORONLY](#manta-tumoronly)
- [MANTA_GERMLINE](#manta-germline)
- [MANTA_SOMATIC](#manta-somatic)
- [BCFTOOLS_CONCAT](#bcftools-concat)
- [BCFTOOLS_SORT](#bcftools-sort)
- [BCFTOOLS_MERGE](#bcftools-merge)
- [BCFTOOLS_MPILEUP](#bcftools-mpileup)
- [BCFTOOLS_ANNOTATE](#bcftools-annotate)
- [BCFTOOLS_NORM](#bcftools-norm)
- [BCFTOOLS_VIEW](#bcftools-view)
- [BCFTOOLS_STATS](#bcftools-stats)
- [BCFTOOLS_ISEC](#bcftools-isec)
- [MSISENSORPRO_SCAN](#msisensorpro-scan)
- [MSISENSORPRO_MSISOMATIC](#msisensorpro-msisomatic)
- [MUSE_SUMP](#muse-sump)
- [MUSE_CALL](#muse-call)
- [PARABRICKS_FQ2BAM](#parabricks-fq2bam)
- [SVDB_MERGE](#svdb-merge)
- [TIDDIT_SV](#tiddit-sv)
- [TABIX_TABIX](#tabix-tabix)
- [TABIX_BGZIPTABIX](#tabix-bgziptabix)
- [CAT_CAT](#cat-cat)
- [CAT_FASTQ](#cat-fastq)
- [CREATE_INTERVALS_BED](#create-intervals-bed)
- [ADD_INFO_TO_VCF](#add-info-to-vcf)
- [SAMTOOLS_REINDEX_BAM](#samtools-reindex-bam)

## MULTIQC {#multiqc}

*Defined in `modules/nf-core/multiqc/main.nf:1`*

**Keywords:** `QC`, `bioinformatics tools`, `Beautiful stand-alone HTML report`

Aggregate results from bioinformatics analyses across many samples into a single report

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

Extract files.

### Tools

#### [untar](https://www.gnu.org/software/tar/manual/)

Extract tar.gz files.

[Documentation](https://www.gnu.org/software/tar/manual/) | License: GPL-3.0-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `archive` | `file` | File to be untar |

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
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@ramprasadn](https://github.com/ramprasadn), [@matthdsm](https://github.com/matthdsm)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@ramprasadn](https://github.com/ramprasadn), [@matthdsm](https://github.com/matthdsm)


## VCFTOOLS {#vcftools}

*Defined in `modules/nf-core/vcftools/main.nf:1`*

**Keywords:** `VCFtools`, `VCF`, `sort`

A set of tools written in Perl and C++ for working with VCF files

### Tools

#### [vcftools](http://vcftools.sourceforge.net/)

A set of tools written in Perl and C++ for working with VCF files. This package only contains the C++ libraries whereas the package perl-vcftools-vcf contains the perl libraries

[Homepage](http://vcftools.sourceforge.net/) | [Documentation](http://vcftools.sourceforge.net/man_latest.html) | [biotools:vcftools](https://bio.tools/vcftools) | License: LGPL

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `variant_file` | `file` | variant input file which can be vcf, vcf.gz, or bcf format. |
| `bed` | `file` | bed file which can be used with different arguments in vcftools (optional) |
| `diff_variant_file` | `file` | secondary variant file which can be used with the 'diff' suite of tools (optional) |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf")` | `tuple` | `vcf` | - |
| `val(meta), path("*.bcf")` | `tuple` | `bcf` | - |
| `val(meta), path("*.frq")` | `tuple` | `frq` | - |
| `val(meta), path("*.frq.count")` | `tuple` | `frq_count` | - |
| `val(meta), path("*.idepth")` | `tuple` | `idepth` | - |
| `val(meta), path("*.ldepth")` | `tuple` | `ldepth` | - |
| `val(meta), path("*.ldepth.mean")` | `tuple` | `ldepth_mean` | - |
| `val(meta), path("*.gdepth")` | `tuple` | `gdepth` | - |
| `val(meta), path("*.hap.ld")` | `tuple` | `hap_ld` | - |
| `val(meta), path("*.geno.ld")` | `tuple` | `geno_ld` | - |
| `val(meta), path("*.geno.chisq")` | `tuple` | `geno_chisq` | - |
| `val(meta), path("*.list.hap.ld")` | `tuple` | `list_hap_ld` | - |
| `val(meta), path("*.list.geno.ld")` | `tuple` | `list_geno_ld` | - |
| `val(meta), path("*.interchrom.hap.ld")` | `tuple` | `interchrom_hap_ld` | - |
| `val(meta), path("*.interchrom.geno.ld")` | `tuple` | `interchrom_geno_ld` | - |
| `val(meta), path("*.TsTv")` | `tuple` | `tstv` | - |
| `val(meta), path("*.TsTv.summary")` | `tuple` | `tstv_summary` | - |
| `val(meta), path("*.TsTv.count")` | `tuple` | `tstv_count` | - |
| `val(meta), path("*.TsTv.qual")` | `tuple` | `tstv_qual` | - |
| `val(meta), path("*.FILTER.summary")` | `tuple` | `filter_summary` | - |
| `val(meta), path("*.sites.pi")` | `tuple` | `sites_pi` | - |
| `val(meta), path("*.windowed.pi")` | `tuple` | `windowed_pi` | - |
| `val(meta), path("*.weir.fst")` | `tuple` | `weir_fst` | - |
| `val(meta), path("*.het")` | `tuple` | `heterozygosity` | - |
| `val(meta), path("*.hwe")` | `tuple` | `hwe` | - |
| `val(meta), path("*.Tajima.D")` | `tuple` | `tajima_d` | - |
| `val(meta), path("*.ifreqburden")` | `tuple` | `freq_burden` | - |
| `val(meta), path("*.LROH")` | `tuple` | `lroh` | - |
| `val(meta), path("*.relatedness")` | `tuple` | `relatedness` | - |
| `val(meta), path("*.relatedness2")` | `tuple` | `relatedness2` | - |
| `val(meta), path("*.lqual")` | `tuple` | `lqual` | - |
| `val(meta), path("*.imiss")` | `tuple` | `missing_individual` | - |
| `val(meta), path("*.lmiss")` | `tuple` | `missing_site` | - |
| `val(meta), path("*.snpden")` | `tuple` | `snp_density` | - |
| `val(meta), path("*.kept.sites")` | `tuple` | `kept_sites` | - |
| `val(meta), path("*.removed.sites")` | `tuple` | `removed_sites` | - |
| `val(meta), path("*.singletons")` | `tuple` | `singeltons` | - |
| `val(meta), path("*.indel.hist")` | `tuple` | `indel_hist` | - |
| `val(meta), path("*.hapcount")` | `tuple` | `hapcount` | - |
| `val(meta), path("*.mendel")` | `tuple` | `mendel` | - |
| `val(meta), path("*.FORMAT")` | `tuple` | `format` | - |
| `val(meta), path("*.INFO")` | `tuple` | `info` | - |
| `val(meta), path("*.012")` | `tuple` | `genotypes_matrix` | - |
| `val(meta), path("*.012.indv")` | `tuple` | `genotypes_matrix_individual` | - |
| `val(meta), path("*.012.pos")` | `tuple` | `genotypes_matrix_position` | - |
| `val(meta), path("*.impute.hap")` | `tuple` | `impute_hap` | - |
| `val(meta), path("*.impute.hap.legend")` | `tuple` | `impute_hap_legend` | - |
| `val(meta), path("*.impute.hap.indv")` | `tuple` | `impute_hap_indv` | - |
| `val(meta), path("*.ldhat.sites")` | `tuple` | `ldhat_sites` | - |
| `val(meta), path("*.ldhat.locs")` | `tuple` | `ldhat_locs` | - |
| `val(meta), path("*.BEAGLE.GL")` | `tuple` | `beagle_gl` | - |
| `val(meta), path("*.BEAGLE.PL")` | `tuple` | `beagle_pl` | - |
| `val(meta), path("*.ped")` | `tuple` | `ped` | - |
| `val(meta), path("*.map")` | `tuple` | `map_` | - |
| `val(meta), path("*.tped")` | `tuple` | `tped` | - |
| `val(meta), path("*.tfam")` | `tuple` | `tfam` | - |
| `val(meta), path("*.diff.sites_in_files")` | `tuple` | `diff_sites_in_files` | - |
| `val(meta), path("*.diff.indv_in_files")` | `tuple` | `diff_indv_in_files` | - |
| `val(meta), path("*.diff.sites")` | `tuple` | `diff_sites` | - |
| `val(meta), path("*.diff.indv")` | `tuple` | `diff_indv` | - |
| `val(meta), path("*.diff.discordance.matrix")` | `tuple` | `diff_discd_matrix` | - |
| `val(meta), path("*.diff.switch")` | `tuple` | `diff_switch_error` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@Mark-S-Hill](https://github.com/Mark-S-Hill)
**Maintainers:** [@Mark-S-Hill](https://github.com/Mark-S-Hill)


## UNZIP {#unzip}

*Defined in `modules/nf-core/unzip/main.nf:1`*

**Keywords:** `unzip`, `decompression`, `zip`, `archiving`

Unzip ZIP archive files

### Tools

#### [unzip](https://sourceforge.net/projects/p7zip/)

p7zip is a quick port of 7z.exe and 7za.exe (command line version of 7zip, see www.7-zip.org) for Unix.

[Homepage](https://sourceforge.net/projects/p7zip/) | [Documentation](https://sourceforge.net/projects/p7zip/) | License: LGPL-2.1-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `archive` | `file` | ZIP file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `unzipped_archive` | `directory` | `${archive.baseName}/` | Directory contents of the unzipped archive |

**Authors:** [@jfy133](https://github.com/jfy133)
**Maintainers:** [@jfy133](https://github.com/jfy133)


## YTE {#yte}

*Defined in `modules/nf-core/yte/main.nf:1`*

**Keywords:** `yaml`, `template`, `python`

A YAML template engine with Python expressions

### Tools

#### [yte](https://yte-template-engine.github.io/)

A YAML template engine with Python expressions

[Homepage](https://yte-template-engine.github.io/) | [Documentation](https://yte-template-engine.github.io/) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. `[ id:'template1' ]` |
| `template` | `file` | YTE template |
| `map_file` | `file` | YAML file containing a map to be used in the template |
| `map` | `map` | Groovy Map containing mapping information to be used in the template e.g. `[ key: value ]` with key being a wildcard in the template |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `rendered` | `file` | `*.yaml` | Rendered YAML file |

**Authors:** [@famosab](https://github.com/famosab)
**Maintainers:** [@famosab](https://github.com/famosab)


## GAWK {#gawk}

*Defined in `modules/nf-core/gawk/main.nf:1`*

**Keywords:** `gawk`, `awk`, `txt`, `text`, `file parsing`

If you are like many computer users, you would frequently like to make changes in various text files
wherever certain patterns appear, or extract data from parts of certain lines while discarding the rest.
The job is easy with awk, especially the GNU implementation gawk.

### Tools

#### [gawk](https://www.gnu.org/software/gawk/)

GNU awk

[Homepage](https://www.gnu.org/software/gawk/) | [Documentation](https://www.gnu.org/software/gawk/manual/) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | The input file - Specify the logic that needs to be executed on this file on the `ext.args2` or in the program file. If the files have a `.gz` extension, they will be unzipped using `zcat`. |
| `program_file` | `file` | Optional file containing logic for awk to execute. If you don't wish to use a file, you can use `ext.args2` to specify the logic. |
| `disable_redirect_output` | `boolean` | Disable the redirection of awk output to a given file. This is useful if you want to use awk's built-in redirect to write files instead of the shell's redirect. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@nvnieuwk](https://github.com/nvnieuwk)


## FASTQC {#fastqc}

*Defined in `modules/nf-core/fastqc/main.nf:1`*

**Keywords:** `quality control`, `qc`, `adapters`, `fastq`

Run FastQC on sequenced reads

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


## ASCAT {#ascat}

*Defined in `modules/nf-core/ascat/main.nf:1`*

**Keywords:** `bam`, `copy number`, `cram`

copy number profiles of tumour cells.

### Tools

#### [ascat](https://github.com/VanLoo-lab/ascat/tree/master/man)

ASCAT is a method to derive copy number profiles of tumour cells, accounting for normal cell admixture and tumour aneuploidy. ASCAT infers tumour purity (the fraction of tumour cells) and ploidy (the amount of DNA per tumour cell), expressed as multiples of haploid genomes from SNP array or massively parallel sequencing data, and calculates whole-genome allele-specific copy number profiles (the number of copies of both parental alleles for all SNP loci across the genome).

[Documentation](https://github.com/VanLoo-lab/ascat/tree/master/man) | [biotools:ascat](https://bio.tools/ascat) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input_normal` | `file` | BAM/CRAM file, must adhere to chr1, chr2, ...chrX notation For modifying chromosome notation in bam files please follow https://josephcckuo.wordpress.com/2016/11/17/modify-chromosome-notation-in-bam-file/. |
| `index_normal` | `file` | index for normal_bam/cram |
| `input_tumor` | `file` | BAM/CRAM file, must adhere to chr1, chr2, ...chrX notation |
| `index_tumor` | `file` | index for tumor_bam/cram |
| `allele_files` | `file` | allele files for ASCAT WGS. Can be downloaded here https://github.com/VanLoo-lab/ascat/tree/master/ReferenceFiles/WGS |
| `loci_files` | `file` | loci files for ASCAT WGS. Loci files without chromosome notation can be downloaded here https://github.com/VanLoo-lab/ascat/tree/master/ReferenceFiles/WGS Make sure the chromosome notation matches the bam/cram input files. To add the chromosome notation to loci files (hg19/hg38) if necessary, you can run this command `if [[ $(samtools view <your_bam_file.bam> | head -n1 | cut -f3)\" == *\"chr\"* ]]; then for i in {1..22} X; do sed -i 's/^/chr/' G1000_loci_hg19_chr_${i}.txt; done; fi` |
| `bed_file` | `file` | Bed file for ASCAT WES (optional, but recommended for WES) |
| `fasta` | `file` | Reference fasta file (optional) |
| `gc_file` | `file` | GC correction file (optional) - Used to do logR correction of the tumour sample(s) with genomic GC content |
| `rt_file` | `file` | replication timing correction file (optional, provide only in combination with gc_file) |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*alleleFrequencies_chr*.txt")` | `tuple` | `allelefreqs` | - |
| `val(meta), path("*BAF.txt")` | `tuple` | `bafs` | - |
| `val(meta), path("*cnvs.txt")` | `tuple` | `cnvs` | - |
| `val(meta), path("*LogR.txt")` | `tuple` | `logrs` | - |
| `val(meta), path("*metrics.txt")` | `tuple` | `metrics` | - |
| `val(meta), path("*png")` | `tuple` | `png` | - |
| `val(meta), path("*purityploidy.txt")` | `tuple` | `purityploidy` | - |
| `val(meta), path("*segments.txt")` | `tuple` | `segments` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@aasNGC](https://github.com/aasNGC), [@lassefolkersen](https://github.com/lassefolkersen), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse), [@SusiJo](https://github.com/SusiJo)
**Maintainers:** [@aasNGC](https://github.com/aasNGC), [@lassefolkersen](https://github.com/lassefolkersen), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse), [@SusiJo](https://github.com/SusiJo)


## FREEBAYES {#freebayes}

*Defined in `modules/nf-core/freebayes/main.nf:1`*

**Keywords:** `variant caller`, `SNP`, `genotyping`, `somatic variant calling`, `germline variant calling`, `bacterial variant calling`, `bayesian`

A haplotype-based variant detector

### Tools

#### [freebayes](https://github.com/freebayes/freebayes)

Bayesian haplotype-based polymorphism discovery and genotyping

[Homepage](https://github.com/freebayes/freebayes) | [Documentation](https://github.com/freebayes/freebayes) | [biotools:freebayes](https://bio.tools/freebayes) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input_1` | `file` | BAM/CRAM/SAM file |
| `input_1_index` | `file` | BAM/CRAM/SAM index file |
| `input_2` | `file` | BAM/CRAM/SAM file |
| `input_2_index` | `file` | BAM/CRAM/SAM index file |
| `target_bed` | `file` | Optional - Limit analysis to targets listed in this BED-format FILE. |
| `meta2` | `map` | Groovy Map containing reference information. e.g. [ id:'test_reference' ] |
| `fasta` | `file` | reference fasta file |
| `meta3` | `map` | Groovy Map containing reference information. e.g. [ id:'test_reference' ] |
| `fasta_fai` | `file` | reference fasta file index |
| `meta4` | `map` | Groovy Map containing meta information for the samples file. e.g. [ id:'test_samples' ] |
| `samples` | `file` | Optional - Limit analysis to samples listed (one per line) in the FILE. |
| `meta5` | `map` | Groovy Map containing meta information for the populations file. e.g. [ id:'test_populations' ] |
| `populations` | `file` | Optional - Each line of FILE should list a sample and a population which it is part of. |
| `meta6` | `map` | Groovy Map containing meta information for the cnv file. e.g. [ id:'test_cnv' ] |
| `cnv` | `file` | A copy number map BED file, which has either a sample-level ploidy: sample_name copy_number or a region-specific format: seq_name start end sample_name copy_number |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.vcf.gz` | Compressed VCF file |

**Authors:** [@maxibor](https://github.com/maxibor), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@maxibor](https://github.com/maxibor), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)


## FASTP {#fastp}

*Defined in `modules/nf-core/fastp/main.nf:1`*

**Keywords:** `trimming`, `quality control`, `fastq`

Perform adapter/quality trimming on sequencing reads

### Tools

#### [fastp](https://github.com/OpenGene/fastp)

A tool designed to provide fast all-in-one preprocessing for FastQ files. This tool is developed in C++ with multithreading supported to afford high performance.

[Documentation](https://github.com/OpenGene/fastp) | [biotools:fastp](https://bio.tools/fastp) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information. Use 'single_end: true' to specify single ended or interleaved FASTQs. Use 'single_end: false' for paired-end reads. e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | List of input FastQ files of size 1 and 2 for single-end and paired-end data, respectively. If you wish to run interleaved paired-end data,  supply as single-end data but with `--interleaved_in` in your `modules.conf`'s `ext.args` for the module. |
| `adapter_fasta` | `file` | File in FASTA format containing possible adapters to remove. |
| `discard_trimmed_pass` | `boolean` | Specify true to not write any reads that pass trimming thresholds. This can be used to use fastp for the output report only. |
| `save_trimmed_fail` | `boolean` | Specify true to save files that failed to pass trimming thresholds ending in `*.fail.fastq.gz` |
| `save_merged` | `boolean` | Specify true to save all merged reads to a file ending in `*.merged.fastq.gz` |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.fastp.fastq.gz')` | `tuple` | `reads` | - |
| `val(meta), path('*.json')` | `tuple` | `json` | - |
| `val(meta), path('*.html')` | `tuple` | `html` | - |
| `val(meta), path('*.log')` | `tuple` | `log` | - |
| `val(meta), path('*.fail.fastq.gz')` | `tuple` | `reads_fail` | - |
| `val(meta), path('*.merged.fastq.gz')` | `tuple` | `reads_merged` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@kevinmenden](https://github.com/kevinmenden)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@kevinmenden](https://github.com/kevinmenden)


## GUNZIP {#gunzip}

*Defined in `modules/nf-core/gunzip/main.nf:1`*

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

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@jfy133](https://github.com/jfy133)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@jfy133](https://github.com/jfy133), [@gallvp](https://github.com/gallvp)


## SPRING_DECOMPRESS {#spring-decompress}

*Defined in `modules/nf-core/spring/decompress/main.nf:1`*

**Keywords:** `FASTQ`, `decompression`, `lossless`

Fast, efficient, lossless decompression of FASTQ files.

### Tools

#### [spring](https://github.com/shubhamchandak94/Spring)

SPRING is a compression tool for Fastq files (containing up to 4.29 Billion reads)

[Homepage](https://github.com/shubhamchandak94/Spring) | [Documentation](https://github.com/shubhamchandak94/Spring/blob/master/README.md) | [biotools:spring](https://bio.tools/spring) | License: Free for non-commercial use

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `spring` | `file` | Spring file to decompress. |
| `write_one_fastq_gz` | `boolean` | Controls whether spring should write one fastq.gz file with reads from both directions or two fastq.gz files with reads from distinct directions |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.fastq.gz")` | `tuple` | `fastq` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@xec-cm](https://github.com/xec-cm)
**Maintainers:** [@xec-cm](https://github.com/xec-cm)


## LOFREQ_CALLPARALLEL {#lofreq-callparallel}

*Defined in `modules/nf-core/lofreq/callparallel/main.nf:1`*

**Keywords:** `variant calling`, `low frequency variant calling`, `call`, `variants`

It predicts variants using multiple processors

### Tools

#### [lofreq](https://csb5.github.io/lofreq/)

Lofreq is a fast and sensitive variant-caller for inferring SNVs and indels from next-generation sequencing data. It's call-parallel programme predicts variants using multiple processors

[Homepage](https://csb5.github.io/lofreq/) | [Documentation](https://csb5.github.io/lofreq/) | [biotools:lofreq](https://bio.tools/lofreq) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `bam` | `file` | Tumor sample sorted BAM file |
| `bai` | `file` | BAM index file |
| `intervals` | `file` | BED file containing target regions for variant calling |
| `meta2` | `map` | Groovy Map containing sample information about the reference fasta e.g. [ id:'reference' ] |
| `fasta` | `file` | Reference genome FASTA file |
| `meta3` | `map` | Groovy Map containing sample information about the reference fasta fai e.g. [ id:'reference' ] |
| `fai` | `file` | Reference genome FASTA index file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@kaurravneet4123](https://github.com/kaurravneet4123), [@bjohnnyd](https://github.com/bjohnnyd)
**Maintainers:** [@kaurravneet4123](https://github.com/kaurravneet4123), [@bjohnnyd](https://github.com/bjohnnyd), [@nevinwu](https://github.com/nevinwu), [@AitorPeseta](https://github.com/AitorPeseta)


## GATK4_INTERVALLISTTOBED {#gatk4-intervallisttobed}

*Defined in `modules/nf-core/gatk4/intervallisttobed/main.nf:1`*

**Keywords:** `bed`, `conversion`, `gatk4`, `interval`

Converts an Picard IntervalList file to a BED file.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Genome Analysis Toolkit (GATK4)

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: BSD-3-clause

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `intervals` | `file` | IntervalList file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## GATK4_CALCULATECONTAMINATION {#gatk4-calculatecontamination}

*Defined in `modules/nf-core/gatk4/calculatecontamination/main.nf:1`*

**Keywords:** `gatk4`, `calculatecontamination`, `cross-samplecontamination`, `getpileupsummaries`, `filtermutectcalls`

Calculates the fraction of reads from cross-sample contamination based on summary tables from getpileupsummaries. Output to be used with filtermutectcalls.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `pileup` | `file` | File containing the pileups summary table of a tumor sample to be used to calculate contamination. |
| `matched` | `file` | File containing the pileups summary table of a normal sample that matches with the tumor sample specified in pileup argument. This is an optional input. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.contamination.table')` | `tuple` | `contamination` | - |
| `val(meta), path('*.segmentation.table')` | `tuple` | `segmentation` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@GCJMackenzie](https://github.com/GCJMackenzie), [@maxulysse](https://github.com/maxulysse)


## GATK4_FILTERMUTECTCALLS {#gatk4-filtermutectcalls}

*Defined in `modules/nf-core/gatk4/filtermutectcalls/main.nf:1`*

**Keywords:** `filtermutectcalls`, `filter`, `gatk4`, `mutect2`, `vcf`

Filters the raw output of mutect2, can optionally use outputs of calculatecontamination and learnreadorientationmodel to improve filtering.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `vcf` | `file` | compressed vcf file of mutect2calls |
| `vcf_tbi` | `file` | Tabix index of vcf file |
| `stats` | `file` | Stats file that pairs with output vcf file |
| `orientationbias` | `file` | files containing artifact priors for input vcf. Optional input. |
| `segmentation` | `file` | tables containing segmentation information for input vcf. Optional input. |
| `table` | `file` | table(s) containing contamination data for input vcf. Optional input, takes priority over estimate. |
| `estimate` | `float` | estimation of contamination value as a double. Optional input, will only be used if table is not specified. |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | The reference fasta file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Index of reference fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `dict` | `file` | GATK sequence dictionary |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*.filteringStats.tsv")` | `tuple` | `stats` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie), [@maxulysse](https://github.com/maxulysse), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@GCJMackenzie](https://github.com/GCJMackenzie), [@maxulysse](https://github.com/maxulysse), [@ramprasadn](https://github.com/ramprasadn)


## GATK4_APPLYVQSR {#gatk4-applyvqsr}

*Defined in `modules/nf-core/gatk4/applyvqsr/main.nf:1`*

**Keywords:** `gatk4`, `variant quality score recalibration`, `vcf`, `vqsr`

Apply a score cutoff to filter variants based on a recalibration table.
AplyVQSR performs the second pass in a two-stage process called Variant Quality Score Recalibration (VQSR).
Specifically, it applies filtering to the input variants based on the recalibration table produced
in the first step by VariantRecalibrator and a target sensitivity value.

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
| `vcf` | `file` | VCF file to be recalibrated, this should be the same file as used for the first stage VariantRecalibrator. |
| `vcf_tbi` | `file` | tabix index for the input vcf file. |
| `recal` | `file` | Recalibration file produced when the input vcf was run through VariantRecalibrator in stage 1. |
| `recal_index` | `file` | Index file for the recalibration file. |
| `tranches` | `file` | Tranches file produced when the input vcf was run through VariantRecalibrator in stage 1. |
| `fasta` | `file` | The reference fasta file |
| `fai` | `file` | Index of reference fasta file |
| `dict` | `file` | GATK sequence dictionary |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie)
**Maintainers:** [@GCJMackenzie](https://github.com/GCJMackenzie)


## GATK4_GENOMICSDBIMPORT {#gatk4-genomicsdbimport}

*Defined in `modules/nf-core/gatk4/genomicsdbimport/main.nf:1`*

**Keywords:** `gatk4`, `genomicsdb`, `genomicsdbimport`, `jointgenotyping`, `panelofnormalscreation`

merge GVCFs from multiple samples. For use in joint genotyping or somatic panel of normal creation.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `vcf` | `list` | either a list of vcf files to be used to create or update a genomicsdb, or a file that contains a map to vcf files to be used. |
| `tbi` | `list` | list of tbi files that match with the input vcf files |
| `interval_file` | `file` | file containing the intervals to be used when creating the genomicsdb |
| `interval_value` | `string` | if an intervals file has not been specified, the value entered here will be used as an interval via the "-L" argument |
| `wspace` | `file` | path to an existing genomicsdb to be used in update db mode or get intervals mode. This WILL NOT specify name of a new genomicsdb in create db mode. |
| `run_intlist` | `boolean` | Specify whether to run get interval list mode, this option cannot be specified at the same time as run_updatewspace. |
| `run_updatewspace` | `boolean` | Specify whether to run update genomicsdb mode, this option takes priority over run_intlist. |
| `input_map` | `boolean` | Specify whether the vcf input is providing a list of vcf file(s) or a single file containing a map of paths to vcf files to be used to create or update a genomicsdb. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie)
**Maintainers:** [@GCJMackenzie](https://github.com/GCJMackenzie)


## GATK4_LEARNREADORIENTATIONMODEL {#gatk4-learnreadorientationmodel}

*Defined in `modules/nf-core/gatk4/learnreadorientationmodel/main.nf:1`*

**Keywords:** `gatk4`, `learnreadorientationmodel`, `mutect2`, `readorientationartifacts`

Uses f1r2 counts collected during mutect2 to Learn the prior probability of read orientation artifacts

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `f1r2` | `list` | list of f1r2 files to be used as input. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.tar.gz")` | `tuple` | `artifactprior` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie)
**Maintainers:** [@GCJMackenzie](https://github.com/GCJMackenzie)


## GATK4_VARIANTRECALIBRATOR {#gatk4-variantrecalibrator}

*Defined in `modules/nf-core/gatk4/variantrecalibrator/main.nf:1`*

**Keywords:** `gatk4`, `recalibration model`, `variantrecalibrator`

Build a recalibration model to score variant quality for filtering purposes.
It is highly recommended to follow GATK best practices when using this module,
the gaussian mixture model requires a large number of samples to be used for the
tool to produce optimal results. For example, 30 samples for exome data. For more details see
https://gatk.broadinstitute.org/hc/en-us/articles/4402736812443-Which-training-sets-arguments-should-I-use-for-running-VQSR-

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `vcf` | `file` | input vcf file containing the variants to be recalibrated |
| `tbi` | `file` | tbi file matching with -vcf |
| `resource_vcf` | `file` | all resource vcf files that are used with the corresponding '--resource' label |
| `resource_tbi` | `file` | all resource tbi files that are used with the corresponding '--resource' label |
| `labels` | `string` | necessary arguments for GATK VariantRecalibrator. Specified to directly match the resources provided. More information can be found at https://gatk.broadinstitute.org/hc/en-us/articles/5358906115227-VariantRecalibrator |
| `fasta` | `file` | The reference fasta file |
| `fai` | `file` | Index of reference fasta file |
| `dict` | `file` | GATK sequence dictionary |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.recal")` | `tuple` | `recal` | - |
| `val(meta), path("*.idx")` | `tuple` | `idx` | - |
| `val(meta), path("*.tranches")` | `tuple` | `tranches` | - |
| `val(meta), path("*plots.R")` | `tuple` | `plots` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie), [@nickhsmith](https://github.com/nickhsmith)
**Maintainers:** [@GCJMackenzie](https://github.com/GCJMackenzie), [@nickhsmith](https://github.com/nickhsmith)


## GATK4_GATHERBQSRREPORTS {#gatk4-gatherbqsrreports}

*Defined in `modules/nf-core/gatk4/gatherbqsrreports/main.nf:1`*

**Keywords:** `base quality score recalibration`, `bqsr`, `gatherbqsrreports`, `gatk4`

Gathers scattered BQSR recalibration reports into a single file

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Genome Analysis Toolkit (GATK4)

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us) | License: BSD-3-clause

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `table` | `file` | File(s) containing BQSR table(s) |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.table")` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## GATK4_GETPILEUPSUMMARIES {#gatk4-getpileupsummaries}

*Defined in `modules/nf-core/gatk4/getpileupsummaries/main.nf:1`*

**Keywords:** `gatk4`, `germlinevariantsites`, `getpileupsumaries`, `readcountssummary`

Summarizes counts of reads that support reference, alternate and other alleles for given sites. Results can be used with CalculateContamination. Requires a common germline variant sites file, such as from gnomAD.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `input` | `file` | BAM/CRAM file to be summarised. |
| `index` | `file` | Index file for the input BAM/CRAM file. |
| `intervals` | `file` | File containing specified sites to be used for the summary. If this option is not specified, variants file is used instead automatically. |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | The reference fasta file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Index of reference fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `dict` | `file` | GATK sequence dictionary |
| `variants` | `file` | Population vcf of germline sequencing, containing allele fractions. Is also used as sites file if no separate sites file is specified. |
| `variants_tbi` | `file` | Index file for the germline resource. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.pileups.table')` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie)
**Maintainers:** [@GCJMackenzie](https://github.com/GCJMackenzie)


## GATK4_GENOTYPEGVCFS {#gatk4-genotypegvcfs}

*Defined in `modules/nf-core/gatk4/genotypegvcfs/main.nf:1`*

**Keywords:** `gatk4`, `genotype`, `gvcf`, `joint genotyping`

Perform joint genotyping on one or more samples pre-called with HaplotypeCaller.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Genome Analysis Toolkit (GATK4)

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: BSD-3-clause

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | gVCF(.gz) file or a GenomicsDB |
| `gvcf_index` | `file` | index of gvcf file, or empty when providing GenomicsDB |
| `intervals` | `file` | Interval file with the genomic regions included in the library (optional) |
| `intervals_index` | `file` | Interval index file (optional) |
| `meta2` | `map` | Groovy Map containing fasta information e.g. [ id:'test' ] |
| `fasta` | `file` | Reference fasta file |
| `meta3` | `map` | Groovy Map containing fai information e.g. [ id:'test' ] |
| `fai` | `file` | Reference fasta index file |
| `meta4` | `map` | Groovy Map containing dict information e.g. [ id:'test' ] |
| `dict` | `file` | Reference fasta sequence dict file |
| `meta5` | `map` | Groovy Map containing dbsnp information e.g. [ id:'test' ] |
| `dbsnp` | `file` | dbSNP VCF file |
| `meta6` | `map` | Groovy Map containing dbsnp tbi information e.g. [ id:'test' ] |
| `dbsnp_tbi` | `file` | dbSNP VCF index file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@santiagorevale](https://github.com/santiagorevale), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@santiagorevale](https://github.com/santiagorevale), [@maxulysse](https://github.com/maxulysse)


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


## GATK4_GATHERPILEUPSUMMARIES {#gatk4-gatherpileupsummaries}

*Defined in `modules/nf-core/gatk4/gatherpileupsummaries/main.nf:1`*

**Keywords:** `gatk4`, `mpileup`, `sort`

write your description here

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Genome Analysis Toolkit (GATK4)

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us) | License: BSD-3-clause

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `pileup` | `file` | Pileup files from gatk4/getpileupsummaries |
| `dict` | `file` | dictionary |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.pileups.table")` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)


## GATK4_ESTIMATELIBRARYCOMPLEXITY {#gatk4-estimatelibrarycomplexity}

*Defined in `modules/nf-core/gatk4/estimatelibrarycomplexity/main.nf:1`*

**Keywords:** `duplication metrics`, `estimatelibrarycomplexity`, `gatk4`, `reporting`

Estimates the numbers of unique molecules in a sequencing library.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Genome Analysis Toolkit (GATK4)

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM/SAM file |
| `fasta` | `file` | The reference fasta file |
| `fai` | `file` | Index of reference fasta file |
| `dict` | `file` | GATK sequence dictionary |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.metrics')` | `tuple` | `metrics` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)


## GATK4_HAPLOTYPECALLER {#gatk4-haplotypecaller}

*Defined in `modules/nf-core/gatk4/haplotypecaller/main.nf:1`*

**Keywords:** `gatk4`, `haplotype`, `haplotypecaller`

Call germline SNPs and indels via local re-assembly of haplotypes

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

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*.realigned.bam")` | `tuple` | `bam` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@suzannejin](https://github.com/suzannejin), [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@suzannejin](https://github.com/suzannejin), [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## GATK4_CNNSCOREVARIANTS {#gatk4-cnnscorevariants}

*Defined in `modules/nf-core/gatk4/cnnscorevariants/main.nf:1`*

**Keywords:** `cnnscorevariants`, `gatk4`, `variants`

Apply a Convolutional Neural Net to filter annotated variants

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
| `vcf` | `file` | VCF file |
| `tbi` | `file` | VCF index file |
| `aligned_input` | `file` | BAM/CRAM file from alignment (optional) |
| `intervals` | `file` | Bed file with the genomic regions included in the library (optional) |
| `fasta` | `file` | The reference fasta file |
| `fai` | `file` | Index of reference fasta file |
| `dict` | `file` | GATK sequence dictionary |
| `architecture` | `file` | Neural Net architecture configuration json file (optional) |
| `weights` | `file` | Keras model HD5 file with neural net weights. (optional) |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*cnn.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*cnn.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


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
| `known_sites` | `file` | VCF files with known sites for indels / snps (optional) |
| `meta6` | `map` | Groovy Map containing reference information e.g. [ id:'genome'] |
| `known_sites_tbi` | `file` | Tabix index of the known_sites (optional) |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.table")` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |

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

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.vcf.gz')` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@kevinmenden](https://github.com/kevinmenden)
**Maintainers:** [@kevinmenden](https://github.com/kevinmenden)


## GATK4_FILTERVARIANTTRANCHES {#gatk4-filtervarianttranches}

*Defined in `modules/nf-core/gatk4/filtervarianttranches/main.nf:1`*

**Keywords:** `filtervarianttranches`, `gatk4`, `tranche filtering`

Apply tranche filtering

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools
with a primary focus on variant discovery and genotyping. Its powerful processing engine
and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360051308071-FilterVariantTranches) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcf` | `file` | a VCF file containing variants, must have info key:CNN_2D |
| `tbi` | `file` | tbi file matching with -vcf |
| `intervals` | `file` | Intervals |
| `resources` | `list` | resource A VCF containing known SNP and or INDEL sites. Can be supplied as many times as necessary |
| `resources_index` | `list` | Index of resource VCF containing known SNP and or INDEL sites. Can be supplied as many times as necessary |
| `fasta` | `file` | The reference fasta file |
| `fai` | `file` | Index of reference fasta file |
| `dict` | `file` | GATK sequence dictionary |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## GATK4_MARKDUPLICATES {#gatk4-markduplicates}

*Defined in `modules/nf-core/gatk4/markduplicates/main.nf:1`*

**Keywords:** `bam`, `gatk4`, `markduplicates`, `sort`

This tool locates and tags duplicate reads in a BAM or SAM file, where duplicate reads are defined as originating from a single fragment of DNA.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools with a primary focus on variant discovery and genotyping. Its powerful processing engine and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360037052812-MarkDuplicates-Picard-) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | Sorted BAM file |
| `fasta` | `file` | Fasta file |
| `fasta_fai` | `file` | Fasta index file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*cram")` | `tuple` | `cram` | - |
| `val(meta), path("*bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.metrics")` | `tuple` | `metrics` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@ajodeh-juma](https://github.com/ajodeh-juma), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@ajodeh-juma](https://github.com/ajodeh-juma), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)


## GATK4_MUTECT2 {#gatk4-mutect2}

*Defined in `modules/nf-core/gatk4/mutect2/main.nf:1`*

**Keywords:** `gatk4`, `haplotype`, `indels`, `mutect2`, `snvs`, `somatic`

Call somatic SNVs and indels via local assembly of haplotypes.

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
| `input` | `list` | list of BAM files, also able to take CRAM as an input |
| `input_index` | `list` | list of BAM file indexes, also able to take CRAM indexes as an input |
| `intervals` | `file` | Specify region the tools is run on. |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | The reference fasta file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Index of reference fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `dict` | `file` | GATK sequence dictionary |
| `germline_resource` | `file` | Population vcf of germline sequencing, containing allele fractions. |
| `germline_resource_tbi` | `file` | Index file for the germline resource. |
| `panel_of_normals` | `file` | vcf file to be used as a panel of normals. |
| `panel_of_normals_tbi` | `file` | Index for the panel of normals. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*.stats")` | `tuple` | `stats` | - |
| `val(meta), path("*.f1r2.tar.gz")` | `tuple` | `f1r2` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@GCJMackenzie](https://github.com/GCJMackenzie), [@ramprasadn](https://github.com/ramprasadn)


## GATK4_MERGEMUTECTSTATS {#gatk4-mergemutectstats}

*Defined in `modules/nf-core/gatk4/mergemutectstats/main.nf:1`*

**Keywords:** `gatk4`, `merge`, `mutect2`, `mutectstats`

Merges mutect2 stats generated on different intervals/regions

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Genome Analysis Toolkit (GATK4)

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/categories/360002369672s) | License: BSD-3-clause

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `stats` | `file` | Stats file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz.stats")` | `tuple` | `stats` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## GATK4SPARK_BASERECALIBRATOR {#gatk4spark-baserecalibrator}

*Defined in `modules/nf-core/gatk4spark/baserecalibrator/main.nf:1`*

**Keywords:** `base quality score recalibration`, `table`, `bqsr`, `gatk4spark`, `sort`

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
| `fasta` | `file` | The reference fasta file |
| `fai` | `file` | Index of reference fasta file |
| `dict` | `file` | GATK sequence dictionary |
| `known_sites` | `file` | VCF files with known sites for indels / snps (optional) |
| `known_sites_tbi` | `file` | Tabix index of the known_sites (optional) |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.table")` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@yocra3](https://github.com/yocra3), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@yocra3](https://github.com/yocra3), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)


## GATK4SPARK_APPLYBQSR {#gatk4spark-applybqsr}

*Defined in `modules/nf-core/gatk4spark/applybqsr/main.nf:1`*

**Keywords:** `bam`, `base quality score recalibration`, `bqsr`, `cram`, `gatk4spark`

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

**Authors:** [@yocra3](https://github.com/yocra3), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@yocra3](https://github.com/yocra3), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)


## GATK4SPARK_MARKDUPLICATES {#gatk4spark-markduplicates}

*Defined in `modules/nf-core/gatk4spark/markduplicates/main.nf:1`*

**Keywords:** `bam`, `gatk4spark`, `markduplicates`, `sort`

This tool locates and tags duplicate reads in a BAM or SAM file, where duplicate reads are defined as originating from a single fragment of DNA.

### Tools

#### [gatk4](https://gatk.broadinstitute.org/hc/en-us)

Developed in the Data Sciences Platform at the Broad Institute, the toolkit offers a wide variety of tools with a primary focus on variant discovery and genotyping. Its powerful processing engine and high-performance computing features make it capable of taking on projects of any size.

[Homepage](https://gatk.broadinstitute.org/hc/en-us) | [Documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360037052812-MarkDuplicates-Picard-) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | Sorted BAM file |
| `fasta` | `file` | The reference fasta file |
| `fasta_fai` | `file` | Index of reference fasta file |
| `dict` | `file` | GATK sequence dictionary |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@ajodeh-juma](https://github.com/ajodeh-juma), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse), [@SusiJo](https://github.com/SusiJo)
**Maintainers:** [@ajodeh-juma](https://github.com/ajodeh-juma), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse), [@SusiJo](https://github.com/SusiJo)


## DEEPVARIANT_RUNDEEPVARIANT {#deepvariant-rundeepvariant}

*Defined in `modules/nf-core/deepvariant/rundeepvariant/main.nf:1`*

**Keywords:** `variant calling`, `machine learning`, `neural network`

DeepVariant is an analysis pipeline that uses a deep neural network to call genetic variants from next-generation DNA sequencing data

### Tools

#### [deepvariant](https://github.com/google/deepvariant)

DeepVariant is an analysis pipeline that uses a deep neural network to call genetic variants from next-generation DNA sequencing data

[Homepage](https://github.com/google/deepvariant) | [Documentation](https://github.com/google/deepvariant) | [biotools:deepvariant](https://bio.tools/deepvariant) | License: BSD-3-clause

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM file |
| `index` | `file` | Index of BAM/CRAM file |
| `intervals` | `file` | file containing intervals |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | The reference fasta file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Index of reference fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `gzi` | `file` | GZI index of reference fasta file |
| `meta5` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `par_bed` | `file` | BED file containing PAR regions |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.vcf.gz` | Compressed VCF file |
| `vcf_index` | `file` | `*.vcf.gz.{tbi,csi}` | Tabix index file of compressed VCF |
| `gvcf` | `file` | `*.g.vcf.gz` | Compressed GVCF file |
| `gvcf_index` | `file` | `*.g.vcf.gz.{tbi,csi}` | Tabix index file of compressed GVCF |

**Authors:** [@abhi18av](https://github.com/abhi18av), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@abhi18av](https://github.com/abhi18av), [@ramprasadn](https://github.com/ramprasadn)


## SENTIEON_GVCFTYPER {#sentieon-gvcftyper}

*Defined in `modules/nf-core/sentieon/gvcftyper/main.nf:1`*

**Keywords:** `joint genotyping`, `genotype`, `gvcf`

Perform joint genotyping on one or more samples pre-called with Sentieon's Haplotyper.

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `gvcfs` | `file` | gVCF(.gz) file |
| `tbis` | `file` | index of gvcf file |
| `intervals` | `file` | Interval file with the genomic regions included in the library (optional) |
| `meta1` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Reference fasta file |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fai` | `file` | Reference fasta index file |
| `meta3` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `dbsnp` | `file` | dbSNP VCF file |
| `meta4` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `dbsnp_tbi` | `file` | dbSNP VCF index file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf_gz` | `file` | `*.vcf.gz` | VCF file |
| `vcf_gz_tbi` | `file` | `*.vcf.gz.tbi` | VCF index file |

**Authors:** [@asp8200](https://github.com/asp8200)
**Maintainers:** [@asp8200](https://github.com/asp8200)


## SENTIEON_TNSCOPE {#sentieon-tnscope}

*Defined in `modules/nf-core/sentieon/tnscope/main.nf:1`*

**Keywords:** `tnscope`, `sentieon`, `variant_calling`

TNscope algorithm performs somatic variant calling on the tumor-normal matched pair or the tumor only data, using a Haplotyper algorithm.

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information. e.g. [ id:'test' ] |
| `input` | `file` | One or more BAM or CRAM files. |
| `input_index` | `file` | Indices for the input files |
| `intervals` | `file` | bed or interval_list file containing interval in the reference that will be used in the analysis. Only recommended for large WGS data, else the overhead may not be worth the additional parallelisation. |
| `meta2` | `map` | Groovy Map containing reference information. e.g. [ id:'test' ] |
| `fasta` | `file` | Genome fasta file |
| `meta3` | `map` | Groovy Map containing reference information. e.g. [ id:'test' ] |
| `fai` | `file` | Index of the genome fasta file |
| `meta4` | `map` | Groovy Map containing reference information. e.g. [ id:'test' ] |
| `dbsnp` | `file` | Single Nucleotide Polymorphism database (dbSNP) file |
| `meta5` | `map` | Groovy Map containing reference information. e.g. [ id:'test' ] |
| `dbsnp_tbi` | `file` | Index of the Single Nucleotide Polymorphism database (dbSNP) file |
| `meta6` | `map` | Groovy Map containing reference information. e.g. [ id:'test' ] |
| `pon` | `file` | Single Nucleotide Polymorphism database (dbSNP) file |
| `meta7` | `map` | Groovy Map containing reference information. e.g. [ id:'test' ] |
| `pon_tbi` | `file` | Index of the Single Nucleotide Polymorphism database (dbSNP) file |
| `meta8` | `map` | Groovy Map containing reference information. e.g. [ id:'test' ] |
| `cosmic` | `file` | Catalogue of Somatic Mutations in Cancer (COSMIC) VCF file. |
| `meta9` | `map` | Groovy Map containing reference information. e.g. [ id:'test' ] |
| `cosmic_tbi` | `file` | Index of the Catalogue of Somatic Mutations in Cancer (COSMIC) VCF file. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.{vcf.gz}` | VCF file |
| `index` | `file` | `*.vcf.gz.tbi` | Index of the VCF file |

**Authors:** [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@ramprasadn](https://github.com/ramprasadn)


## SENTIEON_DNAMODELAPPLY {#sentieon-dnamodelapply}

*Defined in `modules/nf-core/sentieon/dnamodelapply/main.nf:1`*

**Keywords:** `dnamodelapply`, `vcf`, `filter`, `sentieon`

modifies the input VCF file by adding the MLrejected FILTER to the variants

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. `[ id:'test', single_end:false ]` |
| `vcf` | `file` | INPUT VCF file |
| `idx` | `file` | Index of the input VCF file |
| `meta2` | `map` | Groovy Map containing reference information e.g. `[ id:'test' ]` |
| `fasta` | `file` | Genome fasta file |
| `meta3` | `map` | Groovy Map containing reference information e.g. `[ id:'test' ]` |
| `fai` | `file` | Index of the genome fasta file |
| `meta4` | `map` | Groovy Map containing reference information e.g. `[ id:'test' ]` |
| `ml_model` | `file` | machine learning model file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.{vcf,vcf.gz}` | INPUT VCF file |
| `tbi` | `file` | `*.{tbi}` | Index of the input VCF file |

**Authors:** [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@ramprasadn](https://github.com/ramprasadn)


## SENTIEON_BWAMEM {#sentieon-bwamem}

*Defined in `modules/nf-core/sentieon/bwamem/main.nf:1`*

**Keywords:** `mem`, `bwa`, `alignment`, `map`, `fastq`, `bam`, `sentieon`

Performs fastq alignment to a fasta reference using Sentieon's BWA MEM

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | Genome fastq files (single-end or paired-end) |
| `meta2` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `index` | `file` | BWA genome index files |
| `meta3` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Genome fasta file |
| `meta4` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `fasta_fai` | `file` | The index of the FASTA reference. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam_and_bai` | `file` | `*.{bam,bai}, *.{bam,bai}` | BAM file with corresponding index. BAM file with corresponding index. |

**Authors:** [@asp8200](https://github.com/asp8200)
**Maintainers:** [@asp8200](https://github.com/asp8200), [@DonFreed](https://github.com/DonFreed)


## SENTIEON_APPLYVARCAL {#sentieon-applyvarcal}

*Defined in `modules/nf-core/sentieon/applyvarcal/main.nf:1`*

**Keywords:** `sentieon`, `applyvarcal`, `varcal`, `VQSR`

Apply a score cutoff to filter variants based on a recalibration table.
Sentieon's Aplyvarcal performs the second pass in a two-stage process called Variant Quality Score Recalibration (VQSR).
Specifically, it applies filtering to the input variants based on the recalibration table produced
in the previous step VarCal and a target sensitivity value.
https://support.sentieon.com/manual/usages/general/#applyvarcal-algorithm

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `vcf` | `file` | VCF file to be recalibrated, this should be the same file as used for the first stage VariantRecalibrator. |
| `vcf_tbi` | `file` | tabix index for the input vcf file. |
| `recal` | `file` | Recalibration file produced when the input vcf was run through VariantRecalibrator in stage 1. |
| `recal_index` | `file` | Index file for the recalibration file. |
| `tranches` | `file` | Tranches file produced when the input vcf was run through VariantRecalibrator in stage 1. |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `fasta` | `file` | The reference fasta file |
| `meta3` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `fai` | `file` | Index of reference fasta file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.vcf.gz` | compressed vcf file containing the recalibrated variants. |
| `tbi` | `file` | `*vcf.gz.tbi` | Index of recalibrated vcf file. |

**Authors:** [@assp8200](https://github.com/assp8200)
**Maintainers:** [@assp8200](https://github.com/assp8200)


## SENTIEON_VARCAL {#sentieon-varcal}

*Defined in `modules/nf-core/sentieon/varcal/main.nf:1`*

**Keywords:** `sentieon`, `varcal`, `variant recalibration`

Module for Sentieons VarCal. The VarCal algorithm calculates the Variant Quality Score Recalibration (VQSR).
VarCal builds a recalibration model for scoring variant quality.
https://support.sentieon.com/manual/usages/general/#varcal-algorithm

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `vcf` | `file` | input vcf file containing the variants to be recalibrated |
| `tbi` | `file` | tbi file matching with -vcf |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `recal` | `file` | `*.recal` | Output recal file used by ApplyVQSR |
| `idx` | `file` | `*.idx` | Index file for the recal output file |
| `tranches` | `file` | `*.tranches` | Output tranches file used by ApplyVQSR |
| `plots` | `file` | `*plots.R` | Optional output rscript file to aid in visualization of the input data and learned model. |

**Authors:** [@asp8200](https://github.com/asp8200)
**Maintainers:** [@asp8200](https://github.com/asp8200)


## SENTIEON_DNASCOPE {#sentieon-dnascope}

*Defined in `modules/nf-core/sentieon/dnascope/main.nf:1`*

**Keywords:** `dnascope`, `sentieon`, `variant_calling`

DNAscope algorithm performs an improved version of Haplotype variant calling.

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information. e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | BAM file. |
| `bai` | `file` | BAI file |
| `intervals` | `file` | bed or interval_list file containing interval in the reference that will be used in the analysis |
| `meta2` | `map` | Groovy Map containing meta information for fasta. |
| `fasta` | `file` | Genome fasta file |
| `meta3` | `map` | Groovy Map containing meta information for fasta index. |
| `fai` | `file` | Index of the genome fasta file |
| `meta4` | `map` | Groovy Map containing meta information for dbsnp. |
| `dbsnp` | `file` | Single Nucleotide Polymorphism database (dbSNP) file |
| `meta5` | `map` | Groovy Map containing meta information for dbsnp_tbi. |
| `dbsnp_tbi` | `file` | Index of the Single Nucleotide Polymorphism database (dbSNP) file |
| `meta6` | `map` | Groovy Map containing meta information for machine learning model for Dnascope. |
| `ml_model` | `file` | machine learning model file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.unfiltered.vcf.gz` | Compressed VCF file |
| `vcf_tbi` | `file` | `*.unfiltered.vcf.gz.tbi` | Index of VCF file |
| `gvcf` | `file` | `*.g.vcf.gz` | Compressed GVCF file |
| `gvcf_tbi` | `file` | `*.g.vcf.gz.tbi` | Index of GVCF file |

**Authors:** [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@ramprasadn](https://github.com/ramprasadn)


## SENTIEON_HAPLOTYPER {#sentieon-haplotyper}

*Defined in `modules/nf-core/sentieon/haplotyper/main.nf:1`*

**Keywords:** `sentieon`, `haplotypecaller`, `haplotype`

Runs Sentieon's haplotyper for germline variant calling.

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM file from alignment |
| `input_index` | `file` | BAI/CRAI file from alignment |
| `intervals` | `file` | Bed file with the genomic regions included in the library (optional) |
| `recal_table` | `file` | Recalibration table from sentieon/qualcal (optional) |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Genome fasta file |
| `meta3` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fai` | `file` | The index of the FASTA reference. |
| `meta4` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `dbsnp` | `file` | VCF file containing known sites (optional) |
| `meta5` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `dbsnp_tbi` | `file` | VCF index of dbsnp (optional) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.unfiltered.vcf.gz` | Compressed VCF file |
| `vcf_tbi` | `file` | `*.unfiltered.vcf.gz.tbi` | Index of VCF file |
| `gvcf` | `file` | `*.g.vcf.gz` | Compressed GVCF file |
| `gvcf_tbi` | `file` | `*.g.vcf.gz.tbi` | Index of GVCF file |

**Authors:** [@asp8200](https://github.com/asp8200)
**Maintainers:** [@asp8200](https://github.com/asp8200)


## SENTIEON_DEDUP {#sentieon-dedup}

*Defined in `modules/nf-core/sentieon/dedup/main.nf:1`*

**Keywords:** `mem`, `dedup`, `map`, `bam`, `cram`, `sentieon`

Runs the sentieon tool LocusCollector followed by Dedup. LocusCollector collects read information that is used by Dedup which in turn marks or removes duplicate reads.

### Tools

#### [sentieon](https://www.sentieon.com/)

Sentieon® provides complete solutions for secondary DNA/RNA analysis for a variety of sequencing platforms, including short and long reads.
Our software improves upon BWA, STAR, Minimap2, GATK, HaplotypeCaller, Mutect, and Mutect2 based pipelines and is deployable on any generic-CPU-based computing system.

[Homepage](https://www.sentieon.com/) | [Documentation](https://www.sentieon.com/)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | BAM file. |
| `bai` | `file` | BAI file |
| `meta2` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Genome fasta file |
| `meta3` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `fasta_fai` | `file` | The index of the FASTA reference. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `cram` | `file` | `*.cram` | CRAM file |
| `crai` | `file` | `*.crai` | CRAM index file |
| `bam` | `file` | `*.bam` | BAM file. |
| `bai` | `file` | `*.bai` | BAI file |
| `score` | `file` | `*.score` | The score file indicates which reads LocusCollector finds are likely duplicates. |
| `metrics` | `file` | `*.metrics` | Output file containing Dedup metrics incl. histogram data. |
| `metrics_multiqc_tsv` | `file` | `*.metrics.multiqc.tsv` | Output tsv-file containing Dedup metrics excl. histogram data. |

**Authors:** [@asp8200](https://github.com/asp8200)
**Maintainers:** [@asp8200](https://github.com/asp8200)


## SAMTOOLS_BAM2FQ {#samtools-bam2fq}

*Defined in `modules/nf-core/samtools/bam2fq/main.nf:1`*

**Keywords:** `bam2fq`, `samtools`, `fastq`

The module uses bam2fq method from samtools to
convert a SAM, BAM or CRAM file to FASTQ format

### Tools

#### [samtools](http://www.htslib.org/doc/1.1/samtools.html)

Tools for dealing with SAM, BAM and CRAM files

[Documentation](http://www.htslib.org/doc/1.1/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `inputbam` | `file` | BAM/CRAM/SAM file |
| `split` | `boolean` | TRUE/FALSE value to indicate if reads should be separated into /1, /2 and if present other, or singleton. Note: choosing TRUE will generate 4 different files. Choosing FALSE will produce a single file, which will be interleaved in case the input contains paired reads. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.fq.gz")` | `tuple` | `reads` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@lescai](https://github.com/lescai)
**Maintainers:** [@lescai](https://github.com/lescai)


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

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@yuukiiwa ](https://github.com/yuukiiwa ), [@maxulysse](https://github.com/maxulysse), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@yuukiiwa ](https://github.com/yuukiiwa ), [@maxulysse](https://github.com/maxulysse), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@ramprasadn](https://github.com/ramprasadn)


## SAMTOOLS_MPILEUP {#samtools-mpileup}

*Defined in `modules/nf-core/samtools/mpileup/main.nf:1`*

**Keywords:** `mpileup`, `bam`, `sam`, `cram`

BAM

### Tools

#### [samtools](http://www.htslib.org/)

SAMtools is a set of utilities for interacting with and post-processing
short DNA sequence read alignments in the SAM, BAM and CRAM formats, written by Heng Li.
These files are generated as output by short read aligners like BWA.

[Homepage](http://www.htslib.org/) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `input` | `file` | BAM/CRAM/SAM file |
| `intervals` | `file` | Interval FILE |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `fasta` | `file` | FASTA reference file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.mpileup.gz")` | `tuple` | `mpileup` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@joseespinosa](https://github.com/joseespinosa)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@joseespinosa](https://github.com/joseespinosa)


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


## SAMTOOLS_VIEW {#samtools-view}

*Defined in `modules/nf-core/samtools/view/main.nf:1`*

**Keywords:** `view`, `bam`, `sam`, `cram`

filter/convert SAM/BAM/CRAM file

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
| `input` | `file` | BAM/CRAM/SAM file |
| `index` | `file` | BAM.BAI/BAM.CSI/CRAM.CRAI file (optional) |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `fasta` | `file` | Reference file the CRAM was created with (optional) |
| `qname` | `file` | Optional file with read names to output only select alignments |
| `index_format` | `string` | Index format, used together with ext.args = '--write-index' |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@joseespinosa](https://github.com/joseespinosa), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@priyanka-surana](https://github.com/priyanka-surana)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@joseespinosa](https://github.com/joseespinosa), [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@priyanka-surana](https://github.com/priyanka-surana)


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

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.csi")` | `tuple` | `csi` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@ewels](https://github.com/ewels), [@maxulysse](https://github.com/maxulysse)


## SAMTOOLS_COLLATEFASTQ {#samtools-collatefastq}

*Defined in `modules/nf-core/samtools/collatefastq/main.nf:1`*

**Keywords:** `bam2fq`, `samtools`, `fastq`

The module uses collate and then fastq methods from samtools to
convert a SAM, BAM or CRAM file to FASTQ format

### Tools

#### [samtools](http://www.htslib.org/doc/1.1/samtools.html)

Tools for dealing with SAM, BAM and CRAM files

[Documentation](http://www.htslib.org/doc/1.1/samtools.html) | [biotools:samtools](https://bio.tools/samtools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM/SAM file |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `fasta` | `file` | Reference genome fasta file |
| `interleave` | `boolean` | If true, the output is a single interleaved paired-end FASTQ If false, the output split paired-end FASTQ |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@lescai](https://github.com/lescai), [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm)
**Maintainers:** [@lescai](https://github.com/lescai), [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm)


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

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.stats")` | `tuple` | `stats` | - |
| `versions.yml` | `path` | `versions` | - |

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

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm)


## VCFLIB_VCFFILTER {#vcflib-vcffilter}

*Defined in `modules/nf-core/vcflib/vcffilter/main.nf:1`*

**Keywords:** `filter`, `variant`, `vcf`, `quality`

Command line tools for parsing and manipulating VCF files.

### Tools

#### [vcflib](https://github.com/vcflib/vcflib)

Command line tools for parsing and manipulating VCF files.

[Homepage](https://github.com/vcflib/vcflib) | [Documentation](https://github.com/vcflib/vcflib) | [biotools:vcflib](https://bio.tools/vcflib) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test_sample_1' ] |
| `vcf` | `file` | VCF file |
| `tbi` | `file` | Index file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.{vcf.gz}` | Filtered VCF file |

**Authors:** [@zachary-foster](https://github.com/zachary-foster)
**Maintainers:** [@zachary-foster](https://github.com/zachary-foster)


## BBMAP_BBSPLIT {#bbmap-bbsplit}

*Defined in `modules/nf-core/bbmap/bbsplit/main.nf:1`*

**Keywords:** `align`, `map`, `fastq`, `genome`, `reference`

Split sequencing reads by mapping them to multiple references simultaneously

### Tools

#### [bbmap](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/)

BBMap is a short read aligner, as well as various other bioinformatic tools.

[Homepage](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/) | [Documentation](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/) | [biotools:bbmap](https://bio.tools/bbmap) | License: UC-LBL license (see package)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | List of input FastQ files of size 1 and 2 for single-end and paired-end data, respectively. |
| `other_ref_names` | `list` | List of other reference ids apart from the primary |
| `other_ref_paths` | `list` | Path to other references paths corresponding to "other_ref_names" |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `index` | `-` | `-` | - |
| `primary_fastq` | `file` | `*primary*fastq.gz` | Output reads that map to the primary reference |
| `all_fastq` | `file` | `*fastq.gz` | All reads mapping to any of the references |
| `stats` | `file` | `*.txt` | Tab-delimited text file containing mapping statistics |
| `log` | `file` | `*.log` | Log file |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@pinin4fjords](https://github.com/pinin4fjords)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@pinin4fjords](https://github.com/pinin4fjords)


## MSISENSOR2_MSI {#msisensor2-msi}

*Defined in `modules/nf-core/msisensor2/msi/main.nf:1`*

**Keywords:** `msi`, `microsatellite`, `microsatellite instability`, `tumor`, `cfDNA`

msisensor2 detection of MSI regions.

### Tools

#### [msisensor2](https://github.com/niu-lab/msisensor2)

MSIsensor2 is a novel algorithm based machine learning, featuring a large upgrade in the microsatellite instability (MSI) detection for tumor only sequencing data, including Cell-Free DNA (cfDNA), Formalin-Fixed Paraffin-Embedded(FFPE) and other sample types. The original MSIsensor is specially designed for tumor/normal paired sequencing data.

[Homepage](https://github.com/niu-lab/msisensor2) | [Documentation](https://github.com/niu-lab/msisensor2/blob/master/README.md)

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `tumor_bam` | `file` | BAM/CRAM/SAM file |
| `tumor_bam_index` | `file` | BAM/CRAM/SAM index file |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `models` | `file` | Folder of MSISensor2 models (available from Github or as a product of msisensor2/scan) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `msi` | `file` | `-` | MSI classifications as a text file |
| `distribution` | `file` | `-` | Read count distributions of MSI regions |
| `somatic` | `file` | `-` | Somatic MSI regions detected. |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot)


## CONTROLFREEC_FREEC2BED {#controlfreec-freec2bed}

*Defined in `modules/nf-core/controlfreec/freec2bed/main.nf:1`*

**Keywords:** `cna`, `cnv`, `somatic`, `single`, `tumor-only`

Plot Freec output

### Tools

#### [controlfreec](http://boevalab.inf.ethz.ch/FREEC)

Copy number and genotype annotation from whole genome and whole exome sequencing data.

[Homepage](http://boevalab.inf.ethz.ch/FREEC) | [Documentation](http://boevalab.inf.ethz.ch/FREEC/tutorial.html) | License: GPL >=2

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `ratio` | `file` | ratio file generated by FREEC |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bed` | `file` | `*.bed` | Bed file |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## CONTROLFREEC_MAKEGRAPH2 {#controlfreec-makegraph2}

*Defined in `modules/nf-core/controlfreec/makegraph2/main.nf:1`*

**Keywords:** `cna`, `cnv`, `somatic`, `single`, `tumor-only`

Plot Freec output

### Tools

#### [controlfreec](http://boevalab.inf.ethz.ch/FREEC)

Copy number and genotype annotation from whole genome and whole exome sequencing data.

[Homepage](http://boevalab.inf.ethz.ch/FREEC) | [Documentation](http://boevalab.inf.ethz.ch/FREEC/tutorial.html) | License: GPL >=2

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `ratio` | `file` | ratio file generated by FREEC |
| `baf` | `file` | .BAF file generated by FREEC |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `png_baf` | `file` | `*_BAF.png` | Image of BAF plot |
| `png_ratio_log2` | `file` | `*_ratio.log2.png` | Image of ratio log2 plot |
| `png_ratio` | `file` | `*_ratio.png` | Image of ratio plot |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## CONTROLFREEC_FREEC2CIRCOS {#controlfreec-freec2circos}

*Defined in `modules/nf-core/controlfreec/freec2circos/main.nf:1`*

**Keywords:** `cna`, `cnv`, `somatic`, `single`, `tumor-only`

Format Freec output to circos input format

### Tools

#### [controlfreec](http://boevalab.inf.ethz.ch/FREEC)

Copy number and genotype annotation from whole genome and whole exome sequencing data.

[Homepage](http://boevalab.inf.ethz.ch/FREEC) | [Documentation](http://boevalab.inf.ethz.ch/FREEC/tutorial.html) | License: GPL >=2

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `ratio` | `file` | ratio file generated by FREEC |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `circos` | `file` | `*.circos.txt` | Txt file |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## CONTROLFREEC_FREEC {#controlfreec-freec}

*Defined in `modules/nf-core/controlfreec/freec/main.nf:1`*

**Keywords:** `cna`, `cnv`, `somatic`, `single`, `tumor-only`

Copy number and genotype annotation from whole genome and whole exome sequencing data

### Tools

#### [controlfreec/freec](http://boevalab.inf.ethz.ch/FREEC)

Copy number and genotype annotation from whole genome and whole exome sequencing data.

[Homepage](http://boevalab.inf.ethz.ch/FREEC) | [Documentation](http://boevalab.inf.ethz.ch/FREEC/tutorial.html) | License: GPL >=2

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `mpileup_normal` | `file` | miniPileup file |
| `mpileup_tumor` | `file` | miniPileup file |
| `cpn_normal` | `file` | Raw copy number profiles (optional) |
| `cpn_tumor` | `file` | Raw copy number profiles (optional) |
| `minipileup_normal` | `file` | miniPileup file from previous run (optional) |
| `minipileup_tumor` | `file` | miniPileup file from previous run (optional) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bedgraph` | `file` | `.bedgraph` | Bedgraph format for the UCSC genome browser |
| `control_cpn` | `file` | `*_control.cpn` | files with raw copy number profiles |
| `sample_cpn` | `file` | `*_sample.cpn` | files with raw copy number profiles |
| `gcprofile_cpn` | `file` | `GC_profile.*.cpn` | file with GC-content profile. |
| `BAF` | `file` | `*_BAF.txt` | file B-allele frequencies for each possibly heterozygous SNP position |
| `CNV` | `file` | `*_CNVs` | file with coordinates of predicted copy number alterations. |
| `info` | `file` | `*_info.txt` | parsable file with information about FREEC run |
| `ratio` | `file` | `*_ratio.txt` | file with ratios and predicted copy number alterations for each window |
| `config` | `file` | `config.txt` | Config file used to run Control-FREEC |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## CONTROLFREEC_ASSESSSIGNIFICANCE {#controlfreec-assesssignificance}

*Defined in `modules/nf-core/controlfreec/assesssignificance/main.nf:1`*

**Keywords:** `cna`, `cnv`, `somatic`, `single`, `tumor-only`

Add both Wilcoxon test and Kolmogorov-Smirnov test p-values to each CNV output of FREEC

### Tools

#### [controlfreec/assesssignificance](http://boevalab.inf.ethz.ch/FREEC)

Copy number and genotype annotation from whole genome and whole exome sequencing data.

[Homepage](http://boevalab.inf.ethz.ch/FREEC) | [Documentation](http://boevalab.inf.ethz.ch/FREEC/tutorial.html) | License: GPL >=2

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `cnvs` | `file` | _CNVs file generated by FREEC |
| `ratio` | `file` | ratio file generated by FREEC |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `p_value_txt` | `file` | `*.p.value.txt` | CNV file containing p_values for each call |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## GOLEFT_INDEXCOV {#goleft-indexcov}

*Defined in `modules/nf-core/goleft/indexcov/main.nf:1`*

**Keywords:** `coverage`, `cnv`, `genomics`, `depth`

Quickly estimate coverage from a whole-genome bam or cram index. A bam index has 16KB resolution so that's what this gives, but it provides what appears to be a high-quality coverage estimate in seconds per genome.

### Tools

#### [goleft](https://github.com/brentp/goleft)

goleft is a collection of bioinformatics tools distributed under MIT license in a single static binary

[Homepage](https://github.com/brentp/goleft) | [Documentation](https://github.com/brentp/goleft) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false] |
| `bams` | `file` | Sorted BAM/CRAM/SAM files |
| `indexes` | `file` | BAI/CRAI files |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false] |
| `fai` | `file` | FASTA index |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@lindenb](https://github.com/lindenb)
**Maintainers:** [@lindenb](https://github.com/lindenb)


## DRAGMAP_ALIGN {#dragmap-align}

*Defined in `modules/nf-core/dragmap/align/main.nf:1`*

**Keywords:** `alignment`, `map`, `fastq`, `bam`, `sam`

Performs fastq alignment to a reference using DRAGMAP

### Tools

#### [dragmap](https://github.com/Illumina/dragmap)

Dragmap is the Dragen mapper/aligner Open Source Software.

[Homepage](https://github.com/Illumina/dragmap) | [Documentation](https://github.com/Illumina/dragmap) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | List of input FastQ files of size 1 and 2 for single-end and paired-end data, respectively. |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test', single_end:false ] |
| `hashmap` | `file` | DRAGMAP hash table |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome'] |
| `fasta` | `file` | Genome fasta reference files |
| `sort_bam` | `boolean` | Sort the BAM file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.sam")` | `tuple` | `sam` | - |
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `val(meta), path("*.csi")` | `tuple` | `csi` | - |
| `val(meta), path('*.log')` | `tuple` | `log` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@edmundmiller](https://github.com/edmundmiller)
**Maintainers:** [@edmundmiller](https://github.com/edmundmiller)


## DRAGMAP_HASHTABLE {#dragmap-hashtable}

*Defined in `modules/nf-core/dragmap/hashtable/main.nf:1`*

**Keywords:** `index`, `fasta`, `genome`, `reference`

Create DRAGEN hashtable for reference genome

### Tools

#### [dragmap](https://github.com/Illumina/dragmap)

Dragmap is the Dragen mapper/aligner Open Source Software.

[Homepage](https://github.com/Illumina/dragmap) | [Documentation](https://github.com/Illumina/dragmap) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing reference information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Input genome fasta file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `hashmap` | `file` | `*.{cmp,.bin,.txt}` | DRAGMAP hash table |

**Authors:** [@edmundmiller](https://github.com/edmundmiller)
**Maintainers:** [@edmundmiller](https://github.com/edmundmiller)


## STRELKA_GERMLINE {#strelka-germline}

*Defined in `modules/nf-core/strelka/germline/main.nf:1`*

**Keywords:** `variantcalling`, `germline`, `wgs`, `vcf`, `variants`

Strelka2 is a fast and accurate small variant caller optimized for analysis of germline variation

### Tools

#### [strelka](https://github.com/Illumina/strelka)

Strelka calls somatic and germline small variants from mapped sequencing reads

[Homepage](https://github.com/Illumina/strelka) | [Documentation](https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/README.md) | [biotools:strelka](https://bio.tools/strelka) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `input` | `file` | BAM/CRAM file |
| `input_index` | `file` | BAM/CRAI index file |
| `target_bed` | `file` | BED file containing target regions for variant calling |
| `target_bed_index` | `file` | Index for BED file containing target regions for variant calling |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.{vcf.gz}` | gzipped germline variant file |
| `vcf_tbi` | `file` | `*.vcf.gz.tbi` | index file for the vcf file |
| `genome_vcf` | `file` | `*_genome.vcf.gz` | variant records and compressed non-variant blocks |
| `genome_vcf_tbi` | `file` | `*_genome.vcf.gz.tbi` | index file for the genome_vcf file |

**Authors:** [@arontommi](https://github.com/arontommi)
**Maintainers:** [@arontommi](https://github.com/arontommi)


## STRELKA_SOMATIC {#strelka-somatic}

*Defined in `modules/nf-core/strelka/somatic/main.nf:1`*

**Keywords:** `variant calling`, `germline`, `wgs`, `vcf`, `variants`

Strelka2 is a fast and accurate small variant caller optimized for analysis of germline variation in small cohorts and somatic variation in tumor/normal sample pairs

### Tools

#### [strelka](https://github.com/Illumina/strelka)

Strelka calls somatic and germline small variants from mapped sequencing reads

[Homepage](https://github.com/Illumina/strelka) | [Documentation](https://github.com/Illumina/strelka/blob/v2.9.x/docs/userGuide/README.md) | [biotools:strelka](https://bio.tools/strelka) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input_normal` | `file` | BAM/CRAM/SAM file |
| `input_index_normal` | `file` | BAM/CRAM/SAM index file |
| `input_tumor` | `file` | BAM/CRAM/SAM file |
| `input_index_tumor` | `file` | BAM/CRAM/SAM index file |
| `manta_candidate_small_indels` | `file` | VCF.gz file |
| `manta_candidate_small_indels_tbi` | `file` | VCF.gz index file |
| `target_bed` | `file` | BED file containing target regions for variant calling |
| `target_bed_index` | `file` | Index for BED file containing target regions for variant calling |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf_indels` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `vcf_indels_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |
| `vcf_snvs` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `vcf_snvs_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |

**Authors:** [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@drpatelh](https://github.com/drpatelh)


## BWA_INDEX {#bwa-index}

*Defined in `modules/nf-core/bwa/index/main.nf:1`*

**Keywords:** `index`, `fasta`, `genome`, `reference`

Create BWA index for reference genome

### Tools

#### [bwa](http://bio-bwa.sourceforge.net/)

BWA is a software package for mapping DNA sequences against
a large reference genome, such as the human genome.

[Homepage](http://bio-bwa.sourceforge.net/) | [Documentation](https://bio-bwa.sourceforge.net/bwa.shtml) | [biotools:bwa](https://bio.tools/bwa) | License: GPL-3.0-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Input genome fasta file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `index` | `map` | `*.{amb,ann,bwt,pac,sa}` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@maxulysse](https://github.com/maxulysse), [@gallvp](https://github.com/gallvp)


## BWA_MEM {#bwa-mem}

*Defined in `modules/nf-core/bwa/mem/main.nf:1`*

**Keywords:** `mem`, `bwa`, `alignment`, `map`, `fastq`, `bam`, `sam`

Performs fastq alignment to a fasta reference using BWA

### Tools

#### [bwa](http://bio-bwa.sourceforge.net/)

BWA is a software package for mapping DNA sequences against
a large reference genome, such as the human genome.

[Homepage](http://bio-bwa.sourceforge.net/) | [Documentation](https://bio-bwa.sourceforge.net/bwa.shtml) | [biotools:bwa](https://bio.tools/bwa) | License: GPL-3.0-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | List of input FastQ files of size 1 and 2 for single-end and paired-end data, respectively. |
| `meta2` | `map` | Groovy Map containing reference information. e.g. [ id:'test', single_end:false ] |
| `index` | `file` | BWA genome index files |
| `meta3` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Reference genome in FASTA format |
| `sort_bam` | `boolean` | use samtools sort (true) or samtools view (false) |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.csi")` | `tuple` | `csi` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@drpatelh](https://github.com/drpatelh), [@jeremy1805](https://github.com/jeremy1805), [@matthdsm](https://github.com/matthdsm)
**Maintainers:** [@drpatelh](https://github.com/drpatelh), [@jeremy1805](https://github.com/jeremy1805), [@matthdsm](https://github.com/matthdsm)


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
| `report` | `file` | `*.csv` | snpEff report csv file |
| `summary_html` | `file` | `*.html` | snpEff summary statistics in html file |
| `genes_txt` | `file` | `*.genes.txt` | txt (tab separated) file having counts of the number of variants affecting each transcript and gene |

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


## NGSCHECKMATE_NCM {#ngscheckmate-ncm}

*Defined in `modules/nf-core/ngscheckmate/ncm/main.nf:1`*

**Keywords:** `ngscheckmate`, `matching`, `snp`

Determining whether sequencing data comes from the same individual by using SNP matching. Designed for humans on vcf or bam files.

### Tools

#### [ngscheckmate](https://github.com/parklab/NGSCheckMate)

NGSCheckMate is a software package for identifying next generation sequencing (NGS) data files from the same individual, including matching between DNA and RNA.

[Homepage](https://github.com/parklab/NGSCheckMate) | [Documentation](https://github.com/parklab/NGSCheckMate) | [biotools:ngscheckmate](https://bio.tools/ngscheckmate) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test'] |
| `files` | `file` | VCF or BAM files for each sample, in a merged channel (possibly gzipped). BAM files require an index too. |
| `meta2` | `map` | Groovy Map containing SNP information e.g. [ id:'test' ] |
| `snp_bed` | `file` | BED file containing the SNPs to analyse |
| `meta3` | `map` | Groovy Map containing reference fasta index information e.g. [ id:'test' ] |
| `fasta` | `file` | fasta file for the genome, only used in the bam mode |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*_corr_matrix.txt")` | `tuple` | `corr_matrix` | - |
| `val(meta), path("*_matched.txt")` | `tuple` | `matched` | - |
| `val(meta), path("*_all.txt")` | `tuple` | `all` | - |
| `val(meta), path("*.pdf")` | `tuple` | `pdf` | - |
| `val(meta), path("*.vcf")` | `tuple` | `vcf` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@sppearce](https://github.com/sppearce)
**Maintainers:** [@sppearce](https://github.com/sppearce)


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
| `report` | `-` | `-` | - |

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


## VARLOCIRAPTOR_CALLVARIANTS {#varlociraptor-callvariants}

*Defined in `modules/nf-core/varlociraptor/callvariants/main.nf:1`*

**Keywords:** `observations`, `variants`, `calling`

Call variants for a given scenario specified with the varlociraptor calling grammar, preprocessed by varlociraptor preprocessing

### Tools

#### [varlociraptor](https://varlociraptor.github.io/docs/estimating/)

Flexible, uncertainty-aware variant calling with parameter free filtration via FDR control.

[Homepage](https://varlociraptor.github.io/docs/estimating/) | [Documentation](https://varlociraptor.github.io/docs/calling/) | [biotools:varlociraptor](https://bio.tools/varlociraptor) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcfs` | `file` | Sorted VCF/BCF file containing sample observations, Can also be a list of files |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bcf` | `file` | `*.bcf` | BCF file containing sample observations |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@famosab](https://github.com/famosab)


## VARLOCIRAPTOR_PREPROCESS {#varlociraptor-preprocess}

*Defined in `modules/nf-core/varlociraptor/preprocess/main.nf:1`*

**Keywords:** `observations`, `variants`, `preprocessing`

Obtains per-sample observations for the actual calling process with varlociraptor calls

### Tools

#### [varlociraptor](https://varlociraptor.github.io/docs/estimating/)

Flexible, uncertainty-aware variant calling with parameter free
filtration via FDR control.

[Homepage](https://varlociraptor.github.io/docs/estimating/) | [Documentation](https://varlociraptor.github.io/docs/calling/) | [biotools:varlociraptor](https://bio.tools/varlociraptor) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | Sorted BAM/CRAM/SAM file |
| `bai` | `file` | Index of the BAM/CRAM/SAM file |
| `candidates` | `file` | Sorted BCF/VCF file |
| `alignment_json` | `file` | File containing alignment properties obtained with varlociraptor/estimatealignmentproperties |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Reference fasta file |
| `meta3` | `map` | Groovy Map containing reference index information e.g. [ id:'test', single_end:false ] |
| `fai` | `file` | Index for reference fasta file (must be with samtools index) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bcf` | `file` | `*.bcf` | BCF file containing sample observations |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@famosab](https://github.com/famosab)


## VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES {#varlociraptor-estimatealignmentproperties}

*Defined in `modules/nf-core/varlociraptor/estimatealignmentproperties/main.nf:1`*

**Keywords:** `estimation`, `alignment`, `variants`

In order to judge about candidate indel and structural variants, Varlociraptor needs to know about certain properties of the underlying sequencing experiment in combination with the used read aligner.

### Tools

#### [varlociraptor](https://varlociraptor.github.io/docs/estimating/)

Flexible, uncertainty-aware variant calling with parameter free filtration via FDR control.

[Homepage](https://varlociraptor.github.io/docs/estimating/) | [Documentation](https://varlociraptor.github.io/docs/estimating/) | [biotools:varlociraptor](https://bio.tools/varlociraptor) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | Sorted BAM/CRAM/SAM file |
| `bai` | `file` | Index of sorted BAM/CRAM/SAM file |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Reference fasta file |
| `meta3` | `map` | Groovy Map containing reference index information e.g. [ id:'test', single_end:false ] |
| `fai` | `file` | Index for reference fasta file (must be with samtools index) |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `alignment_properties_json` | `file` | `*.alignment-properties.json` | File containing alignment properties |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@famosab](https://github.com/famosab)


## CNVKIT_GENEMETRICS {#cnvkit-genemetrics}

*Defined in `modules/nf-core/cnvkit/genemetrics/main.nf:1`*

**Keywords:** `cnvkit`, `bam`, `fasta`, `copy number`

Copy number variant detection from high-throughput sequencing data

### Tools

#### [cnvkit](https://cnvkit.readthedocs.io/en/stable/index.html)

CNVkit is a Python library and command-line software toolkit to infer and visualize copy number from high-throughput DNA sequencing data. It is designed for use with hybrid capture, including both whole-exome and custom target panels, and short-read sequencing platforms such as Illumina and Ion Torrent.

[Homepage](https://cnvkit.readthedocs.io/en/stable/index.html) | [Documentation](https://cnvkit.readthedocs.io/en/stable/index.html) | [biotools:cnvkit](https://bio.tools/cnvkit) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `cnr` | `file` | CNR file |
| `cns` | `file` | CNS file [Optional] |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.tsv")` | `tuple` | `tsv` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot), [@marrip](https://github.com/marrip), [@priesgo](https://github.com/priesgo)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot), [@marrip](https://github.com/marrip), [@priesgo](https://github.com/priesgo)


## CNVKIT_CALL {#cnvkit-call}

*Defined in `modules/nf-core/cnvkit/call/main.nf:1`*

**Keywords:** `cnvkit`, `bam`, `fasta`, `copy number`

Given segmented log2 ratio estimates (.cns), derive each segment’s absolute integer copy number

### Tools

#### [cnvkit](https://cnvkit.readthedocs.io/en/stable/index.html)

CNVkit is a Python library and command-line software toolkit to infer and visualize copy number from high-throughput DNA sequencing data. It is designed for use with hybrid capture, including both whole-exome and custom target panels, and short-read sequencing platforms such as Illumina and Ion Torrent.

[Homepage](https://cnvkit.readthedocs.io/en/stable/index.html) | [Documentation](https://cnvkit.readthedocs.io/en/stable/index.html) | [biotools:cnvkit](https://bio.tools/cnvkit) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `cns` | `file` | CNVKit CNS file. |
| `vcf` | `file` | Germline VCF file for BAF. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.cns")` | `tuple` | `cns` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot), [@priesgo](https://github.com/priesgo)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot), [@priesgo](https://github.com/priesgo)


## CNVKIT_BATCH {#cnvkit-batch}

*Defined in `modules/nf-core/cnvkit/batch/main.nf:1`*

**Keywords:** `cnvkit`, `bam`, `fasta`, `copy number`

Copy number variant detection from high-throughput sequencing data

### Tools

#### [cnvkit](https://cnvkit.readthedocs.io/en/stable/index.html)

CNVkit is a Python library and command-line software toolkit to infer and visualize copy number from high-throughput DNA sequencing data. It is designed for use with hybrid capture, including both whole-exome and custom target panels, and short-read sequencing platforms such as Illumina and Ion Torrent.

[Homepage](https://cnvkit.readthedocs.io/en/stable/index.html) | [Documentation](https://cnvkit.readthedocs.io/en/stable/index.html) | [biotools:cnvkit](https://bio.tools/cnvkit) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `tumor` | `file` | Input tumour sample bam file (or cram) |
| `normal` | `file` | Input normal sample bam file (or cram) |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `fasta` | `file` | Input reference genome fasta file (only needed for cram_input and/or when normal_samples are provided) |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'test' ] |
| `fasta_fai` | `file` | Input reference genome fasta index (optional, but recommended for cram_input) |
| `meta4` | `map` | Groovy Map containing information about target file e.g. [ id:'test' ] |
| `targets` | `file` | Input target bed file |
| `meta5` | `map` | Groovy Map containing information about reference file e.g. [ id:'test' ] |
| `reference` | `file` | Input reference cnn-file (only for germline and tumor-only running) |
| `panel_of_normals` | `file` | Input panel of normals file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bed")` | `tuple` | `bed` | - |
| `val(meta), path("*.cnn")` | `tuple` | `cnn` | - |
| `val(meta), path("*.cnr")` | `tuple` | `cnr` | - |
| `val(meta), path("*.cns")` | `tuple` | `cns` | - |
| `val(meta), path("*.pdf")` | `tuple` | `pdf` | - |
| `val(meta), path("*.png")` | `tuple` | `png` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot), [@drpatelh](https://github.com/drpatelh), [@fbdtemme](https://github.com/fbdtemme), [@kaurravneet4123](https://github.com/kaurravneet4123), [@KevinMenden](https://github.com/KevinMenden), [@lassefolkersen](https://github.com/lassefolkersen), [@MaxUlysse](https://github.com/MaxUlysse), [@priesgo](https://github.com/priesgo), [@SusiJo](https://github.com/SusiJo)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot), [@drpatelh](https://github.com/drpatelh), [@fbdtemme](https://github.com/fbdtemme), [@kaurravneet4123](https://github.com/kaurravneet4123), [@KevinMenden](https://github.com/KevinMenden), [@lassefolkersen](https://github.com/lassefolkersen), [@MaxUlysse](https://github.com/MaxUlysse), [@priesgo](https://github.com/priesgo), [@SusiJo](https://github.com/SusiJo)


## CNVKIT_ANTITARGET {#cnvkit-antitarget}

*Defined in `modules/nf-core/cnvkit/antitarget/main.nf:1`*

**Keywords:** `cvnkit`, `antitarget`, `cnv`, `copy number`

Derive off-target (“antitarget”) bins from target regions.

### Tools

#### [cnvkit](https://cnvkit.readthedocs.io/en/stable/index.html)

CNVkit is a Python library and command-line software toolkit to infer and visualize copy number from high-throughput DNA sequencing data.
It is designed for use with hybrid capture, including both whole-exome and custom target panels, and short-read sequencing platforms such as Illumina and Ion Torrent.

[Homepage](https://cnvkit.readthedocs.io/en/stable/index.html) | [Documentation](https://cnvkit.readthedocs.io/en/stable/index.html) | [biotools:cnvkit](https://bio.tools/cnvkit) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `targets` | `file` | File containing genomic regions |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bed")` | `tuple` | `bed` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot), [@priesgo](https://github.com/priesgo), [@SusiJo](https://github.com/SusiJo)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot), [@priesgo](https://github.com/priesgo), [@SusiJo](https://github.com/SusiJo)


## CNVKIT_EXPORT {#cnvkit-export}

*Defined in `modules/nf-core/cnvkit/export/main.nf:1`*

**Keywords:** `cnvkit`, `copy number`, `export`

Convert copy number ratio tables (.cnr files) or segments (.cns) to another format.

### Tools

#### [cnvkit](https://cnvkit.readthedocs.io/en/stable/index.html)

CNVkit is a Python library and command-line software toolkit to infer and
visualize copy number from high-throughput DNA sequencing data.
It is designed for use with hybrid capture, including both whole-exome and custom
target panels, and short-read sequencing platforms such as Illumina and Ion Torrent.

[Homepage](https://cnvkit.readthedocs.io/en/stable/index.html) | [Documentation](https://cnvkit.readthedocs.io/en/stable/index.html) | [biotools:cnvkit](https://bio.tools/cnvkit) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `cns` | `file` | CNVKit CNS file. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot), [@priesgo](https://github.com/priesgo)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot), [@priesgo](https://github.com/priesgo)


## CNVKIT_REFERENCE {#cnvkit-reference}

*Defined in `modules/nf-core/cnvkit/reference/main.nf:1`*

**Keywords:** `cnvkit`, `reference`, `cnv`, `copy number`

Compile a coverage reference from the given files (normal samples).

### Tools

#### [cnvkit](https://cnvkit.readthedocs.io/en/stable/index.html)

CNVkit is a Python library and command-line software toolkit to infer and visualize copy number from high-throughput DNA sequencing data.
It is designed for use with hybrid capture, including both whole-exome and custom target panels, and short-read sequencing platforms such as Illumina and Ion Torrent.

[Homepage](https://cnvkit.readthedocs.io/en/stable/index.html) | [Documentation](https://cnvkit.readthedocs.io/en/stable/index.html) | [biotools:cnvkit](https://bio.tools/cnvkit) | License: Apache-2.0

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `fasta` | `file` | File containing reference genome |
| `targets` | `file` | File containing genomic regions |
| `antitargets` | `file` | File containing off-target genomic regions |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `*.cnn` | `path` | `cnn` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot), [@priesgo](https://github.com/priesgo), [@SusiJo](https://github.com/SusiJo)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot), [@priesgo](https://github.com/priesgo), [@SusiJo](https://github.com/SusiJo)


## RBT_VCFSPLIT {#rbt-vcfsplit}

*Defined in `modules/nf-core/rbt/vcfsplit/main.nf:1`*

**Keywords:** `genomics`, `splitting`, `VCF`, `BCF`, `variants`

A tool for splitting VCF/BCF files into N equal chunks, including BND support

### Tools

#### [rust-bio-tools](https://github.com/rust-bio/rust-bio-tools)

A growing collection of fast and secure command line utilities for dealing with NGS data implemented on top of Rust-Bio.

[Homepage](https://github.com/rust-bio/rust-bio-tools) | [Documentation](https://github.com/rust-bio/rust-bio-tools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. `[ id:'sample1' ]` |
| `vcf` | `file` | VCF file with variants to be split |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bcfchunks` | `file` | `*.bcf` | Chunks of the input VCF file, split into `numchunks` equal parts. |

**Authors:** [@famosab](https://github.com/famosab)
**Maintainers:** [@famosab](https://github.com/famosab)


## FGBIO_FASTQTOBAM {#fgbio-fastqtobam}

*Defined in `modules/nf-core/fgbio/fastqtobam/main.nf:1`*

**Keywords:** `unaligned`, `bam`, `cram`

Using the fgbio tools, converts FASTQ files sequenced into unaligned BAM or CRAM files possibly moving the UMI barcode into the RX field of the reads

### Tools

#### [fgbio](http://fulcrumgenomics.github.io/fgbio/)

A set of tools for working with genomic and high throughput sequencing data, including UMIs

[Homepage](http://fulcrumgenomics.github.io/fgbio/) | [Documentation](http://fulcrumgenomics.github.io/fgbio/tools/latest/) | [biotools:fgbio](https://bio.tools/fgbio) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | pair of reads to be converted into BAM file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@lescai](https://github.com/lescai), [@matthdsm](https://github.com/matthdsm), [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@lescai](https://github.com/lescai), [@matthdsm](https://github.com/matthdsm), [@nvnieuwk](https://github.com/nvnieuwk)


## FGBIO_COPYUMIFROMREADNAME {#fgbio-copyumifromreadname}

*Defined in `modules/nf-core/fgbio/copyumifromreadname/main.nf:1`*

**Keywords:** `sort`, `example`, `genomics`

Copies the UMI at the end of a bam files read name to the RX tag.

### Tools

#### [fgbio](http://fulcrumgenomics.github.io/fgbio/)

A set of tools for working with genomic and high throughput sequencing data, including UMIs

[Homepage](http://fulcrumgenomics.github.io/fgbio/) | [Documentation](http://fulcrumgenomics.github.io/fgbio/tools/latest/CallDuplexConsensusReads.html) | [biotools:fgbio](https://bio.tools/fgbio) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. `[ id:'sample1' ]` |
| `bam` | `file` | Sorted BAM/CRAM/SAM file |
| `bai` | `file` | Index for bam file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam` | `file` | `*.{bam}` | Sorted BAM file |
| `bai` | `file` | `*.{bai}` | Index for bam file |

**Authors:** [@sppearce](https://github.com/sppearce)
**Maintainers:** [@sppearce](https://github.com/sppearce)


## FGBIO_CALLMOLECULARCONSENSUSREADS {#fgbio-callmolecularconsensusreads}

*Defined in `modules/nf-core/fgbio/callmolecularconsensusreads/main.nf:1`*

**Keywords:** `UMIs`, `consensus sequence`, `bam`

Calls consensus sequences from reads with the same unique molecular tag.

### Tools

#### [fgbio](https://github.com/fulcrumgenomics/fgbio)

Tools for working with genomic and high throughput sequencing data.

[Homepage](https://github.com/fulcrumgenomics/fgbio) | [Documentation](http://fulcrumgenomics.github.io/fgbio/) | [biotools:fgbio](https://bio.tools/fgbio) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false, collapse:false ] |
| `grouped_bam` | `file` | The input SAM or BAM file, grouped by UMIs |
| `min_reads` | `integer` | Minimum number of original reads to build each consensus read. |
| `min_baseq` | `integer` | Ignore bases in raw reads that have Q below this value. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@sruthipsuresh](https://github.com/sruthipsuresh)
**Maintainers:** [@sruthipsuresh](https://github.com/sruthipsuresh)


## FGBIO_GROUPREADSBYUMI {#fgbio-groupreadsbyumi}

*Defined in `modules/nf-core/fgbio/groupreadsbyumi/main.nf:1`*

**Keywords:** `UMI`, `groupreads`, `fgbio`

Groups reads together that appear to have come from the same original molecule.
Reads are grouped by template, and then templates are sorted by the 5’ mapping positions
of the reads from the template, used from earliest mapping position to latest.
Reads that have the same end positions are then sub-grouped by UMI sequence.
(!) Note: the MQ tag is required on reads with mapped mates (!)
This can be added using samblaster with the optional argument --addMateTags.

### Tools

#### [fgbio](http://fulcrumgenomics.github.io/fgbio/)

A set of tools for working with genomic and high throughput sequencing data, including UMIs

[Homepage](http://fulcrumgenomics.github.io/fgbio/) | [Documentation](http://fulcrumgenomics.github.io/fgbio/tools/latest/) | [biotools:fgbio](https://bio.tools/fgbio) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | BAM file. Note: the MQ tag is required on reads with mapped mates (!) |
| `strategy` | `string` | Required argument: defines the UMI assignment strategy. Must be chosen among: Identity, Edit, Adjacency, Paired. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*histogram.txt")` | `tuple` | `histogram` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@lescai](https://github.com/lescai)
**Maintainers:** [@lescai](https://github.com/lescai)


## BWAMEM2_INDEX {#bwamem2-index}

*Defined in `modules/nf-core/bwamem2/index/main.nf:1`*

**Keywords:** `index`, `fasta`, `genome`, `reference`

Create BWA-mem2 index for reference genome

### Tools

#### [bwamem2](https://github.com/bwa-mem2/bwa-mem2)

BWA-mem2 is a software package for mapping DNA sequences against
a large reference genome, such as the human genome.

[Homepage](https://github.com/bwa-mem2/bwa-mem2) | [Documentation](https://github.com/bwa-mem2/bwa-mem2#usage) | [biotools:bwa-mem2](https://bio.tools/bwa-mem2) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Input genome fasta file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `index` | `file` | `*.{0123,amb,ann,bwt.2bit.64,pac}` | BWA genome index files |

**Authors:** [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@maxulysse](https://github.com/maxulysse)


## BWAMEM2_MEM {#bwamem2-mem}

*Defined in `modules/nf-core/bwamem2/mem/main.nf:1`*

**Keywords:** `mem`, `bwa`, `alignment`, `map`, `fastq`, `bam`, `sam`

Performs fastq alignment to a fasta reference using BWA

### Tools

#### [bwa](https://github.com/bwa-mem2/bwa-mem2)

BWA-mem2 is a software package for mapping DNA sequences against
a large reference genome, such as the human genome.

[Homepage](https://github.com/bwa-mem2/bwa-mem2) | [Documentation](http://www.htslib.org/doc/samtools.html) | [biotools:bwa-mem2](https://bio.tools/bwa-mem2) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | List of input FastQ files of size 1 and 2 for single-end and paired-end data, respectively. |
| `meta2` | `map` | Groovy Map containing reference/index information e.g. [ id:'test' ] |
| `index` | `file` | BWA genome index files |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Reference genome in FASTA format |
| `sort_bam` | `boolean` | use samtools sort (true) or samtools view (false) |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.sam")` | `tuple` | `sam` | - |
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `val(meta), path("*.csi")` | `tuple` | `csi` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm)


## MANTA_TUMORONLY {#manta-tumoronly}

*Defined in `modules/nf-core/manta/tumoronly/main.nf:1`*

**Keywords:** `somatic`, `wgs`, `wxs`, `panel`, `vcf`, `structural variants`, `small indels`

Manta calls structural variants (SVs) and indels from mapped paired-end sequencing reads. It is optimized for analysis of germline variation in small sets of individuals and somatic variation in tumor/normal sample pairs.

### Tools

#### [manta](https://github.com/Illumina/manta)

Structural variant and indel caller for mapped sequencing data

[Homepage](https://github.com/Illumina/manta) | [Documentation](https://github.com/Illumina/manta/blob/v1.6.0/docs/userGuide/README.md) | [biotools:manta_sv](https://bio.tools/manta_sv) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM/SAM file |
| `input_index` | `file` | BAM/CRAM/SAM index file |
| `target_bed` | `file` | BED file containing target regions for variant calling |
| `target_bed_tbi` | `file` | Index for BED file containing target regions for variant calling |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Genome reference FASTA file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Genome reference FASTA index file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `candidate_small_indels_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `candidate_small_indels_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |
| `candidate_sv_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `candidate_sv_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |
| `tumor_sv_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `tumor_sv_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@nvnieuwk](https://github.com/nvnieuwk)


## MANTA_GERMLINE {#manta-germline}

*Defined in `modules/nf-core/manta/germline/main.nf:1`*

**Keywords:** `somatic`, `wgs`, `wxs`, `panel`, `vcf`, `structural variants`, `small indels`

Manta calls structural variants (SVs) and indels from mapped paired-end sequencing reads. It is optimized for analysis of germline variation in small sets of individuals and somatic variation in tumor/normal sample pairs.

### Tools

#### [manta](https://github.com/Illumina/manta)

Structural variant and indel caller for mapped sequencing data

[Homepage](https://github.com/Illumina/manta) | [Documentation](https://github.com/Illumina/manta/blob/v1.6.0/docs/userGuide/README.md) | [biotools:manta_sv](https://bio.tools/manta_sv) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM/SAM file. For joint calling use a list of files. |
| `index` | `file` | BAM/CRAM/SAM index file. For joint calling use a list of files. |
| `target_bed` | `file` | BED file containing target regions for variant calling |
| `target_bed_tbi` | `file` | Index for BED file containing target regions for variant calling |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Genome reference FASTA file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Genome reference FASTA index file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `candidate_small_indels_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `candidate_small_indels_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |
| `candidate_sv_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `candidate_sv_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |
| `diploid_sv_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `diploid_sv_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@ramprasadn](https://github.com/ramprasadn), [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@ramprasadn](https://github.com/ramprasadn), [@nvnieuwk](https://github.com/nvnieuwk)


## MANTA_SOMATIC {#manta-somatic}

*Defined in `modules/nf-core/manta/somatic/main.nf:1`*

**Keywords:** `somatic`, `wgs`, `wxs`, `panel`, `vcf`, `structural variants`, `small indels`

Manta calls structural variants (SVs) and indels from mapped paired-end sequencing reads. It is optimized for analysis of germline variation in small sets of individuals and somatic variation in tumor/normal sample pairs.

### Tools

#### [manta](https://github.com/Illumina/manta)

Structural variant and indel caller for mapped sequencing data

[Homepage](https://github.com/Illumina/manta) | [Documentation](https://github.com/Illumina/manta/blob/v1.6.0/docs/userGuide/README.md) | [biotools:manta_sv](https://bio.tools/manta_sv) | License: GPL v3

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input_normal` | `file` | BAM/CRAM/SAM file |
| `input_index_normal` | `file` | BAM/CRAM/SAM index file |
| `input_tumor` | `file` | BAM/CRAM/SAM file |
| `input_index_tumor` | `file` | BAM/CRAM/SAM index file |
| `target_bed` | `file` | BED file containing target regions for variant calling |
| `target_bed_tbi` | `file` | Index for BED file containing target regions for variant calling |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | Genome reference FASTA file |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | Genome reference FASTA index file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `candidate_small_indels_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `candidate_small_indels_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |
| `candidate_sv_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `candidate_sv_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |
| `diploid_sv_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `diploid_sv_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |
| `somatic_sv_vcf` | `file` | `*.{vcf.gz}` | Gzipped VCF file containing variants |
| `somatic_sv_vcf_tbi` | `file` | `*.{vcf.gz.tbi}` | Index for gzipped VCF file containing variants |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen), [@nvnieuwk](https://github.com/nvnieuwk)


## BCFTOOLS_CONCAT {#bcftools-concat}

*Defined in `modules/nf-core/bcftools/concat/main.nf:1`*

**Keywords:** `variant calling`, `concat`, `bcftools`, `VCF`

Concatenate VCF files

### Tools

#### [concat](http://samtools.github.io/bcftools/bcftools.html)

Concatenate VCF files.

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](http://www.htslib.org/doc/bcftools.html) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcfs` | `list` | List containing 2 or more vcf files e.g. [ 'file1.vcf', 'file2.vcf' ] |
| `tbi` | `list` | List containing 2 or more index files (optional) e.g. [ 'file1.tbi', 'file2.tbi' ] |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@abhi18av](https://github.com/abhi18av), [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@abhi18av](https://github.com/abhi18av), [@nvnieuwk](https://github.com/nvnieuwk)


## BCFTOOLS_SORT {#bcftools-sort}

*Defined in `modules/nf-core/bcftools/sort/main.nf:1`*

**Keywords:** `sorting`, `VCF`, `variant calling`

Sorts VCF files

### Tools

#### [sort](http://samtools.github.io/bcftools/bcftools.html)

Sort VCF files by coordinates.

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](http://www.htslib.org/doc/bcftools.html) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcf` | `file` | The VCF/BCF file to be sorted |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@Gwennid](https://github.com/Gwennid)
**Maintainers:** [@Gwennid](https://github.com/Gwennid)


## BCFTOOLS_MERGE {#bcftools-merge}

*Defined in `modules/nf-core/bcftools/merge/main.nf:1`*

**Keywords:** `variant calling`, `merge`, `VCF`

Merge VCF files

### Tools

#### [merge](http://samtools.github.io/bcftools/bcftools.html)

Merge VCF files.

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](http://www.htslib.org/doc/bcftools.html) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcfs` | `file` | List containing 2 or more vcf files e.g. [ 'file1.vcf', 'file2.vcf' ] |
| `tbis` | `file` | List containing the tbi index files corresponding to the vcfs input files e.g. [ 'file1.vcf.tbi', 'file2.vcf.tbi' ] |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | (Optional) The fasta reference file (only necessary for the `--gvcf FILE` parameter) |
| `meta3` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fai` | `file` | (Optional) The fasta reference file index (only necessary for the `--gvcf FILE` parameter) |
| `meta4` | `map` | Groovy Map containing bed information e.g. [ id:'genome' ] |
| `bed` | `file` | (Optional) The bed regions to merge on |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.{vcf,vcf.gz,bcf,bcf.gz}` | merged output file |
| `index` | `file` | `*.{csi,tbi}` | index of merged output |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@nvnieuwk](https://github.com/nvnieuwk), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@nvnieuwk](https://github.com/nvnieuwk), [@ramprasadn](https://github.com/ramprasadn)


## BCFTOOLS_MPILEUP {#bcftools-mpileup}

*Defined in `modules/nf-core/bcftools/mpileup/main.nf:1`*

**Keywords:** `variant calling`, `mpileup`, `VCF`

Compresses VCF files

### Tools

#### [mpileup](http://samtools.github.io/bcftools/bcftools.html)

Generates genotype likelihoods at each genomic position with coverage.

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](http://www.htslib.org/doc/bcftools.html) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `bam` | `file` | Input BAM file |
| `intervals` | `file` | Input intervals file. A file (commonly '.bed') containing regions to subset |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | FASTA reference file |
| `save_mpileup` | `boolean` | Save mpileup file generated by bcftools mpileup |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*stats.txt")` | `tuple` | `stats` | - |
| `val(meta), path("*.mpileup.gz")` | `tuple` | `mpileup` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh)


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


## BCFTOOLS_NORM {#bcftools-norm}

*Defined in `modules/nf-core/bcftools/norm/main.nf:1`*

**Keywords:** `normalize`, `norm`, `variant calling`, `VCF`

Normalize VCF file

### Tools

#### [norm](http://samtools.github.io/bcftools/bcftools.html)

Normalize VCF files.

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](http://www.htslib.org/doc/bcftools.html) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcf` | `file` | The vcf file to be normalized e.g. 'file1.vcf' |
| `tbi` | `file` | An optional index of the VCF file (for when the VCF is compressed) |
| `meta2` | `map` | Groovy Map containing reference information e.g. [ id:'genome' ] |
| `fasta` | `file` | FASTA reference file |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@abhi18av](https://github.com/abhi18av), [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@abhi18av](https://github.com/abhi18av), [@ramprasadn](https://github.com/ramprasadn)


## BCFTOOLS_VIEW {#bcftools-view}

*Defined in `modules/nf-core/bcftools/view/main.nf:1`*

**Keywords:** `variant calling`, `view`, `bcftools`, `VCF`

View, subset and filter VCF or BCF files by position and filtering expression. Convert between VCF and BCF

### Tools

#### [view](http://samtools.github.io/bcftools/bcftools.html)

View, subset and filter VCF or BCF files by position and filtering expression. Convert between VCF and BCF

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](http://www.htslib.org/doc/bcftools.html) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcf` | `file` | The vcf file to be inspected. e.g. 'file.vcf' |
| `index` | `file` | The tab index for the VCF file to be inspected. e.g. 'file.tbi' |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `file` | `*.{vcf,vcf.gz,bcf,bcf.gz}` | VCF normalized output file |
| `tbi` | `file` | `*.tbi` | Alternative VCF file index |
| `csi` | `file` | `*.csi` | Default VCF file index |

**Authors:** [@abhi18av](https://github.com/abhi18av)
**Maintainers:** [@abhi18av](https://github.com/abhi18av)


## BCFTOOLS_STATS {#bcftools-stats}

*Defined in `modules/nf-core/bcftools/stats/main.nf:1`*

**Keywords:** `variant calling`, `stats`, `VCF`

Generates stats from VCF files

### Tools

#### [stats](http://samtools.github.io/bcftools/bcftools.html)

Parses VCF or BCF and produces text file stats which is suitable for
machine processing and can be plotted using plot-vcfstats.

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](http://www.htslib.org/doc/bcftools.html) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcf` | `file` | VCF input file |
| `tbi` | `file` | The tab index for the VCF file to be inspected. Optional: only required when parameter regions is chosen. |
| `meta2` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `regions` | `file` | Optionally, restrict the operation to regions listed in this file. (VCF, BED or tab-delimited) |
| `meta3` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `targets` | `file` | Optionally, restrict the operation to regions listed in this file (doesn't rely upon tbi index files) |
| `meta4` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `samples` | `file` | Optional, file of sample names to be included or excluded. e.g. 'file.tsv' |
| `meta5` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `exons` | `file` | Tab-delimited file with exons for indel frameshifts (chr,beg,end; 1-based, inclusive, optionally bgzip compressed). e.g. 'exons.tsv.gz' |
| `meta6` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Faidx indexed reference sequence file to determine INDEL context. e.g. 'reference.fa' |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*stats.txt")` | `tuple` | `stats` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@SusiJo](https://github.com/SusiJo), [@TCLamnidis](https://github.com/TCLamnidis)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh), [@SusiJo](https://github.com/SusiJo), [@TCLamnidis](https://github.com/TCLamnidis)


## BCFTOOLS_ISEC {#bcftools-isec}

*Defined in `modules/nf-core/bcftools/isec/main.nf:1`*

**Keywords:** `variant calling`, `intersect`, `union`, `complement`, `VCF`, `BCF`

Apply set operations to VCF files

### Tools

#### [isec](http://samtools.github.io/bcftools/bcftools.html)

Computes intersections, unions and complements of VCF files.

[Homepage](http://samtools.github.io/bcftools/bcftools.html) | [Documentation](http://www.htslib.org/doc/bcftools.html) | [biotools:bcftools](https://bio.tools/bcftools) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `vcfs` | `list` | List containing 2 or more vcf/bcf files. These must be compressed and have an associated index. e.g. [ 'file1.vcf.gz', 'file2.vcf' ] |
| `tbis` | `list` | List containing the tbi index files corresponding to the vcf/bcf input files e.g. [ 'file1.vcf.tbi', 'file2.vcf.tbi' ] |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `results` | `directory` | `${prefix}` | Folder containing the set operations results perform on the vcf files |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh)


## MSISENSORPRO_SCAN {#msisensorpro-scan}

*Defined in `modules/nf-core/msisensorpro/scan/main.nf:1`*

**Keywords:** `micro-satellite-scan`, `msisensor-pro`, `scan`

MSIsensor-pro evaluates Microsatellite Instability (MSI) for cancer patients with next generation sequencing data. It accepts the whole genome sequencing, whole exome sequencing and target region (panel) sequencing data as input

### Tools

#### [msisensorpro](https://github.com/xjtu-omics/msisensor-pro)

Microsatellite Instability (MSI) detection using high-throughput sequencing data.

[Homepage](https://github.com/xjtu-omics/msisensor-pro) | [Documentation](https://github.com/xjtu-omics/msisensor-pro/wiki) | License: Custom Licence

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `fasta` | `file` | Reference genome |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `list` | `file` | `*.{list}` | File containing microsatellite list |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## MSISENSORPRO_MSISOMATIC {#msisensorpro-msisomatic}

*Defined in `modules/nf-core/msisensorpro/msisomatic/main.nf:1`*

**Keywords:** `micro-satellite-scan`, `msisensor-pro`, `msi`, `somatic`

MSIsensor-pro evaluates Microsatellite Instability (MSI) for cancer patients with next generation sequencing data. It accepts the whole genome sequencing, whole exome sequencing and target region (panel) sequencing data as input

### Tools

#### [msisensorpro](https://github.com/xjtu-omics/msisensor-pro)

Microsatellite Instability (MSI) detection using high-throughput sequencing data.

[Homepage](https://github.com/xjtu-omics/msisensor-pro) | [Documentation](https://github.com/xjtu-omics/msisensor-pro/wiki) | License: Custom Licence

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `normal` | `file` | BAM/CRAM/SAM file |
| `normal_index` | `file` | BAM/CRAM/SAM index file |
| `tumor` | `file` | BAM/CRAM/SAM file |
| `tumor_index` | `file` | BAM/CRAM/SAM index file |
| `intervals` | `file` | bed file containing interval information, optional |
| `meta2` | `map` | Groovy Map containing genome information e.g. [ id:'genome' ] |
| `fasta` | `file` | Reference genome |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `output_report` | `file` | `-` | File containing final report with all detected microsatellites, unstable somatic microsatellites, msi score |
| `output_dis` | `file` | `-` | File containing distribution results |
| `output_germline` | `file` | `-` | File containing germline results |
| `output_somatic` | `file` | `-` | File containing somatic results |

**Authors:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@FriederikeHanssen](https://github.com/FriederikeHanssen)


## MUSE_SUMP {#muse-sump}

*Defined in `modules/nf-core/muse/sump/main.nf:1`*

**Keywords:** `variant calling`, `somatic`, `wgs`, `wxs`, `vcf`

Computes tier-based cutoffs from a sample-specific error model which is generated by muse/call and reports the finalized variants

### Tools

#### [MuSE](https://bioinformatics.mdanderson.org/public-software/muse/)

Somatic point mutation caller based on Markov substitution model for molecular evolution

[Homepage](https://bioinformatics.mdanderson.org/public-software/muse/) | [Documentation](https://github.com/wwylab/MuSE) | License: https://github.com/danielfan/MuSE/blob/master/LICENSE

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. `[ id:'sample1', single_end:false ]` |
| `muse_call_txt` | `file` | single input file generated by 'MuSE call' |
| `meta2` | `map` | Groovy Map containing reference information. e.g. `[ id:'test' ]` |
| `ref_vcf` | `file` | dbSNP vcf file that should be bgzip compressed, tabix indexed and based on the same reference genome used in 'MuSE call' |
| `ref_vcf_tbi` | `file` | Tabix index for the dbSNP vcf file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `vcf` | `map` | `*.vcf.gz` | bgzipped vcf file with called variants |
| `tbi` | `map` | `*.vcf.gz.tbi` | tabix index of bgzipped vcf file with called variants |

**Authors:** [@famosab](https://github.com/famosab)
**Maintainers:** [@famosab](https://github.com/famosab)


## MUSE_CALL {#muse-call}

*Defined in `modules/nf-core/muse/call/main.nf:1`*

**Keywords:** `variant calling`, `somatic`, `wgs`, `wxs`, `vcf`

pre-filtering and calculating position-specific summary statistics using the Markov substitution model

### Tools

#### [MuSE](https://bioinformatics.mdanderson.org/public-software/muse/)

Somatic point mutation caller based on Markov substitution model for molecular evolution

[Homepage](https://bioinformatics.mdanderson.org/public-software/muse/) | [Documentation](https://github.com/wwylab/MuSE) | License: https://github.com/danielfan/MuSE/blob/master/LICENSE

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. `[ id:'sample1' ]` |
| `tumor_bam` | `file` | Sorted tumor BAM file |
| `tumor_bai` | `file` | Index file for the tumor BAM file |
| `normal_bam` | `file` | Sorted matched normal BAM file |
| `normal_bai` | `file` | Index file for the normal BAM file |
| `meta2` | `map` | Groovy Map containing reference information. e.g. `[ id:'test' ]` |
| `reference` | `file` | reference genome file |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `txt` | `file` | `*.MuSE.txt` | position-specific summary statistics |

**Authors:** [@famosab](https://github.com/famosab)
**Maintainers:** [@famosab](https://github.com/famosab)


## PARABRICKS_FQ2BAM {#parabricks-fq2bam}

*Defined in `modules/nf-core/parabricks/fq2bam/main.nf:1`*

**Keywords:** `align`, `sort`, `bqsr`, `duplicates`

NVIDIA Clara Parabricks GPU-accelerated alignment, sorting, BQSR calculation, and duplicate marking. Note this nf-core module requires files to be copied into the working directory and not symlinked.

### Tools

#### [parabricks](https://www.nvidia.com/en-us/clara/genomics/)

NVIDIA Clara Parabricks GPU-accelerated genomics tools

[Homepage](https://www.nvidia.com/en-us/clara/genomics/) | [Documentation](https://docs.nvidia.com/clara/parabricks/latest/index.html) | License: custom

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `reads` | `file` | fastq.gz files |
| `meta2` | `map` | Groovy Map containing fasta information |
| `fasta` | `file` | reference fasta file - must be unzipped |
| `meta3` | `map` | Groovy Map containing index information |
| `index` | `file` | reference BWA index |
| `meta4` | `map` | Groovy Map containing index information |
| `interval_file` | `file` | (optional) file(s) containing genomic intervals for use in base quality score recalibration (BQSR) |
| `meta5` | `map` | Groovy Map containing known sites information |
| `known_sites` | `file` | (optional) known sites file(s) for calculating BQSR. markdups must be true to perform BQSR. |

### Outputs

| Name | Type | Pattern | Description |
|------|------|---------|-------------|
| `bam` | `file` | `*.bam` | Sorted BAM file |
| `bai` | `file` | `*.bai` | index corresponding to sorted BAM file |
| `cram` | `file` | `*.cram` | Sorted CRAM file |
| `crai` | `file` | `*.crai` | index corresponding to sorted CRAM file |
| `bqsr_table` | `file` | `*.table` | (optional) table from base quality score recalibration calculation, to be used with parabricks/applybqsr |
| `qc_metrics` | `directory` | `*_qc_metrics` | (optional) optional directory of qc metrics |
| `duplicate_metrics` | `file` | `*.duplicate-metrics.txt` | (optional) metrics calculated from marking duplicates in the bam file |
| `compatible_versions` | `-` | `-` | - |

**Authors:** [@bsiranosian](https://github.com/bsiranosian), [@adamrtalbot](https://github.com/adamrtalbot)
**Maintainers:** [@bsiranosian](https://github.com/bsiranosian), [@adamrtalbot](https://github.com/adamrtalbot), [@gallvp](https://github.com/gallvp), [@famosab](https://github.com/famosab)


## SVDB_MERGE {#svdb-merge}

*Defined in `modules/nf-core/svdb/merge/main.nf:1`*

**Keywords:** `structural variants`, `vcf`, `merge`

The merge module merges structural variants within one or more vcf files.

### Tools

#### [svdb](https://github.com/J35P312/SVDB)

structural variant database software

[Homepage](https://github.com/J35P312/SVDB) | [Documentation](https://github.com/J35P312/SVDB/blob/master/README.md) | License: MIT

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `vcfs` | `list` | One or more VCF files. The order and number of files should correspond to the order and number of tags in the `priority` input channel. |
| `input_priority` | `list` | Prioritize the input VCF files according to this list, e.g ['tiddit','cnvnator']. The order and number of tags should correspond to the order and number of VCFs in the `vcfs` input channel. |
| `sort_inputs` | `boolean` | Should the input files be sorted by name. The priority tag will be sorted together with it's corresponding VCF file. |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@ramprasadn](https://github.com/ramprasadn)
**Maintainers:** [@ramprasadn](https://github.com/ramprasadn), [@fellen31](https://github.com/fellen31)


## TIDDIT_SV {#tiddit-sv}

*Defined in `modules/nf-core/tiddit/sv/main.nf:1`*

**Keywords:** `structural`, `variants`, `vcf`

Identify chromosomal rearrangements.

### Tools

#### [sv](https://github.com/SciLifeLab/TIDDIT)

Search for structural variants.

[Homepage](https://github.com/SciLifeLab/TIDDIT) | [Documentation](https://github.com/SciLifeLab/TIDDIT/blob/master/README.md) | [biotools:tiddit](https://bio.tools/tiddit) | License: GPL-3.0-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `input` | `file` | BAM/CRAM file |
| `input_index` | `file` | BAM/CRAM index file |
| `meta2` | `map` | Groovy Map containing sample information e.g. `[ id:'test_fasta']` |
| `fasta` | `file` | Input FASTA file |
| `meta3` | `map` | Groovy Map containing sample information from bwa index e.g. `[ id:'test_bwa-index' ]` |
| `bwa_index` | `file` | BWA genome index files |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf")` | `tuple` | `vcf` | - |
| `val(meta), path("*.ploidies.tab")` | `tuple` | `ploidy` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@maxulysse](https://github.com/maxulysse)


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
| `tbi` | `file` | `*.{tbi}` | tabix index file |
| `csi` | `file` | `*.{csi}` | coordinate sorted index file |

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
| `gz_tbi` | `file` | `*.gz, *.tbi` | bgzipped tab-delimited genome file tabix index file |
| `gz_csi` | `file` | `*.gz, *.csi` | bgzipped tab-delimited genome file csi index file |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@DLBPointon](https://github.com/DLBPointon)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@DLBPointon](https://github.com/DLBPointon)


## CAT_CAT {#cat-cat}

*Defined in `modules/nf-core/cat/cat/main.nf:1`*

**Keywords:** `concatenate`, `gzip`, `cat`

A module for concatenation of gzipped or uncompressed files

### Tools

#### [cat](https://man7.org/linux/man-pages/man1/cat.1.html)

Just concatenation

[Documentation](https://man7.org/linux/man-pages/man1/cat.1.html) | License: GPL-3.0-or-later

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `meta` | `map` | Groovy Map containing sample information e.g. [ id:'test', single_end:false ] |
| `files_in` | `file` | List of compressed / uncompressed files |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |

**Authors:** [@erikrikarddaniel](https://github.com/erikrikarddaniel), [@FriederikeHanssen](https://github.com/FriederikeHanssen)
**Maintainers:** [@erikrikarddaniel](https://github.com/erikrikarddaniel), [@FriederikeHanssen](https://github.com/FriederikeHanssen)


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

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.merged.fastq.gz")` | `tuple` | `reads` | - |
| `versions.yml` | `path` | `versions` | - |

**Authors:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@joseespinosa](https://github.com/joseespinosa), [@drpatelh](https://github.com/drpatelh)


## CREATE_INTERVALS_BED {#create-intervals-bed}

*Defined in `modules/local/create_intervals_bed/main.nf:1`*

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `*.bed` | `path` | `bed` | - |
| `versions.yml` | `path` | `versions` | - |


## ADD_INFO_TO_VCF {#add-info-to-vcf}

*Defined in `modules/local/add_info_to_vcf/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf_gz)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.added_info.vcf")` | `tuple` | `vcf` | - |
| `versions.yml` | `path` | `versions` | - |


## SAMTOOLS_REINDEX_BAM {#samtools-reindex-bam}

*Defined in `modules/local/samtools/reindex_bam/main.nf:5`*

The aim of this process is to re-index the bam file without the duplicate, supplementary, unmapped etc, for goleft/indexcov
It creates a BAM containing only a header (so indexcov can get the sample name) and a BAM index were low quality reads, supplementary etc, have been removed

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


---

*This pipeline was built with [Nextflow](https://nextflow.io).
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:27:10 UTC.*
