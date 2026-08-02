from fastapi import APIRouter
from search.serper import search_company


router = APIRouter()


@router.get("/search-company")
def search(company: str):

    result = search_company(company)

    return result

from crawler.crawler import crawl_website


@router.get("/crawl")
def crawl(url: str):

    result = crawl_website(url)

    return {
        "pages_found": len(result),
        "pages": result
    }
    
from ai.analyzer import analyze_company


@router.post("/analyze")
def analyze(data: dict):

    result = analyze_company(data)

    return result

from pdf.generator import generate_pdf


@router.post("/generate-pdf")
def create_pdf(data: dict):
    
    print("PDF DATA RECEIVED:")
    print(data)

    file = generate_pdf(data)

    return {
        "message": "PDF created",
        "file": file
    }
    
from services.research_service import run_company_research


@router.post("/research")
def research_company(data: dict):

    company_name = data.get("company")

    result = run_company_research(company_name)

    return result

from discord.settings import discord_settings


@router.post("/discord-settings")
def save_discord_settings(data: dict):

    discord_settings["webhook_url"] = data.get("webhook_url")

    return {
        "message": "Discord settings saved"
    }