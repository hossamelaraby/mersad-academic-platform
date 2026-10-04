# -*- coding: utf-8 -*-
"""
HTML and JavaScript generation for the 9 Dedicated Smart Academic Tools in Mersad.
"""

def get_tools_modal_html():
    return """
<!-- SMART MODAL CONTAINER (9 DEDICATED TOOLS) -->
<div class="modal-overlay" id="smartToolModal" onclick="closeSmartToolOnOverlay(event)">
  <div class="modal-box">
    <button class="modal-close-btn" onclick="closeSmartToolModal()" title="إغلاق">✕</button>
    
    <!-- Modal Header -->
    <div class="modal-header-badge-row">
      <div class="modal-tool-icon" id="toolHeaderIcon">
        <svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>
      </div>
      <div>
        <div style="display:flex; align-items:center; gap:8px;">
          <h3 class="modal-title" id="toolHeaderTitle">مرصاد المصادر</h3>
          <span class="modal-badge-tag" id="toolHeaderBadge">بحث أكاديمي</span>
        </div>
        <p class="modal-desc" id="toolHeaderDesc">البحث في قواعد البيانات والمصادر الموثوقة</p>
      </div>
    </div>

    <!-- 1. TOOL: SOURCES (مرصاد المصادر) -->
    <div class="tool-pane" id="pane-sources" style="display:none;">
      <label class="tool-field-label">أدخل موضوع البحث، الكلمات المفتاحية، أو عنوان الدراسة:</label>
      <div style="display:flex; gap:8px; margin-bottom:12px;">
        <input type="text" id="sourcesQuery" class="tool-input-text" style="margin-bottom:0;" placeholder="مثال: الذكاء الاصطناعي في التعليم الجامعي، إدارة الجودة الشاملة..." />
        <button class="tool-btn-primary" style="width:auto; padding:0 24px;" onclick="runSourcesSearch()">
          <span>بحث حي</span>
          <svg style="width:16px;height:16px;fill:currentColor;" viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0016 9.5 6.5 6.5 0 109.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
        </button>
      </div>

      <div class="tool-file-dropzone" onclick="document.getElementById('sourcesFileInput').click()">
        <input type="file" id="sourcesFileInput" accept="image/*,.pdf,.doc,.docx" style="display:none;" onchange="handleSourcesFile(this)" />
        <svg style="width:30px;height:30px;fill:#64748b;margin-bottom:6px;" viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM14 13v4h-4v-4H7l5-5 5 5h-3z"/></svg>
        <div style="font-size:13px; font-weight:700; color:#0B2A5B;">أو أرفق صورة صفحة عنوان أو مستند للبحث في مصادره</div>
        <div style="font-size:11.5px; color:#64748b;" id="sourcesFileName">يدعم الصور (PNG, JPG) وملفات PDF لاستخراج الكلمات المفتاحية</div>
      </div>

      <!-- Quick External Academic Databases -->
      <div style="margin-top:10px; display:flex; align-items:center; gap:8px; flex-wrap:wrap;">
        <span style="font-size:12px; font-weight:700; color:#475569;">بوابات بحث مباشرة:</span>
        <button type="button" class="paper-btn-link" onclick="openExternalSearch('scholar')">Google Scholar</button>
        <button type="button" class="paper-btn-link" onclick="openExternalSearch('semantic')">Semantic Scholar</button>
        <button type="button" class="paper-btn-link" onclick="openExternalSearch('mandumah')">دار المنظومة</button>
        <button type="button" class="paper-btn-link" onclick="openExternalSearch('sciencedirect')">ScienceDirect</button>
      </div>

      <div class="tool-result-container" id="sourcesResultsArea" style="display:none;"></div>
    </div>

    <!-- 2. TOOL: LITERATURE (مرصاد الدراسات السابقة) -->
    <div class="tool-pane" id="pane-literature" style="display:none;">
      <p style="font-size:13px; color:#475569; margin-bottom:12px;">أدخل عناوين أو ملخصات الدراسات السابقة (دراسة واحدة على الأقل أو عدة دراسات) لاستخراج مصفوفة المقارنة وتحديد الفجوة البحثية:</p>
      
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:10px;">
        <div>
          <label class="tool-field-label">الدراسة الأولى (المؤلف، السنة، العنوان، المنهج):</label>
          <textarea id="litStudy1" class="tool-textarea" style="height:90px;" placeholder="مثال: دراسة (العتيبي، 2023): أثر التحول الرقمي في الجامعات السعودية، استخدم المنهج الوصفي على عينة 300 عضو هيئة تدريس، وتوصلت لوجود أثر إيجابي..."></textarea>
        </div>
        <div>
          <label class="tool-field-label">الدراسة الثانية (المؤلف، السنة، العنوان، المنهج):</label>
          <textarea id="litStudy2" class="tool-textarea" style="height:90px;" placeholder="مثال: دراسة (Smith, 2022): قياس فاعلية الذكاء الاصطناعي التوليدي، استخدم المنهج شبه التجريبي..."></textarea>
        </div>
      </div>

      <div style="margin-bottom:12px;">
        <label class="tool-field-label">موضوع دراستك الحالية المخطط لها:</label>
        <input type="text" id="litCurrentStudy" class="tool-input-text" placeholder="مثال: واقع توظيف الذكاء الاصطناعي في الجامعات المصرية..." />
      </div>

      <button class="tool-btn-primary" onclick="runLiteratureMatrix()">
        <span>توليد مصفوفة المقارنة وصياغة الفجوة البحثية</span>
        <span>⚡</span>
      </button>

      <div class="tool-result-container" id="litResultArea" style="display:none;"></div>
    </div>

    <!-- 3. TOOL: RESEARCHER (مرصاد الباحث) -->
    <div class="tool-pane" id="pane-researcher" style="display:none;">
      <label class="tool-field-label">عنوان البحث أو موضوع الفكرة البحثية:</label>
      <input type="text" id="resTopicInput" class="tool-input-text" placeholder="مثال: دور القيادة الرقمية في تحسين الأداء الوظيفي في المؤسسات الحكومية" />

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:12px;">
        <div>
          <label class="tool-field-label">المتغير المستقل (أو المحور الأول):</label>
          <input type="text" id="resVarIndep" class="tool-input-text" placeholder="مثال: القيادة الرقمية" />
        </div>
        <div>
          <label class="tool-field-label">المتغير التابع (أو المحور الثاني):</label>
          <input type="text" id="resVarDep" class="tool-input-text" placeholder="مثال: الأداء الوظيفي" />
        </div>
      </div>

      <label class="tool-field-label">مجال التطبيق أو مجتمع الدراسة (اختياري):</label>
      <input type="text" id="resContext" class="tool-input-text" placeholder="مثال: وزارة التعليم، الجامعات الحكومية المصرية، القطاع المصرفي..." />

      <button class="tool-btn-primary" onclick="runResearcherBuilder()">
        <span>بناء مشكلة البحث، الأسئلة، الأهداف والفرضيات</span>
        <span>🏛️</span>
      </button>

      <div class="tool-result-container" id="resResultArea" style="display:none;"></div>
    </div>

    <!-- 4. TOOL: CITATIONS (مرصاد التوثيق) -->
    <div class="tool-pane" id="pane-citations" style="display:none;">
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:10px;">
        <div>
          <label class="tool-field-label">نمط التوثيق الأكاديمي:</label>
          <select id="citeStyleSelect" class="tool-select">
            <option value="APA7">APA 7th Edition (الإصدار السابع - الأكثر شيوعاً)</option>
            <option value="MLA9">MLA 9th Edition (الإصدار التاسع)</option>
            <option value="Harvard">Harvard Style (نظام هارفارد)</option>
            <option value="Chicago">Chicago Notes &amp; Bibliography (شيكاغو الحواشي)</option>
          </select>
        </div>
        <div>
          <label class="tool-field-label">نوع المصدر المراد توثيقه:</label>
          <select id="citeTypeSelect" class="tool-select" onchange="toggleCiteFields()">
            <option value="journal">بحث في مجلة علمية محكمة</option>
            <option value="book">كتاب مطبوع أو إلكتروني</option>
            <option value="thesis">رسالة ماجستير أو أطروحة دكتوراه</option>
            <option value="web">موقع إلكتروني أو مقال رقمي</option>
          </select>
        </div>
      </div>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:10px;">
        <div>
          <label class="tool-field-label">المؤلف (أو المؤلفون):</label>
          <input type="text" id="citeAuthor" class="tool-input-text" placeholder="مثال: أحمد محمد علي أو Al-Otaibi, K." />
        </div>
        <div>
          <label class="tool-field-label">سنة النشر:</label>
          <input type="text" id="citeYear" class="tool-input-text" placeholder="مثال: 2024" />
        </div>
      </div>

      <label class="tool-field-label">عنوان البحث / الكتاب / المقال:</label>
      <input type="text" id="citeTitle" class="tool-input-text" placeholder="مثال: فاعلية التعليم الإلكتروني في تنمية التفكير الناقد" />

      <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px; margin-bottom:14px;" id="citeExtraFields">
        <div>
          <label class="tool-field-label">اسم المجلة / الناشر / الجامعة:</label>
          <input type="text" id="citeSource" class="tool-input-text" placeholder="مثال: مجلة الدراسات التربوية" />
        </div>
        <div>
          <label class="tool-field-label">المجلد والعدد أو الصفحات:</label>
          <input type="text" id="citePages" class="tool-input-text" placeholder="مج 12، ع 4، ص 45-68" />
        </div>
        <div>
          <label class="tool-field-label">معرّف الرقمي DOI / الرابط:</label>
          <input type="text" id="citeDoi" class="tool-input-text" placeholder="https://doi.org/..." />
        </div>
      </div>

      <button class="tool-btn-primary" onclick="runCitationGenerator()">
        <span>توليد التوثيق في المتن وقائمة المراجع</span>
        <span>📑</span>
      </button>

      <div class="tool-result-container" id="citeResultArea" style="display:none;"></div>
    </div>

    <!-- 5. TOOL: FILES (مرصاد الملفات) -->
    <div class="tool-pane" id="pane-files" style="display:none;">
      <div class="tool-file-dropzone" onclick="document.getElementById('analyzerFileInput').click()">
        <input type="file" id="analyzerFileInput" accept=".pdf,.doc,.docx,.txt" style="display:none;" onchange="handleAnalyzerFile(this)" />
        <svg style="width:36px;height:36px;fill:#2F6FC7;margin-bottom:8px;" viewBox="0 0 24 24"><path d="M14 2H6c-1.1 0-1.99.9-1.99 2L4 20c0 1.1.89 2 1.99 2H18c1.1 0 2-.9 2-2V8l-6-6zm2 16H8v-2h8v2zm0-4H8v-2h8v2zm-3-5V3.5L18.5 9H13z"/></svg>
        <div style="font-size:14px; font-weight:800; color:#0B2A5B;" id="analyzerDropTitle">انقر لاختيار ملف PDF أو Word لتحليله واستخراج معطياته</div>
        <div style="font-size:12px; color:#64748b; margin-top:4px;" id="analyzerFileInfo">الحد الأقصى الموصى به: 25 ميجابايت (أبحاث، رسائل، مقالات)</div>
      </div>

      <label class="tool-field-label">أو الصق نص المستند مباشرة هنا:</label>
      <textarea id="analyzerTextInput" class="tool-textarea" style="height:100px;" placeholder="الصق المستخلص، مقدمة البحث، أو المنهجية التي تود استخراج معلوماتها..."></textarea>

      <div style="display:flex; gap:10px; margin-bottom:12px;">
        <select id="analyzerModeSelect" class="tool-select" style="margin-bottom:0;">
          <option value="all">تحليل شامل (الملخص، المنهجية، النتائج، التوصيات)</option>
          <option value="summary">استخراج المستخلص التنفيذي فقط</option>
          <option value="methodology">تحليل المنهجية والأدوات والعينة</option>
          <option value="gaps">استخراج محددات الدراسة والبحوث المستقبلية</option>
        </select>
        <button class="tool-btn-primary" style="width:auto; padding:0 24px;" onclick="runFilesAnalysis()">
          <span>بدء التحليل</span>
          <span>⚡</span>
        </button>
      </div>

      <div class="tool-result-container" id="analyzerResultArea" style="display:none;"></div>
    </div>

    <!-- 6. TOOL: DATA (مرصاد البيانات) -->
    <div class="tool-pane" id="pane-data" style="display:none;">
      <p style="font-size:13px; color:#475569; margin-bottom:10px;">أدخل تكرارات الإجابة على عبارات مقياس ليكرت الخماسي (موافق بشدة = 5، موافق = 4، محايد = 3، غير موافق = 2، غير موافق بشدة = 1) لحساب المتوسط الحسابي، الانحراف المعياري، الوزن النسبي، والاتجاه العام:</p>
      
      <div style="background:#ffffff; border:1px solid #e2e8f0; border-radius:10px; padding:12px; margin-bottom:12px;">
        <div style="display:grid; grid-template-columns:2fr 1fr 1fr 1fr 1fr 1fr; gap:6px; font-size:12px; font-weight:700; color:#0B2A5B; margin-bottom:6px; text-align:center;">
          <span style="text-align:right;">نص العبارة / البعد</span>
          <span>موافق بشدة (5)</span>
          <span>موافق (4)</span>
          <span>محايد (3)</span>
          <span>معارض (2)</span>
          <span>معارض بشدة (1)</span>
        </div>
        
        <!-- Row 1 -->
        <div style="display:grid; grid-template-columns:2fr 1fr 1fr 1fr 1fr 1fr; gap:6px; margin-bottom:8px;">
          <input type="text" id="statItem1" class="tool-input-text" style="margin-bottom:0; font-size:12px;" value="1. تسهم أدوات الذكاء الاصطناعي في توفير وقت الباحث الأكاديمي." />
          <input type="number" id="f1_5" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="45" />
          <input type="number" id="f1_4" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="30" />
          <input type="number" id="f1_3" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="12" />
          <input type="number" id="f1_2" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="8" />
          <input type="number" id="f1_1" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="5" />
        </div>

        <!-- Row 2 -->
        <div style="display:grid; grid-template-columns:2fr 1fr 1fr 1fr 1fr 1fr; gap:6px; margin-bottom:8px;">
          <input type="text" id="statItem2" class="tool-input-text" style="margin-bottom:0; font-size:12px;" value="2. توفر المنصة مراجع دقيقة مطابقة لمتطلبات الجامعات." />
          <input type="number" id="f2_5" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="40" />
          <input type="number" id="f2_4" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="35" />
          <input type="number" id="f2_3" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="15" />
          <input type="number" id="f2_2" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="7" />
          <input type="number" id="f2_1" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="3" />
        </div>

        <!-- Row 3 -->
        <div style="display:grid; grid-template-columns:2fr 1fr 1fr 1fr 1fr 1fr; gap:6px;">
          <input type="text" id="statItem3" class="tool-input-text" style="margin-bottom:0; font-size:12px;" value="3. تتميز المنصة بسهولة الاستخدام وتوافقها مع الأجهزة المختلفة." />
          <input type="number" id="f3_5" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="55" />
          <input type="number" id="f3_4" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="28" />
          <input type="number" id="f3_3" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="10" />
          <input type="number" id="f3_2" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="5" />
          <input type="number" id="f3_1" class="tool-input-text" style="margin-bottom:0; text-align:center;" value="2" />
        </div>
      </div>

      <button class="tool-btn-primary" onclick="runStatisticalAnalysis()">
        <span>حساب المؤشرات الإحصائية وتفسير النتائج وفق المعايير الأكاديمية</span>
        <span>📊</span>
      </button>

      <div class="tool-result-container" id="statResultArea" style="display:none;"></div>
    </div>

    <!-- 7. TOOL: WRITING (مرصاد الكتابة) -->
    <div class="tool-pane" id="pane-writing" style="display:none;">
      <label class="tool-field-label">أدخل النص المراد إعادة صياغته أكاديمياً وتحسين أسلوبه العلمي:</label>
      <textarea id="writeOriginalText" class="tool-textarea" style="height:100px;" placeholder="الصق النص هنا... مثلاً: نحن شايفين إن التكنولوجيا مهمة جداً ومفيش حد يقدر يستغنى عنها في التعليم والجامعة..."></textarea>

      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-bottom:12px;">
        <div>
          <label class="tool-field-label">الأسلوب الأكاديمي المستهدف:</label>
          <select id="writeToneSelect" class="tool-select">
            <option value="formal">رسمي وموضوعي (الغائب، رصين)</option>
            <option value="critical">نقدي تحليلي (مناقشة الدراسات)</option>
            <option value="concise">موجز ومباشر (خاتمة ومستخلص)</option>
          </select>
        </div>
        <div>
          <label class="tool-field-label">درجة إعادة الصياغة:</label>
          <select id="writeLevelSelect" class="tool-select">
            <option value="deep">إعادة صياغة شاملة (تغيير التراكيب بالكامل)</option>
            <option value="medium">تحسين الصياغة مع الحفاظ على المصطلحات</option>
            <option value="light">تدقيق نحوي وتركيبي خفيف</option>
          </select>
        </div>
      </div>

      <button class="tool-btn-primary" onclick="runAcademicParaphrase()">
        <span>إعادة الصياغة الأكاديمية المحكمة</span>
        <span>✍️</span>
      </button>

      <div class="tool-result-container" id="writeResultArea" style="display:none;"></div>
    </div>

    <!-- 8. TOOL: REVIEW (مرصاد المراجعة) -->
    <div class="tool-pane" id="pane-review" style="display:none;">
      <label class="tool-field-label">الصق فقرة أو فصلاً للمراجعة المنهجية واللغوية:</label>
      <textarea id="reviewTextInput" class="tool-textarea" style="height:110px;" placeholder="الصق النص هنا للمراجعة والتدقيق... ستقوم المنصة بفحص: سلامة التراكيب، الربط المنطقي، التوافق بين الأسئلة والأهداف، وأسلوب التوثيق."></textarea>

      <button class="tool-btn-primary" onclick="runMethodologicalReview()">
        <span>بدء التدقيق المنهجي واللغوي الفوري</span>
        <span>🔍</span>
      </button>

      <div class="tool-result-container" id="reviewResultArea" style="display:none;"></div>
    </div>

    <!-- 9. TOOL: WORD (تصدير Word) -->
    <div class="tool-pane" id="pane-word" style="display:none;">
      <label class="tool-field-label">عنوان البحث أو المستند الأكاديمي:</label>
      <input type="text" id="docPaperTitle" class="tool-input-text" value="مشروع البحث العلمي - منصة مرصاد" />

      <label class="tool-field-label">محتوى البحث المراد تصديره إلى ملف Microsoft Word (.doc):</label>
      <textarea id="docContentText" class="tool-textarea" style="height:120px;" placeholder="اكتب أو الصق نص تقريرك، مشكلة بحثك، أو مصفوفة دراساتك هنا..."></textarea>

      <div style="display:flex; gap:10px; margin-bottom:12px;">
        <select id="docFontSelect" class="tool-select" style="margin-bottom:0;">
          <option value="Traditional Arabic">الخط: Traditional Arabic (المعتمد للرسائل)</option>
          <option value="Simplified Arabic">الخط: Simplified Arabic</option>
          <option value="Cairo">الخط: Cairo</option>
        </select>
        <button class="tool-btn-primary" style="width:auto; padding:0 24px;" onclick="exportToWordDoc()">
          <span>تنزيل ملف Word (.doc) فوراً</span>
          <svg style="width:16px;height:16px;fill:currentColor;" viewBox="0 0 24 24"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96zM17 13l-5 5-5-5h3V9h4v4h3z"/></svg>
        </button>
      </div>

      <div style="font-size:12px; color:#64748b; line-height:1.6;">
        ✓ يتم تصدير الملف بتنسيق Microsoft Word الكامل مع دعم كامل للغة العربية (RTL) والحواشي والعناوين الجاهزة للطباعة والتحرير.
      </div>
    </div>

    <!-- Modal Footer Actions -->
    <div class="modal-action-row" style="margin-top:20px; border-top:1px solid #edf2f7; padding-top:16px;">
      <a href="https://wa.me/201015034659" target="_blank" class="btn-solid-call" style="flex:1; justify-content:center;">
        <span>تواصل مع باحث متخصص (01015034659)</span>
        <span>←</span>
      </a>
      <button class="btn-outline-wa" onclick="closeSmartToolModal()">إغلاق النافذة</button>
    </div>

  </div>
</div>
"""
