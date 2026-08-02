from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report_data, filename="company_report.pdf"):

    doc = SimpleDocTemplate(filename, pagesize=letter)

    styles = getSampleStyleSheet()

    content = []


    content.append(
        Paragraph(
            "AI Company Research Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))


    # Company Information

    content.append(
        Paragraph(
            "Company Information",
            styles["Heading2"]
        )
    )

    fields = [
        "company_name",
        "website",
        "phone",
        "address"
    ]

    for field in fields:

        value = report_data.get(field, "")

        content.append(
            Paragraph(
                f"{field.replace('_',' ').title()}: {value}",
                styles["BodyText"]
            )
        )


    content.append(Spacer(1, 15))


    # Products

    content.append(
        Paragraph(
            "Products / Services",
            styles["Heading2"]
        )
    )


    for item in report_data.get("products_services", []):

        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )


    content.append(Spacer(1,15))


    # Pain Points

    content.append(
        Paragraph(
            "AI Generated Pain Points",
            styles["Heading2"]
        )
    )


    for item in report_data.get("pain_points", []):

        content.append(
            Paragraph(
                f"• {item}",
                styles["BodyText"]
            )
        )


    content.append(Spacer(1,15))


    # Competitors

    content.append(
        Paragraph(
            "Competitors",
            styles["Heading2"]
        )
    )


    for competitor in report_data.get("competitors", []):

        content.append(
            Paragraph(
                f"{competitor['name']} - {competitor['website']}",
                styles["BodyText"]
            )
        )


    doc.build(content)


    return filename