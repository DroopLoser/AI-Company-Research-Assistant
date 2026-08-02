"use client";

import { useState } from "react";
import { Search, Zap, Radio } from "lucide-react";

// ---------------------------------------------------------------------------
// Relu Consultancy — AI Company Intelligence
// Top header (brand) + centered hero workspace
// ---------------------------------------------------------------------------

const MODEL = "Claude Sonnet 5";

const EXAMPLE_COMPANIES = ["Stripe", "Anduril", "Snowflake", "Ramp", "Figma"];

export default function Page() {
  const [query, setQuery] = useState("");

  const [loading, setLoading] = useState(false);

  const [result, setResult] = useState<any>(null);

  const [error, setError] = useState("");

  async function handleResearch() {

    if (!query.trim()) return;

    try {

      setLoading(true);
      setError("");
      setResult(null);


      const response = await fetch(
        "https://ai-company-research-assistant-qrhh.onrender.com/research/research",
        {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            company: query,
          }),
        }
      );


      if (!response.ok) {
        throw new Error("Research failed");
      }


      const data = await response.json();


      setResult(data);


    } catch (err) {

      setError(
        "Unable to complete research. Check backend connection."
      );

    } finally {

      setLoading(false);

    }
  }

  return (
    <div className="flex min-h-screen w-full flex-col bg-[#101218] text-white antialiased">
      {/* ------------------------------------------------------------- */}
      {/* TOP HEADER — brand only                                        */}
      {/* ------------------------------------------------------------- */}
      <header className="flex items-center justify-center gap-2.5 border-b border-[#343D3F]/60 px-8 py-5">
        <div className="flex h-8 w-8 items-center justify-center rounded-md border border-[#EAB54D]/40 bg-[#EAB54D]/10">
          <span className="font-mono text-[13px] font-semibold text-[#EAB54D]">R</span>
        </div>
        <div className="leading-tight">
          <p className="font-['Inter'] text-[13.5px] font-semibold tracking-tight text-white">
            Relu Consultancy
          </p>
          <p className="font-mono text-[10px] uppercase tracking-[0.14em] text-white/45">
            intelligence engine
          </p>
        </div>
      </header>

      {/* ------------------------------------------------------------- */}
      {/* MAIN — hero workspace                                          */}
      {/* ------------------------------------------------------------- */}
      <main className="relative flex flex-1 flex-col items-center justify-center">
        {/* ambient background */}
        <div
          className="pointer-events-none absolute inset-0"
          style={{
            backgroundImage:
              "radial-gradient(circle at 62% 38%, rgba(212,175,95,0.08), transparent 45%)",
          }}
        />

        <div className="relative z-10 flex w-full max-w-[720px] flex-col items-center px-8 text-center">
          {/* live status badge */}
          <div className="mb-8 flex items-center gap-2 rounded-full border border-[#343D3F]/60 bg-[#343D3F]/20 px-3 py-1.5 backdrop-blur-sm">
            <span className="relative flex h-1.5 w-1.5">
              <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-[#EAB54D] opacity-75" />
              <span className="relative inline-flex h-1.5 w-1.5 rounded-full bg-[#EAB54D]" />
            </span>
            <span className="font-mono text-[10.5px] uppercase tracking-[0.14em] text-white/60">
              Live · 4,812 companies indexed today
            </span>
          </div>

          {/* eyebrow */}
          <div className="mb-5 flex items-center gap-2 font-mono text-[11px] uppercase tracking-[0.2em] text-[#EAB54D]">
            <Zap size={12} strokeWidth={2.5} />
            AI-Powered Intelligence
          </div>

          {/* headline */}
          <h1 className="font-['Inter'] text-[52px] font-semibold leading-[1.05] tracking-[-0.03em] text-white sm:text-[64px]">
            Know any company
            <br />
            in <span className="text-[#EAB54D]">minutes</span>, not weeks
          </h1>

          {/* description */}
          <p className="mt-6 max-w-[520px] font-['Inter'] text-[15.5px] leading-relaxed text-white/60">
            Enter a company name and get a structured intelligence dossier —
            leadership, funding, market position, and risk signals —
            synthesized live from public sources.
          </p>

          {/* example pills */}
          <div className="mt-8 flex flex-wrap items-center justify-center gap-2">
            {EXAMPLE_COMPANIES.map((c) => (
              <button
                key={c}
                onClick={() => setQuery(c)}
                className="rounded-full border border-[#343D3F]/60 bg-[#343D3F]/20 px-3.5 py-1.5 font-mono text-[12px] text-white/60 transition-colors hover:border-[#EAB54D]/40 hover:text-white"
              >
                {c}
              </button>
            ))}
          </div>

          {/* command search bar */}
          <div className="mt-12 w-full max-w-[560px]">
            <div className="flex items-center gap-3 rounded-xl border border-[#343D3F]/60 bg-[#343D3F]/25 px-4 py-3 shadow-[0_0_0_1px_rgba(255,255,255,0.02)_inset,0_20px_40px_-20px_rgba(0,0,0,0.8)] backdrop-blur-md transition-colors focus-within:border-[#EAB54D]/40">
              <Search size={16} className="shrink-0 text-white/45" />
              <input
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search a company, domain, or ticker…"
                className="flex-1 bg-transparent font-['Inter'] text-[14px] text-white placeholder:text-white/35 outline-none"
              />
              <span className="hidden shrink-0 items-center gap-1 rounded border border-[#343D3F]/60 bg-[#343D3F]/20 px-1.5 py-0.5 font-mono text-[10px] text-white/45 sm:flex">
                ⌘K
              </span>
              <button 
                onClick={handleResearch}
                className="flex shrink-0 items-center gap-2 rounded-lg bg-[#EAB54D] px-4 py-2 font-mono text-[12px] font-semibold uppercase tracking-[0.06em] text-black shadow-[0_1px_0_0_rgba(255,255,255,0.25)_inset] transition-all hover:brightness-[1.08] active:brightness-95"
                disabled={loading}
              >
                {loading ? "Researching…" : "Research"}
              </button>
            </div>
            <p className="mt-3 flex items-center justify-center gap-1.5 font-mono text-[10.5px] text-white/35">
              <Radio size={11} />
              
            </p>
          </div>
          {error && (
  <p className="mt-6 text-red-400 font-mono text-sm">
    {error}
  </p>
)}


{result && (
  <div className="mt-8 w-full rounded-xl border border-[#343D3F] bg-[#343D3F]/20 p-6 text-left">

    <h2 className="text-xl font-semibold text-[#EAB54D]">
      {result.report?.company_name}
    </h2>


    <p className="mt-2 text-white/60">
      {result.report?.website}
    </p>


    <h3 className="mt-5 font-semibold">
      Products / Services
    </h3>

    <ul className="mt-2 list-disc pl-5 text-white/70">

      {result.report?.products_services?.map(
        (item:string)=>(
          <li key={item}>
            {item}
          </li>
        )
      )}

    </ul>


    <h3 className="mt-5 font-semibold">
      Pain Points
    </h3>

    <ul className="mt-2 list-disc pl-5 text-white/70">

      {result.report?.pain_points?.map(
        (item:string)=>(
          <li key={item}>
            {item}
          </li>
        )
      )}

    </ul>


    {result.pdf && (
      <a
        href={`http://127.0.0.1:8000/${result.pdf}`}
        target="_blank"
        className="inline-block mt-6 rounded-lg bg-[#EAB54D] px-4 py-2 text-black font-semibold"
      >
        Download PDF
      </a>
    )}

  </div>
)}
        </div>
      </main>
    </div>
  );
}
