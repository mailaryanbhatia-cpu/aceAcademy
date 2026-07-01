#!/usr/bin/env python3
"""
Fix 3 curriculum/worksheet mismatches in worksheets.html:
 1. G10 science: remove extra Unit 4 (nuclear chemistry)
 2. G12 science Unit 2: add 6th topic (nuclear chemistry)
 3. G12 history: insert missing Unit 3 (Economics & Personal Finance)
"""
import sys, json, re

PATH = '/sessions/admiring-stoic-pascal/mnt/outputs/worksheets.html'

def js_str(s):
    return json.dumps(s, ensure_ascii=False)

def build_problem(p):
    return ('{q:' + js_str(p['q']) +
            ',ex:' + js_str(p['ex']) +
            ',a:' + js_str(p['a']) +
            ',diff:' + js_str(p['diff']) + '}')

def build_topic(t):
    probs = '[' + ','.join(build_problem(p) for p in t['problems']) + ']'
    return '{title:' + js_str(t['title']) + ',problems:' + probs + '}'

def build_unit(unit_topics):
    return '[' + ','.join(build_topic(t) for t in unit_topics) + ']'

def build_units(units):
    return '[' + ','.join(build_unit(u) for u in units) + ']'

# ─── New content ──────────────────────────────────────────────────────────────

# G12 Science Unit 2 topic 6: Nuclear chemistry
NUCLEAR_TOPIC = {
    "title": "Nuclear Chemistry: Radioactive Decay, Half-Life, Fission vs. Fusion",
    "problems": [
        {"q": "What is radioactive decay and name the three main types.",
         "ex": "Think about what changes in the nucleus during each type.",
         "a": "Radioactive decay: unstable nuclei lose energy/particles to reach stability. Three types: Alpha (α) — emits helium nucleus (2p+2n), loses 4 mass, 2 atomic number. Beta (β) — neutron → proton + electron emitted, atomic number increases by 1. Gamma (γ) — high-energy photon emitted, no mass/charge change, often accompanies alpha/beta.",
         "diff": "medium"},
        {"q": "A sample has a half-life of 10 years. What fraction remains after 40 years?",
         "ex": "Apply: fraction = (1/2)^(t/t½)",
         "a": "40 years = 4 half-lives. Fraction remaining = (1/2)^4 = 1/16. If you started with 100g, 6.25g remains after 40 years.",
         "diff": "medium"},
        {"q": "Distinguish between nuclear fission and nuclear fusion.",
         "ex": "Which splits? Which combines? Where does energy come from in each?",
         "a": "Fission: a heavy nucleus (uranium-235, plutonium-239) splits into smaller nuclei + neutrons + energy. Used in nuclear reactors and bombs. Fusion: two light nuclei (hydrogen isotopes) combine to form a heavier nucleus + massive energy. Powers the sun. Fusion releases more energy per unit mass but requires extreme temperatures (millions °C) to overcome electrostatic repulsion — not yet practical for sustained power generation.",
         "diff": "medium"},
        {"q": "How is carbon-14 used to determine the age of organic materials?",
         "ex": "Think about the ratio of C-14 to C-12 and decay rate.",
         "a": "Living organisms continuously exchange carbon with the environment, maintaining a constant C-14/C-12 ratio. At death, C-14 decays (half-life 5,730 years) without replenishment. By measuring the remaining C-14/C-12 ratio and comparing to the living ratio, scientists calculate how many half-lives have passed and thus the age of the sample. Effective for materials up to ~50,000 years old.",
         "diff": "hard"},
        {"q": "What are practical applications and safety concerns of nuclear radiation?",
         "ex": "Think about medicine, energy, and exposure risks.",
         "a": "Applications: cancer treatment (radiation therapy targets tumors), medical imaging (PET scans use positron-emitting isotopes), nuclear power generation (fission heats water → steam → turbines). Safety concerns: ionizing radiation damages DNA, increasing cancer risk; long-lived radioactive waste requires thousands of years of safe storage; meltdowns (Chernobyl, Fukushima) can contaminate large areas. Shielding: alpha stopped by paper, beta by plastic/aluminum, gamma requires lead/concrete.",
         "diff": "medium"}
    ]
}

