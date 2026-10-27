import xml.etree.ElementTree as ET
import os

def read_b64(name):
    with open(name + '.b64.txt', 'r', encoding='utf-8') as f:
        return f.read().strip()

hero_left_b64 = read_b64('hero_left_art.png')
lighthouse_b64 = read_b64('lighthouse_only.png')
laptop_art_b64 = read_b64('laptop_banner_clean.png')
header_logo_b64 = read_b64('header_logo_clean.png')
footer_logo_b64 = read_b64('footer_logo_clean.png')

tools = [
    {
        "id": "sources",
        "title": "مرصاد المصادر",
        "desc": "البحث في قواعد البيانات والمصادر الموثوقة",
        "icon": '<svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0016 9.5 6.5 6.5 0 109.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>',
    },
    {
        "id": "literature",
        "title": "مرصاد الدراسات السابقة",
        "desc": "تحليل ومقارنة الدراسات وتحديد الفجوة البحثية",
        "icon": '<svg viewBox="0 0 24 24"><path d="M21 5c-1.11-.35-2.33-.5-3.5-.5-1.95 0-4.05.4-5.5 1.5-1.45-1.1-3.55-1.5-5.5-1.5S2.45 4.9 1 6v14.65c0 .25.25.5.5.5.1 0 .15-.05.25-.05C3.1 20.45 5.05 20 6.5 20c1.95 0 4.05.4 5.5 1.5 1.35-.85 3.8-1.5 5.5-1.5 1.65 0 3.35.3 4.75 1.05.1.05.15.05.25.05.25 0 .5-.25.5-.5V6c-.6-.45-1.25-.75-2-1zm-1 13c-1.05-.3-2.2-.45-3.5-.45-1.6 0-3.4.4-4.5 1.25V7.5c1.1-.85 2.9-1.25 4.5-1.25 1.3 0 2.45.15 3.5.45V18z"/></svg>',
    },
    {
        "id": "researcher",
        "title": "مرصاد الباحث",
        "desc": "بناء مشكلة البحث والأسئلة والأهداف",
        "icon": '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>',
    },
    {
        "id": "citations",
        "title": "مرصاد التوثيق",
        "desc": "إنشاء الحواشي والمراجع بمختلف الأنماط",
        "icon": '<svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>',
    },
    {
        "id": "files",
        "title": "مرصاد الملفات",
        "desc": "تحليل ملفات PDF و Word واستخراج المعلومات",
        "icon": '<svg viewBox="0 0 24 24"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z"/></svg>',
    },
    {
        "id": "data",
        "title": "مرصاد البيانات",
        "desc": "تحليل الاستبيانات والبيانات الإحصائية",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/></svg>',
    },
    {
        "id": "writing",
        "title": "مرصاد الكتابة",
        "desc": "صياغة أكاديمية احترافية مع الحفاظ على صوتك",
        "icon": '<svg viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>',
    },
    {
        "id": "review",
        "title": "مرصاد المراجعة",
        "desc": "اكتشاف التناقضات والثغرات والمشكلات المنهجية",
        "icon": '<svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>',
    },
    {
        "id": "word",
        "title": "تصدير Word",
        "desc": "إخراج بحثك في ملف منسق وجاهز",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>',
    }
]

tools_xml = ""
for t in tools:
    tools_xml += f"""        <div class='tool-card' onclick="openToolModal('{t['title']}', '{t['desc']}')">
          <div class='tool-icon-wrap'>
            {t['icon']}
          </div>
          <h3 class='tool-title'>{t['title']}</h3>
          <p class='tool-desc'>{t['desc']}</p>
        </div>\n"""

# Part 1: XML Header, meta tags, and font imports
part1 = """<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html>
<html b:version='2' class='v2' expr:dir='data:blog.languageDirection' lang='ar' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.blogger.com/2008/html' xmlns:data='http://www.blogger.com/2008/data' xmlns:expr='http://www.blogger.com/2008/expr'>
<head>
  <meta charset='UTF-8'/>
  <meta content='width=device-width, initial-scale=1.0' name='viewport'/>
  
  <b:if cond='data:blog.pageType == &quot;index&quot;'>
    <title><data:blog.pageTitle/></title>
  <b:else/>
    <title><data:blog.pageName/> | <data:blog.title/></title>
  </b:if>

  <!-- SEO and Meta Tags -->
  <b:if cond='data:blog.metaDescription'>
    <meta expr:content='data:blog.metaDescription' name='description'/>
  <b:else/>
    <meta content='مرصاد - منصة الذكاء الاصطناعي للبحث العلمي العربي. نرصد المعرفة، ونبني البحث.' name='description'/>
  </b:if>
  <link expr:href='data:blog.canonicalUrl' rel='canonical'/>

  <!-- Open Graph / Social -->
  <meta expr:content='data:blog.pageTitle' property='og:title'/>
  <meta expr:content='data:blog.canonicalUrl' property='og:url'/>
  <meta expr:content='data:blog.title' property='og:site_name'/>
  <b:if cond='data:blog.postImageUrl'>
    <meta expr:content='data:blog.postImageUrl' property='og:image'/>
  </b:if>
  <meta content='summary_large_image' name='twitter:card'/>

  <!-- Google Fonts Preconnect & Cairo / Reem Kufi / Aref Ruqaa -->
  <link href='https://fonts.googleapis.com' rel='preconnect'/>
  <link crossorigin='' href='https://fonts.gstatic.com' rel='preconnect'/>
  <link href='https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&amp;family=Reem+Kufi:wght@500;600;700&amp;family=Aref+Ruqaa:wght@400;700&amp;display=swap' rel='stylesheet'/>

  <b:skin><![CDATA[
  :root {
    --primary-navy: #0B2A5B;
    --navy-dark: #071D3E;
    --accent-blue: #2F6FC7;
    --accent-blue-hover: #1D58A7;
    --accent-gold: #C9A24B;
    --accent-gold-light: #DEB35C;
    --card-cream: #FAF9F6;
    --card-border: #E2E8F0;
    --text-dark: #14213D;
    --text-muted: #64748b;
    --bg-page: #FAF9F7;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: 'Cairo', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-page);
    color: var(--text-dark);
    direction: rtl;
    text-align: right;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }

  a {
    text-decoration: none;
    color: inherit;
    cursor: pointer;
  }

  .site-wrapper {
    max-width: 1312px;
    margin: 0 auto;
    background: #ffffff;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.05);
    position: relative;
    overflow-x: hidden;
  }

  /* 1. HEADER (65px) */
  header.site-header {
    height: 65px;
    background: #ffffff;
    border-bottom: 1px solid #edf2f7;
    display: flex;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 100;
  }
  .header-container {
    width: 100%;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .header-right-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
  }
  .header-logo-image {
    height: 52px;
    width: auto;
    object-fit: contain;
  }
  .header-center-nav {
    display: flex;
    align-items: center;
    gap: 30px;
  }
  .nav-item {
    font-size: 15px;
    font-weight: 600;
    color: #334155;
    position: relative;
    padding: 6px 0;
    transition: color 0.2s;
  }
  .nav-item:hover {
    color: var(--accent-blue);
  }
  .nav-item.active {
    color: #0B2A5B;
    font-weight: 700;
  }
  .nav-item.active::after {
    content: '';
    position: absolute;
    bottom: -6px;
    right: 0;
    left: 0;
    height: 3px;
    background-color: var(--accent-blue);
    border-radius: 2px;
  }
  .nav-arrow {
    font-size: 11px;
    margin-right: 3px;
    display: inline-block;
  }
  .header-left-actions {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .btn-outline-wa {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 18px;
    border: 1.5px solid #cbd5e1;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 700;
    color: #1e293b;
    background: #ffffff;
    transition: all 0.2s;
  }
  .btn-outline-wa:hover {
    border-color: #25D366;
    color: #128C7E;
    background: #f0fdf4;
  }
  .btn-solid-call {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 8px 20px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 700;
    color: #ffffff;
    background: #0B2A5B;
    transition: background 0.2s;
  }
  .btn-solid-call:hover {
    background: #143e7d;
  }

  /* 2. HERO SECTION */
  section.hero-section {
    height: 275px;
    background: linear-gradient(135deg, #092147 0%, #0B2A5B 45%, #0e3470 100%);
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
  }
  .hero-art-left {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 440px;
"""

