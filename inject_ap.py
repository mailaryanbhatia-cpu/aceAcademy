#!/usr/bin/env python3
"""Inject all 38 AP courses into curriculum.html and update the UI."""
import pathlib, re

base = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs')

# ── AP curriculum data ────────────────────────────────────────────────────────
AP_DATA = """
  ap: {
    math: [
      { unit: 'AP Precalculus', topics: ['Polynomial and rational functions','Exponential and logarithmic functions','Trigonometric functions and unit circle','Trigonometric equations and identities','Conic sections','Parametric equations and polar coordinates','Limits and continuity (intro)'] },
      { unit: 'AP Calculus AB', topics: ['Limits and continuity','Derivatives: definition and basic rules','Derivatives: composite, implicit, and inverse','Contextual applications of differentiation','Applying derivatives to analyze functions','Integration and accumulation of change','Differential equations','Applications of integration'] },
      { unit: 'AP Calculus BC', topics: ['All AB topics (extended depth)','Advanced integration techniques','Series: Taylor and Maclaurin series','Parametric equations and polar curves','Vector-valued functions','Euler\'s method','Logistic differential equations','Infinite sequences and series convergence'] },
      { unit: 'AP Statistics', topics: ['Exploring one-variable data','Exploring two-variable data','Collecting data: sampling and experiments','Probability and random variables','Sampling distributions','Inference for proportions','Inference for means','Chi-square tests','Inference for regression'] },
    ],
    science: [
      { unit: 'AP Biology', topics: ['Chemistry of life','Cell structure and function','Cellular energetics (photosynthesis & respiration)','Cell communication and cell cycle','Heredity and genetics','Gene expression and regulation','Natural selection and evolution','Ecology and population dynamics'] },
      { unit: 'AP Chemistry', topics: ['Atomic structure and properties','Molecular and ionic compound structure','Intermolecular forces and properties','Chemical reactions','Kinetics','Thermodynamics','Equilibrium','Acids and bases','Electrochemistry','Nuclear chemistry'] },
      { unit: 'AP Environmental Science', topics: ['Earth systems and resources','The living world: ecosystems','Populations','Earth\'s atmosphere','Land and water use','Energy resources and consumption','Atmospheric pollution','Aquatic and terrestrial pollution','Global change'] },
      { unit: 'AP Physics 1: Algebra-Based', topics: ['Kinematics','Forces and Newton\'s laws','Circular motion and gravitation','Energy and work','Momentum','Simple harmonic motion','Waves and sound','Electric charge and fields','DC circuits'] },
      { unit: 'AP Physics 2: Algebra-Based', topics: ['Fluids','Thermodynamics','Electric force, field, and potential','Circuits','Magnetism and electromagnetic induction','Geometric and physical optics','Quantum, atomic, and nuclear physics'] },
      { unit: 'AP Physics C: Mechanics', topics: ['Kinematics (calculus-based)','Newton\'s laws (calculus-based)','Work, energy, and power','Systems of particles and linear momentum','Rotation','Oscillations','Gravitation'] },
      { unit: 'AP Physics C: Electricity & Magnetism', topics: ['Electrostatics','Conductors, capacitors, dielectrics','Electric circuits','Magnetic fields','Electromagnetism and induction','Maxwell\'s equations (intro)'] },
    ],
    ela: [
      { unit: 'AP English Language and Composition', topics: ['Rhetorical situation and claims','Reasoning and organization','Style and evidence','Synthesis essay','Rhetorical analysis essay','Argument essay','Close reading non-fiction','Tone, diction, syntax analysis'] },
      { unit: 'AP English Literature and Composition', topics: ['Short fiction and prose','Poetry analysis','Longer fiction and drama','Character, setting, structure','Figurative language and literary devices','Literary argument essay','Free-response poetry essay','Open question essay'] },
    ],
    history: [
      { unit: 'AP United States History', topics: ['Period 1: 1491–1607','Period 2: 1607–1754','Period 3: 1754–1800','Period 4: 1800–1848','Period 5: 1844–1877','Period 6: 1865–1898','Period 7: 1890–1945','Period 8: 1945–1980','Period 9: 1980–Present','DBQ and LEQ essay skills'] },
      { unit: 'AP World History: Modern', topics: ['Period 1: 1200–1450 (Networks of exchange)','Period 2: 1450–1750 (Exploration and encounters)','Period 3: 1750–1900 (Industrialization)','Period 4: 1900–Present (Conflict and independence)','Comparison and causation','Continuity and change over time','Document-based questions (DBQ)'] },
      { unit: 'AP European History', topics: ['Renaissance and Reformation','Exploration and colonialism','Scientific Revolution and Enlightenment','French Revolution and Napoleon','Industrialization and 19th-century ideologies','WWI and interwar period','WWII and Holocaust','Cold War and European integration','Contemporary Europe'] },
      { unit: 'AP United States Government and Politics', topics: ['Foundations of democracy','Interactions among branches','Civil liberties and civil rights','American political ideologies','Political participation','Required Supreme Court cases','Foundational documents analysis'] },
      { unit: 'AP Comparative Government and Politics', topics: ['Political systems and regimes','Sovereignty and legitimacy','Political institutions (legislatures, executives)','Citizens, society, and the state','Political and economic change','Country case studies: UK, Mexico, Russia, China, Iran, Nigeria'] },
      { unit: 'AP Human Geography', topics: ['Thinking geographically','Population and migration','Cultural patterns and processes','Political patterns and processes','Agriculture and rural land use','Cities and urban land use','Industrial and economic development'] },
      { unit: 'AP Macroeconomics', topics: ['Basic economic concepts','Economic indicators and the business cycle','National income and price determination','Financial sector and monetary policy','Stabilization policies','Economic growth and productivity','International trade and finance'] },
      { unit: 'AP Microeconomics', topics: ['Basic economic concepts and scarcity','Supply and demand','Production, cost, and the perfect competition model','Imperfect competition (monopoly, oligopoly)','Factor markets','Market failure and the role of government','International trade'] },
      { unit: 'AP Psychology', topics: ['History and approaches','Research methods and statistics','Biological bases of behavior','Sensation and perception','States of consciousness','Learning','Cognition and memory','Developmental psychology','Personality','Abnormal psychology and treatment','Social psychology'] },
    ],
    cs: [
      { unit: 'AP Computer Science A', topics: ['Primitive types and variables','Using objects','Boolean expressions and if statements','Iteration','Writing classes','Array and ArrayList','2D arrays','Inheritance and polymorphism','Recursion','Sorting and searching algorithms'] },
      { unit: 'AP Computer Science Principles', topics: ['Creative development','Data representation','Algorithms and programming','Computer systems and networks','Impact of computing','Explore Performance Task','Create Performance Task'] },
    ],
    arts: [
      { unit: 'AP Art History', topics: ['Global prehistory','Ancient Mediterranean','Early Europe and colonial Americas','Later Europe and Americas','Indigenous Americas, Africa, and Pacific','South, East, and Southeast Asia','Contemporary art and global connections','Visual analysis and contextual inquiry'] },
      { unit: 'AP Music Theory', topics: ['Pitch, notation, and scales','Rhythm, meter, and melody','Intervals and triads','Diatonic chords and harmonic progressions','Voice leading and part writing','Seventh chords and chromaticism','Form and analysis','Sight-singing and dictation'] },
      { unit: 'AP Studio Art: 2-D Art and Design', topics: ['Elements and principles of design','Conceptual development','Portfolio investigation process','Breadth: range of approaches','Sustained investigation (15 works)','Final portfolio submission'] },
      { unit: 'AP Studio Art: 3-D Art and Design', topics: ['Three-dimensional form and space','Material exploration (clay, metal, glass, fiber)','Conceptual development','Sustained investigation (15 works)','Portfolio breadth and depth'] },
      { unit: 'AP Studio Art: Drawing', topics: ['Mark-making and gesture','Composition and space','Value and light','Figure drawing','Observational and expressive approaches','Sustained investigation portfolio'] },
    ],
    languages: [
      { unit: 'AP Chinese Language and Culture', topics: ['Interpersonal communication','Presentational speaking and writing','Interpretive listening and reading','Family and community','School and education','Contemporary life','Global challenges','Cultural comparisons','Simulated conversation practice'] },
      { unit: 'AP French Language and Culture', topics: ['Global challenges','Science and technology','Contemporary life','Personal and public identities','Families and communities','Beauty and aesthetics','Interpersonal and presentational modes','Cultural comparison essays'] },
      { unit: 'AP German Language and Culture', topics: ['Families in different societies','Science and technology','Contemporary life in German-speaking world','Global challenges','Personal and public identity','Beauty and aesthetics','Oral and written communication'] },
      { unit: 'AP Italian Language and Culture', topics: ['Beauty and aesthetics in Italy','Families and communities','Contemporary Italian life','Science and technology','Global challenges','Personal identity','Italian cultural products and practices'] },
      { unit: 'AP Japanese Language and Culture', topics: ['Interpersonal communication','Presentational modes','Japanese writing systems (hiragana, katakana, kanji)','Families and communities in Japan','Contemporary Japanese life','Global challenges','Cultural comparisons'] },
      { unit: 'AP Latin', topics: ['Caesar: Gallic War','Vergil: Aeneid','Latin prose and poetry translation','Sight reading','Latin grammar mastery','Roman history and culture','Comparative literature and analysis'] },
      { unit: 'AP Spanish Language and Culture', topics: ['Global challenges','Science and technology','Contemporary life','Personal and public identities','Families and communities','Beauty and aesthetics','Oral presentational tasks','Argumentative essay'] },
      { unit: 'AP Spanish Literature and Culture', topics: ['Colonial period texts','19th-century narrative','20th-century avant-garde','Contemporary voices','Poetry analysis','Drama and prose','Literary essay writing','Oral commentary'] },
    ],
    capstone: [
      { unit: 'AP Seminar', topics: ['Identifying and defining problems','Research and evidence evaluation','Analyzing multiple perspectives','Argument and reasoning','Written and oral communication','Team project (TMP)','Individual research report (IWA)','End-of-course exam'] },
      { unit: 'AP Research', topics: ['Selecting a research question','Literature review and gap identification','Research methodology','Data collection and analysis','Drawing evidence-based conclusions','Scholarly writing conventions','Academic paper (5,000 words)','Oral defense of research'] },
    ],
  },
"""

