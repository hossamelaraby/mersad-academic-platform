import os
import xml.etree.ElementTree as ET

def read_b64(name):
    with open(name + '.b64.txt', 'r', encoding='utf-8') as f:
        return f.read().strip()

hero_cover_b64 = read_b64('hero_cover_hd.jpg')
laptop_art_b64 = read_b64('laptop_clean_opt.jpg')
logo_clean_b64 = read_b64('logo_clean_512.png')
logo_footer_b64 = read_b64('logo_footer_light.png')

tools = [
    {
        "id": "sources",
        "title": "مرصاد المصادر",
        "desc": "البحث في قواعد البيانات والمصادر الموثوقة",
        "badge": "بحث أكاديمي حي",
        "icon": '<svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0016 9.5 6.5 6.5 0 109.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>',
    },
    {
        "id": "literature",
        "title": "مرصاد الدراسات السابقة",
        "desc": "تحليل ومقارنة الدراسات وتحديد الفجوة البحثية",
        "badge": "مصفوفة مقارنة",
        "icon": '<svg viewBox="0 0 24 24"><path d="M21 5c-1.11-.35-2.33-.5-3.5-.5-1.95 0-4.05.4-5.5 1.5-1.45-1.1-3.55-1.5-5.5-1.5S2.45 4.9 1 6v14.65c0 .25.25.5.5.5.1 0 .15-.05.25-.05C3.1 20.45 5.05 20 6.5 20c1.95 0 4.05.4 5.5 1.5 1.35-.85 3.8-1.5 5.5-1.5 1.65 0 3.35.3 4.75 1.05.1.05.15.05.25.05.25 0 .5-.25.5-.5V6c-.6-.45-1.25-.75-2-1zm-1 13c-1.05-.3-2.2-.45-3.5-.45-1.6 0-3.4.4-4.5 1.25V7.5c1.1-.85 2.9-1.25 4.5-1.25 1.3 0 2.45.15 3.5.45V18z"/></svg>',
    },
    {
        "id": "researcher",
        "title": "مرصاد الباحث",
        "desc": "بناء مشكلة البحث والأسئلة والأهداف",
        "badge": "خطة البحث",
        "icon": '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>',
    },
    {
        "id": "citations",
        "title": "مرصاد التوثيق",
        "desc": "إنشاء الحواشي والمراجع بمختلف الأنماط",
        "badge": "APA / MLA",
        "icon": '<svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>',
    },
    {
        "id": "files",
        "title": "مرصاد الملفات",
        "desc": "تحليل ملفات PDF و Word واستخراج المعلومات",
        "badge": "تحليل واستخراج",
        "icon": '<svg viewBox="0 0 24 24"><path d="M20 6h-8l-2-2H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zm0 12H4V8h16v10z"/></svg>',
    },
    {
        "id": "data",
        "title": "مرصاد البيانات",
        "desc": "تحليل الاستبيانات والبيانات الإحصائية",
        "badge": "إحصاء وتحليل",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/></svg>',
    },
    {
        "id": "writing",
        "title": "مرصاد الكتابة",
        "desc": "صياغة أكاديمية احترافية مع الحفاظ على صوتك",
        "badge": "صياغة محكمة",
        "icon": '<svg viewBox="0 0 24 24"><path d="M3 17.25V21h3.75L17.81 9.94l-3.75-3.75L3 17.25zM20.71 7.04c.39-.39.39-1.02 0-1.41l-2.34-2.34c-.39-.39-1.02-.39-1.41 0l-1.83 1.83 3.75 3.75 1.83-1.83z"/></svg>',
    },
    {
        "id": "review",
        "title": "مرصاد المراجعة",
        "desc": "اكتشاف التناقضات والثغرات والمشكلات المنهجية",
        "badge": "تدقيق منهجي",
        "icon": '<svg viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>',
    },
    {
        "id": "word",
        "title": "تصدير Word",
        "desc": "إخراج بحثك في ملف منسق وجاهز",
        "badge": "تصدير DOC",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>',
    }
]

