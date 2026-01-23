# Functions

This page documents helper functions defined in the pipeline.

## Contents

- [getGenomeAttribute](#getgenomeattribute)
- [getFileSuffix](#getfilesuffix)
- [addReadgroupToMeta](#addreadgrouptometa)
- [flowcellLaneFromFastq](#flowcelllanefromfastq)
- [readFirstLineOfFastq](#readfirstlineoffastq)
- [checkConfigProvided](#checkconfigprovided)
- [checkProfileProvided](#checkprofileprovided)
- [getWorkflowVersion](#getworkflowversion)
- [processVersionsFromYAML](#processversionsfromyaml)
- [workflowVersionToYAML](#workflowversiontoyaml)
- [softwareVersionsToYAML](#softwareversionstoyaml)
- [paramsSummaryMultiqc](#paramssummarymultiqc)
- [logColours](#logcolours)
- [getSingleReport](#getsinglereport)
- [completionEmail](#completionemail)
- [completionSummary](#completionsummary)
- [imNotification](#imnotification)
- [dumpParametersToJSON](#dumpparameterstojson)
- [checkCondaChannels](#checkcondachannels)
- [isCloudUrl](#iscloudurl)
- [validateInputParameters](#validateinputparameters)
- [genomeExistsError](#genomeexistserror)
- [sparkAndBam](#sparkandbam)
- [toolCitationText](#toolcitationtext)
- [toolBibliographyText](#toolbibliographytext)
- [methodsDescriptionText](#methodsdescriptiontext)
- [retrieveInput](#retrieveinput)

## getGenomeAttribute {#getgenomeattribute}

*Defined in `main.nf:342`*

```groovy
def getGenomeAttribute(attribute)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `attribute` | - | - |


## getFileSuffix {#getfilesuffix}

*Defined in `modules/nf-core/cat/cat/main.nf:75`*

```groovy
def getFileSuffix(filename)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `filename` | - | - |


## addReadgroupToMeta {#addreadgrouptometa}

*Defined in `workflows/sarek/main.nf:631`*

```groovy
def addReadgroupToMeta(meta, files)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `meta` | - | - |
| `files` | - | - |


## flowcellLaneFromFastq {#flowcelllanefromfastq}

*Defined in `workflows/sarek/main.nf:653`*

```groovy
def flowcellLaneFromFastq(path)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `path` | - | - |


## readFirstLineOfFastq {#readfirstlineoffastq}

*Defined in `workflows/sarek/main.nf:681`*

```groovy
def readFirstLineOfFastq(path)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `path` | - | - |


## checkConfigProvided {#checkconfigprovided}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:32`*

```groovy
def checkConfigProvided()
```


## checkProfileProvided {#checkprofileprovided}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:46`*

```groovy
def checkProfileProvided(nextflow_cli_args)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `nextflow_cli_args` | - | - |


## getWorkflowVersion {#getworkflowversion}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:62`*

```groovy
def getWorkflowVersion()
```


## processVersionsFromYAML {#processversionsfromyaml}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:80`*

```groovy
def processVersionsFromYAML(yaml_file)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `yaml_file` | - | - |


## workflowVersionToYAML {#workflowversiontoyaml}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:89`*

```groovy
def workflowVersionToYAML()
```


## softwareVersionsToYAML {#softwareversionstoyaml}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:100`*

```groovy
def softwareVersionsToYAML(ch_versions)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `ch_versions` | - | - |


## paramsSummaryMultiqc {#paramssummarymultiqc}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:107`*

```groovy
def paramsSummaryMultiqc(summary_params)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `summary_params` | - | - |


## logColours {#logcolours}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:141`*

```groovy
def logColours(monochrome_logs)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `monochrome_logs` | - | - |


## getSingleReport {#getsinglereport}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:208`*

```groovy
def getSingleReport(multiqc_reports)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `multiqc_reports` | - | - |


## completionEmail {#completionemail}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:229`*

```groovy
def completionEmail(summary_params, email, email_on_fail, plaintext_email, outdir, monochrome_logs, multiqc_report)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `summary_params` | - | - |
| `email` | - | - |
| `email_on_fail` | - | - |
| `plaintext_email` | - | - |
| `outdir` | - | - |
| `monochrome_logs` | - | - |
| `multiqc_report` | - | - |


## completionSummary {#completionsummary}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:342`*

```groovy
def completionSummary(monochrome_logs)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `monochrome_logs` | - | - |


## imNotification {#imnotification}

*Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:360`*

```groovy
def imNotification(summary_params, hook_url)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `summary_params` | - | - |
| `hook_url` | - | - |


## dumpParametersToJSON {#dumpparameterstojson}

*Defined in `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:73`*

```groovy
def dumpParametersToJSON(outdir)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `outdir` | - | - |


## checkCondaChannels {#checkcondachannels}

*Defined in `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:87`*

```groovy
def checkCondaChannels()
```


## isCloudUrl {#iscloudurl}

*Defined in `subworkflows/local/annotation_cache_initialisation/main.nf:70`*

```groovy
def isCloudUrl(cache_url)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `cache_url` | - | - |


## validateInputParameters {#validateinputparameters}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:248`*

```groovy
def validateInputParameters()
```


## genomeExistsError {#genomeexistserror}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:254`*

```groovy
def genomeExistsError()
```


## sparkAndBam {#sparkandbam}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:262`*

```groovy
def sparkAndBam()
```


## toolCitationText {#toolcitationtext}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:271`*

```groovy
def toolCitationText()
```


## toolBibliographyText {#toolbibliographytext}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:285`*

```groovy
def toolBibliographyText()
```


## methodsDescriptionText {#methodsdescriptiontext}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:297`*

```groovy
def methodsDescriptionText(mqc_methods_yaml)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `mqc_methods_yaml` | - | - |


## retrieveInput {#retrieveinput}

*Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:338`*

```groovy
def retrieveInput(need_input, step, outdir)
```

### Parameters

| Name | Description | Default |
|------|-------------|---------|
| `need_input` | - | - |
| `step` | - | - |
| `outdir` | - | - |


---

*This pipeline was built with [Nextflow](https://nextflow.io).
Documentation generated by [nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:27:10 UTC.*