# ── AP subject definitions (for JS) ──────────────────────────────────────────
AP_SUBJECTS_JS = """
const AP_SUBJECTS = [
  { id: 'math',      label: 'Mathematics',          color: '#60a5fa' },
  { id: 'science',   label: 'Science',              color: '#34d399' },
  { id: 'ela',       label: 'English',              color: '#a78bfa' },
  { id: 'history',   label: 'History & Social Studies', color: '#fbbf24' },
  { id: 'cs',        label: 'Computer Science',     color: '#22d3ee' },
  { id: 'arts',      label: 'Arts',                 color: '#f472b6' },
  { id: 'languages', label: 'World Languages',      color: '#fb923c' },
  { id: 'capstone',  label: 'AP Capstone',          color: '#818cf8' },
];
"""

# ── Load curriculum.html ──────────────────────────────────────────────────────
p = base / 'curriculum.html'
html = p.read_text(encoding='utf-8')

# ── 1. Inject AP data into CURRICULUM object ──────────────────────────────────
# Find the end of grade 12 data (last closing before `};` of CURRICULUM)
# We'll insert before the closing `};` of the CURRICULUM object
CURRICULUM_END = '};  // end CURRICULUM'
if CURRICULUM_END not in html:
    # Find the pattern: the CURRICULUM closing
    # The CURRICULUM object ends with `\n};\n` after the last grade block
    # Locate `const CURRICULUM = {` then find its matching closing `};`
    idx_start = html.index('const CURRICULUM = {')
    # Find closing }; after that
    depth = 0
    i = idx_start + len('const CURRICULUM = {')
    while i < len(html):
        c = html[i]
        if c == '{': depth += 1
        elif c == '}':
            if depth == 0:
                # This is the closing } of CURRICULUM
                # Check it's followed by ;
                if html[i+1] == ';':
                    insert_pos = i  # insert AP before this }
                    break
            else:
                depth -= 1
        i += 1
    html = html[:insert_pos] + AP_DATA + html[insert_pos:]
    print('✅ AP data injected into CURRICULUM')