tools_html = ""
for t in tools:
    tools_html += f"""        <div class="tool-card" onclick="openSmartTool('{t['id']}')">
          <div class="tool-icon-wrap">
            {t['icon']}
          </div>
          <h3 class="tool-title">{t['title']}</h3>
          <p class="tool-desc">{t['desc']}</p>
        </div>\n"""

# Common CSS for both preview.html and theme.xml
common_css = f"""
  :root {{
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
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  body {{
    font-family: 'Cairo', -apple-system, BlinkMacSystemFont, sans-serif;
    background-color: var(--bg-page);
    color: var(--text-dark);
    direction: rtl;
    text-align: right;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }}

  a {{
    text-decoration: none;
    color: inherit;
    cursor: pointer;
  }}

  .site-wrapper {{
    max-width: 1312px;
    margin: 0 auto;
    background: #ffffff;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.05);
    position: relative;
    overflow-x: hidden;
  }}

  /* 1. HEADER (68px) */
  header.site-header {{
    height: 68px;
    background: #ffffff;
    border-bottom: 1px solid #edf2f7;
    display: flex;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 100;
  }}
  .header-container {{
    width: 100%;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .header-right-logo {{
    display: flex;
    align-items: center;
    gap: 12px;
    text-decoration: none;
  }}
  .header-logo-icon {{
    height: 48px;
    width: 48px;
    object-fit: contain;
    flex-shrink: 0;
  }}
  .header-brand-texts {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: right;
  }}
  .header-brand-name {{
    font-family: 'Reem Kufi', sans-serif;
    font-size: 24px;
    font-weight: 700;
    color: #0B2A5B;
    line-height: 1.1;
    letter-spacing: -0.5px;
  }}
  .header-brand-sub {{
    font-family: 'Cairo', sans-serif;
    font-size: 11px;
    font-weight: 700;
    color: #B88E39;
    letter-spacing: 0px;
    line-height: 1.25;
  }}
  .header-center-nav {{
    display: flex;
    align-items: center;
    gap: 30px;
  }}
  .nav-item {{
    font-size: 15px;
    font-weight: 600;
    color: #334155;
    position: relative;
    padding: 6px 0;
    transition: color 0.2s;
  }}
  .nav-item:hover {{
    color: var(--accent-blue);
  }}
  .nav-item.active {{
    color: #0B2A5B;
    font-weight: 700;
  }}
  .nav-item.active::after {{
    content: '';
    position: absolute;
    bottom: -6px;
    right: 0;
    left: 0;
    height: 3px;
    background-color: var(--accent-blue);
    border-radius: 2px;
  }}
  .nav-arrow {{
    font-size: 11px;
    margin-right: 3px;
    display: inline-block;
  }}
  .header-left-actions {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .btn-outline-wa {{
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
  }}
  .btn-outline-wa:hover {{
    border-color: #25D366;
    color: #128C7E;
    background: #f0fdf4;
  }}
  .btn-solid-call {{
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
  }}
  .btn-solid-call:hover {{
    background: #143e7d;
  }}

  /* 2. HERO SECTION */
  section.hero-section {{
    height: 285px;
    background-color: #0B2A5B;
    background-image: url('{hero_cover_b64}');
    background-size: cover;
    background-position: left center;
    background-repeat: no-repeat;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
  }}
  .hero-art-right-emblem {{
    position: absolute;
    right: 40px;
    top: 50%;
    transform: translateY(-50%);
    width: 170px;
    height: 190px;
    background-image: url('{logo_clean_b64}');
    background-size: contain;
    background-position: center;
    background-repeat: no-repeat;
    filter: drop-shadow(0 0 25px rgba(222, 179, 92, 0.45));
    z-index: 2;
    pointer-events: none;
  }}
  .hero-center-content {{
    position: relative;
    z-index: 2;
    margin-right: 235px;
    max-width: 535px;
    text-align: right;
  }}
  .hero-brand-title {{
    font-family: 'Reem Kufi', sans-serif;
    font-size: 46px;
    font-weight: 700;
    color: var(--accent-gold-light);
    line-height: 1;
    margin-bottom: 3px;
    letter-spacing: -0.5px;
    text-shadow: 0 2px 10px rgba(0,0,0,0.3);
  }}
  .hero-slogan-title {{
    font-size: 23px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 7px;
    letter-spacing: -0.2px;
  }}
  .hero-paragraph {{
    font-size: 13px;
    color: #e2e8f0;
    line-height: 1.6;
    margin-bottom: 14px;
    font-weight: 500;
  }}
  .hero-search-form {{
    background: #ffffff;
    border-radius: 30px;
    padding: 3px 5px 3px 18px;
    display: flex;
    align-items: center;
    width: 530px;
    box-shadow: 0 6px 24px rgba(0,0,0,0.25);
  }}
  .hero-search-field {{
    flex: 1;
    border: none;
    outline: none;
    font-family: 'Cairo', sans-serif;
    font-size: 13.5px;
    color: #1e293b;
    padding: 7px 10px;
  }}
  .hero-search-field::placeholder {{
    color: #94a3b8;
  }}
  .hero-search-button {{
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
  }}
  .hero-search-button:hover {{
    background: #143e7d;
  }}
  .hero-chips-row {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 11px;
  }}
  .chips-label {{
    font-size: 12px;
    color: #cbd5e1;
    font-weight: 600;
  }}
  .chip-button {{
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
  }}
  .chip-button:hover {{
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-1px);
  }}

  /* 3. TOOLS GRID (9 Vector Clean Cards) */
  section.tools-grid-section {{
    background: #FAF9F7;
    padding: 24px 16px;
    border-bottom: 1px solid #edf2f7;
  }}
  .tools-row-container {{
    width: 100%;
    max-width: 1260px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(9, 1fr);
    gap: 10px;
  }}
  .tool-card {{
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
  }}
  .tool-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(11, 42, 91, 0.1);
    border-color: #2F6FC7;
  }}
  .tool-icon-wrap {{
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #0B2A5B;
    margin-bottom: 10px;
    transition: transform 0.2s;
  }}
  .tool-card:hover .tool-icon-wrap {{
    transform: scale(1.1);
    color: #2F6FC7;
  }}
  .tool-icon-wrap svg {{
    width: 26px;
    height: 26px;
    fill: currentColor;
  }}
  .tool-title {{
    font-size: 13.5px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 5px;
    line-height: 1.3;
  }}
  .tool-desc {{
    font-size: 10.5px;
    color: #64748b;
    line-height: 1.45;
    font-weight: 500;
  }}

  /* 4. MIDDLE SECTION (RTL: 415px Why Us on Right, 805px Integrated on Left) */
  section.middle-features-section {{
    background: #FAF9F7;
    padding: 20px 16px;
  }}
  .middle-row-container {{
    width: 100%;
    max-width: 1240px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 415px 805px;
    gap: 20px;
  }}

  /* Right Card: Why Us */
  .card-why-us {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
  }}
  .why-us-heading {{
    font-size: 20px;
    font-weight: 800;
    color: #0B2A5B;
    text-align: center;
    margin-bottom: 14px;
  }}
  .why-us-items {{
    display: flex;
    flex-direction: column;
    gap: 11px;
  }}
  .why-us-row {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .why-us-badge {{
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
  }}
  .why-us-texts h4 {{
    font-size: 13px;
    font-weight: 800;
    color: #0B2A5B;
    line-height: 1.2;
  }}
  .why-us-texts p {{
    font-size: 11px;
    color: #64748b;
    margin-top: 1px;
  }}

  /* Left Card: Integrated Tools */
  .card-integrated {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    overflow: hidden;
    display: flex;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
    min-height: 250px;
  }}
  .integrated-content {{
    flex: 1.15;
    padding: 22px 24px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}
  .integrated-title {{
    font-size: 20px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 6px;
  }}
  .integrated-description {{
    font-size: 12.5px;
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 12px;
  }}
  .integrated-checklist {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 16px;
  }}
  .integrated-checklist li {{
    font-size: 12.5px;
    font-weight: 700;
    color: #1e293b;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .check-badge {{
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
  }}
  .btn-integrated-explore {{
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
  }}
  .btn-integrated-explore:hover {{
    background: #143e7d;
  }}
  .integrated-banner-side {{
    flex: 0.95;
    background-color: #f8fafc;
    background-image: url('{laptop_art_b64}');
    background-size: cover;
    background-position: center;
    min-height: 250px;
  }}

  /* 5. BOTTOM SECTION (RTL: Services 315px Right, Packages 425px Center, How 460px Left) */
  section.bottom-three-section {{
    background: #FAF9F7;
    padding: 10px 16px 28px;
  }}
  .bottom-grid-container {{
    width: 100%;
    max-width: 1240px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 315px 425px 460px;
    gap: 20px;
    align-items: stretch;
  }}

  /* Services Card */
  .card-services {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 20px 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
  }}
  .services-top-header {{
    display: flex;
    align-items: center;
    gap: 8px;
    color: #0B2A5B;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 5px;
  }}
  .services-short-desc {{
    font-size: 11.5px;
    color: #64748b;
    margin-bottom: 10px;
    line-height: 1.5;
  }}
  .services-items-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 12px;
    font-size: 12px;
    font-weight: 600;
    color: #1e293b;
  }}
  .services-items-list li {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .services-items-list li::before {{
    content: '✓';
    color: #2F6FC7;
    font-weight: 800;
  }}
  .services-contact-bubble {{
    background: #edf2f7;
    border-right: 3px solid #0B2A5B;
    padding: 8px 10px;
    border-radius: 4px;
    margin-bottom: 12px;
    font-size: 11px;
    color: #334155;
    line-height: 1.5;
  }}
  .services-contact-bubble a {{
    color: #0B2A5B;
    font-weight: bold;
    direction: ltr;
    display: inline-block;
  }}
  .services-actions-group {{
    display: flex;
    gap: 8px;
  }}
  .services-call-btn {{
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
  }}
  .services-call-btn:hover {{
    background: #143e7d;
  }}
  .services-wa-icon-btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 14px;
    background: #25D366;
    color: #ffffff;
    border-radius: 8px;
    transition: background 0.2s;
  }}
  .services-wa-icon-btn:hover {{
    background: #1ebd5b;
  }}

  /* Packages Card */
  .card-packages {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 20px 16px;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
    display: flex;
    flex-direction: column;
  }}
  .packages-header-title {{
    font-size: 19px;
    font-weight: 800;
    color: #0B2A5B;
    text-align: center;
    margin-bottom: 16px;
  }}
  .packages-cards-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 8px;
    flex: 1;
  }}
  .tier-box {{
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
  }}
  .tier-box.popular {{
    border: 2px solid #2F6FC7;
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(47, 111, 199, 0.12);
  }}
  .tier-popular-tag {{
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
  }}
  .tier-title {{
    font-size: 14.5px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 2px;
  }}
  .tier-cost {{
    font-size: 11px;
    color: #64748b;
    margin-bottom: 8px;
    padding-bottom: 6px;
    border-bottom: 1px solid #f1f5f9;
  }}
  .tier-cost strong {{
    font-size: 16px;
    color: #0B2A5B;
  }}
  .tier-perks {{
    list-style: none;
    text-align: right;
    display: flex;
    flex-direction: column;
    gap: 5px;
    margin-bottom: 10px;
    font-size: 10px;
    color: #475569;
    flex: 1;
  }}
  .tier-perks li {{
    display: flex;
    align-items: flex-start;
    gap: 4px;
    line-height: 1.35;
  }}
  .tier-perks li::before {{
    content: '✓';
    color: #2F6FC7;
    font-weight: bold;
    font-size: 10.5px;
    flex-shrink: 0;
  }}
  .tier-action-btn {{
    display: block;
    width: 100%;
    padding: 6px 0;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 700;
    text-align: center;
    transition: all 0.2s;
    cursor: pointer;
  }}
  .tier-btn-outline {{
    border: 1.5px solid #0B2A5B;
    color: #0B2A5B;
    background: transparent;
  }}
  .tier-btn-outline:hover {{
    background: #0B2A5B;
    color: #fff;
  }}
  .tier-btn-fill {{
    background: #2F6FC7;
    color: #ffffff;
    border: none;
  }}
  .tier-btn-fill:hover {{
    background: #1D58A7;
  }}

  /* How to Start Card */
  .card-how-to-start {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 24px 20px 18px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 3px 12px rgba(0,0,0,0.03);
  }}
  .how-title {{
    font-size: 19px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 20px;
  }}
  .how-steps-diagram {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 20px 0;
    padding: 0 4px;
  }}
  .step-item {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 76px;
    position: relative;
    cursor: pointer;
    transition: transform 0.2s;
  }}
  .step-item:hover {{
    transform: scale(1.05);
  }}
  .step-num {{
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
  }}
  .step-round-circle {{
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
  }}
  .step-round-circle svg {{
    width: 22px;
    height: 22px;
    fill: currentColor;
  }}
  .step-label {{
    font-size: 11px;
    font-weight: 700;
    color: #1e293b;
    line-height: 1.35;
  }}
  .step-divider-arrow {{
    color: #94a3b8;
    font-size: 14px;
    margin-top: -24px;
  }}
  .how-quote {{
    font-family: 'Aref Ruqaa', serif;
    font-size: 18px;
    color: #0B2A5B;
    text-align: center;
    margin-top: 14px;
  }}

  /* 6. ARTICLES SECTION */
  .inner-section-view {{
    padding: 40px 20px;
    max-width: 1240px;
    margin: 0 auto;
  }}
  .inner-section-header {{
    text-align: center;
    margin-bottom: 30px;
  }}
  .inner-section-header h2 {{
    font-size: 26px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 8px;
  }}
  .inner-section-header p {{
    font-size: 14px;
    color: #64748b;
  }}
  .articles-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }}
  .article-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    transition: transform 0.2s;
    cursor: pointer;
    display: flex;
    flex-direction: column;
  }}
  .article-card:hover {{
    transform: translateY(-4px);
    box-shadow: 0 8px 20px rgba(11, 42, 91, 0.08);
  }}
  .article-card-cover {{
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
    line-height: 1.4;
  }}
  .article-card-body {{
    padding: 18px;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .article-tag {{
    display: inline-block;
    background: #FAF5E9;
    color: #B88E39;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
    margin-bottom: 8px;
    align-self: flex-start;
  }}
  .article-title {{
    font-size: 15.5px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 6px;
    line-height: 1.4;
  }}
  .article-snippet {{
    font-size: 12px;
    color: #64748b;
    line-height: 1.6;
    margin-bottom: 12px;
  }}
  .article-link-more {{
    color: #2F6FC7;
    font-size: 12.5px;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    gap: 4px;
    margin-top: auto;
  }}

  /* 7. HELP SECTION */
  .help-accordion {{
    max-width: 800px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}
  .help-item {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 10px;
    overflow: hidden;
  }}
  .help-q {{
    padding: 16px 20px;
    font-size: 15px;
    font-weight: 700;
    color: #0B2A5B;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .help-a {{
    padding: 0 20px 16px;
    font-size: 13.5px;
    color: #475569;
    line-height: 1.6;
  }}

  /* BLOGGER POST VIEW / INNER PAGE STYLES */
  .blog-inner-container {{
    max-width: 900px;
    margin: 0 auto;
    padding: 40px 20px;
  }}
  .post-article {{
    background: #ffffff;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
    padding: 36px 32px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.03);
  }}
  .post-header {{
    border-bottom: 1px solid #edf2f7;
    padding-bottom: 20px;
    margin-bottom: 24px;
  }}
  .post-title {{
    font-size: 28px;
    font-weight: 900;
    color: #0B2A5B;
    line-height: 1.4;
    margin-bottom: 12px;
  }}
  .post-meta {{
    font-size: 13px;
    color: #64748b;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
  }}
  .post-body {{
    font-size: 16px;
    line-height: 1.85;
    color: #1e293b;
  }}
  .post-body p {{
    margin-bottom: 18px;
  }}
  .post-body h2, .post-body h3 {{
    color: #0B2A5B;
    margin: 26px 0 14px;
  }}
  .post-body img {{
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    margin: 16px 0;
  }}
  .post-contact-card {{
    margin-top: 36px;
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-right: 4px solid #0B2A5B;
    padding: 24px;
    border-radius: 12px;
    text-align: right;
  }}
  .post-contact-card h4 {{
    color: #0B2A5B;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 8px;
  }}
  .post-contact-card p {{
    color: #475569;
    font-size: 13.5px;
    line-height: 1.6;
    margin-bottom: 16px;
  }}

  /* 8. FOOTER */
  footer.site-footer {{
    background: #0B2A5B;
    color: #ffffff;
    padding: 20px 0;
  }}
  .footer-container {{
    width: 100%;
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .footer-right-brand {{
    display: flex;
    align-items: center;
  }}
  .footer-center-nav {{
    display: flex;
    align-items: center;
    gap: 22px;
  }}
  .footer-link {{
    color: #cbd5e1;
    font-size: 13.5px;
    font-weight: 600;
    transition: color 0.2s;
  }}
  .footer-link:hover {{
    color: #ffffff;
  }}
  .footer-left-social {{
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 4px;
  }}
  .social-icons-row {{
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .social-link {{
    color: #94a3b8;
    transition: color 0.2s;
    display: inline-flex;
  }}
  .social-link:hover {{
    color: #ffffff;
  }}
  .social-link svg {{
    width: 18px;
    height: 18px;
    fill: currentColor;
  }}
  .copyright-text {{
    font-size: 11.5px;
    color: #94a3b8;
  }}

  /* ADVANCED SMART MODALS & DEDICATED TOOLS */
  .modal-overlay {{
    position: fixed;
    inset: 0;
    background: rgba(11, 42, 91, 0.7);
    backdrop-filter: blur(6px);
    display: none;
    align-items: center;
    justify-content: center;
    z-index: 9999;
    padding: 20px;
    overflow-y: auto;
  }}
  .modal-overlay.active {{
    display: flex;
  }}
  .modal-box {{
    background: #ffffff;
    border-radius: 18px;
    max-width: 760px;
    width: 100%;
    max-height: 90vh;
    overflow-y: auto;
    padding: 30px;
    box-shadow: 0 15px 50px rgba(0,0,0,0.3);
    position: relative;
    text-align: right;
    animation: modalPop 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  }}
  @keyframes modalPop {{
    0% {{ transform: scale(0.92); opacity: 0; }}
    100% {{ transform: scale(1); opacity: 1; }}
  }}
  .modal-close-btn {{
    position: absolute;
    left: 20px;
    top: 20px;
    background: #f1f5f9;
    border: none;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: bold;
    color: #64748b;
    cursor: pointer;
    transition: all 0.2s;
    z-index: 10;
  }}
  .modal-close-btn:hover {{
    background: #e2e8f0;
    color: #0f172a;
    transform: scale(1.08);
  }}
  .modal-header-badge-row {{
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 12px;
  }}
  .modal-tool-icon {{
    width: 48px;
    height: 48px;
    background: #FAF5E9;
    color: #B88E39;
    border: 1px solid #E6D4AA;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }}
  .modal-tool-icon svg {{
    width: 26px;
    height: 26px;
    fill: currentColor;
  }}
  .modal-title {{
    font-size: 22px;
    font-weight: 800;
    color: #0B2A5B;
    line-height: 1.2;
  }}
  .modal-badge-tag {{
    display: inline-block;
    background: #edf2f7;
    color: #0B2A5B;
    font-size: 11px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 6px;
  }}
  .modal-desc {{
    font-size: 13.5px;
    color: #64748b;
    line-height: 1.5;
    margin-bottom: 20px;
  }}

  /* Tool Specific Form Elements */
  .tool-field-label {{
    display: block;
    font-size: 13px;
    font-weight: 700;
    color: #0B2A5B;
    margin-bottom: 6px;
  }}
  .tool-input-text, .tool-select, .tool-textarea {{
    width: 100%;
    padding: 10px 14px;
    border: 1.5px solid #cbd5e1;
    border-radius: 10px;
    font-family: 'Cairo', sans-serif;
    font-size: 13.5px;
    color: #1e293b;
    background: #fff;
    outline: none;
    transition: border-color 0.2s;
    margin-bottom: 14px;
  }}
  .tool-input-text:focus, .tool-select:focus, .tool-textarea:focus {{
    border-color: #2F6FC7;
    box-shadow: 0 0 0 3px rgba(47, 111, 199, 0.1);
  }}
  .tool-textarea {{
    min-height: 90px;
    resize: vertical;
  }}
  .tool-file-dropzone {{
    border: 2px dashed #94a3b8;
    background: #f8fafc;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    cursor: pointer;
    margin-bottom: 14px;
    transition: all 0.2s;
  }}
  .tool-file-dropzone:hover {{
    border-color: #2F6FC7;
    background: #f0fdf4;
  }}
  .tool-btn-primary {{
    background: #0B2A5B;
    color: #ffffff;
    border: none;
    padding: 11px 24px;
    border-radius: 10px;
    font-family: 'Cairo', sans-serif;
    font-size: 14px;
    font-weight: 800;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    transition: background 0.2s;
    width: 100%;
  }}
  .tool-btn-primary:hover {{
    background: #143e7d;
  }}
  .tool-result-container {{
    margin-top: 20px;
    padding: 18px;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    text-align: right;
  }}
  .paper-source-card {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 10px;
    transition: all 0.2s;
  }}
  .paper-source-card:hover {{
    border-color: #2F6FC7;
    box-shadow: 0 4px 12px rgba(11, 42, 91, 0.06);
  }}
  .paper-title {{
    font-size: 14.5px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 4px;
  }}
  .paper-meta {{
    font-size: 11.5px;
    color: #64748b;
    margin-bottom: 8px;
  }}
  .paper-links-row {{
    display: flex;
    gap: 10px;
    margin-top: 8px;
  }}
  .paper-btn-link {{
    font-size: 11.5px;
    font-weight: 700;
    color: #2F6FC7;
    background: #f1f5f9;
    padding: 4px 10px;
    border-radius: 6px;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }}
  .paper-btn-link:hover {{
    background: #e2e8f0;
  }}

  /* Citation Output Box */
  .citation-box {{
    background: #ffffff;
    border: 1px solid #cbd5e1;
    border-right: 4px solid #C9A24B;
    border-radius: 8px;
    padding: 12px 14px;
    margin-top: 10px;
    font-size: 13.5px;
    color: #1e293b;
    line-height: 1.6;
    position: relative;
  }}

  /* Matrix Table */
  .matrix-table {{
    width: 100%;
    border-collapse: collapse;
    margin-top: 12px;
    font-size: 12px;
  }}
  .matrix-table th, .matrix-table td {{
    border: 1px solid #cbd5e1;
    padding: 8px 10px;
    text-align: right;
  }}
  .matrix-table th {{
    background: #0B2A5B;
    color: #ffffff;
    font-weight: 700;
  }}
  .matrix-table tr:nth-child(even) {{
    background: #f8fafc;
  }}

  /* Responsive Rules */
  @media (max-width: 1024px) {{
    .hero-center-content {{
      margin-right: 20px;
      max-width: calc(100% - 40px);
    }}
    .hero-art-right-emblem {{
      display: none;
    }}
    .tools-row-container {{
      grid-template-columns: repeat(5, 1fr);
    }}
    .middle-row-container {{
      grid-template-columns: 1fr;
    }}
    .bottom-grid-container {{
      grid-template-columns: 1fr;
    }}
    .articles-grid {{
      grid-template-columns: 1fr;
    }}
  }}

  @media (max-width: 768px) {{
    .header-center-nav {{
      display: none;
    }}
    .hero-section {{
      height: auto;
      padding: 30px 16px;
      background-position: center;
    }}
    .hero-center-content {{
      margin-right: 0;
      max-width: 100%;
    }}
    .hero-brand-title {{
      font-size: 36px;
    }}
    .hero-slogan-title {{
      font-size: 19px;
    }}
    .hero-search-form {{
      width: 100%;
    }}
    .hero-chips-row {{
      flex-wrap: wrap;
    }}
    .tools-row-container {{
      grid-template-columns: repeat(3, 1fr);
    }}
    .card-integrated {{
      flex-direction: column-reverse;
    }}
    .packages-cards-grid {{
      grid-template-columns: 1fr;
    }}
    .footer-container {{
      flex-direction: column;
      gap: 16px;
      text-align: center;
    }}
    .footer-left-social {{
      align-items: center;
    }}
  }}
"""

print("Common CSS compiled successfully.")
