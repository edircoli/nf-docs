# Pipeline Inputs

This page documents all input parameters for the pipeline.

## Input/output options

### `--input` {#input}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to comma-separated file containing information about the samples in the experiment.

> A design file with information about the samples in your experiment. Use this parameter to specify
> the location of the input files. It has to be a comma-separated file with a header row. See
> [usage docs](https://nf-co.re/sarek/usage#input).

If no input file is specified, sarek will attempt to locate one in the `{outdir}` directory. If no
input should be supplied, i.e. when --step is supplied or --build_only_index, then set --input false

**Pattern:** `^\S+\.(csv|tsv|yaml|yml|json)$`

### `--input_restart` {#input-restart}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Automatic retrieval for restart

**Pattern:** `^\S+\.(csv|tsv|yaml|yml|json)$`

### `--step` {#step}

**Type:** `string` | **Required**

Starting step

> The pipeline starts from this step and then runs through the possible subsequent steps.

**Default:** `mapping`

**Allowed values:**

- `mapping`
- `markduplicates`
- `prepare_recalibration`
- `recalibrate`
- `variant_calling`
- `annotate`

### `--outdir` {#outdir}

**Type:** `string` | **Required** | **Format:** `directory-path`

The output directory where the results will be saved. You have to use absolute paths to storage on
Cloud infrastructure.

## Main options

### `--split_fastq` {#split-fastq}

**Type:** `integer` | _Optional_

Specify how many reads each split of a FastQ file contains. Set 0 to turn off splitting at all.

> Use the the tool FastP to split FASTQ file by number of reads. This parallelizes across fastq file
> shards speeding up mapping. Note although the minimum value is 250 reads, if you have fewer than
> 250 reads a single FASTQ shard will still be created.

**Default:** `50000000`

### `--nucleotides_per_second` {#nucleotides-per-second}

**Type:** `integer` | _Optional_

Estimate interval size.

> Intervals are parts of the chopped up genome used to speed up preprocessing and variant calling.
> See `--intervals` for more info.

Changing this parameter, changes the number of intervals that are grouped and processed together.
Bed files from target sequencing can contain thousands or small intervals. Spinning up a new process
for each can be quite resource intensive. Instead it can be desired to process small intervals
together on larger nodes. In order to make use of this parameter, no runtime estimate can be present
in the bed file (column 5).

**Default:** `200000`

### `--intervals` {#intervals}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to target bed file in case of whole exome or targeted sequencing or intervals file.

> To speed up preprocessing and variant calling processes, the execution is parallelized across a
> reference chopped into smaller pieces.

Parts of preprocessing and variant calling are done by these intervals, the different resulting
files are then merged. This can parallelize processes, and push down wall clock time significantly.

We are aligning to the whole genome, and then run Base Quality Score Recalibration and Variant
Calling on the supplied regions.

**Whole Genome Sequencing:**

The (provided) intervals are chromosomes cut at their centromeres (so each chromosome arm processed
separately) also additional unassigned contigs.

We are ignoring the `hs37d5` contig that contains concatenated decoy sequences.

The calling intervals can be defined using a .list or a BED file. A .list file contains one interval
per line in the format `chromosome:start-end` (1-based coordinates). A BED file must be a
tab-separated text file with one interval per line. There must be at least three columns:
chromosome, start, and end (0-based coordinates). Additionally, the score column of the BED file can
be used to provide an estimate of how many seconds it will take to call variants on that interval.
The fourth column remains unused.

```
|chr1|10000|207666|NA|47.3|
```

This indicates that variant calling on the interval chr1:10001-207666 takes approximately 47.3
seconds.

The runtime estimate is used in two different ways. First, when there are multiple consecutive
intervals in the file that take little time to compute, they are processed as a single job, thus
reducing the number of processes that needs to be spawned. Second, the jobs with largest processing
time are started first, which reduces wall-clock time. If no runtime is given, a time of 200000
nucleotides per second is assumed. See `--nucleotides_per_second` on how to customize this. Actual
figures vary from 2 nucleotides/second to 30000 nucleotides/second. If you prefer, you can specify
the full path to your reference genome when you run the pipeline:

> **NB** If none provided, will be generated automatically from the FASTA reference **NB** Use
> --no_intervals to disable automatic generation.

**Targeted Sequencing:**

The recommended flow for targeted sequencing data is to use the workflow as it is, but also provide
a `BED` file containing targets for all steps using the `--intervals` option. In addition, the
parameter `--wes` should be set. It is advised to pad the variant calling regions (exons or target)
to some extent before submitting to the workflow.

The procedure is similar to whole genome sequencing, except that only BED file are accepted. See
above for formatting description. Adding every exon as an interval in case of `WES` can
generate >200K processes or jobs, much more forks, and similar number of directories in the Nextflow
work directory. These are appropriately grouped together to reduce number of processes run in
parallel (see above and `--nucleotides_per_second` for details). Furthermore, primers and/or baits
are not 100% specific, (certainly not for MHC and KIR, etc.), quite likely there going to be reads
mapping to multiple locations. If you are certain that the target is unique for your genome (all the
reads will certainly map to only one location), and aligning to the whole genome is an overkill, it
is actually better to change the reference itself.

**Pattern:** `\S+\.(bed|interval_list)$`

### `--no_intervals` {#no-intervals}

**Type:** `boolean` | _Optional_

Disable usage of intervals.

> Intervals are parts of the chopped up genome used to speed up preprocessing and variant calling.
> See `--intervals` for more info.

If `--no_intervals` is set no intervals will be taken into account for speed up or data processing.

### `--wes` {#wes}

**Type:** `boolean` | _Optional_

Enable when exome or panel data is provided.

> With this parameter flags in various tools are set for targeted sequencing data. It is recommended
> to enable for whole-exome and panel data analysis.

### `--tools` {#tools}

**Type:** `string` | _Optional_

Tools to use for contamination removal, duplicate marking, variant calling and/or for annotation.

> Multiple tools separated with commas.

**Variant Calling:**

Germline variant calling can currently be performed with the following variant callers:

- SNPs/Indels: DeepVariant, FreeBayes, GATK HaplotypeCaller, mpileup, Sentieon Haplotyper
- Structural Variants: indexcov, Manta, TIDDIT
- Copy-number: CNVKit

Tumor-only somatic variant calling can currently be performed with the following variant callers:

- SNPs/Indels: FreeBayes, Lofreq, mpileup, Mutect2, Sentieon TNScope, Strelka
- Structural Variants: Manta, Sentieon TNScope, TIDDIT
- Copy-number: CNVKit, ControlFREEC

Somatic variant calling can currently only be performed with the following variant callers:

- SNPs/Indels: FreeBayes, Mutect2, Sentieon TNScope, Strelka2
- Structural variants: Manta, TIDDIT
- Copy-Number: ASCAT, CNVKit, Control-FREEC, Sentieon TNScope
- Microsatellite Instability: MSIsensor2, MSIsensorpro

> **NB** Mutect2 for somatic variant calling cannot be combined with `--no_intervals`

**Annotation:**

- snpEff, VEP, merge (both consecutively), and bcftools annotate (needs `--bcftools_annotation`).

> **NB** As Sarek will use bgzip and tabix to compress and index VCF files annotated, it expects VCF
> files to be sorted when starting from `--step annotate`.

**Pattern:**
`^((ascat|bbsplit|bcfann|cnvkit|controlfreec|deepvariant|freebayes|haplotypecaller|indexcov|lofreq|manta|merge|mpileup|msisensor2|msisensorpro|muse|mutect2|ngscheckmate|sentieon_dedup|sentieon_dnascope|sentieon_haplotyper|sentieon_tnscope|snpeff|strelka|tiddit|vep|varlociraptor)?,?)*(?<!,)$`

### `--skip_tools` {#skip-tools}

**Type:** `string` | _Optional_

Disable specified tools.

> Multiple tools can be specified, separated by commas.

> **NB** `--skip_tools baserecalibrator_report` is actually just not saving the reports. **NB**
> `--skip_tools markduplicates_report` does not skip `MarkDuplicates` but prevent the collection of
> duplicate metrics that slows down performance.

**Pattern:**
`^((baserecalibrator|baserecalibrator_report|bcftools|dnascope_filter|documentation|fastqc|haplotypecaller_filter|haplotyper_filter|markduplicates|markduplicates_report|mosdepth|multiqc|samtools|vcftools|versions)?,?)*(?<!,)$`

## FASTQ Preprocessing

### `--trim_fastq` {#trim-fastq}

**Type:** `boolean` | _Optional_

Run FastP for read trimming

> Use this to perform adapter trimming. Adapter are detected automatically by using the FastP flag
> `--detect_adapter_for_pe`. For more info see [FastP](https://github.com/OpenGene/fastp).

### `--clip_r1` {#clip-r1}

**Type:** `integer` | _Optional_

Remove bp from the 5' end of read 1

> This may be useful if the qualities were very poor, or if there is some sort of unwanted bias at
> the 5' end. Corresponds to the FastP flag `--trim_front1`.

**Default:** `0`

### `--clip_r2` {#clip-r2}

**Type:** `integer` | _Optional_

Remove bp from the 5' end of read 2

> This may be useful if the qualities were very poor, or if there is some sort of unwanted bias at
> the 5' end. Corresponds to the FastP flag `--trim_front2`.

**Default:** `0`

### `--three_prime_clip_r1` {#three-prime-clip-r1}

**Type:** `integer` | _Optional_

Remove bp from the 3' end of read 1

> This may remove some unwanted bias from the 3'. Corresponds to the FastP flag `--trim_tail1`.

**Default:** `0`

### `--three_prime_clip_r2` {#three-prime-clip-r2}

**Type:** `integer` | _Optional_

Remove bp from the 3' end of read 2

> This may remove some unwanted bias from the 3' end. Corresponds to the FastP flag `--trim_tail2`.

**Default:** `0`

### `--trim_nextseq` {#trim-nextseq}

**Type:** `boolean` | _Optional_

Removing poly-G tails.

> DetectS polyG in read tails and trim them. Corresponds to the FastP flag `--trim_poly_g`.

### `--length_required` {#length-required}

**Type:** `integer` | _Optional_

Minimum length of reads to keep

> This is the minimum length of reads to keep after trimming. Corresponds to the FastP flag
> `--length_required` (default in FastP is 15bp).

**Default:** `15`

### `--save_trimmed` {#save-trimmed}

**Type:** `boolean` | _Optional_

Save trimmed FastQ file intermediates.

### `--save_split_fastqs` {#save-split-fastqs}

**Type:** `boolean` | _Optional_

If set, publishes split FASTQ files. Intended for testing purposes.

## Unique Molecular Identifiers

### `--umi_read_structure` {#umi-read-structure}

**Type:** `string` | _Optional_

Specify UMI read structure for fgbio UMI consensus read generation

> One structure if UMI is present on one end (i.e. '+T 2M11S+T'), or two structures separated by a
> blank space if UMIs a present on both ends (i.e. '2M11S+T 2M11S+T'); please note, this does not
> handle duplex-UMIs.

For more info on UMI usage in the pipeline, also check docs
[here](./docs/usage/#how-to-handle-umis).

### `--group_by_umi_strategy` {#group-by-umi-strategy}

**Type:** `string` | _Optional_

Default strategy for fgbio UMI-based consensus read generation

**Default:** `Adjacency`

**Allowed values:**

- `Identity`
- `Edit`
- `Adjacency`
- `Paired`

### `--umi_in_read_header` {#umi-in-read-header}

**Type:** `boolean` | _Optional_

Move UMIs from fastq read headers to a tag prior to deduplication.

> Set to true if UMIs are already present in the header of the read, for instance from using
> OverrideCycles in bclconvert or umi_tools/extract.

### `--umi_location` {#umi-location}

**Type:** `string` | _Optional_

Location of the UMI(s) to be extracted with fastp.

> Use if UMIs are not present in the read header, but in a specific location within the reads/fastq
> header index. This will be used to extract UMIs from reads or index in the fastq header and store
> them in the RX tag.

**Allowed values:**

- `read1`
- `read2`
- `per_read`
- `index1`
- `index2`
- `per_index`

### `--umi_length` {#umi-length}

**Type:** `integer` | _Optional_

Length of the UMI(s) in the read.

> If UMIs are being extracted using fastp, specify the length of the UMI here. This will be used to
> extract UMIs from reads and store them in the RX tag.

### `--umi_base_skip` {#umi-base-skip}

**Type:** `integer` | _Optional_

Number of bases to skip after the UMI(s) in the read when extracting with fastp.

> If UMIs are being extracted using fastp, specify the number of bases to skip after the UMI here.
> This will trim some bases after the UMI.

### `--umi_tag` {#umi-tag}

**Type:** `string` | _Optional_

Tag detailing where UMIs are present inside the bam/cram file (e.g. RX).

> If UMIs are already present in the cram/bam file, this details the tag which will be used in GATK
> MarkDuplicates and Sentieon dedup. This should be set to RX if restarting from bam files where the
> UMIs have been extracted by the umi_in_read_header or umi_length options. Note this is not
> compatible with MarkDuplicates Spark.

### `--bbsplit_fasta_list` {#bbsplit-fasta-list}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to comma-separated file containing a list of reference genomes to filter reads against with
BBSplit. You have to also explicitly set `--tools bbsplit` if you want to use BBSplit.

> The file should contain 2 columns: short name and full path to reference genome(s) e.g.

```
mm10,/path/to/mm10.fa
ecoli,/path/to/ecoli.fa
```

### `--bbsplit_index` {#bbsplit-index}

**Type:** `string` | _Optional_ | **Format:** `path`

Path to directory or tar.gz archive for pre-built BBSplit index.

> The BBSplit index will have to be built at least once with this pipeline (see `--save_reference`
> to save index). It can then be provided via `--bbsplit_index` for future runs.

### `--save_bbsplit_reads` {#save-bbsplit-reads}

**Type:** `boolean` | _Optional_

If this option is specified, FastQ files split by reference will be saved in the results directory.

## Preprocessing

### `--aligner` {#aligner}

**Type:** `string` | _Optional_

Specify aligner to be used to map reads to reference genome.

> Sarek will build missing indices automatically if not provided. Set `--bwa false` if indices
> should be (re-)built. If DragMap is selected as aligner, it is recommended to skip
> baserecalibration with `--skip_tools baserecalibrator`. For more info see
> [here](https://gatk.broadinstitute.org/hc/en-us/articles/4407897446939--How-to-Run-germline-single-sample-short-variant-discovery-in-DRAGEN-mode).

**Default:** `bwa-mem`

**Allowed values:**

- `bwa-mem`
- `bwa-mem2`
- `dragmap`
- `sentieon-bwamem`
- `parabricks`

### `--save_mapped` {#save-mapped}

**Type:** `boolean` | _Optional_

Save mapped files.

> If the parameter `--split-fastq` is used, the sharded bam files are merged and converted to CRAM
> before saving them.

### `--save_output_as_bam` {#save-output-as-bam}

**Type:** `boolean` | _Optional_

Saves output from mapping (if `--save_mapped`), Markduplicates & Baserecalibration as BAM file
instead of CRAM

### `--use_gatk_spark` {#use-gatk-spark}

**Type:** `string` | _Optional_

Enable usage of GATK Spark implementation for duplicate marking and/or base quality score
recalibration

> Multiple separated with commas.

> The GATK4 Base Quality Score recalibration tools `Baserecalibrator` and `ApplyBQSR` are currently
> available as Beta release. Please be aware that `--use_gatk_spark` is not compatible with
> `--save_output_as_bam --save_mapped`. Use with caution!

**Pattern:** `^((baserecalibrator|markduplicates)?,?)*(?<!,)$`

### `--markduplicates_pixel_distance` {#markduplicates-pixel-distance}

**Type:** `integer` | _Optional_

> Pixel distance for GATK MarkDuplicates.

### `--sentieon_consensus` {#sentieon-consensus}

**Type:** `boolean` | _Optional_

Generate consensus reads with Sentieon dedup rather than choosing one best read.

> If set, the Sentieon dedup output will combine duplicate reads into single consensus read. This is
> only relevant if `--tools` contains `sentieon_dedup`.

## Variant Calling

### `--only_paired_variant_calling` {#only-paired-variant-calling}

**Type:** `boolean` | _Optional_

If true, skips germline variant calling for matched normal to tumor sample. Normal samples without
matched tumor will still be processed through germline variant calling tools.

> This can speed up computation for somatic variant calling with matched normal samples. If false,
> all normal samples are processed as well through the germline variantcalling tools. If true, only
> somatic variant calling is done.

### `--ascat_min_base_qual` {#ascat-min-base-qual}

**Type:** `integer` | _Optional_

Overwrite Ascat min base quality required for a read to be counted.

> For more details see
> [here](https://raw.githubusercontent.com/VanLoo-lab/ascat/master/man/ASCAT-manual.pdf)

**Default:** `20`

### `--ascat_min_counts` {#ascat-min-counts}

**Type:** `integer` | _Optional_

Overwrite Ascat minimum depth required in the normal for a SNP to be considered.

> For more details, see
> [here](https://raw.githubusercontent.com/VanLoo-lab/ascat/master/man/ASCAT-manual.pdf).

**Default:** `10`

### `--ascat_min_map_qual` {#ascat-min-map-qual}

**Type:** `integer` | _Optional_

Overwrite Ascat min mapping quality required for a read to be counted.

> For more details, see
> [here](https://raw.githubusercontent.com/VanLoo-lab/ascat/master/man/ASCAT-manual.pdf).

**Default:** `35`

### `--ascat_ploidy` {#ascat-ploidy}

**Type:** `number` | _Optional_

Overwrite ASCAT ploidy.

> ASCAT: optional argument to override ASCAT optimization and supply psi parameter (expert
> parameter, do not adapt unless you know what you are doing). See
> [here](https://raw.githubusercontent.com/VanLoo-lab/ascat/master/man/ASCAT-manual.pdf)

### `--ascat_purity` {#ascat-purity}

**Type:** `number` | _Optional_

Overwrite ASCAT purity.

> Overwrites ASCAT's `rho_manual` parameter. Expert use only, see
> [here](https://raw.githubusercontent.com/VanLoo-lab/ascat/master/man/ASCAT-manual.pdf) for
> details. Requires that `--ascat_ploidy` is set.

### `--cf_chrom_len` {#cf-chrom-len}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Specify a custom chromosome length file.

> Control-FREEC requires a file containing all chromosome lengths. By default the fasta.fai is used.
> If the fasta.fai file contains chromosomes not present in the intervals, it fails (see:
> https://github.com/BoevaLab/FREEC/issues/106).

In this case, a custom chromosome length can be specified. It must be of the same format as the fai,
but only contain the relevant chromosomes.

**Pattern:** `^\S+\.(fai|len)$`

### `--cf_coeff` {#cf-coeff}

**Type:** `number` | _Optional_

Overwrite Control-FREEC coefficientOfVariation

> Details, see [ControlFREEC manual](http://boevalab.inf.ethz.ch/FREEC/tutorial.html).

**Default:** `0.05`

### `--cf_contamination_adjustment` {#cf-contamination-adjustment}

**Type:** `boolean` | _Optional_

Overwrite Control-FREEC contaminationAdjustement

> Details, see [ControlFREEC manual](http://boevalab.inf.ethz.ch/FREEC/tutorial.html).

### `--cf_contamination` {#cf-contamination}

**Type:** `integer` | _Optional_

Design known contamination value for Control-FREEC

> Details, see [ControlFREEC manual](http://boevalab.inf.ethz.ch/FREEC/tutorial.html).

**Default:** `0`

### `--cf_minqual` {#cf-minqual}

**Type:** `integer` | _Optional_

Minimal sequencing quality for a position to be considered in BAF analysis.

> Details, see [ControlFREEC manual](http://boevalab.inf.ethz.ch/FREEC/tutorial.html).

**Default:** `0`

### `--cf_mincov` {#cf-mincov}

**Type:** `integer` | _Optional_

Minimal read coverage for a position to be considered in BAF analysis.

> Details, see [ControlFREEC manual](http://boevalab.inf.ethz.ch/FREEC/tutorial.html).

**Default:** `0`

### `--cf_ploidy` {#cf-ploidy}

**Type:** `string` | _Optional_

Genome ploidy used by ControlFREEC

> In case of doubt, you can set different values and Control-FREEC will select the one that explains
> most observed CNAs Example: ploidy=2 , ploidy=2,3,4. For more details, see the
> [manual](http://boevalab.inf.ethz.ch/FREEC/tutorial.html).

**Default:** `2`

### `--cf_window` {#cf-window}

**Type:** `number` | _Optional_

Overwrite Control-FREEC window size.

> Details, see [ControlFREEC manual](http://boevalab.inf.ethz.ch/FREEC/tutorial.html).

### `--cnvkit_reference` {#cnvkit-reference}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Copy-number reference for CNVkit

> https://cnvkit.readthedocs.io/en/stable/pipeline.html?highlight=reference.cnn#batch

**Pattern:** `^\S+\.cnn$`

### `--freebayes_filter` {#freebayes-filter}

**Type:** `string` | _Optional_

Filtering expression for vcflib/vcffilter

> Freebayes offers a QUAL score for each called variant. The QUAL estimate provides the phred-scaled
> probability that the locus is not polymorphic provided the data and the model. This is
> reasonably-well calibrated, so you can specify that you want things where we expect error rates of
> no more than 1/100 (QUAL > 20) or 1/1000 (QUAL > 30). Where the default setting for sarek is
> QUAL > 30.

**Default:** `30`

### `--joint_germline` {#joint-germline}

**Type:** `boolean` | _Optional_

Turn on the joint germline variant calling for GATK haplotypecaller

> Uses all normal germline samples (as designated by `status` in the input csv) in the joint
> germline variant calling process.

### `--joint_mutect2` {#joint-mutect2}

**Type:** `boolean` | _Optional_

Runs Mutect2 in joint (multi-sample) mode for better concordance among variant calls of tumor
samples from the same patient. Mutect2 outputs will be stored in a subfolder named with patient ID
under `variant_calling/mutect2/` folder. Only a single normal sample per patient is allowed.
Tumor-only mode is also supported.

### `--ignore_soft_clipped_bases` {#ignore-soft-clipped-bases}

**Type:** `boolean` | _Optional_

Do not analyze soft clipped bases in the reads for GATK Mutect2.

> use the `--dont-use-soft-clipped-bases` params with GATK Mutect2.

### `--pon` {#pon}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Panel-of-normals VCF (bgzipped) for GATK Mutect2

> Without PON, there will be no calls with PASS in the INFO field, only an unfiltered VCF is
> written. It is highly recommended to make your own PON, as it depends on sequencer and library
> preparation.

The pipeline is shipped with a panel-of-normals for `--genome GATK.GRCh38` provided by
[GATK](https://gatk.broadinstitute.org/hc/en-us/articles/360035890631-Panel-of-Normals-PON-).

See
[PON documentation](https://gatk.broadinstitute.org/hc/en-us/articles/360042479112-CreateSomaticPanelOfNormals-BETA)

> **NB** PON file should be bgzipped.

**Pattern:** `^\S+\.vcf\.gz$`

### `--pon_tbi` {#pon-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Index of PON panel-of-normals VCF.

> If none provided, will be generated automatically from the PON bgzipped VCF file.

**Pattern:** `^\S+\.vcf\.gz\.tbi$`

### `--sentieon_haplotyper_emit_mode` {#sentieon-haplotyper-emit-mode}

**Type:** `string` | _Optional_

Option for selecting output and emit-mode of Sentieon's Haplotyper.

> The option `--sentieon_haplotyper_emit_mode` can be set to the same string values as the
> Haplotyper's `--emit_mode`. To output both a vcf and a gvcf, specify both a vcf-option (currently,
> `all`, `confident` and `variant`) and `gvcf`. For example, to obtain a vcf and gvcf one could set
> `--sentieon_haplotyper_emit_mode` to `variant, gvcf`.

**Default:** `variant`

**Pattern:**
`^(all|confident|gvcf|variant|gvcf,all|gvcf,confident|gvcf,variant|all,gvcf|confident,gvcf|variant,gvcf)(?<!,)$`

### `--sentieon_dnascope_emit_mode` {#sentieon-dnascope-emit-mode}

**Type:** `string` | _Optional_

Option for selecting output and emit-mode of Sentieon's Dnascope.

> The option `--sentieon_dnascope_emit_mode` can be set to the same string values as the Dnascope's
> `--emit_mode`. To output both a vcf and a gvcf, specify both a vcf-option (currently, `all`,
> `confident` and `variant`) and `gvcf`. For example, to obtain a vcf and gvcf one could set
> `--sentieon_dnascope_emit_mode` to `variant, gvcf`.

**Default:** `variant`

**Pattern:**
`^(all|confident|gvcf|variant|gvcf,all|gvcf,confident|gvcf,variant|all,gvcf|confident,gvcf|variant,gvcf)(?<!,)$`

### `--sentieon_dnascope_pcr_indel_model` {#sentieon-dnascope-pcr-indel-model}

**Type:** `string` | _Optional_

Option for selecting the PCR indel model used by Sentieon Dnascope.

> PCR indel model used to weed out false positive indels more or less aggressively. The possible
> MODELs are: NONE (used for PCR free samples), and HOSTILE, AGGRESSIVE and CONSERVATIVE, in order
> of decreasing aggressiveness. The default value is CONSERVATIVE.

**Default:** `CONSERVATIVE`

**Pattern:** `^(NONE|HOSTILE|AGGRESSIVE|CONSERVATIVE)(?<!,)$`

### `--gatk_pcr_indel_model` {#gatk-pcr-indel-model}

**Type:** `string` | _Optional_

> Option for selecting the PCR indel model used by GATK HaplotypeCaller.

**Default:** `CONSERVATIVE`

## Post variant calling

### `--filter_vcfs` {#filter-vcfs}

**Type:** `boolean` | _Optional_

Enable filtering of VCFs with bcftools view

> Filtering of all vcf-files from each applied variant-caller using bfctools filter and applying
> filtering criteria specified in --bcftools_filter_criteria.

### `--bcftools_filter_criteria` {#bcftools-filter-criteria}

**Type:** `string` | _Optional_

Filter criteria. Uses bcftools view filter options. To customize, follow instructions here:
https://samtools.github.io/bcftools/bcftools.html#view

**Default:** `-f PASS,.`

### `--normalize_vcfs` {#normalize-vcfs}

**Type:** `boolean` | _Optional_

Option for normalization of vcf-files.

> Normalization of all vcf-files from each applied variant-caller using bfctools norm.

### `--snv_consensus_calling` {#snv-consensus-calling}

**Type:** `boolean` | _Optional_

Enable consensus calling of multiple VCF files from one sample

> Intersects multiple VCF files from one sample using `bcftools isec`. As consensus criterium
> `-n+${params.snv_consensus_calling}` is used, meaning a variant is found in this many or more
> files. For details, visit: https://samtools.github.io/bcftools/bcftools.html#isec

### `--consensus_min_count` {#consensus-min-count}

**Type:** `integer` | _Optional_

Minimum number of variant callers calling a variant for consensus results

> Determines the minimum number of variant callers a variant must be called in to be included in the
> consensus results. As consensus criterium `-n+${params.consensus_min_count}` is used, meaning a
> variant is found in this many or more files. For details, visit:
> https://samtools.github.io/bcftools/bcftools.html#isec

**Default:** `2`

### `--concatenate_vcfs` {#concatenate-vcfs}

**Type:** `boolean` | _Optional_

Option for concatenating germline vcf-files.

> Enable concatenation of germline vcf-files from each applied variant-caller into one vcf-file
> using bfctools concat.

### `--varlociraptor_chunk_size` {#varlociraptor-chunk-size}

**Type:** `integer` | _Optional_

Number of chunks to split the vcf-files for varlociraptor. Minimum 1, indicates no splitting

**Default:** `15`

### `--varlociraptor_scenario_tumor_only` {#varlociraptor-scenario-tumor-only}

**Type:** `string` | _Optional_

Yte compatible scenario file for tumor only samples. Defaults to
assets/varlociraptor_tumor_only.yte.yaml

### `--varlociraptor_scenario_somatic` {#varlociraptor-scenario-somatic}

**Type:** `string` | _Optional_

Yte compatible scenario file for somatic samples. Defaults to assets/varlociraptor_somatic.yte.yaml

### `--varlociraptor_scenario_germline` {#varlociraptor-scenario-germline}

**Type:** `string` | _Optional_

Yte compatible scenario file for germline samples. Defaults to
assets/varlociraptor_germline.yte.yaml

## Annotation

### `--vep_include_fasta` {#vep-include-fasta}

**Type:** `boolean` | _Optional_

Allow usage of fasta file for annotation with VEP

> By pointing VEP to a FASTA file, it is possible to retrieve reference sequence locally. This
> enables VEP to retrieve HGVS notations (--hgvs), check the reference sequence given in input data,
> and construct transcript models from a GFF or GTF file without accessing a database.

For details, see [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_cache.html#fasta).

### `--vep_dbnsfp` {#vep-dbnsfp}

**Type:** `boolean` | _Optional_

Enable the use of the VEP dbNSFP plugin.

> For details, see
> [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html#dbnsfp).

### `--dbnsfp` {#dbnsfp}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to dbNSFP processed file.

> Will not work without a provided `dbnsfp_tbi`. To be used with `--vep_dbnsfp`. dbNSFP files and
> more information are available at
> https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html#dbnsfp and
> https://sites.google.com/site/jpopgen/dbNSFP/

**Pattern:** `^\S+\.gz$`

### `--dbnsfp_tbi` {#dbnsfp-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to dbNSFP tabix indexed file.

> To be used with `--vep_dbnsfp`.

**Pattern:** `^\S+\.vcf\.gz\.(csi|tbi)$`

### `--dbnsfp_consequence` {#dbnsfp-consequence}

**Type:** `string` | _Optional_

Consequence to annotate with

> To be used with `--vep_dbnsfp`. This params is used to filter/limit outputs to a specific effect
> of the variant. The set of consequence terms is defined by the Sequence Ontology and an overview
> of those used in VEP can be found here:
> https://www.ensembl.org/info/genome/variation/prediction/predicted_data.html If one wants to
> filter using several consequences, then separate those by using '&' (i.e.
> 'consequence=3_prime_UTR_variant&intron_variant'.

### `--dbnsfp_fields` {#dbnsfp-fields}

**Type:** `string` | _Optional_

Fields to annotate with

> To be used with `--vep_dbnsfp`. This params can be used to retrieve individual values from the
> dbNSFP file. The values correspond to the name of the columns in the dbNSFP file and are separated
> by comma. The column names might differ between the different dbNSFP versions. Please check the
> Readme.txt file, which is provided with the dbNSFP file, to obtain the correct column names. The
> Readme file contains also a short description of the provided values and the version of the tools
> used to generate them.

Default value are explained below:

rs_dbSNP - rs number from dbSNP HGVSc_VEP - HGVS coding variant presentation from VEP. Multiple
entries separated by ';', corresponds to Ensembl_transcriptid HGVSp_VEP - HGVS protein variant
presentation from VEP. Multiple entries separated by ';', corresponds to Ensembl_proteinid
1000Gp3_EAS_AF - Alternative allele frequency in the 1000Gp3 East Asian descendent samples
1000Gp3_AMR_AF - Alternative allele counts in the 1000Gp3 American descendent samples LRT_score -
Original LRT two-sided p-value (LRTori), ranges from 0 to 1 GERP++\_RS - Conservation score. The
larger the score, the more conserved the site, ranges from -12.3 to 6.17 gnomAD_exomes_AF -
Alternative allele frequency in the whole gnomAD exome samples.

**Default:**
`rs_dbSNP,HGVSc_VEP,HGVSp_VEP,1000Gp3_EAS_AF,1000Gp3_AMR_AF,LRT_score,GERP++_RS,gnomAD_exomes_AF`

### `--vep_loftee` {#vep-loftee}

**Type:** `boolean` | _Optional_

Enable the use of the VEP LOFTEE plugin.

> For details, see [here](https://github.com/konradjk/loftee).

### `--vep_spliceai` {#vep-spliceai}

**Type:** `boolean` | _Optional_

Enable the use of the VEP SpliceAI plugin.

> For details, see
> [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html#spliceai).

### `--spliceai_snv` {#spliceai-snv}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to spliceai raw scores snv file.

> To be used with `--vep_spliceai`.

**Pattern:** `^\S+\.\vcf\.gz$`

### `--spliceai_snv_tbi` {#spliceai-snv-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to spliceai raw scores snv tabix indexed file.

> To be used with `--vep_spliceai`.

**Pattern:** `^\S+\\.vcf\.gz.(csi|tbi)$`

### `--spliceai_indel` {#spliceai-indel}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to spliceai raw scores indel file.

> To be used with `--vep_spliceai`.

**Pattern:** `^\S+\.vcf\.gz$`

### `--spliceai_indel_tbi` {#spliceai-indel-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to spliceai raw scores indel tabix indexed file.

> To be used with `--vep_spliceai`.

**Pattern:** `^\S+\.vcf\.gz\.(csi|tbi)$`

### `--vep_spliceregion` {#vep-spliceregion}

**Type:** `boolean` | _Optional_

Enable the use of the VEP SpliceRegion plugin.

> For details, see
> [here](https://www.ensembl.org/info/docs/tools/vep/script/vep_plugins.html#spliceregion) and
> [here](https://www.ensembl.info/2018/10/26/cool-stuff-the-vep-can-do-splice-site-variant-annotation/).

### `--vep_custom_args` {#vep-custom-args}

**Type:** `string` | _Optional_

Add an extra custom argument to VEP.

> Using this params you can add custom args to VEP.

**Default:** `--everything --filter_common --per_gene --total_length --offline --format vcf`

### `--vep_version` {#vep-version}

**Type:** `string` | _Optional_

Should reflect the VEP version used in the container.

> Used by the loftee plugin that need the full path.

**Default:** `111.0-0`

### `--outdir_cache` {#outdir-cache}

**Type:** `string` | _Optional_ | **Format:** `directory-path`

The output directory where the cache will be saved. You have to use absolute paths to storage on
Cloud infrastructure.

### `--vep_out_format` {#vep-out-format}

**Type:** `string` | _Optional_

VEP output-file format.

> Sets the format of the output-file from VEP. Available formats: json, tab and vcf.

**Default:** `vcf`

**Allowed values:**

- `json`
- `tab`
- `vcf`

### `--bcftools_annotations` {#bcftools-annotations}

**Type:** `string` | _Optional_ | **Format:** `file-path`

A vcf file containing custom annotations to be used with bcftools annotate. Needs to be bgzipped.

**Pattern:** `^\S+\.vcf\.gz$`

### `--bcftools_annotations_tbi` {#bcftools-annotations-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Index file for `bcftools_annotations`

**Pattern:** `^\S+\.vcf\.gz\.tbi$`

### `--bcftools_columns` {#bcftools-columns}

**Type:** `string` | _Optional_

Optional text file with list of columns to use from `bcftools_annotations`, one name per row

### `--bcftools_header_lines` {#bcftools-header-lines}

**Type:** `string` | _Optional_

Text file with the header lines of `bcftools_annotations`

## General reference genome options

### `--igenomes_base` {#igenomes-base}

**Type:** `string` | _Optional_ | **Format:** `directory-path`

The base path to the igenomes reference files

**Default:** `s3://ngi-igenomes/igenomes/`

### `--igenomes_ignore` {#igenomes-ignore}

**Type:** `boolean` | _Optional_

Do not load the iGenomes reference config.

> Do not load `igenomes.config` when running the pipeline. You may choose this option if you observe
> clashes between custom parameters and those supplied in `igenomes.config`. **NB** You can then run
> `Sarek` by specifying at least a FASTA genome file

### `--save_reference` {#save-reference}

**Type:** `boolean` | _Optional_

Save built references.

> Set this parameter, if you wish to save all computed reference files. This is useful to avoid
> re-computation on future runs.

### `--build_only_index` {#build-only-index}

**Type:** `boolean` | _Optional_

Only built references.

> Set this parameter, if you wish to compute and save all computed reference files. No alignment or
> any other downstream steps will be performed.

### `--download_cache` {#download-cache}

**Type:** `boolean` | _Optional_

Download annotation cache.

> Set this parameter, if you wish to download annotation cache. Using this parameter will download
> cache even if --snpeff_cache and --vep_cache are provided.

## Reference genome options

### `--genome` {#genome}

**Type:** `string` | _Optional_

Name of iGenomes reference.

> If using a reference genome configured in the pipeline using iGenomes, use this parameter to give
> the ID for the reference. This is then used to build the full paths for all required reference
> genome files e.g. `--genome GRCh38`.

See the [nf-core website docs](https://nf-co.re/usage/reference_genomes) for more details.

**Default:** `GATK.GRCh38`

### `--ascat_genome` {#ascat-genome}

**Type:** `string` | _Optional_

ASCAT genome.

> Must be set to run ASCAT, either hg19 or hg38.

If you use AWS iGenomes, this has already been set for you appropriately.

**Allowed values:**

- `hg19`
- `hg38`

### `--ascat_alleles` {#ascat-alleles}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to ASCAT allele zip file.

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.zip$`

### `--ascat_loci` {#ascat-loci}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to ASCAT loci zip file.

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.zip$`

### `--ascat_loci_gc` {#ascat-loci-gc}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to ASCAT GC content correction file.

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.zip$`

### `--ascat_loci_rt` {#ascat-loci-rt}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to ASCAT RT (replictiming) correction file.

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.zip$`

### `--bwa` {#bwa}

**Type:** `string` | _Optional_ | **Format:** `directory-path`

Path to BWA mem indices.

> If you wish to recompute indices available on igenomes, set `--bwa false`.

> **NB** If none provided, will be generated automatically from the FASTA reference. Combine with
> `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

### `--bwamem2` {#bwamem2}

**Type:** `string` | _Optional_ | **Format:** `directory-path`

Path to bwa-mem2 mem indices.

> If you use AWS iGenomes, this has already been set for you appropriately.

If you wish to recompute indices available on igenomes, set `--bwamem2 false`.

> **NB** If none provided, will be generated automatically from the FASTA reference, if
> `--aligner bwa-mem2` is specified. Combine with `--save_reference` to save for future runs.

### `--chr_dir` {#chr-dir}

**Type:** `string` | _Optional_ | **Format:** `path`

Path to chromosomes folder used with ControLFREEC.

> If you use AWS iGenomes, this has already been set for you appropriately.

### `--dbsnp` {#dbsnp}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to dbsnp file.

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.vcf\.gz$`

### `--dbsnp_tbi` {#dbsnp-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to dbsnp index.

> > **NB** If none provided, will be generated automatically from the dbsnp file. Combine with
> > `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.vcf\.gz\.tbi$`

### `--dbsnp_vqsr` {#dbsnp-vqsr}

**Type:** `string` | _Optional_

Label string for VariantRecalibration (haplotypecaller joint variant calling).

If you use AWS iGenomes, this has already been set for you appropriately.

### `--dict` {#dict}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to FASTA dictionary file.

> > **NB** If none provided, will be generated automatically from the FASTA reference. Combine with
> > `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.dict$`

### `--dragmap` {#dragmap}

**Type:** `string` | _Optional_ | **Format:** `directory-path`

Path to dragmap indices.

> If you wish to recompute indices available on igenomes, set `--dragmap false`.

> **NB** If none provided, will be generated automatically from the FASTA reference, if
> `--aligner dragmap` is specified. Combine with `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

### `--fasta` {#fasta}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to FASTA genome file.

> This parameter is _mandatory_ if `--genome` is not specified.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.fn?a(sta)?(\.gz)?$`

### `--fasta_fai` {#fasta-fai}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to FASTA reference index.

> > **NB** If none provided, will be generated automatically from the FASTA reference. Combine with
> > `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

### `--germline_resource` {#germline-resource}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to GATK Mutect2 Germline Resource File.

> The germline resource VCF file (bgzipped and tabixed) needed by GATK4 Mutect2 is a collection of
> calls that are likely present in the sample, with allele frequencies. The AF info field must be
> present. You can find a smaller, stripped gnomAD VCF file (most of the annotation is removed and
> only calls signed by PASS are stored) in the AWS iGenomes Annotation/GermlineResource folder.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `\S+\.vcf\.gz$`

### `--germline_resource_tbi` {#germline-resource-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to GATK Mutect2 Germline Resource Index.

> > **NB** If none provided, will be generated automatically from the Germline Resource file, if
> > provided. Combine with `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `\S+\.vcf\.gz\.tbi$`

### `--known_indels` {#known-indels}

**Type:** `string` | _Optional_ | **Format:** `file-path-pattern`

Path to known indels file.

> If you use AWS iGenomes, this has already been set for you appropriately.

### `--known_indels_tbi` {#known-indels-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path-pattern`

Path to known indels file index.

> > **NB** If none provided, will be generated automatically from the known index file, if provided.
> > Combine with `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

### `--known_indels_vqsr` {#known-indels-vqsr}

**Type:** `string` | _Optional_

Label string for VariantRecalibration (haplotypecaller joint variant calling). If you use AWS
iGenomes, this has already been set for you appropriately.

### `--known_snps` {#known-snps}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to known snps file.

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.vcf\.gz$`

### `--known_snps_tbi` {#known-snps-tbi}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to known snps file snps.

> > **NB** If none provided, will be generated automatically from the known index file, if provided.
> > Combine with `--save_reference` to save for future runs.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.vcf\.gz\.tbi$`

### `--known_snps_vqsr` {#known-snps-vqsr}

**Type:** `string` | _Optional_

Label string for VariantRecalibration (haplotypecaller joint variant calling).If you use AWS
iGenomes, this has already been set for you appropriately.

### `--mappability` {#mappability}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to Control-FREEC mappability file.

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.gem$`

### `--msisensor2_models` {#msisensor2-models}

**Type:** `string` | _Optional_ | **Format:** `path`

Path to models folder used with MSIsensor2.

> If you use AWS iGenomes, this has already been set for you appropriately.

### `--msisensor2_scan` {#msisensor2-scan}

**Type:** `string` | _Optional_ | **Format:** `path`

Path to scan file used with MSIsensor2.

> If you use AWS iGenomes, this has already been set for you appropriately.

### `--msisensorpro_scan` {#msisensorpro-scan}

**Type:** `string` | _Optional_ | **Format:** `path`

Path to scan file used with MSIsensorPro.

> If you use AWS iGenomes, this has already been set for you appropriately.

### `--ngscheckmate_bed` {#ngscheckmate-bed}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Path to SNP bed file for sample checking with NGSCheckMate

> If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.bed$`

### `--sentieon_dnascope_model` {#sentieon-dnascope-model}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Machine learning model for Sentieon Dnascope.

> It is recommended to use DNAscope with a machine learning model to perform variant calling with
> higher accuracy by improving the candidate detection and filtering. Sentieon can provide you with
> a model trained using a subset of the data from the GiAB truth-set found in
> https://github.com/genome-in-a-bottle. In addition, Sentieon can assist you in the creation of
> models using your own data, which will calibrate the specifics of your sequencing and
> bio-informatics processing.

If you use AWS iGenomes, this has already been set for you appropriately.

**Pattern:** `^\S+\.model$`

### `--snpeff_cache` {#snpeff-cache}

**Type:** `string` | _Optional_ | **Format:** `directory-path`

Path to snpEff cache.

> Path to snpEff cache which should contain the relevant genome and build directory in the path
> ${snpeff_species}.${snpeff_version}

If you use AWS iGenomes, this has already been set for you appropriately.

**Default:** `s3://annotation-cache/snpeff_cache/`

### `--snpeff_db` {#snpeff-db}

**Type:** `string` | _Optional_

snpEff DB version.

> This is used to specify the database to be use to annotate with. Alternatively databases' names
> can be listed with the `snpEff databases`.

If you use AWS iGenomes, this has already been set for you appropriately.

### `--vep_cache` {#vep-cache}

**Type:** `string` | _Optional_ | **Format:** `directory-path`

Path to VEP cache.

> Path to VEP cache which should contain the relevant species, genome and build directories at the
> path ${vep_species}/${vep*genome}*${vep_cache_version}

If you use AWS iGenomes, this has already been set for you appropriately.

**Default:** `s3://annotation-cache/vep_cache/`

### `--vep_cache_version` {#vep-cache-version}

**Type:** `string` | _Optional_

VEP cache version.

> Alternative cache version can be used to specify the correct Ensembl Genomes version number as
> these differ from the concurrent Ensembl/VEP version numbers.

If you use AWS iGenomes, this has already been set for you appropriately.

### `--vep_genome` {#vep-genome}

**Type:** `string` | _Optional_

VEP genome.

> This is used to specify the genome when looking for local cache, or cloud based cache.

If you use AWS iGenomes, this has already been set for you appropriately.

### `--vep_species` {#vep-species}

**Type:** `string` | _Optional_

VEP species.

> Alternatively species listed in Ensembl Genomes caches can be used.

If you use AWS iGenomes, this has already been set for you appropriately.

## Institutional config options

### `--custom_config_version` {#custom-config-version}

**Type:** `string` | _Optional_

Git commit id for Institutional configs.

**Default:** `master`

### `--custom_config_base` {#custom-config-base}

**Type:** `string` | _Optional_

Base directory for Institutional configs.

> If you're running offline, Nextflow will not be able to fetch the institutional config files from
> the internet. If you don't need them, then this is not a problem. If you do need them, you should
> download the files from the repo and tell Nextflow where to find them with this parameter.

**Default:** `https://raw.githubusercontent.com/nf-core/configs/master`

### `--config_profile_name` {#config-profile-name}

**Type:** `string` | _Optional_

Institutional config name.

### `--config_profile_description` {#config-profile-description}

**Type:** `string` | _Optional_

Institutional config description.

### `--config_profile_contact` {#config-profile-contact}

**Type:** `string` | _Optional_

Institutional config contact information.

### `--config_profile_url` {#config-profile-url}

**Type:** `string` | _Optional_

Institutional config URL link.

### `--test_data_base` {#test-data-base}

**Type:** `string` | _Optional_

Base path / URL for data used in the test profiles

> Warning: The `-profile test` samplesheet file itself contains remote paths. Setting this parameter
> does not alter the contents of that file.

**Default:** `https://raw.githubusercontent.com/nf-core/test-datasets/sarek3`

### `--modules_testdata_base_path` {#modules-testdata-base-path}

**Type:** `string` | _Optional_

Base path / URL for data used in the modules

### `--seq_center` {#seq-center}

**Type:** `string` | _Optional_

Sequencing center information to be added to read group (CN field).

### `--seq_platform` {#seq-platform}

**Type:** `string` | _Optional_

Sequencing platform information to be added to read group (PL field).

> Default: ILLUMINA. Will be used to create a proper header for further GATK4 downstream analysis.

**Default:** `ILLUMINA`

## Generic options

### `--version` {#version}

**Type:** `boolean` | _Optional_

Display version and exit.

### `--publish_dir_mode` {#publish-dir-mode}

**Type:** `string` | _Optional_

Method used to save pipeline results to output directory.

> The Nextflow `publishDir` option specifies which intermediate files should be saved to the output
> directory. This option tells the pipeline what method should be used to move these files. See
> [Nextflow docs](https://www.nextflow.io/docs/latest/process.html#publishdir) for details.

**Default:** `copy`

**Allowed values:**

- `symlink`
- `rellink`
- `link`
- `copy`
- `copyNoFollow`
- `move`

### `--email` {#email}

**Type:** `string` | _Optional_

Email address for completion summary.

> Set this parameter to your e-mail address to get a summary e-mail with details of the run sent to
> you when the workflow exits. If set in your user config file (`~/.nextflow/config`) then you don't
> need to specify this on the command line for every run.

**Pattern:** `^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$`

### `--email_on_fail` {#email-on-fail}

**Type:** `string` | _Optional_

Email address for completion summary, only when pipeline fails.

> An email address to send a summary email to when the pipeline is completed - ONLY sent if the
> pipeline does not exit successfully.

**Pattern:** `^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$`

### `--plaintext_email` {#plaintext-email}

**Type:** `boolean` | _Optional_

Send plain-text email instead of HTML.

### `--max_multiqc_email_size` {#max-multiqc-email-size}

**Type:** `string` | _Optional_

File size limit when attaching MultiQC reports to summary emails.

**Default:** `25.MB`

**Pattern:** `^\d+(\.\d+)?\.?\s*(K|M|G|T)?B$`

### `--monochrome_logs` {#monochrome-logs}

**Type:** `boolean` | _Optional_

Do not use coloured log outputs.

### `--hook_url` {#hook-url}

**Type:** `string` | _Optional_

Incoming hook URL for messaging service

> Incoming hook URL for messaging service. Currently, MS Teams and Slack are supported.

### `--multiqc_title` {#multiqc-title}

**Type:** `string` | _Optional_

MultiQC report title. Printed as page header, used for filename if not otherwise specified.

### `--multiqc_config` {#multiqc-config}

**Type:** `string` | _Optional_ | **Format:** `file-path`

Custom config file to supply to MultiQC.

### `--multiqc_logo` {#multiqc-logo}

**Type:** `string` | _Optional_

Custom logo file to supply to MultiQC. File name must also be set in the MultiQC config file

### `--multiqc_methods_description` {#multiqc-methods-description}

**Type:** `string` | _Optional_

Custom MultiQC yaml file containing HTML including a methods description.

### `--validate_params` {#validate-params}

**Type:** `boolean` | _Optional_

Boolean whether to validate parameters against the schema at runtime

**Default:** `True`

### `--pipelines_testdata_base_path` {#pipelines-testdata-base-path}

**Type:** `string` | _Optional_

Base URL or local path to location of pipeline test dataset files

**Default:** `https://raw.githubusercontent.com/nf-core/test-datasets/`

### `--trace_report_suffix` {#trace-report-suffix}

**Type:** `string` | _Optional_

Suffix to add to the trace report filename. Default is the date and time in the format
yyyy-MM-dd_HH-mm-ss.

### `--help` {#help}

**Type:** `boolean` | _Optional_

Display the help message.

### `--help_full` {#help-full}

**Type:** `boolean` | _Optional_

Display the full detailed help message.

### `--show_hidden` {#show-hidden}

**Type:** `boolean` | _Optional_

Display hidden parameters in the help message (only works when --help or --help_full are provided).

---

_This pipeline was built with [Nextflow](https://nextflow.io). Documentation generated by
[nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:27:10 UTC._
