"""Tests for data models."""

from nf_docs.models import (
    ConfigParam,
    Function,
    FunctionParam,
    Pipeline,
    PipelineInput,
    PipelineMetadata,
    Process,
    ProcessInput,
    ProcessOutput,
    Workflow,
    WorkflowInput,
    WorkflowOutput,
)


class TestProcessInput:
    def test_creation(self):
        inp = ProcessInput(name="reads", type="path", description="Input reads")
        assert inp.name == "reads"
        assert inp.type == "path"
        assert inp.description == "Input reads"

    def test_to_dict(self):
        inp = ProcessInput(name="reads", type="path", description="Input reads", qualifier="file")
        data = inp.to_dict()
        assert data["name"] == "reads"
        assert data["type"] == "path"
        assert data["description"] == "Input reads"
        assert data["qualifier"] == "file"


class TestProcessOutput:
    def test_creation(self):
        out = ProcessOutput(name="*.bam", type="path", emit="bam")
        assert out.name == "*.bam"
        assert out.type == "path"
        assert out.emit == "bam"

    def test_to_dict(self):
        out = ProcessOutput(name="*.bam", type="path", emit="bam", description="BAM output")
        data = out.to_dict()
        assert data["name"] == "*.bam"
        assert data["emit"] == "bam"


class TestProcess:
    def test_creation(self):
        process = Process(
            name="BWA_MEM",
            docstring="Align reads",
            file="main.nf",
            line=10,
        )
        assert process.name == "BWA_MEM"
        assert process.docstring == "Align reads"

    def test_with_inputs_outputs(self):
        process = Process(
            name="BWA_MEM",
            inputs=[ProcessInput(name="reads", type="path")],
            outputs=[ProcessOutput(name="*.bam", type="path", emit="bam")],
        )
        assert len(process.inputs) == 1
        assert len(process.outputs) == 1

    def test_to_dict(self):
        process = Process(
            name="BWA_MEM",
            docstring="Align reads",
            inputs=[ProcessInput(name="reads", type="path")],
            directives={"cpus": 8, "memory": "16.GB"},
        )
        data = process.to_dict()
        assert data["name"] == "BWA_MEM"
        assert data["directives"]["cpus"] == 8
        assert len(data["inputs"]) == 1


class TestWorkflow:
    def test_creation(self):
        workflow = Workflow(name="MAIN", is_entry=True)
        assert workflow.name == "MAIN"
        assert workflow.is_entry is True

    def test_with_calls(self):
        workflow = Workflow(
            name="ANALYSIS",
            calls=["FASTQC", "BWA_MEM", "SAMTOOLS_SORT"],
        )
        assert len(workflow.calls) == 3
        assert "FASTQC" in workflow.calls

    def test_to_dict(self):
        workflow = Workflow(
            name="ANALYSIS",
            docstring="Main workflow",
            inputs=[WorkflowInput(name="reads")],
            outputs=[WorkflowOutput(name="bam")],
            calls=["FASTQC"],
        )
        data = workflow.to_dict()
        assert data["name"] == "ANALYSIS"
        assert len(data["inputs"]) == 1
        assert len(data["calls"]) == 1


class TestFunction:
    def test_creation(self):
        func = Function(name="parseInput", docstring="Parse input file")
        assert func.name == "parseInput"

    def test_with_params(self):
        func = Function(
            name="parseInput",
            params=[
                FunctionParam(name="path", type="string"),
                FunctionParam(name="format", default="csv"),
            ],
        )
        assert len(func.params) == 2

    def test_to_dict(self):
        func = Function(
            name="parseInput",
            params=[FunctionParam(name="path")],
            return_description="Parsed data",
        )
        data = func.to_dict()
        assert data["name"] == "parseInput"
        assert data["return_description"] == "Parsed data"


class TestPipelineInput:
    def test_creation(self):
        inp = PipelineInput(
            name="input",
            type="string",
            description="Input samplesheet",
            required=True,
        )
        assert inp.name == "input"
        assert inp.required is True

    def test_to_dict_minimal(self):
        inp = PipelineInput(name="input", type="string")
        data = inp.to_dict()
        assert "name" in data
        assert "type" in data
        assert "help_text" not in data  # Not included when empty

    def test_to_dict_full(self):
        inp = PipelineInput(
            name="genome",
            type="string",
            description="Reference genome",
            help_text="Choose from GRCh37 or GRCh38",
            enum=["GRCh37", "GRCh38"],
            default="GRCh38",
            group="Reference",
        )
        data = inp.to_dict()
        assert data["enum"] == ["GRCh37", "GRCh38"]
        assert data["default"] == "GRCh38"
        assert data["group"] == "Reference"


class TestConfigParam:
    def test_creation(self):
        param = ConfigParam(name="max_cpus", type="integer", default=16)
        assert param.name == "max_cpus"
        assert param.default == 16

    def test_to_dict(self):
        param = ConfigParam(
            name="max_cpus",
            type="integer",
            description="Maximum CPUs",
            default=16,
        )
        data = param.to_dict()
        assert data["name"] == "max_cpus"
        assert data["default"] == 16


class TestPipeline:
    def test_creation(self):
        pipeline = Pipeline()
        assert pipeline.metadata is not None
        assert pipeline.inputs == []
        assert pipeline.processes == []

    def test_to_dict(self):
        pipeline = Pipeline(
            metadata=PipelineMetadata(name="test", version="1.0.0"),
            inputs=[PipelineInput(name="input", type="string")],
            processes=[Process(name="TEST")],
        )
        data = pipeline.to_dict()
        assert data["pipeline"]["name"] == "test"
        assert len(data["inputs"]) == 1
        assert len(data["processes"]) == 1

    def test_get_input_groups(self):
        pipeline = Pipeline(
            inputs=[
                PipelineInput(name="input", type="string", group="Input/output"),
                PipelineInput(name="outdir", type="string", group="Input/output"),
                PipelineInput(name="genome", type="string", group="Reference"),
            ]
        )
        groups = pipeline.get_input_groups()
        assert "Input/output" in groups
        assert "Reference" in groups
        assert len(groups["Input/output"]) == 2

    def test_get_process_by_name(self):
        pipeline = Pipeline(
            processes=[
                Process(name="FASTQC"),
                Process(name="BWA_MEM"),
            ]
        )
        proc = pipeline.get_process_by_name("BWA_MEM")
        assert proc is not None
        assert proc.name == "BWA_MEM"

        proc = pipeline.get_process_by_name("NONEXISTENT")
        assert proc is None

    def test_get_workflow_by_name(self):
        pipeline = Pipeline(
            workflows=[
                Workflow(name="MAIN", is_entry=True),
                Workflow(name="ANALYSIS"),
            ]
        )
        wf = pipeline.get_workflow_by_name("ANALYSIS")
        assert wf is not None
        assert wf.name == "ANALYSIS"

    def test_get_entry_workflow(self):
        pipeline = Pipeline(
            workflows=[
                Workflow(name="ANALYSIS"),
                Workflow(name="MAIN", is_entry=True),
            ]
        )
        entry = pipeline.get_entry_workflow()
        assert entry is not None
        assert entry.name == "MAIN"
