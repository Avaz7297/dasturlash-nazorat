# -*- coding: utf-8 -*-
import io
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_excel_report(results):
    """Natijalarni Excel (.xlsx) formatida generatsiya qilish"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Joriy Nazorat Natijalari"

    # Sarlavha
    ws.merge_cells("A1:K1")
    title_cell = ws["A1"]
    title_cell.value = "Python dasturlash fanidan masofaviy joriy nazorat natijalari"
    title_cell.font = Font(name="Calibri", size=16, bold=True, color="1E3A8A")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 40

    headers = [
        "№", "F.I.Sh.", "Yo‘nalish", "Kurs", "Guruh",
        "To‘g‘ri javoblar", "Noto‘g‘ri javoblar", "To‘plangan ball",
        "Natija", "Test topshirilgan sana va vaqt", "Sahifadan chiqishlar"
    ]

    ws.append([]) # Bo'sh qator
    ws.append(headers)
    ws.row_dimensions[3].height = 25

    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="2563EB", end_color="2563EB", fill_type="solid")
    center_align = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin_border = Border(
        left=Side(style='thin', color='D1D5DB'),
        right=Side(style='thin', color='D1D5DB'),
        top=Side(style='thin', color='D1D5DB'),
        bottom=Side(style='thin', color='D1D5DB')
    )

    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=3, column=col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    pass_fill = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
    fail_fill = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")

    for i, r in enumerate(results, start=1):
        row_num = i + 3
        status = r['status_text']
        date_str = r['finished_at'] if r['finished_at'] else r['started_at']
        
        row_data = [
            i,
            r['full_name'],
            r['direction'],
            f"{r['course']}-kurs",
            r['group_name'],
            r['correct_count'],
            r['incorrect_count'],
            f"{r['total_score']} / {r['max_score']}",
            status,
            date_str,
            f"{r['tab_switch_count']} marta"
        ]
        ws.append(row_data)
        ws.row_dimensions[row_num].height = 20

        for col_idx in range(1, len(row_data) + 1):
            cell = ws.cell(row=row_num, column=col_idx)
            cell.font = Font(name="Calibri", size=10)
            cell.border = thin_border
            if col_idx in [1, 4, 6, 7, 8, 10, 11]:
                cell.alignment = center_align
            elif col_idx == 9:
                cell.alignment = center_align
                if "o‘tdi" in status.lower():
                    cell.fill = pass_fill
                    cell.font = Font(name="Calibri", size=10, bold=True, color="166534")
                else:
                    cell.fill = fail_fill
                    cell.font = Font(name="Calibri", size=10, bold=True, color="991B1B")

    # Ustunlar kengligini moslashtirish
    col_widths = [5, 28, 22, 10, 12, 16, 16, 16, 22, 24, 18]
    for idx, width in enumerate(col_widths, start=1):
        col_letter = ws.cell(row=3, column=idx).column_letter
        ws.column_dimensions[col_letter].width = width

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    return output.getvalue()


def generate_pdf_report(results):
    """Natijalarni PDF formatida generatsiya qilish"""
    output = io.BytesIO()
    doc = SimpleDocTemplate(
        output,
        pagesize=landscape(A4),
        leftMargin=20,
        rightMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=15,
        alignment=1, # Center
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=15
    )

    cell_style = ParagraphStyle(
        'CellStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10
    )
    cell_center = ParagraphStyle(
        'CellCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10,
        alignment=1
    )
    header_style = ParagraphStyle(
        'HeaderStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.white,
        alignment=1
    )

    elements = []
    title = Paragraph("Python dasturlash fanidan joriy nazorat natijalari (Vedomost)", title_style)
    elements.append(title)

    table_data = [[
        Paragraph("№", header_style),
        Paragraph("F.I.Sh.", header_style),
        Paragraph("Yo'nalish", header_style),
        Paragraph("Kurs", header_style),
        Paragraph("Guruh", header_style),
        Paragraph("To'g'ri", header_style),
        Paragraph("Noto'g'ri", header_style),
        Paragraph("Ball", header_style),
        Paragraph("Natija", header_style),
        Paragraph("Topshirilgan vaqt", header_style)
    ]]

    for i, r in enumerate(results, start=1):
        status = r['status_text']
        date_str = r['finished_at'] if r['finished_at'] else r['started_at']
        
        status_color = "#166534" if "o‘tdi" in status.lower() else "#991B1B"
        status_para = Paragraph(f"<font color='{status_color}'><b>{status}</b></font>", cell_center)

        table_data.append([
            Paragraph(str(i), cell_center),
            Paragraph(r['full_name'], cell_style),
            Paragraph(r['direction'], cell_style),
            Paragraph(f"{r['course']}", cell_center),
            Paragraph(r['group_name'], cell_center),
            Paragraph(str(r['correct_count']), cell_center),
            Paragraph(str(r['incorrect_count']), cell_center),
            Paragraph(f"<b>{r['total_score']} / {r['max_score']}</b>", cell_center),
            status_para,
            Paragraph(str(date_str), cell_center)
        ])

    col_widths = [25, 140, 130, 35, 55, 45, 50, 60, 110, 105]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563EB')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')])
    ]))

    elements.append(t)
    doc.build(elements)
    output.seek(0)
    return output.getvalue()