else:
    print('AP data already present')

# ── 2. Add AP_SUBJECTS constant after SUBJECTS ────────────────────────────────
if 'AP_SUBJECTS' not in html:
    SUBJECTS_END = '];\n\nconst CURRICULUM'
    if SUBJECTS_END in html:
        html = html.replace(SUBJECTS_END, '];\n' + AP_SUBJECTS_JS + '\nconst CURRICULUM', 1)
        print('✅ AP_SUBJECTS injected')
    else:
        print('⚠️  Could not find SUBJECTS end marker')
else:
    print('AP_SUBJECTS already present')

# ── 3. Add "AP Courses" to grade list sidebar ─────────────────────────────────
OLD_GRADE_LIST_END = '      <li><a href="#" data-grade="12">Grade 12</a></li>\n    </ul>'
NEW_GRADE_LIST_END = '      <li><a href="#" data-grade="12">Grade 12</a></li>\n      <li style="margin-top:10px;padding:0 16px 4px"><span style="font-size:.6rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;color:#7a8fa8">Advanced</span></li>\n      <li><a href="#" data-grade="ap">🎓 AP Courses</a></li>\n    </ul>'

if 'data-grade="ap"' not in html:
    if OLD_GRADE_LIST_END in html:
        html = html.replace(OLD_GRADE_LIST_END, NEW_GRADE_LIST_END, 1)
        print('✅ AP grade added to sidebar')
    else:
        print('⚠️  Could not find grade list end')
