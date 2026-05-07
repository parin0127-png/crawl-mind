from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import os

def generate_report(data):
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "output", "audit_report.pdf")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = SimpleDocTemplate(output_path)

    style = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("CrawlMind SEO Report", style["Title"]))
    elements.append(Paragraph("On Page Analysis" , style["Heading1"]))
    elements.append(Paragraph("Title : " + data["title"] , style["Normal"]))
    elements.append(Paragraph("Word count : " + str(data["word_count"]),style["Normal"]))
    elements.append(Paragraph("Total image : " + str(data["total"]), style["Normal"]))
    elements.append(Paragraph("Missing Alt Tag : " + str(data["missing_alt"]), style["Normal"]))
    elements.append(Spacer(1,20))
    elements.append(Paragraph("Website: " + data["url"] , style["Normal"]))
    doc.build(elements)
    return output_path