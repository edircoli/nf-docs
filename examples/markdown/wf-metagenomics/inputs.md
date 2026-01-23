# Pipeline Inputs

This page documents all input parameters for the pipeline.

## Other

### `--aws_image_prefix` {#aws-image-prefix}

**Type:** `string` | *Optional*


### `--aws_queue` {#aws-queue}

**Type:** `string` | *Optional*


### `--monochrome_logs` {#monochrome-logs}

**Type:** `boolean` | *Optional*


### `--validate_params` {#validate-params}

**Type:** `boolean` | *Optional*

**Default:** `True`


### `--show_hidden_params` {#show-hidden-params}

**Type:** `boolean` | *Optional*



## Input Options

### `--fastq` {#fastq}

**Type:** `string` | *Optional* | **Format:** `path`

FASTQ files to use in the analysis.

> This accepts one of three cases: (i) the path to a single FASTQ file; (ii) the path to a top-level directory containing FASTQ files; (iii) the path to a directory containing one level of sub-directories which in turn contain FASTQ files. In the first and second case, a sample name can be supplied with `--sample`. In the last case, the data is assumed to be multiplexed with the names of the sub-directories as barcodes. In this case, a sample sheet can be provided with `--sample_sheet`.


### `--bam` {#bam}

**Type:** `string` | *Optional* | **Format:** `path`

BAM or unaligned BAM (uBAM) files to use in the analysis.

> This accepts one of three cases: (i) the path to a single BAM file; (ii) the path to a top-level directory containing BAM files; (iii) the path to a directory containing one level of sub-directories which in turn contain BAM files. In the first and second case, a sample name can be supplied with `--sample`. In the last case, the data is assumed to be multiplexed with the names of the sub-directories as barcodes. In this case, a sample sheet can be provided with `--sample_sheet`.


### `--classifier` {#classifier}

**Type:** `string` | *Optional*

Kraken2 or Minimap2 workflow to be used for classification of reads.

> Use Kraken2 for fast classification and minimap2 for finer resolution, see Readme for further info.

**Default:** `kraken2`

**Allowed values:**
- `kraken2`
- `minimap2`


### `--analyse_unclassified` {#analyse-unclassified}

**Type:** `boolean` | *Optional*

Analyse unclassified reads from input directory. By default the workflow will not process reads in the unclassified directory.

> If selected and if the input is a multiplex directory the workflow will also process the unclassified directory.

**Default:** `False`


### `--exclude_host` {#exclude-host}

**Type:** `string` | *Optional* | **Format:** `file-path`

A FASTA or MMI file of the host reference. Reads that align with this reference will be excluded from the analysis.



## Sample Options

### `--sample_sheet` {#sample-sheet}

**Type:** `string` | *Optional* | **Format:** `file-path`

A CSV file used to map barcodes to sample aliases. The sample sheet can be provided when the input data is a directory containing sub-directories with FASTQ files.

> The sample sheet is a CSV file with, minimally, columns named `barcode`,`alias`. Extra columns are allowed. A `type` column is required for certain workflows and should have the following values; `test_sample`, `positive_control`, `negative_control`, `no_template_control`.


### `--sample` {#sample}

**Type:** `string` | *Optional*

A single sample name for non-multiplexed data. Permissible if passing a single .fastq(.gz) file or directory of .fastq(.gz) files.



## Reference Options

### `--database_set` {#database-set}

**Type:** `string` | *Optional*

Sets the reference, databases and taxonomy datasets that will be used for classifying reads. Choices: ['ncbi_16s_18s','ncbi_16s_18s_28s_ITS', 'SILVA_138_1', 'Greengenes2_plus', 'Standard-8', 'PlusPF-8', 'PlusPFP-8']. Memory requirement will be slightly higher than the size of the database. Standard-8, PlusPF-8 and PlusPFP-8 databases require more than 8GB and are only available in the kraken2 approach.

> This setting is overridable by providing an explicit taxonomy, database or reference path in the other reference options.

**Default:** `Standard-8`

**Allowed values:**
- `ncbi_16s_18s`
- `ncbi_16s_18s_28s_ITS`
- `SILVA_138_1`
- `Greengenes2_plus`
- `Standard-8`
- `PlusPF-8`
- `PlusPFP-8`


### `--store_dir` {#store-dir}