part2 = f"""    background-image: url('{hero_left_b64}');\n"""

part3 = """    background-size: cover;
    background-position: left center;
    background-repeat: no-repeat;
    z-index: 1;
    mask-image: linear-gradient(to right, rgba(0,0,0,1) 60%, rgba(0,0,0,0) 100%);
    -webkit-mask-image: linear-gradient(to right, rgba(0,0,0,1) 60%, rgba(0,0,0,0) 100%);
    pointer-events: none;
  }
  .hero-art-right {
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
    width: 275px;
"""

part4 = f"""    background-image: url('{lighthouse_b64}');\n"""

part5 = """    background-size: contain;
    background-position: right center;
    background-repeat: no-repeat;
    z-index: 1;
    pointer-events: none;
  }
  .hero-center-content {
    position: relative;
    z-index: 2;
    margin-right: 285px;
    max-width: 550px;
    text-align: right;
  }
  .hero-brand-title {
    font-family: 'Reem Kufi', sans-serif;
    font-size: 44px;
    font-weight: 700;
    color: var(--accent-gold-light);
    line-height: 1;
    margin-bottom: 3px;
    letter-spacing: -0.5px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
  }
  .hero-slogan-title {
    font-size: 23px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 7px;
    letter-spacing: -0.2px;
  }
  .hero-paragraph {
    font-size: 13px;
    color: #e2e8f0;
    line-height: 1.6;
    margin-bottom: 14px;
    font-weight: 500;
  }
  .hero-search-form {
    background: #ffffff;
    border-radius: 30px;
    padding: 3px 5px 3px 18px;
    display: flex;
    align-items: center;
    width: 530px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.25);
  }
  .hero-search-field {
    flex: 1;
    border: none;
    outline: none;
    font-family: 'Cairo', sans-serif;
    font-size: 13.5px;
    color: #1e293b;
    padding: 7px 10px;
  }
  .hero-search-field::placeholder {
    color: #94a3b8;
  }
  .hero-search-button {
    background: #0B2A5B;
    color: #ffffff;
    border: none;
    border-radius: 22px;
    padding: 7px 20px;
    font-family: 'Cairo', sans-serif;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: background 0.2s;
  }
  .hero-search-button:hover {
    background: #143e7d;
  }
  .hero-chips-row {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 11px;
  }
  .chips-label {
    font-size: 12px;
    color: #cbd5e1;
    font-weight: 600;
  }
  .chip-button {
    background: rgba(255, 255, 255, 0.14);
    backdrop-filter: blur(6px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    color: #ffffff;
    font-size: 12px;
    font-weight: 600;
    padding: 3px 12px;
    border-radius: 16px;
    cursor: pointer;
    transition: all 0.2s;
  }
  .chip-button:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-1px);
  }

  /* 3. TOOLS GRID (9 Vector Clean Cards) */
  section.tools-grid-section {
    background: #FAF9F7;
    padding: 24px 16px;
    border-bottom: 1px solid #edf2f7;
  }
  .tools-row-container {
    width: 100%;
    max-width: 1260px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(9, 1fr);
    gap: 10px;
  }
  .tool-card {
    background: #ffffff;
    border: 1px solid #e7ecf2;
    border-radius: 12px;
    padding: 16px 8px 14px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    cursor: pointer;
    transition: all 0.25s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
  }
  .tool-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(11, 42, 91, 0.1);
    border-color: #2F6FC7;
  }
  .tool-icon-wrap {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0B2A5B;
    margin-bottom: 10px;
    transition: transform 0.2s;
  }
  .tool-card:hover .tool-icon-wrap {
    transform: scale(1.1);
    color: #2F6FC7;
  }
  .tool-icon-wrap svg {
    width: 26px;
    height: 26px;
    fill: currentColor;
  }
  .tool-title {
    font-size: 13.5px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 5px;
    line-height: 1.3;
  }
  .tool-desc {
    font-size: 10.5px;
    color: #64748b;
    line-height: 1.45;
    font-weight: 500;
  }

  /* 4. MIDDLE SECTION (RTL: Why Us 415px on right, Integrated 805px on left) */
  section.middle-features-section {
    background: #FAF9F7;
    padding: 20px 16px;
  }
  .middle-row-container {
    width: 100%;
    max-width: 1240px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 415px 805px;
    gap: 20px;
  }

  /* Right Card: Why Us */
  .card-why-us {
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
  }
  .why-us-heading {
    font-size: 20px;
    font-weight: 800;
    color: #0B2A5B;
    text-align: center;
    margin-bottom: 14px;
  }
  .why-us-items {
    display: flex;
    flex-direction: column;
    gap: 11px;
  }
  .why-us-row {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .why-us-badge {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #FAF5E9;
    border: 1px solid #E6D4AA;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #B88E39;
    flex-shrink: 0;
  }
  .why-us-texts h4 {
    font-size: 13px;
    font-weight: 800;
    color: #0B2A5B;
    line-height: 1.2;
  }
  .why-us-texts p {
    font-size: 11px;
    color: #64748b;
    margin-top: 1px;
  }

  /* Left Card: Integrated Tools */
  .card-integrated {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    overflow: hidden;
    display: flex;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
    min-height: 240px;
  }
  .integrated-content {
    flex: 1.15;
    padding: 22px 24px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  .integrated-title {
    font-size: 20px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 6px;
  }
  .integrated-description {
    font-size: 12.5px;
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 12px;
  }
  .integrated-checklist {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 16px;
  }
  .integrated-checklist li {
    font-size: 12.5px;
    font-weight: 700;
    color: #1e293b;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .check-badge {
    width: 17px;
    height: 17px;
    background: #0B2A5B;
    color: #fff;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 9.5px;
    flex-shrink: 0;
  }
  .btn-integrated-explore {
    align-self: flex-start;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: #0B2A5B;
    color: #ffffff;
    font-size: 12.5px;
    font-weight: 700;
    padding: 8px 18px;
    border-radius: 8px;
    transition: background 0.2s;
  }
  .btn-integrated-explore:hover {
    background: #143e7d;
  }
  .integrated-banner-side {
    flex: 0.95;
    background-color: #f1ede8;
"""

