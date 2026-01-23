# Pipeline Inputs

This page documents all input parameters for the pipeline.

## Input/output options

### `--input` {#input}

**Type:** `string` | **Required** | **Format:** `file-path`

Path to comma-separated file containing information about the samples in the experiment.

> A design file with information about the samples in your experiment. Use this parameter to specify the location of the input files. It has to be a tab or comma-separated file with a header row or a JSON/YAML file. See [usage docs](https://nf-co.re/rnavar/usage#input).

**Pattern:** `^\S+\.(csv|tsv|yaml|yml|json)$`


### `--outdir` {#outdir}

**Type:** `string` | **Required** | **Format:** `directory-path`

The output directory where the results will be saved. You have to use absolute paths to storage on Cloud infrastructure.


### `--tools` {#tools}

**Type:** `string` | *Optional*

Specify which additional tools RNAvar should use. Values can be 'seq2hla', 'bcfann', 'snpeff', 'vep' or 'merge'. If you specify 'merge', the pipeline runs both snpeff and VEP annotation.

> List of tools to be used in addition to variant calling: currently hlatyping with Seq2HLA and a choice of annotation tools.

**Pattern:** `^((bcfann|seq2hla|snpeff|vep|merge)*(,)*)*$`


### `--save_merged_fastq` {#save-merged-fastq}

**Type:** `boolean` | *Optional*

Save FastQ files after merging re-sequenced libraries in the results directory.



## Preprocessing of alignment

### `--extract_umi` {#extract-umi}

**Type:** `boolean` | *Optional*

Specify whether to remove UMIs from the reads with UMI-tools extract.


### `--umitools_extract_method` {#umitools-extract-method}

**Type:** `string` | *Optional*

UMI pattern to use. Can be either 'string' (default) or 'regex'.

> More details can be found in the [UMI-tools documentation](https://umi-tools.readthedocs.io/en/latest/reference/extract.html#extract-method).


**Default:** `string`

**Allowed values:**
- `string`
- `regex`


### `--umitools_bc_pattern` {#umitools-bc-pattern}

**Type:** `string` | *Optional*

The UMI barcode pattern to use e.g. 'NNNNNN' indicates that the first 6 nucleotides of the read are from the UMI.

> More details can be found in the [UMI-tools documentation](https://umi-tools.readthedocs.io/en/latest/reference/extract.html#extract-method).

**Pattern:** `^[NXC]*$`


### `--umitools_bc_pattern2` {#umitools-bc-pattern2}

**Type:** `string` | *Optional*

The UMI barcode pattern to use if the UMI is located in read 2.

**Pattern:** `^[NXC]*$`


### `--umitools_umi_separator` {#umitools-umi-separator}

**Type:** `string` | *Optional*

The character that separates the UMI in the read name. Most likely a colon if you skipped the extraction with UMI-tools and used other software.



## Alignment options

### `--aligner` {#aligner}

**Type:** `string` | **Required**

Specifies the alignment algorithm to use.

> This parameter define which aligner is to be used for aligning the RNA reads to the reference genome.

**Default:** `star`

**Allowed values:**
- `star`


### `--star_index` {#star-index}

**Type:** `string` | *Optional* | **Format:** `path`

Path to STAR index folder or compressed file (tar.gz)

> This parameter can be used if there is an pre-defined STAR index available. You can either give the full path to the index directory or a compressed file in tar.gz format.


### `--star_twopass` {#star-twopass}

**Type:** `boolean` | *Optional*

Enable STAR 2-pass mapping mode.

> This parameter enables STAR to perform 2-pass mapping. Default true.

**Default:** `True`


### `--star_ignore_sjdbgtf` {#star-ignore-sjdbgtf}

**Type:** `boolean` | *Optional*

Do not use GTF file during STAR index building step

> Do not use parameter --sjdbGTFfile <GTF file> during the STAR genomeGenerate process.


### `--star_max_memory_bamsort` {#star-max-memory-bamsort}

**Type:** `integer` | *Optional*

Option to limit RAM when sorting BAM file. Value to be specified in bytes. If 0, will be set to the genome index size.

> This parameter specifies the maximum available RAM (bytes) for sorting BAM during STAR alignment.

**Default:** `0`


### `--star_bins_bamsort` {#star-bins-bamsort}

**Type:** `integer` | *Optional*

Specifies the number of genome bins for coordinate-sorting

> This parameter specifies the number of bins to be used for coordinate sorting during STAR alignment step.

**Default:** `50`


### `--star_max_collapsed_junc` {#star-max-collapsed-junc}

**Type:** `integer` | *Optional*

Specifies the maximum number of collapsed junctions

**Default:** `1000000`


### `--star_max_intron_size` {#star-max-intron-size}

**Type:** `integer` | *Optional*

Specifies the maximum intron size

> This parameter specifies the maximum intron size for STAR alignment


### `--seq_center` {#seq-center}

**Type:** `string` | *Optional*

Sequencing center information to be added to read group of BAM files.

> This parameter is required for creating a proper BAM header to use in the downstream analysis of GATK. 


### `--seq_platform` {#seq-platform}

**Type:** `string` | **Required**

Specify the sequencing platform used

> This parameter is required for creating a proper BAM header to use in the downstream analysis of GATK. 

**Default:** `illumina`


### `--save_unaligned` {#save-unaligned}

**Type:** `boolean` | *Optional*

Where possible, save unaligned reads from aligner to the results directory.

> This may either be in the form of FastQ or BAM files depending on the options available for that particular tool.


### `--save_align_intermeds` {#save-align-intermeds}

**Type:** `boolean` | *Optional*

Save the intermediate BAM files from the alignment step.

> By default, intermediate BAM files will not be saved. The final BAM files created after the appropriate filtering step are always saved to limit storage usage. Set this parameter to also save other intermediate BAM files.


### `--bam_csi_index` {#bam-csi-index}

**Type:** `boolean` | *Optional*

Create a CSI index for BAM files instead of the traditional BAI index. This will be required for genomes with larger chromosome sizes.



## Postprocessing of alignment

### `--remove_duplicates` {#remove-duplicates}

**Type:** `boolean` | *Optional*

Specify whether to remove duplicates from the BAM during Picard MarkDuplicates step.

> Specify true for removing duplicates from BAM file during Picard MarkDuplicates step.



## Variant calling

### `--gatk_hc_call_conf` {#gatk-hc-call-conf}

**Type:** `integer` | *Optional*

The minimum phred-scaled confidence threshold at which variants should be called.

> Specify the minimum phred-scaled confidence threshold at which variants should be called.

**Default:** `20`


### `--generate_gvcf` {#generate-gvcf}

**Type:** `boolean` | *Optional*

Enable generation of GVCFs by sample additionnaly to the VCFs.

> This parameter enables GATK HAPLOTYPECALLER to generate GVCFs. Default false.


### `--gatk_interval_scatter_count` {#gatk-interval-scatter-count}

**Type:** `integer` | *Optional*

Number of times the gene interval list to be split in order to run GATK haplotype caller in parallel

> Set this parameter to decide the number of splits for the gene interval list file.

**Default:** `25`


### `--no_intervals` {#no-intervals}

**Type:** `boolean` | *Optional*

Do not use gene interval file during variant calling

> This parameter, if set to True, does not use the gene intervals during the variant calling step, which then results in variants from all regions including non-genic. Default is False



## Variant filtering

### `--gatk_vf_qd_filter` {#gatk-vf-qd-filter}

**Type:** `number` | *Optional*

Value to be used for the QualByDepth (QD) filter

> This parameter defines the value to use for the QualByDepth (QD) filter in the GATK variant-filtering step. 
The value should given in a float number format.

**Default:** `2`


### `--gatk_vf_fs_filter` {#gatk-vf-fs-filter}

**Type:** `number` | *Optional*

Value to be used for the FisherStrand (FS) filter

> This parameter defines the value to use for the FisherStrand (FS) filter in the GATK variant-filtering step. 
The value should given in a float number format.

**Default:** `30`


### `--gatk_vf_window_size` {#gatk-vf-window-size}

**Type:** `integer` | *Optional*

The window size (in bases) in which to evaluate clustered SNPs.

> This parameter is used by GATK variant filteration step. It defines the window size (in bases) in which to evaluate clustered SNPs. It has to be used together with the other option 'cluster'.

**Default:** `35`


### `--gatk_vf_cluster_size` {#gatk-vf-cluster-size}

**Type:** `integer` | *Optional*

The number of SNPs which make up a cluster. Must be at least 2.

> This parameter is used by GATK variant filteration step. It defines the number of SNPs which make up a cluster within a window. Must be at least 2.

**Default:** `3`



## Variant Annotation

### `--vep_cache` {#vep-cache}

**Type:** `string` | *Optional* | **Format:** `directory-path`

Path to VEP cache.

> Path to VEP cache which should contain the relevant species, genome and build directories at the path ${vep_species}/${vep_genome}_${vep_cache_version}

**Default:** `s3://annotation-cache/vep_cache/`


### `--snpeff_cache` {#snpeff-cache}

**Type:** `string` | *Optional* | **Format:** `directory-path`

Path to snpEff cache.

> Path to snpEff cache which should contain the relevant genome and build directory in the path ${snpeff_species}.${snpeff_version}

**Default:** `s3://annotation-cache/snpeff_cache/`


### `--vep_include_fasta` {#vep-include-fasta}

**Type:** `boolean` | *Optional*

Allow usage of fasta file for annotation with VEP

> By pointing VEP to a FASTA file, it is possible to retrieve reference sequence locally. This enables VEP to retrieve HGVS notations (--hgvs), check the reference sequence given in input data, and construct transcript models from a GFF or GTF file without accessing a database.

For details, see [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_cache.html#fasta).


### `--vep_dbnsfp` {#vep-dbnsfp}

**Type:** `boolean` | *Optional*

Enable the use of the VEP dbNSFP plugin.

> For details, see [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html#dbnsfp).


### `--dbnsfp` {#dbnsfp}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to dbNSFP processed file.

> To be used with `--vep_dbnsfp`.
dbNSFP files and more information are available at https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html#dbnsfp and https://sites.google.com/site/jpopgen/dbNSFP/

**Pattern:** `^\S+\.gz$`


### `--dbnsfp_tbi` {#dbnsfp-tbi}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to dbNSFP tabix indexed file.

> To be used with `--vep_dbnsfp`.

**Pattern:** `^\S+\.tbi$`


### `--dbnsfp_consequence` {#dbnsfp-consequence}

**Type:** `string` | *Optional*

Consequence to annotate with

> To be used with `--vep_dbnsfp`.
This params is used to filter/limit outputs to a specific effect of the variant.
The set of consequence terms is defined by the Sequence Ontology and an overview of those used in VEP can be found here: https://www.ensembl.org/info/genome/variation/prediction/predicted_data.html
If one wants to filter using several consequences, then separate those by using '&' (i.e. 'consequence=3_prime_UTR_variant&intron_variant'.


### `--dbnsfp_fields` {#dbnsfp-fields}

**Type:** `string` | *Optional*

Fields to annotate with

> To be used with `--vep_dbnsfp`.
This params can be used to retrieve individual values from the dbNSFP file. The values correspond to the name of the columns in the dbNSFP file and are separated by comma.
The column names might differ between the different dbNSFP versions. Please check the Readme.txt file, which is provided with the dbNSFP file, to obtain the correct column names. The Readme file contains also a short description of the provided values and the version of the tools used to generate them.

Default value are explained below:

rs_dbSNP - rs number from dbSNP
HGVSc_VEP - HGVS coding variant presentation from VEP. Multiple entries separated by ';', corresponds to Ensembl_transcriptid
HGVSp_VEP - HGVS protein variant presentation from VEP. Multiple entries separated by ';', corresponds to Ensembl_proteinid
1000Gp3_EAS_AF - Alternative allele frequency in the 1000Gp3 East Asian descendent samples
1000Gp3_AMR_AF - Alternative allele counts in the 1000Gp3 American descendent samples
LRT_score - Original LRT two-sided p-value (LRTori), ranges from 0 to 1
GERP++_RS - Conservation score. The larger the score, the more conserved the site, ranges from -12.3 to 6.17
gnomAD_exomes_AF - Alternative allele frequency in the whole gnomAD exome samples.

**Default:** `rs_dbSNP,HGVSc_VEP,HGVSp_VEP,1000Gp3_EAS_AF,1000Gp3_AMR_AF,LRT_score,GERP++_RS,gnomAD_exomes_AF`


### `--vep_loftee` {#vep-loftee}

**Type:** `boolean` | *Optional*

Enable the use of the VEP LOFTEE plugin.

> For details, see [here](https://github.com/konradjk/loftee).


### `--vep_spliceai` {#vep-spliceai}

**Type:** `boolean` | *Optional*

Enable the use of the VEP SpliceAI plugin.

> For details, see [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html#spliceai).


### `--spliceai_snv` {#spliceai-snv}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to spliceai raw scores snv file.

> To be used with `--vep_spliceai`.

**Pattern:** `^\S+\.vcf\.gz$`


### `--spliceai_snv_tbi` {#spliceai-snv-tbi}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to spliceai raw scores snv tabix indexed file.

> To be used with `--vep_spliceai`.

**Pattern:** `^\S+\.tbi$`


### `--spliceai_indel` {#spliceai-indel}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to spliceai raw scores indel file.

> To be used with `--vep_spliceai`.

**Pattern:** `^\S+\.vcf\.gz$`


### `--spliceai_indel_tbi` {#spliceai-indel-tbi}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to spliceai raw scores indel tabix indexed file.

> To be used with `--vep_spliceai`.

**Pattern:** `^\S+\.tbi$`


### `--vep_spliceregion` {#vep-spliceregion}

**Type:** `boolean` | *Optional*

Enable the use of the VEP SpliceRegion plugin.

> For details, see [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html#spliceregion) and [here](https://www.ensembl.info/2018/10/26/cool-stuff-the-vep-can-do-splice-site-variant-annotation/).


### `--vep_custom_args` {#vep-custom-args}

**Type:** `string` | *Optional*

Add an extra custom argument to VEP.

> Using this parameter, you can add custom args to VEP.

**Default:** `--everything --filter_common --per_gene --total_length --offline --format vcf`


### `--outdir_cache` {#outdir-cache}

**Type:** `string` | *Optional* | **Format:** `directory-path`

The output directory where the cache will be saved. You have to use absolute paths to storage on Cloud infrastructure.


### `--vep_out_format` {#vep-out-format}

**Type:** `string` | *Optional*

VEP output-file format.

> Sets the format of the output-file from VEP.

**Default:** `vcf`

**Allowed values:**
- `json`
- `tab`
- `vcf`


### `--bcftools_annotations` {#bcftools-annotations}

**Type:** `string` | *Optional* | **Format:** `file-path`

A vcf file containing custom annotations to be used with bcftools annotate. Needs to be bgzipped.

**Pattern:** `^\S+\.vcf\.gz$`


### `--bcftools_annotations_tbi` {#bcftools-annotations-tbi}

**Type:** `string` | *Optional* | **Format:** `file-path`

Index file for `bcftools_annotations`

**Pattern:** `^\S+\.vcf\.gz\.tbi$`


### `--bcftools_columns` {#bcftools-columns}

**Type:** `string` | *Optional*

Optional text file with list of columns to use from `bcftools_annotations`, one name per row


### `--bcftools_header_lines` {#bcftools-header-lines}

**Type:** `string` | *Optional*

Text file with the header lines of `bcftools_annotations`



## Pipeline stage options

### `--skip_baserecalibration` {#skip-baserecalibration}

**Type:** `boolean` | *Optional*

Skip the process of base recalibration steps i.e., GATK BaseRecalibrator and GATK ApplyBQSR.

> This parameter disable the base recalibration step, thus using a un-calibrated BAM file for variant calling.


### `--skip_intervallisttools` {#skip-intervallisttools}

**Type:** `boolean` | *Optional*

Skip the process of preparing interval lists for the GATK variant calling step

> This parameter disable preparing multiple interval lists to use with HaplotypeCaller module of GATK. It is recommended not to disable the step as it is required to run the variant calling correctly.


### `--skip_variantfiltration` {#skip-variantfiltration}

**Type:** `boolean` | *Optional*

Skip variant filtering of GATK

> Set this parameter if you don't want to filter any variants.


### `--skip_variantannotation` {#skip-variantannotation}

**Type:** `boolean` | *Optional*

Skip variant annotation

> Set this parameter if you don't want to run variant annotation.


### `--skip_multiqc` {#skip-multiqc}

**Type:** `boolean` | *Optional*

Skip MultiQC reports

> This parameter disable all QC reports


### `--skip_exon_bed_check` {#skip-exon-bed-check}

**Type:** `boolean` | *Optional*

Skip the check of the exon bed

> Set this parameter if you don't want to the pipeline to check and filter unknown regions in the exon bed file.



## General reference genome options

### `--igenomes_base` {#igenomes-base}

**Type:** `string` | *Optional* | **Format:** `directory-path`

The base path to the igenomes reference files

**Default:** `s3://ngi-igenomes/igenomes/`


### `--igenomes_ignore` {#igenomes-ignore}

**Type:** `boolean` | *Optional*

Do not load the iGenomes reference config.

> Do not load `igenomes.config` when running the pipeline. You may choose this option if you observe clashes between custom parameters and those supplied in `igenomes.config`. **NB** You can then run `Sarek` by specifying at least a FASTA genome file


### `--save_reference` {#save-reference}

**Type:** `boolean` | *Optional*

Save built references.

> Set this parameter, if you wish to save all computed reference files. This is useful to avoid re-computation on future runs.


### `--download_cache` {#download-cache}

**Type:** `boolean` | *Optional*

Download annotation cache.

> Set this parameter, if you wish to download annotation cache.
Using this parameter will download cache even if --snpeff_cache and --vep_cache are provided.



## Reference genome options

### `--genome` {#genome}

**Type:** `string` | *Optional*

Name of iGenomes reference.

> If using a reference genome configured in the pipeline using iGenomes, use this parameter to give the ID for the reference. This is then used to build the full paths for all required reference genome files e.g. `--genome GRCh38`.

See the [nf-core website docs](https://nf-co.re/usage/reference_genomes) for more details.

**Default:** `GRCh38`


### `--fasta` {#fasta}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to FASTA genome file.

> This parameter is *mandatory* if `--genome` is not specified.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.fn?a(sta)?(\.gz)?$`


### `--dict` {#dict}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to FASTA dictionary file.

> > **NB** If none provided, will be generated automatically from the FASTA reference. Combine with `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.dict$`


### `--fasta_fai` {#fasta-fai}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to FASTA reference index.

> > **NB** If none provided, will be generated automatically from the FASTA reference. Combine with `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.


### `--gtf` {#gtf}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to GTF annotation file.

> This parameter is *mandatory* if `--genome` is not specified.

**Pattern:** `^\S+\.gtf$`


### `--gff` {#gff}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to GFF3 annotation file.

> This parameter must be specified if `--genome` or `--gtf` are not specified.

**Pattern:** `^\S+\.gff\d?$`


### `--exon_bed` {#exon-bed}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to BED file containing exon intervals. This will be created from the GTF file if not specified.

**Pattern:** `^\S+\.bed$`


### `--read_length` {#read-length}

**Type:** `number` | *Optional*

Read length

> Specify the read length for the STAR aligner.

**Default:** `150`


### `--known_indels` {#known-indels}

**Type:** `string` | *Optional* | **Format:** `file-path-pattern`

Path to known indels file.

> If you use AWS iGenomes, this has already been set for you appropriately.


### `--known_indels_tbi` {#known-indels-tbi}

**Type:** `string` | *Optional* | **Format:** `file-path-pattern`

Path to known indels file index.

> > **NB** If none provided, will be generated automatically from the known index file, if provided. Combine with `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.


### `--dbsnp` {#dbsnp}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to dbsnp file.

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.vcf\.gz$`


### `--dbsnp_tbi` {#dbsnp-tbi}

**Type:** `string` | *Optional* | **Format:** `file-path`

Path to dbsnp index.

> > **NB** If none provided, will be generated automatically from the dbsnp file. Combine with `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.vcf\.gz\.tbi$`


### `--snpeff_db` {#snpeff-db}

**Type:** `string` | *Optional*

snpEff DB version.

> This is used to specify the database to be use to annotate with.
Alternatively databases' names can be listed with the `snpEff databases`.

If you use AWS iGenomes, this has already been set for you appropriately.


### `--vep_genome` {#vep-genome}

**Type:** `string` | *Optional*

VEP genome.

> This is used to specify the genome when looking for local cache, or cloud based cache.

If you use AWS iGenomes, this has already been set for you appropriately.


### `--vep_species` {#vep-species}

**Type:** `string` | *Optional*

VEP species.

> Alternatively species listed in Ensembl Genomes caches can be used.

If you use AWS iGenomes, this has already been set for you appropriately.


### `--vep_cache_version` {#vep-cache-version}

**Type:** `integer` | *Optional*

VEP cache version.

> Alternative cache version can be used to specify the correct Ensembl Genomes version number as these differ from the concurrent Ensembl/VEP version numbers.

If you use AWS iGenomes, this has already been set for you appropriately.


### `--feature_type` {#feature-type}

**Type:** `string` | *Optional*

Type of feature to parse from annotation file

**Default:** `exon`

**Allowed values:**
- `exon`
- `transcript`
- `gene`



## Institutional config options

### `--custom_config_version` {#custom-config-version}

**Type:** `string` | *Optional*

Git commit id for Institutional configs.

**Default:** `master`


### `--custom_config_base` {#custom-config-base}

**Type:** `string` | *Optional*

Base directory for Institutional configs.

> If you're running offline, Nextflow will not be able to fetch the institutional config files from the internet. If you don't need them, then this is not a problem. If you do need them, you should download the files from the repo and tell Nextflow where to find them with this parameter.

**Default:** `https://raw.githubusercontent.com/nf-core/configs/master`


### `--config_profile_name` {#config-profile-name}

**Type:** `string` | *Optional*

Institutional config name.


### `--config_profile_description` {#config-profile-description}

**Type:** `string` | *Optional*

Institutional config description.


### `--config_profile_contact` {#config-profile-contact}

**Type:** `string` | *Optional*

Institutional config contact information.


### `--config_profile_url` {#config-profile-url}

**Type:** `string` | *Optional*

Institutional config URL link.



## Generic options

### `--version` {#version}

**Type:** `boolean` | *Optional*

Display version and exit.


### `--publish_dir_mode` {#publish-dir-mode}

**Type:** `string` | *Optional*

Method used to save pipeline results to output directory.

> The Nextflow `publishDir` option specifies which intermediate files should be saved to the output directory. This option tells the pipeline what method should be used to move these files. See [Nextflow docs](https://www.nextflow.io/docs/latest/process.html#publishdir) for details.

**Default:** `copy`

**Allowed values:**
- `symlink`
- `rellink`
- `link`
- `copy`
- `copyNoFollow`
- `move`


### `--email` {#email}

**Type:** `string` | *Optional*

Email address for completion summary.

> Set this parameter to your e-mail address to get a summary e-mail with details of the run sent to you when the workflow exits. If set in your user config file (`~/.nextflow/config`) then you don't need to specify this on the command line for every run.

**Pattern:** `^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$`


### `--email_on_fail` {#email-on-fail}

**Type:** `string` | *Optional*

Email address for completion summary, only when pipeline fails.

> An email address to send a summary email to when the pipeline is completed - ONLY sent if the pipeline does not exit successfully.

**Pattern:** `^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$`


### `--plaintext_email` {#plaintext-email}

**Type:** `boolean` | *Optional*

Send plain-text email instead of HTML.


### `--max_multiqc_email_size` {#max-multiqc-email-size}

**Type:** `string` | *Optional*

File size limit when attaching MultiQC reports to summary emails.

**Default:** `25.MB`

**Pattern:** `^\d+(\.\d+)?\.?\s*(K|M|G|T)?B$`


### `--monochrome_logs` {#monochrome-logs}

**Type:** `boolean` | *Optional*

Do not use coloured log outputs.


### `--hook_url` {#hook-url}

**Type:** `string` | *Optional*

Incoming hook URL for messaging service

> Incoming hook URL for messaging service. Currently, MS Teams and Slack are supported.


### `--multiqc_config` {#multiqc-config}

**Type:** `string` | *Optional* | **Format:** `file-path`

Custom config file to supply to MultiQC.


### `--multiqc_logo` {#multiqc-logo}

**Type:** `string` | *Optional*

Custom logo file to supply to MultiQC. File name must also be set in the MultiQC config file


### `--multiqc_methods_description` {#multiqc-methods-description}

**Type:** `string` | *Optional*

Custom MultiQC yaml file containing HTML including a methods description.


### `--multiqc_title` {#multiqc-title}

**Type:** `string` | *Optional*

MultiQC report title. Printed as page header, used for filename if not otherwise specified.


### `--validate_params` {#validate-params}

**Type:** `boolean` | *Optional*

Boolean whether to validate parameters against the schema at runtime

**Default:** `True`


### `--modules_testdata_base_path` {#modules-testdata-base-path}

**Type:** `string` | *Optional*

Base URL or local path to location of pipeline test dataset files

**Default:** `https://raw.githubusercontent.com/nf-core/test-datasets/modules/data/`


### `--pipelines_testdata_base_path` {#pipelines-testdata-base-path}

**Type:** `string` | *Optional*

Base URL or local path to location of pipeline test dataset files

**Default:** `https://raw.githubusercontent.com/nf-core/test-datasets/rnavar/data/`


### `--trace_report_suffix` {#trace-report-suffix}

**Type:** `string` | *Optional*

Suffix to add to the trace report filename. Default is the date and time in the format yyyy-MM-dd_HH-mm-ss.


### `--help` {#help}

**Type:** `boolean` | *Optional*

Display the help message.


### `--help_full` {#help-full}

**Type:** `boolean` | *Optional*

Display the full detailed help message.


### `--show_hidden` {#show-hidden}

**Type:** `boolean` | *Optional*

Display hidden parameters in the help message (only works when --help or --help_full are provided).



---

*This pipeline was built with [Nextflow](https://nextflow.io).
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:23:12 UTC.*