**Type:** `string` | *Optional* | **Format:** `directory-path`

Where to store initial download of database.

> database set selected will be downloaded as part of the workflow and saved in this location, on subsequent runs it will use this as the database. 

**Default:** `store_dir`


### `--database` {#database}

**Type:** `string` | *Optional* | **Format:** `path`

Not required but can be used to specifically override Kraken2 database [.tar.gz or Directory].

> By default uses database chosen in database_set parameter.


### `--taxonomy` {#taxonomy}

**Type:** `string` | *Optional* | **Format:** `path`

Not required but can be used to specifically override taxonomy database. Change the default to use a different taxonomy file  [.tar.gz or directory].

> By default NCBI taxonomy file will be downloaded and used.


### `--reference` {#reference}

**Type:** `string` | *Optional* | **Format:** `file-path`

Override the FASTA reference file selected by the database_set parameter. It can be a FASTA format reference sequence collection or a minimap2 MMI format index.

> This option should be used in conjunction with the database parameter to specify a custom database.


### `--ref2taxid` {#ref2taxid}

**Type:** `string` | *Optional* | **Format:** `file-path`

Not required but can be used to specify a  ref2taxid mapping. Format is .tsv (refname  taxid), no header row.

> By default uses ref2taxid for option chosen in database_set parameter.


### `--taxonomic_rank` {#taxonomic-rank}

**Type:** `string` | *Optional*

Returns results at the taxonomic rank chosen. In the Kraken2 pipeline: set the level that Bracken will estimate abundance at. Default: S (species). Other possible options are P (phylum), C (class), O (order), F (family), and G (genus).

**Default:** `S`

**Allowed values:**
- `S`
- `G`
- `F`
- `O`
- `C`
- `P`



## Kraken2 Options

### `--bracken_length` {#bracken-length}

**Type:** `integer` | *Optional*

Set the length value Bracken will use

> Should be set to the length used to generate the kmer distribution file supplied in the Kraken database input directory. For the default datasets these will be set automatically. ncbi_16s_18s = 1000 , ncbi_16s_18s_28s_ITS = 1000 , PlusPF-8 = 300


### `--bracken_threshold` {#bracken-threshold}

**Type:** `integer` | *Optional*

Set the minimum read threshold Bracken will use to consider a taxon

> Bracken will only consider taxa with a read count greater than or equal to this value.

**Default:** `10`


### `--kraken2_memory_mapping` {#kraken2-memory-mapping}

**Type:** `boolean` | *Optional*

Avoids loading database into RAM

> Kraken 2 will by default load the database into process-local RAM; this flag will avoid doing so. It may be useful if the available RAM memory is lower than the size of the chosen database.

**Default:** `False`


### `--kraken2_confidence` {#kraken2-confidence}

**Type:** `number` | *Optional*

Kraken2 Confidence score threshold. Default: 0.0. Valid interval: 0-1