part6 = f"""    background-image: url('{laptop_art_b64}');\n"""

part7 = """    background-size: cover;
    background-position: center;
    min-height: 240px;
  }

  /* 5. BOTTOM SECTION (RTL: Services 315px on right, Packages 425px center, How 460px left) */
  section.bottom-three-section {
    background: #FAF9F7;
    padding: 10px 16px 28px;
  }
  .bottom-grid-container {
    width: 100%;
    max-width: 1240px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 315px 425px 460px;
    gap: 20px;
    align-items: stretch;
  }

  /* Services Card */
  .card-services {
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 20px 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
  }
  .services-top-header {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #0B2A5B;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 5px;
  }
  .services-short-desc {
    font-size: 11.5px;
    color: #64748b;
    margin-bottom: 10px;
    line-height: 1.5;
  }
  .services-items-list {
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 12px;
    font-size: 12px;
    font-weight: 600;
    color: #1e293b;
  }
  .services-items-list li {
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .services-items-list li::before {
    content: '✓';
    color: #2F6FC7;
    font-weight: 800;
  }
  .services-contact-bubble {
    background: #edf2f7;
    border-right: 3px solid #0B2A5B;
    padding: 8px 10px;
    border-radius: 4px;
    margin-bottom: 12px;
    font-size: 11px;
    color: #334155;
    line-height: 1.5;
  }
  .services-contact-bubble a {
    color: #0B2A5B;
    font-weight: bold;
    direction: ltr;
    display: inline-block;
  }
  .services-actions-group {
    display: flex;
    gap: 8px;
  }
  .services-call-btn {
    flex: 1;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    background: #0B2A5B;
    color: #ffffff;
    font-size: 12.5px;
    font-weight: 700;
    padding: 8px 0;
    border-radius: 8px;
    transition: background 0.2s;
  }
  .services-call-btn:hover {
    background: #143e7d;
  }
  .services-wa-icon-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 14px;
    background: #25D366;
    color: #ffffff;
    border-radius: 8px;
    transition: background 0.2s;
  }
  .services-wa-icon-btn:hover {
    background: #1ebd5b;
  }

  /* Packages Card */
  .card-packages {
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 20px 16px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
    display: flex;
    flex-direction: column;
  }
  .packages-header-title {
    font-size: 19px;
    font-weight: 800;
    color: #0B2A5B;
    text-align: center;
    margin-bottom: 16px;
  }
  .packages-cards-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    flex: 1;
  }
  .tier-box {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px 8px 10px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    text-align: center;
    box-shadow: 0 2px 6px rgba(0,0,0,0.02);
  }
  .tier-box.popular {
    border: 2px solid #2F6FC7;
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(47, 111, 199, 0.12);
  }
  .tier-popular-tag {
    position: absolute;
    top: -9px;
    left: 50%;
    transform: translateX(-50%);
    background: #2F6FC7;
    color: #fff;
    font-size: 9.5px;
    font-weight: 700;
    padding: 1px 8px;
    border-radius: 8px;
    white-space: nowrap;
  }
  .tier-title {
    font-size: 14.5px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 2px;
  }
  .tier-cost {
    font-size: 11px;
    color: #64748b;
    margin-bottom: 8px;
    padding-bottom: 6px;
    border-bottom: 1px solid #f1f5f9;
  }
  .tier-cost strong {
    font-size: 16px;
    color: #0B2A5B;
  }
  .tier-perks {
    list-style: none;
    text-align: right;
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin-bottom: 10px;
    font-size: 10px;
    color: #475569;
    flex: 1;
  }
  .tier-perks li {
    display: flex;
    align-items: flex-start;
    gap: 4px;
    line-height: 1.35;
  }
  .tier-perks li::before {
    content: '✓';
    color: #2F6FC7;
    font-weight: bold;
    font-size: 10.5px;
    flex-shrink: 0;
  }
  .tier-action-btn {
    display: block;
    width: 100%;
    padding: 6px 0;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 700;
    text-align: center;
    transition: all 0.2s;
    cursor: pointer;
  }
  .tier-btn-outline {
    border: 1.5px solid #0B2A5B;
    color: #0B2A5B;
    background: transparent;
  }
  .tier-btn-outline:hover {
    background: #0B2A5B;
    color: #fff;
  }
  .tier-btn-fill {
    background: #2F6FC7;
    color: #ffffff;
    border: none;
  }
  .tier-btn-fill:hover {
    background: #1D58A7;
  }

  /* How to Start Card */
  .card-how-to-start {
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 24px 20px 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
  }
  .how-title {
    font-size: 19px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 20px;
  }
  .how-steps-diagram {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 20px 0;
    padding: 0 4px;
  }
  .step-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 76px;
    position: relative;
    cursor: pointer;
    transition: transform 0.2s;
  }
  .step-item:hover {
    transform: scale(1.05);
  }
  .step-num {
    position: absolute;
    top: -5px;
    right: 18px;
    width: 16px;
    height: 16px;
    background: #0B2A5B;
    color: #fff;
    font-size: 9.5px;
    font-weight: 700;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #fff;
  }
  .step-round-circle {
    width: 46px;
    height: 46px;
    background: #ffffff;
    border: 1.5px solid #d8e2ed;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0B2A5B;
    margin-bottom: 10px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.03);
  }
  .step-round-circle svg {
    width: 22px;
    height: 22px;
    fill: currentColor;
  }
  .step-label {
    font-size: 11px;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.35;
  }
  .step-divider-arrow {
    color: #94a3b8;
    font-size: 14px;
    margin-top: -24px;
  }
  .how-quote {
    font-family: 'Aref Ruqaa', serif;
    font-size: 18px;
    color: #0B2A5B;
    text-align: center;
    margin-top: 14px;
  }

  /* 6. ARTICLES SECTION */
  .inner-section-view {
    padding: 40px 20px;
    max-width: 1240px;
    margin: 0 auto;
  }
  .inner-section-header {
    text-align: center;
    margin-bottom: 30px;
  }
  .inner-section-header h2 {
    font-size: 26px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 8px;
  }
  .inner-section-header p {
    font-size: 14px;
    color: #64748b;
  }
  .articles-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }
  .article-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    transition: transform 0.2s;
    cursor: pointer;
  }
  .article-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(11, 42, 91, 0.08);
  }
  .article-card-cover {
    height: 150px;
    background: linear-gradient(135deg, #0B2A5B, #2F6FC7);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    padding: 20px;
    text-align: center;
    font-weight: bold;
    font-size: 16px;
  }
  .article-card-body {
    padding: 18px;
  }
  .article-tag {
    display: inline-block;
    background: #FAF5E9;
    color: #B88E39;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
    margin-bottom: 8px;
  }
  .article-title {
    font-size: 15.5px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 6px;
    line-height: 1.4;
  }
  .article-snippet {
    font-size: 12px;
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 12px;
  }
  .article-link-more {
    color: #2F6FC7;
    font-size: 12.5px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }

  /* 7. HELP SECTION */
  .help-accordion {
    max-width: 800px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .help-item {
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 10px;
    overflow: hidden;
  }
  .help-q {
    padding: 16px 20px;
    font-size: 15px;
    font-weight: 700;
    color: #0B2A5B;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .help-a {
    padding: 0 20px 16px;
    font-size: 13.5px;
    color: #475569;
    line-height: 1.6;
  }

  /* BLOGGER POST VIEW / INNER PAGE STYLES */
  .blog-inner-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px;
  }
  .post-article {
    background: #ffffff;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    padding: 36px 32px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.03);
  }
  .post-header {
    border-bottom: 1px solid #edf2f7;
    padding-bottom: 20px;
    margin-bottom: 24px;
  }
  .post-title {
    font-size: 28px;
    font-weight: 900;
    color: #0B2A5B;
    line-height: 1.4;
    margin-bottom: 12px;
  }
  .post-meta {
    font-size: 13px;
    color: #64748b;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .post-body {
    font-size: 16px;
    line-height: 1.85;
    color: #1e293b;
  }
  .post-body p {
    margin-bottom: 18px;
  }
  .post-body h2, .post-body h3 {
    color: #0B2A5B;
    margin: 26px 0 14px;
  }
  .post-body img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    margin: 16px 0;
  }
  .post-contact-card {
    margin-top: 36px;
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-right: 4px solid #0B2A5B;
    padding: 24px;
    border-radius: 12px;
    text-align: right;
  }
  .post-contact-card h4 {
    color: #0B2A5B;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 8px;
  }
  .post-contact-card p {
    color: #475569;
    font-size: 13.5px;
    line-height: 1.6;
    margin-bottom: 16px;
  }

  /* 8. FOOTER */
  footer.site-footer {
    background: #0B2A5B;
    color: #ffffff;
    padding: 20px 0;
  }
  .footer-container {
    width: 100%;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .footer-right-brand {
    display: flex;
    align-items: center;
  }
  .footer-logo-image {
    height: 44px;
    width: auto;
    object-fit: contain;
  }
  .footer-center-nav {
    display: flex;
    align-items: center;
    gap: 22px;
  }
  .footer-link {
    color: #cbd5e1;
    font-size: 13.5px;
    font-weight: 600;
    transition: color 0.2s;
  }
  .footer-link:hover {
    color: #ffffff;
  }
  .footer-left-social {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
  }
  .social-icons-row {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .social-link {
    color: #94a3b8;
    transition: color 0.2s;
    display: inline-flex;
  }
  .social-link:hover {
    color: #ffffff;
  }
  .social-link svg {
    width: 18px;
    height: 18px;
    fill: currentColor;
  }
  .copyright-text {
    font-size: 11.5px;
    color: #94a3b8;
  }

  /* MODALS & POPUPS */
  .modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(11, 42, 91, 0.6);
    backdrop-filter: blur(4px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    padding: 20px;
  }
  .modal-overlay.active {
    display: flex;
  }
  .modal-box {
    background: #ffffff;
    border-radius: 16px;
    max-width: 580px;
    width: 100%;
    padding: 28px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.25);
    position: relative;
    text-align: right;
    animation: modalPop 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }
  @keyframes modalPop {
    0% { transform: scale(0.92); opacity: 0; }
    100% { transform: scale(1); opacity: 1; }
  }
  .modal-close-btn {
    position: absolute;
    left: 20px;
    top: 20px;
    background: #f1f5f9;
    border: none;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: bold;
    color: #64748b;
    cursor: pointer;
  }
  .modal-close-btn:hover {
    background: #e2e8f0;
    color: #0f172a;
  }
  .modal-header-icon {
    width: 48px;
    height: 48px;
    background: #FAF5E9;
    color: #B88E39;
    border: 1px solid #E6D4AA;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 14px;
  }
  .modal-header-icon svg {
    width: 26px;
    height: 26px;
    fill: currentColor;
  }
  .modal-title {
    font-size: 22px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 8px;
  }
  .modal-desc {
    font-size: 14px;
    color: #475569;
    line-height: 1.6;
    margin-bottom: 20px;
  }
  .modal-content-area {
    background: #f8fafc;
    border: 1px dashed #cbd5e1;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    text-align: center;
  }
  .modal-action-row {
    display: flex;
    gap: 10px;
  }

  /* Responsive Rules */
  @media (max-width: 1024px) {
    .hero-center-content {
      margin-right: 20px;
      max-width: calc(100% - 40px);
    }
    .hero-art-right {
      display: none;
    }
    .tools-row-container {
      grid-template-columns: repeat(5, 1fr);
    }
    .middle-row-container {
      grid-template-columns: 1fr;
    }
    .bottom-grid-container {
      grid-template-columns: 1fr;
    }
    .articles-grid {
      grid-template-columns: 1fr;
    }
  }

  @media (max-width: 768px) {
    .header-center-nav {
      display: none;
    }
    .hero-search-form {
      width: 100%;
    }
    .tools-row-container {
      grid-template-columns: repeat(3, 1fr);
    }
    .card-integrated {
      flex-direction: column-reverse;
    }
    .packages-cards-grid {
      grid-template-columns: 1fr;
    }
    .footer-container {
      flex-direction: column;
      gap: 16px;
      text-align: center;
    }
    .footer-left-social {
      align-items: center;
    }
  }
  ]]></b:skin>
</head>
<body>

<div class='site-wrapper'>

  <!-- 1. HEADER (65px) -->
  <header class='site-header'>
    <div class='header-container'>
      
      <!-- Right: Logo with clear sub-text -->
      <a class='header-right-logo' href='/'>
"""

