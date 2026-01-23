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
| `versions.yml` | `path` | `versions` | - |


## VCFTOOLS {#vcftools}

*Defined in `modules/nf-core/vcftools/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(variant_file)` | `tuple` | - |

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


## UNZIP {#unzip}

*Defined in `modules/nf-core/unzip/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(archive)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## YTE {#yte}

*Defined in `modules/nf-core/yte/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(template), path(map_file), val(map)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.yaml")` | `tuple` | `rendered` | - |
| `versions.yml` | `path` | `versions` | - |


## GAWK {#gawk}

*Defined in `modules/nf-core/gawk/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input, arity: '0..*')` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## FASTQC {#fastqc}

*Defined in `modules/nf-core/fastqc/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.html")` | `tuple` | `html` | - |
| `val(meta), path("*.zip")` | `tuple` | `zip` | - |
| `versions.yml` | `path` | `versions` | - |


## ASCAT {#ascat}

*Defined in `modules/nf-core/ascat/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input_normal), path(index_normal), path(input_tumor), path(index_tumor)` | `tuple` | - |

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


## FREEBAYES {#freebayes}

*Defined in `modules/nf-core/freebayes/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input_1), path(input_1_index), path(input_2), path(input_2_index), path(target_bed)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fasta_fai)` | `tuple` | - |
| `val(meta4), path(samples)` | `tuple` | - |
| `val(meta5), path(populations)` | `tuple` | - |
| `val(meta6), path(cnv)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `versions.yml` | `path` | `versions` | - |


## FASTP {#fastp}

*Defined in `modules/nf-core/fastp/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |

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


## GUNZIP {#gunzip}

*Defined in `modules/nf-core/gunzip/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(archive)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## SPRING_DECOMPRESS {#spring-decompress}

*Defined in `modules/nf-core/spring/decompress/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(spring)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.fastq.gz")` | `tuple` | `fastq` | - |
| `versions.yml` | `path` | `versions` | - |


## LOFREQ_CALLPARALLEL {#lofreq-callparallel}

*Defined in `modules/nf-core/lofreq/callparallel/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_INTERVALLISTTOBED {#gatk4-intervallisttobed}

*Defined in `modules/nf-core/gatk4/intervallisttobed/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(intervals)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## GATK4_CALCULATECONTAMINATION {#gatk4-calculatecontamination}

