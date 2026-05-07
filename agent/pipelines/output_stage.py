import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.report_generator import generate_report
from datetime import datetime
import markdown


def save_markdown(analysis_text, output_folder):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"SEO_REPORT_{timestamp}.md"
    filepath = os.path.join(output_folder, filename)

    with open(filepath , "w", encoding = "utf-8") as f:
        f.write(analysis_text)
    
    return filepath


def save_html(scraped_data, analysis_text, output_folder):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"Dashboard_{timestamp}.html"

    score = 100
    if not scraped_data.get("meta_description", ""):
        score -= 20
    if scraped_data.get("missing_alt" , 0) > 0:
        score -= 15
    if scraped_data.get("word_count", 0) < 300:
        score -= 15
    if not scraped_data.get("h1", []):
        score -= 15
    if scraped_data.get("word_count", 0) < 100:
        score -= 10
    if not scraped_data.get("title", ""):
        score -= 10
    if scraped_data.get("missing_alt", 0) > 5:
        score -= 10
    
    score = max(0, score)
    filepath = os.path.join(output_folder, filename)
    analysis_html = markdown.markdown(analysis_text)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <title>CrawlMind SEO Dashboard</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{ font-family: 'Inter', sans-serif; background: #0a0a0f; color: #e0e0e0; padding: 40px; }}
        
        .header {{ margin-bottom: 32px; }}
        .header h1 {{ font-size: 24px; font-weight: 600; color: #ffffff; letter-spacing: -0.5px; }}
        .header p {{ font-size: 13px; color: #666; margin-top: 4px; }}
        .url-badge {{ display: inline-block; background: #1a1d27; border: 1px solid #2a2d3a; border-radius: 20px; padding: 4px 12px; font-size: 12px; color: #888; margin-top: 8px; }}
        
        .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 24px; }}
        .card {{ background: #111118; border-radius: 16px; padding: 20px; border: 1px solid #1e1e2e; position: relative; overflow: hidden; }}
        
        .card .label {{ font-size: 11px; color: #555; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 10px; font-weight: 500; }}
        .card .value {{ font-size: 28px; font-weight: 700; letter-spacing: -1px; display: flex; align-items: center; gap: 8px; }}
        .card .sub {{ font-size: 11px; color: #555; margin-top: 6px; }}
        
        .green {{ color: #00d4a0; }}
        .orange {{ color: #f5a623; }}
        .red {{ color: #ff4d4d; }}

        .chart-row {{ display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 12px; margin-bottom: 24px; }}
        .chart-card {{ background: #111118; border-radius: 16px; padding: 24px; border: 1px solid #1e1e2e; display: flex; flex-direction: column; min-height: 380px; }}
        .chart-card .title {{ font-size: 13px; font-weight: 500; color: #aaa; margin-bottom: 20px; }}

        .dual-chart-container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; flex-grow: 1; align-items: center; }}
        .score-ring {{ position: relative; display: flex; align-items: center; justify-content: center; width: 100%; }}
        .score-label {{ position: absolute; font-size: 20px; font-weight: 700; color: {'#00d4a0' if score >= 70 else '#f5a623' if score >= 50 else '#ff4d4d'}; }}
        
        .bar-container {{ flex-grow: 1; width: 100%; position: relative; margin-top: 10px; }}

        .analysis-card {{ background: #111118; border-radius: 16px; padding: 32px; border: 1px solid #1e1e2e; }}
        .analysis-content {{ font-size: 13px; color: #999; line-height: 1.8; }}
        
        .alert-dot {{ width: 8px; height: 8px; background: #ff4d4d; border-radius: 50%; display: inline-block; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} 100% {{ opacity: 1; }} }}
    </style>
</head>
<body>
    <div class="header">
        <h1>CrawlMind SEO Dashboard</h1>
        <p>Automated SEO Intelligence Report</p>
        <span class="url-badge">🔍 {scraped_data.get('url', 'Unknown')}</span>
    </div>

    <div class="grid">
        <div class="card">
            <div class="label">Health Score</div>
            <div class="value {'green' if score >= 70 else 'red'}">{score}</div>
            <div class="sub">{'Performance Stable' if score >= 70 else 'Critical Review Needed'}</div>
        </div>
        <div class="card">
            <div class="label">Word Count</div>
            <div class="value {'green' if scraped_data.get('word_count', 0) >= 300 else 'red'}">{scraped_data.get('word_count', 0)}</div>
            <div class="sub">{'Content Rich' if scraped_data.get('word_count', 0) >= 300 else 'Thin Content Alert'}</div>
        </div>
        <div class="card">
            <div class="label">Missing Alt Tags</div>
            <div class="value {'red' if scraped_data.get('missing_alt', 0) > 0 else 'green'}">
                {scraped_data.get('missing_alt', 0)}
                { '<span class="alert-dot"></span>' if scraped_data.get('missing_alt', 0) > 0 else '' }
            </div>
            <div class="sub">{ 'Fix Images' if scraped_data.get('missing_alt', 0) > 0 else 'Accessibility Optimized' }</div>
        </div>
        <div class="card">
            <div class="label">Meta Description</div>
            <div class="value {'green' if scraped_data.get('meta_description') else 'red'}">{'Present ✓' if scraped_data.get('meta_description') else 'Missing ✗'}</div>
            <div class="sub">{'Snippet Found' if scraped_data.get('meta_description') else 'No SEO Snippet'}</div>
        </div>
    </div>

    <div class="chart-row">
        <div class="chart-card">
            <div style="display: flex; justify-content: space-between;">
                <div class="title">Performance Ring</div>
                <div class="title" style="margin-right: 20%;">Content Distribution</div>
            </div>
            <div class="dual-chart-container">
                <div class="score-ring">
                    <canvas id="scoreChart"></canvas>
                    <div class="score-label">{score}</div>
                </div>
                <div class="score-ring">
                    <canvas id="contentChart"></canvas>
                </div>
            </div>
        </div>

        <div class="chart-card">
            <div class="title">SEO Issues Overview (Logarithmic Scale)</div>
            <div class="bar-container">
                <canvas id="issuesChart"></canvas>
            </div>
        </div>
    </div>

    <div class="analysis-card">
        <div class="analysis-content">{analysis_html}</div>
    </div>

    <script>
        // Doughnut Chart
        new Chart(document.getElementById('scoreChart'), {{
            type: 'doughnut',
            data: {{
                datasets: [{{
                    data: [{score}, {100 - score}],
                    backgroundColor: ['{('#00d4a0' if score >= 70 else '#f5a623' if score >= 50 else '#ff4d4d')}', '#1e1e2e'],
                    borderWidth: 0
                }}]
            }},
            options: {{ cutout: '75%', plugins: {{ legend: {{ display: false }} }} }}
        }});

        // Pie Chart
        new Chart(document.getElementById('contentChart'), {{
            type: 'pie',
            data: {{
                labels: ['Text', 'Media', 'Other'],
                datasets: [{{
                    data: [{scraped_data.get('word_count', 100)}, {scraped_data.get('missing_alt', 0) + 10}, 20],
                    backgroundColor: ['#00d4a0', '#378ADD', '#f5a623'],
                    borderWidth: 0
                }}]
            }},
            options: {{ plugins: {{ legend: {{ display: false }} }} }}
        }});

        // Updated Bar Chart with Logarithmic Scale
        new Chart(document.getElementById('issuesChart'), {{
            type: 'bar',
            data: {{
                labels: ['Words', 'Alt Tags', 'Meta', 'Score'],
                datasets: [{{
                    data: [{scraped_data.get('word_count', 1)}, {scraped_data.get('missing_alt', 0) + 0.1}, 1, {score}],
                    backgroundColor: ['#378ADD', '#ff4d4d', '#f5a623', '#00d4a0'],
                    borderRadius: 6
                }}]
            }},
            options: {{
                maintainAspectRatio: false,
                responsive: true,
                plugins: {{ legend: {{ display: false }} }},
                scales: {{
                    y: {{ 
                        type: 'logarithmic',
                        beginAtZero: false,
                        min: 0.1,
                        ticks: {{ 
                            color: '#555', 
                            font: {{ size: 10 }},
                            callback: function(value) {{
                                if (value === 1 || value === 10 || value === 100 || value === 1000) return value;
                            }}
                        }},
                        grid: {{ color: '#1e1e2e', drawTicks: false }}
                    }},
                    x: {{ 
                        ticks: {{ color: '#888', font: {{ size: 11, weight: '500' }} }},
                        grid: {{ display: false }}
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>"""

    with open(filepath, "w", encoding = "utf-8")as f:
        f.write(html)

    return filepath

def run(scraped_data, analysis_text):
    output_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "output")
    os.makedirs(output_folder, exist_ok = True)

    md_path = save_markdown(analysis_text, output_folder)
    html_path = save_html(scraped_data, analysis_text, output_folder)
    pdf_path = generate_report(scraped_data)

    print(f"Markdown save ->    {md_path}")
    print(f"HTML save     ->    {html_path}")
    print(f"Pdf save      ->    {pdf_path}")

    return md_path,html_path,pdf_path