else:
    print('AP grade already in sidebar')

# ── 4. Update gradeNames to include 'ap' ─────────────────────────────────────
OLD_NAMES = "const gradeNames = { 6:'Sixth',7:'Seventh',8:'Eighth',9:'Ninth',10:'Tenth',11:'Eleventh',12:'Twelfth' };"
NEW_NAMES = "const gradeNames = { 6:'Sixth',7:'Seventh',8:'Eighth',9:'Ninth',10:'Tenth',11:'Eleventh',12:'Twelfth', ap:'AP' };"
if OLD_NAMES in html:
    html = html.replace(OLD_NAMES, NEW_NAMES, 1)
    print('✅ gradeNames updated')

# ── 5. Update render() to use AP_SUBJECTS when grade is 'ap' ─────────────────
OLD_RENDER_SUBJECTS = "  let rendered = 0;\n  SUBJECTS.forEach(subj => {"
NEW_RENDER_SUBJECTS = """  let rendered = 0;
  const activeSubjects = (currentGrade === 'ap') ? AP_SUBJECTS : SUBJECTS;
  activeSubjects.forEach(subj => {"""
if OLD_RENDER_SUBJECTS in html:
    html = html.replace(OLD_RENDER_SUBJECTS, NEW_RENDER_SUBJECTS, 1)
    print('✅ render() updated to use AP_SUBJECTS')

# ── 6. Update grade header for AP ─────────────────────────────────────────────
OLD_HEADER = "  let html = `<div class=\"grade-header\"><h1>${gradeNames[currentGrade]} Grade</h1><span>Full curriculum — select a subject to filter</span></div>`;"
NEW_HEADER = """  const isAP = currentGrade === 'ap';
  const gradeTitle = isAP ? 'AP Courses' : gradeNames[currentGrade] + ' Grade';
  const gradeSubtitle = isAP ? '38 College Board AP courses — click a unit to expand topics' : 'Full curriculum — select a subject to filter';
  let html = `<div class="grade-header"><h1>${gradeTitle}</h1><span>${gradeSubtitle}</span></div>`;"""
if OLD_HEADER in html:
    html = html.replace(OLD_HEADER, NEW_HEADER, 1)
    print('✅ Grade header updated')

# ── 7. Fix setGrade to not parseInt 'ap' ─────────────────────────────────────
OLD_SET_GRADE = "    setGrade(parseInt(a.dataset.grade));"
NEW_SET_GRADE = "    const g = a.dataset.grade; setGrade(g === 'ap' ? 'ap' : parseInt(g));"
if OLD_SET_GRADE in html:
    html = html.replace(OLD_SET_GRADE, NEW_SET_GRADE, 1)
    print('✅ setGrade click handler fixed')

# ── 8. Fix setGrade active class selector ─────────────────────────────────────
OLD_SELECTOR = '  document.querySelector(`#gradeList a[data-grade="${g}"]`).classList.add(\'active\');'
NEW_SELECTOR = '  const activeLink = document.querySelector(`#gradeList a[data-grade="${g}"]`); if(activeLink) activeLink.classList.add(\'active\');'
if OLD_SELECTOR in html:
    html = html.replace(OLD_SELECTOR, NEW_SELECTOR, 1)
    print('✅ setGrade selector made safe')

# ── 9. Update sidebar subject buttons to use active subjects ──────────────────
OLD_SUBJ_BTNS = "  SUBJECTS.forEach(s => {\n    html += `<button class=\"subj-btn ${activeSubject===s.id?'active':''}\" onclick=\"setSubject('${s.id}')\">\n      <span class=\"dot\" style=\"background:${s.color}\"></span>${s.label}\n    </button>`;\n  });"
NEW_SUBJ_BTNS = """  const sidebarSubjects = (currentGrade === 'ap') ? AP_SUBJECTS : SUBJECTS;
  sidebarSubjects.forEach(s => {
    html += `<button class="subj-btn ${activeSubject===s.id?'active':''}" onclick="setSubject('${s.id}')">
      <span class="dot" style="background:${s.color}"></span>${s.label}
    </button>`;
  });"""
if OLD_SUBJ_BTNS in html:
    html = html.replace(OLD_SUBJ_BTNS, NEW_SUBJ_BTNS, 1)
    print('✅ Subject sidebar buttons updated')

# ── Save ──────────────────────────────────────────────────────────────────────
p.write_text(html, encoding='utf-8')
print('\n✅ curriculum.html saved')
print(f'   File size: {len(html):,} bytes')
