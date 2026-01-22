"""
HTML renderer for nf-docs.

Outputs pipeline documentation as a self-contained static HTML site.
"""

from pathlib import Path

from jinja2 import Environment, BaseLoader

from nf_docs.models import Pipeline
from nf_docs.renderers.base import BaseRenderer


# Self-contained HTML template
HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        :root {
            --primary-color: #0ea5e9;
            --primary-dark: #0284c7;
            --bg-color: #f8fafc;
            --text-color: #1e293b;
            --border-color: #e2e8f0;
            --code-bg: #f1f5f9;
            --sidebar-width: 280px;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: var(--bg-color);
        }

        .container {
            display: flex;
            min-height: 100vh;
        }

        /* Sidebar */
        .sidebar {
            width: var(--sidebar-width);
            background: white;
            border-right: 1px solid var(--border-color);
            padding: 2rem 1rem;
            position: fixed;
            height: 100vh;
            overflow-y: auto;
        }

        .sidebar h1 {
            font-size: 1.25rem;
            color: var(--primary-color);
            margin-bottom: 0.5rem;
        }

        .sidebar .version {
            font-size: 0.875rem;
            color: #64748b;
            margin-bottom: 1.5rem;
        }

        .sidebar nav ul {
            list-style: none;
        }

        .sidebar nav > ul > li {
            margin-bottom: 1rem;
        }

        .sidebar nav a {
            color: var(--text-color);
            text-decoration: none;
            display: block;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            transition: background 0.2s;
        }

        .sidebar nav a:hover {
            background: var(--code-bg);
        }

        .sidebar nav a.active {
            background: var(--primary-color);
            color: white;
        }

        .sidebar .section-title {
            font-weight: 600;
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #64748b;
            margin-bottom: 0.5rem;
        }

        .sidebar .nested {
            margin-left: 1rem;
            font-size: 0.875rem;
        }

        /* Main content */
        .main {
            margin-left: var(--sidebar-width);
            flex: 1;
            padding: 2rem 3rem;
            max-width: 900px;
        }

        .main h1 {
            font-size: 2rem;
            margin-bottom: 1rem;
            color: var(--text-color);
        }

        .main h2 {
            font-size: 1.5rem;
            margin-top: 2rem;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid var(--border-color);
        }

        .main h3 {
            font-size: 1.25rem;
            margin-top: 1.5rem;
            margin-bottom: 0.75rem;
        }

        .main p {
            margin-bottom: 1rem;
        }

        .main a {
            color: var(--primary-color);
            text-decoration: none;
        }

        .main a:hover {
            text-decoration: underline;
        }

        /* Code */
        code {
            background: var(--code-bg);
            padding: 0.125rem 0.375rem;
            border-radius: 4px;
            font-family: 'SF Mono', 'Fira Code', monospace;
            font-size: 0.875em;
        }

        pre {
            background: #1e293b;
            color: #e2e8f0;
            padding: 1rem;
            border-radius: 8px;
            overflow-x: auto;
            margin-bottom: 1rem;
        }

        pre code {
            background: none;
            padding: 0;
            color: inherit;
        }

        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 1rem;
        }

        th, td {
            text-align: left;
            padding: 0.75rem;
            border-bottom: 1px solid var(--border-color);
        }

        th {
            background: var(--code-bg);
            font-weight: 600;
        }

        tr:hover {
            background: var(--code-bg);
        }

        /* Badges */
        .badge {
            display: inline-block;
            padding: 0.125rem 0.5rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: 500;
        }

        .badge-required {
            background: #fee2e2;
            color: #dc2626;
        }

        .badge-optional {
            background: #e0f2fe;
            color: #0284c7;
        }

        .badge-type {
            background: #f3e8ff;
            color: #7c3aed;
        }

        .badge-entry {
            background: #dcfce7;
            color: #16a34a;
        }

        /* Cards */
        .card {
            background: white;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
        }

        .card-header {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 0.5rem;
        }

        .card-title {
            font-weight: 600;
            font-size: 1rem;
        }

        /* Section */
        .section {
            display: none;
        }

        .section.active {
            display: block;
        }

        /* Source link */
        .source-link {
            font-size: 0.875rem;
            color: #64748b;
        }

        /* Parameter list */
        .param-item {
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid var(--border-color);
        }

        .param-item:last-child {
            border-bottom: none;
        }

        .param-name {
            font-family: 'SF Mono', 'Fira Code', monospace;
            font-weight: 600;
        }

        .param-meta {
            display: flex;
            gap: 0.5rem;
            margin: 0.5rem 0;
        }

        .param-help {
            background: var(--code-bg);
            padding: 0.75rem;
            border-radius: 4px;
            font-size: 0.875rem;
            margin-top: 0.5rem;
        }

        /* Responsive */
        @media (max-width: 768px) {
            .sidebar {
                display: none;
            }
            .main {
                margin-left: 0;
                padding: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <aside class="sidebar">
            <h1>{{ pipeline.metadata.name or 'Pipeline' }}</h1>
            {% if pipeline.metadata.version %}
            <div class="version">v{{ pipeline.metadata.version }}</div>
            {% endif %}

            <nav>
                <ul>
                    <li>
                        <a href="#overview" class="nav-link active" data-section="overview">Overview</a>
                    </li>

                    {% if pipeline.inputs %}
                    <li>
                        <div class="section-title">Inputs</div>
                        <a href="#inputs" class="nav-link" data-section="inputs">Parameters ({{ pipeline.inputs|length }})</a>
                        <ul class="nested">
                            {% for group, items in input_groups.items() %}
                            <li><a href="#inputs-{{ group|lower|replace(' ', '-') }}" class="nav-link" data-section="inputs">{{ group }}</a></li>
                            {% endfor %}
                        </ul>
                    </li>
                    {% endif %}

                    {% if pipeline.config_params %}
                    <li>
                        <a href="#config" class="nav-link" data-section="config">Configuration ({{ pipeline.config_params|length }})</a>
                    </li>
                    {% endif %}

                    {% if pipeline.workflows %}
                    <li>
                        <div class="section-title">Workflows</div>
                        <a href="#workflows" class="nav-link" data-section="workflows">All Workflows ({{ pipeline.workflows|length }})</a>
                        <ul class="nested">
                            {% for wf in pipeline.workflows %}
                            <li><a href="#workflow-{{ wf.name or 'entry' }}" class="nav-link" data-section="workflows">{{ wf.name or '(entry)' }}</a></li>
                            {% endfor %}
                        </ul>
                    </li>
                    {% endif %}

                    {% if pipeline.processes %}
                    <li>
                        <div class="section-title">Processes</div>
                        <a href="#processes" class="nav-link" data-section="processes">All Processes ({{ pipeline.processes|length }})</a>
                        <ul class="nested">
                            {% for proc in pipeline.processes[:10] %}
                            <li><a href="#process-{{ proc.name }}" class="nav-link" data-section="processes">{{ proc.name }}</a></li>
                            {% endfor %}
                            {% if pipeline.processes|length > 10 %}
                            <li><em>... and {{ pipeline.processes|length - 10 }} more</em></li>
                            {% endif %}
                        </ul>
                    </li>
                    {% endif %}

                    {% if pipeline.functions %}
                    <li>
                        <a href="#functions" class="nav-link" data-section="functions">Functions ({{ pipeline.functions|length }})</a>
                    </li>
                    {% endif %}
                </ul>
            </nav>
        </aside>

        <main class="main">
            <!-- Overview Section -->
            <section id="overview" class="section active">
                <h1>{{ title }}</h1>

                {% if pipeline.metadata.description %}
                <p>{{ pipeline.metadata.description }}</p>
                {% endif %}

                <h2>Quick Stats</h2>
                <table>
                    <tr><th>Item</th><th>Count</th></tr>
                    <tr><td>Input Parameters</td><td>{{ pipeline.inputs|length }}</td></tr>
                    {% if pipeline.config_params %}
                    <tr><td>Config Parameters</td><td>{{ pipeline.config_params|length }}</td></tr>
                    {% endif %}
                    <tr><td>Workflows</td><td>{{ pipeline.workflows|length }}</td></tr>
                    <tr><td>Processes</td><td>{{ pipeline.processes|length }}</td></tr>
                    {% if pipeline.functions %}
                    <tr><td>Functions</td><td>{{ pipeline.functions|length }}</td></tr>
                    {% endif %}
                </table>

                {% if pipeline.metadata.authors %}
                <h2>Authors</h2>
                <ul>
                    {% for author in pipeline.metadata.authors %}
                    <li>{{ author }}</li>
                    {% endfor %}
                </ul>
                {% endif %}

                {% if pipeline.metadata.homepage or pipeline.metadata.repository %}
                <h2>Links</h2>
                <ul>
                    {% if pipeline.metadata.homepage %}
                    <li><a href="{{ pipeline.metadata.homepage }}" target="_blank">Homepage</a></li>
                    {% endif %}
                    {% if pipeline.metadata.repository %}
                    <li><a href="{{ pipeline.metadata.repository }}" target="_blank">Repository</a></li>
                    {% endif %}
                </ul>
                {% endif %}
            </section>

            <!-- Inputs Section -->
            <section id="inputs" class="section">
                <h1>Pipeline Inputs</h1>
                <p>This page documents all input parameters for the pipeline.</p>

                {% for group, items in input_groups.items() %}
                <h2 id="inputs-{{ group|lower|replace(' ', '-') }}">{{ group }}</h2>

                {% for inp in items %}
                <div class="param-item" id="param-{{ inp.name }}">
                    <div class="param-name">--{{ inp.name }}</div>
                    <div class="param-meta">
                        <span class="badge badge-type">{{ inp.type }}</span>
                        {% if inp.required %}
                        <span class="badge badge-required">Required</span>
                        {% else %}
                        <span class="badge badge-optional">Optional</span>
                        {% endif %}
                        {% if inp.format %}
                        <span class="badge badge-type">{{ inp.format }}</span>
                        {% endif %}
                    </div>
                    {% if inp.description %}
                    <p>{{ inp.description }}</p>
                    {% endif %}
                    {% if inp.help_text %}
                    <div class="param-help">{{ inp.help_text }}</div>
                    {% endif %}
                    {% if inp.default is not none %}
                    <p><strong>Default:</strong> <code>{{ inp.default }}</code></p>
                    {% endif %}
                    {% if inp.enum %}
                    <p><strong>Allowed values:</strong>
                        {% for val in inp.enum %}<code>{{ val }}</code>{% if not loop.last %}, {% endif %}{% endfor %}
                    </p>
                    {% endif %}
                </div>
                {% endfor %}
                {% endfor %}
            </section>

            <!-- Config Section -->
            {% if pipeline.config_params %}
            <section id="config" class="section">
                <h1>Configuration Parameters</h1>
                <p>These are additional configuration parameters that are not primary pipeline inputs.</p>

                {% for param in pipeline.config_params %}
                <div class="param-item">
                    <div class="param-name">{{ param.name }}</div>
                    <div class="param-meta">
                        <span class="badge badge-type">{{ param.type }}</span>
                    </div>
                    {% if param.description %}
                    <p>{{ param.description }}</p>
                    {% endif %}
                    {% if param.default is not none %}
                    <p><strong>Default:</strong> <code>{{ param.default }}</code></p>
                    {% endif %}
                </div>
                {% endfor %}
            </section>
            {% endif %}

            <!-- Workflows Section -->
            {% if pipeline.workflows %}
            <section id="workflows" class="section">
                <h1>Workflows</h1>
                <p>This page documents all workflows in the pipeline.</p>

                {% for wf in pipeline.workflows %}
                <div class="card" id="workflow-{{ wf.name or 'entry' }}">
                    <div class="card-header">
                        <span class="card-title">{{ wf.name or '(entry)' }}</span>
                        {% if wf.is_entry %}
                        <span class="badge badge-entry">Entry Point</span>
                        {% endif %}
                    </div>
                    {% if wf.file %}
                    <div class="source-link">{{ wf.file }}:{{ wf.line }}</div>
                    {% endif %}
                    {% if wf.docstring %}
                    <p>{{ wf.docstring }}</p>
                    {% endif %}

                    {% if wf.inputs %}
                    <h3>Inputs (take)</h3>
                    <table>
                        <tr><th>Name</th><th>Description</th></tr>
                        {% for inp in wf.inputs %}
                        <tr><td><code>{{ inp.name }}</code></td><td>{{ inp.description or '-' }}</td></tr>
                        {% endfor %}
                    </table>
                    {% endif %}

                    {% if wf.outputs %}
                    <h3>Outputs (emit)</h3>
                    <table>
                        <tr><th>Name</th><th>Description</th></tr>
                        {% for out in wf.outputs %}
                        <tr><td><code>{{ out.name }}</code></td><td>{{ out.description or '-' }}</td></tr>
                        {% endfor %}
                    </table>
                    {% endif %}

                    {% if wf.calls %}
                    <h3>Calls</h3>
                    <ul>
                        {% for call in wf.calls %}
                        <li><a href="#process-{{ call }}"><code>{{ call }}</code></a></li>
                        {% endfor %}
                    </ul>
                    {% endif %}
                </div>
                {% endfor %}
            </section>
            {% endif %}

            <!-- Processes Section -->
            {% if pipeline.processes %}
            <section id="processes" class="section">
                <h1>Processes</h1>
                <p>This page documents all processes in the pipeline.</p>

                {% for proc in pipeline.processes %}
                <div class="card" id="process-{{ proc.name }}">
                    <div class="card-header">
                        <span class="card-title">{{ proc.name }}</span>
                    </div>
                    {% if proc.file %}
                    <div class="source-link">{{ proc.file }}:{{ proc.line }}</div>
                    {% endif %}
                    {% if proc.docstring %}
                    <p>{{ proc.docstring }}</p>
                    {% endif %}

                    {% if proc.inputs %}
                    <h3>Inputs</h3>
                    <table>
                        <tr><th>Name</th><th>Type</th><th>Description</th></tr>
                        {% for inp in proc.inputs %}
                        <tr>
                            <td><code>{{ inp.name }}</code></td>
                            <td><code>{{ inp.type }}</code></td>
                            <td>{{ inp.description or '-' }}</td>
                        </tr>
                        {% endfor %}
                    </table>
                    {% endif %}

                    {% if proc.outputs %}
                    <h3>Outputs</h3>
                    <table>
                        <tr><th>Name</th><th>Type</th><th>Emit</th><th>Description</th></tr>
                        {% for out in proc.outputs %}
                        <tr>
                            <td><code>{{ out.name }}</code></td>
                            <td><code>{{ out.type }}</code></td>
                            <td>{% if out.emit %}<code>{{ out.emit }}</code>{% else %}-{% endif %}</td>
                            <td>{{ out.description or '-' }}</td>
                        </tr>
                        {% endfor %}
                    </table>
                    {% endif %}

                    {% if proc.directives %}
                    <h3>Directives</h3>
                    <table>
                        <tr><th>Directive</th><th>Value</th></tr>
                        {% for name, value in proc.directives.items() %}
                        <tr><td><code>{{ name }}</code></td><td><code>{{ value }}</code></td></tr>
                        {% endfor %}
                    </table>
                    {% endif %}
                </div>
                {% endfor %}
            </section>
            {% endif %}

            <!-- Functions Section -->
            {% if pipeline.functions %}
            <section id="functions" class="section">
                <h1>Functions</h1>
                <p>This page documents helper functions defined in the pipeline.</p>

                {% for func in pipeline.functions %}
                <div class="card" id="function-{{ func.name }}">
                    <div class="card-header">
                        <span class="card-title">{{ func.name }}</span>
                    </div>
                    {% if func.file %}
                    <div class="source-link">{{ func.file }}:{{ func.line }}</div>
                    {% endif %}

                    <pre><code>def {{ func.name }}({% for p in func.params %}{{ p.name }}{% if not loop.last %}, {% endif %}{% endfor %})</code></pre>

                    {% if func.docstring %}
                    <p>{{ func.docstring }}</p>
                    {% endif %}

                    {% if func.params %}
                    <h3>Parameters</h3>
                    <table>
                        <tr><th>Name</th><th>Description</th><th>Default</th></tr>
                        {% for p in func.params %}
                        <tr>
                            <td><code>{{ p.name }}</code></td>
                            <td>{{ p.description or '-' }}</td>
                            <td>{% if p.default is not none %}<code>{{ p.default }}</code>{% else %}-{% endif %}</td>
                        </tr>
                        {% endfor %}
                    </table>
                    {% endif %}

                    {% if func.return_description %}
                    <h3>Returns</h3>
                    <p>{{ func.return_description }}</p>
                    {% endif %}
                </div>
                {% endfor %}
            </section>
            {% endif %}
        </main>
    </div>

    <script>
        // Simple navigation
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();

                // Update active nav link
                document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
                link.classList.add('active');

                // Show corresponding section
                const sectionId = link.dataset.section;
                document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
                document.getElementById(sectionId).classList.add('active');

                // Scroll to anchor if present
                const href = link.getAttribute('href');
                if (href.startsWith('#') && href.length > 1) {
                    const target = document.querySelector(href);
                    if (target) {
                        setTimeout(() => target.scrollIntoView({ behavior: 'smooth' }), 100);
                    }
                } else {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                }
            });
        });

        // Handle direct hash navigation
        if (window.location.hash) {
            const hash = window.location.hash;
            const target = document.querySelector(hash);
            if (target) {
                // Find which section contains this target
                let section = target.closest('.section');
                if (section) {
                    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
                    section.classList.add('active');
                    setTimeout(() => target.scrollIntoView(), 100);
                }
            }
        }
    </script>
</body>
</html>'''


class HTMLRenderer(BaseRenderer):
    """
    Render pipeline documentation as a self-contained HTML page.

    This creates a single-page application with navigation that works
    without any server or build step.
    """

    def __init__(self, title: str | None = None):
        """
        Initialize the HTML renderer.

        Args:
            title: Optional custom title for the documentation
        """
        super().__init__(title)
        self.env = Environment(loader=BaseLoader())
        self.template = self.env.from_string(HTML_TEMPLATE)

    def render(self, pipeline: Pipeline) -> str:
        """
        Render the pipeline to HTML.

        Args:
            pipeline: The Pipeline model to render

        Returns:
            HTML string
        """
        title = self.get_title(pipeline)
        input_groups = pipeline.get_input_groups()

        return self.template.render(
            title=title,
            pipeline=pipeline,
            input_groups=input_groups,
        )

    def render_to_directory(self, pipeline: Pipeline, output_dir: str | Path) -> list[Path]:
        """
        Render the pipeline to a directory.

        For HTML, this creates a single index.html file.

        Args:
            pipeline: The Pipeline model to render
            output_dir: Output directory path

        Returns:
            List containing the single output file path
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        filename = output_path / "index.html"
        self.render_to_file(pipeline, filename)
        return [filename]
