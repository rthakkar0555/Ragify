"use client";

import React, { useState, useEffect, useRef } from "react";

export default function HomePage() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);
  const [particles, setParticles] = useState<
    { id: number; left: string; top: string; size: string; delay: string; duration: string; translateY: string }[]
  >([]);

  // Stats State for JS Count-Up Animation
  const statsRef = useRef<HTMLDivElement>(null);
  const [queriesText, setQueriesText] = useState("0M+");
  const [docsText, setDocsText] = useState("0K+");
  const [timeText, setTimeText] = useState("<0min");
  const [statsAnimated, setStatsAnimated] = useState(false);

  // Monitor Scroll for Navbar styling
  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  // Generate 20 floating micro-particles dynamically with random translations
  useEffect(() => {
    const newParticles = Array.from({ length: 20 }).map((_, i) => ({
      id: i,
      left: `${5 + Math.random() * 90}%`,
      top: `${10 + Math.random() * 80}%`,
      size: `${2 + Math.random() * 2}px`, // 2–4px
      delay: `${Math.random() * -8}s`, // Negative delay makes them start mid-animation
      duration: `${4 + Math.random() * 4}s`, // 4-8s duration
      translateY: `${-20 - Math.random() * 40}px`, // random translateY 20-60px
    }));
    setParticles(newParticles);
  }, []);

  // Intersection Observer for Scroll Reveals
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
          }
        });
      },
      { threshold: 0.1 }
    );
    const elements = document.querySelectorAll(".reveal-element");
    elements.forEach((el) => observer.observe(el));
    return () => observer.disconnect();
  }, []);

  // Intersection Observer for Stats Count-Up
  useEffect(() => {
    const statsEl = statsRef.current;
    if (!statsEl) return;

    const animateValue = (
      start: number,
      end: number,
      duration: number,
      callback: (value: number) => void
    ) => {
      let startTimestamp: number | null = null;
      const step = (timestamp: number) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const easeOutQuad = progress * (2 - progress);
        const current = Math.floor(easeOutQuad * (end - start) + start);
        callback(current);
        if (progress < 1) {
          window.requestAnimationFrame(step);
        } else {
          callback(end);
        }
      };
      window.requestAnimationFrame(step);
    };

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !statsAnimated) {
            setStatsAnimated(true);

            // Count Queries: 0 to 10 over 2s
            animateValue(0, 10, 2000, (v) => setQueriesText(`${v}M+`));

            // Count Documents: 0 to 50 over 2s
            animateValue(0, 50, 2000, (v) => setDocsText(`${v}K+`));

            // Count Time: 0 to 5 over 2s (retaining the < suffix)
            animateValue(0, 5, 2000, (v) => setTimeText(`<${v}min`));

            observer.unobserve(statsEl);
          }
        });
      },
      { threshold: 0.15 }
    );

    observer.observe(statsEl);
    return () => observer.disconnect();
  }, [statsAnimated]);

  // Card 3D Tilt Handlers (Skip on touch devices)
  const handleMouseMove = (e: React.MouseEvent<HTMLDivElement>) => {
    if ("ontouchstart" in window || window.innerWidth < 768) return;
    const card = e.currentTarget;
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    const centerX = rect.width / 2;
    const centerY = rect.height / 2;
    const rotateX = ((centerY - y) / centerY) * 8; // Max 8 degrees tilt
    const rotateY = ((x - centerX) / centerX) * 8; // Max 8 degrees tilt
    card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(8px)`;
    card.style.transition = "transform 0.15s ease-out";
  };

  const handleMouseLeave = (e: React.MouseEvent<HTMLDivElement>) => {
    const card = e.currentTarget;
    card.style.transform = "perspective(800px) rotateX(0deg) rotateY(0deg) translateZ(0px)";
    card.style.transition = "transform 0.5s ease-out";
  };

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const closeMenu = () => {
    setIsMenuOpen(false);
  };

  // Keyboard accessibility: trap focus inside mobile navigation overlay
  useEffect(() => {
    if (!isMenuOpen) return;
    const focusableElements = document.querySelectorAll(
      ".mobile-menu-overlay a, .mobile-menu-overlay button"
    );
    if (focusableElements.length === 0) return;
    const firstElement = focusableElements[0] as HTMLElement;
    const lastElement = focusableElements[focusableElements.length - 1] as HTMLElement;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key !== "Tab") return;
      if (e.shiftKey) {
        if (document.activeElement === firstElement) {
          lastElement.focus();
          e.preventDefault();
        }
      } else {
        if (document.activeElement === lastElement) {
          firstElement.focus();
          e.preventDefault();
        }
      }
    };

    // Set initial focus
    firstElement.focus();

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isMenuOpen]);

  // Smooth scroll support using Javascript scrollIntoView integration
  useEffect(() => {
    const handleHashClick = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      const link = target.closest("a");
      if (!link) return;
      const href = link.getAttribute("href");
      if (href && href.startsWith("#")) {
        e.preventDefault();
        const id = href.substring(1);
        const element = id === "" ? document.body : document.getElementById(id);
        if (element) {
          element.scrollIntoView({ behavior: "smooth" });
          window.history.pushState(null, "", href);
        }
      }
    };
    document.addEventListener("click", handleHashClick);
    return () => document.removeEventListener("click", handleHashClick);
  }, []);

  // Concentric ring configurations for the 3D Orb visualizer (8 rings with decreasing opacity)
  const orbRings = [
    { size: "100%", rotX: "65deg", rotY: "25deg", color: "rgba(0, 255, 255, 0.08)", speed: "18s", cw: true }, // Outermost (0.08 opacity)
    { size: "85%", rotX: "45deg", rotY: "-35deg", color: "rgba(0, 255, 255, 0.15)", speed: "14s", cw: false },
    { size: "70%", rotX: "75deg", rotY: "15deg", color: "rgba(0, 255, 255, 0.25)", speed: "22s", cw: true },
    { size: "55%", rotX: "-55deg", rotY: "45deg", color: "rgba(0, 255, 255, 0.35)", speed: "12s", cw: false },
    { size: "40%", rotX: "35deg", rotY: "-65deg", color: "rgba(0, 255, 255, 0.45)", speed: "16s", cw: true },
    { size: "25%", rotX: "80deg", rotY: "60deg", color: "rgba(0, 255, 255, 0.55)", speed: "10s", cw: false },
    { size: "15%", rotX: "-25deg", rotY: "-15deg", color: "rgba(0, 255, 255, 0.65)", speed: "8s", cw: true },
    { size: "8%", rotX: "10deg", rotY: "45deg", color: "rgba(0, 255, 255, 0.8)", speed: "6s", cw: false } // Innermost (0.8 opacity)
  ];

  return (
    <>
      {/* ───────────────── 1. NAVBAR ───────────────── */}
      <header className={`navbar-header ${isScrolled ? "scrolled" : ""}`}>
        <div className="nav-container">
          <a href="#" className="logo" onClick={closeMenu}>
            RAGify<span>.</span>
          </a>

          <nav className="nav-links">
            <a href="#platform" className="nav-link">Platform</a>
            <a href="#solutions" className="nav-link">Solutions</a>
            <a href="#docs" className="nav-link">Documentation</a>
            <a href="#pricing" className="nav-link">Pricing</a>
          </nav>

          <div className="nav-actions">
            <button className="btn-signin">Sign In</button>
            <button className="btn-deploy">Deploy Now</button>
          </div>

          <button
            className={`hamburger ${isMenuOpen ? "active" : ""}`}
            onClick={toggleMenu}
            aria-label="Toggle navigation menu"
          >
            <span className="hamburger-line"></span>
            <span className="hamburger-line"></span>
            <span className="hamburger-line"></span>
          </button>
        </div>
      </header>

      {/* Mobile Slide-down Menu stacked vertically */}
      <div className={`mobile-menu-overlay ${isMenuOpen ? "active" : ""}`}>
        <a href="#platform" className="mobile-menu-link" onClick={closeMenu}>Platform</a>
        <a href="#solutions" className="mobile-menu-link" onClick={closeMenu}>Solutions</a>
        <a href="#docs" className="mobile-menu-link" onClick={closeMenu}>Documentation</a>
        <a href="#pricing" className="mobile-menu-link" onClick={closeMenu}>Pricing</a>
        <div style={{ display: "flex", flexDirection: "column", gap: "16px", width: "100%", maxWidth: "240px", marginTop: "16px" }}>
          <button className="btn-signin" style={{ padding: "12px", width: "100%", border: "1px solid rgba(99,179,237,0.15)", borderRadius: "8px" }} onClick={closeMenu}>
            Sign In
          </button>
          <button className="btn-deploy" style={{ padding: "12px", width: "100%" }} onClick={closeMenu}>
            Deploy Now
          </button>
        </div>
      </div>

      {/* ───────────────── 2. HERO SECTION ───────────────── */}
      <section className="hero">
        <div className="hero-radial-bg"></div>
        <div className="hero-dot-grid"></div>

        {/* Dynamic Float Particles */}
        <div className="particle-field">
          {particles.map((p) => (
            <div
              key={p.id}
              className="particle"
              style={{
                left: p.left,
                top: p.top,
                width: p.size,
                height: p.size,
                animationDelay: p.delay,
                animationDuration: p.duration,
                "--translate-y": p.translateY,
              } as React.CSSProperties}
            ></div>
          ))}
        </div>

        <div className="hero-content">
          <h1 className="hero-title text-shimmer">RAGify</h1>
          <p className="hero-subtitle">
            POST your data. GET intelligent answers.
            <br />
            We handle everything in between.
          </p>

          <div className="hero-ctas">
            <button className="btn-cta-starter">Start for Free</button>
            <button className="btn-cta-docs">Read the Docs</button>
          </div>
        </div>

        {/* 3D concentric portal rings (orb) with decreasing outward opacity */}
        <div className="orb-viewport">
          <div className="orb-container">
            <div className="orb-center-glow"></div>
            {orbRings.map((ring, idx) => (
              <div
                key={idx}
                className="orb-ring"
                style={{
                  width: ring.size,
                  height: ring.size,
                  zIndex: idx + 1,
                  animation: `${ring.cw ? "spin-cw" : "spin-ccw"} ${ring.speed} linear infinite`,
                  boxShadow: idx === 0 ? "0 0 60px rgba(0, 255, 255, 0.1)" : undefined, // Faint glow on outermost ring
                  // CSS variables to configure parameters for raw CSS keyframes
                  "--rot-x": ring.rotX,
                  "--rot-y": ring.rotY,
                  "--ring-border": ring.color,
                } as React.CSSProperties}
              ></div>
            ))}
          </div>
        </div>
      </section>

      {/* ───────────────── 3. STATS BAR ───────────────── */}
      <section className="stats-bar" ref={statsRef}>
        <div className="stats-container">
          <div className="stat-item">
            <div className="stat-number">{queriesText}</div>
            <div className="stat-label">Queries Processed</div>
          </div>
          <div className="stat-divider"></div>
          <div className="stat-item">
            <div className="stat-number">{docsText}</div>
            <div className="stat-label">Documents Indexed</div>
          </div>
          <div className="stat-divider"></div>
          <div className="stat-item">
            <div className="stat-number">{timeText}</div>
            <div className="stat-label">Time to First Query</div>
          </div>
        </div>
      </section>

      {/* ───────────────── 4. ORCHESTRATING INTELLIGENCE ───────────────── */}
      <section className="section-padding" id="platform">
        <div className="section-container">
          <div className="section-header reveal-element">
            <h2 className="section-title">Orchestrating Intelligence</h2>
            <div className="section-underline"></div>
          </div>

          <div className="grid-3col">
            {/* Card 1 */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "0ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper" style={{ animationDelay: "0s" }}>
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#3B82F6" }}>
                    <rect x="3" y="3" width="18" height="18" rx="2" ry="2" />
                    <polyline points="17 8 12 3 7 8" />
                    <line x1="12" y1="3" x2="12" y2="15" />
                  </svg>
                </div>
                <h3 className="card-title-3d">POST Your Content</h3>
                <p className="card-desc-3d">
                  Sync your data from any source. PDFs, API endpoints, or raw text — we ingest
                  everything into high-dimensional vector space.
                </p>
              </div>
            </div>

            {/* Card 2 */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "150ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper" style={{ animationDelay: "0.5s" }}>
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#06b6d4" }}>
                    <path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
                    <path d="M12 2a4 4 0 0 1 4 4c0 3-4 6-4 6s-4-3-4-6a4 4 0 0 1 4-4z" />
                    <path d="M19 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0z" />
                  </svg>
                </div>
                <h3 className="card-title-3d">We Process Everything</h3>
                <p className="card-desc-3d">
                  Our autonomous pipeline handles chunking, embedding generation, and metadata
                  enrichment without manual tuning.
                </p>
              </div>
            </div>

            {/* Card 3 */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "300ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper" style={{ animationDelay: "1s" }}>
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#00ffff" }}>
                    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
                  </svg>
                </div>
                <h3 className="card-title-3d">GET Intelligent Answers</h3>
                <p className="card-desc-3d">
                  Query your data via natural language. Receive hallucination-free, cited responses
                  through our production-ready API.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ───────────────── 5. READY IN 4 LINES OF CODE ───────────────── */}
      <section className="section-padding" id="docs" style={{ borderTop: "1px solid rgba(99,179,237,0.05)", borderBottom: "1px solid rgba(99,179,237,0.05)" }}>
        <div className="section-container">
          <div className="code-section-layout">
            {/* Left Info Col */}
            <div className="code-info-col reveal-element">
              <h2 className="code-title">Ready in 4 Lines of Code</h2>
              <p className="code-desc">
                Stop building glue code. RAGify provides a unified interface for the entire
                retrieval-augmented generation lifecycle.
              </p>
              <div className="bullets-list">
                <div className="bullet-item">
                  <span className="bullet-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12" />
                    </svg>
                  </span>
                  Managed Vector Databases
                </div>
                <div className="bullet-item">
                  <span className="bullet-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12" />
                    </svg>
                  </span>
                  SOTA Embedding Models
                </div>
                <div className="bullet-item">
                  <span className="bullet-icon">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                      <polyline points="20 6 9 17 4 12" />
                    </svg>
                  </span>
                  Built-in Reranking & Retrieval
                </div>
              </div>
            </div>

            {/* Right Terminal Col - 3D floating window card */}
            <div className="terminal-wrapper reveal-element">
              <div className="terminal-card">
                <div className="terminal-header">
                  <div className="terminal-dots">
                    <span className="terminal-dot red"></span>
                    <span className="terminal-dot yellow"></span>
                    <span className="terminal-dot green"></span>
                  </div>
                  <div className="terminal-title">main.py</div>
                </div>
                <div className="terminal-body">
                  <pre className="terminal-code">
                    <span className="code-keyword">from</span> ragify <span className="code-keyword">import</span> <span className="code-class">RAGify</span>{`\n\n`}
                    client = <span className="code-class">RAGify</span>(api_key=<span className="code-string">&quot;rg_live_...&quot;</span>){`\n\n`}
                    client.<span className="code-method">ingest</span>.<span className="code-method">file</span>({`\n`}    <span className="code-string">&quot;./docs/handbook.pdf&quot;</span>,{`\n`}    index_id=<span className="code-string">&quot;my-index&quot;</span>{`\n`}){`\n\n`}
                    response = client.<span className="code-method">query</span>({`\n`}    <span className="code-string">&quot;What is our parental leave policy?&quot;</span>,{`\n`}    index_id=<span className="code-string">&quot;my-index&quot;</span>{`\n`}){`\n\n`}
                    <span className="code-method">print</span>(response.<span className="code-method">answer</span>)
                  </pre>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ───────────────── 6. SCROLLING MARQUEE ───────────────── */}
      <section className="marquee-fade-overlay">
        <div className="marquee-container">
          {/* Row 1 scrolls LEFT */}
          <div className="marquee-row scroll-left">
            <div className="marquee-inner">
              {["CSV", "MP3", "MP4", "NOTION", "SLACK", "GITHUB", "PDF", "DOCX", "JSON", "AUDIO", "VIDEO", "IMAGES"].map((tag, idx) => (
                <div key={idx} className="marquee-badge">{tag}</div>
              ))}
            </div>
            <div className="marquee-inner" aria-hidden="true">
              {["CSV", "MP3", "MP4", "NOTION", "SLACK", "GITHUB", "PDF", "DOCX", "JSON", "AUDIO", "VIDEO", "IMAGES"].map((tag, idx) => (
                <div key={`dup-${idx}`} className="marquee-badge">{tag}</div>
              ))}
            </div>
          </div>

          {/* Row 2 scrolls RIGHT */}
          <div className="marquee-row scroll-right">
            <div className="marquee-inner">
              {["WEBSITES", "XLSX", "PARQUET", "YOUTUBE", "CONFLUENCE", "SALESFORCE", "POSTGRES", "S3", "REST API", "CODE"].map((tag, idx) => (
                <div key={idx} className="marquee-badge">{tag}</div>
              ))}
            </div>
            <div className="marquee-inner" aria-hidden="true">
              {["WEBSITES", "XLSX", "PARQUET", "YOUTUBE", "CONFLUENCE", "SALESFORCE", "POSTGRES", "S3", "REST API", "CODE"].map((tag, idx) => (
                <div key={`dup-${idx}`} className="marquee-badge">{tag}</div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* ───────────────── 7. FEATURES GRID ───────────────── */}
      <section className="section-padding" id="solutions">
        <div className="section-container">
          <div className="section-header reveal-element">
            <h2 className="section-title">Everything You Need to Ship</h2>
            <div className="section-underline"></div>
          </div>

          <div className="grid-2col-tablet">
            {/* Feature Card 1 - Any Content */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "0ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#3B82F6" }}>
                    <path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z" />
                    <line x1="12" y1="11" x2="12" y2="17" />
                    <line x1="9" y1="14" x2="15" y2="14" />
                  </svg>
                </div>
                <h3 className="card-title-3d">🗂 Any Content</h3>
                <p className="card-desc-3d">
                  Direct integration with your SaaS stack and local file systems.
                </p>
              </div>
            </div>

            {/* Feature Card 2 - Instant API */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "100ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#06b6d4" }}>
                    <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
                  </svg>
                </div>
                <h3 className="card-title-3d">⚡ Instant API</h3>
                <p className="card-desc-3d">
                  Low-latency REST endpoints for production-grade applications.
                </p>
              </div>
            </div>

            {/* Feature Card 3 - Hybrid Retrieval */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "200ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#00ffff" }}>
                    <circle cx="11" cy="11" r="8" />
                    <line x1="21" y1="21" x2="16.65" y2="16.65" />
                    <line x1="11" y1="8" x2="11" y2="14" />
                    <line x1="8" y1="11" x2="14" y2="11" />
                  </svg>
                </div>
                <h3 className="card-title-3d">🔍 Hybrid Retrieval</h3>
                <p className="card-desc-3d">
                  Semantic search paired with keyword matching for precision retrieval.
                </p>
              </div>
            </div>

            {/* Feature Card 4 - Audio & Video RAG */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "300ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#3B82F6" }}>
                    <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z" />
                    <path d="M19 10v2a7 7 0 0 1-14 0v-2" />
                    <line x1="12" y1="19" x2="12" y2="23" />
                  </svg>
                </div>
                <h3 className="card-title-3d">🎙 Audio & Video RAG</h3>
                <p className="card-desc-3d">
                  Extract and query context from multimedia files automatically.
                </p>
              </div>
            </div>

            {/* Feature Card 5 - Agentic Mode */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "400ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#06b6d4" }}>
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" />
                    <polyline points="3.27 6.96 12 12.01 20.73 6.96" />
                  </svg>
                </div>
                <h3 className="card-title-3d">🤖 Agentic Mode</h3>
                <p className="card-desc-3d">
                  Tool-calling agents that can act on retrieved information dynamically.
                </p>
              </div>
            </div>

            {/* Feature Card 6 - Observability */}
            <div className="card-perspective reveal-element" style={{ transitionDelay: "500ms" }}>
              <div
                className="card-3d"
                onMouseMove={handleMouseMove}
                onMouseLeave={handleMouseLeave}
              >
                <div className="icon-wrapper">
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" style={{ color: "#00ffff" }}>
                    <line x1="18" y1="20" x2="18" y2="10" />
                    <line x1="12" y1="20" x2="12" y2="4" />
                    <line x1="6" y1="20" x2="6" y2="14" />
                    <line x1="2" y1="20" x2="22" y2="20" />
                  </svg>
                </div>
                <h3 className="card-title-3d">📊 Observability</h3>
                <p className="card-desc-3d">
                  Full trace logs for every query to monitor RAG performance in real-time.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ───────────────── 8. PRICING SECTION ───────────────── */}
      <section className="section-padding pricing-section" id="pricing">
        <div className="section-container">
          <div className="section-header reveal-element">
            <h2 className="section-title">Simple Scale-Out Pricing</h2>
            <div className="section-underline"></div>
          </div>

          <div className="pricing-layout">
            {/* Starter Tier */}
            <div className="pricing-card reveal-element" style={{ transitionDelay: "0ms" }}>
              <div>
                <div className="pricing-label">Starter</div>
                <div className="pricing-price">$0<span>/mo</span></div>
                <ul className="pricing-features">
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check">✓</span> 500 Documents
                  </li>
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check">✓</span> 1,000 Queries
                  </li>
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check">✓</span> Community Support
                  </li>
                </ul>
              </div>
              <button className="btn-pricing outline">Get Started</button>
            </div>

            {/* Growth Tier (Elevated, Order -1 on mobile overlay) */}
            <div className="pricing-card elevated reveal-element" style={{ transitionDelay: "150ms" }}>
              <div className="pricing-badge">Popular</div>
              <div>
                <div className="pricing-label">Growth</div>
                <div className="pricing-price">$79<span>/mo</span></div>
                <ul className="pricing-features">
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check" style={{ color: "#3B82F6" }}>✓</span> 10,000 Documents
                  </li>
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check" style={{ color: "#3B82F6" }}>✓</span> Unlimited Queries
                  </li>
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check" style={{ color: "#3B82F6" }}>✓</span> Priority API Access
                  </li>
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check" style={{ color: "#3B82F6" }}>✓</span> 99.99% Uptime SLA
                  </li>
                </ul>
              </div>
              <button className="btn-pricing solid">Deploy Growth</button>
            </div>

            {/* Enterprise Tier */}
            <div className="pricing-card reveal-element" style={{ transitionDelay: "300ms" }}>
              <div>
                <div className="pricing-label">Enterprise</div>
                <div className="pricing-price">Custom</div>
                <ul className="pricing-features">
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check">✓</span> Unlimited Docs
                  </li>
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check">✓</span> Custom Model Support
                  </li>
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check">✓</span> On-prem Deployment
                  </li>
                  <li className="pricing-feature-item">
                    <span className="pricing-feature-check">✓</span> Dedicated Engineer
                  </li>
                </ul>
              </div>
              <button className="btn-pricing outline">Contact Sales</button>
            </div>
          </div>
        </div>
      </section>

      {/* ───────────────── 9. FOOTER ───────────────── */}
      <footer className="footer">
        <div className="footer-container">
          <div className="footer-left">
            <a href="#" className="logo">
              RAGify<span>.</span>
            </a>
            <p className="footer-copy">
              © 2026 RAGify Infrastructure. Built for the era of intelligence.
            </p>
          </div>

          <div className="footer-links">
            <a href="#docs" className="footer-link">Documentation</a>
            <a href="#api" className="footer-link">API Reference</a>
            <a href="#status" className="footer-link">Status</a>
            <a href="#github" className="footer-link">GitHub</a>
            <a href="#privacy" className="footer-link">Privacy Policy</a>
          </div>
        </div>
      </footer>
    </>
  );
}

