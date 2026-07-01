#!/usr/bin/env python3
"""
rebuild_ap_worksheets.py
Replaces the sparse AP section in WORKSHEETS with comprehensive coverage
matching the scope of regular grades (math, science, ela, history, cs, health).
"""
import json, re

BASE = '/sessions/admiring-stoic-pascal/mnt/outputs'

def make_unit(topics):
    """Wrap list of topic dicts into a unit (list)."""
    return topics

AP_WORKSHEETS_FULL = {
  "math": [
    # Unit 1: Limits & Continuity
    make_unit([
      {"title": "Understanding Limits",
       "problems": [
         {"q":"Evaluate lim(x→3) (x²−9)/(x−3).","ex":"Factor the numerator: x²−9=(x+3)(x−3).","a":"6","diff":"easy"},
         {"q":"Find lim(x→0) (sin x)/x.","ex":"This is a standard limit result.","a":"1","diff":"easy"},
         {"q":"Determine lim(x→∞) (4x²+3x)/(2x²−1).","ex":"Divide every term by x² (highest power).","a":"2","diff":"medium"},
         {"q":"Evaluate lim(x→2⁻) (x²−4)/(x−2) and lim(x→2⁺) (x²−4)/(x−2). Does the limit exist?","ex":"Factor numerator, then check if both one-sided limits agree.","a":"Both equal 4; limit = 4","diff":"medium"},
         {"q":"Find lim(x→0) (1−cos x)/x².","ex":"Use the identity 1−cos x = 2sin²(x/2) or L'Hôpital twice.","a":"1/2","diff":"hard"}
       ]},
      {"title": "Continuity and Discontinuities",
       "problems": [
         {"q":"Is f(x) = (x²−1)/(x−1) continuous at x=1? Explain.","ex":"Check all three continuity conditions.","a":"No; f(1) is undefined (0/0). It has a removable discontinuity at x=1.","diff":"easy"},
         {"q":"Classify the discontinuity of f(x)=1/x at x=0.","ex":"Consider left-hand and right-hand limits.","a":"Infinite (essential) discontinuity — left limit is −∞, right limit is +∞.","diff":"medium"},
         {"q":"Define k so that f(x) is continuous: f(x) = {kx+2 if x<3; x²−1 if x≥3}.","ex":"Set left-hand limit equal to f(3).","a":"3k+2=8 → k=2","diff":"hard"}
       ]}
    ]),
    # Unit 2: Derivatives — Rules
    make_unit([
      {"title": "Basic Differentiation Rules",
       "problems": [
         {"q":"Differentiate f(x)=5x³−3x²+7x−2.","ex":"Apply the power rule to each term.","a":"f′(x)=15x²−6x+7","diff":"easy"},
         {"q":"Find dy/dx for y=4√x − 3/x.","ex":"Rewrite as 4x^(1/2)−3x^(−1), then differentiate.","a":"dy/dx = 2x^(−1/2)+3x^(−2) = 2/√x + 3/x²","diff":"easy"},
         {"q":"Differentiate g(x)=(3x+1)(x²−5) using the product rule.","ex":"(uv)′=u′v+uv′","a":"g′(x)=3(x²−5)+(3x+1)(2x)=9x²+2x−15","diff":"medium"},
         {"q":"Find f′(x) for f(x)=sin²(x) using the chain rule.","ex":"f=u² where u=sin x; f′=2u·u′","a":"f′(x)=2sin x cos x = sin(2x)","diff":"medium"},
         {"q":"Differentiate h(x)=ln(x²+1).","ex":"Chain rule: d/dx[ln u] = u′/u","a":"h′(x)=2x/(x²+1)","diff":"medium"},
         {"q":"Find dy/dx using implicit differentiation: x²y+xy²=6.","ex":"Differentiate both sides w.r.t. x; remember d/dx[y]=dy/dx.","a":"dy/dx = −(2xy+y²)/(x²+2xy)","diff":"hard"}
       ]}
    ]),
    # Unit 3: Derivative Applications
    make_unit([
      {"title": "Curve Sketching & Optimization",
       "problems": [
         {"q":"Find all critical points of f(x)=x³−6x²+9x+1.","ex":"Set f′(x)=0 and solve.","a":"f′(x)=3x²−12x+9=3(x−1)(x−3)=0 → x=1 and x=3","diff":"easy"},
         {"q":"Determine whether x=1 is a local max or min for f(x)=x³−6x²+9x+1.","ex":"Use second derivative test or first derivative sign chart.","a":"f″(x)=6x−12; f″(1)=−6<0 → local maximum","diff":"medium"},
         {"q":"A rectangle has perimeter 40 cm. Find dimensions that maximize area.","ex":"Let width=w, length=20−w; maximize A=w(20−w).","a":"w=10; dimensions are 10×10 (square), max area=100 cm²","diff":"medium"},
         {"q":"A particle moves along x-axis with position s(t)=t³−6t²+9t. Find when it is at rest.","ex":"Set v(t)=s′(t)=0.","a":"v(t)=3t²−12t+9=0 → t=1 and t=3","diff":"medium"},
         {"q":"Using the Mean Value Theorem, verify there exists c in (0,2) where f′(c)=(f(2)−f(0))/(2−0) for f(x)=x³.","ex":"Compute the average rate of change, then find c.","a":"Average ROC = (8−0)/2=4; f′(c)=3c²=4 → c=√(4/3)=2/√3 ≈ 1.15 ∈ (0,2) ✓","diff":"hard"}
       ]}
    ]),
    # Unit 4: Integrals
    make_unit([
      {"title": "Antiderivatives and Definite Integrals",
       "problems": [
         {"q":"Find ∫(4x³−2x+5)dx.","ex":"Apply power rule in reverse to each term.","a":"x⁴−x²+5x+C","diff":"easy"},
         {"q":"Evaluate ∫[0,3] (2x+1)dx.","ex":"Find antiderivative F(x), then compute F(3)−F(0).","a":"F(x)=x²+x; F(3)−F(0)=12−0=12","diff":"easy"},
         {"q":"Use u-substitution to evaluate ∫2x(x²+1)⁴dx.","ex":"Let u=x²+1, du=2x dx.","a":"(x²+1)⁵/5+C","diff":"medium"},
         {"q":"Evaluate ∫sin(3x)dx.","ex":"Let u=3x, du=3dx.","a":"−cos(3x)/3+C","diff":"medium"},
         {"q":"Find the area under y=x² from x=0 to x=3.","ex":"Compute ∫[0,3] x²dx using FTC.","a":"∫[0,3] x²dx=[x³/3]₀³=9−0=9","diff":"medium"},
         {"q":"Evaluate ∫[1,e] (1/x)dx.","ex":"Antiderivative of 1/x is ln|x|.","a":"ln e − ln 1 = 1−0=1","diff":"easy"}
       ]}
    ]),
    # Unit 5: Statistics — Data & Distributions
    make_unit([
      {"title": "Descriptive Statistics",
       "problems": [
         {"q":"Find the mean, median, and mode of: 4, 7, 7, 9, 13.","ex":"Mean=sum/n; median=middle value; mode=most frequent.","a":"Mean=8; Median=7; Mode=7","diff":"easy"},
         {"q":"Calculate the standard deviation of {2, 4, 4, 4, 5, 5, 7, 9}.","ex":"Find mean, compute squared deviations, average them, take √.","a":"Mean=5; variance=4; SD=2","diff":"medium"},
         {"q":"A distribution has mean 50 and SD 10. What percent of data falls between 40 and 60?","ex":"Apply the empirical rule: mean ± 1 SD.","a":"~68% (one standard deviation on each side of the mean)","diff":"easy"},
         {"q":"Describe what a boxplot shows and identify its five-number summary components.","ex":"Think about minimum, quartiles, and maximum.","a":"Min, Q1 (25th percentile), Median (Q2), Q3 (75th percentile), Max. Box spans IQR=Q3−Q1.","diff":"medium"}
       ]},
      {"title": "Probability and Inference",
       "problems": [
         {"q":"A fair die is rolled. P(even or greater than 4) = ?","ex":"Outcomes: {1,2,3,4,5,6}; even={2,4,6}; >4={5,6}; union.","a":"P(even ∪ >4) = P(even)+P(>4)−P(both) = 3/6+2/6−1/6 = 4/6 = 2/3","diff":"medium"},
         {"q":"In a hypothesis test, the p-value is 0.02 and α=0.05. What do you conclude?","ex":"Compare p-value to α.","a":"Reject H₀; there is sufficient evidence against the null hypothesis at the 5% significance level.","diff":"easy"},
         {"q":"A 95% CI for a population mean is (23.1, 28.9). Interpret this interval.","ex":"Do NOT say 'probability' — use 'confidence'.","a":"We are 95% confident that the true population mean falls between 23.1 and 28.9.","diff":"medium"},
         {"q":"Two events A and B are independent with P(A)=0.4 and P(B)=0.5. Find P(A and B).","ex":"For independent events, P(A∩B)=P(A)·P(B).","a":"P(A∩B)=0.4×0.5=0.20","diff":"easy"}
       ]}
    ])
  ],

  "science": [
    # Unit 1: AP Biology — Cell & Molecular
    make_unit([
      {"title": "Cell Structure and Function",
       "problems": [
         {"q":"Describe two differences between prokaryotic and eukaryotic cells.","ex":"Consider nucleus, organelles, size.","a":"Eukaryotes have a membrane-bound nucleus and membrane-bound organelles (mitochondria, ER); prokaryotes lack these and are generally smaller.","diff":"easy"},
         {"q":"What is the function of the mitochondria and why are they called the 'powerhouse'?","ex":"Think ATP production.","a":"Mitochondria produce ATP via aerobic cellular respiration (Krebs cycle + electron transport chain), providing energy for cell functions.","diff":"easy"},
         {"q":"Explain how the structure of the cell membrane enables selective permeability.","ex":"Consider the phospholipid bilayer and embedded proteins.","a":"The hydrophobic lipid core blocks polar/charged molecules; channel and carrier proteins selectively transport specific molecules. Small nonpolar molecules diffuse freely.","diff":"medium"},
         {"q":"Compare passive transport and active transport.","ex":"Consider energy requirements and direction.","a":"Passive transport moves substances down their concentration gradient without energy (diffusion, osmosis, facilitated diffusion). Active transport moves substances against the gradient, requiring ATP.","diff":"medium"}
       ]},
      {"title": "DNA, RNA, and Protein Synthesis",
       "problems": [
         {"q":"Write the complementary mRNA strand for DNA template: 3′-TACGGATCC-5′","ex":"RNA uses U instead of T; complement A=U, T=A, G=C, C=G.","a":"5′-AUGCCUAGG-3′","diff":"easy"},
         {"q":"What amino acid does the codon AUG code for? What else does it signal?","ex":"AUG is the start codon.","a":"AUG codes for Methionine and serves as the start codon initiating translation.","diff":"easy"},
         {"q":"Explain how a mutation (substitution of one base) can be 'silent'.","ex":"Consider the redundancy of the genetic code.","a":"The genetic code is redundant — multiple codons code for the same amino acid. A base substitution may produce a synonymous codon, causing no amino acid change.","diff":"medium"},
         {"q":"Describe the role of tRNA in translation.","ex":"Think anticodon, amino acid attachment.","a":"tRNA carries a specific amino acid attached to its 3′ end. Its anticodon loop base-pairs with the complementary mRNA codon at the ribosome, delivering the correct amino acid for polypeptide assembly.","diff":"medium"}
       ]}
    ]),
    # Unit 2: AP Biology — Genetics & Evolution
    make_unit([
      {"title": "Mendelian Genetics",
       "problems": [
         {"q":"In a monohybrid cross between two Aa individuals, what fraction of offspring are homozygous recessive?","ex":"Set up a Punnett square.","a":"1/4 (25%): AA, Aa, Aa, aa → 1 out of 4 is aa.","diff":"easy"},
         {"q":"Two parents are both carriers (Aa) for a recessive disorder. What is the probability their child has the disorder?","ex":"Carriers are Aa; the disorder requires aa.","a":"25% (probability of aa = 1/4)","diff":"easy"},
         {"q":"In a dihybrid cross (AaBb × AaBb), what fraction of offspring show both dominant phenotypes?","ex":"Use the 9:3:3:1 rule.","a":"9/16","diff":"medium"},
         {"q":"Explain why sex-linked traits appear more often in males than females.","ex":"Consider X-linked recessive traits and X chromosome count.","a":"Males have only one X chromosome (XY), so a single recessive allele on X causes the trait. Females (XX) need two recessive alleles, making expression less likely.","diff":"medium"}
       ]},
      {"title": "Evolution and Natural Selection",
       "problems": [
         {"q":"List the four conditions required for natural selection to occur.","ex":"Darwin's key observations.","a":"(1) Variation in traits, (2) traits are heritable, (3) more offspring produced than survive, (4) differential reproductive success based on traits.","diff":"easy"},
         {"q":"A population of beetles has 80% green (dominant) and 20% brown. If p=0.8 (G frequency), find q and the frequency of each genotype (Hardy-Weinberg).","ex":"p+q=1; genotype frequencies: p², 2pq, q².","a":"q=0.2; GG=64%, Gg=32%, gg=4%","diff":"hard"},
         {"q":"What is genetic drift and when does it have the strongest effect?","ex":"Consider random changes in allele frequency.","a":"Genetic drift is random change in allele frequency due to chance events. It has the greatest effect in small populations where chance deviations from expected ratios have large proportional impact.","diff":"medium"}
       ]}
    ]),
    # Unit 3: AP Chemistry
    make_unit([
      {"title": "Atomic Structure and Periodicity",
       "problems": [
         {"q":"Write the ground-state electron configuration of Cl (Z=17).","ex":"Fill subshells in order: 1s, 2s, 2p, 3s, 3p.","a":"1s²2s²2p⁶3s²3p⁵","diff":"easy"},
         {"q":"Which has a larger atomic radius: Na or Cl? Explain.","ex":"Consider nuclear charge and electron shielding across a period.","a":"Na (sodium). Moving right across period 3, nuclear charge increases without adding a new shell, pulling electrons closer. Cl has more protons pulling the same shell tighter.","diff":"medium"},
         {"q":"Arrange in order of increasing first ionization energy: Na, Mg, Al, Si, P.","ex":"IE generally increases across a period, with exceptions at group 13 and 16.","a":"Na < Al < Mg < Si < P (Mg > Al due to full 3s²; P has extra stability from half-filled 3p)","diff":"hard"},
         {"q":"What is the de Broglie wavelength of an electron (m=9.11×10⁻³¹ kg) moving at 2×10⁶ m/s? (h=6.626×10⁻³⁴ J·s)","ex":"λ=h/(mv)","a":"λ=6.626×10⁻³⁴/(9.11×10⁻³¹×2×10⁶)≈3.6×10⁻¹⁰ m","diff":"hard"}
       ]},
      {"title": "Chemical Bonding and Molecular Geometry",
       "problems": [
         {"q":"Draw the Lewis structure for CO₂ and predict its molecular geometry.","ex":"C is central; count valence electrons: 4+6+6=16.","a":"O=C=O; linear geometry; 2 double bonds, no lone pairs on C.","diff":"easy"},
         {"q":"Using VSEPR theory, predict the shape of H₂O.","ex":"Count electron domains around O.","a":"O has 2 bonding pairs and 2 lone pairs → tetrahedral electron geometry → bent molecular shape, ~104.5°","diff":"medium"},
         {"q":"Explain why HF has a much higher boiling point than HCl despite smaller molar mass.","ex":"Consider intermolecular forces.","a":"HF forms hydrogen bonds (N,O,F can H-bond) which are much stronger than the dipole-dipole forces in HCl. More energy is needed to overcome H-bonds, raising boiling point.","diff":"medium"},
         {"q":"Identify the hybridization of carbon in CH₄, C₂H₄, and C₂H₂.","ex":"Count electron domains around each C atom.","a":"CH₄: sp³; C₂H₄: sp² (double bond); C₂H₂: sp (triple bond)","diff":"medium"}
       ]}
    ]),
    # Unit 4: AP Physics
    make_unit([
      {"title": "Kinematics and Newton's Laws",
       "problems": [
         {"q":"A car accelerates from 0 to 60 m/s in 8 seconds. Find acceleration and distance covered.","ex":"Use v=v₀+at and x=v₀t+½at².","a":"a=7.5 m/s²; x=0+½(7.5)(64)=240 m","diff":"easy"},
         {"q":"A 10 kg box is pulled at 30° above horizontal with force 50 N. Find the normal force (g=10 m/s²).","ex":"Resolve force into components; vertical equilibrium.","a":"F_y=50sin30°=25 N; N+25=mg=100 N → N=75 N","diff":"medium"},
         {"q":"Two blocks (5 kg and 3 kg) are connected by a string over a frictionless pulley. Find acceleration (g=10 m/s²).","ex":"Net force = (m₁−m₂)g; total mass = m₁+m₂ (Atwood machine).","a":"a=(5−3)×10/(5+3)=20/8=2.5 m/s²","diff":"medium"},
         {"q":"A projectile is launched at 45° with initial speed 20 m/s. Find range (g=10 m/s²).","ex":"Range R=v₀²sin(2θ)/g","a":"R=400×sin90°/10=40 m","diff":"medium"}
       ]},
      {"title": "Energy, Momentum, and Waves",
       "problems": [
         {"q":"A 2 kg ball dropped from 5 m. What is its speed just before impact? (g=10 m/s²)","ex":"Conservation of energy: mgh=½mv²","a":"v=√(2gh)=√(100)=10 m/s","diff":"easy"},
         {"q":"A 0.5 kg ball moving at 4 m/s collides with a stationary 1.5 kg ball. They stick together. Find final velocity.","ex":"Conservation of momentum: m₁v₁=(m₁+m₂)v_f","a":"v_f=(0.5×4)/(0.5+1.5)=2/2=1 m/s","diff":"medium"},
         {"q":"A wave has frequency 440 Hz and speed 343 m/s. Find wavelength.","ex":"v=fλ → λ=v/f","a":"λ=343/440≈0.78 m","diff":"easy"},
         {"q":"Explain the Doppler effect and give a real-world example.","ex":"Consider relative motion between source and observer.","a":"When a wave source moves toward an observer, observed frequency increases; moving away decreases it. Example: a police siren sounds higher-pitched as it approaches and lower as it recedes.","diff":"medium"}
       ]}
    ]),
    # Unit 5: AP Environmental Science
    make_unit([
      {"title": "Ecosystems and Earth Systems",
       "problems": [
         {"q":"Explain the difference between gross primary productivity (GPP) and net primary productivity (NPP).","ex":"Consider what producers use for their own respiration.","a":"GPP is the total rate of photosynthesis. NPP=GPP−plant respiration. NPP represents energy available to consumers.","diff":"medium"},
         {"q":"Describe the nitrogen cycle. Name two processes that convert N₂ to usable forms.","ex":"Think fixation, nitrification, denitrification.","a":"Nitrogen fixation (by bacteria or lightning) converts N₂ to NH₃/NH₄⁺. Nitrification converts NH₃ → NO₂⁻ → NO₃⁻. Denitrification returns nitrogen to the atmosphere as N₂.","diff":"hard"},
         {"q":"What is eutrophication? Describe the sequence of events leading to hypoxia.","ex":"Start with nutrient runoff.","a":"Excess nutrients (N,P from fertilizer runoff) → algal bloom → algae die → decomposers consume O₂ → hypoxic zone where most aquatic life cannot survive.","diff":"hard"},
         {"q":"Compare the greenhouse effect (natural) with the enhanced greenhouse effect (anthropogenic).","ex":"Consider the role of atmospheric CO₂.","a":"The natural greenhouse effect keeps Earth habitable (~33°C warming). The enhanced effect results from human-released CO₂, CH₄, and N₂O thickening the blanket of GHGs, causing additional warming beyond natural levels.","diff":"medium"}
       ]}
    ])
  ],

  "ela": [
    # Unit 1: AP Language — Rhetorical Analysis
    make_unit([
      {"title": "Analyzing Rhetorical Appeals",
       "problems": [
         {"q":"A speaker says: 'I've spent 15 years studying climate data, and the evidence is clear.' Identify and explain the rhetorical appeal used.","ex":"Which of ethos, pathos, logos?","a":"Ethos — the speaker establishes credibility through professional expertise ('15 years of study'), positioning themselves as a trustworthy authority on the subject.","diff":"easy"},
         {"q":"Identify the appeal in: 'Think of the children who will inherit a polluted world.' Explain how it functions.","ex":"How does it persuade?","a":"Pathos — appeals to parental instinct and fear for the future, creating emotional urgency that motivates the audience beyond rational argument.","diff":"easy"},
         {"q":"Analyze the rhetorical effect of including this statistic: 'Carbon emissions have risen 40% since 1990, with the last decade seeing the steepest increase on record.'","ex":"What is the effect on the argument?","a":"Logos — concrete, quantifiable data provides evidence that strengthens credibility and makes the argument harder to dismiss emotionally or anecdotally. The specificity (40%, 'last decade') signals rigorous sourcing.","diff":"medium"},
         {"q":"Explain how SOAPS is used to analyze a rhetorical situation.","ex":"Spell out what each letter stands for.","a":"S=Subject (what it's about), O=Occasion (context/event that prompted it), A=Audience (who it's for), P=Purpose (what it aims to achieve), S=Speaker (who created it and their credibility).","diff":"medium"}
       ]},
      {"title": "Argument and Synthesis",
       "problems": [
         {"q":"A classmate argues: 'Social media is harmful because my friends spend too much time on it.' Identify the logical weakness in this argument.","ex":"Consider what type of evidence this is.","a":"Anecdotal evidence / hasty generalization — personal observation from a small, unrepresentative sample cannot justify a broad claim about social media's general harmfulness.","diff":"medium"},
         {"q":"Write a 2-3 sentence thesis for an essay arguing standardized testing should be eliminated in public schools.","ex":"Include a claim and two to three lines of reasoning.","a":"Example: Standardized testing should be eliminated from public schools because it narrows curriculum to test-preparation, systematically disadvantages students from lower-income backgrounds, and fails to measure the higher-order thinking skills essential for 21st-century success.","diff":"medium"},
         {"q":"Explain how to integrate a source into an argument without just 'quote-dropping'.","ex":"What must surround the quote?","a":"Introduce the source (author, title, context), provide the quote or paraphrase, then explain how it supports your claim (analysis). The quote should never be the first or last sentence of a paragraph.","diff":"medium"},
         {"q":"What is the difference between a concession and a refutation in argumentation?","ex":"Both address opposing views.","a":"A concession acknowledges that the opposing side has a valid point. A refutation then explains why your position still stands — either by limiting the concession's scope or providing stronger counter-evidence.","diff":"easy"}
       ]}
    ]),
    # Unit 2: AP Language — Style and Composition
    make_unit([
      {"title": "Diction, Syntax, and Tone",
       "problems": [
         {"q":"Identify the tone shift in this passage and what device creates it: 'The war hero returned home to confetti and cheers. Two years later, he slept on a park bench, forgotten.'","ex":"What changes and what device is used?","a":"Tone shifts from celebratory/triumphant to bleak/ironic. Juxtaposition and contrast create this shift, emphasizing the neglect of veterans after their service ends.","diff":"medium"},
         {"q":"Rewrite this sentence to increase formal register without changing meaning: 'The policy is gonna mess up a lot of people's lives.'","ex":"Adjust vocabulary and syntax for academic/formal context.","a":"Example: 'This policy will have significantly detrimental effects on a substantial portion of the affected population.'","diff":"easy"},
         {"q":"Explain the effect of short, declarative sentences versus long, subordinate-heavy sentences in a persuasive text.","ex":"Consider pacing, emphasis, and audience impact.","a":"Short declarative sentences create urgency, emphasis, and a confident tone — each claim stands alone. Long complex sentences suggest nuance, qualification, and careful reasoning. Effective writers vary sentence structure for rhythm and to signal which ideas are central vs. supporting.","diff":"medium"},
         {"q":"Identify the rhetorical device and explain its effect: 'We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields...' (Churchill)","ex":"Look for repetition of structure.","a":"Anaphora — the repetition of 'we shall fight' at the start of each clause creates a rhythmic crescendo that builds resolve and unity, making the commitment feel absolute and collective.","diff":"medium"}
       ]}
    ]),
    # Unit 3: AP Literature — Poetry and Fiction
    make_unit([
      {"title": "Poetry Analysis",
       "problems": [
         {"q":"What is a volta in a sonnet, and where does it typically appear in a Petrarchan vs. Shakespearean sonnet?","ex":"Consider the 14-line structure of each type.","a":"A volta is a shift in argument, tone, or perspective. In Petrarchan sonnets it typically occurs at line 9 (between octave and sestet). In Shakespearean sonnets it often appears at the final couplet (line 13).","diff":"medium"},
         {"q":"Identify the figurative language: 'Hope is the thing with feathers / That perches in the soul' (Dickinson).","ex":"What is hope being compared to?","a":"Extended metaphor (or metaphorical conceit) — hope is compared to a bird throughout the poem. 'Feathers' and 'perches' are the vehicle; the tenor is the persistent, uplifting quality of hope.","diff":"easy"},
         {"q":"A poem has the rhyme scheme ABAB CDCD EFEF GG. What form is this and what does the final GG typically do?","ex":"Count lines and identify the pattern.","a":"Shakespearean sonnet (14 lines, 3 quatrains + couplet). The final GG (couplet) typically delivers the volta — a resolution, ironic twist, or summary of the preceding argument.","diff":"easy"},
         {"q":"Explain how enjambment differs from end-stopped lines and what effect each creates.","ex":"Consider how meaning flows across lines.","a":"End-stopped lines pause at the line break (punctuation), creating emphasis and finality. Enjambment runs sentences across line breaks, creating momentum, suspense, or mimicking natural speech — and can create double meanings at the break point.","diff":"medium"}
       ]},
      {"title": "Fiction and Drama Analysis",
       "problems": [
         {"q":"What is a 'foil' character? Give an example from classic literature.","ex":"Consider character contrasts.","a":"A foil is a character whose contrasting traits highlight the qualities of another character. Example: Laertes in Hamlet foils Hamlet — both have murdered fathers, but Laertes acts impulsively while Hamlet agonizes, highlighting Hamlet's philosophical paralysis.","diff":"easy"},
         {"q":"Explain the significance of an 'unreliable narrator' and give one reason a reader should approach such narrators skeptically.","ex":"Consider The Tell-Tale Heart or Gone Girl.","a":"An unreliable narrator's account cannot be fully trusted due to psychological instability, bias, limited knowledge, or deliberate deception. Readers must read 'between the lines' to reconstruct a more objective version of events.","diff":"medium"},
         {"q":"What is dramatic irony and how does it affect the reader/audience?","ex":"Think about the gap between audience and character knowledge.","a":"Dramatic irony occurs when the audience knows something a character does not. It creates tension, suspense, or dark comedy, and engages the audience emotionally — they may feel dread, sympathy, or frustration watching characters act on incomplete information.","diff":"easy"},
         {"q":"Analyze how setting functions as more than backdrop in Gothic fiction.","ex":"Think about atmosphere and symbolism.","a":"In Gothic fiction, setting (decaying mansions, storms, isolated moors) externalizes characters' psychological states, creates atmosphere of dread, and often functions symbolically — e.g., the crumbling house mirrors the protagonist's fractured mind.","diff":"hard"}
       ]}
    ])
  ],

  "history": [
    # Unit 1: AP US History
    make_unit([
      {"title": "Colonial America and the Founding",
       "problems": [
         {"q":"Explain one economic and one political cause of the American Revolution.","ex":"Consider mercantilism and taxation without representation.","a":"Economic: British mercantilism and taxes (Stamp Act, Townshend Acts) drained colonial wealth. Political: colonists had no representation in Parliament, violating their tradition of self-governance through colonial assemblies.","diff":"medium"},
         {"q":"How did Enlightenment ideas influence the Declaration of Independence?","ex":"Think Locke, natural rights.","a":"Jefferson drew heavily on Locke's concept of natural rights (life, liberty, property → pursuit of happiness) and the social contract — that government derives legitimacy from the consent of the governed and may be overthrown when it violates rights.","diff":"medium"},
         {"q":"What were the major weaknesses of the Articles of Confederation?","ex":"Think about central government power.","a":"No power to tax or regulate commerce; no national currency; no executive or judiciary; amendments required unanimous consent; states often ignored Congress. This led to Shays' Rebellion and ultimately the Constitutional Convention.","diff":"easy"},
         {"q":"Compare the Federalist and Anti-Federalist positions on ratifying the Constitution.","ex":"Consider size of government, rights, power distribution.","a":"Federalists (Hamilton, Madison, Jay) argued the Constitution created necessary strong central government with adequate checks and balances. Anti-Federalists (Patrick Henry) feared tyranny, lack of a Bill of Rights, and loss of state sovereignty.","diff":"hard"}
       ]},
      {"title": "Civil War and Reconstruction",
       "problems": [
         {"q":"How did the Kansas-Nebraska Act (1854) reignite the slavery debate?","ex":"Consider popular sovereignty and the Missouri Compromise.","a":"It repealed the Missouri Compromise's prohibition on slavery above 36°30′N and introduced popular sovereignty, allowing residents to vote on slavery. 'Bleeding Kansas' — violent clashes between pro- and anti-slavery settlers — demonstrated the irreconcilability of the conflict.","diff":"medium"},
         {"q":"What were the 13th, 14th, and 15th Amendments and what did each accomplish?","ex":"These are the Reconstruction Amendments.","a":"13th: abolished slavery; 14th: guaranteed citizenship and equal protection to all persons born in US; 15th: prohibited denying vote based on race, color, or previous servitude.","diff":"easy"},
         {"q":"Why did Reconstruction ultimately fail to secure lasting rights for Black Americans?","ex":"Consider political compromises and resistance.","a":"The Compromise of 1877 withdrew federal troops from the South. Without enforcement, Southern states implemented Black Codes and later Jim Crow laws, disenfranchisement (poll taxes, literacy tests), and terror via groups like the KKK undermined the Reconstruction amendments.","diff":"hard"}
       ]}
    ]),
    # Unit 2: AP World History
    make_unit([
      {"title": "Trade Networks and Cultural Exchange",
       "problems": [
         {"q":"Explain two ways the Silk Road facilitated cultural exchange beyond trade in goods.","ex":"Think religion, disease, technology.","a":"Buddhism spread from India to East Asia along Silk Road merchants' routes. The bubonic plague (Black Death) traveled westward via trade routes. Technologies like papermaking and gunpowder also diffused.","diff":"medium"},
         {"q":"Compare the role of the Indian Ocean trade network with the Silk Road in connecting the pre-modern world.","ex":"Consider geography, goods, and participants.","a":"Indian Ocean trade used monsoon winds to link East Africa, Arabia, India, and Southeast Asia, primarily by sea. It facilitated spread of Islam and spice trade. The Silk Road was overland and maritime, connecting China to the Mediterranean. Both networks spread religion, disease, and ideas, but Indian Ocean trade relied more on seasonal wind patterns and dhow ships.","diff":"hard"},
         {"q":"What was the Columbian Exchange and what were its most significant consequences?","ex":"Consider both hemispheres.","a":"The Columbian Exchange was the transfer of plants, animals, diseases, and ideas between the Americas and Afro-Eurasia after 1492. Old World diseases (smallpox, measles) devastated Indigenous American populations. New World crops (potato, maize) dramatically increased food supply in Europe and Asia, contributing to population growth.","diff":"medium"}
       ]},
      {"title": "Industrialization and Imperialism",
       "problems": [
         {"q":"Why did industrialization begin in Britain rather than elsewhere?","ex":"Consider geography, resources, government, and markets.","a":"Britain had: abundant coal and iron; a colonial empire providing raw materials and markets; a stable government with property rights; an agricultural revolution that freed labor; and geographic advantages (navigable rivers, coastal access). Additionally, the enclosure movement pushed rural workers into urban factories.","diff":"hard"},
         {"q":"Explain the 'White Man's Burden' ideology and how it was used to justify imperialism.","ex":"Consider Kipling's poem and social Darwinism.","a":"Rudyard Kipling's poem framed colonization as a moral duty — 'civilizing' non-European peoples. Combined with Social Darwinism (applying 'survival of the fittest' to races/nations), Western powers justified political, economic, and cultural domination as benevolent and natural rather than exploitative.","diff":"medium"},
         {"q":"Compare economic and humanitarian motivations for 19th-century European imperialism.","ex":"What did colonizers officially say vs. what did they actually do?","a":"Official justification included spreading Christianity, civilization, and 'progress.' Actual primary motivations were economic: raw materials (rubber, cotton, ivory), new markets for manufactured goods, investment opportunities, and geostrategic advantages. Humanitarian claims often masked exploitative extraction economies.","diff":"hard"}
       ]}
    ]),
    # Unit 3: AP Government
    make_unit([
      {"title": "Constitutional Structure and Federalism",
       "problems": [
         {"q":"Explain the significance of Marbury v. Madison (1803).","ex":"What power did it establish?","a":"Marbury v. Madison established the principle of judicial review — the Supreme Court's authority to declare acts of Congress unconstitutional. Chief Justice Marshall ruled the Judiciary Act of 1789 partially unconstitutional, giving the Court power to strike down laws that conflict with the Constitution.","diff":"easy"},
         {"q":"Distinguish between enumerated powers and implied powers.","ex":"Consider Articles I and the elastic clause.","a":"Enumerated (expressed) powers are explicitly listed in the Constitution (e.g., declare war, coin money). Implied powers derive from the Necessary and Proper Clause (elastic clause), allowing Congress to exercise powers not explicitly listed if necessary to carry out enumerated powers.","diff":"medium"},
         {"q":"What is fiscal federalism and how do categorical grants differ from block grants?","ex":"Consider how the federal government influences states.","a":"Fiscal federalism refers to federal funding to states with conditions attached. Categorical grants fund specific programs with strict requirements (e.g., Head Start). Block grants give states lump sums with broad purposes and fewer restrictions, giving states more discretion.","diff":"hard"}
       ]},
      {"title": "Civil Liberties and Civil Rights",
       "problems": [
         {"q":"What is selective incorporation? Give an example.","ex":"How does the 14th Amendment apply the Bill of Rights to states?","a":"Selective incorporation is the process by which the Supreme Court has applied specific provisions of the Bill of Rights to state governments via the 14th Amendment's Due Process Clause. Example: Mapp v. Ohio (1961) incorporated the 4th Amendment's exclusionary rule to the states.","diff":"hard"},
         {"q":"Explain the significance of Brown v. Board of Education (1954).","ex":"What did it overturn and what standard did it establish?","a":"Brown unanimously overturned Plessy v. Ferguson's 'separate but equal' doctrine, ruling that racially segregated public schools violated the 14th Amendment's Equal Protection Clause. It declared that separate facilities are inherently unequal, providing the constitutional foundation for the civil rights movement.","diff":"medium"},
         {"q":"What 'clear and present danger' test did Schenck v. US establish for First Amendment speech?","ex":"Consider limits on free speech during wartime.","a":"Schenck v. US (1919) held that free speech could be restricted if it poses a 'clear and present danger' of producing substantive evils. Holmes used the example: falsely shouting fire in a crowded theater. Context (e.g., wartime) could make otherwise protected speech punishable.","diff":"hard"}
       ]}
    ]),
    # Unit 4: AP Psychology
    make_unit([
      {"title": "Biological Bases of Behavior",
       "problems": [
         {"q":"Trace the path of a neural signal from a sensory receptor to a muscle response.","ex":"Consider receptor → sensory neuron → CNS → motor neuron → effector.","a":"Sensory receptor detects stimulus → sensory neuron carries signal to spinal cord/brain → interneurons process signal → motor neuron carries signal to muscle → muscle contracts (effector response).","diff":"medium"},
         {"q":"Compare the functions of the sympathetic and parasympathetic nervous systems.","ex":"Think fight-or-flight vs. rest-and-digest.","a":"Sympathetic ('fight-or-flight'): increases heart rate, dilates pupils, slows digestion, releases adrenaline. Parasympathetic ('rest-and-digest'): decreases heart rate, constricts pupils, promotes digestion, promotes relaxation. They are complementary systems.","diff":"easy"},
         {"q":"What are neurotransmitters? Name two and describe their functions.","ex":"Chemical messengers in synapses.","a":"Neurotransmitters are chemical messengers that cross the synapse to transmit signals between neurons. Dopamine: involved in reward, motivation, and movement (deficiency linked to Parkinson's; excess linked to schizophrenia). Serotonin: regulates mood, sleep, and appetite (low levels associated with depression).","diff":"easy"}
       ]},
      {"title": "Cognition, Learning, and Development",
       "problems": [
         {"q":"Explain Piaget's concept of 'schema' and how 'assimilation' differs from 'accommodation'.","ex":"How do we process new information?","a":"A schema is a mental framework for understanding the world. Assimilation: fitting new information into an existing schema (e.g., calling all round objects 'ball'). Accommodation: modifying a schema when new information doesn't fit (e.g., learning that a 'balloon' is different from a 'ball').","diff":"medium"},
         {"q":"What is the difference between negative reinforcement and punishment? (A common misconception)","ex":"Both involve unpleasant stimuli — but how do they affect behavior?","a":"Negative reinforcement: removing an aversive stimulus INCREASES behavior (e.g., taking aspirin relieves headache → you take aspirin more often). Punishment: adding an aversive stimulus or removing a pleasant one DECREASES behavior. Both 'negative' doesn't mean punishment!","diff":"medium"},
         {"q":"Describe the serial position effect in memory and its two components.","ex":"Think about which items in a list are best remembered.","a":"The serial position effect is the tendency to remember the first and last items in a list best. The primacy effect (remembering first items) is due to long-term memory encoding. The recency effect (remembering last items) is due to items still in working memory at recall.","diff":"medium"}
       ]}
    ]),
    # Unit 5: AP Economics
    make_unit([
      {"title": "Supply, Demand, and Market Equilibrium",
       "problems": [
         {"q":"A new study shows coffee reduces heart disease risk. Predict the effect on the coffee market using supply and demand.","ex":"Which curve shifts? In which direction? What happens to price and quantity?","a":"Demand for coffee increases (shifts right). Assuming supply is unchanged, equilibrium price and quantity both increase.","diff":"easy"},
         {"q":"Explain why a perfectly competitive firm is a 'price taker'.","ex":"Consider market structure and firm's market power.","a":"In perfect competition, many firms sell identical products and each is too small to influence market price. If a firm raises its price above market price, consumers buy from competitors. So each firm must accept the market price — making them price takers.","diff":"medium"},
         {"q":"Calculate the price elasticity of demand if quantity falls from 200 to 160 units when price rises from $10 to $12.","ex":"PED = (% change in Qd) / (% change in P)","a":"%ΔQ = (160−200)/200 = −20%; %ΔP = (12−10)/10 = 20%; PED = −20%/20% = −1. Demand is unit elastic.","diff":"hard"}
       ]}
    ])
  ],

  "cs": [
    # Unit 1: AP CS A — Java
    make_unit([
      {"title": "Java Fundamentals and OOP",
       "problems": [
         {"q":"What is the output of: int x=10; int y=3; System.out.println(x/y + ' ' + x%y);","ex":"Java integer division truncates; % is remainder.","a":"3 1 (10/3=3 truncated; 10%3=1)","diff":"easy"},
         {"q":"Write a Java class 'Circle' with a double field 'radius', a constructor, and a method 'getArea()' returning the area.","ex":"Area = π × r²; use Math.PI.","a":"public class Circle { double radius; Circle(double r){radius=r;} double getArea(){return Math.PI*radius*radius;} }","diff":"medium"},
         {"q":"Explain the difference between '==' and '.equals()' when comparing Strings in Java.","ex":"Consider reference vs. value comparison.","a":"'==' compares references (memory addresses) — whether two variables point to the same object. '.equals()' compares the content (character sequence) of strings. Use '.equals()' for string value comparison.","diff":"medium"},
         {"q":"What is the purpose of the 'super' keyword in Java inheritance?","ex":"Think about subclass accessing parent.","a":"'super' refers to the parent class. 'super()' calls the parent constructor. 'super.methodName()' calls an overridden parent method from within the subclass, enabling access to parent functionality the subclass has overridden.","diff":"medium"}
       ]},
      {"title": "Arrays, ArrayLists, and Algorithms",
       "problems": [
         {"q":"Trace through bubble sort on array {5,2,8,1}. Show each pass.","ex":"Compare adjacent elements, swap if out of order.","a":"Pass 1: {2,5,1,8}→wait: {2,5,1,8}; compare 5,8 no swap; {2,1,5,8} after full pass 1: {2,1,5,8}. Full trace: P1:{2,1,5,8}, P2:{1,2,5,8}, P3:{1,2,5,8} (done)","diff":"hard"},
         {"q":"Write a Java method that returns the sum of all elements in an int array.","ex":"Use a for-each loop.","a":"int sum(int[] arr){ int s=0; for(int x:arr) s+=x; return s; }","diff":"easy"},
         {"q":"What is the time complexity of binary search vs. linear search on an array of n elements?","ex":"How many comparisons in the worst case?","a":"Linear search: O(n) — checks each element. Binary search: O(log n) — halves the search space each step, but requires the array to be sorted.","diff":"easy"},
         {"q":"Explain what 'ArrayIndexOutOfBoundsException' means and how to prevent it.","ex":"Consider valid array indices.","a":"It occurs when code tries to access an index outside the valid range (0 to array.length−1). Prevent by ensuring loop bounds use array.length correctly, e.g., for(int i=0; i<arr.length; i++) rather than i<=arr.length.","diff":"easy"}
       ]}
    ]),
    # Unit 2: AP CS Principles
    make_unit([
      {"title": "Data, Internet, and Algorithms",
       "problems": [
         {"q":"Convert the binary number 10110 to decimal.","ex":"Each bit represents a power of 2, right to left.","a":"0×1 + 1×2 + 1×4 + 0×8 + 1×16 = 0+2+4+0+16 = 22","diff":"easy"},
         {"q":"What is the difference between the internet and the World Wide Web?","ex":"Consider infrastructure vs. application.","a":"The internet is the global physical infrastructure of interconnected networks (routers, cables, protocols like TCP/IP). The World Wide Web is an application built on top of the internet — a system of interlinked hypertext documents accessed via browsers using HTTP.","diff":"easy"},
         {"q":"Describe how public-key (asymmetric) encryption works for secure communication.","ex":"Consider the roles of the public and private keys.","a":"The recipient has a public key (shared openly) and a private key (secret). The sender encrypts a message with the recipient's public key. Only the recipient's private key can decrypt it. This allows secure communication without needing to share a secret key in advance.","diff":"medium"},
         {"q":"Explain why sorting a list is classified as O(n log n) for efficient algorithms and why that matters.","ex":"Compare to O(n²) bubble sort.","a":"Efficient sorts (merge sort, quicksort average case) use divide-and-conquer to split lists into halves, reducing comparisons. For 1,000,000 items: O(n²)=10¹² operations; O(n log n)≈20,000,000 — a massive practical difference. This makes fast sorts essential for large datasets.","diff":"hard"}
       ]},
      {"title": "Programming Concepts and Impact",
       "problems": [
         {"q":"What is an 'abstraction' in programming? Give an example.","ex":"Think about hiding complexity.","a":"Abstraction hides implementation details behind a simpler interface. Example: when you call print() in Python, you don't need to know how the OS converts bytes to pixels on screen — the function abstracts that complexity, letting you focus on what you want (print text), not how it works.","diff":"easy"},
         {"q":"Describe a beneficial and a harmful societal impact of artificial intelligence.","ex":"Think broadly — jobs, bias, healthcare, privacy.","a":"Beneficial: AI-powered medical imaging detects cancers earlier than human radiologists, saving lives. Harmful: algorithmic bias in hiring or lending systems can perpetuate racial and gender discrimination at scale, with less transparency than human decision-making.","diff":"medium"},
         {"q":"What is 'crowdsourcing' in computing, and give an example of a project that uses it.","ex":"Think about distributed effort across many users.","a":"Crowdsourcing distributes a task among a large group, often online. Example: Wikipedia — millions of volunteer contributors collaboratively create and edit articles. SETI@home used volunteers' idle computers to analyze radio telescope data for signs of extraterrestrial intelligence.","diff":"easy"}
       ]}
    ])
  ],

  "health": [
    # Unit 1: AP Psychology — Mental Health
    make_unit([
      {"title": "Mental Health and Psychological Disorders",
       "problems": [
         {"q":"According to the DSM-5, what three criteria must be met for a behavior to be considered a psychological disorder?","ex":"Think about distress, dysfunction, and deviance.","a":"(1) Deviance — behavior differs significantly from societal norms; (2) Distress — causes significant personal suffering; (3) Dysfunction — interferes with daily functioning. Some add 'danger' (risk of harm to self or others) as a fourth criterion.","diff":"medium"},
         {"q":"Distinguish between major depressive disorder and bipolar disorder.","ex":"Consider the range of mood states.","a":"Major depressive disorder involves persistent depressive episodes (sadness, hopelessness, loss of interest, fatigue). Bipolar disorder involves cycles between depressive episodes and manic episodes (elevated mood, decreased sleep, grandiosity, impulsivity). Bipolar requires at least one manic episode.","diff":"medium"},
         {"q":"Explain the biopsychosocial model of mental health.","ex":"Why is it considered more complete than purely biological or psychological models?","a":"The biopsychosocial model holds that mental health is determined by three interacting factors: biological (genetics, brain chemistry, neurological factors), psychological (thoughts, emotions, behavior patterns), and social (relationships, culture, socioeconomic status, trauma). It's more complete because it recognizes no single factor fully explains mental illness.","diff":"medium"},
         {"q":"What is cognitive-behavioral therapy (CBT) and for what disorders is it most evidence-based?","ex":"Think about thoughts, behaviors, and their interaction.","a":"CBT is a therapy that identifies and restructures maladaptive thought patterns and behaviors. It holds that distorted thinking leads to negative emotions and behaviors — changing thoughts changes feelings. Most evidence-based for: depression, anxiety disorders, PTSD, OCD, eating disorders, and insomnia.","diff":"medium"}
       ]},
      {"title": "Stress, Coping, and Health Psychology",
       "problems": [
         {"q":"Describe Selye's General Adaptation Syndrome (GAS) and its three stages.","ex":"How does the body respond to chronic stress?","a":"GAS describes the body's response to chronic stressors: (1) Alarm — fight-or-flight activation (adrenaline release); (2) Resistance — body adapts, stress hormones normalize, coping continues; (3) Exhaustion — prolonged stress depletes resources, increasing vulnerability to illness and breakdown.","diff":"medium"},
         {"q":"What is the difference between problem-focused and emotion-focused coping? Give an example of each.","ex":"How do they each address stress?","a":"Problem-focused coping addresses the source of stress directly (e.g., studying more before an exam). Emotion-focused coping manages the emotional response (e.g., meditating or talking to a friend). Both are adaptive; emotion-focused is most useful when the stressor cannot be changed.","diff":"easy"},
         {"q":"Explain how chronic stress affects the immune system.","ex":"Consider cortisol and its long-term effects.","a":"Chronic stress leads to sustained cortisol release. While cortisol temporarily suppresses immune function to prioritize fight-or-flight, prolonged elevation suppresses immune responses, reducing the body's ability to fight pathogens. This explains why chronically stressed people are more susceptible to colds and infections.","diff":"hard"}
       ]}
    ]),
    # Unit 2: AP Biology — Human Body Systems
    make_unit([
      {"title": "Homeostasis and Body Systems",
       "problems": [
         {"q":"Define homeostasis and give an example of a negative feedback loop in the human body.","ex":"Think body temperature or blood glucose.","a":"Homeostasis is the maintenance of a stable internal environment. Example: blood glucose regulation — when glucose rises after eating, the pancreas releases insulin, which signals cells to absorb glucose; when glucose falls too low, glucagon triggers glycogen breakdown, restoring equilibrium.","diff":"easy"},
         {"q":"Compare the roles of the nervous system and endocrine system in maintaining homeostasis.","ex":"Consider speed, specificity, and duration.","a":"The nervous system uses electrical signals and neurotransmitters — fast (milliseconds), specific (targets individual cells), short-duration. The endocrine system uses hormones in the bloodstream — slower (seconds to hours), broad targets (many cells), longer-lasting effects.","diff":"medium"},
         {"q":"Explain how vaccinations use the immune system's memory to prevent disease.","ex":"Think about B cells, antibodies, and memory cells.","a":"Vaccines introduce antigens (weakened/inactivated pathogen or antigen fragments). The immune system mounts a primary response, producing antibodies and memory B cells. If the actual pathogen is later encountered, memory cells enable a rapid, stronger secondary response, neutralizing the pathogen before symptoms develop.","diff":"medium"},
         {"q":"Describe one way the digestive system and circulatory system work together.","ex":"Think about nutrient absorption.","a":"The digestive system breaks food into nutrients (glucose, amino acids, fatty acids). The small intestine absorbs these into the bloodstream via capillaries. The circulatory system then distributes nutrients to all body cells, linking digestion to cellular metabolism.","diff":"easy"}
       ]}
    ]),
    # Unit 3: Social and Environmental Health
    make_unit([
      {"title": "Public Health and Environmental Factors",
       "problems": [
         {"q":"What is the social determinants of health framework, and name three social determinants.","ex":"Think beyond individual behavior.","a":"Social determinants of health are non-medical factors shaping health outcomes: where people are born, live, work, and age. Examples: (1) income and economic stability, (2) access to education and literacy, (3) access to healthcare, neighborhood safety, food security.","diff":"medium"},
         {"q":"Explain how air pollution affects respiratory and cardiovascular health.","ex":"Consider particulate matter and ozone.","a":"Fine particulate matter (PM2.5) penetrates deep into lungs, causing inflammation, reducing lung function, and triggering asthma. Ozone irritates airways. Long-term exposure increases risk of chronic obstructive pulmonary disease (COPD) and cardiovascular disease, as particles enter the bloodstream and cause systemic inflammation.","diff":"medium"},
         {"q":"What is the epidemiological triangle and how does it help explain disease spread?","ex":"Think about host, agent, and environment.","a":"The epidemiological triangle describes disease as the interaction of: Agent (pathogen/cause), Host (susceptible person — age, immunity, behavior), and Environment (conditions facilitating transmission — climate, sanitation, population density). Disease emerges when all three factors interact; public health interventions target one or more sides.","diff":"hard"},
         {"q":"Why is health literacy important and how does low health literacy affect health outcomes?","ex":"Think about understanding prescriptions or doctor instructions.","a":"Health literacy is the ability to understand health information and make informed decisions. Low health literacy leads to misunderstanding medication instructions, missing preventive screenings, incorrect diagnoses, medication errors, and higher hospitalizations — disproportionately affecting older adults, those with limited education, and non-native speakers.","diff":"medium"}
       ]}
    ])
  ]
}

