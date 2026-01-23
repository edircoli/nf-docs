# Workflows

This page documents all workflows in the pipeline.

## Contents

- [NFCORE_SAREK](#nfcore-sarek)
- [(entry)](#entry) *(entry point)*
- [SAREK](#sarek)
- [BAM_NGSCHECKMATE](#bam-ngscheckmate)
- [UTILS_NFCORE_PIPELINE](#utils-nfcore-pipeline)
- [UTILS_NEXTFLOW_PIPELINE](#utils-nextflow-pipeline)
- [VCF_ANNOTATE_SNPEFF](#vcf-annotate-snpeff)
- [UTILS_NFSCHEMA_PLUGIN](#utils-nfschema-plugin)
- [VCF_ANNOTATE_ENSEMBLVEP](#vcf-annotate-ensemblvep)
- [BAM_VARIANT_CALLING_SOMATIC_MUTECT2](#bam-variant-calling-somatic-mutect2)
- [SAMPLESHEET_TO_CHANNEL](#samplesheet-to-channel)
- [CHANNEL_VARIANT_CALLING_CREATE_CSV](#channel-variant-calling-create-csv)
- [BAM_VARIANT_CALLING_TUMOR_ONLY_LOFREQ](#bam-variant-calling-tumor-only-lofreq)
- [BAM_VARIANT_CALLING_TUMOR_ONLY_MUTECT2](#bam-variant-calling-tumor-only-mutect2)
- [BAM_JOINT_CALLING_GERMLINE_SENTIEON](#bam-joint-calling-germline-sentieon)
- [VCF_QC_BCFTOOLS_VCFTOOLS](#vcf-qc-bcftools-vcftools)
- [BAM_VARIANT_CALLING_SENTIEON_DNASCOPE](#bam-variant-calling-sentieon-dnascope)
- [BAM_VARIANT_CALLING_SOMATIC_MUSE](#bam-variant-calling-somatic-muse)
- [BAM_VARIANT_CALLING_FREEBAYES](#bam-variant-calling-freebayes)
- [CHANNEL_BASERECALIBRATOR_CREATE_CSV](#channel-baserecalibrator-create-csv)
- [BAM_VARIANT_CALLING_SOMATIC_MANTA](#bam-variant-calling-somatic-manta)
- [BAM_VARIANT_CALLING_TUMOR_ONLY_ALL](#bam-variant-calling-tumor-only-all)
- [PREPARE_REFERENCE_CNVKIT](#prepare-reference-cnvkit)
- [CONCATENATE_GERMLINE_VCFS](#concatenate-germline-vcfs)
- [BAM_VARIANT_CALLING_TUMOR_ONLY_CONTROLFREEC](#bam-variant-calling-tumor-only-controlfreec)
- [BAM_VARIANT_CALLING_TUMOR_ONLY_MANTA](#bam-variant-calling-tumor-only-manta)
- [BAM_VARIANT_CALLING_SOMATIC_ALL](#bam-variant-calling-somatic-all)
- [BAM_MARKDUPLICATES_SPARK](#bam-markduplicates-spark)
- [BAM_APPLYBQSR_SPARK](#bam-applybqsr-spark)
- [BAM_VARIANT_CALLING_SOMATIC_STRELKA](#bam-variant-calling-somatic-strelka)
- [CHANNEL_MARKDUPLICATES_CREATE_CSV](#channel-markduplicates-create-csv)
- [BAM_VARIANT_CALLING_DEEPVARIANT](#bam-variant-calling-deepvariant)
- [VCF_VARLOCIRAPTOR_SINGLE](#vcf-varlociraptor-single)
- [CRAM_QC_MOSDEPTH_SAMTOOLS](#cram-qc-mosdepth-samtools)
- [DOWNLOAD_CACHE_SNPEFF_VEP](#download-cache-snpeff-vep)
- [FASTQ_PREPROCESS_GATK](#fastq-preprocess-gatk)
- [BAM_MERGE_INDEX_SAMTOOLS](#bam-merge-index-samtools)
- [FASTQ_PREPROCESS_PARABRICKS](#fastq-preprocess-parabricks)
- [VCF_VARIANT_FILTERING_GATK](#vcf-variant-filtering-gatk)
- [BAM_CONVERT_SAMTOOLS](#bam-convert-samtools)
- [BAM_SENTIEON_DEDUP](#bam-sentieon-dedup)
- [BAM_VARIANT_CALLING_SOMATIC_TIDDIT](#bam-variant-calling-somatic-tiddit)
- [CHANNEL_ALIGN_CREATE_CSV](#channel-align-create-csv)
- [BAM_MARKDUPLICATES](#bam-markduplicates)
- [CRAM_MERGE_INDEX_SAMTOOLS](#cram-merge-index-samtools)
- [ANNOTATION_CACHE_INITIALISATION](#annotation-cache-initialisation)
- [BAM_VARIANT_CALLING_SENTIEON_HAPLOTYPER](#bam-variant-calling-sentieon-haplotyper)
- [BAM_VARIANT_CALLING_SINGLE_TIDDIT](#bam-variant-calling-single-tiddit)
- [BAM_VARIANT_CALLING_CNVKIT](#bam-variant-calling-cnvkit)
- [CRAM_SAMPLEQC](#cram-sampleqc)
- [CONSENSUS](#consensus)
- [BAM_VARIANT_CALLING_INDEXCOV](#bam-variant-calling-indexcov)
- [FASTQ_CREATE_UMI_CONSENSUS_FGBIO](#fastq-create-umi-consensus-fgbio)
- [BAM_VARIANT_CALLING_MPILEUP](#bam-variant-calling-mpileup)
- [BAM_VARIANT_CALLING_SINGLE_STRELKA](#bam-variant-calling-single-strelka)
- [POST_VARIANTCALLING](#post-variantcalling)
- [VCF_VARLOCIRAPTOR_SOMATIC](#vcf-varlociraptor-somatic)
- [BAM_VARIANT_CALLING_GERMLINE_MANTA](#bam-variant-calling-germline-manta)
- [BAM_APPLYBQSR](#bam-applybqsr)
- [BAM_VARIANT_CALLING_SOMATIC_TNSCOPE](#bam-variant-calling-somatic-tnscope)
- [NORMALIZE_VCFS](#normalize-vcfs)
- [BAM_VARIANT_CALLING_TUMOR_ONLY_TNSCOPE](#bam-variant-calling-tumor-only-tnscope)
- [BAM_VARIANT_CALLING_HAPLOTYPECALLER](#bam-variant-calling-haplotypecaller)
- [PIPELINE_INITIALISATION](#pipeline-initialisation)
- [PIPELINE_COMPLETION](#pipeline-completion)
- [PREPARE_GENOME](#prepare-genome)
- [BAM_VARIANT_CALLING_SOMATIC_CONTROLFREEC](#bam-variant-calling-somatic-controlfreec)
- [BAM_BASERECALIBRATOR_SPARK](#bam-baserecalibrator-spark)
- [BAM_BASERECALIBRATOR](#bam-baserecalibrator)
- [BAM_JOINT_CALLING_GERMLINE_GATK](#bam-joint-calling-germline-gatk)
- [CHANNEL_APPLYBQSR_CREATE_CSV](#channel-applybqsr-create-csv)
- [FASTQ_ALIGN](#fastq-align)
- [BAM_VARIANT_CALLING_GERMLINE_ALL](#bam-variant-calling-germline-all)
- [VCF_ANNOTATE_ALL](#vcf-annotate-all)
- [BAM_VARIANT_CALLING_SOMATIC_ASCAT](#bam-variant-calling-somatic-ascat)

## NFCORE_SAREK {#nfcore-sarek}

*Defined in `main.nf:86`*

### Inputs

| Name | Description |
|------|-------------|
| `samplesheet` | - |

### Outputs

| Name | Description |
|------|-------------|
| `multiqc_report` | - |


## (entry) {#entry}

**Entry workflow**

*Defined in `main.nf:298`*


## SAREK {#sarek}

*Defined in `workflows/sarek/main.nf:63`*

### Inputs

| Name | Description |
|------|-------------|
| `input_sample` | - |
| `aligner` | - |
| `skip_tools` | - |
| `step` | - |
| `tools` | - |
| `ascat_alleles` | - |
| `ascat_loci` | - |
| `ascat_loci_gc` | - |
| `ascat_loci_rt` | - |
| `bbsplit_index` | - |
| `bcftools_annotations` | - |
| `bcftools_annotations_tbi` | - |
| `bcftools_columns` | - |
| `bcftools_header_lines` | - |
| `cf_chrom_len` | - |
| `chr_files` | - |
| `cnvkit_reference` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dbsnp_vqsr` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `germline_resource` | - |
| `germline_resource_tbi` | - |
| `index_alignment` | - |
| `intervals_and_num_intervals` | - |
| `intervals_bed_combined` | - |
| `intervals_bed_combined_for_variant_calling` | - |
| `intervals_bed_gz_tbi_and_num_intervals` | - |
| `intervals_bed_gz_tbi_combined` | - |
| `intervals_for_preprocessing` | - |
| `known_indels_vqsr` | - |
| `known_sites_indels` | - |
| `known_sites_indels_tbi` | - |
| `known_sites_snps` | - |
| `known_sites_snps_tbi` | - |
| `known_snps_vqsr` | - |
| `mappability` | - |
| `msisensor2_models` | - |
| `msisensorpro_scan` | - |
| `ngscheckmate_bed` | - |
| `pon` | - |
| `pon_tbi` | - |
| `sentieon_dnascope_model` | - |
| `varlociraptor_scenario_germline` | - |
| `varlociraptor_scenario_somatic` | - |
| `varlociraptor_scenario_tumor_only` | - |
| `snpeff_cache` | - |
| `snpeff_db` | - |
| `vep_cache` | - |
| `vep_cache_version` | - |
| `vep_extra_files` | - |
| `vep_fasta` | - |
| `vep_genome` | - |
| `vep_species` | - |
| `versions` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


## BAM_NGSCHECKMATE {#bam-ngscheckmate}

*Defined in `subworkflows/nf-core/bam_ngscheckmate/main.nf:4`*

**Keywords:** `ngscheckmate`, `qc`, `bam`, `snp`

Take a set of bam files and run NGSCheckMate to determine whether samples match with each other, using a set of SNPs.

### Components

This workflow uses the following modules/subworkflows:

- `bcftools/mpileup`
- `ngscheckmate/ncm`

### Inputs

| Name | Description |
|------|-------------|
| `meta1` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `bam` | BAM files for each sample |
| `meta2` | Groovy Map containing bed file information e.g. [ id:'sarscov2' ] |
| `snp_bed` | BED file containing the SNPs to analyse. NGSCheckMate provides some default ones for hg19/hg38. |
| `meta3` | Groovy Map containing reference genome meta information e.g. [ id:'sarscov2' ] |
| `fasta` | fasta file for the genome |

### Outputs

| Name | Description |
|------|-------------|
| `pdf` | A pdf containing a dendrogram showing how the samples match up |
| `corr_matrix` | A text file containing the correlation matrix between each sample |
| `matched` | A txt file containing only the samples that match with each other |
| `all` | A txt file containing all the sample comparisons, whether they match or not |
| `vcf` | vcf files for each sample giving the SNP calls |
| `versions` | File containing software versions |

**Authors:** [@SPPearce](https://github.com/SPPearce)
**Maintainers:** [@SPPearce](https://github.com/SPPearce)


## UTILS_NFCORE_PIPELINE {#utils-nfcore-pipeline}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:11`*

**Keywords:** `utility`, `pipeline`, `initialise`, `version`

Subworkflow with utility functions specific to the nf-core pipeline template

### Inputs

| Name | Description |
|------|-------------|
| `nextflow_cli_args` | Nextflow CLI positional arguments |

### Outputs

| Name | Description |
|------|-------------|
| `success` | Dummy output to indicate success |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot), [@maxulysse](https://github.com/maxulysse)


## UTILS_NEXTFLOW_PIPELINE {#utils-nextflow-pipeline}

*Defined in `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:11`*

**Keywords:** `utility`, `pipeline`, `initialise`, `version`

Subworkflow with functionality that may be useful for any Nextflow pipeline

### Inputs

| Name | Description |
|------|-------------|
| `print_version` | Print the version of the pipeline and exit |
| `dump_parameters` | Dump the parameters of the pipeline to a JSON file |
| `output_directory` | Path to output dir to write JSON file to. |
| `check_conda_channel` | Check if the conda channel priority is correct. |

### Outputs

| Name | Description |
|------|-------------|
| `dummy_emit` | Dummy emit to make nf-core subworkflows lint happy |

**Authors:** [@adamrtalbot](https://github.com/adamrtalbot), [@drpatelh](https://github.com/drpatelh)
**Maintainers:** [@adamrtalbot](https://github.com/adamrtalbot), [@drpatelh](https://github.com/drpatelh), [@maxulysse](https://github.com/maxulysse)


## VCF_ANNOTATE_SNPEFF {#vcf-annotate-snpeff}

*Defined in `subworkflows/nf-core/vcf_annotate_snpeff/main.nf:8`*

**Keywords:** `vcf`, `annotation`, `snpeff`

Perform annotation with snpEff and bgzip + tabix index the resulting VCF file

### Components

This workflow uses the following modules/subworkflows:

- `snpeff`
- `snpeff/snpeff`
- `tabix/bgziptabix`

### Inputs

| Name | Description |
|------|-------------|
| `ch_vcf` | vcf file Structure: [ val(meta), path(vcf) ] |
| `val_snpeff_db` | db version to use |
| `ch_snpeff_cache` | path to root cache folder for snpEff (optional) Structure: [ path(cache) ] |

### Outputs

| Name | Description |
|------|-------------|
| `vcf_tbi` | Compressed vcf file + tabix index Structure: [ val(meta), path(vcf), path(tbi) ] |
| `reports` | html reports Structure: [ path(html) ] |
| `summary` | html reports Structure: [ path(csv) ] |
| `genes_txt` | html reports Structure: [ path(txt) ] |
| `versions` | Files containing software versions Structure: [ path(versions.yml) ] |

**Authors:** [@maxulysse](https://github.com/maxulysse)
**Maintainers:** [@maxulysse](https://github.com/maxulysse)


## UTILS_NFSCHEMA_PLUGIN {#utils-nfschema-plugin}

*Defined in `subworkflows/nf-core/utils_nfschema_plugin/main.nf:9`*

**Keywords:** `validation`, `JSON schema`, `plugin`, `parameters`, `summary`

Run nf-schema to validate parameters and create a summary of changed parameters

### Inputs

| Name | Description |
|------|-------------|
| `input_workflow` | The workflow object of the used pipeline. This object contains meta data used to create the params summary log |
| `validate_params` | Validate the parameters and error if invalid. |
| `parameters_schema` | Path to the parameters JSON schema. This has to be the same as the schema given to the `validation.parametersSchema` config option. When this input is empty it will automatically use the configured schema or "${projectDir}/nextflow_schema.json" as default. The schema should not be given in this way for meta pipelines. |

### Outputs

| Name | Description |
|------|-------------|
| `dummy_emit` | Dummy emit to make nf-core subworkflows lint happy |

**Authors:** [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@nvnieuwk](https://github.com/nvnieuwk)


## VCF_ANNOTATE_ENSEMBLVEP {#vcf-annotate-ensemblvep}

*Defined in `subworkflows/nf-core/vcf_annotate_ensemblvep/main.nf:8`*

**Keywords:** `vcf`, `annotation`, `ensemblvep`

Perform annotation with ensemblvep and bgzip + tabix index the resulting VCF file

### Components

This workflow uses the following modules/subworkflows:

- `ensemblvep/vep`
- `tabix/tabix`

### Inputs

| Name | Description |
|------|-------------|
| `ch_vcf` | vcf file to annotate Structure: [ val(meta), path(vcf), [path(custom_file1), path(custom_file2)... (optional)] ] |
| `ch_fasta` | Reference genome fasta file (optional) Structure: [ val(meta2), path(fasta) ] |
| `val_genome` | genome to use |
| `val_species` | species to use |
| `val_cache_version` | cache version to use |
| `ch_cache` | the root cache folder for ensemblvep (optional) Structure: [ val(meta3), path(cache) ] |
| `ch_extra_files` | any extra files needed by plugins for ensemblvep (optional) Structure: [ path(file1), path(file2)... ] |

### Outputs

| Name | Description |
|------|-------------|
| `vcf_tbi` | Compressed vcf file + tabix index Structure: [ val(meta), path(vcf), path(tbi) ] |
| `json` | json file Structure: [ val(meta), path(json) ] |
| `tab` | tab file Structure: [ val(meta), path(tab) ] |
| `reports` | html reports |
| `versions` | File containing software versions |

**Authors:** [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm), [@nvnieuwk](https://github.com/nvnieuwk)
**Maintainers:** [@maxulysse](https://github.com/maxulysse), [@matthdsm](https://github.com/matthdsm), [@nvnieuwk](https://github.com/nvnieuwk)


## BAM_VARIANT_CALLING_SOMATIC_MUTECT2 {#bam-variant-calling-somatic-mutect2}

*Defined in `subworkflows/local/bam_variant_calling_somatic_mutect2/main.nf:17`*

**Keywords:** `gatk4`, `mutect2`, `learnreadorientationmodel`, `getpileupsummaries`, `calculatecontamination`, `filtermutectcalls`, `variant_calling`, `tumor_only`, `filtered_vcf`

Perform variant calling on a paired tumor normal set of samples using mutect2 tumor normal mode.
f1r2 output of mutect2 is run through learnreadorientationmodel to get the artifact priors.
Run the input bam files through getpileupsummarries and then calculatecontamination to get the contamination and segmentation tables.
Filter the mutect2 output vcf using filtermutectcalls, artifact priors and the contamination & segmentation tables for additional filtering.

### Components

This workflow uses the following modules/subworkflows:

- `gatk4/mutect2`
- `gatk4/learnreadorientationmodel`
- `gatk4/getpileupsummaries`
- `gatk4/calculatecontamination`
- `gatk4/filtermutectcalls`

### Inputs

| Name | Description |
|------|-------------|
| `meta` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `input` | list containing the tumor and normal BAM files, in that order, also able to take CRAM as an input |
| `input_index` | list containing the tumor and normal BAM file indexes, in that order, also able to take CRAM index as an input |
| `which_norm` | optional list of sample headers contained in the normal sample input file. |
| `fasta` | The reference fasta file |
| `fai` | Index of reference fasta file |
| `dict` | GATK sequence dictionary |
| `germline_resource` | Population vcf of germline sequencing, containing allele fractions. |
| `germline_resource_tbi` | Index file for the germline resource. |
| `panel_of_normals` | vcf file to be used as a panel of normals. |
| `panel_of_normals_tbi` | Index for the panel of normals. |
| `interval_file` | File containing intervals. |

### Outputs

| Name | Description |
|------|-------------|
| `versions` | File containing software versions |
| `mutect2_vcf` | Compressed vcf file to be used for variant_calling. |
| `mutect2_tbi` | Indexes of the mutect2_vcf file |
| `mutect2_stats` | Stats files for the mutect2 vcf |
| `mutect2_f1r2` | file containing information to be passed to LearnReadOrientationModel. |
| `artifact_priors` | file containing artifact-priors to be used by filtermutectcalls. |
| `pileup_table_tumor` | File containing the tumor pileup summary table, kept separate as calculatecontamination needs them individually specified. |
| `pileup_table_normal` | File containing the normal pileup summary table, kept separate as calculatecontamination needs them individually specified. |
| `contamination_table` | File containing the contamination table. |
| `segmentation_table` | Output table containing segmentation of tumor minor allele fractions. |
| `filtered_vcf` | file containing filtered mutect2 calls. |
| `filtered_tbi` | tbi file that pairs with filtered vcf. |
| `filtered_stats` | file containing statistics of the filtermutectcalls run. |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie)


## SAMPLESHEET_TO_CHANNEL {#samplesheet-to-channel}

*Defined in `subworkflows/local/samplesheet_to_channel/main.nf:3`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_from_samplesheet` | - |
| `aligner` | - |
| `ascat_alleles` | - |
| `ascat_loci` | - |
| `ascat_loci_gc` | - |
| `ascat_loci_rt` | - |
| `bcftools_annotations` | - |
| `bcftools_annotations_tbi` | - |
| `bcftools_columns` | - |
| `bcftools_header_lines` | - |
| `build_only_index` | - |
| `dbsnp` | - |
| `fasta` | - |
| `germline_resource` | - |
| `intervals` | - |
| `joint_germline` | - |
| `joint_mutect2` | - |
| `known_indels` | - |
| `known_snps` | - |
| `no_intervals` | - |
| `pon` | - |
| `sentieon_dnascope_emit_mode` | - |
| `sentieon_haplotyper_emit_mode` | - |
| `seq_center` | - |
| `seq_platform` | - |
| `skip_tools` | - |
| `snpeff_cache` | - |
| `snpeff_db` | - |
| `step` | - |
| `tools` | - |
| `umi_length` | - |
| `umi_location` | - |
| `umi_in_read_header` | - |
| `umi_read_structure` | - |
| `wes` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |


## CHANNEL_VARIANT_CALLING_CREATE_CSV {#channel-variant-calling-create-csv}

*Defined in `subworkflows/local/channel_variant_calling_create_csv/main.nf:5`*

### Inputs

| Name | Description |
|------|-------------|
| `vcf_to_annotate` | - |
| `outdir` | - |

### Outputs

| Name | Description |
|------|-------------|
| `<none>` | - |


## BAM_VARIANT_CALLING_TUMOR_ONLY_LOFREQ {#bam-variant-calling-tumor-only-lofreq}

*Defined in `subworkflows/local/bam_variant_calling_tumor_only_lofreq/main.nf:4`*

### Inputs

| Name | Description |
|------|-------------|
| `input` | - |
| `fasta` | - |
| `fai` | - |
| `intervals` | - |
| `dict` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_TUMOR_ONLY_MUTECT2 {#bam-variant-calling-tumor-only-mutect2}

*Defined in `subworkflows/local/bam_variant_calling_tumor_only_mutect2/main.nf:16`*

**Keywords:** `gatk4`, `mutect2`, `getpileupsummaries`, `calculatecontamination`, `filtermutectcalls`, `variant_calling`, `tumor_only`, `filtered_vcf`

Perform variant calling on a single tumor sample using mutect2 tumor only mode.
Run the input bam file through getpileupsummarries and then calculatecontaminationto get the contamination and segmentation tables.
Filter the mutect2 output vcf using filtermutectcalls and the contamination & segmentation tables for additional filtering.

### Components

This workflow uses the following modules/subworkflows:

- `gatk4/mutect2`
- `gatk4/getpileupsummaries`
- `gatk4/calculatecontamination`
- `gatk4/filtermutectcalls`

### Inputs

| Name | Description |
|------|-------------|
| `meta` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `input` | list containing one BAM file, also able to take CRAM as an input |
| `input_index` | list containing one BAM file indexe, also able to take CRAM index as an input |
| `fasta` | The reference fasta file |
| `fai` | Index of reference fasta file |
| `dict` | GATK sequence dictionary |
| `germline_resource` | Population vcf of germline sequencing, containing allele fractions. |
| `germline_resource_tbi` | Index file for the germline resource. |
| `panel_of_normals` | vcf file to be used as a panel of normals. |
| `panel_of_normals_tbi` | Index for the panel of normals. |
| `interval_file` | File containing intervals. |

### Outputs

| Name | Description |
|------|-------------|
| `versions` | File containing software versions |
| `mutect2_vcf` | Compressed vcf file to be used for variant_calling. |
| `mutect2_tbi` | Indexes of the mutect2_vcf file |
| `mutect2_stats` | Stats files for the mutect2 vcf |
| `pileup_table` | File containing the pileup summary table. |
| `contamination_table` | File containing the contamination table. |
| `segmentation_table` | Output table containing segmentation of tumor minor allele fractions. |
| `filtered_vcf` | file containing filtered mutect2 calls. |
| `filtered_tbi` | tbi file that pairs with filtered vcf. |
| `filtered_stats` | file containing statistics of the filtermutectcalls run. |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie)


## BAM_JOINT_CALLING_GERMLINE_SENTIEON {#bam-joint-calling-germline-sentieon}

*Defined in `subworkflows/local/bam_joint_calling_germline_sentieon/main.nf:15`*

### Inputs

| Name | Description |
|------|-------------|
| `input` | - |
| `fasta` | - |
| `fai` | - |
| `dict` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dbsnp_vqsr` | - |
| `resource_indels_vcf` | - |
| `resource_indels_tbi` | - |
| `known_indels_vqsr` | - |
| `resource_snps_vcf` | - |
| `resource_snps_tbi` | - |
| `known_snps_vqsr` | - |
| `variant_caller` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## VCF_QC_BCFTOOLS_VCFTOOLS {#vcf-qc-bcftools-vcftools}

*Defined in `subworkflows/local/vcf_qc_bcftools_vcftools/main.nf:6`*

### Inputs

| Name | Description |
|------|-------------|
| `vcf` | - |
| `target_bed` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bcftools_stats` | - |
| `vcftools_tstv_counts` | - |
| `vcftools_tstv_qual` | - |
| `vcftools_filter_summary` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SENTIEON_DNASCOPE {#bam-variant-calling-sentieon-dnascope}

*Defined in `subworkflows/local/bam_variant_calling_sentieon_dnascope/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `dict` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dbsnp_vqsr` | - |
| `intervals` | - |
| `joint_germline` | - |
| `sentieon_dnascope_emit_mode` | - |
| `sentieon_dnascope_pcr_indel_model` | - |
| `sentieon_dnascope_model` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SOMATIC_MUSE {#bam-variant-calling-somatic-muse}

*Defined in `subworkflows/local/bam_variant_calling_somatic_muse/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `bam_normal` | - |
| `bam_tumor` | - |
| `fasta` | - |
| `dbsnp` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_FREEBAYES {#bam-variant-calling-freebayes}

*Defined in `subworkflows/local/bam_variant_calling_freebayes/main.nf:14`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_cram` | - |
| `ch_dict` | - |
| `ch_fasta` | - |
| `ch_fasta_fai` | - |
| `ch_intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `vcf_unfiltered` | - |
| `vcf` | - |
| `tbi` | - |
| `?` | - |


## CHANNEL_BASERECALIBRATOR_CREATE_CSV {#channel-baserecalibrator-create-csv}

*Defined in `subworkflows/local/channel_baserecalibrator_create_csv/main.nf:5`*

### Inputs

| Name | Description |
|------|-------------|
| `cram_table_bqsr` | - |
| `tools` | - |
| `skip_tools` | - |
| `outdir` | - |
| `save_output_as_bam` | - |

### Outputs

| Name | Description |
|------|-------------|
| `<none>` | - |


## BAM_VARIANT_CALLING_SOMATIC_MANTA {#bam-variant-calling-somatic-manta}

*Defined in `subworkflows/local/bam_variant_calling_somatic_manta/main.nf:9`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_TUMOR_ONLY_ALL {#bam-variant-calling-tumor-only-all}

*Defined in `subworkflows/local/bam_variant_calling_tumor_only_all/main.nf:17`*

### Inputs

| Name | Description |
|------|-------------|
| `tools` | - |
| `bam` | - |
| `cram` | - |
| `bwa` | - |
| `cf_chrom_len` | - |
| `chr_files` | - |
| `cnvkit_reference` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `germline_resource` | - |
| `germline_resource_tbi` | - |
| `intervals` | - |
| `intervals_bed_gz_tbi` | - |
| `intervals_bed_combined` | - |
| `intervals_bed_gz_tbi_combined` | - |
| `mappability` | - |
| `msisensor2_models` | - |
| `panel_of_normals` | - |
| `panel_of_normals_tbi` | - |
| `joint_mutect2` | - |
| `wes` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## PREPARE_REFERENCE_CNVKIT {#prepare-reference-cnvkit}

*Defined in `subworkflows/local/prepare_reference_cnvkit/main.nf:4`*

### Inputs

| Name | Description |
|------|-------------|
| `fasta` | - |
| `intervals_bed_combined` | - |

### Outputs

| Name | Description |
|------|-------------|
| `cnvkit_reference` | - |
| `?` | - |


## CONCATENATE_GERMLINE_VCFS {#concatenate-germline-vcfs}

*Defined in `subworkflows/local/vcf_concatenate_germline/main.nf:12`*

### Inputs

| Name | Description |
|------|-------------|
| `vcfs` | - |

### Outputs

| Name | Description |
|------|-------------|
| `vcfs` | - |
| `tbis` | - |
| `?` | - |


## BAM_VARIANT_CALLING_TUMOR_ONLY_CONTROLFREEC {#bam-variant-calling-tumor-only-controlfreec}

*Defined in `subworkflows/local/bam_variant_calling_tumor_only_controlfreec/main.nf:13`*

### Inputs

| Name | Description |
|------|-------------|
| `controlfreec_input` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `chr_files` | - |
| `mappability` | - |
| `intervals_bed` | - |

### Outputs

| Name | Description |
|------|-------------|
| `versions` | - |


## BAM_VARIANT_CALLING_TUMOR_ONLY_MANTA {#bam-variant-calling-tumor-only-manta}

*Defined in `subworkflows/local/bam_variant_calling_tumor_only_manta/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SOMATIC_ALL {#bam-variant-calling-somatic-all}

*Defined in `subworkflows/local/bam_variant_calling_somatic_all/main.nf:21`*

### Inputs

| Name | Description |
|------|-------------|
| `tools` | - |
| `bam` | - |
| `cram` | - |
| `bwa` | - |
| `cf_chrom_len` | - |
| `chr_files` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `germline_resource` | - |
| `germline_resource_tbi` | - |
| `intervals` | - |
| `intervals_bed_gz_tbi` | - |
| `intervals_bed_combined` | - |
| `intervals_bed_gz_tbi_combined` | - |
| `mappability` | - |
| `msisensorpro_scan` | - |
| `panel_of_normals` | - |
| `panel_of_normals_tbi` | - |
| `allele_files` | - |
| `loci_files` | - |
| `gc_file` | - |
| `rt_file` | - |
| `joint_mutect2` | - |
| `wes` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_MARKDUPLICATES_SPARK {#bam-markduplicates-spark}

*Defined in `subworkflows/local/bam_markduplicates_spark/main.nf:12`*

### Inputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals_bed_combined` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_APPLYBQSR_SPARK {#bam-applybqsr-spark}

*Defined in `subworkflows/local/bam_applybqsr_spark/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `cram` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SOMATIC_STRELKA {#bam-variant-calling-somatic-strelka}

*Defined in `subworkflows/local/bam_variant_calling_somatic_strelka/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## CHANNEL_MARKDUPLICATES_CREATE_CSV {#channel-markduplicates-create-csv}

*Defined in `subworkflows/local/channel_markduplicates_create_csv/main.nf:5`*

### Inputs

| Name | Description |
|------|-------------|
| `cram_markduplicates` | - |
| `csv_subfolder` | - |
| `outdir` | - |
| `save_output_as_bam` | - |

### Outputs

| Name | Description |
|------|-------------|
| `<none>` | - |


## BAM_VARIANT_CALLING_DEEPVARIANT {#bam-variant-calling-deepvariant}

*Defined in `subworkflows/local/bam_variant_calling_deepvariant/main.nf:12`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## VCF_VARLOCIRAPTOR_SINGLE {#vcf-varlociraptor-single}

*Defined in `subworkflows/local/vcf_varlociraptor_single/main.nf:9`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_cram` | - |
| `ch_fasta` | - |
| `ch_fasta_fai` | - |
| `ch_scenario` | - |
| `ch_vcf` | - |
| `val_num_chunks` | - |
| `val_sampletype` | - |

### Outputs

| Name | Description |
|------|-------------|
| `vcf` | - |
| `tbi` | - |
| `versions` | - |


## CRAM_QC_MOSDEPTH_SAMTOOLS {#cram-qc-mosdepth-samtools}

*Defined in `subworkflows/local/cram_qc_mosdepth_samtools/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


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
| `?` | - |


## FASTQ_PREPROCESS_GATK {#fastq-preprocess-gatk}

*Defined in `subworkflows/local/fastq_preprocess_gatk/main.nf:52`*

### Inputs

| Name | Description |
|------|-------------|
| `input_fastq` | - |
| `input_sample` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `index_alignment` | - |
| `intervals_and_num_intervals` | - |
| `intervals_for_preprocessing` | - |
| `known_sites_indels` | - |
| `known_sites_indels_tbi` | - |
| `bbsplit_index` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_MERGE_INDEX_SAMTOOLS {#bam-merge-index-samtools}

*Defined in `subworkflows/local/bam_merge_index_samtools/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `bam` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


## FASTQ_PREPROCESS_PARABRICKS {#fastq-preprocess-parabricks}

*Defined in `subworkflows/local/fastq_preprocess_parabricks/main.nf:4`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_reads` | - |
| `ch_fasta` | - |
| `ch_index` | - |
| `ch_interval_file` | - |
| `ch_known_sites` | - |
| `val_output_fmt` | - |

### Outputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `versions` | - |
| `reports` | - |


## VCF_VARIANT_FILTERING_GATK {#vcf-variant-filtering-gatk}

*Defined in `subworkflows/local/vcf_variant_filtering_gatk/main.nf:4`*

### Inputs

| Name | Description |
|------|-------------|
| `vcf` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `dict` | - |
| `intervals_bed_combined` | - |
| `known_sites` | - |
| `known_sites_tbi` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_CONVERT_SAMTOOLS {#bam-convert-samtools}

*Defined in `subworkflows/local/bam_convert_samtools/main.nf:14`*

### Inputs

| Name | Description |
|------|-------------|
| `input` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `interleaved` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


## BAM_SENTIEON_DEDUP {#bam-sentieon-dedup}

*Defined in `subworkflows/local/bam_sentieon_dedup/main.nf:7`*

### Inputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `bai` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals_bed_combined` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SOMATIC_TIDDIT {#bam-variant-calling-somatic-tiddit}

*Defined in `subworkflows/local/bam_variant_calling_somatic_tiddit/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram_normal` | - |
| `cram_tumor` | - |
| `fasta` | - |
| `bwa` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## CHANNEL_ALIGN_CREATE_CSV {#channel-align-create-csv}

*Defined in `subworkflows/local/channel_align_create_csv/main.nf:5`*

### Inputs

| Name | Description |
|------|-------------|
| `bam_indexed` | - |
| `outdir` | - |
| `save_output_as_bam` | - |

### Outputs

| Name | Description |
|------|-------------|
| `<none>` | - |


## BAM_MARKDUPLICATES {#bam-markduplicates}

*Defined in `subworkflows/local/bam_markduplicates/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals_bed_combined` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## CRAM_MERGE_INDEX_SAMTOOLS {#cram-merge-index-samtools}

*Defined in `subworkflows/local/cram_merge_index_samtools/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


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


## BAM_VARIANT_CALLING_SENTIEON_HAPLOTYPER {#bam-variant-calling-sentieon-haplotyper}

*Defined in `subworkflows/local/bam_variant_calling_sentieon_haplotyper/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `dict` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dbsnp_vqsr` | - |
| `intervals` | - |
| `joint_germline` | - |
| `sentieon_haplotyper_emit_mode` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SINGLE_TIDDIT {#bam-variant-calling-single-tiddit}

*Defined in `subworkflows/local/bam_variant_calling_single_tiddit/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `bwa` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_CNVKIT {#bam-variant-calling-cnvkit}

*Defined in `subworkflows/local/bam_variant_calling_cnvkit/main.nf:12`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `targets` | - |
| `reference` | - |

### Outputs

| Name | Description |
|------|-------------|
| `cnv_calls_raw` | - |
| `cnv_calls_export` | - |
| `?` | - |


## CRAM_SAMPLEQC {#cram-sampleqc}

*Defined in `subworkflows/local/cram_sampleqc/main.nf:4`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `ngscheckmate_bed` | - |
| `fasta` | - |
| `skip_baserecalibration` | - |
| `intervals_for_preprocessing` | - |

### Outputs

| Name | Description |
|------|-------------|
| `corr_matrix` | - |
| `matched` | - |
| `all` | - |
| `vcf` | - |
| `pdf` | - |
| `?` | - |
| `?` | - |


## CONSENSUS {#consensus}

*Defined in `subworkflows/local/vcf_consensus/main.nf:8`*

### Inputs

| Name | Description |
|------|-------------|
| `vcfs` | - |

### Outputs

| Name | Description |
|------|-------------|
| `versions` | - |
| `vcfs` | - |
| `tbis` | - |


## BAM_VARIANT_CALLING_INDEXCOV {#bam-variant-calling-indexcov}

*Defined in `subworkflows/local/bam_variant_calling_indexcov/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |

### Outputs

| Name | Description |
|------|-------------|
| `out_indexcov` | - |
| `?` | - |


## FASTQ_CREATE_UMI_CONSENSUS_FGBIO {#fastq-create-umi-consensus-fgbio}

*Defined in `subworkflows/local/fastq_create_umi_consensus_fgbio/main.nf:16`*

### Inputs

| Name | Description |
|------|-------------|
| `reads` | - |
| `fasta` | - |
| `fai` | - |
| `map_index` | - |
| `groupreadsbyumi_strategy` | - |

### Outputs

| Name | Description |
|------|-------------|
| `umibam` | - |
| `groupbam` | - |
| `consensusbam` | - |
| `versions` | - |


## BAM_VARIANT_CALLING_MPILEUP {#bam-variant-calling-mpileup}

*Defined in `subworkflows/local/bam_variant_calling_mpileup/main.nf:12`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `dict` | - |
| `fasta` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SINGLE_STRELKA {#bam-variant-calling-single-strelka}

*Defined in `subworkflows/local/bam_variant_calling_single_strelka/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## POST_VARIANTCALLING {#post-variantcalling}

*Defined in `subworkflows/local/post_variantcalling/main.nf:12`*

### Inputs

| Name | Description |
|------|-------------|
| `tools` | - |
| `cram_germline` | - |
| `germline_vcfs` | - |
| `germline_tbis` | - |
| `cram_tumor_only` | - |
| `tumor_only_vcfs` | - |
| `tumor_only_tbis` | - |
| `cram_somatic` | - |
| `somatic_vcfs` | - |
| `somatic_tbis` | - |
| `fasta` | - |
| `fai` | - |
| `concatenate_vcfs` | - |
| `filter_vcfs` | - |
| `snv_consensus_calling` | - |
| `normalize_vcfs` | - |
| `varlociraptor_chunk_size` | - |
| `varlociraptor_scenario_germline` | - |
| `varlociraptor_scenario_somatic` | - |
| `varlociraptor_scenario_tumor_only` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## VCF_VARLOCIRAPTOR_SOMATIC {#vcf-varlociraptor-somatic}

*Defined in `subworkflows/local/vcf_varlociraptor_somatic/main.nf:15`*

### Inputs

| Name | Description |
|------|-------------|
| `ch_cram` | - |
| `ch_fasta` | - |
| `ch_fasta_fai` | - |
| `ch_scenario` | - |
| `ch_somatic_vcf` | - |
| `ch_germline_vcf` | - |
| `val_num_chunks` | - |

### Outputs

| Name | Description |
|------|-------------|
| `vcf` | - |
| `tbi` | - |
| `versions` | - |


## BAM_VARIANT_CALLING_GERMLINE_MANTA {#bam-variant-calling-germline-manta}

*Defined in `subworkflows/local/bam_variant_calling_germline_manta/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_APPLYBQSR {#bam-applybqsr}

*Defined in `subworkflows/local/bam_applybqsr/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `bam` | - |
| `cram` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SOMATIC_TNSCOPE {#bam-variant-calling-somatic-tnscope}

*Defined in `subworkflows/local/bam_variant_calling_somatic_tnscope/main.nf:9`*

### Inputs

| Name | Description |
|------|-------------|
| `input` | - |
| `fasta` | - |
| `fai` | - |
| `dict` | - |
| `germline_resource` | - |
| `germline_resource_tbi` | - |
| `panel_of_normals` | - |
| `panel_of_normals_tbi` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## NORMALIZE_VCFS {#normalize-vcfs}

*Defined in `subworkflows/local/vcf_normalization/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `vcfs` | - |
| `fasta` | - |

### Outputs

| Name | Description |
|------|-------------|
| `vcfs` | - |
| `tbis` | - |
| `?` | - |


## BAM_VARIANT_CALLING_TUMOR_ONLY_TNSCOPE {#bam-variant-calling-tumor-only-tnscope}

*Defined in `subworkflows/local/bam_variant_calling_tumor_only_tnscope/main.nf:9`*

**Keywords:** `gatk4`, `mutect2`, `getpileupsummaries`, `calculatecontamination`, `filtermutectcalls`, `variant_calling`, `tumor_only`, `filtered_vcf`

Perform variant calling on a single tumor sample using mutect2 tumor only mode.
Run the input bam file through getpileupsummarries and then calculatecontaminationto get the contamination and segmentation tables.
Filter the mutect2 output vcf using filtermutectcalls and the contamination & segmentation tables for additional filtering.

### Components

This workflow uses the following modules/subworkflows:

- `gatk4/mutect2`
- `gatk4/getpileupsummaries`
- `gatk4/calculatecontamination`
- `gatk4/filtermutectcalls`

### Inputs

| Name | Description |
|------|-------------|
| `meta` | Groovy Map containing sample information e.g. [ id:'test' ] |
| `input` | list containing one BAM file, also able to take CRAM as an input |
| `input_index` | list containing one BAM file indexe, also able to take CRAM index as an input |
| `fasta` | The reference fasta file |
| `fai` | Index of reference fasta file |
| `dict` | GATK sequence dictionary |
| `germline_resource` | Population vcf of germline sequencing, containing allele fractions. |
| `germline_resource_tbi` | Index file for the germline resource. |
| `panel_of_normals` | vcf file to be used as a panel of normals. |
| `panel_of_normals_tbi` | Index for the panel of normals. |
| `interval_file` | File containing intervals. |

### Outputs

| Name | Description |
|------|-------------|
| `versions` | File containing software versions |
| `mutect2_vcf` | Compressed vcf file to be used for variant_calling. |
| `mutect2_tbi` | Indexes of the mutect2_vcf file |
| `mutect2_stats` | Stats files for the mutect2 vcf |
| `pileup_table` | File containing the pileup summary table. |
| `contamination_table` | File containing the contamination table. |
| `segmentation_table` | Output table containing segmentation of tumor minor allele fractions. |
| `filtered_vcf` | file containing filtered mutect2 calls. |
| `filtered_tbi` | tbi file that pairs with filtered vcf. |
| `filtered_stats` | file containing statistics of the filtermutectcalls run. |

**Authors:** [@GCJMackenzie](https://github.com/GCJMackenzie)


## BAM_VARIANT_CALLING_HAPLOTYPECALLER {#bam-variant-calling-haplotypecaller}

*Defined in `subworkflows/local/bam_variant_calling_haplotypecaller/main.nf:11`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `dict` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `intervals` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## PIPELINE_INITIALISATION {#pipeline-initialisation}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:26`*

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
| `?` | - |


## PIPELINE_COMPLETION {#pipeline-completion}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:203`*

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


## PREPARE_GENOME {#prepare-genome}

*Defined in `subworkflows/local/prepare_genome/main.nf:22`*

### Inputs

| Name | Description |
|------|-------------|
| `ascat_alleles_in` | - |
| `ascat_loci_in` | - |
| `ascat_loci_gc_in` | - |
| `ascat_loci_rt_in` | - |
| `bbsplit_fasta_list_in` | - |
| `bbsplit_index_in` | - |
| `bcftools_annotations_in` | - |
| `bcftools_annotations_tbi_in` | - |
| `bwa_in` | - |
| `bwamem2_in` | - |
| `chr_dir_in` | - |
| `dbsnp_in` | - |
| `dbsnp_tbi_in` | - |
| `dict_in` | - |
| `dragmap_in` | - |
| `fasta_in` | - |
| `fasta_fai_in` | - |
| `germline_resource_in` | - |
| `germline_resource_tbi_in` | - |
| `known_indels_in` | - |
| `known_indels_tbi_in` | - |
| `known_snps_in` | - |
| `known_snps_tbi_in` | - |
| `msisensor2_models_in` | - |
| `msisensorpro_scan_in` | - |
| `pon_in` | - |
| `pon_tbi_in` | - |
| `aligner` | - |
| `step` | - |
| `tools` | - |
| `vep_include_fasta` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_SOMATIC_CONTROLFREEC {#bam-variant-calling-somatic-controlfreec}

*Defined in `subworkflows/local/bam_variant_calling_somatic_controlfreec/main.nf:13`*

### Inputs

| Name | Description |
|------|-------------|
| `controlfreec_input` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `chr_files` | - |
| `mappability` | - |
| `intervals_bed` | - |

### Outputs

| Name | Description |
|------|-------------|
| `versions` | - |


## BAM_BASERECALIBRATOR_SPARK {#bam-baserecalibrator-spark}

*Defined in `subworkflows/local/bam_baserecalibrator_spark/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |
| `known_sites` | - |
| `known_sites_tbi` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


## BAM_BASERECALIBRATOR {#bam-baserecalibrator}

*Defined in `subworkflows/local/bam_baserecalibrator/main.nf:10`*

### Inputs

| Name | Description |
|------|-------------|
| `cram` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |
| `known_sites` | - |
| `known_sites_tbi` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |


## BAM_JOINT_CALLING_GERMLINE_GATK {#bam-joint-calling-germline-gatk}

*Defined in `subworkflows/local/bam_joint_calling_germline_gatk/main.nf:17`*

### Inputs

| Name | Description |
|------|-------------|
| `input` | - |
| `fasta` | - |
| `fai` | - |
| `dict` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dbsnp_vqsr` | - |
| `resource_indels_vcf` | - |
| `resource_indels_tbi` | - |
| `known_indels_vqsr` | - |
| `resource_snps_vcf` | - |
| `resource_snps_tbi` | - |
| `known_snps_vqsr` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |


## CHANNEL_APPLYBQSR_CREATE_CSV {#channel-applybqsr-create-csv}

*Defined in `subworkflows/local/channel_applybqsr_create_csv/main.nf:5`*

### Inputs

| Name | Description |
|------|-------------|
| `cram_recalibrated_index` | - |
| `outdir` | - |
| `save_output_as_bam` | - |

### Outputs

| Name | Description |
|------|-------------|
| `<none>` | - |


## FASTQ_ALIGN {#fastq-align}

*Defined in `subworkflows/local/fastq_align/main.nf:12`*

### Inputs

| Name | Description |
|------|-------------|
| `reads` | - |
| `index` | - |
| `sort` | - |
| `fasta` | - |
| `fasta_fai` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## BAM_VARIANT_CALLING_GERMLINE_ALL {#bam-variant-calling-germline-all}

*Defined in `subworkflows/local/bam_variant_calling_germline_all/main.nf:22`*

### Inputs

| Name | Description |
|------|-------------|
| `tools` | - |
| `skip_tools` | - |
| `bam` | - |
| `cram` | - |
| `bwa` | - |
| `cnvkit_reference` | - |
| `dbsnp` | - |
| `dbsnp_tbi` | - |
| `dbsnp_vqsr` | - |
| `dict` | - |
| `fasta` | - |
| `fasta_fai` | - |
| `intervals` | - |
| `intervals_bed_combined` | - |
| `intervals_bed_gz_tbi_combined` | - |
| `intervals_bed_combined_haplotypec` | - |
| `intervals_bed_gz_tbi` | - |
| `known_indels_vqsr` | - |
| `known_sites_indels` | - |
| `known_sites_indels_tbi` | - |
| `known_sites_snps` | - |
| `known_sites_snps_tbi` | - |
| `known_snps_vqsr` | - |
| `joint_germline` | - |
| `skip_haplotypecaller_filter` | - |
| `sentieon_haplotyper_emit_mode` | - |
| `sentieon_dnascope_emit_mode` | - |
| `sentieon_dnascope_pcr_indel_model` | - |
| `sentieon_dnascope_model` | - |

### Outputs

| Name | Description |
|------|-------------|
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |
| `?` | - |


## VCF_ANNOTATE_ALL {#vcf-annotate-all}

*Defined in `subworkflows/local/vcf_annotate_all/main.nf:10`*

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
| `?` | - |


## BAM_VARIANT_CALLING_SOMATIC_ASCAT {#bam-variant-calling-somatic-ascat}

*Defined in `subworkflows/local/bam_variant_calling_somatic_ascat/main.nf:9`*

### Inputs

| Name | Description |
|------|-------------|
| `cram_pair` | - |
| `allele_files` | - |
| `loci_files` | - |
| `intervals_bed` | - |
| `fasta` | - |
| `gc_file` | - |
| `rt_file` | - |

### Outputs

| Name | Description |
|------|-------------|
| `versions` | - |


---

*This pipeline was built with [Nextflow](https://nextflow.io).
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 14:20:18 UTC.*
