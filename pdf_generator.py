"""
PDF Report Generator for FarmScan
Creates professional disease analysis reports
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import io
from PIL import Image

def generate_scan_report_pdf(scan_data, image_data=None, user_info=None):
    """
    Generate a comprehensive PDF report for a crop scan
    
    Args:
        scan_data: Dictionary with scan results
        image_data: PIL Image object or None
        user_info: Dictionary with user information
    
    Returns:
        BytesIO object containing the PDF
    """
    
    # Create PDF buffer
    buffer = io.BytesIO()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for PDF elements
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2E7D32'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#1976D2'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        alignment=TA_JUSTIFY
    )
    
    warning_style = ParagraphStyle(
        'WarningStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#D32F2F'),
        spaceAfter=8,
        fontName='Helvetica-Bold'
    )
    
    # Add title
    elements.append(Paragraph("🌾 FarmScan Crop Analysis Report", title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Add report metadata
    current_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    elements.append(Paragraph(f"<b>Report Generated:</b> {current_time}", normal_style))
    
    if user_info:
        elements.append(Paragraph(f"<b>Farmer Name:</b> {user_info.get('name', 'N/A')}", normal_style))
        elements.append(Paragraph(f"<b>Phone:</b> {user_info.get('phone', 'N/A')}", normal_style))
    
    elements.append(Spacer(1, 0.3*inch))
    
    # Add horizontal line
    elements.append(Table([['']], colWidths=[6.5*inch], style=[
        ('LINEBELOW', (0, 0), (-1, -1), 2, colors.HexColor('#2E7D32'))
    ]))
    elements.append(Spacer(1, 0.2*inch))
    
    # === DIAGNOSIS SECTION ===
    elements.append(Paragraph("📊 Diagnosis Results", subtitle_style))
    
    # Create diagnosis table
    diagnosis_data = [
        ['Disease Detected:', scan_data.get('diseaseName', 'Unknown')],
        ['Confidence Level:', f"{int(scan_data.get('confidence', 0) * 100)}%"],
        ['Severity:', scan_data.get('severity', 'Unknown')],
    ]
    
    diagnosis_table = Table(diagnosis_data, colWidths=[2*inch, 4*inch])
    diagnosis_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#E8F5E9')),
        ('BACKGROUND', (1, 0), (1, -1), colors.white),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    elements.append(diagnosis_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # === RISK ASSESSMENT ===
    elements.append(Paragraph("⚠️ Risk Assessment", subtitle_style))
    elements.append(Paragraph(scan_data.get('spreadRisk', 'No information available'), normal_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # === TREATMENT SECTION ===
    elements.append(Paragraph("💊 Recommended Treatment", subtitle_style))
    elements.append(Paragraph(scan_data.get('treatment', 'No treatment information available'), normal_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # === ORGANIC TREATMENT ===
    organic = scan_data.get('organicTreatment', {})
    if organic:
        elements.append(Paragraph(f"🌿 {organic.get('title', 'Organic Treatment Options')}", subtitle_style))
        
        details = organic.get('details', [])
        for i, detail in enumerate(details, 1):
            elements.append(Paragraph(f"{i}. {detail}", normal_style))
        
        elements.append(Spacer(1, 0.2*inch))
    
    # === SAFETY WARNING ===
    elements.append(Paragraph("🛡️ Safety Warning", subtitle_style))
    elements.append(Paragraph(scan_data.get('safetyWarning', 'Follow all safety precautions'), warning_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # === IMAGE SECTION ===
    if image_data:
        try:
            elements.append(Paragraph("📸 Analyzed Image", subtitle_style))
            
            # Resize image to fit on page
            img_width, img_height = image_data.size
            max_width = 5 * inch
            max_height = 4 * inch
            
            scale = min(max_width / img_width, max_height / img_height)
            new_width = img_width * scale
            new_height = img_height * scale
            
            # Save image to buffer
            img_buffer = io.BytesIO()
            image_data.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            
            # Add image to PDF
            img = RLImage(img_buffer, width=new_width, height=new_height)
            elements.append(img)
            elements.append(Spacer(1, 0.2*inch))
        except Exception as e:
            print(f"Error adding image to PDF: {e}")
    
    # === RECOMMENDATIONS ===
    elements.append(PageBreak())
    elements.append(Paragraph("📋 General Recommendations", subtitle_style))
    
    recommendations = [
        "Monitor your crop daily for any changes in symptoms",
        "Keep detailed records of all treatments applied",
        "Maintain proper spacing between plants for air circulation",
        "Remove and destroy infected plant material properly",
        "Practice crop rotation to prevent disease buildup",
        "Use disease-resistant varieties when available",
        "Ensure proper irrigation - avoid overwatering",
        "Consult local agricultural extension for region-specific advice"
    ]
    
    for i, rec in enumerate(recommendations, 1):
        elements.append(Paragraph(f"✓ {rec}", normal_style))
    
    elements.append(Spacer(1, 0.3*inch))
    
    # === FOOTER ===
    elements.append(Spacer(1, 0.5*inch))
    elements.append(Table([['']], colWidths=[6.5*inch], style=[
        ('LINEABOVE', (0, 0), (-1, -1), 1, colors.grey)
    ]))
    
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_CENTER
    )
    
    elements.append(Paragraph(
        "This report is generated by FarmScan AI Disease Detection System<br/>"
        "For best results, consult with local agricultural experts<br/>"
        "© 2026 FarmScan - Helping Farmers Grow Better",
        footer_style
    ))
    
    # Build PDF
    doc.build(elements)
    
    # Get PDF data
    buffer.seek(0)
    return buffer

def create_history_report_pdf(scans_list, user_info=None):
    """
    Generate a PDF report with scan history
    
    Args:
        scans_list: List of scan dictionaries
        user_info: Dictionary with user information
    
    Returns:
        BytesIO object containing the PDF
    """
    
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)
    
    elements = []
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#2E7D32'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Title
    elements.append(Paragraph("🌾 FarmScan Scan History Report", title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # User info
    if user_info:
        elements.append(Paragraph(f"<b>Farmer:</b> {user_info.get('name', 'N/A')}", styles['Normal']))
        elements.append(Paragraph(f"<b>Phone:</b> {user_info.get('phone', 'N/A')}", styles['Normal']))
    
    elements.append(Paragraph(f"<b>Generated:</b> {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))
    elements.append(Spacer(1, 0.3*inch))
    
    # Table header
    table_data = [['Date', 'Disease', 'Confidence', 'Severity']]
    
    # Add scan data
    for scan in scans_list[:20]:  # Limit to 20 most recent
        table_data.append([
            scan.get('date', 'N/A')[:16],  # Truncate datetime
            scan.get('disease_name', 'Unknown'),
            f"{int(scan.get('confidence', 0) * 100)}%",
            scan.get('severity', 'N/A')
        ])
    
    # Create table
    table = Table(table_data, colWidths=[1.5*inch, 2.5*inch, 1.2*inch, 1.2*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2E7D32')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    
    elements.append(table)
    
    # Summary
    elements.append(Spacer(1, 0.3*inch))
    elements.append(Paragraph(f"<b>Total Scans:</b> {len(scans_list)}", styles['Normal']))
    
    doc.build(elements)
    buffer.seek(0)
    return buffer
