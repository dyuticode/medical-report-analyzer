from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_medical_pdf(df, recommendations_text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=22, textColor=colors.HexColor('#1A365D'), spaceAfter=15)
    section_style = ParagraphStyle('SectionStyle', parent=styles['Heading2'], fontSize=14, textColor=colors.HexColor('#2C5282'), spaceAfter=10, spaceBefore=10)
    body_style = ParagraphStyle('BodyStyle', parent=styles['Normal'], fontSize=10, leading=14)
    
    # Document Header
    story.append(Paragraph("🩺 MediInsight AI - Patient Analysis Report", title_style))
    story.append(Paragraph("Generated Laboratory Review & Structural Assessment", body_style))
    story.append(Spacer(1, 15))
    
    # Parameters Table Heading
    story.append(Paragraph("Parameters Analysis Matrix", section_style))
    
    # Prepare Table Data Layout
    table_data = [["Parameter Test", "Observed Value", "Evaluated Status"]]
    for _, row in df.iterrows():
        table_data.append([str(row["Test"]), str(row["Value"]), str(row["Status"])])
        
    t = Table(table_data, colWidths=[200, 150, 180])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F2F4F8')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#1A365D')),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('GRID', (0,0), (-1,-1), 0.5, colors.lightgrey),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
    ]))
    story.append(t)
    story.append(Spacer(1, 20))
    
    # Recommendations Block
    story.append(Paragraph("AI Recommendations & Risk Analysis", section_style))
    clean_recs = recommendations_text.replace("\n", "<br/>")
    story.append(Paragraph(clean_recs, body_style))
    
    doc.build(story)
    buffer.seek(0)
    return buffer