from datetime import datetime
# -*- coding: utf-8 -*-
import io
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from reportlab.lib.pagesizes import A4, landscape, portrait
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


def generate_vedomost_excel(results, group_name="Barcha guruhlar"):
    """Dasturlash fanidan har bir guruh uchun joriy nazorat vedomostini Excel formatida shakllantirish"""
    wb = Workbook()
    ws = wb.active
    ws.title = "Joriy Nazorat Vedomosti"

    # Sarlavha
    ws.merge_cells("A1:E1")
    title_cell = ws["A1"]
    title_cell.value = "DASTURLASH FANIDAN JORIY NAZORAT JADVALI (VEDOMOST)"
    title_cell.font = Font(name="Calibri", size=14, bold=True, color="1E3A8A")
    title_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 32

    # Guruh va fan ma'lumotlari
    ws.merge_cells("A2:E2")
    info_cell = ws["A2"]
    today_str = datetime.now().strftime('%d.%m.%Y')
    info_cell.value = f"Guruh: {group_name}   |   Fan: Dasturlash   |   Maksimal ball: 30 ball   |   Sana: {today_str}"
    info_cell.font = Font(name="Calibri", size=10, italic=True, color="475569")
    info_cell.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[2].height = 22

    headers = ["№", "Talaba ID", "F.I.O.", "Guruh", "Joriy nazorat bali"]
    ws.append([]) # Bo'sh qator
    ws.append(headers)
    ws.row_dimensions[4].height = 25

    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    header_fill = PatternFill(start_color="1E40AF", end_color="1E40AF", fill_type="solid")
    center_align = Alignment(horizontal="center", vertical="center")
    left_align = Alignment(horizontal="left", vertical="center")
    thin_border = Border(
        left=Side(style='thin', color='CBD5E1'),
        right=Side(style='thin', color='CBD5E1'),
        top=Side(style='thin', color='CBD5E1'),
        bottom=Side(style='thin', color='CBD5E1')
    )

    for col_idx in range(1, len(headers) + 1):
        cell = ws.cell(row=4, column=col_idx)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = center_align
        cell.border = thin_border

    pass_font = Font(name="Calibri", size=10, bold=True, color="15803D")
    fail_font = Font(name="Calibri", size=10, bold=True, color="B91C1C")

    for i, r in enumerate(results, start=1):
        row_num = i + 4
        score = r.get('total_score', 0)
        score_display = f"{score} ball" if score is not None else "-"
        
        row_data = [
            i,
            r.get('student_id_number') or r.get('studentId') or "-",
            r.get('full_name') or r.get('fullName') or "",
            r.get('group_name') or r.get('groupName') or group_name,
            score_display
        ]
        ws.append(row_data)
        ws.row_dimensions[row_num].height = 20

        for col_idx in range(1, len(row_data) + 1):
            cell = ws.cell(row=row_num, column=col_idx)
            cell.font = Font(name="Calibri", size=10)
            cell.border = thin_border
            if col_idx in [1, 2, 4]:
                cell.alignment = center_align
            elif col_idx == 3:
                cell.alignment = left_align
            elif col_idx == 5:
                cell.alignment = center_align
                if score is not None and score >= 18:
                    cell.font = pass_font
                elif score is not None:
                    cell.font = fail_font

    # Imzo qatori
    sign_row = len(results) + 6
    ws.merge_cells(f"A{sign_row}:C{sign_row}")
    sign_cell = ws[f"A{sign_row}"]
    sign_cell.value = "O‘qituvchi: _______________________ (imzo)"
    sign_cell.font = Font(name="Calibri", size=10, italic=True)
    sign_cell.alignment = Alignment(horizontal="left", vertical="center")

    ws.merge_cells(f"D{sign_row}:E{sign_row}")
    date_cell = ws[f"D{sign_row}"]
    date_cell.value = f"Sana: {today_str}"
    date_cell.font = Font(name="Calibri", size=10, italic=True)
    date_cell.alignment = Alignment(horizontal="right", vertical="center")

    # Ustunlar kengligi
    ws.column_dimensions['A'].width = 6
    ws.column_dimensions['B'].width = 18
    ws.column_dimensions['C'].width = 38
    ws.column_dimensions['D'].width = 20
    ws.column_dimensions['E'].width = 22

    output = io.BytesIO()
    wb.save(output)
    output.seek(0)
    return output.getvalue()


def generate_vedomost_pdf(results, group_name="Barcha guruhlar"):
    """Dasturlash fanidan har bir guruh uchun joriy nazorat vedomostini PDF formatida shakllantirish"""
    output = io.BytesIO()
    doc = SimpleDocTemplate(
        output,
        pagesize=portrait(A4),
        leftMargin=25,
        rightMargin=25,
        topMargin=25,
        bottomMargin=25
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'VedomostTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12,
        alignment=1,
        textColor=colors.HexColor('#1E3A8A'),
        spaceAfter=4
    )
    subtitle_style = ParagraphStyle(
        'VedomostSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        alignment=1,
        textColor=colors.HexColor('#475569'),
        spaceAfter=12
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
    today_str = datetime.now().strftime('%d.%m.%Y')

    elements.append(Paragraph("DASTURLASH FANIDAN JORIY NAZORAT JADVALI (VEDOMOST)", title_style))
    elements.append(Paragraph(f"<b>Guruh:</b> {group_name} &nbsp;&nbsp;|&nbsp;&nbsp; <b>Fan:</b> Dasturlash &nbsp;&nbsp;|&nbsp;&nbsp; <b>Maksimal ball:</b> 30 ball &nbsp;&nbsp;|&nbsp;&nbsp; <b>Sana:</b> {today_str}", subtitle_style))

    table_data = [[
        Paragraph("№", header_style),
        Paragraph("Talaba ID", header_style),
        Paragraph("F.I.O.", header_style),
        Paragraph("Guruh", header_style),
        Paragraph("Joriy nazorat bali", header_style)
    ]]

    for i, r in enumerate(results, start=1):
        score = r.get('total_score', 0)
        score_color = "#15803D" if (score is not None and score >= 18) else "#B91C1C"
        score_text = f"<b><font color='{score_color}'>{score} ball</font></b>" if score is not None else "-"
        
        sid = r.get('student_id_number') or r.get('studentId') or "-"
        fname = r.get('full_name') or r.get('fullName') or ""
        gname = r.get('group_name') or r.get('groupName') or group_name

        table_data.append([
            Paragraph(str(i), cell_center),
            Paragraph(str(sid), cell_center),
            Paragraph(str(fname), cell_style),
            Paragraph(str(gname), cell_center),
            Paragraph(score_text, cell_center)
        ])

    col_widths = [25, 100, 240, 95, 85]
    t = Table(table_data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E40AF')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F8FAFC')])
    ]))

    elements.append(t)
    elements.append(Spacer(1, 20))

    # Imzolar jadvali
    sign_data = [
        [
            Paragraph("<b>O‘qituvchi:</b> ___________________________ (imzo)", cell_style),
            Paragraph(f"<b>Sana:</b> {today_str}", cell_center)
        ]
    ]
    sign_table = Table(sign_data, colWidths=[350, 195])
    sign_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0)
    ]))
    elements.append(sign_table)

    doc.build(elements)
    output.seek(0)
    return output.getvalue()
