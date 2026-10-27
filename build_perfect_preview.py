import os

def read_b64(name):
    with open(name + '.b64.txt', 'r', encoding='utf-8') as f:
        return f.read().strip()

hero_bg = read_b64('hero_clean_bg.png')
laptop_banner = read_b64('laptop_books_banner.png')
header_logo = read_b64('header_logo_exact.png')
footer_logo = read_b64('footer_logo_exact.png')

tool_cards_b64 = [read_b64(f'tool_card_{i}.png') for i in range(1, 10)]

tools_data = [
    ("المصادر", "/search/label/المصادر"),
    ("الدراسات السابقة", "/search/label/الدراسات%20السابقة"),
    ("الباحث", "/search/label/الباحث"),
    ("التوثيق", "/search/label/التوثيق"),
    ("الملفات", "/search/label/الملفات"),
    ("البيانات", "/search/label/البيانات"),
    ("الكتابة", "/search/label/الكتابة"),
    ("المراجعة", "/search/label/المراجعة"),
    ("تصدير Word", "/search/label/تصدير%20Word"),
]

# Generate tool cards HTML
tools_html = ""
for idx, (title, link) in enumerate(tools_data):
    img_src = tool_cards_b64[idx]
    tools_html += f"""        <a href="{link}" class="tool-card-link" title="{title}">
          <img src="{img_src}" alt="{title}" class="tool-card-img" />
        </a>\n"""

