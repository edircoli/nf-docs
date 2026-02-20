# Writing docs

## Sources

Information is pulled from multiple sources (each only if available):

| Source                 | Content                                                 |
| ---------------------- | ------------------------------------------------------- |
| `README.md`            | Pipeline overview                                       |
| `nextflow_schema.json` | Typed input parameters with validation rules            |
| `nextflow.config`      | Runtime configuration defaults                          |
| Language Server        | Processes, workflows, functions with Groovydoc comments |
| `meta.yml`             | nf-core module metadata (tools, keywords, authors)      |

## Groovydoc comments

`nf-docs` reads Groovydoc-style `/** ... */` comments on processes, workflows, and functions.

```groovy
/**
 * Align reads to a reference genome using BWA MEM.
 *
 * Handles both single-end and paired-end reads automatically.
 *
 * @param reads  Tuple of sample ID and FASTQ files
 * @param index  BWA index files
 * @return       Tuple of sample ID and aligned BAM file
 */
process BWA_MEM {
    input:
    tuple val(sample_id), path(reads)
    path index

    output:
    tuple val(sample_id), path("*.bam"), emit: bam

    // ...
}
```

Supported tags: `@param`, `@return`.

## Input parameters

Input parameters are sourced from `nextflow_schema.json` (
[nf-schema](https://nextflow-io.github.io/nf-schema/latest/nextflow_schema/nextflow_schema_specification/)
format). Use `description` for a short label and `help_text` for extended detail.

```json
{
  "$defs": {
    "input_output_options": {
      "properties": {
        "input": {
          "type": "string",
          "format": "file-path",
          "description": "Path to the sample sheet",
          "help_text": "CSV file with columns: sample, fastq_1, fastq_2"
        }
      }
    }
  }
}
```