> Apply a threshold to determine if a sequence is classified or unclassified. See the [kraken2 manual section on confidence scoring](https://github.com/DerrickWood/kraken2/wiki/Manual#confidence-scoring) for further details about how it works.

**Default:** `0.0`



## Minimap2 Options

### `--minimap2filter` {#minimap2filter}

**Type:** `string` | *Optional*

Filter output of minimap2 by taxids inc. child nodes, E.g. "9606,1404"

> Provide a list of taxids if you are only interested in certain ones in your minimap2 analysis outputs.


### `--minimap2exclude` {#minimap2exclude}

**Type:** `boolean` | *Optional*

Invert minimap2filter and exclude the given taxids instead

> Exclude a list of taxids from analysis outputs.

**Default:** `False`


### `--keep_bam` {#keep-bam}

**Type:** `boolean` | *Optional*

Copy bam files into the output directory.

**Default:** `False`


### `--minimap2_by_reference` {#minimap2-by-reference}

**Type:** `boolean` | *Optional*

Add a table with the mean sequencing depth per reference, standard deviation and coefficient of variation. It adds a scatterplot of the sequencing depth vs. the coverage and a heatmap showing the depth per percentile to the report

**Default:** `False`


### `--min_percent_identity` {#min-percent-identity}

**Type:** `number` | *Optional*

Minimum percentage of identity with the matched reference to define a sequence as classified; sequences with a value lower than this are defined as unclassified.

**Default:** `90`


### `--min_ref_coverage` {#min-ref-coverage}

**Type:** `number` | *Optional*

Minimum coverage value to define a sequence as classified; sequences with a coverage value lower than this are defined as unclassified. Use this option if you expect reads whose lengths are similar to the references' lengths.

**Default:** `0`



## Antimicrobial Resistance Options

### `--amr` {#amr}

**Type:** `boolean` | *Optional*

Scan reads for antimicrobial resistance or virulence genes

> Reads will be scanned using abricate and the chosen database (`--amr_db`) to identify any acquired antimicrobial resistance or virulence genes found present in the dataset. NOTE: It cannot identify mutational resistance genes.

**Default:** `False`


### `--amr_db` {#amr-db}

**Type:** `string` | *Optional*

Database of antimicrobial resistance or virulence genes to use.

**Default:** `resfinder`

**Allowed values:**
- `resfinder`
- `ecoli_vf`
- `plasmidfinder`
- `card`
- `argannot`
- `vfdb`
- `ncbi`
- `megares`
- `ecoh`


### `--amr_minid` {#amr-minid}

**Type:** `integer` | *Optional*

Threshold of required identity to report a match between a gene in the database and fastq reads. Valid interval: 0-100

**Default:** `80`


### `--amr_mincov` {#amr-mincov}

**Type:** `integer` | *Optional*

Minimum coverage (breadth-of) threshold required to report a match between a gene in the database and fastq reads. Valid interval: 0-100.

**Default:** `80`



## Report Options

### `--abundance_threshold` {#abundance-threshold}

**Type:** `number` | *Optional*

Remove those taxa whose abundance is equal or lower than the chosen value.

> To remove taxa with abundances lower than or equal to a relative value (compared to the total number of reads) use a decimal between 0-1 (1 not inclusive). To remove taxa with abundances lower than or equal to an absolute value, provide a number larger or equal to 1.

**Default:** `0`


### `--n_taxa_barplot` {#n-taxa-barplot}

**Type:** `integer` | *Optional*

Number of most abundant taxa to be displayed in the barplot. The rest of taxa will be grouped under the "Other" category.

**Default:** `9`



## Output Options

### `--out_dir` {#out-dir}

**Type:** `string` | *Optional* | **Format:** `directory-path`

Directory for output of all user-facing files.

**Default:** `output`


### `--igv` {#igv}

**Type:** `boolean` | *Optional*

Enable IGV visualisation in the EPI2ME Desktop Application by creating the required files. This will cause the workflow to emit the BAM files as well. If using a custom reference, this must be a FASTA file and not a minimap2 MMI format index.

**Default:** `False`


### `--include_read_assignments` {#include-read-assignments}

**Type:** `boolean` | *Optional*

A per sample TSV file that indicates the taxonomy assigned to each sequence.

**Default:** `False`


### `--output_unclassified` {#output-unclassified}

**Type:** `boolean` | *Optional*

Output a FASTQ of the unclassified reads.

**Default:** `False`



## Advanced Options

### `--min_len` {#min-len}

**Type:** `integer` | *Optional*

Specify read length lower limit.

> Any reads shorter than this limit will not be included in the analysis.

**Default:** `0`


### `--min_read_qual` {#min-read-qual}

**Type:** `number` | *Optional*

Specify read quality lower limit.

> Any reads with a quality lower than this limit will not be included in the analysis.


### `--max_len` {#max-len}

**Type:** `integer` | *Optional*

Specify read length upper limit

> Any reads longer than this limit will not be included in the analysis.


### `--threads` {#threads}

**Type:** `integer` | *Optional*

Maximum number of CPU threads to use in each parallel workflow task.

> Several tasks in this workflow benefit from using multiple CPU threads. This option sets the number of CPU threads for all such processes.

**Default:** `4`



## Miscellaneous Options

### `--disable_ping` {#disable-ping}

**Type:** `boolean` | *Optional*

Enable to prevent sending a workflow ping.

**Default:** `False`


### `--help` {#help}

**Type:** `boolean` | *Optional*

**Default:** `False`


### `--version` {#version}

**Type:** `boolean` | *Optional*

Display version and exit.

**Default:** `False`



---

*This pipeline was built with [Nextflow](https://nextflow.io).
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:27:31 UTC.*