part8 = f"""        <img alt='مرصاد - منصة الذكاء الاصطناعي للبحث العلمي العربي' class='header-logo-image' src='{header_logo_b64}'/>\n"""

part9 = """      </a>

      <!-- Center: Navigation -->
      <nav class='header-center-nav'>
        <a class='nav-item active' href='/'>الرئيسية</a>
        <a class='nav-item' href='#tools'>الأدوات <span class='nav-arrow'>▾</span></a>
        <a class='nav-item' href='#services'>خدمات الأبحاث</a>
        <a class='nav-item' href='#articles-section'>المقالات</a>
        <a class='nav-item' href='#help-section'>مساعدة</a>
      </nav>

      <!-- Left: WhatsApp & Call CTA -->
      <div class='header-left-actions'>
        <a class='btn-outline-wa' href='https://wa.me/201015034659' target='_blank'>
          <svg fill='currentColor' style='width:16px; height:16px;' viewBox='0 0 24 24'><path d='M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z'/></svg>
          <span>واتساب</span>
        </a>
        <a class='btn-solid-call' href='tel:01015034659'>
          <svg fill='currentColor' style='width:16px; height:16px;' viewBox='0 0 24 24'><path d='M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-2.2 2.2a15.045 15.045 0 01-6.59-6.59l2.2-2.21a.96.96 0 00.25-1.01A11.36 11.36 0 018.57 3.9c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.52c0-.55-.45-1-.99-1z'/></svg>
          <span>اتصل الآن</span>
        </a>
      </div>

    </div>
  </header>

  <!-- HOMEPAGE CONTENT -->
  <b:if cond='data:blog.pageType == &quot;index&quot;'>

    <!-- 2. HERO SECTION -->
    <section class='hero-section'>
      <div class='hero-art-left'></div>
      <div class='hero-art-right'></div>
      <div class='hero-center-content'>
        <h1 class='hero-brand-title'>مِرْصَاد</h1>
        <h2 class='hero-slogan-title'>نرصد المعرفة، ونبني البحث.</h2>
        <p class='hero-paragraph'>
          منصة ذكاء اصطناعي للباحثين والمعلمين وطلاب الدراسات العليا،<br/>
          تساعدك على إنجاز بحثك بدقة واحترافية، من الفكرة إلى الملف النهائي.
        </p>
        <form class='hero-search-form' onsubmit='handleSearch(event)'>
          <input class='hero-search-field' id='searchInput' placeholder='اكتب موضوع بحثك أو ارفع ملفك...' type='text'/>
          <button class='hero-search-button' type='submit'>
            <span>ابدأ الآن</span>
            <span>✦</span>
          </button>
        </form>
        <div class='hero-chips-row'>
          <span class='chips-label'>أمثلة مقترحة:</span>
          <button class='chip-button' onclick='searchFor(&quot;الدراسات السابقة&quot;)' type='button'>الدراسات السابقة</button>
          <button class='chip-button' onclick='searchFor(&quot;تحليل الاستبيان&quot;)' type='button'>تحليل الاستبيان</button>
          <button class='chip-button' onclick='searchFor(&quot;توثيق المراجع&quot;)' type='button'>توثيق المراجع</button>
          <button class='chip-button' onclick='searchFor(&quot;صياغة أكاديمية&quot;)' type='button'>صياغة أكاديمية</button>
        </div>
      </div>
    </section>

    <!-- 3. TOOLS GRID (9 Vector Clean Cards) -->
    <section class='tools-grid-section' id='tools'>
      <div class='tools-row-container'>
"""

