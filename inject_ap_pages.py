#!/usr/bin/env python3
"""
inject_ap_pages.py
Injects AP-level content into tests.html, worksheets.html, and flashcards.html.
"""
import re, json, os

BASE = '/sessions/admiring-stoic-pascal/mnt/outputs'

# ═══════════════════════════════════════════════════════════════════════════════
# AP TEST DATA  (keyed by SUBJECTS: math, science, ela, history, cs)
# Each value is a list of "unit" objects  {title, questions:[{type,q,choices,correct,exp}]}
# ═══════════════════════════════════════════════════════════════════════════════
AP_TESTS = {
  "math": [
    {
      "title": "AP Calculus AB — Limits & Continuity",
      "questions": [
        {"type":"mc","q":"What is lim(x→2) (x²−4)/(x−2)?","choices":["0","2","4","Undefined"],"correct":2,"exp":"Factor: (x−2)(x+2)/(x−2)=x+2. At x=2: 4."},
        {"type":"mc","q":"A function f is continuous at x=a if:","choices":["f(a) exists only","lim f(x) exists only","f(a)=lim(x→a)f(x)","f is differentiable at a"],"correct":2,"exp":"Continuity requires the limit to equal the function value."},
        {"type":"mc","q":"lim(x→∞) (3x²+2)/(x²−5) equals:","choices":["0","3","∞","−3"],"correct":1,"exp":"Divide numerator and denominator by x²; leading coefficients dominate."},
        {"type":"mc","q":"Which of the following has a removable discontinuity at x=1?","choices":["1/(x−1)","(x²−1)/(x−1)","√(x−1)","ln(x−1)"],"correct":1,"exp":"(x²−1)/(x−1)=(x+1) with a hole at x=1."},
        {"type":"mc","q":"The Intermediate Value Theorem guarantees:","choices":["A local maximum","A point where f=0 always","A value c in (a,b) where f(c)=N if f is continuous","f is differentiable"],"correct":2,"exp":"IVT applies to continuous functions on closed intervals."}
      ]
    },
    {
      "title": "AP Calculus AB — Derivatives",
      "questions": [
        {"type":"mc","q":"d/dx[x³ sin x] equals:","choices":["3x² cos x","3x² sin x + x³ cos x","x³ cos x","3x² sin x − x³ cos x"],"correct":1,"exp":"Product rule: u′v + uv′ = 3x²sinx + x³cosx."},
        {"type":"mc","q":"If f(x)=e^(2x), then f′(x) is:","choices":["e^(2x)","2e^(2x)","2xe^(2x)","e^x"],"correct":1,"exp":"Chain rule: derivative of e^(2x) is 2e^(2x)."},
        {"type":"mc","q":"The derivative of ln(x) is:","choices":["ln(x)","1/x","x","1/ln(x)"],"correct":1,"exp":"d/dx[ln x]=1/x for x>0."},
        {"type":"mc","q":"A critical point occurs where:","choices":["f″=0","f′=0 or f′ is undefined","f=0","f is continuous"],"correct":1,"exp":"Critical points are where f′=0 or DNE."},
        {"type":"mc","q":"Using implicit differentiation on x²+y²=25, dy/dx equals:","choices":["x/y","−x/y","y/x","−y/x"],"correct":1,"exp":"2x+2y(dy/dx)=0, so dy/dx=−x/y."}
      ]
    },
    {
      "title": "AP Statistics — Data Analysis",
      "questions": [
        {"type":"mc","q":"The median of {2,5,7,9,12} is:","choices":["2","7","9","6.7"],"correct":1,"exp":"Middle value of 5 sorted numbers is the 3rd: 7."},
        {"type":"mc","q":"A distribution skewed right has the mean __ the median.","choices":["equal to","less than","greater than","unrelated to"],"correct":2,"exp":"Right skew pulls the mean toward high outliers."},
        {"type":"mc","q":"Standard deviation measures:","choices":["Center","Spread","Shape","Outliers"],"correct":1,"exp":"Standard deviation quantifies the spread around the mean."},
        {"type":"mc","q":"In a Normal distribution, ~95% of data falls within:","choices":["1 SD","2 SD","3 SD","0.5 SD"],"correct":1,"exp":"Empirical rule: 68%, 95%, 99.7% within 1, 2, 3 SDs."},
        {"type":"mc","q":"A p-value of 0.03 at α=0.05 means:","choices":["Fail to reject H₀","Reject H₀","Accept H₀","Data is conclusive"],"correct":1,"exp":"p < α leads to rejection of the null hypothesis."}
      ]
    },
    {
      "title": "AP Precalculus — Functions & Modeling",
      "questions": [
        {"type":"mc","q":"For f(x)=2x+3, f⁻¹(x) equals:","choices":["(x−3)/2","2x−3","(x+3)/2","x/2+3"],"correct":0,"exp":"Swap x and y, then solve: x=2y+3 → y=(x−3)/2."},
        {"type":"mc","q":"log₂(32) equals:","choices":["4","5","6","16"],"correct":1,"exp":"2⁵=32, so log₂(32)=5."},
        {"type":"mc","q":"The period of y=sin(2x) is:","choices":["π","2π","π/2","4π"],"correct":0,"exp":"Period = 2π/|B| = 2π/2 = π."},
        {"type":"mc","q":"A function is even if:","choices":["f(−x)=−f(x)","f(−x)=f(x)","f(x+1)=f(x)","f is increasing"],"correct":1,"exp":"Even functions are symmetric about the y-axis."},
        {"type":"mc","q":"The domain of f(x)=√(x−4) is:","choices":["x>4","x≥4","x≤4","All reals"],"correct":1,"exp":"The radicand must be ≥ 0: x−4≥0 → x≥4."}
      ]
    }
  ],
  "science": [
    {
      "title": "AP Biology — Cell Biology & Genetics",
      "questions": [
        {"type":"mc","q":"Which organelle is the site of ATP synthesis via oxidative phosphorylation?","choices":["Ribosome","Nucleus","Mitochondria","Golgi apparatus"],"correct":2,"exp":"The mitochondrial inner membrane houses the electron transport chain and ATP synthase."},
        {"type":"mc","q":"In Mendel's dihybrid cross (AaBb × AaBb), the expected ratio of dominant phenotypes is:","choices":["9:3:3:1","1:2:1","3:1","1:1:1:1"],"correct":0,"exp":"Law of Independent Assortment gives a 9:3:3:1 phenotypic ratio."},
        {"type":"mc","q":"Which of the following best describes natural selection?","choices":["Random change in allele frequency","Differential reproductive success due to heritable traits","Mutation of beneficial genes","Migration between populations"],"correct":1,"exp":"Natural selection acts on heritable variation, leading to differential survival and reproduction."},
        {"type":"mc","q":"mRNA is translated into protein at the:","choices":["Nucleus","Ribosome","Lysosome","Endoplasmic reticulum only"],"correct":1,"exp":"Ribosomes read mRNA codons and link amino acids into polypeptides."},
        {"type":"mc","q":"An enzyme lowers the activation energy by:","choices":["Adding energy to the reaction","Stabilizing the transition state","Changing the equilibrium constant","Increasing temperature"],"correct":1,"exp":"Enzymes bind substrates and stabilize the transition state, reducing Ea."}
      ]
    },
    {
      "title": "AP Chemistry — Atomic Structure & Bonding",
      "questions": [
        {"type":"mc","q":"The electron configuration of Fe (Z=26) is:","choices":["[Ar] 3d⁶ 4s²","[Ar] 3d⁸","[Kr] 3d⁶ 4s²","[Ar] 4s² 4p⁶"],"correct":0,"exp":"Iron fills [Ar], then 4s², then 3d⁶."},
        {"type":"mc","q":"Which bond is most polar?","choices":["C−H","N−H","O−H","F−H"],"correct":3,"exp":"F has the highest electronegativity, making H−F the most polar bond."},
        {"type":"mc","q":"VSEPR theory predicts the geometry of CH₄ is:","choices":["Linear","Trigonal planar","Tetrahedral","Bent"],"correct":2,"exp":"Four bonding pairs around C with no lone pairs → tetrahedral, 109.5°."},
        {"type":"mc","q":"A buffer resists pH changes because it contains:","choices":["A strong acid only","A weak acid and its conjugate base","A strong base","Pure water"],"correct":1,"exp":"Buffers neutralize added H⁺ or OH⁻ using a weak acid/conjugate base pair."},
        {"type":"mc","q":"For the reaction 2H₂+O₂→2H₂O, if ΔH<0 and ΔS<0, the reaction is spontaneous when:","choices":["T is high","T is low","Always","Never"],"correct":1,"exp":"ΔG=ΔH−TΔS; both negative terms mean ΔG<0 at low T."}
      ]
    },
    {
      "title": "AP Physics 1 — Mechanics",
      "questions": [
        {"type":"mc","q":"A 5 kg object accelerates at 3 m/s². The net force is:","choices":["1.7 N","8 N","15 N","0 N"],"correct":2,"exp":"F=ma=5×3=15 N."},
        {"type":"mc","q":"Kinetic energy of a 4 kg object moving at 6 m/s is:","choices":["12 J","24 J","72 J","144 J"],"correct":2,"exp":"KE=½mv²=½(4)(36)=72 J."},
        {"type":"mc","q":"According to Newton's third law, when you push a wall:","choices":["The wall does not push back","The wall pushes you back with equal force","The wall pushes back with less force","The wall pushes back harder"],"correct":1,"exp":"Action-reaction pairs are equal in magnitude, opposite in direction."},
        {"type":"mc","q":"The period of a simple pendulum depends on:","choices":["Mass only","Length and gravity","Amplitude only","Mass and length"],"correct":1,"exp":"T=2π√(L/g); period is independent of mass and (for small angles) amplitude."},
        {"type":"mc","q":"The work done by a force F at angle θ over displacement d is:","choices":["Fd","Fd sinθ","Fd cosθ","F/d"],"correct":2,"exp":"W=Fd cosθ — only the component of force along displacement does work."}
      ]
    },
    {
      "title": "AP Environmental Science — Ecosystems",
      "questions": [
        {"type":"mc","q":"Which best describes the greenhouse effect?","choices":["Ozone absorbs UV","Atmospheric gases trap outgoing infrared radiation","Deforestation cools the planet","Oceans absorb solar energy only"],"correct":1,"exp":"Greenhouse gases (CO₂, CH₄, H₂O) absorb and re-emit IR radiation, warming Earth."},
        {"type":"mc","q":"Primary productivity is measured by:","choices":["Decomposition rate","Rate of organic matter production by producers","Animal biomass","Soil nutrient content"],"correct":1,"exp":"Net Primary Productivity (NPP) = GPP − plant respiration."},
        {"type":"mc","q":"Eutrophication is caused by:","choices":["Oil spills","Excess nutrients leading to algal blooms and oxygen depletion","Acid rain","Heavy metal pollution"],"correct":1,"exp":"Excess N and P cause algal blooms; decomposition depletes dissolved O₂."},
        {"type":"mc","q":"The IPAT equation represents:","choices":["Irrigation × Population × Agriculture × Technology","Impact = Population × Affluence × Technology","Income × Production × Area × Time","None of the above"],"correct":1,"exp":"I=PAT: environmental Impact = Population × Affluence × Technology."},
        {"type":"mc","q":"Biotic potential refers to:","choices":["The carrying capacity","The maximum reproduction rate under ideal conditions","The actual population growth rate","Competition between species"],"correct":1,"exp":"Biotic potential is the maximum reproductive rate when resources are unlimited."}
      ]
    }
  ],
  "ela": [
    {
      "title": "AP English Language — Rhetoric & Argumentation",
      "questions": [
        {"type":"mc","q":"An appeal to the audience's emotions is called:","choices":["Logos","Ethos","Pathos","Kairos"],"correct":2,"exp":"Pathos appeals to emotion; ethos to credibility; logos to logic."},
        {"type":"mc","q":"A rhetorical situation includes all EXCEPT:","choices":["Audience","Purpose","Occasion","Font size"],"correct":3,"exp":"Rhetorical situation: speaker, audience, purpose, context/occasion, and message."},
        {"type":"mc","q":"Anaphora is the repetition of:","choices":["End words","Beginning words or phrases","Sound patterns","A refrain in poetry"],"correct":1,"exp":"Anaphora repeats a word or phrase at the beginning of successive clauses (e.g., 'I have a dream...')."},
        {"type":"mc","q":"A concession in an argument:","choices":["Refutes the opposing side","Acknowledges a valid point of the opposition","Provides statistical evidence","Restates the thesis"],"correct":1,"exp":"A concession grants partial validity to the opposition before offering a rebuttal."},
        {"type":"mc","q":"The primary purpose of a synthesis essay is to:","choices":["Summarize multiple texts","Argue a position using multiple sources as evidence","Compare two texts","Analyze one author's style"],"correct":1,"exp":"AP Lang synthesis essays require constructing an argument supported by provided sources."}
      ]
    },
    {
      "title": "AP English Literature — Literary Analysis",
      "questions": [
        {"type":"mc","q":"A story within a story is called a:","choices":["Motif","Frame narrative","Allegory","Foil"],"correct":1,"exp":"A frame narrative encloses an inner story (e.g., The Canterbury Tales, Heart of Darkness)."},
        {"type":"mc","q":"Which of the following is an example of dramatic irony?","choices":["A character says one thing but means another","The audience knows something a character does not","Two characters have opposite traits","A story ends unexpectedly"],"correct":1,"exp":"Dramatic irony creates tension when the audience has information characters lack."},
        {"type":"mc","q":"Free indirect discourse blends:","choices":["Dialogue and stage directions","Third-person narration with a character's thoughts","First and second person","Symbolism and metaphor"],"correct":1,"exp":"Free indirect discourse presents a character's thoughts/speech in the narrator's voice without quotation."},
        {"type":"mc","q":"A Bildungsroman follows:","choices":["A hero's journey to war","A character's psychological and moral growth from youth to adulthood","A tragic hero's downfall","A society's political change"],"correct":1,"exp":"Bildungsroman (coming-of-age novel) traces a protagonist's moral and social development."},
        {"type":"mc","q":"In poetry, a volta is:","choices":["A type of rhyme scheme","A shift in tone, argument, or perspective","The final couplet","A metrical foot"],"correct":1,"exp":"The volta marks a turn—a pivot in thought or feeling—especially in sonnets."}
      ]
    }
  ],
  "history": [
    {
      "title": "AP US History — Colonial to Civil War",
      "questions": [
        {"type":"mc","q":"The primary cause of the Civil War was:","choices":["Tariff disputes only","States' rights regarding slavery","Industrial competition","Foreign interference"],"correct":1,"exp":"Historians broadly agree slavery and its expansion were the central cause of the Civil War."},
        {"type":"mc","q":"The Compromise of 1850 included:","choices":["Missouri as a free state","California admitted as a free state and the Fugitive Slave Act","Kansas-Nebraska Act","Emancipation in border states"],"correct":1,"exp":"Compromise of 1850: CA free, popular sovereignty in territories, stricter Fugitive Slave Law."},
        {"type":"mc","q":"Manifest Destiny referred to the belief that:","choices":["The US should remain isolated","American expansion across the continent was inevitable and justified","The US should abolish slavery","Democracy would spread globally"],"correct":1,"exp":"Manifest Destiny (1840s) held that the US was destined to expand from Atlantic to Pacific."},
        {"type":"mc","q":"The Declaration of Independence drew most heavily from:","choices":["Thomas Hobbes","John Locke","Jean-Jacques Rousseau","Montesquieu"],"correct":1,"exp":"Jefferson's natural rights philosophy (life, liberty, property) reflects Locke's Second Treatise."},
        {"type":"mc","q":"The XYZ Affair involved:","choices":["British impressment of US sailors","French agents demanding bribes from US diplomats","Spanish land disputes in Florida","A Native American confederation"],"correct":1,"exp":"French agents (X,Y,Z) demanded bribes from US envoys in 1797, sparking the Quasi-War."}
      ]
    },
    {
      "title": "AP World History — Global Connections",
      "questions": [
        {"type":"mc","q":"The Silk Roads primarily facilitated the exchange of:","choices":["Military technology only","Goods, ideas, and diseases across Afro-Eurasia","Political boundaries","Democratic governments"],"correct":1,"exp":"Silk Roads (c. 100 BCE–1450 CE) spread goods, religions (Buddhism, Islam), and diseases like the plague."},
        {"type":"mc","q":"The Columbian Exchange most immediately introduced to the Americas:","choices":["Horses and wheat","Democracy and capitalism","Printing press","Silk and porcelain"],"correct":0,"exp":"Europeans brought horses, cattle, wheat, and diseases; Americas gave potatoes, corn, and tomatoes."},
        {"type":"mc","q":"Gunpowder empires include all EXCEPT:","choices":["Ottoman Empire","Mughal Empire","Safavid Empire","Song Dynasty"],"correct":3,"exp":"Song Dynasty predated the gunpowder empire era; Ottomans, Mughals, and Safavids built empires using firearms."},
        {"type":"mc","q":"The Atlantic slave trade peaked in which century?","choices":["15th","16th","18th","20th"],"correct":2,"exp":"The 18th century saw the highest volume of enslaved African transatlantic deportations."},
        {"type":"mc","q":"Which best describes mercantilism?","choices":["Free trade between nations","A colonial economic policy maximizing exports and accumulating bullion","Industrialization of colonies","Democratic capitalism"],"correct":1,"exp":"Mercantilism held that wealth was finite; colonies existed to enrich the mother country via trade surpluses."}
      ]
    },
    {
      "title": "AP US Government — Constitution & Civil Liberties",
      "questions": [
        {"type":"mc","q":"Judicial review was established in:","choices":["Marbury v. Madison","McCulloch v. Maryland","Brown v. Board","Roe v. Wade"],"correct":0,"exp":"Marbury v. Madison (1803) established the Supreme Court's power to strike down unconstitutional laws."},
        {"type":"mc","q":"The elastic clause grants Congress:","choices":["Power to declare war","Necessary and proper powers to carry out enumerated powers","The right to tax","Veto power"],"correct":1,"exp":"Article I, Section 8 allows Congress to make all laws 'necessary and proper.'"},
        {"type":"mc","q":"Federalism divides power between:","choices":["Three branches of government","The national and state governments","The president and Congress","Courts and legislatures"],"correct":1,"exp":"Federalism is the division of authority between national and subnational (state) governments."},
        {"type":"mc","q":"Which amendment protects against unreasonable searches and seizures?","choices":["First","Fourth","Sixth","Fourteenth"],"correct":1,"exp":"The Fourth Amendment requires probable cause and warrants for searches and seizures."},
        {"type":"mc","q":"An iron triangle involves:","choices":["President, Senate, House","Congress, executive agencies, and interest groups","Courts, media, and lobbyists","State, local, and federal governments"],"correct":1,"exp":"Iron triangles are stable policy relationships among congressional committees, agencies, and interest groups."}
      ]
    },
    {
      "title": "AP Psychology — Behavior & Mental Processes",
      "questions": [
        {"type":"mc","q":"Classical conditioning pairs a neutral stimulus with a(n):","choices":["Conditioned response","Unconditioned stimulus","Operant behavior","Punishment"],"correct":1,"exp":"Pavlov's classical conditioning associates a neutral stimulus with an unconditioned stimulus to elicit a response."},
        {"type":"mc","q":"According to Maslow's hierarchy, which need must be met first?","choices":["Esteem","Belonging","Safety","Physiological"],"correct":3,"exp":"Maslow's hierarchy: physiological → safety → belonging → esteem → self-actualization."},
        {"type":"mc","q":"The part of the neuron that receives signals is the:","choices":["Axon","Myelin sheath","Dendrite","Terminal button"],"correct":2,"exp":"Dendrites are branching extensions that receive signals from other neurons."},
        {"type":"mc","q":"In an experiment, the variable the researcher manipulates is:","choices":["Dependent variable","Control variable","Independent variable","Confounding variable"],"correct":2,"exp":"The independent variable is deliberately changed; the dependent variable is measured in response."},
        {"type":"mc","q":"Cognitive dissonance occurs when:","choices":["Two people disagree","A person holds contradictory beliefs or behaviors","Memory fails","A stimulus goes unnoticed"],"correct":1,"exp":"Festinger's cognitive dissonance: mental discomfort from holding conflicting cognitions, motivating change."}
      ]
    }
  ],
  "cs": [
    {
      "title": "AP Computer Science A — Java Programming",
      "questions": [
        {"type":"mc","q":"In Java, which keyword is used to define a subclass?","choices":["implements","inherits","extends","super"],"correct":2,"exp":"The 'extends' keyword creates a subclass that inherits from a superclass."},
        {"type":"mc","q":"What is the output of: int x=5; System.out.println(x++);","choices":["6","5","4","Error"],"correct":1,"exp":"Post-increment x++ returns the original value (5), then increments x to 6."},
        {"type":"mc","q":"Which data structure uses LIFO order?","choices":["Queue","Stack","ArrayList","LinkedList"],"correct":1,"exp":"A Stack uses Last-In-First-Out — the last element pushed is the first popped."},
        {"type":"mc","q":"Binary search requires the array to be:","choices":["Unsorted","Sorted","Filled with integers","Of even length"],"correct":1,"exp":"Binary search divides the sorted array in half each step, requiring a sorted input."},
        {"type":"mc","q":"Polymorphism allows:","choices":["A class to have two constructors","Different classes to respond differently to the same method call","Variables to hold any data type","Recursive functions"],"correct":1,"exp":"Polymorphism (via method overriding) lets subclasses provide specific implementations of parent methods."}
      ]
    },
    {
      "title": "AP Computer Science Principles — Digital Concepts",
      "questions": [
        {"type":"mc","q":"What does 1101 in binary equal in decimal?","choices":["11","12","13","14"],"correct":2,"exp":"8+4+0+1=13. (1×8)+(1×4)+(0×2)+(1×1)=13."},
        {"type":"mc","q":"The 'internet' refers to:","choices":["A single server","A global network of interconnected networks","Only the World Wide Web","A programming language"],"correct":1,"exp":"The internet is a global infrastructure of interconnected computer networks using TCP/IP."},
        {"type":"mc","q":"Which of the following is an example of lossless compression?","choices":["JPEG","MP3","ZIP","MPEG"],"correct":2,"exp":"ZIP (and formats like PNG) use lossless compression — no data is lost on decompression."},
        {"type":"mc","q":"A public key encryption system:","choices":["Uses one shared secret key","Uses a public key to encrypt and a private key to decrypt","Is the same as a Caesar cipher","Requires direct physical exchange of keys"],"correct":1,"exp":"Asymmetric encryption uses a public key (encrypt) and a private key (decrypt)."},
        {"type":"mc","q":"A citizen science project that uses many computers to solve a large problem is an example of:","choices":["Machine learning","Crowdsourcing","Encryption","Abstraction"],"correct":1,"exp":"Crowdsourcing distributes computational tasks across many volunteer computers (e.g., SETI@home)."}
      ]
    }
  ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# AP WORKSHEET DATA
# ═══════════════════════════════════════════════════════════════════════════════
AP_WORKSHEETS = {
  "math": [
    [
      {
        "title": "AP Calculus — Derivatives Practice",
        "problems": [
          {"q":"Find d/dx[3x⁴ − 2x² + 7].","ex":"Apply the power rule to each term.","a":"12x³ − 4x","diff":"easy"},
          {"q":"Use the chain rule to differentiate f(x) = (2x+1)⁵.","ex":"Let u = 2x+1, apply chain rule.","a":"10(2x+1)⁴","diff":"medium"},
          {"q":"Differentiate g(x) = x² · eˣ using the product rule.","ex":"(uv)′ = u′v + uv′","a":"2xeˣ + x²eˣ = eˣ(x²+2x)","diff":"medium"},
          {"q":"Find the equation of the tangent line to y = x³ at x = 2.","ex":"Find slope via derivative, then point-slope form.","a":"Slope=12; line: y−8=12(x−2), or y=12x−16","diff":"hard"}
        ]
      }
    ],
    [
      {
        "title": "AP Statistics — Hypothesis Testing",
        "problems": [
          {"q":"A sample of 36 students has mean score 78 (σ=12). Test H₀: μ=75 at α=0.05.","ex":"Compute z-score: z=(x̄−μ)/(σ/√n)","a":"z=(78−75)/(12/6)=1.5; critical z=1.645; fail to reject H₀","diff":"hard"},
          {"q":"State the null and alternative hypotheses for: 'A new drug lowers blood pressure more than the current drug.'","ex":"H₀ states no difference or equality.","a":"H₀: μ_new ≥ μ_old (or μ_new − μ_old ≤ 0); H₁: μ_new < μ_old","diff":"medium"},
          {"q":"A 95% confidence interval for a mean is (42.1, 47.9). What is the margin of error?","ex":"ME = (upper − lower)/2","a":"ME = (47.9−42.1)/2 = 2.9","diff":"easy"}
        ]
      }
    ]
  ],
  "science": [
    [
      {
        "title": "AP Biology — Cellular Respiration",
        "problems": [
          {"q":"Write the overall equation for aerobic cellular respiration.","ex":"Include glucose, oxygen, ATP, CO₂, and water.","a":"C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + ~36–38 ATP","diff":"easy"},
          {"q":"Where in the cell does the Krebs cycle occur?","ex":"Name the specific compartment.","a":"Mitochondrial matrix","diff":"easy"},
          {"q":"What is the electron carrier that shuttles electrons to the electron transport chain?","ex":"Two molecules are involved.","a":"NADH and FADH₂","diff":"medium"},
          {"q":"Explain why oxygen is the final electron acceptor in aerobic respiration.","ex":"Consider electronegativity and water formation.","a":"Oxygen has high electronegativity; it accepts electrons and protons to form H₂O, maintaining the electron flow that drives ATP synthesis.","diff":"hard"}
        ]
      }
    ],
    [
      {
        "title": "AP Chemistry — Stoichiometry",
        "problems": [
          {"q":"How many moles of H₂O are produced from 4 mol H₂ reacting with excess O₂? (2H₂ + O₂ → 2H₂O)","ex":"Use mole ratio from balanced equation.","a":"4 mol H₂O","diff":"easy"},
          {"q":"What mass of CO₂ is produced from burning 44 g of propane? (C₃H₈ + 5O₂ → 3CO₂ + 4H₂O)","ex":"Find mol propane, use mole ratio, convert to mass.","a":"Molar mass C₃H₈=44 g/mol → 1 mol; produces 3 mol CO₂ × 44 g/mol = 132 g CO₂","diff":"hard"},
          {"q":"A reaction has a theoretical yield of 50 g but only 40 g are collected. Calculate percent yield.","ex":"% yield = (actual/theoretical) × 100","a":"80%","diff":"easy"}
        ]
      }
    ]
  ],
  "ela": [
    [
      {
        "title": "AP Lang — Rhetorical Analysis",
        "problems": [
          {"q":"Identify and analyze one rhetorical appeal (ethos, pathos, or logos) in this claim: 'As a 20-year veteran teacher, I can assure you that standardized testing harms student learning.'","ex":"Name the appeal and explain how it functions.","a":"Ethos: the speaker establishes credibility through professional experience ('20-year veteran'), positioning themselves as an authoritative voice on education.","diff":"medium"},
          {"q":"Rewrite the following to strengthen its logos appeal: 'Many people are hurt by social media every day.'","ex":"Add specific, verifiable evidence.","a":"Example: 'A 2023 Pew Research study found that 46% of teens report feeling worse about their bodies after using social media, highlighting its measurable psychological impact.'","diff":"hard"},
          {"q":"What is the effect of using short, declarative sentences in an argument?","ex":"Consider rhythm, emphasis, and audience impact.","a":"Short declarative sentences create urgency and emphasis, making claims feel absolute and memorable. They break complexity into digestible assertions and can drive home key points with authority.","diff":"medium"}
        ]
      }
    ]
  ],
  "history": [
    [
      {
        "title": "AP US History — Document Analysis",
        "problems": [
          {"q":"Identify ONE cause of the Great Depression and explain its effect on American society.","ex":"Consider economic, banking, or agricultural factors.","a":"Example: Overproduction and weak consumer demand led to factory closures and mass unemployment, pushing poverty rates above 25% by 1933 and eroding public confidence in capitalism.","diff":"medium"},
          {"q":"Compare Booker T. Washington's and W.E.B. Du Bois's approaches to racial equality.","ex":"Consider their strategies and historical context.","a":"Washington advocated vocational education and economic self-sufficiency within the existing segregated system ('Atlanta Compromise'). Du Bois demanded immediate civil and political rights, co-founding the NAACP and championing the 'Talented Tenth' who would lead through higher education.","diff":"hard"},
          {"q":"Explain how the Emancipation Proclamation changed the purpose of the Civil War.","ex":"Consider its legal, military, and symbolic dimensions.","a":"It transformed the war from primarily a fight to preserve the Union into a war to end slavery, securing moral high ground, discouraging European recognition of the Confederacy, and allowing Black men to enlist in the Union Army.","diff":"hard"}
        ]
      }
    ],
    [
      {
        "title": "AP Psychology — Research Methods",
        "problems": [
          {"q":"A researcher randomly assigns 200 participants to a drug or placebo. What type of study is this?","ex":"Consider random assignment and control group.","a":"A true experiment; random assignment controls for confounding variables, allowing causal conclusions.","diff":"easy"},
          {"q":"Define 'operational definition' and give an example.","ex":"How do researchers measure abstract concepts?","a":"An operational definition specifies how a variable is measured. Example: 'Stress is operationally defined as participants' scores on the Perceived Stress Scale (PSS-10).'","diff":"medium"},
          {"q":"What is the difference between correlation and causation? Give an example.","ex":"Correlation ≠ causation.","a":"Correlation means two variables move together; causation means one causes the other. Example: Ice cream sales and drowning rates correlate (both rise in summer), but ice cream does not cause drowning—summer heat is the confounding variable.","diff":"medium"}
        ]
      }
    ]
  ],
  "cs": [
    [
      {
        "title": "AP CS A — Object-Oriented Programming",
        "problems": [
          {"q":"Write a Java class 'Rectangle' with fields width and height, a constructor, and a method getArea() that returns the area.","ex":"Include field declarations, constructor, and method.","a":"public class Rectangle { int width, height; Rectangle(int w, int h){width=w; height=h;} int getArea(){return width*height;} }","diff":"medium"},
          {"q":"What is the output of this Java snippet?\nint[] arr = {3,1,4,1,5};\nfor(int x : arr) System.out.print(x+\" \");","ex":"Trace through the enhanced for loop.","a":"3 1 4 1 5","diff":"easy"},
          {"q":"Explain the difference between a class and an object in OOP.","ex":"Use an analogy if helpful.","a":"A class is a blueprint (e.g., 'Car'), while an object is an instance of that class (e.g., a specific red Toyota Camry). The class defines properties and methods; the object has specific values for those properties.","diff":"easy"}
        ]
      }
    ]
  ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# AP FLASHCARD DATA  (added to each subject in CARDS)
# ═══════════════════════════════════════════════════════════════════════════════
AP_FLASHCARDS = {
  "math": [
    {"term":"Limit","def":"The value a function approaches as the input approaches a given point. Written as lim(x→a) f(x)."},
    {"term":"Derivative","def":"The instantaneous rate of change of a function; the slope of the tangent line at a point. Notation: f′(x) or dy/dx."},
    {"term":"Integral","def":"The area under a curve; the reverse of differentiation. Definite integrals give numerical values; indefinite give functions."},
    {"term":"Fundamental Theorem of Calculus","def":"Links differentiation and integration: ∫[a,b] f(x)dx = F(b)−F(a), where F is an antiderivative of f."},
    {"term":"Chain Rule","def":"For composite functions: d/dx[f(g(x))] = f′(g(x))·g′(x). Differentiate the outside then multiply by derivative of inside."},
    {"term":"p-value","def":"The probability of obtaining a test statistic as extreme as observed, assuming H₀ is true. Small p-value (< α) → reject H₀."},
    {"term":"Standard Deviation","def":"A measure of spread: the average distance of data values from the mean. Square of SD = variance."},
    {"term":"Normal Distribution","def":"A symmetric, bell-shaped distribution characterized by mean μ and standard deviation σ. ~68-95-99.7% rule applies."},
    {"term":"Confidence Interval","def":"A range of values constructed from sample data that is likely to contain the true population parameter."},
    {"term":"Regression Line","def":"The least-squares line ŷ = a + bx that minimizes the sum of squared residuals; used to predict y from x."}
  ],
  "science": [
    {"term":"Activation Energy","def":"The minimum energy required to initiate a chemical reaction. Enzymes lower activation energy without being consumed."},
    {"term":"Mitosis","def":"Cell division producing two genetically identical daughter cells. Phases: prophase, metaphase, anaphase, telophase."},
    {"term":"Natural Selection","def":"The process by which heritable traits that increase reproductive success become more common in a population over generations."},
    {"term":"Entropy","def":"A measure of disorder or randomness in a system (S). The Second Law states entropy of an isolated system tends to increase."},
    {"term":"Le Chatelier's Principle","def":"If a system at equilibrium is disturbed, it shifts to counteract the disturbance and restore equilibrium."},
    {"term":"Electromagnetic Spectrum","def":"The range of all types of EM radiation, from gamma rays (shortest wavelength) to radio waves (longest)."},
    {"term":"Hardy-Weinberg Equilibrium","def":"A principle stating allele frequencies remain constant in a large, randomly mating population with no evolutionary forces."},
    {"term":"pH","def":"A logarithmic scale measuring hydrogen ion concentration. pH < 7 = acidic; pH = 7 = neutral; pH > 7 = basic."},
    {"term":"Electronegativity","def":"An atom's ability to attract shared electrons in a bond. Fluorine is most electronegative (3.98 on Pauling scale)."},
    {"term":"Newton's Second Law","def":"F = ma. Net force equals mass times acceleration. Force is measured in Newtons (kg·m/s²)."}
  ],
  "ela": [
    {"term":"Rhetorical Situation","def":"The context of a communication act: speaker/writer, audience, purpose, occasion/context, and the message itself."},
    {"term":"Ethos","def":"An appeal to credibility or character. Convincing an audience by demonstrating expertise or trustworthiness."},
    {"term":"Pathos","def":"An appeal to the audience's emotions—fear, sympathy, joy, anger—to persuade or engage."},
    {"term":"Logos","def":"An appeal to logic, reason, and evidence—statistics, facts, expert testimony—to support an argument."},
    {"term":"Anaphora","def":"Repetition of a word or phrase at the beginning of successive clauses (e.g., MLK's 'I have a dream...')."},
    {"term":"Chiasmus","def":"A rhetorical figure in which grammatical structures are reversed: 'Ask not what your country can do for you...'"},
    {"term":"Synthesis Essay","def":"An AP Lang essay type requiring students to develop an argument drawing on multiple provided source documents."},
    {"term":"Bildungsroman","def":"A coming-of-age novel tracing a protagonist's moral and psychological growth from youth to maturity."},
    {"term":"Volta","def":"A turn or shift in argument, emotion, or perspective—especially significant in sonnets (often at line 9 or 13)."},
    {"term":"Unreliable Narrator","def":"A narrator whose credibility is compromised by bias, limited knowledge, or psychological instability."}
  ],
  "history": [
    {"term":"Manifest Destiny","def":"19th-century belief that the United States was destined to expand across the North American continent."},
    {"term":"Checks and Balances","def":"Constitutional system in which each branch of government can limit the powers of the other branches."},
    {"term":"Columbian Exchange","def":"The transfer of plants, animals, diseases, and ideas between the Americas and the Old World after 1492."},
    {"term":"Mercantilism","def":"An economic theory holding that a nation's wealth depends on accumulating bullion through favorable trade; colonies exist to serve the mother country."},
    {"term":"Judicial Review","def":"The Supreme Court's power to declare laws unconstitutional; established in Marbury v. Madison (1803)."},
    {"term":"Cold War","def":"A period of geopolitical tension (1947–1991) between the US/NATO and USSR/Warsaw Pact, characterized by proxy wars and arms race without direct military conflict."},
    {"term":"Cognitive Dissonance","def":"(AP Psych) Mental discomfort from holding contradictory beliefs or behaviors, motivating attitude change to restore consistency."},
    {"term":"Operant Conditioning","def":"(AP Psych) B.F. Skinner's learning model: behavior is shaped by consequences—reinforcement increases and punishment decreases behaviors."},
    {"term":"Federalism","def":"A system dividing sovereignty between national and state governments, each having authority in defined areas."},
    {"term":"Silk Road","def":"Ancient trade networks linking East Asia, Central Asia, South Asia, the Middle East, and Europe, facilitating exchange of goods, culture, and disease."}
  ],
  "cs": [
    {"term":"Algorithm","def":"A step-by-step set of instructions for solving a problem or completing a task, with a defined input and output."},
    {"term":"Binary","def":"A base-2 number system using only 0 and 1. Computers use binary at the hardware level to represent all data."},
    {"term":"Object-Oriented Programming","def":"A programming paradigm organizing code into objects (instances of classes) that have properties and methods."},
    {"term":"Polymorphism","def":"OOP concept allowing objects of different classes to be treated as objects of a common superclass; methods behave differently per class."},
    {"term":"Recursion","def":"A function that calls itself with a modified input until a base case is reached, solving problems by breaking them into subproblems."},
    {"term":"Time Complexity","def":"A measure of how runtime grows with input size, expressed in Big-O notation (e.g., O(n), O(n²), O(log n))."},
    {"term":"Encryption","def":"The process of encoding data so only authorized parties can read it. Public-key encryption uses key pairs."},
    {"term":"Abstraction","def":"Hiding implementation details to reduce complexity, allowing programmers to use interfaces without knowing internals."},
    {"term":"Boolean Logic","def":"Logic using true/false values and operators AND, OR, NOT. The basis for all computer circuit design and conditionals."},
    {"term":"Inheritance","def":"An OOP mechanism where a subclass acquires properties and methods of a superclass using 'extends'."}
  ]
}

# ═══════════════════════════════════════════════════════════════════════════════
# HELPER: find closing `};` of a top-level JS object by bracket depth
# ═══════════════════════════════════════════════════════════════════════════════
def find_object_end(content, start_idx):
    depth = 0
    i = start_idx
    in_str = False
    str_char = None
    while i < len(content):
        ch = content[i]
        if in_str:
            if ch == '\\': i += 2; continue
            if ch == str_char: in_str = False
        else:
            if ch in ('"', "'", '`'):
                in_str = True; str_char = ch
            elif ch == '{': depth += 1
            elif ch == '}':
                depth -= 1
                if depth == 0:
                    return i
        i += 1
    return -1

# ═══════════════════════════════════════════════════════════════════════════════
# 1. PATCH tests.html
# ═══════════════════════════════════════════════════════════════════════════════
print("Patching tests.html...")
with open(f'{BASE}/tests.html', 'r') as f:
    html = f.read()

# Add AP key to TESTS
tests_start = html.find('const TESTS')
if '"ap"' not in html[tests_start:tests_start+500000]:
    obj_start = html.index('{', tests_start)
    obj_end = find_object_end(html, obj_start)
    ap_tests_json = json.dumps(AP_TESTS, ensure_ascii=False)
    # Insert before closing }
    html = html[:obj_end] + ',\n  "ap": ' + ap_tests_json + '\n' + html[obj_end:]
    print("  ✓ AP data inserted into TESTS")
else:
    print("  ✓ AP already present in TESTS")

# Add AP grade button
if 'onclick="selectGrade(\'ap\'' not in html:
    html = html.replace(
        '<button class="grade-btn" onclick="selectGrade(12,this)">Grade 12</button>',
        '<button class="grade-btn" onclick="selectGrade(12,this)">Grade 12</button>\n  <button class="grade-btn" onclick="selectGrade(\'ap\',this)">AP Courses</button>'
    )
    print("  ✓ AP grade button added")

# Fix selectGrade to handle 'ap' grade — update currentGrade assignment
if "currentGrade = grade" in html and "AP_SUBJECTS" not in html:
    # Add AP_SUBJECTS constant after SUBJECTS
    ap_subj_block = """
const AP_SUBJECTS = {
  math:    {label:"Mathematics (AP)",       icon:"📐"},
  science: {label:"Science (AP)",           icon:"🔬"},
  ela:     {label:"English (AP)",           icon:"📚"},
  history: {label:"History & Social Sci (AP)",icon:"🌍"},
  cs:      {label:"Computer Science (AP)",  icon:"💻"},
};
"""
    html = html.replace('let currentGrade = 6;', ap_subj_block + 'let currentGrade = 6;')
    print("  ✓ AP_SUBJECTS added")

# Fix buildSidebar to use AP_SUBJECTS when grade is 'ap'
if "const gradeData = TESTS[grade]" in html and "activeSubjects" not in html:
    html = html.replace(
        'function buildSidebar(grade){',
        'function buildSidebar(grade){\n  const activeSubjects = (grade === \'ap\') ? AP_SUBJECTS : SUBJECTS;'
    )
    html = html.replace(
        "for(const [subj, meta] of Object.entries(SUBJECTS)){",
        "for(const [subj, meta] of Object.entries(activeSubjects)){"
    )
    print("  ✓ buildSidebar patched for AP_SUBJECTS")

with open(f'{BASE}/tests.html', 'w') as f:
    f.write(html)
print("  ✓ tests.html saved\n")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. PATCH worksheets.html
# ═══════════════════════════════════════════════════════════════════════════════
print("Patching worksheets.html...")
with open(f'{BASE}/worksheets.html', 'r') as f:
    html = f.read()

# Add AP key to WORKSHEETS
ws_start = html.find('const WORKSHEETS')
if '"ap"' not in html[ws_start:ws_start+500000]:
    obj_start = html.index('{', ws_start)
    obj_end = find_object_end(html, obj_start)
    ap_ws_json = json.dumps(AP_WORKSHEETS, ensure_ascii=False)
    html = html[:obj_end] + ',\n  "ap": ' + ap_ws_json + '\n' + html[obj_end:]
    print("  ✓ AP data inserted into WORKSHEETS")
else:
    print("  ✓ AP already present in WORKSHEETS")

# Add AP grade button
if 'onclick="selectGrade(\'ap\'' not in html:
    html = html.replace(
        '<button class="grade-btn" data-grade="12" onclick="selectGrade(12,this)">12th</button>',
        '<button class="grade-btn" data-grade="12" onclick="selectGrade(12,this)">12th</button>\n  <button class="grade-btn" data-grade="ap" onclick="selectGrade(\'ap\',this)">AP</button>'
    )
    print("  ✓ AP grade button added")

# Add AP_SUBJECTS and fix buildSidebar for worksheets
if "AP_SUBJECTS" not in html:
    ap_subj_block = """
const AP_SUBJECTS = {
  math:    { label:"Mathematics (AP)",          icon:"📐" },
  science: { label:"Science (AP)",              icon:"🔬" },
  ela:     { label:"English (AP)",              icon:"📚" },
  history: { label:"History & Social Sci (AP)", icon:"🌍" },
  cs:      { label:"Computer Science (AP)",     icon:"💻" },
};
"""
    html = html.replace('let currentGrade = 6;', ap_subj_block + 'let currentGrade = 6;')
    print("  ✓ AP_SUBJECTS added")

# Fix buildSidebar for worksheets
if "const gradeData = WORKSHEETS[grade]" in html and "AP_SUBJECTS" in html:
    html = html.replace(
        'function buildSidebar(grade){',
        'function buildSidebar(grade){\n  const activeSubjects = (grade === \'ap\') ? AP_SUBJECTS : SUBJECTS;'
    )
    # Replace SUBJECTS usage in buildSidebar
    # There should be one occurrence after the function start
    html = html.replace(
        "for(const [subj, meta] of Object.entries(SUBJECTS)){",
        "for(const [subj, meta] of Object.entries(activeSubjects)){"
    )
    print("  ✓ buildSidebar patched for AP_SUBJECTS")

with open(f'{BASE}/worksheets.html', 'w') as f:
    f.write(html)
print("  ✓ worksheets.html saved\n")

# ═══════════════════════════════════════════════════════════════════════════════
# 3. PATCH flashcards.html
# ═══════════════════════════════════════════════════════════════════════════════
print("Patching flashcards.html...")
with open(f'{BASE}/flashcards.html', 'r') as f:
    html = f.read()

# Add AP cards to each subject in CARDS
cards_start = html.find('const CARDS')
if 'g:\'ap\'' not in html[cards_start:cards_start+500000]:
    for subj, cards in AP_FLASHCARDS.items():
        # Find the array for this subject and append before its closing ]
        # Pattern: math: [ ... ]
        pat = f"  {subj}: ["
        idx = html.find(pat, cards_start)
        if idx == -1:
            print(f"  ! Could not find {subj} array in CARDS")
            continue
        arr_start = html.index('[', idx)
        # Find matching ]
        depth = 0
        i = arr_start
        in_str = False
        str_char = None
        while i < len(html):
            ch = html[i]
            if in_str:
                if ch == '\\': i += 2; continue
                if ch == str_char: in_str = False
            else:
                if ch in ('"', "'", '`'):
                    in_str = True; str_char = ch
                elif ch == '[': depth += 1
                elif ch == ']':
                    depth -= 1
                    if depth == 0:
                        arr_end = i
                        break
            i += 1
        else:
            print(f"  ! Could not find end of {subj} array")
            continue
        # Build AP cards JS snippet
        cards_js = ',\n    ' + ',\n    '.join(
            f"{{g:'ap',term:{json.dumps(c['term'])},def:{json.dumps(c['def'])}}}"
            for c in cards
        )
        html = html[:arr_end] + cards_js + '\n  ' + html[arr_end:]
        # Update cards_start so indices remain valid for next iteration
        cards_start = html.find('const CARDS')
        print(f"  ✓ AP cards added to {subj}")
else:
    print("  ✓ AP cards already present")

# Fix grade filter to include 'ap' option
if "setGrade('ap')" not in html:
    # Find the grade filter rendering
    old_gb = "[6,7,8,9,10,11,12].map(g=>"
    new_gb = "[6,7,8,9,10,11,12,'ap'].map(g=>"
    html = html.replace(old_gb, new_gb)
    # Fix the label for 'ap' in the button
    old_label = "`<button class=\"grade-btn${activeGrade==g?' active':''}\" onclick=\"setGrade(${g})\">${g}</button>`"
    new_label = "`<button class=\"grade-btn${activeGrade==g?' active':''}\" onclick=\"setGrade(${JSON.stringify(g)})\">${g==='ap'?'AP':g}</button>`"
    if old_label in html:
        html = html.replace(old_label, new_label)
        print("  ✓ Grade filter updated to include AP")
    else:
        # Try alternate pattern
        html = html.replace(
            "onclick=\"setGrade(${g})\">${g}</button>`",
            "onclick=\"setGrade(${JSON.stringify(g)})\">${g==='ap'?'AP':g}</button>`"
        )
        print("  ✓ Grade filter onclick updated")

# Fix buildDeck filter for 'ap' grade
# The filter uses: activeGrade==='all' || c.g===activeGrade
# This should work for 'ap' already since c.g will be 'ap' string
# But double-check the filter isn't doing numeric comparison
if ".filter(c=>" in html:
    # Check what the filter looks like
    idx = html.find(".filter(c=>")
    ctx = html[idx:idx+120]
    print(f"  Filter context: {ctx[:80]}")

with open(f'{BASE}/flashcards.html', 'w') as f:
    f.write(html)
print("  ✓ flashcards.html saved\n")

# ═══════════════════════════════════════════════════════════════════════════════
# 4. PATCH tutor.html — add AP awareness to the knowledge base
# ═══════════════════════════════════════════════════════════════════════════════
print("Patching tutor.html...")
with open(f'{BASE}/tutor.html', 'r') as f:
    html = f.read()

AP_TUTOR_KNOWLEDGE = """
    // ── AP Courses ──────────────────────────────────────────────────────────
    {
      subject:"AP Calculus", grade:"ap",
      topic:"Derivatives",
      explanation:"A derivative measures instantaneous rate of change. Key rules: Power rule d/dx[xⁿ]=nxⁿ⁻¹; Product rule (uv)′=u′v+uv′; Chain rule d/dx[f(g(x))]=f′(g(x))·g′(x); Quotient rule (u/v)′=(u′v−uv′)/v².",
      examples:["d/dx[x³]=3x²","d/dx[sin x]=cos x","d/dx[eˣ]=eˣ"],
      practice:"Find d/dx[x²·ln(x)]. Use product rule: 2x·ln(x)+x²·(1/x)=2x·ln(x)+x."
    },
    {
      subject:"AP Calculus", grade:"ap",
      topic:"Integrals",
      explanation:"Integration is the reverse of differentiation. ∫xⁿdx = xⁿ⁺¹/(n+1)+C. Definite integrals compute area: ∫[a,b] f(x)dx = F(b)−F(a). Substitution (u-sub) handles composite functions.",
      examples:["∫x²dx = x³/3+C","∫cos x dx = sin x+C","∫eˣdx = eˣ+C"],
      practice:"Evaluate ∫[0,2] 3x² dx. Antiderivative = x³. F(2)−F(0)=8−0=8."
    },
    {
      subject:"AP Statistics", grade:"ap",
      topic:"Hypothesis Testing",
      explanation:"A hypothesis test evaluates evidence against H₀ (null). Steps: state H₀ and H₁, choose α, compute test statistic, find p-value, decide. If p<α, reject H₀. Types: z-test (known σ), t-test (unknown σ), chi-square (categorical).",
      examples:["z=(x̄−μ)/(σ/√n)","p-value < 0.05 → reject H₀"],
      practice:"Is p=0.03 significant at α=0.05? Yes, 0.03<0.05 → reject H₀."
    },
    {
      subject:"AP Biology", grade:"ap",
      topic:"Cellular Respiration",
      explanation:"Aerobic respiration: C₆H₁₂O₆+6O₂→6CO₂+6H₂O+~36–38 ATP. Stages: Glycolysis (cytoplasm, 2 ATP net), Pyruvate oxidation, Krebs Cycle (matrix, 2 ATP), Electron Transport Chain (inner membrane, ~32–34 ATP). NADH and FADH₂ shuttle electrons to ETC.",
      examples:["Glycolysis: glucose → 2 pyruvate + 2 ATP + 2 NADH","ETC: O₂ is final electron acceptor → H₂O"],
      practice:"Where does the Krebs cycle occur? Mitochondrial matrix."
    },
    {
      subject:"AP Chemistry", grade:"ap",
      topic:"Chemical Equilibrium",
      explanation:"At equilibrium, forward and reverse reaction rates are equal. Equilibrium constant K=[products]/[reactants] (exclude pure solids/liquids). Le Chatelier's principle: adding reactant shifts right; removing product shifts right; increasing pressure favors fewer moles of gas.",
      examples:["For N₂+3H₂⇌2NH₃, K=[NH₃]²/([N₂][H₂]³)"],
      practice:"If K>1, products are favored at equilibrium. If K<1, reactants are favored."
    },
    {
      subject:"AP Physics", grade:"ap",
      topic:"Mechanics",
      explanation:"Newton's Laws: (1) Inertia — objects stay in motion unless acted on; (2) F=ma; (3) Action-reaction pairs. Energy: KE=½mv², PE=mgh, Work=Fd cosθ. Conservation of energy: KE+PE=constant (no friction). Momentum p=mv; impulse=Δp=FΔt.",
      examples:["F=ma: 10 kg × 5 m/s² = 50 N","KE=½(2)(3²)=9 J"],
      practice:"A 3 kg ball falls 5 m. Its speed at impact: v=√(2gh)=√(2·9.8·5)≈9.9 m/s."
    },
    {
      subject:"AP English Language", grade:"ap",
      topic:"Rhetorical Analysis",
      explanation:"Analyze how an author's choices (diction, syntax, tone, appeals, structure) achieve purpose with a specific audience. Ethos=credibility; Pathos=emotion; Logos=logic. Identify the rhetorical situation and evaluate effectiveness of strategies.",
      examples:["Anaphora: 'I have a dream...' (King) builds momentum","Antithesis: 'Ask not what your country can do for you...' (JFK) creates contrast"],
      practice:"In a passage arguing for climate action, identify one ethos appeal and explain how it builds credibility."
    },
    {
      subject:"AP US History", grade:"ap",
      topic:"Causes of the Civil War",
      explanation:"The Civil War (1861–65) was primarily caused by slavery—its expansion into new territories and Southern states' insistence on maintaining it. Key events: Missouri Compromise, Compromise of 1850, Kansas-Nebraska Act, Dred Scott decision, John Brown's Raid, 1860 election of Lincoln. Confederacy formed before Lincoln took office.",
      examples:["'Bleeding Kansas' — violent conflict over slavery in new territories","Dred Scott (1857): ruled Congress couldn't ban slavery in territories"],
      practice:"How did the Kansas-Nebraska Act undermine the Missouri Compromise? It allowed popular sovereignty, reopening territories to slavery."
    },
    {
      subject:"AP Psychology", grade:"ap",
      topic:"Learning and Conditioning",
      explanation:"Classical conditioning (Pavlov): neutral stimulus paired with unconditioned stimulus → conditioned response. Operant conditioning (Skinner): reinforcement (positive/negative) increases behavior; punishment decreases it. Schedules: continuous, fixed-ratio, variable-ratio (most resistant to extinction), fixed-interval, variable-interval.",
      examples:["Pavlov: bell (NS) + food (US) → salivation (CR)","Variable-ratio: slot machines — unpredictable reinforcement"],
      practice:"A student gets candy every 5th correct answer. What schedule is this? Fixed-ratio (FR-5)."
    },
    {
      subject:"AP Computer Science", grade:"ap",
      topic:"Algorithms and Data Structures",
      explanation:"Key structures: Array O(1) access, O(n) search; Linked List O(n) access; Stack LIFO; Queue FIFO; Binary Search Tree O(log n) search if balanced. Algorithm efficiency: O(1) constant, O(log n) logarithmic, O(n) linear, O(n²) quadratic. Binary search requires sorted data, runs in O(log n).",
      examples:["Binary search on 1000 items: ~10 steps","Bubble sort: O(n²) — inefficient for large arrays"],
      practice:"What is the time complexity of searching an unsorted array of n elements? O(n) — must check each element."
    },
"""

# Find tutor knowledge base and inject AP entries
if 'grade:"ap"' not in html:
    # Find the knowledge array
    kb_idx = html.find('const KNOWLEDGE')
    if kb_idx == -1:
        kb_idx = html.find('const knowledge')
    if kb_idx != -1:
        arr_start = html.index('[', kb_idx)
        # Find closing ]
        depth = 0
        i = arr_start
        in_str = False
        str_char = None
        arr_end = -1
        while i < len(html):
            ch = html[i]
            if in_str:
                if ch == '\\': i += 2; continue
                if ch == str_char: in_str = False
            else:
                if ch in ('"', "'", '`'):
                    in_str = True; str_char = ch
                elif ch == '[': depth += 1
                elif ch == ']':
                    depth -= 1
                    if depth == 0: arr_end = i; break
            i += 1
        if arr_end > 0:
            html = html[:arr_end] + AP_TUTOR_KNOWLEDGE + '\n  ' + html[arr_end:]
            print("  ✓ AP knowledge entries added to tutor")
        else:
            print("  ! Could not find end of KNOWLEDGE array")
    else:
        print("  ! KNOWLEDGE array not found in tutor.html")
else:
    print("  ✓ AP knowledge already present in tutor.html")

with open(f'{BASE}/tutor.html', 'w') as f:
    f.write(html)
print("  ✓ tutor.html saved\n")

print("All done!")