# G12 History Unit 3: Economics & Personal Finance
ECONOMICS_UNIT = [
    {"title": "Macroeconomics Fundamentals",
     "problems": [
         {"q": "What is GDP and what does it measure?",
          "ex": "GDP = C + I + G + (X−M)",
          "a": "GDP (Gross Domestic Product): total market value of all final goods and services produced within a country in a given year. Components: Consumer spending (C, ~70% of US GDP) + Investment by businesses (I) + Government spending (G) + Net exports (X−M). GDP measures economic output and is the primary indicator of a country's economic size and health.",
          "diff": "easy"},
         {"q": "Distinguish between inflation and deflation and explain their economic effects.",
          "ex": "Think about purchasing power and the price level.",
          "a": "Inflation: general rise in the price level — purchasing power of money decreases; debtors benefit (pay back cheaper dollars), creditors lose. Moderate inflation (~2%) is normal and targeted by the Fed. Deflation: general fall in prices — purchasing power rises but consumers delay purchases (expecting lower prices), causing economic slowdown. The Fed uses interest rate policy to target stable ~2% inflation. Hyperinflation (like Weimar Germany 1923) destroys economies.",
          "diff": "medium"},
         {"q": "What is the business cycle and name its four phases?",
          "ex": "Think about how GDP changes over time.",
          "a": "The business cycle: the recurring pattern of economic expansion and contraction. Four phases: (1) Expansion — GDP grows, unemployment falls, consumer spending rises; (2) Peak — maximum output, often overheating; (3) Contraction/Recession — GDP falls for 2+ consecutive quarters, unemployment rises; (4) Trough — lowest point, economy begins recovery. Governments use fiscal and monetary policy to moderate the cycle.",
          "diff": "medium"},
         {"q": "What is unemployment and distinguish between frictional, structural, and cyclical unemployment?",
          "ex": "Think about why each type occurs.",
          "a": "Frictional: temporary unemployment between jobs — workers searching for better fit (natural, healthy sign of labor market mobility). Structural: skills mismatch — workers' skills no longer match available jobs due to technological change or industry shifts (e.g., coal miners displaced by renewable energy). Cyclical: caused by economic downturns — demand falls, firms lay off workers. The 'natural rate' of unemployment includes frictional + structural (typically 4–5% in the US).",
          "diff": "medium"},
         {"q": "How does the Federal Reserve control the money supply and interest rates?",
          "ex": "Think about open market operations and the federal funds rate.",
          "a": "The Fed uses three tools: (1) Open market operations — buys/sells government securities; buying injects money into the system (expansionary), selling withdraws it (contractionary). (2) Federal funds rate — the target interest rate for overnight bank lending; lowering it stimulates borrowing and spending. (3) Reserve requirements — minimum fraction of deposits banks must hold. Post-2008, the Fed also uses quantitative easing (large-scale asset purchases) to stimulate the economy.",
          "diff": "hard"}
     ]},
    {"title": "Supply, Demand, and Markets",
     "problems": [
         {"q": "State the law of demand and explain why it holds.",
          "ex": "Think about price and quantity bought.",
          "a": "Law of demand: as price increases, quantity demanded decreases (inverse relationship), ceteris paribus. Reasons: (1) Substitution effect — higher price makes alternatives look more attractive; (2) Income effect — higher price reduces real purchasing power, so consumers buy less; (3) Diminishing marginal utility — each additional unit provides less satisfaction, so consumers only buy more at lower prices.",
          "diff": "easy"},
         {"q": "What shifts the demand curve vs. what causes movement along the demand curve?",
          "ex": "Think about price changes vs. non-price factors.",
          "a": "Movement along: only a change in the good's own price → quantity demanded changes (staying on same curve). Shift of the curve: non-price factors change the entire relationship — income (normal vs. inferior goods), prices of related goods (substitutes/complements), consumer tastes, expectations, number of buyers. Example: a price increase → movement along curve; rising consumer incomes → whole demand curve shifts right (for normal goods).",
          "diff": "medium"},
         {"q": "Calculate equilibrium: Qd = 120 − 2P and Qs = 3P − 30. What is the equilibrium price and quantity?",
          "ex": "Set Qd = Qs and solve for P, then find Q.",
          "a": "120 − 2P = 3P − 30 → 150 = 5P → P* = $30. Q* = 120 − 2(30) = 60. Equilibrium: price=$30, quantity=60 units.",
          "diff": "hard"},
         {"q": "What is price elasticity of demand and what factors determine it?",
          "ex": "PED = %ΔQd / %ΔP",
          "a": "Price elasticity of demand: measures how responsive quantity demanded is to a price change. PED = %ΔQd / %ΔP. |PED|>1: elastic (demand is sensitive). |PED|<1: inelastic. Determinants: (1) Availability of substitutes — more substitutes = more elastic; (2) Necessity vs. luxury — necessities are inelastic; (3) Budget share — larger share = more elastic; (4) Time horizon — more elastic in the long run as consumers adjust.",
          "diff": "medium"},
         {"q": "What is market failure and give two examples?",
          "ex": "Think about externalities and public goods.",
          "a": "Market failure: when free markets allocate resources inefficiently. Examples: (1) Externalities — costs/benefits not reflected in prices. Negative: factory pollution harms third parties not party to the transaction (overproduction). Positive: vaccination benefits society beyond the vaccinated person (underproduction). (2) Public goods — non-excludable and non-rival (national defense, lighthouses); free-rider problem leads to underprovision by private markets. (3) Information asymmetry — one party has more information (used cars, insurance).",
          "diff": "hard"}
     ]},
    {"title": "Personal Finance: Budgeting, Credit, and Investing",
     "problems": [
         {"q": "What is the 50/30/20 budgeting rule?",
          "ex": "Think about needs, wants, and savings.",
          "a": "50/30/20 rule: allocate after-tax income as follows — 50% to needs (rent, utilities, groceries, minimum debt payments); 30% to wants (entertainment, dining out, subscriptions, clothing beyond basics); 20% to savings and debt repayment (emergency fund, retirement contributions, extra debt payments). It's a guideline, not a rigid rule — adjust based on income level and financial goals.",
          "diff": "easy"},
         {"q": "What is compound interest and why is starting early so powerful for investing?",
          "ex": "A = P(1 + r/n)^(nt)",
          "a": "Compound interest: earning interest on interest. Formula: A = P(1+r/n)^(nt). Example: $1,000 at 7% annually for 30 years = $7,612. The same amount invested for 40 years = $14,974 — doubling by waiting just 10 more years. Starting at 22 vs. 32 can mean hundreds of thousands of dollars difference at retirement. The Rule of 72: divide 72 by annual rate to estimate years to double (72/7%≈10 years).",
          "diff": "medium"},
         {"q": "What factors make up a FICO credit score and why does it matter?",
          "ex": "Think about the five components.",
          "a": "FICO score (300–850): (1) Payment history 35% — on-time vs. late/missed payments; (2) Amounts owed 30% — credit utilization ratio (keep below 30%); (3) Length of credit history 15% — longer is better; (4) New credit 10% — recent hard inquiries; (5) Credit mix 10% — variety of credit types. Why it matters: determines loan approval and interest rates — a 760+ score vs. 620 score on a $300,000 mortgage could mean $100,000+ more in total interest paid.",
          "diff": "medium"},
         {"q": "Explain the difference between stocks, bonds, and index funds.",
          "ex": "Think about risk, return, and diversification.",
          "a": "Stocks: ownership shares in a company — potential for high returns but high volatility; can lose all value. Bonds: loans to governments/companies — fixed interest payments, lower risk, lower returns; return principal at maturity. Index funds: baskets of stocks that track a market index (S&P 500) — low cost, instant diversification, historically outperform most actively managed funds. Risk/return tradeoff: higher potential returns = higher risk. Diversification across asset classes reduces risk without proportionally reducing returns.",
          "diff": "medium"},
         {"q": "What is the difference between a Roth IRA and a Traditional IRA?",
          "ex": "Think about when taxes are paid.",
          "a": "Traditional IRA: contributions are tax-deductible (lower taxable income now); money grows tax-deferred; withdrawals in retirement are taxed as ordinary income. Best if you expect to be in a lower tax bracket in retirement. Roth IRA: contributions are after-tax (no deduction now); money grows tax-free; qualified withdrawals in retirement are completely tax-free. Best if you expect to be in a higher bracket in retirement or want tax-free income later. 2024 contribution limit: $7,000/year ($8,000 if 50+).",
          "diff": "hard"}
     ]},
    {"title": "Fiscal and Monetary Policy",
     "problems": [
         {"q": "What is the difference between expansionary and contractionary fiscal policy?",
          "ex": "Think about taxes, spending, and the business cycle.",
          "a": "Expansionary fiscal policy: used during recessions — increase government spending and/or cut taxes → stimulates aggregate demand → boosts GDP and employment. Contractionary: used during inflation — decrease spending and/or raise taxes → reduces demand → cools price pressures. The fiscal multiplier effect means a $1 change in government spending has a larger (multiplied) effect on GDP because of successive rounds of spending.",
          "diff": "medium"},
         {"q": "What is the national debt and how does it differ from the annual deficit?",
          "ex": "Think about the difference between a stock and a flow.",
          "a": "Annual deficit: when government spending exceeds revenue in a single year (flow). National debt: the cumulative total of all past annual deficits (stock) — money the government owes to creditors who hold Treasury bonds. The US national debt exceeds $33 trillion as of 2024. Deficits add to debt; surpluses (rare) reduce it. The debt-to-GDP ratio is a better measure of sustainability than the raw number.",
          "diff": "medium"},
         {"q": "What are automatic stabilizers and how do they work?",
          "ex": "Think about programs that automatically expand during recessions.",
          "a": "Automatic stabilizers: government programs that automatically increase spending (or decrease taxes) during economic downturns without requiring new legislation. Examples: unemployment insurance — automatically pays more when unemployment rises; food stamps/SNAP — enrollment expands in recessions; progressive income tax — tax revenue automatically falls when incomes fall, leaving more money in the private sector. They moderate the business cycle without political delays.",
          "diff": "hard"},
         {"q": "What is quantitative easing (QE) and when is it used?",
          "ex": "Think about what happens when interest rates are already near zero.",
          "a": "QE: when the central bank purchases large quantities of long-term assets (mortgage-backed securities, government bonds) from financial institutions, injecting money into the economy. Used when conventional monetary policy (lowering interest rates) is exhausted — the 'zero lower bound' problem. The Fed used QE extensively after the 2008 financial crisis and during COVID-19. Goal: lower long-term interest rates, encourage lending and investment. Criticized for potentially inflating asset prices and widening wealth inequality.",
          "diff": "hard"},
         {"q": "Compare capitalism, socialism, and mixed economies.",
          "ex": "Think about who owns the means of production and how resources are allocated.",
          "a": "Capitalism: private ownership of means of production; resources allocated through price signals and markets; profit motive drives innovation; minimal government role. Socialism: collective or government ownership of major industries; resources allocated by central planning or democratic decision; emphasizes equality. Mixed economy: combines elements of both — private markets for most goods, government provision/regulation of others (healthcare, education, infrastructure). All modern developed economies are mixed, varying in the balance.",
          "diff": "medium"}
     ]},
    {"title": "Global Trade and International Economics",
     "problems": [
         {"q": "What is comparative advantage and how does it justify international trade?",
          "ex": "Think about relative (not absolute) efficiency.",
          "a": "Comparative advantage: a country should produce goods for which it has the lowest opportunity cost, even if another country can produce everything more efficiently (absolute advantage). Example: if Country A gives up less to produce wheat than Country B, A should specialize in wheat; B in whatever it does at lower opportunity cost. Both benefit from trading because they consume beyond their production possibilities. This is the economic foundation for free trade.",
          "diff": "hard"},
         {"q": "What are tariffs and trade barriers and what are the arguments for and against them?",
          "ex": "Think about who benefits and who loses from protectionism.",
          "a": "Tariffs: taxes on imported goods — raise their price, protecting domestic producers. Other barriers: quotas, subsidies, regulations. Arguments for: protect infant industries, national security, retaliate against unfair practices, preserve jobs. Arguments against: raise prices for consumers, reduce efficiency (resources go to less competitive industries), invite retaliation (trade wars), reduce overall economic output. Economists generally favor free trade; politics often favors protectionism (concentrated benefits to domestic industries vs. dispersed costs to consumers).",
          "diff": "hard"},
         {"q": "What is the role of the World Trade Organization (WTO)?",
          "ex": "Think about rules-based international trade.",
          "a": "The WTO (est. 1995) is an international organization that: sets and enforces rules for international trade; provides a forum for trade negotiations; resolves trade disputes between member nations through a formal dispute settlement mechanism. The WTO operates on the principle of non-discrimination — most-favored-nation (MFN) status means concessions to one member extend to all. Member nations can challenge each other's trade barriers through WTO arbitration.",
          "diff": "medium"},
         {"q": "What causes currency exchange rates to fluctuate and how does this affect trade?",
          "ex": "Think about supply and demand for currency.",
          "a": "Exchange rates are determined by supply and demand for currencies, driven by: interest rate differentials (higher rates attract foreign capital → currency appreciates); inflation (high inflation erodes purchasing power → currency depreciates); trade balances (export demand → currency demand → appreciation); speculation and capital flows. Effects on trade: a stronger dollar makes US imports cheaper (consumers benefit) but US exports more expensive for foreign buyers (exporters hurt). A weak dollar does the reverse.",
          "diff": "hard"},
         {"q": "What is globalization and what are its main benefits and criticisms?",
          "ex": "Think about trade, investment, and inequality.",
          "a": "Globalization: the increasing integration of economies, cultures, and societies through trade, investment, migration, and technology. Benefits: economic growth, access to goods, poverty reduction in developing countries (hundreds of millions lifted from poverty), innovation diffusion. Criticisms: job displacement in developed economies (manufacturing to low-wage countries), suppression of labor/environmental standards in competition for investment, cultural homogenization, increased inequality within countries, vulnerability to global shocks (COVID supply chains).",
          "diff": "medium"}
     ]}
]

