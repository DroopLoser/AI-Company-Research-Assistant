import requests


def send_discord_report(
    webhook_url,
    applicant_name,
    applicant_email,
    company_name,
    company_website,
    pdf_path
):

    message = {
        "content": f"""
New Company Research Completed

Applicant:
{applicant_name}

Email:
{applicant_email}

Company:
{company_name}

Website:
{company_website}
"""
    }


    response = requests.post(
        webhook_url,
        json=message
    )


    return response.status_code