part10 = """      </div>
    </section>

    <!-- 4. MIDDLE SECTION -->
    <section class='middle-features-section'>
      <div class='middle-row-container'>
        
        <!-- Right Card: Why Us (First in RTL Grid) -->
        <div class='card-why-us'>
          <h3 class='why-us-heading'>لماذا مِرْصَاد؟</h3>
          <div class='why-us-items'>
            
            <div class='why-us-row'>
              <div class='why-us-badge'>
                <svg style='width:20px;height:20px;fill:currentColor;' viewBox='0 0 24 24'><path d='M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z'/></svg>
              </div>
              <div class='why-us-texts'>
                <h4>يوفر وقتك وجهدك</h4>
                <p>بدلاً من البحث اليدوي الطويل</p>
              </div>
            </div>

            <div class='why-us-row'>
              <div class='why-us-badge'>
                <svg style='width:20px;height:20px;fill:currentColor;' viewBox='0 0 24 24'><path d='M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z'/></svg>
              </div>
              <div class='why-us-texts'>
                <h4>دقة وموثوقية</h4>
                <p>بمصادر حقيقية وقابلة للتحقق</p>
              </div>
            </div>

            <div class='why-us-row'>
              <div class='why-us-badge'>
                <svg style='width:20px;height:20px;fill:currentColor;' viewBox='0 0 24 24'><path d='M12.87 15.07l-2.54-2.51.03-.03c1.74-1.94 2.98-4.17 3.71-6.53H17V4h-7V2H8v2H1v1.99h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12zm-2.62 7l1.62-4.33L19.12 17h-3.24z'/></svg>
              </div>
              <div class='why-us-texts'>
                <h4>دعم كامل باللغة العربية</h4>
                <p>بأسلوب أكاديمي واضح وسليم</p>
              </div>
            </div>

            <div class='why-us-row'>
              <div class='why-us-badge'>
                <svg style='width:20px;height:20px;fill:currentColor;' viewBox='0 0 24 24'><path d='M4 8h4V4H4v4zm6 12h4v-4h-4v4zm-6 0h4v-4H4v4zm0-6h4v-4H4v4zm6 0h4v-4h-4v4zm6-10v4h4V4h-4zm-6 4h4V4h-4v4zm6 6h4v-4h-4v4zm0 6h4v-4h-4v4z'/></svg>
              </div>
              <div class='why-us-texts'>
                <h4>مناسب لجميع التخصصات</h4>
                <p>من العلوم الإنسانية إلى العلوم التطبيقية</p>
              </div>
            </div>

          </div>
        </div>

        <!-- Left Card: Integrated Tools (Second in RTL Grid) -->
        <div class='card-integrated'>
          <div class='integrated-content'>
            <h3 class='integrated-title'>أدوات متكاملة لرحلتك البحثية</h3>
            <p class='integrated-description'>
              لا نفهمك للكتابة فقط، بل نساعدك في التحليل، والمراجعة، والتوثيق،<br/>
              حتى تصل إلى بحث متكامل وجاهز للنشر أو المناقشة.
            </p>
            <ul class='integrated-checklist'>
              <li><span class='check-badge'>✓</span> مصادر موثوقة ومحدثة</li>
              <li><span class='check-badge'>✓</span> نتائج دقيقة وقابلة للتحقق</li>
              <li><span class='check-badge'>✓</span> دعم اللغة العربية الأكاديمية</li>
              <li><span class='check-badge'>✓</span> تصدير احترافي إلى Word</li>
            </ul>
            <a class='btn-integrated-explore' href='#tools'>
              <span>استكشف جميع الأدوات</span>
              <span>←</span>
            </a>
          </div>
          <div class='integrated-banner-side'></div>
        </div>

      </div>
    </section>

    <!-- 5. BOTTOM SECTION -->
    <section class='bottom-three-section'>
      <div class='bottom-grid-container'>
        
        <!-- Right Card: Services (First in RTL Grid) -->
        <div class='card-services' id='services'>
          <div>
            <div class='services-top-header'>
              <svg style='width:20px;height:20px;fill:currentColor;' viewBox='0 0 24 24'><path d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z'/></svg>
              <span>خدمات الباحث</span>
            </div>
            <p class='services-short-desc'>يمكنك طلب خدمات احترافية من فريق أبحاثنا المتخصص:</p>
            <ul class='services-items-list'>
              <li>تنسيق رسالة ماجستير</li>
              <li>تدقيق لغوي</li>
              <li>تحليل إحصائي</li>
              <li>تفريغ مقابلات</li>
              <li>تنسيق مراجع</li>
            </ul>
            <div class='services-contact-bubble'>
              للاتفاق على أي عمل فيما يخص الأبحاث العلمية يرجى الاتصال على: <a href='tel:01015034659'>01015034659</a>
            </div>
          </div>
          <div class='services-actions-group'>
            <a class='services-call-btn' href='tel:01015034659'>
              <span>اطلب خدمة الآن</span>
              <span>←</span>
            </a>
            <a class='services-wa-icon-btn' href='https://wa.me/201015034659' target='_blank' title='تواصل عبر واتساب'>
              <svg style='width:16px;height:16px;fill:currentColor;' viewBox='0 0 24 24'><path d='M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z'/></svg>
            </a>
          </div>
        </div>

        <!-- Center Card: Packages (Second in RTL Grid) -->
        <div class='card-packages'>
          <h3 class='packages-header-title'>باقات الاشتراك</h3>
          <div class='packages-cards-grid'>
            
            <!-- Free -->
            <div class='tier-box'>
              <div>
                <h4 class='tier-title'>مجاني</h4>
                <div class='tier-cost'><strong>0</strong> جنيه / شهر</div>
                <ul class='tier-perks'>
                  <li>3 عمليات يوميًا</li>
                  <li>تلخيص 3 مصادر</li>
                  <li>أدوات صياغة محدودة</li>
                </ul>
              </div>
              <button class='tier-action-btn tier-btn-outline' onclick='openTierModal(&quot;مجاني&quot;, &quot;0 جنيه&quot;)' type='button'>ابدأ الآن</button>
            </div>

            <!-- Researcher -->
            <div class='tier-box popular'>
              <span class='tier-popular-tag'>الأكثر اختياراً</span>
              <div>
                <h4 class='tier-title'>باحث</h4>
                <div class='tier-cost'><strong>99</strong> جنيه / شهر</div>
                <ul class='tier-perks'>
                  <li>استخدام أكبر للأدوات</li>
                  <li>رفع الملفات وتحليلها</li>
                  <li>إنشاء الحواشي والمراجع</li>
                  <li>تصدير Word</li>
                </ul>
              </div>
              <button class='tier-action-btn tier-btn-fill' onclick='openTierModal(&quot;باحث&quot;, &quot;99 جنيه&quot;)' type='button'>اشترك الآن</button>
            </div>

            <!-- Plus -->
            <div class='tier-box'>
              <div>
                <h4 class='tier-title'>باحث+</h4>
                <div class='tier-cost'><strong>249</strong> جنيه / شهر</div>
                <ul class='tier-perks'>
                  <li>استخدام غير محدود</li>
                  <li>تحليل ملفات كبيرة</li>
                  <li>تحليل الدراسات السابقة</li>
                  <li>تحليل الاستبيانات</li>
                  <li>أدوات متقدمة</li>
                  <li>أولوية في المعالجة</li>
                </ul>
              </div>
              <button class='tier-action-btn tier-btn-fill' onclick='openTierModal(&quot;باحث+&quot;, &quot;249 جنيه&quot;)' type='button'>اشترك الآن</button>
            </div>

          </div>
        </div>

        <!-- Left Card: How to Start (Third in RTL Grid) -->
        <div class='card-how-to-start'>
          <div>
            <h3 class='how-title'>كيف تبدأ؟</h3>
            <div class='how-steps-diagram'>
              
              <div class='step-item' onclick='openStepModal(&quot;أنشئ حسابك مجاناً&quot;, &quot;يمكنك التسجيل في دقائق والبدء في استكشاف كافة الأدوات البحثية المتطورة.&quot;)'>
                <span class='step-num'>4</span>
                <div class='step-round-circle'>
                  <svg viewBox='0 0 24 24'><path d='M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z'/></svg>
                </div>
                <div class='step-label'>أنشئ حسابك<br/>مجانًا</div>
              </div>

              <div class='step-divider-arrow'>←</div>

              <div class='step-item' onclick='openStepModal(&quot;أدخل موضوع بحثك أو ارفع ملفك&quot;, &quot;قم بكتابة عنوان بحثك أو ارفع ملف الرسالة بصيغة Word أو PDF لاستخلاص البيانات وتحليلها.&quot;)'>
                <span class='step-num'>2</span>
                <div class='step-round-circle'>
                  <svg viewBox='0 0 24 24'><path d='M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z'/></svg>
                </div>
                <div class='step-label'>أدخل موضوع بحثك<br/>أو ارفع ملفك</div>
              </div>

              <div class='step-divider-arrow'>←</div>

              <div class='step-item' onclick='openStepModal(&quot;اختر الأداة المناسبة وابدأ التحليل&quot;, &quot;اختر من بين 9 أدوات بحثية متخصصة (المصادر، الدراسات السابقة، الاستبيانات، التوثيق، الصياغة).&quot;)'>
                <span class='step-num'>3</span>
                <div class='step-round-circle'>
                  <svg viewBox='0 0 24 24'><path d='M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z'/></svg>
                </div>
                <div class='step-label'>اختر الأداة المناسبة<br/>وابدأ التحليل</div>
              </div>

              <div class='step-divider-arrow'>←</div>

              <div class='step-item' onclick='openStepModal(&quot;استلم النتائج وقم بتصديرها&quot;, &quot;حمّل النتائج كملف Word منسق بالكامل وجاهز للطباعة أو الإضافة إلى رسالتك مباشرة.&quot;)'>
                <span class='step-num'>1</span>
                <div class='step-round-circle'>
                  <svg viewBox='0 0 24 24'><path d='M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z'/></svg>
                </div>
                <div class='step-label'>استلم النتائج<br/>وقم بتصديرها</div>
              </div>

            </div>
          </div>
          <div class='how-quote'>
            خطوات بسيطة ... ونتيجة احترافية
          </div>
        </div>

      </div>
    </section>

    <!-- 6. ARTICLES SECTION (LIVE & CLICKABLE) -->
    <section class='inner-section-view' id='articles-section'>
      <div class='inner-section-header'>
        <h2>أحدث المقالات والأدلة البحثية</h2>
        <p>مقالات أكاديمية متخصصة ومحدثة خطوة بخطوة لمساعدتك في إنجاز أطروحتك وبحثك العلمي</p>
      </div>
      <div class='articles-grid'>
        
        <div class='article-card' onclick='openArticleModal(&quot;دليل كتابة الإطار النظري والدراسات السابقة 2026&quot;, &quot;أحدث منهجية علمية لتحديد الفجوة البحثية وصياغة مراجعة الأدبيات بطريقة محكمة قابلة للنشر في المجلات الدولية.&quot;)'>
          <div class='article-card-cover'>
            دليل كتابة الإطار النظري
          </div>
          <div class='article-card-body'>
            <span class='article-tag'>الدراسات السابقة</span>
            <h3 class='article-title'>دليل كتابة الإطار النظري والدراسات السابقة 2026</h3>
            <p class='article-snippet'>أحدث منهجية علمية لتحديد الفجوة البحثية وصياغة مراجعة الأدبيات بطريقة محكمة...</p>
            <span class='article-link-more'>اقرأ المقال كاملاً ←</span>
          </div>
        </div>

        <div class='article-card' onclick='openArticleModal(&quot;التحليل الإحصائي للاستبيانات باستخدام SPSS و AMOS&quot;, &quot;شرح عملي لاختبارات الصدق والثبات، ومعامل ألفا كرونباخ، والتحليل العاملي التوكيدي لرسائل الماجستير.&quot;)'>
          <div class='article-card-cover' style='background: linear-gradient(135deg, #1d58a7, #0B2A5B);'>
            التحليل الإحصائي للاستبيان
          </div>
          <div class='article-card-body'>
            <span class='article-tag'>تحليل الاستبيان</span>
            <h3 class='article-title'>التحليل الإحصائي للاستبيانات باستخدام SPSS و AMOS</h3>
            <p class='article-snippet'>شرح عملي لاختبارات الصدق والثبات، ومعامل ألفا كرونباخ، والتحليل العاملي التوكيدي...</p>
            <span class='article-link-more'>اقرأ المقال كاملاً ←</span>
          </div>
        </div>

        <div class='article-card' onclick='openArticleModal(&quot;قواعد التوثيق الأكاديمي وفق الإصدار السابع APA 7th&quot;, &quot;كيف توثق المقالات والكتب والرسائل والذكاء الاصطناعي في المتن وقائمة المراجع بلا أخطاء شائعة.&quot;)'>
          <div class='article-card-cover' style='background: linear-gradient(135deg, #deb35c, #0B2A5B);'>
            التوثيق الأكاديمي APA 7th
          </div>
          <div class='article-card-body'>
            <span class='article-tag'>توثيق المراجع</span>
            <h3 class='article-title'>قواعد التوثيق الأكاديمي وفق الإصدار السابع APA 7th</h3>
            <p class='article-snippet'>كيف توثق المقالات والكتب والرسائل والذكاء الاصطناعي في المتن وقائمة المراجع بلا أخطاء...</p>
            <span class='article-link-more'>اقرأ المقال كاملاً ←</span>
          </div>
        </div>

      </div>
    </section>

    <!-- 7. HELP SECTION (ACCORDION & FAQ) -->
    <section class='inner-section-view' id='help-section' style='background: #ffffff; border-top: 1px solid #edf2f7;'>
      <div class='inner-section-header'>
        <h2>مركز المساعدة والأسئلة الشائعة</h2>
        <p>إليك أهم الأسئلة التي يطرحها الباحثون حول كيفية الاستفادة القصوى من منصة مرصاد</p>
      </div>
      <div class='help-accordion'>
        
        <div class='help-item'>
          <div class='help-q' onclick='toggleHelp(this)'>
            <span>ما هي الخدمات التي تقدمها منصة مرصاد للباحثين؟</span>
            <span>▾</span>
          </div>
          <div class='help-a'>
            منصة مرصاد تقدم 9 أدوات ذكية متكاملة تغطي كافة مراحل البحث العلمي: البحث في قواعد البيانات العالمية، تحليل ومقارنة الدراسات السابقة، بناء خطة البحث والمشكلة والأهداف، توثيق المراجع بأسلوب APA و MLA وغيرها، تحليل الاستبيانات إحصائياً، الصياغة الأكاديمية السليمة، والمراجعة اللغوية والمنهجية مع التصدير النهائي إلى Word.
          </div>
        </div>

        <div class='help-item'>
          <div class='help-q' onclick='toggleHelp(this)'>
            <span>كيف يمكنني طلب خدمة مخصصة (تنسيق رسالة أو تحليل إحصائي)؟</span>
            <span>▾</span>
          </div>
          <div class='help-a'>
            يمكنك التواصل المباشر مع فريقنا المتخصص عبر الاتصال على الرقم <strong>01015034659</strong> أو مراسلتنا فوراً عبر الواتساب على نفس الرقم، وسيتم الاتفاق على نطاق العمل والتسليم بأعلى معايير الجودة والأمانة العلمية.
          </div>
        </div>

        <div class='help-item'>
          <div class='help-q' onclick='toggleHelp(this)'>
            <span>هل تضمن المنصة الحفاظ على سرية الأبحاث والبيانات؟</span>
            <span>▾</span>
          </div>
          <div class='help-a'>
            نعم، نحن نلتزم بالسرية التامة لجميع الملفات والبيانات التي ترفعها على المنصة، ولا يتم مشاركة أي ملف مع أي طرف خارجي، وتبقى حقوق الملكية الفكرية ملكاً خالصاً لك كباحث.
          </div>
        </div>

      </div>
    </section>

  </b:if>

  <!-- MAIN BLOG SECTION (POSTS / PAGES / ARCHIVES) -->
  <main class='blog-inner-container'>
    <b:section class='main' id='main' showaddelement='yes'>
      <b:widget id='Blog1' locked='true' title='رسائل المدونة الإلكترونية' type='Blog'>
        <b:includable id='main' var='top'>
          <b:loop values='data:posts' var='post'>
            <b:if cond='data:blog.pageType != &quot;index&quot;'>
              <article class='post-article'>
                <header class='post-header'>
                  <h1 class='post-title'><data:post.title/></h1>
                  <div class='post-meta'>
                    <span>بواسطة: <data:post.author/></span>
                    <span>•</span>
                    <span><data:post.dateHeader/></span>
                  </div>
                </header>

                <div class='post-body'>
                  <data:post.body/>
                </div>

                <div class='post-contact-card'>
                  <h4>تحتاج إلى مساعدة متخصصة في بحثك العلمي؟</h4>
                  <p>فريق مرصاد مستعد لمساعدتك في التدقيق، التنسيق، والتحليل الإحصائي بأعلى دقة أكاديمية.</p>
                  <a class='btn-solid-call' href='tel:01015034659' style='display:inline-flex;'>
                    <span>اتصل بنا الآن: 01015034659</span>
                  </a>
                </div>
              </article>
            </b:if>
          </b:loop>
        </b:includable>
      </b:widget>
    </b:section>
  </main>

  <!-- 8. FOOTER -->
  <footer class='site-footer'>
    <div class='footer-container'>
      
      <!-- Right: Logo -->
      <div class='footer-right-brand'>
        <a href='/'>
"""

