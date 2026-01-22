"""
nf-docs: Generate API documentation for Nextflow pipelines.

This tool queries the Nextflow Language Server to extract docstrings,
type information, and structure from Nextflow pipelines, producing
documentation similar to Sphinx for Python or Javadoc.
"""

__version__ = "0.1.0"

from nf_docs.models import (
    ConfigParam,
    Function,
    Pipeline,
    PipelineInput,
    Process,
    ProcessInput,
    ProcessOutput,
    Workflow,
    WorkflowInput,
    WorkflowOutput,
)

__all__ = [
    "__version__",
    "Pipeline",
    "PipelineInput",
    "ConfigParam",
    "Workflow",
    "Process",
    "Function",
    "ProcessInput",
    "ProcessOutput",
    "WorkflowInput",
    "WorkflowOutput",
]