# ─── Patch helpers ────────────────────────────────────────────────────────────

def find_bracket_end(text, start):
    open_ch = text[start]
    close_ch = ']' if open_ch == '[' else '}'
    depth = 0
    i = start
    in_str = False
    escape = False
    while i < len(text):
        ch = text[i]
        if escape:
            escape = False
        elif ch == '\\' and in_str:
            escape = True
        elif ch == '"' and not escape:
            in_str = not in_str
        elif not in_str:
            if ch == open_ch:
                depth += 1
            elif ch == close_ch:
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return -1

def find_grade_subject_start(html, grade, subj):
    """Find the opening '[' of WORKSHEETS[grade][subj]."""
    ws_match = re.search(r'\bWORKSHEETS\s*=\s*\{', html)
    ws_brace = ws_match.end() - 1
    ws_end = find_bracket_end(html, ws_brace)
    ws_block = html[ws_brace:ws_end+1]

    grade_pattern = re.compile(r'["\']\s*' + re.escape(str(grade)) + r'\s*["\']\s*:\s*\{')
    gm = grade_pattern.search(ws_block)
    if not gm:
        print(f"Grade {grade} not found"); return None, None
    grade_brace_local = gm.end() - 1
    grade_end_local = find_bracket_end(ws_block, grade_brace_local)
    grade_block = ws_block[grade_brace_local:grade_end_local+1]

    subj_pattern = re.compile(r'["\']\s*' + re.escape(subj) + r'\s*["\']\s*:\s*\[')
    sm = subj_pattern.search(grade_block)
    if not sm:
        print(f"Subject {subj} not found in grade {grade}"); return None, None

    subj_bracket_local = sm.end() - 1
    subj_abs = ws_brace + (gm.start() + grade_brace_local) + subj_bracket_local
    # recompute absolute position properly
    grade_brace_abs = ws_brace + gm.end() - 1
    grade_block_abs = ws_brace + grade_brace_local  # this is wrong - let me fix
    # Correct approach: compute absolute positions
    grade_brace_abs2 = ws_brace + gm.end() - 1  # grade '{'
    grade_block_str = html[grade_brace_abs2: find_bracket_end(html, grade_brace_abs2)+1]
    sm2 = subj_pattern.search(grade_block_str)
    subj_bracket_abs = grade_brace_abs2 + sm2.end() - 1
    subj_end_abs = find_bracket_end(html, subj_bracket_abs)
    return subj_bracket_abs, subj_end_abs