part11 = f"""          <img alt='مرصاد' class='footer-logo-image' src='{footer_logo_b64}'/>\n"""

part12 = """        </a>
      </div>

      <!-- Center: Links -->
      <nav class='footer-center-nav'>
        <a class='footer-link' href='/'>الرئيسية</a>
        <a class='footer-link' href='#tools'>الأدوات</a>
        <a class='footer-link' href='#services'>خدمات الأبحاث</a>
        <a class='footer-link' href='#articles-section'>المقالات</a>
        <a class='footer-link' href='#help-section'>مساعدة</a>
      </nav>

      <!-- Left: Social & Rights -->
      <div class='footer-left-social'>
        <div class='social-icons-row'>
          <a class='social-link' href='#' title='YouTube'><svg viewBox='0 0 24 24'><path d='M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z'/></svg></a>
          <a class='social-link' href='#' title='X'><svg viewBox='0 0 24 24'><path d='M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z'/></svg></a>
          <a class='social-link' href='#' title='Facebook'><svg viewBox='0 0 24 24'><path d='M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z'/></svg></a>
          <a class='social-link' href='#' title='LinkedIn'><svg viewBox='0 0 24 24'><path d='M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z'/></svg></a>
        </div>
        <div class='copyright-text'>© مرصاد. جميع الحقوق محفوظة.</div>
      </div>

    </div>
  </footer>

</div>

<!-- INTERACTIVE MODAL POPUP -->
<div class='modal-overlay' id='mainModal' onclick='closeModalOnOverlay(event)'>
  <div class='modal-box'>
    <button class='modal-close-btn' onclick='closeModal()'>✕</button>
    <div class='modal-header-icon' id='modalIcon'>
      <svg viewBox='0 0 24 24'><path d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z'/></svg>
    </div>
    <h3 class='modal-title' id='modalTitle'>عنوان النافذة</h3>
    <p class='modal-desc' id='modalDesc'>تفاصيل المحتوى التفاعلي</p>
    <div class='modal-content-area' id='modalCustomContent'>
      <p style='font-size: 13.5px; color: #475569;'>جاري تجهيز بيئة التحليل الذكية لبحثك...</p>
    </div>
    <div class='modal-action-row'>
      <a class='btn-solid-call' href='https://wa.me/201015034659' style='flex:1; justify-content:center;' target='_blank'>
        <span>تواصل مع باحث متخصص</span>
        <span>←</span>
      </a>
      <button class='btn-outline-wa' onclick='closeModal()'>إغلاق</button>
    </div>
  </div>
</div>

<script type='text/javascript'>
//<![CDATA[
  function openToolModal(title, desc) {
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalDesc').innerText = desc;
    document.getElementById('modalCustomContent').innerHTML = `
      <div style="text-align: right;">
        <label style="font-size:12.5px; font-weight:700; color:#0B2A5B; display:block; margin-bottom:6px;">أدخل نص البحث أو ارفع ملفك للبدء في ` + title + `:</label>
        <textarea style="width:100%; height:80px; padding:8px; border:1px solid #cbd5e1; border-radius:8px; font-family:Cairo; font-size:13px; margin-bottom:10px;" placeholder="اكتب أو الصق نص السؤال أو عنوان الدراسة..."></textarea>
        <div style="display:flex; justify-content:space-between; align-items:center;">
          <input type="file" style="font-size:11.5px; color:#64748b;" />
          <button style="background:#0B2A5B; color:#fff; border:none; padding:6px 16px; border-radius:6px; font-family:Cairo; font-size:12.5px; cursor:pointer;" onclick="alert('تم استلام طلبك بنجاح! جاري معالجة البيانات...')">بدء التحليل</button>
        </div>
      </div>
    `;
    document.getElementById('mainModal').classList.add('active');
  }

  function openStepModal(stepTitle, stepDesc) {
    document.getElementById('modalTitle').innerText = stepTitle;
    document.getElementById('modalDesc').innerText = stepDesc;
    document.getElementById('modalCustomContent').innerHTML = `
      <p style="font-size:14px; color:#1e293b; line-height:1.7;">
        ` + stepDesc + `<br/>
        لأي استفسار بخصوص هذه الخطوة يمكنك الاتصال مباشرة على: <strong>01015034659</strong>
      </p>
    `;
    document.getElementById('mainModal').classList.add('active');
  }

  function openTierModal(tierName, tierPrice) {
    document.getElementById('modalTitle').innerText = 'الاشتراك في باقة ' + tierName;
    document.getElementById('modalDesc').innerText = 'تكلفة الباقة: ' + tierPrice + ' شهرياً. تمتع بكافة الصلاحيات الأكاديمية.';
    document.getElementById('modalCustomContent').innerHTML = `
      <p style="font-size:13.5px; color:#334155; line-height:1.7;">
        لتفعيل اشتراكك الفوري في باقة <strong>` + tierName + `</strong>، يرجى التواصل مع الدعم عبر واتساب أو الاتصال على الرقم: <strong>01015034659</strong>
      </p>
    `;
    document.getElementById('mainModal').classList.add('active');
  }

  function openArticleModal(artTitle, artDesc) {
    document.getElementById('modalTitle').innerText = artTitle;
    document.getElementById('modalDesc').innerText = artDesc;
    document.getElementById('modalCustomContent').innerHTML = `
      <div style="font-size:13.5px; color:#334155; line-height:1.8; text-align:right;">
        <p><strong>ملخص المقال:</strong> ` + artDesc + `</p>
        <hr style="margin:12px 0; border:none; border-top:1px solid #e2e8f0;"/>
        <p>يتناول هذا المقال التوجيهات الأكاديمية المعتمدة لطلاب الدراسات العليا، مع نماذج تطبيقية قابلة للتحميل. لقراءة المسودة الكاملة أو طلب مساعدة في تطبيقها على بحثك، تواصل مع فريق مرصاد.</p>
      </div>
    `;
    document.getElementById('mainModal').classList.add('active');
  }

  function searchFor(keyword) {
    document.getElementById('searchInput').value = keyword;
    openToolModal('البحث في: ' + keyword, 'نتائج واستكشافات ذكية حول موضوع: ' + keyword);
  }

  function handleSearch(e) {
    e.preventDefault();
    const q = document.getElementById('searchInput').value.trim();
    if(q) {
      openToolModal('البحث عن: ' + q, 'جاري معالجة استفسارك: ' + q);
    } else {
      alert('يرجى كتابة موضوع البحث أو استفسارك أولاً!');
    }
  }

  function closeModal() {
    document.getElementById('mainModal').classList.remove('active');
  }

  function closeModalOnOverlay(e) {
    if(e.target === document.getElementById('mainModal')) {
      closeModal();
    }
  }

  function toggleHelp(el) {
    const a = el.nextElementSibling;
    if(a.style.display === 'none' || a.style.display === '') {
      a.style.display = 'block';
    } else {
      a.style.display = 'none';
    }
  }
//]]>
</script>

</body>
</html>
"""

full_xml = part1 + part2 + part3 + part4 + part5 + part6 + part7 + part8 + part9 + tools_xml + part10 + part11 + part12

with open('theme.xml', 'w', encoding='utf-8') as f:
    f.write(full_xml)

print('Wrote theme.xml. Length:', len(full_xml))

try:
    ET.fromstring(full_xml)
    print('SUCCESS: XML parsed cleanly with ElementTree and is 100% syntactically valid!')
except Exception as e:
    print('ERROR parsing XML:', e)
