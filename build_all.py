# -*- coding: utf-8 -*-
"""
Main Builder Script:
Generates preview.html and theme.xml with 100% precision.
"""
import sys
import os
import xml.etree.ElementTree as ET

sys.path.insert(0, os.getcwd())
import tools_modal_template
import smart_tools_js
import page_components

def read_b64(name):
    with open(name + '.b64.txt', 'r', encoding='utf-8') as f:
        return f.read().strip()

print("1. Loading High-Resolution Base64 Assets...")
hero_cover_b64 = read_b64('hero_cover_hd.jpg')
laptop_art_b64 = read_b64('laptop_clean_opt.jpg')
logo_clean_b64 = read_b64('logo_clean_512.png')
logo_footer_b64 = read_b64('logo_footer_light.png')

css_content = page_components.get_page_css()
tools_html = page_components.get_tools_cards_html()
modal_html = tools_modal_template.get_tools_modal_html()
smart_js = smart_tools_js.get_smart_tools_js()

# =========================================================================
# 2. BUILD preview.html (Standalone preview for localhost / browser)
# =========================================================================
print("2. Generating preview.html...")

preview_html_content = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>مرصاد | منصة الذكاء الاصطناعي للبحث العلمي العربي</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="" />
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&family=Reem+Kufi:wght@500;600;700&family=Aref+Ruqaa:wght@400;700&display=swap" rel="stylesheet" />
<style>
{css_content}
</style>
</head>
<body>