html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>مرصاد | منصة الذكاء الاصطناعي للبحث العلمي العربي</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Reem+Kufi:wght@500;600;700&family=Aref+Ruqaa:wght@400;700&display=swap" rel="stylesheet" />
<style>
  :root {{
    --primary-navy: #0B2A5B;
    --navy-dark: #0B233F;
    --accent-blue: #2F6FC7;
    --accent-blue-hover: #1D58A7;
    --accent-gold: #C9A24B;
    --card-cream: #FAF9F6;
    --card-border: #E2E8F0;
    --text-dark: #14213D;
    --text-muted: #6B7280;
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
  }}

  /* Page Wrapper */
  .site-wrapper {{
    max-width: 1312px;
    margin: 0 auto;
    background: #ffffff;
    box-shadow: 0 0 30px rgba(0, 0, 0, 0.05);
    overflow: hidden;
  }}

  /* 1. HEADER (65px) */
  header.site-header {{
    height: 65px;
    background: #ffffff;
    border-bottom: 1px solid #edf2f7;
    display: flex;
    align-items: center;
    position: relative;
    z-index: 50;
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
  }}
  .header-logo-image {{
    height: 48px;
    width: auto;
    object-fit: contain;
  }}
  .header-center-nav {{
    display: flex;
    align-items: center;
    gap: 32px;
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

  /* 2. HERO SECTION (270px) */
  section.hero-section {{
    height: 270px;
    background-color: #0B2A5B;
    background-image: url('{hero_bg}');
    background-size: 1312px 270px;
    background-position: center;
    background-repeat: no-repeat;
    position: relative;
    overflow: hidden;
  }}
  .hero-content-box {{
    position: absolute;
    right: 310px;
    top: 25px;
    width: 540px;
    text-align: right;
  }}
  .hero-brand-title {{
    font-family: 'Reem Kufi', sans-serif;
    font-size: 42px;
    font-weight: 700;
    color: #deb35c;
    line-height: 1;
    margin-bottom: 2px;
    letter-spacing: -0.5px;
  }}
  .hero-slogan-title {{
    font-size: 22.5px;
    font-weight: 800;
    color: #ffffff;
    margin-bottom: 6px;
    letter-spacing: -0.2px;
  }}
  .hero-paragraph {{
    font-size: 12.5px;
    color: #e2e8f0;
    line-height: 1.55;
    margin-bottom: 12px;
    font-weight: 500;
  }}
  .hero-search-form {{
    background: #ffffff;
    border-radius: 30px;
    padding: 3px 5px 3px 16px;
    display: flex;
    align-items: center;
    width: 530px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.2);
  }}
  .hero-search-field {{
    flex: 1;
    border: none;
    outline: none;
    font-family: 'Cairo', sans-serif;
    font-size: 13.5px;
    color: #1e293b;
    padding: 6px 8px;
  }}
  .hero-search-field::placeholder {{
    color: #94a3b8;
  }}
  .hero-search-button {{
    background: #0f2c4f;
    color: #ffffff;
    border: none;
    border-radius: 22px;
    padding: 6px 18px;
    font-family: 'Cairo', sans-serif;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 5px;
    transition: background 0.2s;
  }}
  .hero-search-button:hover {{
    background: #19467d;
  }}
  .hero-chips-row {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 10px;
  }}
  .chips-label {{
    font-size: 12px;
    color: #cbd5e1;
    font-weight: 600;
  }}
  .chip-button {{
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(4px);
    border: 1px solid rgba(255, 255, 255, 0.22);
    color: #ffffff;
    font-size: 11.5px;
    font-weight: 600;
    padding: 2px 10px;
    border-radius: 14px;
    transition: all 0.2s;
  }}
  .chip-button:hover {{
    background: rgba(255, 255, 255, 0.28);
    color: #ffffff;
  }}

  /* 3. TOOLS GRID (133px) */
  section.tools-grid-section {{
    height: 133px;
    background: #FAF9F7;
    display: flex;
    align-items: center;
    padding: 0 16px;
    overflow: hidden;
  }}
  .tools-row-container {{
    width: 100%;
    max-width: 1280px;
    margin: 0 auto;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 7px;
  }}
  .tool-card-link {{
    display: block;
    flex: 1;
    max-width: 135px;
    height: 115px;
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.03);
  }}
  .tool-card-link:hover {{
    transform: translateY(-3px);
    box-shadow: 0 6px 16px rgba(11, 42, 91, 0.12);
  }}
  .tool-card-img {{
    width: 100%;
    height: 100%;
    object-fit: fill;
    display: block;
  }}

  /* 4. MIDDLE SECTION (257px) */
  section.middle-features-section {{
    height: 257px;
    background: #FAF9F7;
    padding: 10px 16px 12px;
    display: flex;
    align-items: center;
  }}
  .middle-row-container {{
    width: 100%;
    max-width: 1240px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 805px 415px;
    gap: 20px;
    height: 235px;
  }}

  /* Left card (Integrated Tools) */
  .card-integrated {{
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    overflow: hidden;
    display: flex;
    box-shadow: 0 3px 10px rgba(0,0,0,0.03);
    height: 100%;
  }}
  .integrated-content {{
    flex: 1.15;
    padding: 18px 22px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }}
  .integrated-title {{
    font-size: 19px;
    font-weight: 800;
    color: #0B2A5B;
    margin-bottom: 6px;
  }}
  .integrated-description {{
    font-size: 12px;
    color: #64748b;
    line-height: 1.55;
    margin-bottom: 12px;
  }}
  .integrated-checklist {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 14px;
  }}
  .integrated-checklist li {{
    font-size: 12px;
    font-weight: 700;
    color: #1e293b;
    display: flex;
    align-items: center;
    gap: 7px;
  }}
  .check-badge {{
    width: 16px;
    height: 16px;
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
    font-size: 12px;
    font-weight: 700;
    padding: 7px 16px;
    border-radius: 7px;
    transition: background 0.2s;
  }}
  .btn-integrated-explore:hover {{
    background: #143e7d;
  }}
  .integrated-banner-side {{
    flex: 0.95;
    background-color: #f1ede8;
    background-image: url('{laptop_banner}');
    background-size: cover;
    background-position: center;
    height: 100%;
  }}

  /* Right card (Why Us) */
  .card-why-us {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 16px 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 3px 10px rgba(0,0,0,0.03);
    height: 100%;
  }}
  .why-us-heading {{
    font-size: 19px;
    font-weight: 800;
    color: #0B2A5B;
    text-align: center;
    margin-bottom: 12px;
  }}
  .why-us-items {{
    display: flex;
    flex-direction: column;
    gap: 10px;
  }}
  .why-us-row {{
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .why-us-badge {{
    width: 34px;
    height: 34px;
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
    font-size: 12.5px;
    font-weight: 800;
    color: #0B2A5B;
    line-height: 1.2;
  }}
  .why-us-texts p {{
    font-size: 10.5px;
    color: #64748b;
    margin-top: 1px;
  }}

  /* 5. BOTTOM SECTION (404px) */
  section.bottom-three-section {{
    height: 404px;
    background: #FAF9F7;
    padding: 10px 16px 16px;
    display: flex;
    align-items: center;
  }}
  .bottom-grid-container {{
    width: 100%;
    max-width: 1240px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: 460px 425px 315px;
    gap: 20px;
    height: 375px;
    align-items: stretch;
  }}

  /* Left card (How to Start) */
  .card-how-to-start {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 22px 18px 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 3px 10px rgba(0,0,0,0.03);
    height: 100%;
  }}
  .how-title {{
    font-size: 18px;
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
    width: 44px;
    height: 44px;
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
    font-size: 17px;
    color: #0B2A5B;
    text-align: center;
    margin-top: 10px;
  }}

  /* Center card (Subscription Packages / Latest Posts) */
  .card-packages {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 18px 14px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.03);
    height: 100%;
    display: flex;
    flex-direction: column;
  }}
  .packages-header-title {{
    font-size: 18px;
    font-weight: 800;
    color: #0B2A5B;
    text-align: center;
    margin-bottom: 14px;
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
    font-size: 14px;
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

  /* Right card (Researcher Services) */
  .card-services {{
    background: #FAF8F5;
    border: 1px solid #e7ecf2;
    border-radius: 16px;
    padding: 18px 16px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: 0 3px 10px rgba(0,0,0,0.03);
    height: 100%;
  }}
  .services-top-header {{
    display: flex;
    align-items: center;
    gap: 7px;
    color: #0B2A5B;
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 4px;
  }}
  .services-short-desc {{
    font-size: 11px;
    color: #64748b;
    margin-bottom: 10px;
    line-height: 1.45;
  }}
  .services-items-list {{
    list-style: none;
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-bottom: 12px;
    font-size: 11.5px;
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
    padding: 7px 9px;
    border-radius: 4px;
    margin-bottom: 12px;
    font-size: 10.5px;
    color: #334155;
    line-height: 1.45;
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
    font-size: 12px;
    font-weight: 700;
    padding: 8px 0;
    border-radius: 7px;
    transition: background 0.2s;
  }}
  .services-call-btn:hover {{
    background: #143e7d;
  }}
  .services-wa-icon-btn {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 12px;
    background: #25D366;
    color: #ffffff;
    border-radius: 7px;
    transition: background 0.2s;
  }}
  .services-wa-icon-btn:hover {{
    background: #1ebd5b;
  }}

  /* 6. FOOTER (70px) */
  footer.site-footer {{
    height: 70px;
    background: #0B2A5B;
    color: #ffffff;
    display: flex;
    align-items: center;
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
  .footer-logo-image {{
    height: 42px;
    width: auto;
    object-fit: contain;
  }}
  .footer-center-nav {{
    display: flex;
    align-items: center;
    gap: 22px;
  }}
  .footer-link {{
    color: #cbd5e1;
    font-size: 13px;
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
  .copyright-text {{
    font-size: 11px;
    color: #94a3b8;
  }}

  /* SVGs */
  .icon-svg {{
    width: 18px;
    height: 18px;
    fill: currentColor;
    display: inline-block;
  }}
  .icon-svg-sm {{
    width: 15px;
    height: 15px;
    fill: currentColor;
    display: inline-block;
  }}

  /* Responsive Rules */
  @media (max-width: 1024px) {{
    section.hero-section {{
      background-size: cover;
    }}
    .hero-content-box {{
      right: 20px;
      width: calc(100% - 40px);
    }}
    section.tools-grid-section {{
      height: auto;
      padding: 16px;
    }}
    .tools-row-container {{
      flex-wrap: wrap;
      justify-content: center;
    }}
    .tool-card-link {{
      flex: 0 0 calc(20% - 8px);
    }}
    section.middle-features-section {{
      height: auto;
      padding: 16px;
    }}
    .middle-row-container {{
      grid-template-columns: 1fr;
      height: auto;
    }}
    section.bottom-three-section {{
      height: auto;
      padding: 16px;
    }}
    .bottom-grid-container {{
      grid-template-columns: 1fr;
      height: auto;
    }}
  }}

  @media (max-width: 768px) {{
    .header-center-nav {{
      display: none;
    }}
    .hero-search-form {{
      width: 100%;
    }}
    .tool-card-link {{
      flex: 0 0 calc(33.333% - 8px);
    }}
    .card-integrated {{
      flex-direction: column-reverse;
    }}
    .integrated-banner-side {{
      height: 180px;
    }}
    .packages-cards-grid {{
      grid-template-columns: 1fr;
    }}
    footer.site-footer {{
      height: auto;
      padding: 20px 0;
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
</style>
</head>
<body>

<div class="site-wrapper">

  <!-- 1. HEADER (65px) -->
  <header class="site-header">
    <div class="header-container">
      
      <!-- Right: Logo -->
      <div class="header-right-logo">
        <a href="/">
          <img class="header-logo-image" src="{header_logo}" alt="مرصاد - منصة الذكاء الاصطناعي للبحث العلمي العربي" />
        </a>
      </div>

      <!-- Center: Navigation -->
      <nav class="header-center-nav">
        <a href="#" class="nav-item active">الرئيسية</a>
        <a href="#tools" class="nav-item">الأدوات <span class="nav-arrow">▾</span></a>
        <a href="#services" class="nav-item">خدمات الأبحاث</a>
        <a href="#articles" class="nav-item">المقالات</a>
        <a href="#help" class="nav-item">مساعدة</a>
      </nav>

      <!-- Left: WhatsApp & Call CTA -->
      <div class="header-left-actions">
        <a href="https://wa.me/201015034659" target="_blank" class="btn-outline-wa">
          <svg class="icon-svg-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          <span>واتساب</span>
        </a>
        <a href="tel:01015034659" class="btn-solid-call">
          <svg class="icon-svg-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-2.2 2.2a15.045 15.045 0 01-6.59-6.59l2.2-2.21a.96.96 0 00.25-1.01A11.36 11.36 0 018.57 3.9c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1 0 9.39 7.61 17 17 17 .55 0 1-.45 1-1v-3.52c0-.55-.45-1-.99-1z"/></svg>
          <span>اتصل الآن</span>
        </a>
      </div>

    </div>
  </header>

  <!-- 2. HERO SECTION (270px) -->
  <section class="hero-section">
    <div class="hero-content-box">
      <h1 class="hero-brand-title">مِرْصَاد</h1>
      <h2 class="hero-slogan-title">نرصد المعرفة، ونبني البحث.</h2>
      <p class="hero-paragraph">
        منصة ذكاء اصطناعي للباحثين والمعلمين وطلاب الدراسات العليا،<br/>
        تساعدك على إنجاز بحثك بدقة واحترافية، من الفكرة إلى الملف النهائي.
      </p>
      <form class="hero-search-form" action="/search" method="get">
        <input type="text" name="q" class="hero-search-field" placeholder="اكتب موضوع بحثك أو ارفع ملفك..." />
        <button type="submit" class="hero-search-button">
          <span>ابدأ الآن</span>
          <span>✦</span>
        </button>
      </form>
      <div class="hero-chips-row">
        <span class="chips-label">أمثلة مقترحة:</span>
        <a href="/search?q=الدراسات+السابقة" class="chip-button">الدراسات السابقة</a>
        <a href="/search?q=تحليل+الاستبيان" class="chip-button">تحليل الاستبيان</a>
        <a href="/search?q=توثيق+المراجع" class="chip-button">توثيق المراجع</a>
        <a href="/search?q=صياغة+أكاديمية" class="chip-button">صياغة أكاديمية</a>
      </div>
    </div>
  </section>

  <!-- 3. TOOLS GRID (133px) -->
  <section class="tools-grid-section" id="tools">
    <div class="tools-row-container">
{tools_html}    </div>
  </section>

  <!-- 4. MIDDLE SECTION (257px) -->
  <section class="middle-features-section">
    <div class="middle-row-container">
      
      <!-- Left Card: Integrated Tools (805px) -->
      <div class="card-integrated">
        <div class="integrated-content">
          <h3 class="integrated-title">أدوات متكاملة لرحلتك البحثية</h3>
          <p class="integrated-description">
            لا نفهمك للكتابة فقط، بل نساعدك في التحليل، والمراجعة، والتوثيق،<br/>
            حتى تصل إلى بحث متكامل وجاهز للنشر أو المناقشة.
          </p>
          <ul class="integrated-checklist">
            <li><span class="check-badge">✓</span> مصادر موثوقة ومحدثة</li>
            <li><span class="check-badge">✓</span> نتائج دقيقة وقابلة للتحقق</li>
            <li><span class="check-badge">✓</span> دعم اللغة العربية الأكاديمية</li>
            <li><span class="check-badge">✓</span> تصدير احترافي إلى Word</li>
          </ul>
          <a href="#tools" class="btn-integrated-explore">
            <span>استكشف جميع الأدوات</span>
            <span>←</span>
          </a>
        </div>
        <div class="integrated-banner-side"></div>
      </div>

      <!-- Right Card: Why Us (415px) -->
      <div class="card-why-us">
        <h3 class="why-us-heading">لماذا مِرْصَاد؟</h3>
        <div class="why-us-items">
          
          <div class="why-us-row">
            <div class="why-us-badge">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
            </div>
            <div class="why-us-texts">
              <h4>يوفر وقتك وجهدك</h4>
              <p>بدلاً من البحث اليدوي الطويل</p>
            </div>
          </div>

          <div class="why-us-row">
            <div class="why-us-badge">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg>
            </div>
            <div class="why-us-texts">
              <h4>دقة وموثوقية</h4>
              <p>بمصادر حقيقية وقابلة للتحقق</p>
            </div>
          </div>

          <div class="why-us-row">
            <div class="why-us-badge">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12.87 15.07l-2.54-2.51.03-.03c1.74-1.94 2.98-4.17 3.71-6.53H17V4h-7V2H8v2H1v1.99h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11.76-2.04zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2l-4.5-12zm-2.62 7l1.62-4.33L19.12 17h-3.24z"/></svg>
            </div>
            <div class="why-us-texts">
              <h4>دعم كامل باللغة العربية</h4>
              <p>بأسلوب أكاديمي واضح وسليم</p>
            </div>
          </div>

          <div class="why-us-row">
            <div class="why-us-badge">
              <svg class="icon-svg" viewBox="0 0 24 24"><path d="M4 8h4V4H4v4zm6 12h4v-4h-4v4zm-6 0h4v-4H4v4zm0-6h4v-4H4v4zm6 0h4v-4h-4v4zm6-10v4h4V4h-4zm-6 4h4V4h-4v4zm6 6h4v-4h-4v4zm0 6h4v-4h-4v4z"/></svg>
            </div>
            <div class="why-us-texts">
              <h4>مناسب لجميع التخصصات</h4>
              <p>من العلوم الإنسانية إلى العلوم التطبيقية</p>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>

  <!-- 5. BOTTOM SECTION (404px) -->
  <section class="bottom-three-section">
    <div class="bottom-grid-container">
      
      <!-- Left: How to start (460px) -->
      <div class="card-how-to-start">
        <div>
          <h3 class="how-title">كيف تبدأ؟</h3>
          <div class="how-steps-diagram">
            
            <div class="step-item">
              <span class="step-num">4</span>
              <div class="step-round-circle">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
              </div>
              <div class="step-label">أنشئ حسابك<br/>مجانًا</div>
            </div>

            <div class="step-divider-arrow">←</div>

            <div class="step-item">
              <span class="step-num">2</span>
              <div class="step-round-circle">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
              </div>
              <div class="step-label">أدخل موضوع بحثك<br/>أو ارفع ملفك</div>
            </div>

            <div class="step-divider-arrow">←</div>

            <div class="step-item">
              <span class="step-num">3</span>
              <div class="step-round-circle">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>
              </div>
              <div class="step-label">اختر الأداة المناسبة<br/>وابدأ التحليل</div>
            </div>

            <div class="step-divider-arrow">←</div>

            <div class="step-item">
              <span class="step-num">1</span>
              <div class="step-round-circle">
                <svg class="icon-svg" viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
              </div>
              <div class="step-label">استلم النتائج<br/>وقم بتصديرها</div>
            </div>

          </div>
        </div>
        <div class="how-quote">
          خطوات بسيطة ... ونتيجة احترافية
        </div>
      </div>

      <!-- Center: Packages / Latest Posts (425px) -->
      <div class="card-packages">
        <h3 class="packages-header-title">باقات الاشتراك</h3>
        <div class="packages-cards-grid">
          
          <!-- Free -->
          <div class="tier-box">
            <div>
              <h4 class="tier-title">مجاني</h4>
              <div class="tier-cost"><strong>0</strong> جنيه / شهر</div>
              <ul class="tier-perks">
                <li>3 عمليات يوميًا</li>
                <li>تلخيص 3 مصادر</li>
                <li>أدوات صياغة محدودة</li>
              </ul>
            </div>
            <a href="#" class="tier-action-btn tier-btn-outline">ابدأ الآن</a>
          </div>

          <!-- Researcher (Highlighted) -->
          <div class="tier-box popular">
            <span class="tier-popular-tag">الأكثر اختياراً</span>
            <div>
              <h4 class="tier-title">باحث</h4>
              <div class="tier-cost"><strong>99</strong> جنيه / شهر</div>
              <ul class="tier-perks">
                <li>استخدام أكبر للأدوات</li>
                <li>رفع الملفات وتحليلها</li>
                <li>إنشاء الحواشي والمراجع</li>
                <li>تصدير Word</li>
              </ul>
            </div>
            <a href="#" class="tier-action-btn tier-btn-fill">اشترك الآن</a>
          </div>

          <!-- Plus -->
          <div class="tier-box">
            <div>
              <h4 class="tier-title">باحث+</h4>
              <div class="tier-cost"><strong>249</strong> جنيه / شهر</div>
              <ul class="tier-perks">
                <li>استخدام غير محدود</li>
                <li>تحليل ملفات كبيرة</li>
                <li>تحليل الدراسات السابقة</li>
                <li>تحليل الاستبيانات</li>
                <li>أدوات متقدمة</li>
                <li>أولوية في المعالجة</li>
              </ul>
            </div>
            <a href="#" class="tier-action-btn tier-btn-fill">اشترك الآن</a>
          </div>

        </div>
      </div>

      <!-- Right: Researcher Services (315px) -->
      <div class="card-services" id="services">
        <div>
          <div class="services-top-header">
            <svg class="icon-svg" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
            <span>خدمات الباحث</span>
          </div>
          <p class="services-short-desc">يمكنك طلب خدمات احترافية من فريق أبحاثنا المتخصص:</p>
          <ul class="services-items-list">
            <li>تنسيق رسالة ماجستير</li>
            <li>تدقيق لغوي</li>
            <li>تحليل إحصائي</li>
            <li>تفريغ مقابلات</li>
            <li>تنسيق مراجع</li>
          </ul>
          <div class="services-contact-bubble">
            للاتفاق على أي عمل فيما يخص الأبحاث العلمية يرجى الاتصال على: <a href="tel:01015034659">01015034659</a>
          </div>
        </div>
        <div class="services-actions-group">
          <a href="tel:01015034659" class="services-call-btn">
            <span>اطلب خدمة الآن</span>
            <span>←</span>
          </a>
          <a href="https://wa.me/201015034659" target="_blank" class="services-wa-icon-btn" title="تواصل عبر واتساب">
            <svg class="icon-svg-sm" viewBox="0 0 24 24" fill="currentColor"><path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946.003-6.556 5.338-11.891 11.893-11.891 3.181.001 6.167 1.24 8.413 3.488 2.245 2.248 3.481 5.236 3.48 8.414-.003 6.557-5.338 11.892-11.893 11.892-1.99-.001-3.951-.5-5.688-1.448l-6.305 1.654zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"/></svg>
          </a>
        </div>
      </div>

    </div>
  </section>

  <!-- 6. FOOTER (70px) -->
  <footer class="site-footer">
    <div class="footer-container">
      
      <!-- Right: Logo -->
      <div class="footer-right-brand">
        <a href="/">
          <img class="footer-logo-image" src="{footer_logo}" alt="مرصاد" />
        </a>
      </div>

      <!-- Center: Links -->
      <nav class="footer-center-nav">
        <a href="#" class="footer-link">الرئيسية</a>
        <a href="#tools" class="footer-link">الأدوات</a>
        <a href="#services" class="footer-link">خدمات الأبحاث</a>
        <a href="#articles" class="footer-link">المقالات</a>
        <a href="#about" class="footer-link">من نحن</a>
        <a href="#contact" class="footer-link">تواصل معنا</a>
      </nav>

      <!-- Left: Social & Rights -->
      <div class="footer-left-social">
        <div class="social-icons-row">
          <a href="#" class="social-link" title="YouTube"><svg class="icon-svg" viewBox="0 0 24 24"><path d="M23.498 6.186a3.016 3.016 0 00-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 00.502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 002.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 002.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg></a>
          <a href="#" class="social-link" title="X"><svg class="icon-svg" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
          <a href="#" class="social-link" title="Facebook"><svg class="icon-svg" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg></a>
          <a href="#" class="social-link" title="LinkedIn"><svg class="icon-svg" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
        </div>
        <div class="copyright-text">© مرصاد. جميع الحقوق محفوظة.</div>
      </div>

    </div>
  </footer>

</div>

</body>
</html>
"""

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Updated preview.html successfully written!')
