import requests




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