def main():
    with open(PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    original_len = len(html)

    # ── Fix 1: G10 science — remove Unit 4 ────────────────────────────────────
    print("Fix 1: G10 science - removing extra Unit 4...")
    s_start, s_end = find_grade_subject_start(html, '10', 'science')
    if s_start is None:
        sys.exit(1)
    # s_start points to '[' of the units array
    # Parse the 4 units, keep only first 3
    units_str = html[s_start:s_end+1]
    # Find and collect unit bracket spans
    i = s_start + 1  # skip opening '['
    units = []
    while i < s_end:
        if html[i] == '[':
            end = find_bracket_end(html, i)
            units.append((i, end))
            i = end + 1
        else:
            i += 1
    print(f"  Found {len(units)} units in G10 science")
    if len(units) == 4:
        # Keep first 3 — rebuild the subject array
        kept = [html[u[0]:u[1]+1] for u in units[:3]]
        new_subj = '[' + ','.join(kept) + ']'
        html = html[:s_start] + new_subj + html[s_end+1:]
        print("  Removed Unit 4 ✓")
    else:
        print(f"  Expected 4 units, got {len(units)} — skipping")

    # ── Fix 2: G12 science Unit 2 — add 6th topic ─────────────────────────────
    print("Fix 2: G12 science Unit 2 - adding nuclear chemistry topic...")
    s_start, s_end = find_grade_subject_start(html, '12', 'science')
    if s_start is None:
        sys.exit(1)
    # Find Unit 2 (index 1)
    i = s_start + 1
    units = []
    while i < s_end:
        if html[i] == '[':
            end = find_bracket_end(html, i)
            units.append((i, end))
            i = end + 1
        else:
            i += 1
    print(f"  Found {len(units)} units in G12 science")
    unit2_start, unit2_end = units[1]
    # Add nuclear topic to the end of Unit 2
    new_topic_js = build_topic(NUCLEAR_TOPIC)
    # Insert before closing ']'
    new_unit2 = html[unit2_start:unit2_end] + ',' + new_topic_js + ']'
    html = html[:unit2_start] + new_unit2 + html[unit2_end+1:]
    print("  Added nuclear chemistry topic to G12 science Unit 2 ✓")

    # ── Fix 3: G12 history — insert Economics unit as Unit 3 ──────────────────
    print("Fix 3: G12 history - inserting Economics & Personal Finance unit...")
    s_start, s_end = find_grade_subject_start(html, '12', 'history')
    if s_start is None:
        sys.exit(1)
    i = s_start + 1
    units = []
    while i < s_end:
        if html[i] == '[':
            end = find_bracket_end(html, i)
            units.append((i, end))
            i = end + 1
        else:
            i += 1
    print(f"  Found {len(units)} units in G12 history")
    if len(units) == 3:
        # Insert economics as Unit 3 (before Unit 3/Philosophy which becomes Unit 4)
        econ_js = build_unit(ECONOMICS_UNIT)
        # Insert after Unit 2 (units[1])
        insert_pos = units[1][1] + 1  # right after Unit 2's ']'
        html = html[:insert_pos] + ',' + econ_js + html[insert_pos:]
        print("  Inserted Economics & Personal Finance as Unit 3 ✓")
    else:
        print(f"  Expected 3 units, got {len(units)} — skipping")

    with open(PATH, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\nDone! File size: {original_len:,} → {len(html):,} bytes")

if __name__ == '__main__':
    main()
