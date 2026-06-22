from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(alert):
    file = f"report_{alert['ip']}.pdf"
    doc = SimpleDocTemplate(file)

    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("SOC INCIDENT REPORT", styles["Title"]))
    content.append(Paragraph(f"IP: {alert['ip']}", styles["Normal"]))
    content.append(Paragraph(f"Severity: {alert['severity']}", styles["Normal"]))
    content.append(Paragraph(f"Details: {alert['message']}", styles["Normal"]))

    doc.build(content)

    return file