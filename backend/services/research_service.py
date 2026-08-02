from search.serper import search_company
from crawler.crawler import crawl_website
from ai.analyzer import analyze_company
from pdf.generator import generate_pdf

def run_company_research(company_name):
    BACKEND_URL = "https://ai-company-research-assistant-qrhh.onrender.com"
    print("STEP 1: Starting research")

    search_result = search_company(company_name)

    print("STEP 2: Search completed")
    print(search_result)


    website = search_result.get("website")

    print("STEP 3: Website found:", website)


    crawl_result = crawl_website(website)

    print("STEP 4: Crawling completed")


    company_data = {
        "company_name": company_name,
        "website": website,
        "pages": crawl_result
    }


    print("STEP 5: Sending data to AI")


    report = analyze_company(company_data)


    print("STEP 6: AI completed")
    print(report)


    pdf_path = generate_pdf(
        report,
        filename=f"reports/{company_name}_report.pdf"
    )
    



    print("STEP 7: PDF generated")
    print(pdf_path)


   

   return {
      "report": report,
      "pdf": f"{BACKEND_URL}/{pdf_path}"
   }