*Defined in `modules/nf-core/gatk4/calculatecontamination/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(pileup), path(matched)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.contamination.table')` | `tuple` | `contamination` | - |
| `val(meta), path('*.segmentation.table')` | `tuple` | `segmentation` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_FILTERMUTECTCALLS {#gatk4-filtermutectcalls}

*Defined in `modules/nf-core/gatk4/filtermutectcalls/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(vcf_tbi), path(stats), path(orientationbias), path(segmentation), path(table), val(estimate)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dict)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*.filteringStats.tsv")` | `tuple` | `stats` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_APPLYVQSR {#gatk4-applyvqsr}

*Defined in `modules/nf-core/gatk4/applyvqsr/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(vcf_tbi), path(recal), path(recal_index), path(tranches)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_GENOMICSDBIMPORT {#gatk4-genomicsdbimport}

*Defined in `modules/nf-core/gatk4/genomicsdbimport/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi), path(interval_file), val(interval_value), path(wspace)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## GATK4_LEARNREADORIENTATIONMODEL {#gatk4-learnreadorientationmodel}

*Defined in `modules/nf-core/gatk4/learnreadorientationmodel/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(f1r2)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.tar.gz")` | `tuple` | `artifactprior` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_VARIANTRECALIBRATOR {#gatk4-variantrecalibrator}

*Defined in `modules/nf-core/gatk4/variantrecalibrator/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.recal")` | `tuple` | `recal` | - |
| `val(meta), path("*.idx")` | `tuple` | `idx` | - |
| `val(meta), path("*.tranches")` | `tuple` | `tranches` | - |
| `val(meta), path("*plots.R")` | `tuple` | `plots` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_GATHERBQSRREPORTS {#gatk4-gatherbqsrreports}

*Defined in `modules/nf-core/gatk4/gatherbqsrreports/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(table)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.table")` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_GETPILEUPSUMMARIES {#gatk4-getpileupsummaries}

*Defined in `modules/nf-core/gatk4/getpileupsummaries/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(index), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dict)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.pileups.table')` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_GENOTYPEGVCFS {#gatk4-genotypegvcfs}

*Defined in `modules/nf-core/gatk4/genotypegvcfs/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(gvcf_index), path(intervals), path(intervals_index)` | `tuple` | - |
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


## GATK4_GATHERPILEUPSUMMARIES {#gatk4-gatherpileupsummaries}

*Defined in `modules/nf-core/gatk4/gatherpileupsummaries/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(pileup)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.pileups.table")` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_ESTIMATELIBRARYCOMPLEXITY {#gatk4-estimatelibrarycomplexity}

*Defined in `modules/nf-core/gatk4/estimatelibrarycomplexity/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path('*.metrics')` | `tuple` | `metrics` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_HAPLOTYPECALLER {#gatk4-haplotypecaller}

*Defined in `modules/nf-core/gatk4/haplotypecaller/main.nf:1`*

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


## GATK4_CNNSCOREVARIANTS {#gatk4-cnnscorevariants}

*Defined in `modules/nf-core/gatk4/cnnscorevariants/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi), path(aligned_input), path(intervals)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*cnn.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*cnn.vcf.gz.tbi")` | `tuple` | `tbi` | - |
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


## GATK4_FILTERVARIANTTRANCHES {#gatk4-filtervarianttranches}

*Defined in `modules/nf-core/gatk4/filtervarianttranches/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi), path(intervals)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_MARKDUPLICATES {#gatk4-markduplicates}

*Defined in `modules/nf-core/gatk4/markduplicates/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*cram")` | `tuple` | `cram` | - |
| `val(meta), path("*bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.metrics")` | `tuple` | `metrics` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_MUTECT2 {#gatk4-mutect2}

*Defined in `modules/nf-core/gatk4/mutect2/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dict)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*.stats")` | `tuple` | `stats` | - |
| `val(meta), path("*.f1r2.tar.gz")` | `tuple` | `f1r2` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4_MERGEMUTECTSTATS {#gatk4-mergemutectstats}

*Defined in `modules/nf-core/gatk4/mergemutectstats/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(stats)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz.stats")` | `tuple` | `stats` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4SPARK_BASERECALIBRATOR {#gatk4spark-baserecalibrator}

*Defined in `modules/nf-core/gatk4spark/baserecalibrator/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(intervals)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.table")` | `tuple` | `table` | - |
| `versions.yml` | `path` | `versions` | - |


## GATK4SPARK_APPLYBQSR {#gatk4spark-applybqsr}

*Defined in `modules/nf-core/gatk4spark/applybqsr/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(bqsr_table), path(intervals)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## GATK4SPARK_MARKDUPLICATES {#gatk4spark-markduplicates}

*Defined in `modules/nf-core/gatk4spark/markduplicates/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## DEEPVARIANT_RUNDEEPVARIANT {#deepvariant-rundeepvariant}

*Defined in `modules/nf-core/deepvariant/rundeepvariant/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(index), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(gzi)` | `tuple` | - |
| `val(meta5), path(par_bed)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## SENTIEON_GVCFTYPER {#sentieon-gvcftyper}

*Defined in `modules/nf-core/sentieon/gvcftyper/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(gvcfs), path(tbis), path(intervals)` | `tuple` | - |
| `val(meta1), path(fasta)` | `tuple` | - |
| `val(meta2), path(fai)` | `tuple` | - |
| `val(meta3), path(dbsnp)` | `tuple` | - |
| `val(meta4), path(dbsnp_tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf_gz` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `vcf_gz_tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## SENTIEON_TNSCOPE {#sentieon-tnscope}

*Defined in `modules/nf-core/sentieon/tnscope/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dbsnp)` | `tuple` | - |
| `val(meta5), path(dbsnp_tbi)` | `tuple` | - |
| `val(meta6), path(pon)` | `tuple` | - |
| `val(meta7), path(pon_tbi)` | `tuple` | - |
| `val(meta8), path(cosmic)` | `tuple` | - |
| `val(meta9), path(cosmic_tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `index` | - |
| `versions.yml` | `path` | `versions` | - |


## SENTIEON_DNAMODELAPPLY {#sentieon-dnamodelapply}

*Defined in `modules/nf-core/sentieon/dnamodelapply/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(idx)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(ml_model)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## SENTIEON_BWAMEM {#sentieon-bwamem}

*Defined in `modules/nf-core/sentieon/bwamem/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |
| `val(meta2), path(index)` | `tuple` | - |
| `val(meta3), path(fasta)` | `tuple` | - |
| `val(meta4), path(fasta_fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## SENTIEON_APPLYVARCAL {#sentieon-applyvarcal}

*Defined in `modules/nf-core/sentieon/applyvarcal/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(vcf_tbi), path(recal), path(recal_index), path(tranches)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## SENTIEON_VARCAL {#sentieon-varcal}

*Defined in `modules/nf-core/sentieon/varcal/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.recal")` | `tuple` | `recal` | - |
| `val(meta), path("*.idx")` | `tuple` | `idx` | - |
| `val(meta), path("*.tranches")` | `tuple` | `tranches` | - |
| `val(meta), path("*plots.R")` | `tuple` | `plots` | - |
| `versions.yml` | `path` | `versions` | - |


## SENTIEON_DNASCOPE {#sentieon-dnascope}

*Defined in `modules/nf-core/sentieon/dnascope/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dbsnp)` | `tuple` | - |
| `val(meta5), path(dbsnp_tbi)` | `tuple` | - |
| `val(meta6), path(ml_model)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.unfiltered.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.unfiltered.vcf.gz.tbi")` | `tuple` | `vcf_tbi` | - |
| `val(meta), path("*.g.vcf.gz")` | `tuple` | `gvcf` | - |
| `val(meta), path("*.g.vcf.gz.tbi")` | `tuple` | `gvcf_tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## SENTIEON_HAPLOTYPER {#sentieon-haplotyper}

*Defined in `modules/nf-core/sentieon/haplotyper/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(intervals), path(recal_table)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(dbsnp)` | `tuple` | - |
| `val(meta5), path(dbsnp_tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.unfiltered.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.unfiltered.vcf.gz.tbi")` | `tuple` | `vcf_tbi` | - |
| `val(meta), path("*.g.vcf.gz")` | `tuple` | `gvcf` | - |
| `val(meta), path("*.g.vcf.gz.tbi")` | `tuple` | `gvcf_tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## SENTIEON_DEDUP {#sentieon-dedup}

*Defined in `modules/nf-core/sentieon/dedup/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fasta_fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.score")` | `tuple` | `score` | - |
| `val(meta), path("*.metrics")` | `tuple` | `metrics` | - |
| `val(meta), path("*.metrics.multiqc.tsv")` | `tuple` | `metrics_multiqc_tsv` | - |
| `versions.yml` | `path` | `versions` | - |


## SAMTOOLS_BAM2FQ {#samtools-bam2fq}

*Defined in `modules/nf-core/samtools/bam2fq/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(inputbam)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.fq.gz")` | `tuple` | `reads` | - |
| `versions.yml` | `path` | `versions` | - |


## SAMTOOLS_MERGE {#samtools-merge}

*Defined in `modules/nf-core/samtools/merge/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input_files, stageAs: "?/*")` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## SAMTOOLS_MPILEUP {#samtools-mpileup}

*Defined in `modules/nf-core/samtools/mpileup/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.mpileup.gz")` | `tuple` | `mpileup` | - |
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


## SAMTOOLS_VIEW {#samtools-view}

*Defined in `modules/nf-core/samtools/view/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(index)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

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


## SAMTOOLS_COLLATEFASTQ {#samtools-collatefastq}

*Defined in `modules/nf-core/samtools/collatefastq/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


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
| `versions.yml` | `path` | `versions` | - |


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


## VCFLIB_VCFFILTER {#vcflib-vcffilter}

*Defined in `modules/nf-core/vcflib/vcffilter/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `versions.yml` | `path` | `versions` | - |


## BBMAP_BBSPLIT {#bbmap-bbsplit}

*Defined in `modules/nf-core/bbmap/bbsplit/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |
| `val(other_ref_names), path(other_ref_paths)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `bbsplit_index` | `path` | `index` | - |
| `val(meta), path('*primary*fastq.gz')` | `tuple` | `primary_fastq` | - |
| `val(meta), path('*fastq.gz')` | `tuple` | `all_fastq` | - |
| `val(meta), path('*txt')` | `tuple` | `stats` | - |
| `val(meta), path('*.log')` | `tuple` | `log` | - |
| `versions.yml` | `path` | `versions` | - |


## MSISENSOR2_MSI {#msisensor2-msi}

*Defined in `modules/nf-core/msisensor2/msi/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(tumor_bam), path(tumor_bam_index)` | `tuple` | - |
| `val(meta2), path(models)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## CONTROLFREEC_FREEC2BED {#controlfreec-freec2bed}

*Defined in `modules/nf-core/controlfreec/freec2bed/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(ratio)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bed")` | `tuple` | `bed` | - |
| `versions.yml` | `path` | `versions` | - |


## CONTROLFREEC_MAKEGRAPH2 {#controlfreec-makegraph2}

*Defined in `modules/nf-core/controlfreec/makegraph2/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(ratio), path(baf)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*_BAF.png")` | `tuple` | `png_baf` | - |
| `val(meta), path("*_ratio.log2.png")` | `tuple` | `png_ratio_log2` | - |
| `val(meta), path("*_ratio.png")` | `tuple` | `png_ratio` | - |
| `versions.yml` | `path` | `versions` | - |


## CONTROLFREEC_FREEC2CIRCOS {#controlfreec-freec2circos}

*Defined in `modules/nf-core/controlfreec/freec2circos/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(ratio)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.circos.txt")` | `tuple` | `circos` | - |
| `versions.yml` | `path` | `versions` | - |


## CONTROLFREEC_FREEC {#controlfreec-freec}

*Defined in `modules/nf-core/controlfreec/freec/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(mpileup_normal), path(mpileup_tumor), path(cpn_normal), path(cpn_tumor), path(minipileup_normal), path(minipileup_tumor)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*_ratio.BedGraph")` | `tuple` | `bedgraph` | - |
| `val(meta), path("*_control.cpn")` | `tuple` | `control_cpn` | - |
| `val(meta), path("*_sample.cpn")` | `tuple` | `sample_cpn` | - |
| `val(meta), path("GC_profile.*.cpn")` | `tuple` | `gcprofile_cpn` | - |
| `val(meta), path("*_BAF.txt")` | `tuple` | `BAF` | - |
| `val(meta), path("*_CNVs")` | `tuple` | `CNV` | - |
| `val(meta), path("*_info.txt")` | `tuple` | `info` | - |
| `val(meta), path("*_ratio.txt")` | `tuple` | `ratio` | - |
| `val(meta), path("config.txt")` | `tuple` | `config` | - |
| `versions.yml` | `path` | `versions` | - |


## CONTROLFREEC_ASSESSSIGNIFICANCE {#controlfreec-assesssignificance}

*Defined in `modules/nf-core/controlfreec/assesssignificance/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(cnvs), path(ratio)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.p.value.txt")` | `tuple` | `p_value_txt` | - |
| `versions.yml` | `path` | `versions` | - |


## GOLEFT_INDEXCOV {#goleft-indexcov}

*Defined in `modules/nf-core/goleft/indexcov/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bams), path(indexes)` | `tuple` | - |
| `val(meta2), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## DRAGMAP_ALIGN {#dragmap-align}

*Defined in `modules/nf-core/dragmap/align/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |
| `val(meta2), path(hashmap)` | `tuple` | - |
| `val(meta3), path(fasta)` | `tuple` | - |

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


## DRAGMAP_HASHTABLE {#dragmap-hashtable}

*Defined in `modules/nf-core/dragmap/hashtable/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("dragmap")` | `tuple` | `hashmap` | - |
| `versions.yml` | `path` | `versions` | - |


## STRELKA_GERMLINE {#strelka-germline}

*Defined in `modules/nf-core/strelka/germline/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(target_bed), path(target_bed_index)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*variants.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*variants.vcf.gz.tbi")` | `tuple` | `vcf_tbi` | - |
| `val(meta), path("*genome.vcf.gz")` | `tuple` | `genome_vcf` | - |
| `val(meta), path("*genome.vcf.gz.tbi")` | `tuple` | `genome_vcf_tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## STRELKA_SOMATIC {#strelka-somatic}

*Defined in `modules/nf-core/strelka/somatic/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input_normal), path(input_index_normal), path(input_tumor), path(input_index_tumor), path(manta_candidate_small_indels), path(manta_candidate_small_indels_tbi), path(target_bed), path(target_bed_index)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.somatic_indels.vcf.gz")` | `tuple` | `vcf_indels` | - |
| `val(meta), path("*.somatic_indels.vcf.gz.tbi")` | `tuple` | `vcf_indels_tbi` | - |
| `val(meta), path("*.somatic_snvs.vcf.gz")` | `tuple` | `vcf_snvs` | - |
| `val(meta), path("*.somatic_snvs.vcf.gz.tbi")` | `tuple` | `vcf_snvs_tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## BWA_INDEX {#bwa-index}

*Defined in `modules/nf-core/bwa/index/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("bwa")` | `tuple` | `index` | - |
| `versions.yml` | `path` | `versions` | - |


## BWA_MEM {#bwa-mem}

*Defined in `modules/nf-core/bwa/mem/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |
| `val(meta2), path(index)` | `tuple` | - |
| `val(meta3), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.csi")` | `tuple` | `csi` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
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
| `val(meta), path("*.csv")` | `tuple` | `report` | - |
| `val(meta), path("*.html")` | `tuple` | `summary_html` | - |
| `val(meta), path("*.genes.txt")` | `tuple` | `genes_txt` | - |
| `versions.yml` | `path` | `versions` | - |


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
| `versions.yml` | `path` | `versions` | - |


## NGSCHECKMATE_NCM {#ngscheckmate-ncm}

*Defined in `modules/nf-core/ngscheckmate/ncm/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(files)` | `tuple` | - |
| `val(meta2), path(snp_bed)` | `tuple` | - |
| `val(meta3), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*_corr_matrix.txt")` | `tuple` | `corr_matrix` | - |
| `val(meta), path("*_matched.txt")` | `tuple` | `matched` | - |
| `val(meta), path("*_all.txt")` | `tuple` | `all` | - |
| `val(meta), path("*.pdf")` | `tuple` | `pdf` | - |
| `val(meta), path("*.vcf")` | `tuple` | `vcf` | - |
| `versions.yml` | `path` | `versions` | - |


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
| `*.html` | `path` | `report` | - |
| `versions.yml` | `path` | `versions` | - |


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
| `versions.yml` | `path` | `versions` | - |


## VARLOCIRAPTOR_CALLVARIANTS {#varlociraptor-callvariants}

*Defined in `modules/nf-core/varlociraptor/callvariants/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcfs)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bcf")` | `tuple` | `bcf` | - |
| `versions.yml` | `path` | `versions` | - |


## VARLOCIRAPTOR_PREPROCESS {#varlociraptor-preprocess}

*Defined in `modules/nf-core/varlociraptor/preprocess/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai), path(candidates), path(alignment_json)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bcf")` | `tuple` | `bcf` | - |
| `versions.yml` | `path` | `versions` | - |


## VARLOCIRAPTOR_ESTIMATEALIGNMENTPROPERTIES {#varlociraptor-estimatealignmentproperties}

*Defined in `modules/nf-core/varlociraptor/estimatealignmentproperties/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.alignment-properties.json")` | `tuple` | `alignment_properties_json` | - |
| `versions.yml` | `path` | `versions` | - |


## CNVKIT_GENEMETRICS {#cnvkit-genemetrics}

*Defined in `modules/nf-core/cnvkit/genemetrics/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(cnr), path(cns)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.tsv")` | `tuple` | `tsv` | - |
| `versions.yml` | `path` | `versions` | - |


## CNVKIT_CALL {#cnvkit-call}

*Defined in `modules/nf-core/cnvkit/call/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(cns), path(vcf)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.cns")` | `tuple` | `cns` | - |
| `versions.yml` | `path` | `versions` | - |


## CNVKIT_BATCH {#cnvkit-batch}

*Defined in `modules/nf-core/cnvkit/batch/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(tumor), path(normal)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fasta_fai)` | `tuple` | - |
| `val(meta4), path(targets)` | `tuple` | - |
| `val(meta5), path(reference)` | `tuple` | - |

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


## CNVKIT_ANTITARGET {#cnvkit-antitarget}

*Defined in `modules/nf-core/cnvkit/antitarget/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(targets)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bed")` | `tuple` | `bed` | - |
| `versions.yml` | `path` | `versions` | - |


## CNVKIT_EXPORT {#cnvkit-export}

*Defined in `modules/nf-core/cnvkit/export/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(cns)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## CNVKIT_REFERENCE {#cnvkit-reference}

*Defined in `modules/nf-core/cnvkit/reference/main.nf:1`*

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `*.cnn` | `path` | `cnn` | - |
| `versions.yml` | `path` | `versions` | - |


## RBT_VCFSPLIT {#rbt-vcfsplit}

*Defined in `modules/nf-core/rbt/vcfsplit/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bcf")` | `tuple` | `bcfchunks` | - |
| `versions.yml` | `path` | `versions` | - |


## FGBIO_FASTQTOBAM {#fgbio-fastqtobam}

*Defined in `modules/nf-core/fgbio/fastqtobam/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `versions.yml` | `path` | `versions` | - |


## FGBIO_COPYUMIFROMREADNAME {#fgbio-copyumifromreadname}

*Defined in `modules/nf-core/fgbio/copyumifromreadname/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(bai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `versions.yml` | `path` | `versions` | - |


## FGBIO_CALLMOLECULARCONSENSUSREADS {#fgbio-callmolecularconsensusreads}

*Defined in `modules/nf-core/fgbio/callmolecularconsensusreads/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(grouped_bam)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `versions.yml` | `path` | `versions` | - |


## FGBIO_GROUPREADSBYUMI {#fgbio-groupreadsbyumi}

*Defined in `modules/nf-core/fgbio/groupreadsbyumi/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*histogram.txt")` | `tuple` | `histogram` | - |
| `versions.yml` | `path` | `versions` | - |


## BWAMEM2_INDEX {#bwamem2-index}

*Defined in `modules/nf-core/bwamem2/index/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("bwamem2")` | `tuple` | `index` | - |
| `versions.yml` | `path` | `versions` | - |


## BWAMEM2_MEM {#bwamem2-mem}

*Defined in `modules/nf-core/bwamem2/mem/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |
| `val(meta2), path(index)` | `tuple` | - |
| `val(meta3), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.sam")` | `tuple` | `sam` | - |
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `val(meta), path("*.csi")` | `tuple` | `csi` | - |
| `versions.yml` | `path` | `versions` | - |


## MANTA_TUMORONLY {#manta-tumoronly}

*Defined in `modules/nf-core/manta/tumoronly/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index), path(target_bed), path(target_bed_tbi)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*candidate_small_indels.vcf.gz")` | `tuple` | `candidate_small_indels_vcf` | - |
| `val(meta), path("*candidate_small_indels.vcf.gz.tbi")` | `tuple` | `candidate_small_indels_vcf_tbi` | - |
| `val(meta), path("*candidate_sv.vcf.gz")` | `tuple` | `candidate_sv_vcf` | - |
| `val(meta), path("*candidate_sv.vcf.gz.tbi")` | `tuple` | `candidate_sv_vcf_tbi` | - |
| `val(meta), path("*tumor_sv.vcf.gz")` | `tuple` | `tumor_sv_vcf` | - |
| `val(meta), path("*tumor_sv.vcf.gz.tbi")` | `tuple` | `tumor_sv_vcf_tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## MANTA_GERMLINE {#manta-germline}

*Defined in `modules/nf-core/manta/germline/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(index), path(target_bed), path(target_bed_tbi)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*candidate_small_indels.vcf.gz")` | `tuple` | `candidate_small_indels_vcf` | - |
| `val(meta), path("*candidate_small_indels.vcf.gz.tbi")` | `tuple` | `candidate_small_indels_vcf_tbi` | - |
| `val(meta), path("*candidate_sv.vcf.gz")` | `tuple` | `candidate_sv_vcf` | - |
| `val(meta), path("*candidate_sv.vcf.gz.tbi")` | `tuple` | `candidate_sv_vcf_tbi` | - |
| `val(meta), path("*diploid_sv.vcf.gz")` | `tuple` | `diploid_sv_vcf` | - |
| `val(meta), path("*diploid_sv.vcf.gz.tbi")` | `tuple` | `diploid_sv_vcf_tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## MANTA_SOMATIC {#manta-somatic}

*Defined in `modules/nf-core/manta/somatic/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input_normal), path(input_index_normal), path(input_tumor), path(input_index_tumor), path(target_bed), path(target_bed_tbi)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.candidate_small_indels.vcf.gz")` | `tuple` | `candidate_small_indels_vcf` | - |
| `val(meta), path("*.candidate_small_indels.vcf.gz.tbi")` | `tuple` | `candidate_small_indels_vcf_tbi` | - |
| `val(meta), path("*.candidate_sv.vcf.gz")` | `tuple` | `candidate_sv_vcf` | - |
| `val(meta), path("*.candidate_sv.vcf.gz.tbi")` | `tuple` | `candidate_sv_vcf_tbi` | - |
| `val(meta), path("*.diploid_sv.vcf.gz")` | `tuple` | `diploid_sv_vcf` | - |
| `val(meta), path("*.diploid_sv.vcf.gz.tbi")` | `tuple` | `diploid_sv_vcf_tbi` | - |
| `val(meta), path("*.somatic_sv.vcf.gz")` | `tuple` | `somatic_sv_vcf` | - |
| `val(meta), path("*.somatic_sv.vcf.gz.tbi")` | `tuple` | `somatic_sv_vcf_tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## BCFTOOLS_CONCAT {#bcftools-concat}

*Defined in `modules/nf-core/bcftools/concat/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcfs), path(tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## BCFTOOLS_SORT {#bcftools-sort}

*Defined in `modules/nf-core/bcftools/sort/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## BCFTOOLS_MERGE {#bcftools-merge}

*Defined in `modules/nf-core/bcftools/merge/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcfs), path(tbis)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(fai)` | `tuple` | - |
| `val(meta4), path(bed)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## BCFTOOLS_MPILEUP {#bcftools-mpileup}

*Defined in `modules/nf-core/bcftools/mpileup/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(bam), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*stats.txt")` | `tuple` | `stats` | - |
| `val(meta), path("*.mpileup.gz")` | `tuple` | `mpileup` | - |
| `versions.yml` | `path` | `versions` | - |


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


## BCFTOOLS_NORM {#bcftools-norm}

*Defined in `modules/nf-core/bcftools/norm/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## BCFTOOLS_VIEW {#bcftools-view}

*Defined in `modules/nf-core/bcftools/view/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(index)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## BCFTOOLS_STATS {#bcftools-stats}

*Defined in `modules/nf-core/bcftools/stats/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcf), path(tbi)` | `tuple` | - |
| `val(meta2), path(regions)` | `tuple` | - |
| `val(meta3), path(targets)` | `tuple` | - |
| `val(meta4), path(samples)` | `tuple` | - |
| `val(meta5), path(exons)` | `tuple` | - |
| `val(meta6), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*stats.txt")` | `tuple` | `stats` | - |
| `versions.yml` | `path` | `versions` | - |


## BCFTOOLS_ISEC {#bcftools-isec}

*Defined in `modules/nf-core/bcftools/isec/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcfs), path(tbis)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## MSISENSORPRO_SCAN {#msisensorpro-scan}

*Defined in `modules/nf-core/msisensorpro/scan/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.list")` | `tuple` | `list` | - |
| `versions.yml` | `path` | `versions` | - |


## MSISENSORPRO_MSISOMATIC {#msisensorpro-msisomatic}

*Defined in `modules/nf-core/msisensorpro/msisomatic/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(normal), path(normal_index), path(tumor), path(tumor_index), path(intervals)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## MUSE_SUMP {#muse-sump}

*Defined in `modules/nf-core/muse/sump/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(muse_call_txt)` | `tuple` | - |
| `val(meta2), path(ref_vcf), path(ref_vcf_tbi)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf.gz")` | `tuple` | `vcf` | - |
| `val(meta), path("*.vcf.gz.tbi")` | `tuple` | `tbi` | - |
| `versions.yml` | `path` | `versions` | - |


## MUSE_CALL {#muse-call}

*Defined in `modules/nf-core/muse/call/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(tumor_bam), path(tumor_bai), path(normal_bam), path(normal_bai)` | `tuple` | - |
| `val(meta2), path(reference)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.MuSE.txt")` | `tuple` | `txt` | - |
| `versions.yml` | `path` | `versions` | - |


## PARABRICKS_FQ2BAM {#parabricks-fq2bam}

*Defined in `modules/nf-core/parabricks/fq2bam/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(reads)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(index)` | `tuple` | - |
| `val(meta4), path(interval_file)` | `tuple` | - |
| `val(meta5), path(known_sites)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.bam")` | `tuple` | `bam` | - |
| `val(meta), path("*.bai")` | `tuple` | `bai` | - |
| `val(meta), path("*.cram")` | `tuple` | `cram` | - |
| `val(meta), path("*.crai")` | `tuple` | `crai` | - |
| `val(meta), path("*.table")` | `tuple` | `bqsr_table` | - |
| `val(meta), path("*_qc_metrics")` | `tuple` | `qc_metrics` | - |
| `val(meta), path("*.duplicate-metrics.txt")` | `tuple` | `duplicate_metrics` | - |
| `compatible_versions.yml` | `path` | `compatible_versions` | - |
| `versions.yml` | `path` | `versions` | - |


## SVDB_MERGE {#svdb-merge}

*Defined in `modules/nf-core/svdb/merge/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(vcfs)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


## TIDDIT_SV {#tiddit-sv}

*Defined in `modules/nf-core/tiddit/sv/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input), path(input_index)` | `tuple` | - |
| `val(meta2), path(fasta)` | `tuple` | - |
| `val(meta3), path(bwa_index)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.vcf")` | `tuple` | `vcf` | - |
| `val(meta), path("*.ploidies.tab")` | `tuple` | `ploidy` | - |
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
| `val(meta), path("*.tbi")` | `tuple` | `tbi` | - |
| `val(meta), path("*.csi")` | `tuple` | `csi` | - |
| `versions.yml` | `path` | `versions` | - |


## TABIX_BGZIPTABIX {#tabix-bgziptabix}

*Defined in `modules/nf-core/tabix/bgziptabix/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(input)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta), path("*.gz"), path("*.tbi")` | `tuple` | `gz_tbi` | - |
| `val(meta), path("*.gz"), path("*.csi")` | `tuple` | `gz_csi` | - |
| `versions.yml` | `path` | `versions` | - |


## CAT_CAT {#cat-cat}

*Defined in `modules/nf-core/cat/cat/main.nf:1`*

### Inputs

| Name | Type | Description |
|------|------|-------------|
| `val(meta), path(files_in)` | `tuple` | - |

### Outputs

| Name | Type | Emit | Description |
|------|------|------|-------------|
| `val(meta)` | `tuple` | - | - |


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
| `versions.yml` | `path` | `versions` | - |


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
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:02:59 UTC.*