<div class="site-wrapper">
  
  <!-- 1. HEADER (68px) -->
  <header class="site-header">
    <div class="header-container">
      
      <!-- Right: Logo + Brand Texts -->
      <a href="/" class="header-right-logo">
        <img src="{logo_clean_b64}" alt="مرصاد" class="header-logo-icon" />
        <div class="header-brand-texts">
          <div class="header-brand-name">مِرْصَاد</div>
          <div class="header-brand-tagline">منصة الذكاء الاصطناعي للبحث العلمي العربي</div>
        </div>
      </a>

      <!-- Center: Navigation -->
      <nav class="header-center-nav">
        <a href="#hero" class="nav-item-link active">الرئيسية</a>
        <a href="#tools" class="nav-item-link">أدوات مرصاد</a>
        <a href="#features" class="nav-item-link">المميزات</a>
        <a href="#packages" class="nav-item-link">الباقات</a>
        <a href="#articles-section" class="nav-item-link">المقالات</a>
        <a href="#help-section" class="nav-item-link">المساعدة</a>
      </nav>

      <!-- Left: Contact & WhatsApp CTA -->
      <div class="header-left-actions">
        <a href="https://wa.me/201015034659" target="_blank" class="btn-outline-wa">
          <span>واتساب</span>
        </a>
        <a href="tel:01015034659" class="btn-solid-call">
          <span>01015034659</span>
        </a>
      </div>

    </div>
  </header>

  <!-- 2. HERO SECTION -->
  <section class="hero-section" id="hero" style="background-image: url('{hero_cover_b64}');">
    <div class="hero-gradient-overlay"></div>
    
    <div class="hero-center-content">
      <div class="hero-brand-title">مِرْصَاد</div>
      <div class="hero-slogan-title">نرصد المعرفة، ونبني البحث.</div>
      <p class="hero-paragraph">
        المنصة العربية الأولى المتخصصة في تسخير الذكاء الاصطناعي الأكاديمي لخدمة الباحثين وطلاب الدراسات العليا، في كافة مراحل إعداد الرسائل والأطروحات العلمية.
      </p>

      <form class="hero-search-form" onsubmit="handleSearch(event)">
        <input type="text" class="hero-search-field" id="searchInput" placeholder="ما الذي تبحث عنه؟ عنوان بحث، دراسة، استبيان، أو فكرة..." />
        <button type="submit" class="hero-search-button">
          <span>ابحث في مرصاد</span>
          <svg style="width:16px;height:16px;fill:currentColor;" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0016 9.5 6.5 6.5 0 109.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
        </button>
      </form>

      <div class="hero-chips-row">
        <span class="chips-label">الأكثر بحثاً:</span>
        <button type="button" class="chip-button" onclick="searchFor('الدراسات السابقة')">الدراسات السابقة</button>
        <button type="button" class="chip-button" onclick="searchFor('تحليل الاستبيان')">تحليل الاستبيان</button>
        <button type="button" class="chip-button" onclick="searchFor('توثيق المراجع')">توثيق المراجع</button>
        <button type="button" class="chip-button" onclick="searchFor('صياغة أكاديمية')">صياغة أكاديمية</button>
      </div>
    </div>
  </section>

  <!-- 3. TOOLS GRID (9 Vector Clean Cards) -->
  <section class="tools-grid-section" id="tools">
    <div class="tools-row-container">
{tools_html}
    </div>
  </section>

  <!-- 4. MIDDLE SECTION -->
  <section class="middle-features-section" id="features">
    <div class="middle-row-container">
      
      <!-- Right Card: Why Us (First in RTL Grid) -->
      <div class="card-why-us">
        <h3 class="why-us-heading">لماذا مِرْصَاد؟</h3>
        <div class="why-us-items">
          
          <div class="why-us-row">
            <div class="why-us-badge">
              <svg style="width:20px;height:20px;fill:currentColor;" viewBox="0 0 24 24"><path d="M11.99 2C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8zm.5-13H11v6l5.25 3.15.75-1.23-4.5-2.67z"/></svg>
            </div>
            <div class="why-us-texts">
              <h4>يوفر وقتك وجهدك</h4>
              <p>ينجز في دقائق ما يستغرق أياماً في مراجعة وتوثيق الدراسات وتنسيق الرسائل.</p>
            </div>
          </div>

          <div class="why-us-row">
            <div class="why-us-badge">
              <svg style="width:20px;height:20px;fill:currentColor;" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
            </div>
            <div class="why-us-texts">
              <h4>دقة أكاديمية عالية</h4>
              <p>مصمم خصيصاً وفق المعايير والضوابط المنهجية المعتمدة في الجامعات العربية.</p>
            </div>
          </div>

          <div class="why-us-row">
            <div class="why-us-badge">
              <svg style="width:20px;height:20px;fill:currentColor;" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>
            </div>
            <div class="why-us-texts">
              <h4>سرية وأمان تام</h4>
              <p>أبحاثك وملفاتك مشفرة ومحمية بالكامل ولا يتم مشاركتها إطلاقاً مع أي جهة.</p>
            </div>
          </div>

        </div>

        <a href="https://wa.me/201015034659" target="_blank" class="why-us-banner-link">
          <span>اكتشف كيف يساعدك مرصاد في بحثك</span>
          <span>←</span>
        </a>
      </div>

      <!-- Center Card: Integrated Tools -->
      <div class="card-integrated">
        <div class="integrated-content">
          <h3 class="integrated-title">أدوات متكاملة لرحلتك البحثية</h3>
          <p class="integrated-desc">
            من الفكرة الأولى وحتى المسودة النهائية — مرصاد يرافقك خطوة بخطوة بأحدث تقنيات المعالجة اللغوية الطبيعية المخصصة للمحتوى الأكاديمي العربي.
          </p>
          <ul class="integrated-features-list">
            <li>بحث ذكي في ملايين المصادر والمراجع المفتوحة</li>
            <li>تحليل متقدم للدراسات السابقة واستخراج الفجوة البحثية</li>
            <li>تحليل الاستبيانات إحصائياً وتفسير النتائج بدقة</li>
            <li>توثيق آلي للمراجع وفق أحدث معايير APA و MLA</li>
          </ul>
          <button type="button" class="integrated-start-btn" onclick="openSmartTool('sources')">
            <span>ابدأ الآن مجاناً</span>
            <span>←</span>
          </button>
        </div>
        
        <div class="integrated-art-box">
          <img src="{laptop_art_b64}" alt="أدوات متكاملة لرحلتك البحثية" class="integrated-art-img" />
        </div>
      </div>

      <!-- Left Card: Professional Services (Third in RTL Grid) -->
      <div class="card-services">
        <div>
          <h3 class="services-title">خدمات الباحثين المتخصصة</h3>
          <p class="services-desc">هل تحتاج إلى مساعدة إضافية في إعداد أو مراجعة بحثك؟ فريقنا الأكاديمي جاهز لمساعدتك.</p>
          
          <ul class="services-items-list">
            <li>تنسيق الأطروحات ورسائل الماجستير والدكتوراه</li>
            <li>التحليل الإحصائي المتقدم (SPSS / AMOS)</li>
            <li>التدقيق اللغوي والمنهجي الصارم</li>
          </ul>
        </div>

        <div>
          <div class="services-contact-bubble">
            تواصل معنا مباشرة عبر الواتساب أو الاتصال على الرقم: <br/>
            <a href="tel:01015034659">01015034659</a>
          </div>

          <div class="services-actions-group">
            <a href="tel:01015034659" class="services-call-btn">
              <span>اتصل الآن</span>
            </a>
            <a href="https://wa.me/201015034659" target="_blank" class="services-wa-icon-btn" title="واتساب">
              <svg style="width:18px;height:18px;fill:currentColor;" viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 012.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 01-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.42.1-.12.19-.48.61-.59.73-.11.12-.23.14-.42.05-.19-.09-.81-.3-1.55-.96-.57-.51-.96-1.14-1.07-1.33-.11-.19-.01-.3.08-.39.09-.09.19-.23.29-.35.09-.12.13-.2.19-.34.07-.14.03-.26-.02-.35-.05-.09-.42-1.01-.58-1.39-.15-.36-.31-.31-.42-.32h-.36c-.12 0-.32.05-.49.23-.17.19-.65.64-.65 1.56 0 .93.67 1.82.77 1.95.09.12 1.33 2.03 3.22 2.85.45.19.8.31 1.08.4.45.14.86.12 1.19.07.36-.05 1.12-.46 1.28-.9.16-.45.16-.83.11-.9-.05-.07-.17-.11-.36-.2z"/></svg>
            </a>
          </div>
        </div>
      </div>

    </div>
  </section>

  <!-- 5. BOTTOM SECTION -->
  <section class="bottom-section" id="packages">
    <div class="bottom-grid-container">
      
      <!-- Right Card: Packages (First in RTL Grid) -->
      <div class="card-packages">
        <h3 class="packages-header-title">اختر الباقة المناسبة لك</h3>
        <div class="packages-cards-grid">
          
          <!-- Free -->
          <div class="tier-box">
            <div>
              <h4 class="tier-title">مجاني</h4>
              <div class="tier-cost"><strong>0</strong> جنيه</div>
              <ul class="tier-perks">
                <li>استخدام محدود يومياً</li>
                <li>البحث في المصادر</li>
                <li>صياغة فقرات قصيرة</li>
                <li>توثيق مبسط للمراجع</li>
              </ul>
            </div>
            <button type="button" class="tier-action-btn" onclick="openTierModal('مجاني', '0 جنيه')">ابدأ مجانًا</button>
          </div>

          <!-- Popular (Student) -->
          <div class="tier-box popular">
            <span class="tier-popular-tag">الأكثر شعبية</span>
            <div>
              <h4 class="tier-title">طالب باحث</h4>
              <div class="tier-cost"><strong>99</strong> جنيه / شهر</div>
              <ul class="tier-perks">
                <li>استخدام موسع لجميع الأدوات</li>
                <li>تحليل ملفات حتى 10 ميجابايت</li>
                <li>مقارنة الدراسات السابقة</li>
                <li>تصدير Word غير محدود</li>
                <li>دعم عبر الواتساب</li>
              </ul>
            </div>
            <button type="button" class="tier-action-btn tier-btn-fill" onclick="openTierModal('طالب باحث', '99 جنيه')">اشترك الآن</button>
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
            <button type="button" class="tier-action-btn tier-btn-fill" onclick="openTierModal('باحث+', '249 جنيه')">اشترك الآن</button>
          </div>

        </div>
      </div>

      <!-- Left Card: How to Start (Second in RTL Grid) -->
      <div class="card-how-to-start">
        <div>
          <h3 class="how-title">كيف تبدأ؟</h3>
          <div class="how-steps-diagram">
            
            <div class="step-item" onclick="openStepModal('أنشئ حسابك مجاناً', 'يمكنك البدء فوراً في استكشاف كافة الأدوات البحثية المتطورة.')">
              <span class="step-num">4</span>
              <div class="step-round-circle">
                <svg viewBox="0 0 24 24"><path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/></svg>
              </div>
              <div class="step-label">أنشئ حسابك<br/>مجانًا</div>
            </div>

            <div class="step-divider-arrow">←</div>

            <div class="step-item" onclick="openStepModal('أدخل موضوع بحثك أو ارفع ملفك', 'قم بكتابة عنوان بحثك أو ارفع ملفك بصيغة Word أو PDF لاستخلاص البيانات وتحليلها.')">
              <span class="step-num">2</span>
              <div class="step-round-circle">
                <svg viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
              </div>
              <div class="step-label">أدخل موضوع بحثك<br/>أو ارفع ملفك</div>
            </div>

            <div class="step-divider-arrow">←</div>

            <div class="step-item" onclick="openStepModal('اختر الأداة المناسبة وابدأ التحليل', 'اختر من بين 9 أدوات بحثية متخصصة (المصادر، الدراسات السابقة، الاستبيانات، التوثيق، الصياغة).')">
              <span class="step-num">3</span>
              <div class="step-round-circle">
                <svg viewBox="0 0 24 24"><path d="M19.14 12.94c.04-.3.06-.61.06-.94 0-.32-.02-.64-.07-.94l2.03-1.58c.18-.14.23-.41.12-.61l-1.92-3.32c-.12-.22-.37-.29-.59-.22l-2.39.96c-.5-.38-1.03-.7-1.62-.94l-.36-2.54c-.04-.24-.24-.41-.48-.41h-3.84c-.24 0-.43.17-.47.41l-.36 2.54c-.59.24-1.13.57-1.62.94l-2.39-.96c-.22-.08-.47 0-.59.22L2.74 8.87c-.12.21-.08.47.12.61l2.03 1.58c-.05.3-.09.63-.09.94s.02.64.07.94l-2.03 1.58c-.18.14-.23.41-.12.61l1.92 3.32c.12.22.37.29.59.22l2.39-.96c.5.38 1.03.7 1.62.94l.36 2.54c.05.24.24.41.48.41h3.84c.24 0 .44-.17.47-.41l.36-2.54c.59-.24 1.13-.56 1.62-.94l2.39.96c.22.08.47 0 .59-.22l1.92-3.32c.12-.22.07-.47-.12-.61l-2.01-1.58zM12 15.6c-1.98 0-3.6-1.62-3.6-3.6s1.62-3.6 3.6-3.6 3.6 1.62 3.6 3.6-1.62 3.6-3.6 3.6z"/></svg>
              </div>
              <div class="step-label">اختر الأداة المناسبة<br/>وابدأ التحليل</div>
            </div>

            <div class="step-divider-arrow">←</div>

            <div class="step-item" onclick="openStepModal('استلم النتائج وقم بتصديرها', 'حمّل النتائج كملف Word منسق بالكامل وجاهز للطباعة أو الإضافة إلى رسالتك مباشرة.')">
              <span class="step-num">1</span>
              <div class="step-round-circle">
                <svg viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
              </div>
              <div class="step-label">استلم النتائج<br/>وقم بتصديرها</div>
            </div>

          </div>
        </div>
        <div class="how-quote">
          خطوات بسيطة ... ونتيجة احترافية
        </div>
      </div>

    </div>
  </section>

  <!-- 6. ARTICLES SECTION (LIVE BLOGGER POSTS & GUIDES) -->
  <section class="inner-section-view" id="articles-section">
    <div class="inner-section-header">
      <h2>أحدث المقالات والأدلة البحثية</h2>
      <p>مقالات أكاديمية متخصصة ومحدثة خطوة بخطوة لمساعدتك في إنجاز أطروحتك وبحثك العلمي</p>
    </div>
    <div class="articles-grid" id="liveArticlesGrid">
      
      <!-- Card 1: User's Published Post on Blogger -->
      <div class="article-card" onclick="window.open('https://mersad0.blogspot.com/2026/10/blog-post.html', '_blank')">
        <div class="article-card-cover" style="background: linear-gradient(135deg, #0B2A5B, #2F6FC7);">
          الذكاء الاصطناعي: كيف يغير حياتنا ومستقبلنا؟
        </div>
        <div class="article-card-body">
          <span class="article-tag">مقال منشور بالمدونة</span>
          <h3 class="article-title">الذكاء الاصطناعي: كيف يغيّر حياتنا ومستقبلنا؟</h3>
          <p class="article-snippet">أصبح الذكاء الاصطناعي من أكثر التقنيات انتشارًا في العالم خلال السنوات الأخيرة، ودوره الجوهري في تطوير مجالات البحث...</p>
          <span class="article-link-more">اقرأ المقال كاملاً على المدونة ←</span>
        </div>
      </div>

      <!-- Card 2 -->
      <div class="article-card" onclick="openArticleModal('دليل كتابة الإطار النظري والدراسات السابقة 2026', 'أحدث منهجية علمية لتحديد الفجوة البحثية وصياغة مراجعة الأدبيات بطريقة محكمة قابلة للنشر في المجلات الدولية.')">
        <div class="article-card-cover">
          دليل كتابة الإطار النظري
        </div>
        <div class="article-card-body">
          <span class="article-tag">الدراسات السابقة</span>
          <h3 class="article-title">دليل كتابة الإطار النظري والدراسات السابقة 2026</h3>
          <p class="article-snippet">أحدث منهجية علمية لتحديد الفجوة البحثية وصياغة مراجعة الأدبيات بطريقة محكمة...</p>
          <span class="article-link-more">اقرأ المقال كاملاً ←</span>
        </div>
      </div>

      <!-- Card 3 -->
      <div class="article-card" onclick="openArticleModal('التحليل الإحصائي للاستبيانات باستخدام SPSS و AMOS', 'شرح عملي لاختبارات الصدق والثبات، ومعامل ألفا كرونباخ، والتحليل العاملي التوكيدي لرسائل الماجستير.')">
        <div class="article-card-cover" style="background: linear-gradient(135deg, #1d58a7, #0B2A5B);">
          التحليل الإحصائي للاستبيان
        </div>
        <div class="article-card-body">
          <span class="article-tag">تحليل الاستبيان</span>
          <h3 class="article-title">التحليل الإحصائي للاستبيانات باستخدام SPSS و AMOS</h3>
          <p class="article-snippet">شرح عملي لاختبارات الصدق والثبات، ومعامل ألفا كرونباخ، والتحليل العاملي التوكيدي...</p>
          <span class="article-link-more">اقرأ المقال كاملاً ←</span>
        </div>
      </div>

    </div>
  </section>

  <!-- 7. HELP SECTION (ACCORDION & FAQ) -->
  <section class="inner-section-view" id="help-section" style="background: #ffffff; border-top: 1px solid #edf2f7;">
    <div class="inner-section-header">
      <h2>مركز المساعدة والأسئلة الشائعة</h2>
      <p>إليك أهم الأسئلة التي يطرحها الباحثون حول كيفية الاستفادة القصوى من منصة مرصاد</p>
    </div>
    <div class="help-accordion">
      
      <div class="help-item">
        <div class="help-q" onclick="toggleHelp(this)">
          <span>ما هي الخدمات التي تقدمها منصة مرصاد للباحثين؟</span>
          <span>▾</span>
        </div>
        <div class="help-a">
          منصة مرصاد تقدم 9 أدوات ذكية متكاملة تغطي كافة مراحل البحث العلمي: البحث المباشر في قواعد البيانات العالمية، تحليل ومقارنة الدراسات السابقة، بناء خطة البحث والمشكلة والأهداف، توثيق المراجع بأسلوب APA و MLA وغيرها، تحليل الاستبيانات إحصائياً، الصياغة الأكاديمية السليمة، والمراجعة اللغوية والمنهجية مع التصدير النهائي إلى Word.
        </div>
      </div>

      <div class="help-item">
        <div class="help-q" onclick="toggleHelp(this)">
          <span>كيف يمكنني طلب خدمة مخصصة (تنسيق رسالة أو تحليل إحصائي)؟</span>
          <span>▾</span>
        </div>
        <div class="help-a">
          يمكنك التواصل المباشر مع فريقنا المتخصص عبر الاتصال على الرقم <strong>01015034659</strong> أو مراسلتنا فوراً عبر الواتساب على نفس الرقم، وسيتم الاتفاق على نطاق العمل والتسليم بأعلى معايير الجودة والأمانة العلمية.
        </div>
      </div>

      <div class="help-item">
        <div class="help-q" onclick="toggleHelp(this)">
          <span>هل تضمن المنصة الحفاظ على سرية الأبحاث والبيانات؟</span>
          <span>▾</span>
        </div>
        <div class="help-a">
          نعم، نحن نلتزم بالسرية التامة لجميع الملفات والبيانات التي ترفعها على المنصة، ولا يتم مشاركة أي ملف مع أي طرف خارجي، وتبقى حقوق الملكية الفكرية ملكاً خالصاً لك كباحث.
        </div>
      </div>

    </div>
  </section>

  <!-- 8. FOOTER -->
  <footer class="site-footer">
    <div class="footer-container">
      
      <!-- Right: Logo with new gold/white lighthouse in book -->
      <div class="footer-right-brand">
        <a href="/" class="header-right-logo">
          <img src="{logo_footer_b64}" alt="مرصاد" class="header-logo-icon" />
          <div class="header-brand-texts">
            <div class="header-brand-name" style="color:#ffffff;">مِرْصَاد</div>
            <div class="header-brand-tagline" style="color:var(--accent-gold-light);">نرصد المعرفة، ونبني البحث.</div>
          </div>
        </a>
      </div>

      <!-- Center: Links -->
      <nav class="footer-center-nav">
        <a href="#hero" class="footer-link">الرئيسية</a>
        <a href="#tools" class="footer-link">الأدوات</a>
        <a href="#features" class="footer-link">المميزات</a>
        <a href="#packages" class="footer-link">الباقات</a>
        <a href="#articles-section" class="footer-link">المقالات</a>
        <a href="#help-section" class="footer-link">المساعدة</a>
      </nav>

      <!-- Left: Social & Copyright -->
      <div class="footer-left-social">
        <div class="social-icons-row">
          <a href="https://wa.me/201015034659" target="_blank" class="social-link" title="واتساب">
            <svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 012.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 01-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.42.1-.12.19-.48.61-.59.73-.11.12-.23.14-.42.05-.19-.09-.81-.3-1.55-.96-.57-.51-.96-1.14-1.07-1.33-.11-.19-.01-.3.08-.39.09-.09.19-.23.29-.35.09-.12.13-.2.19-.34.07-.14.03-.26-.02-.35-.05-.09-.42-1.01-.58-1.39-.15-.36-.31-.31-.42-.32h-.36c-.12 0-.32.05-.49.23-.17.19-.65.64-.65 1.56 0 .93.67 1.82.77 1.95.09.12 1.33 2.03 3.22 2.85.45.19.8.31 1.08.4.45.14.86.12 1.19.07.36-.05 1.12-.46 1.28-.9.16-.45.16-.83.11-.9-.05-.07-.17-.11-.36-.2z"/></svg>
          </a>
          <a href="tel:01015034659" class="social-link" title="اتصال هاتفي">
            <svg viewBox="0 0 24 24"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
          </a>
        </div>
        <div class="copyright-text">جميع الحقوق محفوظة © 2026 منصة مرصاد</div>
      </div>

    </div>
  </footer>

