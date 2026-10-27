import os

def read_file(name):
    with open(name, 'r', encoding='utf-8') as f:
        return f.read().strip()

hero_bg = read_file('hero_bg_full.png.b64.txt')
laptop_banner = read_file('laptop_banner.png.b64.txt')
header_logo = read_file('header_logo.png.b64.txt')
footer_logo = read_file('footer_logo.png.b64.txt')

template_part1 = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>مرصاد | منصة الذكاء الاصطناعي للبحث العلمي العربي</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Reem+Kufi:wght@500;600;700&family=Aref+Ruqaa:wght@400;700&display=swap" rel="stylesheet" />
<style>
  :root {
    --primary-navy: #0c2a4d;
    --primary-deep: #0b233f;
    --accent-blue: #1d68bd;
    --accent-blue-hover: #15529a;
    --accent-gold: #c6a052;
    --card-cream: #faf9f6;
    --card-border: #e6ebf1;
    --card-shadow: 0 4px 14px rgba(12, 42, 77, 0.04);
    --text-dark: #122840;
    --text-muted: #64748b;
    --text-desc: #7b8a9b;
    --bg-light: #f5f7f9;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Cairo', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-light);
    color: var(--text-dark);
    direction: rtl;
    text-align: right;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }

  a {
    text-decoration: none;
    color: inherit;
  }

  /* Container */
  .container {
    max-width: 1260px;
    margin: 0 auto;
    padding: 0 16px;
  }

  /* HEADER */
  header.site-header {
    background: #ffffff;
    border-bottom: 1px solid #ebf0f5;
    position: sticky;
    top: 0;
    z-index: 100;
  }
  .header-inner {
    max-width: 1260px;
    margin: 0 auto;
    padding: 8px 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .header-brand {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .header-logo-img {
    height: 48px;
    width: auto;
    object-fit: contain;
  }
  .header-nav {
    display: flex;
    align-items: center;
    gap: 28px;
  }
  .nav-link {
    font-size: 15px;
    font-weight: 600;
    color: #334155;
    position: relative;
    padding: 6px 2px;
    transition: color 0.2s;
  }
  .nav-link:hover {
    color: var(--accent-blue);
  }
  .nav-link.active {
    color: #0c2a4d;
    font-weight: 700;
  }
  .nav-link.active::after {
    content: '';
    position: absolute;
    bottom: -6px;
    right: 0;
    left: 0;
    height: 3px;
    background-color: var(--accent-blue);
    border-radius: 2px;
  }
  .nav-dropdown-arrow {
    display: inline-block;
    font-size: 11px;
    margin-right: 4px;
    vertical-align: middle;
  }
  .header-actions {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .btn-header-whatsapp {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 6px 16px;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    font-size: 13.5px;
    font-weight: 700;
    color: #1e293b;
    background: #ffffff;
    transition: all 0.2s;
  }
  .btn-header-whatsapp:hover {
    border-color: #25D366;
    color: #128C7E;
    background: #f0fdf4;
  }
  .btn-header-call {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 7px 18px;
    border-radius: 8px;
    font-size: 13.5px;
    font-weight: 700;
    color: #ffffff;
    background: var(--primary-navy);
    transition: background 0.2s;
  }
  .btn-header-call:hover {
    background: #143863;
  }

  /* HERO SECTION */
  .hero-section {
    position: relative;
    min-height: 270px;
    background-color: #0b2444;
"""

template_part2 = """
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    display: flex;
    align-items: center;
    overflow: hidden;
  }
  .hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, rgba(11,36,68,0) 0%, rgba(11,36,68,0.2) 30%, rgba(11,36,68,0.55) 65%, rgba(11,36,68,0.75) 100%);
    pointer-events: none;
  }
  .hero-container {
    position: relative;
    z-index: 2;
    max-width: 1260px;
    width: 100%;
    margin: 0 auto;
    padding: 24px 20px;
    display: flex;
    justify-content: flex-end;
  }
  .hero-content {
    max-width: 760px;
    text-align: right;
  }
  .hero-title-group {
    margin-bottom: 8px;
  }
  .hero-brand-name {
    font-family: 'Reem Kufi', sans-serif;
    font-size: 42px;
    font-weight: 700;
    color: #deb35c;
    line-height: 1.1;
    display: inline-block;
  }
  .hero-slogan {
    font-size: 24px;
    font-weight: 800;
    color: #ffffff;
    margin-top: 4px;
    letter-spacing: -0.3px;
  }
  .hero-description {
    font-size: 13.5px;
    color: #e2e8f0;
    line-height: 1.6;
    margin-bottom: 16px;
    max-width: 620px;
    font-weight: 500;
  }
  .hero-search-box {
    background: #ffffff;
    border-radius: 30px;
    padding: 4px 6px 4px 18px;
    display: flex;
    align-items: center;
    max-width: 590px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.18);
  }
  .hero-search-input {
    flex: 1;
    border: none;
    outline: none;
    font-family: 'Cairo', sans-serif;
    font-size: 14px;
    color: #1e293b;
    padding: 8px 10px;
  }
  .hero-search-input::placeholder {
    color: #94a3b8;
  }
  .hero-search-btn {
    background: #0f2c4f;
    color: #ffffff;
    border: none;
    border-radius: 24px;
    padding: 8px 22px;
    font-family: 'Cairo', sans-serif;
    font-size: 13.5px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: background 0.2s;
  }
  .hero-search-btn:hover {
    background: #19467d;
  }
  .hero-suggestions {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 12px;
  }
  .suggestions-label {
    font-size: 12.5px;
    color: #cbd5e1;
    font-weight: 600;
  }
  .chip-tag {
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #ffffff;
    font-size: 12px;
    font-weight: 600;
    padding: 3px 12px;
    border-radius: 16px;
    transition: all 0.2s;
  }
  .chip-tag:hover {
    background: rgba(255, 255, 255, 0.25);
    color: #fff;
  }

  /* TOOLS GRID - 9 CARDS */
  .tools-section {
    padding: 28px 0 16px;
  }
  .tools-grid {
    display: grid;
    grid-template-columns: repeat(9, 1fr);
    gap: 12px;
  }
  .tool-card {
    background: #fbfbfa;
    border: 1px solid #e7ecf2;
    border-radius: 14px;
    padding: 16px 8px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
  }
  .tool-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 18px rgba(12, 42, 77, 0.08);
    border-color: #cbd5e1;
  }
  .tool-icon-wrap {
    width: 38px;
    height: 38px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0c2a4d;
    margin-bottom: 10px;
  }
  .tool-title {
    font-size: 13.5px;
    font-weight: 800;
    color: #0c2a4d;
    margin-bottom: 6px;
    line-height: 1.3;
  }
  .tool-desc {
    font-size: 10.5px;
    color: #707e94;
    line-height: 1.45;
    font-weight: 500;
  }

  /* MIDDLE SECTION - 2 EQUAL / ASYMMETRIC COLUMNS */
  .features-section {
    padding: 12px 0 20px;
  }
  .features-row {
    display: grid;
    grid-template-columns: 1.8fr 1fr;
    gap: 18px;
  }

  /* Left Banner Card (أدوات متكاملة) */
  .integrated-tools-card {
    background: #ffffff;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    overflow: hidden;
    display: flex;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }
  .integrated-tools-info {
    flex: 1.2;
    padding: 24px 22px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .integrated-tools-title {
    font-size: 21px;
    font-weight: 800;
    color: #0c2a4d;
    margin-bottom: 8px;
  }
  .integrated-tools-desc {
    font-size: 12.5px;
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 14px;
  }
  .integrated-checklist {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 7px;
    margin-bottom: 18px;
  }
  .integrated-checklist li {
    font-size: 12.5px;
    font-weight: 700;
    color: #1e293b;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .check-icon {
    width: 17px;
    height: 17px;
    background: #0c2a4d;
    color: #fff;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    flex-shrink: 0;
  }
  .btn-explore {
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #0c2a4d;
    color: #ffffff;
    font-size: 13px;
    font-weight: 700;
    padding: 8px 18px;
    border-radius: 8px;
    transition: background 0.2s;
  }
  .btn-explore:hover {
    background: #174275;
  }
  .integrated-tools-banner {
    flex: 1;
    position: relative;
    min-height: 220px;
    background-color: #f1ede8;
"""

template_part3 = """
    background-size: cover;
    background-position: center;
  }

  /* Right Card (لماذا مرصاد؟) */
  .why-us-card {
    background: #fbfbfa;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 24px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }
  .why-us-title {
    font-size: 21px;
    font-weight: 800;
    color: #0c2a4d;
    text-align: center;
    margin-bottom: 18px;
  }
  .why-us-list {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .why-us-item {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .why-us-icon-wrap {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: #fbf7ee;
    border: 1px solid #ebd9b0;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #b58d34;
    flex-shrink: 0;
  }
  .why-us-text h4 {
    font-size: 13.5px;
    font-weight: 800;
    color: #0c2a4d;
    line-height: 1.2;
  }
  .why-us-text p {
    font-size: 11px;
    color: #64748b;
    margin-top: 2px;
  }

  /* BOTTOM SECTION - 3 CARDS */
  .bottom-section {
    padding: 10px 0 36px;
  }
  .bottom-row {
    display: grid;
    grid-template-columns: 1fr 1.35fr 0.95fr;
    gap: 16px;
    align-items: stretch;
  }

  /* Left: How to start card */
  .how-to-start-card {
    background: #fbfbfa;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 24px 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }
  .card-top-title {
    font-size: 19px;
    font-weight: 800;
    color: #0c2a4d;
    margin-bottom: 16px;
    text-align: right;
  }
  .steps-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
    margin: 15px 0;
  }
  .step-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 65px;
    position: relative;
    z-index: 2;
  }
  .step-badge {
    position: absolute;
    top: -6px;
    right: 14px;
    width: 16px;
    height: 16px;
    background: #0c2a4d;
    color: #fff;
    font-size: 9.5px;
    font-weight: 700;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #fff;
  }
  .step-circle {
    width: 44px;
    height: 44px;
    background: #ffffff;
    border: 1.5px solid #dbe3ed;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0c2a4d;
    margin-bottom: 8px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.04);
  }
  .step-title {
    font-size: 10.5px;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.3;
  }
  .step-arrow {
    color: #94a3b8;
    font-size: 14px;
    margin-top: -18px;
  }
  .how-to-start-footer-quote {
    font-family: 'Aref Ruqaa', serif;
    font-size: 17px;
    color: #0c2a4d;
    text-align: center;
    margin-top: 14px;
  }

  /* Center: Packages / Latest Articles */
  .packages-container-card {
    background: #fbfbfa;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 20px 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }
  .packages-title {
    font-size: 19px;
    font-weight: 800;
    color: #0c2a4d;
    text-align: center;
    margin-bottom: 16px;
  }
  .packages-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
  }
  .pkg-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    padding: 16px 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
  }
  .pkg-card.highlighted {
    border: 2px solid #1d68bd;
    transform: translateY(-2px);
    box-shadow: 0 6px 16px rgba(29, 104, 189, 0.12);
  }
  .pkg-badge {
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    background: #1d68bd;
    color: #fff;
    font-size: 10px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 10px;
    white-space: nowrap;
  }
  .pkg-name {
    font-size: 15px;
    font-weight: 800;
    color: #0c2a4d;
    margin-bottom: 4px;
  }
  .pkg-price {
    font-size: 12px;
    color: #64748b;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid #f1f5f9;
  }
  .pkg-price strong {
    font-size: 18px;
    color: #0c2a4d;
  }
  .pkg-features {
    list-style: none;
    text-align: right;
    display: flex;
    flex-direction: column;
    gap: 7px;
    margin-bottom: 14px;
    font-size: 11px;
    color: #475569;
  }
  .pkg-features li {
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .pkg-features li::before {
    content: '✓';
    color: #1d68bd;
    font-weight: bold;
    font-size: 12px;
  }
  .pkg-btn {
    display: block;
    width: 100%;
    padding: 7px 0;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 700;
    text-align: center;
    transition: all 0.2s;
  }
  .pkg-btn-outline {
    border: 1.5px solid #0c2a4d;
    color: #0c2a4d;
    background: transparent;
  }
  .pkg-btn-outline:hover {
    background: #0c2a4d;
    color: #fff;
  }
  .pkg-btn-fill {
    background: #1d68bd;
    color: #ffffff;
    border: none;
  }
  .pkg-btn-fill:hover {
    background: #15529a;
  }

  /* Right: Services Card */
  .services-card {
    background: #fbfbfa;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 22px 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 4px 12px rgba(0,0,0,0.03);
  }
  .services-header {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #0c2a4d;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 6px;
  }
  .services-subtext {
    font-size: 11.5px;
    color: #64748b;
    margin-bottom: 12px;
    line-height: 1.5;
  }
  .services-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 7px;
    margin-bottom: 14px;
    font-size: 12px;
    font-weight: 600;
    color: #1e293b;
  }
  .services-list li {
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .services-list li::before {
    content: '✓';
    color: #1d68bd;
    font-weight: 800;
  }
  .contact-notice-box {
    background: #f1f5f9;
    border-right: 3px solid #0c2a4d;
    padding: 8px 10px;
    border-radius: 4px;
    margin-bottom: 12px;
    font-size: 11px;
    color: #334155;
    line-height: 1.5;
  }
  .contact-notice-box a {
    color: #0c2a4d;
    font-weight: bold;
    direction: ltr;
    display: inline-block;
  }
  .services-btn-row {
    display: flex;
    gap: 8px;
  }
  .services-btn-call {
    flex: 1;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    background: #0c2a4d;
    color: #ffffff;
    font-size: 12.5px;
    font-weight: 700;
    padding: 8px 0;
    border-radius: 8px;
    transition: background 0.2s;
  }
  .services-btn-call:hover {
    background: #174275;
  }
  .services-btn-wa {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 12px;
    background: #25D366;
    color: #ffffff;
    border-radius: 8px;
    transition: background 0.2s;
  }
  .services-btn-wa:hover {
    background: #1ebd5b;
  }

  /* FOOTER */
  footer.site-footer {
    background: #0c2a4c;
    color: #ffffff;
    padding: 22px 0 16px;
  }
  .footer-inner {
    max-width: 1260px;
    margin: 0 auto;
    padding: 0 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 16px;
  }
  .footer-brand {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .footer-logo-img {
    height: 44px;
    width: auto;
    object-fit: contain;
  }
  .footer-nav {
    display: flex;
    align-items: center;
    gap: 20px;
  }
  .footer-nav a {
    color: #cbd5e1;
    font-size: 13.5px;
    font-weight: 600;
    transition: color 0.2s;
  }
  .footer-nav a:hover {
    color: #ffffff;
  }
  .footer-social-rights {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
  }
  .footer-social {
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .footer-social a {
    color: #94a3b8;
    transition: color 0.2s;
    display: inline-flex;
  }
  .footer-social a:hover {
    color: #ffffff;
  }
  .footer-rights {
    font-size: 11.5px;
    color: #94a3b8;
  }

  /* SVG Icons Inline */
  .icon-svg {
    width: 20px;
    height: 20px;
    fill: currentColor;
    display: inline-block;
  }
  .icon-svg-sm {
    width: 16px;
    height: 16px;
    fill: currentColor;
    display: inline-block;
  }

  /* Responsive Rules */
  @media (max-width: 1024px) {
    .tools-grid {
      grid-template-columns: repeat(5, 1fr);
    }
    .features-row {
      grid-template-columns: 1fr;
    }
    .bottom-row {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 768px) {
    .header-nav {
      display: none;
    }
    .tools-grid {
      grid-template-columns: repeat(3, 1fr);
    }
    .packages-grid {
      grid-template-columns: 1fr;
    }
    .integrated-tools-card {
      flex-direction: column-reverse;
    }
    .integrated-tools-banner {
      min-height: 180px;
    }
    .footer-inner {
      flex-direction: column;
      text-align: center;
    }
    .footer-social-rights {
      align-items: center;
    }
  }
</style>
</head>
<body>

  <!-- HEADER -->
  <header class="site-header">
    <div class="header-inner">
      <!-- Right: Brand Logo -->
      <div class="header-brand">
"""

template_part4 = """
      </div>

      <!-- Center: Navigation -->
      <nav class="header-nav">
        <a href="#" class="nav-link active">الرئيسية</a>
        <a href="#tools" class="nav-link">الأدوات <span class="nav-dropdown-arrow">▾</span></a>
        <a href="#services" class="nav-link">خدمات الأبحاث</a>
        <a href="#articles" class="nav-link">المقالات</a>
        <a href="#help" class="nav-link">مساعدة</a>
      </nav>

      <!-- Left: CTA Buttons -->
      <div class="header-actions">
        <a href="https://wa.me/201015034659" target="_blank" class="btn-header-whatsapp">
          <svg class="icon-svg-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          <span>واتساب</span>
        </a>
        <a href="tel:01015034659" class="btn-header-call">
          <svg class="icon-svg-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-2.2 2.2a15.045 15.045 0 01-6.59-6.59l2.2-2.21a.96.96 0 00.25-1.01A11.36 11.36 0 018.57 3.9c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.52c0-.55-.45-1-.99-1z"/></svg>
          <span>اتصل الآن</span>
        </a>
      </div>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section class="hero-section">
    <div class="hero-overlay"></div>
    <div class="hero-container">
      <div class="hero-content">
        <div class="hero-title-group">
          <h1 class="hero-brand-name">مِرْصَاد</h1>
          <h2 class="hero-slogan">نرصد المعرفة، ونبني البحث.</h2>
        </div>
        <p class="hero-description">
          منصة ذكاء اصطناعي للباحثين والمعلمين وطلاب الدراسات العليا،<br/>
          تساعدك على إنجاز بحثك بدقة واحترافية، من الفكرة إلى الملف النهائي.
        </p>
        <form class="hero-search-box" action="/search" method="get">
          <input type="text" name="q" class="hero-search-input" placeholder="اكتب موضوع بحثك أو ارفع ملفك..." />
          <button type="submit" class="hero-search-btn">
            <span>ابدأ الآن</span>
            <span>✦</span>
          </button>
        </form>
        <div class="hero-suggestions">
          <span class="suggestions-label">أمثلة مقترحة:</span>
          <a href="/search?q=الدراسات+السابقة" class="chip-tag">الدراسات السابقة</a>
          <a href="/search?q=تحليل+الاستبيان" class="chip-tag">تحليل الاستبيان</a>
          <a href="/search?q=توثيق+المراجع" class="chip-tag">توثيق المراجع</a>
          <a href="/search?q=صياغة+أكاديمية" class="chip-tag">صياغة أكاديمية</a>
        </div>
      </div>
    </div>
  </section>

  <!-- MAIN BODY -->
  <main class="container">

    <!-- TOOLS GRID - 9 CARDS -->
    <section class="tools-section" id="tools">
      <div class="tools-grid">
        
        <!-- 1. المصادر -->
        <a href="/search/label/المصادر" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0016 9.5 6.5 6.5 0 109.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
          </div>
          <h3 class="tool-title">مرصاد المصادر</h3>
          <p class="tool-desc">البحث في قواعد البيانات والمصادر الموثوقة</p>
        </a>

        <!-- 2. الدراسات السابقة -->
        <a href="/search/label/الدراسات%20السابقة" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M21 5c-1.11-.35-2.33-.5-3.5-.5-1.95 0-4.05.4-5.5 1.5-1.45-1.1-3.55-1.5-5.5-1.5S2.45 4.9 1 6v14.65c0 .25.25.5.5.5.1 0 .15-.05.25-.05C3.1 20.45 5.05 20 6.5 20c1.95 0 4.05.4 5.5 1.5 1.35-.85 3.8-1.5 5.5-1.5 1.65 0 3.35.3 4.75 1.05.1.05.15.05.25.05.25 0 .5-.25.5-.5V6c-.6-.45-1.25-.75-2-1zm-1 13c-1.05-.3-2.2-.45-3.5-.45-1.6 0-3.4.4-4.5 1.25V7.5c1.1-.85 2.9-1.25 4.5-1.25 1.3 0 2.45.15 3.5.45V18z"/></svg>
          </div>
          <h3 class="tool-title">مرصاد الدراسات السابقة</h3>
          <p class="tool-desc">تحليل ومقارنة الدراسات وتحديد الفجوة البحثية</p>
        </a>

        <!-- 3. الباحث -->
        <a href="/search/label/الباحث" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
          </div>
          <h3 class="tool-title">مرصاد الباحث</h3>
          <p class="tool-desc">بناء مشكلة البحث والأسئلة والأهداف</p>
        </a>

        <!-- 4. التوثيق -->
        <a href="/search/label/التوثيق" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
          </div>
          <h3 class="tool-title">مرصاد التوثيق</h3>
          <p class="tool-desc">إنشاء الحواشي والمراجع بمختلف الأنماط</p>
        </a>

        <!-- 5. الملفات -->
        <a href="/search/label/الملفات" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z"/></svg>
          </div>
          <h3 class="tool-title">مرصاد الملفات</h3>
          <p class="tool-desc">تحليل ملفات PDF و Word واستخراج المعلومات</p>
        </a>

        <!-- 6. البيانات -->
        <a href="/search/label/البيانات" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/></svg>
          </div>
          <h3 class="tool-title">مرصاد البيانات</h3>
          <p class="tool-desc">تحليل الاستبيانات والبيانات الإحصائية</p>
        </a>

        <!-- 7. الكتابة -->
        <a href="/search/label/الكتابة" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>
          </div>
          <h3 class="tool-title">مرصاد الكتابة</h3>
          <p class="tool-desc">صياغة أكاديمية احترافية مع الحفاظ على صوتك</p>
        </a>

        <!-- 8. المراجعة -->
        <a href="/search/label/المراجعة" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
          </div>
          <h3 class="tool-title">مرصاد المراجعة</h3>
          <p class="tool-desc">اكتشاف التناقضات والثغرات والمشكلات المنهجية</p>
        </a>

        <!-- 9. تصدير Word -->
        <a href="/search/label/تصدير%20Word" class="tool-card">
          <div class="tool-icon-wrap">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
          </div>
          <h3 class="tool-title">تصدير Word</h3>
          <p class="tool-desc">إخراج بحثك في ملف منسق وجاهز</p>
        </a>

      </div>
    </section>

    <!-- MIDDLE SECTION: 2 COLUMNS -->
    <section class="features-section">
      <div class="features-row">
        
        <!-- Left: Integrated tools with laptop banner -->
        <div class="integrated-tools-card">
          <div class="integrated-tools-info">
            <h3 class="integrated-tools-title">أدوات متكاملة لرحلتك البحثية</h3>
            <p class="integrated-tools-desc">
              لا نفهمك للكتابة فقط، بل نساعدك في التحليل والمراجعة والتوثيق،<br/>
              حتى تصل إلى بحث متكامل وجاهز للنشر أو المناقشة.
            </p>
            <ul class="integrated-checklist">
              <li><span class="check-icon">✓</span> مصادر موثوقة ومحدثة</li>
              <li><span class="check-icon">✓</span> نتائج دقيقة وقابلة للتحقق</li>
              <li><span class="check-icon">✓</span> دعم اللغة العربية الأكاديمية</li>
              <li><span class="check-icon">✓</span> تصدير احترافي إلى Word</li>
            </ul>
            <a href="#tools" class="btn-explore">
              <span>استكشف جميع الأدوات</span>
              <span>←</span>
            </a>
          </div>
          <div class="integrated-tools-banner"></div>
        </div>

        <!-- Right: Why us -->
        <div class="why-us-card">
          <h3 class="why-us-title">لماذا مِرْصَاد؟</h3>
          <div class="why-us-list">
            
            <div class="why-us-item">
              <div class="why-us-icon-wrap">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
              </div>
              <div class="why-us-text">
                <h4>يوفر وقتك وجهدك</h4>
                <p>بدلاً من البحث اليدوي الطويل</p>
              </div>
            </div>

            <div class="why-us-item">
              <div class="why-us-icon-wrap">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
              </div>
              <div class="why-us-text">
                <h4>دقة وموثوقية</h4>
                <p>بمصادر حقيقية وقابلة للتحقق</p>
              </div>
            </div>

            <div class="why-us-item">
              <div class="why-us-icon-wrap">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12.87 15.07l-2.54-2.51.03-.03c1.74-1.94 2.98-4.17 3.71-6.53H17V4h-7V2H8v2H1v1.99h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12zm-2.62 7l1.62-4.33L19.12 17h-3.24z"/></svg>
              </div>
              <div class="why-us-text">
                <h4>دعم كامل باللغة العربية</h4>
                <p>بأسلوب أكاديمي واضح وسليم</p>
              </div>
            </div>

            <div class="why-us-item">
              <div class="why-us-icon-wrap">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M4 8h4V4H4v4zm6 12h4v-4h-4v4zm-6 0h4v-4H4v4zm0-6h4v-4H4v4zm6 0h4v-4h-4v4zm6-10v4h4V4h-4zm-6 4h4V4h-4v4zm6 6h4v-4h-4v4zm0 6h4v-4h-4v4z"/></svg>
              </div>
              <div class="why-us-text">
                <h4>مناسب لجميع التخصصات</h4>
                <p>من العلوم الإنسانية إلى العلوم التطبيقية</p>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- BOTTOM SECTION: 3 CARDS -->
    <section class="bottom-section">
      <div class="bottom-row">
        
        <!-- Left: How to start -->
        <div class="how-to-start-card">
          <div>
            <h3 class="card-top-title">كيف تبدأ؟</h3>
            <div class="steps-row">
              
              <div class="step-node">
                <span class="step-badge">4</span>
                <div class="step-circle">
                  <svg class="icon-svg-sm" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
                </div>
                <div class="step-title">أنشئ حسابك<br/>مجانًا</div>
              </div>

              <div class="step-arrow">←</div>

              <div class="step-node">
                <span class="step-badge">2</span>
                <div class="step-circle">
                  <svg class="icon-svg-sm" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
                </div>
                <div class="step-title">أدخل موضوع بحثك<br/>أو ارفع ملفك</div>
              </div>

              <div class="step-arrow">←</div>

              <div class="step-node">
                <span class="step-badge">3</span>
                <div class="step-circle">
                  <svg class="icon-svg-sm" viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>
                </div>
                <div class="step-title">اختر الأداة المناسبة<br/>وابدأ التحليل</div>
              </div>

              <div class="step-arrow">←</div>

              <div class="step-node">
                <span class="step-badge">1</span>
                <div class="step-circle">
                  <svg class="icon-svg-sm" viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
                </div>
                <div class="step-title">استلم النتائج<br/>وقم بتصديرها</div>
              </div>

            </div>
          </div>
          <div class="how-to-start-footer-quote">
            خطوات بسيطة ... ونتيجة احترافية
          </div>
        </div>

        <!-- Center: Packages / Latest Articles -->
        <div class="packages-container-card">
          <h3 class="packages-title">باقات الاشتراك</h3>
          <div class="packages-grid">
            
            <!-- Free / مجاني -->
            <div class="pkg-card">
              <div>
                <h4 class="pkg-name">مجاني</h4>
                <div class="pkg-price"><strong>0</strong> جنيه / شهر</div>
                <ul class="pkg-features">
                  <li>3 عمليات يوميًا</li>
                  <li>تلخيص 3 مصادر</li>
                  <li>أدوات صياغة محدودة</li>
                </ul>
              </div>
              <a href="#" class="pkg-btn pkg-btn-outline">ابدأ الآن</a>
            </div>

            <!-- Researcher / باحث (Highlighted) -->
            <div class="pkg-card highlighted">
              <span class="pkg-badge">الأكثر اختياراً</span>
              <div>
                <h4 class="pkg-name">باحث</h4>
                <div class="pkg-price"><strong>99</strong> جنيه / شهر</div>
                <ul class="pkg-features">
                  <li>استخدام أكبر للأدوات</li>
                  <li>رفع الملفات وتحليلها</li>
                  <li>إنشاء الحواشي والمراجع</li>
                  <li>تصدير Word</li>
                </ul>
              </div>
              <a href="#" class="pkg-btn pkg-btn-fill">اشترك الآن</a>
            </div>

            <!-- Plus / باحث+ -->
            <div class="pkg-card">
              <div>
                <h4 class="pkg-name">باحث+</h4>
                <div class="pkg-price"><strong>249</strong> جنيه / شهر</div>
                <ul class="pkg-features">
                  <li>استخدام غير محدود (ضمن الرصيد)</li>
                  <li>تحليل ملفات كبيرة</li>
                  <li>تحليل الدراسات السابقة</li>
                  <li>تحليل الاستبيانات</li>
                  <li>أدوات متقدمة</li>
                  <li>أولوية في المعالجة</li>
                </ul>
              </div>
              <a href="#" class="pkg-btn pkg-btn-fill">اشترك الآن</a>
            </div>

          </div>
        </div>

        <!-- Right: Services Card -->
        <div class="services-card" id="services">
          <div>
            <div class="services-header">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
              <span>خدمات الباحث</span>
            </div>
            <p class="services-subtext">يمكنك طلب خدمات احترافية من فريق أبحاثنا المتخصص:</p>
            <ul class="services-list">
              <li>تنسيق رسالة ماجستير</li>
              <li>تدقيق لغوي</li>
              <li>تحليل إحصائي</li>
              <li>تفريغ مقابلات</li>
              <li>تنسيق مراجع</li>
            </ul>
            <div class="contact-notice-box">
              للاتفاق على أي عمل فيما يخص الأبحاث العلمية يرجى الاتصال على: <a href="tel:01015034659">01015034659</a>
            </div>
          </div>
          <div class="services-btn-row">
            <a href="tel:01015034659" class="services-btn-call">
              <span>اطلب خدمة الآن</span>
              <span>←</span>
            </a>
            <a href="https://wa.me/201015034659" target="_blank" class="services-btn-wa" title="تواصل عبر واتساب">
              <svg class="icon-svg-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
            </a>
          </div>
        </div>

      </div>
    </section>

  </main>

  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="footer-inner">
      <!-- Right: Brand Logo -->
      <div class="footer-brand">
"""

template_part5 = """
      </div>

      <!-- Center: Links -->
      <nav class="footer-nav">
        <a href="#">الرئيسية</a>
        <a href="#tools">الأدوات</a>
        <a href="#services">خدمات الأبحاث</a>
        <a href="#articles">المقالات</a>
        <a href="#about">من نحن</a>
        <a href="#contact">تواصل معنا</a>
      </nav>

      <!-- Left: Social & Copyright -->
      <div class="footer-social-rights">
        <div class="footer-social">
          <a href="#" title="YouTube"><svg class="icon-svg" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>
          <a href="#" title="X"><svg class="icon-svg" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
          <a href="#" title="Facebook"><svg class="icon-svg" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
          <a href="#" title="LinkedIn"><svg class="icon-svg" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
        </div>
        <div class="footer-rights">© مرصاد. جميع الحقوق محفوظة.</div>
      </div>
    </div>
  </footer>

</body>
</html>
"""

with open('preview.html', 'w', encoding='utf-8') as out:
    out.write(template_part1)
    out.write(f'    background-image: url("{hero_bg}");\n')
    out.write(template_part2)
    out.write(f'    background-image: url("{laptop_banner}");\n')
    out.write(template_part3)
    out.write(f'        <img class="header-logo-img" src="{header_logo}" alt="مرصاد" />\n')
    out.write(template_part4)
    out.write(f'        <img class="footer-logo-img" src="{footer_logo}" alt="مرصاد" />\n')
    out.write(template_part5)

print('preview.html assembled successfully!')
