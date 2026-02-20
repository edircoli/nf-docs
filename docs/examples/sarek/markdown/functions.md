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

_Defined in `main.nf:342`_

```groovy
def getGenomeAttribute(attribute)
```

### Parameters

| Name        | Description | Default |
| ----------- | ----------- | ------- |
| `attribute` | -           | -       |

## getFileSuffix {#getfilesuffix}

_Defined in `modules/nf-core/cat/cat/main.nf:75`_

```groovy
def getFileSuffix(filename)
```

### Parameters

| Name       | Description | Default |
| ---------- | ----------- | ------- |
| `filename` | -           | -       |

## addReadgroupToMeta {#addreadgrouptometa}

_Defined in `workflows/sarek/main.nf:631`_

```groovy
def addReadgroupToMeta(meta, files)
```

### Parameters

| Name    | Description | Default |
| ------- | ----------- | ------- |
| `meta`  | -           | -       |
| `files` | -           | -       |

## flowcellLaneFromFastq {#flowcelllanefromfastq}

_Defined in `workflows/sarek/main.nf:653`_

```groovy
def flowcellLaneFromFastq(path)
```

### Parameters

| Name   | Description | Default |
| ------ | ----------- | ------- |
| `path` | -           | -       |

## readFirstLineOfFastq {#readfirstlineoffastq}

_Defined in `workflows/sarek/main.nf:681`_

```groovy
def readFirstLineOfFastq(path)
```

### Parameters

| Name   | Description | Default |
| ------ | ----------- | ------- |
| `path` | -           | -       |

## checkConfigProvided {#checkconfigprovided}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:32`_

```groovy
def checkConfigProvided()
```

## checkProfileProvided {#checkprofileprovided}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:46`_

```groovy
def checkProfileProvided(nextflow_cli_args)
```

### Parameters

| Name                | Description | Default |
| ------------------- | ----------- | ------- |
| `nextflow_cli_args` | -           | -       |

## getWorkflowVersion {#getworkflowversion}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:62`_

```groovy
def getWorkflowVersion()
```

## processVersionsFromYAML {#processversionsfromyaml}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:80`_

```groovy
def processVersionsFromYAML(yaml_file)
```

### Parameters

| Name        | Description | Default |
| ----------- | ----------- | ------- |
| `yaml_file` | -           | -       |

## workflowVersionToYAML {#workflowversiontoyaml}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:89`_

```groovy
def workflowVersionToYAML()
```

## softwareVersionsToYAML {#softwareversionstoyaml}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:100`_

```groovy
def softwareVersionsToYAML(ch_versions)
```

### Parameters

| Name          | Description | Default |
| ------------- | ----------- | ------- |
| `ch_versions` | -           | -       |

## paramsSummaryMultiqc {#paramssummarymultiqc}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:107`_

```groovy
def paramsSummaryMultiqc(summary_params)
```

### Parameters

| Name             | Description | Default |
| ---------------- | ----------- | ------- |
| `summary_params` | -           | -       |

## logColours {#logcolours}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:141`_

```groovy
def logColours(monochrome_logs)
```

### Parameters

| Name              | Description | Default |
| ----------------- | ----------- | ------- |
| `monochrome_logs` | -           | -       |

## getSingleReport {#getsinglereport}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:208`_

```groovy
def getSingleReport(multiqc_reports)
```

### Parameters

| Name              | Description | Default |
| ----------------- | ----------- | ------- |
| `multiqc_reports` | -           | -       |

## completionEmail {#completionemail}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:229`_

```groovy
def completionEmail(summary_params, email, email_on_fail, plaintext_email, outdir, monochrome_logs, multiqc_report)
```

### Parameters

| Name              | Description | Default |
| ----------------- | ----------- | ------- |
| `summary_params`  | -           | -       |
| `email`           | -           | -       |
| `email_on_fail`   | -           | -       |
| `plaintext_email` | -           | -       |
| `outdir`          | -           | -       |
| `monochrome_logs` | -           | -       |
| `multiqc_report`  | -           | -       |

## completionSummary {#completionsummary}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:342`_

```groovy
def completionSummary(monochrome_logs)
```

### Parameters

| Name              | Description | Default |
| ----------------- | ----------- | ------- |
| `monochrome_logs` | -           | -       |

## imNotification {#imnotification}

_Defined in `subworkflows/nf-core/utils_nfcore_pipeline/main.nf:360`_

```groovy
def imNotification(summary_params, hook_url)
```

### Parameters

| Name             | Description | Default |
| ---------------- | ----------- | ------- |
| `summary_params` | -           | -       |
| `hook_url`       | -           | -       |

## dumpParametersToJSON {#dumpparameterstojson}

_Defined in `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:73`_

```groovy
def dumpParametersToJSON(outdir)
```

### Parameters

| Name     | Description | Default |
| -------- | ----------- | ------- |
| `outdir` | -           | -       |

## checkCondaChannels {#checkcondachannels}

_Defined in `subworkflows/nf-core/utils_nextflow_pipeline/main.nf:87`_

```groovy
def checkCondaChannels()
```

## isCloudUrl {#iscloudurl}

_Defined in `subworkflows/local/annotation_cache_initialisation/main.nf:70`_

```groovy
def isCloudUrl(cache_url)
```

### Parameters

| Name        | Description | Default |
| ----------- | ----------- | ------- |
| `cache_url` | -           | -       |

## validateInputParameters {#validateinputparameters}

_Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:248`_

```groovy
def validateInputParameters()
```

## genomeExistsError {#genomeexistserror}

_Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:254`_

```groovy
def genomeExistsError()
```

## sparkAndBam {#sparkandbam}

_Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:262`_

```groovy
def sparkAndBam()
```

## toolCitationText {#toolcitationtext}

_Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:271`_

```groovy
def toolCitationText()
```

## toolBibliographyText {#toolbibliographytext}

_Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:285`_

```groovy
def toolBibliographyText()
```

## methodsDescriptionText {#methodsdescriptiontext}

_Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:297`_

```groovy
def methodsDescriptionText(mqc_methods_yaml)
```

### Parameters

| Name               | Description | Default |
| ------------------ | ----------- | ------- |
| `mqc_methods_yaml` | -           | -       |

## retrieveInput {#retrieveinput}

_Defined in `subworkflows/local/utils_nfcore_sarek_pipeline/main.nf:338`_

```groovy
def retrieveInput(need_input, step, outdir)
```

### Parameters

| Name         | Description | Default |
| ------------ | ----------- | ------- |
| `need_input` | -           | -       |
| `step`       | -           | -       |
| `outdir`     | -           | -       |

---

_This pipeline was built with [Nextflow](https://nextflow.io). Documentation generated by
[nf-docs](https://github.com/ewels/nf-docs) v0.1.0 on 2026-01-23 17:27:10 UTC._