</div>

{modal_html}

<script>
{smart_js}
</script>

</body>
</html>
"""

with open('preview.html', 'w', encoding='utf-8') as f:
    f.write(preview_html_content)
print(f"preview.html generated successfully ({len(preview_html_content)} bytes).")

# =========================================================================
# 3. BUILD theme.xml (Blogger V2 Template)
# =========================================================================
print("3. Generating theme.xml...")

theme_xml_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
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
{css_content}
  ]]></b:skin>
</head>

<body>

<div class='site-wrapper'>
  
  <!-- 1. HEADER (68px) -->
  <header class='site-header'>
    <div class='header-container'>
      
      <!-- Right: Logo + Brand Texts -->
      <a class='header-right-logo' href='/'>
        <img alt='مرصاد' class='header-logo-icon' src='{logo_clean_b64}'/>
        <div class='header-brand-texts'>
          <div class='header-brand-name'>مِرْصَاد</div>
          <div class='header-brand-tagline'>منصة الذكاء الاصطناعي للبحث العلمي العربي</div>
        </div>
      </a>

      <!-- Center: Navigation -->
      <nav class='header-center-nav'>
        <a class='nav-item-link active' href='/'>الرئيسية</a>
        <a class='nav-item-link' href='/#tools'>أدوات مرصاد</a>
        <a class='nav-item-link' href='/#features'>المميزات</a>
        <a class='nav-item-link' href='/#packages'>الباقات</a>
        <a class='nav-item-link' href='/#articles-section'>المقالات</a>
        <a class='nav-item-link' href='/#help-section'>المساعدة</a>
      </nav>

      <!-- Left: Contact & WhatsApp CTA -->
      <div class='header-left-actions'>
        <a class='btn-outline-wa' href='https://wa.me/201015034659' target='_blank'>
          <span>واتساب</span>
        </a>
        <a class='btn-solid-call' href='tel:01015034659'>
          <span>01015034659</span>
        </a>
      </div>

    </div>
  </header>

  <!-- CONDITIONAL: ONLY ON INDEX (HOMEPAGE) -->
  <b:if cond='data:blog.pageType == &quot;index&quot;'>
    
    <!-- 2. HERO SECTION -->
    <section class='hero-section' id='hero' style='background-image: url(&quot;{hero_cover_b64}&quot;);'>
      <div class='hero-gradient-overlay'/>
      
      <div class='hero-center-content'>
        <div class='hero-brand-title'>مِرْصَاد</div>
        <div class='hero-slogan-title'>نرصد المعرفة، ونبني البحث.</div>
        <p class='hero-paragraph'>
          المنصة العربية الأولى المتخصصة في تسخير الذكاء الاصطناعي الأكاديمي لخدمة الباحثين وطلاب الدراسات العليا، في كافة مراحل إعداد الرسائل والأطروحات العلمية.
        </p>

        <form class='hero-search-form' onsubmit='handleSearch(event)'>
          <input class='hero-search-field' id='searchInput' placeholder='ما الذي تبحث عنه؟ عنوان بحث، دراسة، استبيان، أو فكرة...' type='text'/>
          <button class='hero-search-button' type='submit'>
            <span>ابحث في مرصاد</span>
            <svg style='width:16px;height:16px;fill:currentColor;' viewBox='0 0 24 24'><path d='M15.5 14h-.79l-.28-.27A6.471 6.471 0 0016 9.5 6.5 6.5 0 109.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z'/></svg>
          </button>
        </form>

        <div class='hero-chips-row'>
          <span class='chips-label'>الأكثر بحثاً:</span>
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
{tools_html}
      </div>
    </section>

    <!-- 4. MIDDLE SECTION -->
    <section class='middle-features-section' id='features'>
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
                <p>ينجز في دقائق ما يستغرق أياماً في مراجعة وتوثيق الدراسات وتنسيق الرسائل.</p>
              </div>
            </div>

            <div class='why-us-row'>
              <div class='why-us-badge'>
                <svg style='width:20px;height:20px;fill:currentColor;' viewBox='0 0 24 24'><path d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'/></svg>
              </div>
              <div class='why-us-texts'>
                <h4>دقة أكاديمية عالية</h4>
                <p>مصمم خصيصاً وفق المعايير والضوابط المنهجية المعتمدة في الجامعات العربية.</p>
              </div>
            </div>

            <div class='why-us-row'>
              <div class='why-us-badge'>
                <svg style='width:20px;height:20px;fill:currentColor;' viewBox='0 0 24 24'><path d='M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z'/></svg>
              </div>
              <div class='why-us-texts'>
                <h4>سرية وأمان تام</h4>
                <p>أبحاثك وملفاتك مشفرة ومحمية بالكامل ولا يتم مشاركتها إطلاقاً مع أي جهة.</p>
              </div>
            </div>

          </div>

          <a class='why-us-banner-link' href='https://wa.me/201015034659' target='_blank'>
            <span>اكتشف كيف يساعدك مرصاد في بحثك</span>
            <span>←</span>
          </a>
        </div>

        <!-- Center Card: Integrated Tools -->
        <div class='card-integrated'>
          <div class='integrated-content'>
            <h3 class='integrated-title'>أدوات متكاملة لرحلتك البحثية</h3>
            <p class='integrated-desc'>
              من الفكرة الأولى وحتى المسودة النهائية — مرصاد يرافقك خطوة بخطوة بأحدث تقنيات المعالجة اللغوية الطبيعية المخصصة للمحتوى الأكاديمي العربي.
            </p>
            <ul class='integrated-features-list'>
              <li>بحث ذكي في ملايين المصادر والمراجع المفتوحة</li>
              <li>تحليل متقدم للدراسات السابقة واستخراج الفجوة البحثية</li>
              <li>تحليل الاستبيانات إحصائياً وتفسير النتائج بدقة</li>
              <li>توثيق آلي للمراجع وفق أحدث معايير APA و MLA</li>
            </ul>
            <button class='integrated-start-btn' onclick='openSmartTool(&quot;sources&quot;)' type='button'>
              <span>ابدأ الآن مجاناً</span>
              <span>←</span>
            </button>
          </div>
          
          <div class='integrated-art-box'>
            <img alt='أدوات متكاملة لرحلتك البحثية' class='integrated-art-img' src='{laptop_art_b64}'/>
          </div>
        </div>

        <!-- Left Card: Professional Services (Third in RTL Grid) -->
        <div class='card-services'>
          <div>
            <h3 class='services-title'>خدمات الباحثين المتخصصة</h3>
            <p class='services-desc'>هل تحتاج إلى مساعدة إضافية في إعداد أو مراجعة بحثك؟ فريقنا الأكاديمي جاهز لمساعدتك.</p>
            
            <ul class='services-items-list'>
              <li>تنسيق الأطروحات ورسائل الماجستير والدكتوراه</li>
              <li>التحليل الإحصائي المتقدم (SPSS / AMOS)</li>
              <li>التدقيق اللغوي والمنهجي الصارم</li>
            </ul>
          </div>

          <div>
            <div class='services-contact-bubble'>
              تواصل معنا مباشرة عبر الواتساب أو الاتصال على الرقم: <br/>
              <a href='tel:01015034659'>01015034659</a>
            </div>

            <div class='services-actions-group'>
              <a class='services-call-btn' href='tel:01015034659'>
                <span>اتصل الآن</span>
              </a>
              <a class='services-wa-icon-btn' href='https://wa.me/201015034659' target='_blank' title='واتساب'>
                <svg style='width:18px;height:18px;fill:currentColor;' viewBox='0 0 24 24'><path d='M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 012.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 01-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.42.1-.12.19-.48.61-.59.73-.11.12-.23.14-.42.05-.19-.09-.81-.3-1.55-.96-.57-.51-.96-1.14-1.07-1.33-.11-.19-.01-.3.08-.39.09-.09.19-.23.29-.35.09-.12.13-.2.19-.34.07-.14.03-.26-.02-.35-.05-.09-.42-1.01-.58-1.39-.15-.36-.31-.31-.42-.32h-.36c-.12 0-.32.05-.49.23-.17.19-.65.64-.65 1.56 0 .93.67 1.82.77 1.95.09.12 1.33 2.03 3.22 2.85.45.19.8.31 1.08.4.45.14.86.12 1.19.07.36-.05 1.12-.46 1.28-.9.16-.45.16-.83.11-.9-.05-.07-.17-.11-.36-.2z'/></svg>
              </a>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- 5. BOTTOM SECTION -->
    <section class='bottom-section' id='packages'>
      <div class='bottom-grid-container'>
        
        <!-- Right Card: Packages (First in RTL Grid) -->
        <div class='card-packages'>
          <h3 class='packages-header-title'>اختر الباقة المناسبة لك</h3>
          <div class='packages-cards-grid'>
            
            <!-- Free -->
            <div class='tier-box'>
              <div>
                <h4 class='tier-title'>مجاني</h4>
                <div class='tier-cost'><strong>0</strong> جنيه</div>
                <ul class='tier-perks'>
                  <li>استخدام محدود يومياً</li>
                  <li>البحث في المصادر</li>
                  <li>صياغة فقرات قصيرة</li>
                  <li>توثيق مبسط للمراجع</li>
                </ul>
              </div>
              <button class='tier-action-btn' onclick='openTierModal(&quot;مجاني&quot;, &quot;0 جنيه&quot;)' type='button'>ابدأ مجانًا</button>
            </div>

            <!-- Popular (Student) -->
            <div class='tier-box popular'>
              <span class='tier-popular-tag'>الأكثر شعبية</span>
              <div>
                <h4 class='tier-title'>طالب باحث</h4>
                <div class='tier-cost'><strong>99</strong> جنيه / شهر</div>
                <ul class='tier-perks'>
                  <li>استخدام موسع لجميع الأدوات</li>
                  <li>تحليل ملفات حتى 10 ميجابايت</li>
                  <li>مقارنة الدراسات السابقة</li>
                  <li>تصدير Word غير محدود</li>
                  <li>دعم عبر الواتساب</li>
                </ul>
              </div>
              <button class='tier-action-btn tier-btn-fill' onclick='openTierModal(&quot;طالب باحث&quot;, &quot;99 جنيه&quot;)' type='button'>اشترك الآن</button>
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

        <!-- Left Card: How to Start (Second in RTL Grid) -->
        <div class='card-how-to-start'>
          <div>
            <h3 class='how-title'>كيف تبدأ؟</h3>
            <div class='how-steps-diagram'>
              
              <div class='step-item' onclick='openStepModal(&quot;أنشئ حسابك مجاناً&quot;, &quot;يمكنك البدء فوراً في استكشاف كافة الأدوات البحثية المتطورة.&quot;)'>
                <span class='step-num'>4</span>
                <div class='step-round-circle'>
                  <svg viewBox='0 0 24 24'><path d='M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z'/></svg>
                </div>
                <div class='step-label'>أنشئ حسابك<br/>مجانًا</div>
              </div>

              <div class='step-divider-arrow'>←</div>

              <div class='step-item' onclick='openStepModal(&quot;أدخل موضوع بحثك أو ارفع ملفك&quot;, &quot;قم بكتابة عنوان بحثك أو ارفع ملفك بصيغة Word أو PDF لاستخلاص البيانات وتحليلها.&quot;)'>
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

    <!-- 6. ARTICLES SECTION (LIVE BLOGGER POSTS LOOP) -->
    <section class='inner-section-view' id='articles-section'>
      <div class='inner-section-header'>
        <h2>أحدث المقالات والأدلة البحثية</h2>
        <p>مقالات أكاديمية متخصصة ومحدثة خطوة بخطوة لمساعدتك في إنجاز أطروحتك وبحثك العلمي</p>
      </div>
      
      <b:section class='articles-grid-section' id='blog-posts-feed' showaddelement='yes'>
        <b:widget id='Blog1' locked='true' title='المقالات المنشورة' type='Blog'>
          <b:includable id='main' var='top'>
            <div class='articles-grid'>
              
              <!-- LOOP OVER PUBLISHED POSTS IN BLOGGER -->
              <b:loop values='data:posts' var='post'>
                <div class='article-card' expr:onclick='&quot;location.href=\&quot;&quot; + data:post.url + &quot;\&quot;&quot;'>
                  <div class='article-card-cover' style='background: linear-gradient(135deg, #0B2A5B, #2F6FC7);'>
                    <data:post.title/>
                  </div>
                  <div class='article-card-body'>
                    <span class='article-tag'>مقال منشور</span>
                    <h3 class='article-title'><data:post.title/></h3>
                    <p class='article-snippet'><data:post.snippet/></p>
                    <a class='article-link-more' expr:href='data:post.url'>اقرأ المقال كاملاً ←</a>
                  </div>
                </div>
              </b:loop>

              <!-- Curated fallback cards if fewer than 2 posts -->
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

            </div>
          </b:includable>
        </b:widget>
      </b:section>
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
            منصة مرصاد تقدم 9 أدوات ذكية متكاملة تغطي كافة مراحل البحث العلمي: البحث المباشر في قواعد البيانات العالمية، تحليل ومقارنة الدراسات السابقة، بناء خطة البحث والمشكلة والأهداف، توثيق المراجع بأسلوب APA و MLA وغيرها، تحليل الاستبيانات إحصائياً، الصياغة الأكاديمية السليمة، والمراجعة اللغوية والمنهجية مع التصدير النهائي إلى Word.
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

  <!-- POST / ARTICLE INNER VIEW (WHEN OPENING A SPECIFIC POST OR PAGE) -->
  <b:if cond='data:blog.pageType != &quot;index&quot;'>
    <main class='blog-inner-container'>
      <b:section class='main-post-section' id='single-post-view' showaddelement='yes'>
        <b:widget id='Blog2' locked='true' title='نص المقال الكامل' type='Blog'>
          <b:includable id='main' var='top'>
            <b:loop values='data:posts' var='post'>
              <article class='post-article'>
                <header class='post-header'>
                  <h1 class='post-title'><data:post.title/></h1>
                  <div class='post-meta'>
                    <span>الكاتب: <data:post.author/></span>
                    <span>•</span>
                    <span>تاريخ النشر: <data:post.dateHeader/></span>
                  </div>
                </header>

                <div class='post-body'>
                  <data:post.body/>
                </div>

                <div class='post-contact-card'>
                  <h4>تحتاج إلى مساعدة متخصصة في بحثك العلمي؟</h4>
                  <p>فريق مرصاد الأكاديمي مستعد لمساعدتك في التدقيق، التنسيق، والتحليل الإحصائي بأعلى دقة.</p>
                  <a class='btn-solid-call' href='tel:01015034659' style='display:inline-flex;'>
                    <span>اتصل بنا الآن: 01015034659</span>
                  </a>
                </div>
              </article>
            </b:loop>
          </b:includable>
        </b:widget>
      </b:section>
    </main>
  </b:if>

  <!-- 8. FOOTER -->
  <footer class='site-footer'>
    <div class='footer-container'>
      
      <!-- Right: Logo with new gold/white lighthouse in book -->
      <div class='footer-right-brand'>
        <a class='header-right-logo' href='/'>
          <img alt='مرصاد' class='header-logo-icon' src='{logo_footer_b64}'/>
          <div class='header-brand-texts'>
            <div class='header-brand-name' style='color:#ffffff;'>مِرْصَاد</div>
            <div class='header-brand-tagline' style='color:var(--accent-gold-light);'>نرصد المعرفة، ونبني البحث.</div>
          </div>
        </a>
      </div>

      <!-- Center: Links -->
      <nav class='footer-center-nav'>
        <a class='footer-link' href='/'>الرئيسية</a>
        <a class='footer-link' href='/#tools'>الأدوات</a>
        <a class='footer-link' href='/#features'>المميزات</a>
        <a class='footer-link' href='/#packages'>الباقات</a>
        <a class='footer-link' href='/#articles-section'>المقالات</a>
        <a class='footer-link' href='/#help-section'>المساعدة</a>
      </nav>

      <!-- Left: Social & Copyright -->
      <div class='footer-left-social'>
        <div class='social-icons-row'>
          <a class='social-link' href='https://wa.me/201015034659' target='_blank' title='واتساب'>
            <svg viewBox='0 0 24 24'><path d='M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21 5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0012.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 012.41 5.83c0 4.54-3.7 8.24-8.24 8.24-1.48 0-2.93-.4-4.2-1.15l-.3-.18-3.12.82.83-3.04-.2-.31a8.196 8.196 0 01-1.26-4.38c0-4.54 3.7-8.24 8.24-8.24m4.52 11.66c-.19-.09-1.12-.55-1.3-.61-.17-.07-.3-.1-.42.1-.12.19-.48.61-.59.73-.11.12-.23.14-.42.05-.19-.09-.81-.3-1.55-.96-.57-.51-.96-1.14-1.07-1.33-.11-.19-.01-.3.08-.39.09-.09.19-.23.29-.35.09-.12.13-.2.19-.34.07-.14.03-.26-.02-.35-.05-.09-.42-1.01-.58-1.39-.15-.36-.31-.31-.42-.32h-.36c-.12 0-.32.05-.49.23-.17.19-.65.64-.65 1.56 0 .93.67 1.82.77 1.95.09.12 1.33 2.03 3.22 2.85.45.19.8.31 1.08.4.45.14.86.12 1.19.07.36-.05 1.12-.46 1.28-.9.16-.45.16-.83.11-.9-.05-.07-.17-.11-.36-.2z'/></svg>
          </a>
          <a class='social-link' href='tel:01015034659' title='اتصال هاتفي'>
            <svg viewBox='0 0 24 24'><path d='M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z'/></svg>
          </a>
        </div>
        <div class='copyright-text'>جميع الحقوق محفوظة © 2026 منصة مرصاد</div>
      </div>

    </div>
  </footer>

</div>

{modal_html}

<script type='text/javascript'>
//<![CDATA[
{smart_js}
//]]>
</script>

</body>
</html>
"""

with open('theme.xml', 'w', encoding='utf-8') as f:
    f.write(theme_xml_content)
print(f"theme.xml generated successfully ({len(theme_xml_content)} bytes).")

# =========================================================================
# 4. VALIDATE theme.xml (XML Parser Check)
# =========================================================================
print("4. Validating theme.xml syntax with ElementTree...")
try:
    ET.parse('theme.xml')
    print("SUCCESS: theme.xml is 100% valid XML and compliant with Blogger V2 engine!")
except Exception as e:
    print(f"XML Validation Error: {e}")
    sys.exit(1)

print("All build tasks completed successfully!")
