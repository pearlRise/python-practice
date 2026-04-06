from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle

def create_aiqa_minutes():
    file_name = "aiqa_project_setup_minutes_8pages.pdf"
    doc = SimpleDocTemplate(file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # 커스텀 스타일 설정
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=18, spaceAfter=20, alignment=1)
    sub_title_style = ParagraphStyle('SubTitle', parent=styles['Heading2'], fontSize=14, spaceAfter=10, textColor=colors.navy)
    body_style = styles['Normal']

    # --- Page 1: Cover Page ---
    story.append(Spacer(1, 200))
    story.append(Paragraph("Project: aiqa (AI-driven QA Automation)", title_style))
    story.append(Paragraph("Subject: Infrastructure Setup & Strategic Planning", title_style))
    story.append(Spacer(1, 50))
    story.append(Paragraph("Date: April 6, 2026", body_style))
    story.append(Paragraph("Chairperson: Kim Tae-sung (General Manager)", body_style))
    story.append(PageBreak())

    # --- Page 2: Participants & Objectives ---
    story.append(Paragraph("1. Meeting Participants", sub_title_style))
    data = [
        ['Role', 'Name', 'Responsibility'],
        ['General Manager', 'Kim Tae-sung', 'Project Decision Maker'],
        ['Manager', 'Park Min-seok', 'Infrastructure Lead'],
        ['Assistant Manager', 'Lee Ji-hye', 'QA Strategy'],
        ['Engineer 1', 'Choi Yun-a', 'Ubuntu Server & Docker'],
        ['Engineer 2', 'Jung Hyun-woo', 'Data Engineering'],
        ['Engineer 3', 'Kim Ji-hun', 'CI/CD & DevOps']
    ]
    t = Table(data, colWidths=[100, 100, 200])
    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey), ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('GRID', (0, 0), (-1, -1), 0.5, colors.black)]))
    story.append(t)
    story.append(Spacer(1, 20))
    story.append(Paragraph("2. Objectives", sub_title_style))
    story.append(Paragraph("- Establishment of local LLM serving environment.", body_style))
    story.append(Paragraph("- Defining the workstation roles (Desktop vs MacBook).", body_style))
    story.append(PageBreak())

    # --- Page 3-7: Detailed Discussions (Loop to fill pages) ---
    topics = [
        ("3. Hardware Resource Allocation", "Discussing the use of RTX 3090 and 3060 for model training and inference. Decided to use the desktop as a dedicated workstation."),
        ("4. Network & Security Architecture", "Internal network configuration, SSH tunneling, and port forwarding for remote access from MacBook Pro M5."),
        ("5. Software Stack Selection", "Selection of Ubuntu 24.04 LTS, Docker, and Python 3.12 for the primary development environment."),
        ("6. LLM Integration Strategy", "Using LangChain and PyTorch to bridge the gap between local resources and the QA automation framework."),
        ("7. Data Privacy & Dummy Generation", "Implementation of Faker and synthetic data generators to prevent sensitive data leakage.")
    ]

    for title, content in topics:
        story.append(Paragraph(title, sub_title_style))
        # 텍스트 양을 늘리기 위해 상세 설명 추가
        for _ in range(15): 
            story.append(Paragraph(f"{content} Detailed analysis of system logs and performance metrics will be conducted weekly.", body_style))
            story.append(Spacer(1, 12))
        story.append(PageBreak())

    # --- Page 8: Conclusion & Action Items ---
    story.append(Paragraph("8. Action Items & Next Meeting", sub_title_style))
    todo = [
        ['Task', 'Owner', 'Deadline'],
        ['Ubuntu Server Setup', 'Choi Yun-a', '2026-04-10'],
        ['LLM Model Benchmarking', 'Jung Hyun-woo', '2026-04-12'],
        ['Network Tunneling Test', 'Kim Ji-hun', '2026-04-13']
    ]
    t_todo = Table(todo, colWidths=[200, 100, 100])
    t_todo.setStyle(TableStyle([('GRID', (0, 0), (-1, -1), 0.5, colors.black), ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey)]))
    story.append(t_todo)
    story.append(Spacer(1, 50))
    story.append(Paragraph("Final Approval: ____________________ (Kim Tae-sung)", body_style))

    doc.build(story)
    print(f"File created: {file_name}")

if __name__ == "__main__":
    create_aiqa_minutes()