# ── Find and replace the AP section in WORKSHEETS ────────────────────────────
with open(f'{BASE}/worksheets.html', 'r') as f:
    content = f.read()

# Find WORKSHEETS object
ws_idx = content.find('const WORKSHEETS')
brace = content.index('{', ws_idx)

# Walk to find the AP key and its value bounds
def find_bracket_end(text, start, open_ch='{', close_ch='}'):
    depth = 0
    i = start
    in_str = False
    str_char = None
    while i < len(text):
        ch = text[i]
        if in_str:
            if ch == '\\': i += 2; continue
            if ch == str_char: in_str = False
        else:
            if ch in ('"', "'", '`'): in_str = True; str_char = ch
            elif ch == open_ch: depth += 1
            elif ch == close_ch:
                depth -= 1
                if depth == 0: return i
        i += 1
    return -1

ws_end = find_bracket_end(content, brace)
ws_text = content[brace:ws_end+1]

# Find "ap": { ... } within ws_text
ap_key_idx = ws_text.find('"ap":')
if ap_key_idx < 0:
    print("ERROR: 'ap' key not found in WORKSHEETS")
    exit(1)

# Find the object start for ap
ap_obj_start = ws_text.index('{', ap_key_idx)
ap_obj_end = find_bracket_end(ws_text, ap_obj_start)

print(f"Found AP section: chars {ap_obj_start} to {ap_obj_end} within WORKSHEETS")
print(f"Current AP section length: {ap_obj_end - ap_obj_start} chars")

# Build replacement JSON
new_ap_json = json.dumps(AP_WORKSHEETS_FULL, ensure_ascii=False, indent=2)
print(f"New AP section length: {len(new_ap_json)} chars")

# Build replacement: ws_text with ap section replaced
new_ws_text = ws_text[:ap_obj_start] + new_ap_json + ws_text[ap_obj_end+1:]

# Put it back into content
new_content = content[:brace] + new_ws_text + content[ws_end+1:]

with open(f'{BASE}/worksheets.html', 'w') as f:
    f.write(new_content)

print("✓ AP worksheets section replaced successfully")

# Count new topics
topic_count = new_ap_json.count('"title":')
print(f"  Total AP topics: {topic_count}")
subj_counts = {}
for subj in ['math','science','ela','history','cs','health']:
    count = AP_WORKSHEETS_FULL.get(subj,[])
    topics = sum(len(unit) for unit in count)
    subj_counts[subj] = topics
    print(f"  {subj}: {topics} topics")
