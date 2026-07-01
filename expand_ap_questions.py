#!/usr/bin/env python3
"""Expand original AP units from 5 to 20 questions."""
import json, re

def find_end(text, start):
    depth=0; i=start; in_str=False; esc=False
    while i < len(text):
        c=text[i]
        if esc: esc=False
        elif c=='\\' and in_str: esc=True
        elif c=='"' and not esc: in_str=not in_str
        elif not in_str:
            if c=='{': depth+=1
            elif c=='}':
                depth-=1
                if depth==0: return i
        i+=1
    return -1

def Q(q, choices, a, diff="medium"):
    return {"q": q, "choices": choices, "answer": a, "difficulty": diff}

# 15 extra questions for each of the 16 units
EXTRA = {
("ap","math",0): [ # AP Calculus AB — Limits & Continuity
  Q("What is lim(x→2) (x²-4)/(x-2)?",["1","2","4","0"],"4","easy"),
  Q("A function f is continuous at x=a if lim(x→a) f(x) equals:",["f(0)","f(a)","0","undefined"],"f(a)","easy"),
  Q("What is lim(x→0) sin(x)/x?",["0","∞","1","undefined"],"1","medium"),
  Q("Which describes a removable discontinuity?",["A jump in the graph","A hole in the graph","A vertical asymptote","An oscillation"],"A hole in the graph","medium"),
  Q("lim(x→∞) (3x²+1)/(x²+5) equals:",["3","1","0","∞"],"3","medium"),
  Q("What is lim(x→0⁺) ln(x)?",["0","1","-∞","∞"],"-∞","medium"),
  Q("The Squeeze Theorem requires the squeezed function to be:",["greater than both bounds","between two functions with the same limit","differentiable","continuous"],"between two functions with the same limit","medium"),
  Q("lim(x→4) √x equals:",["2","4","√2","16"],"2","easy"),
  Q("Which condition is NOT required for continuity at x=a?",["f(a) is defined","lim exists at a","f is differentiable at a","limit equals f(a)"],"f is differentiable at a","hard"),
  Q("lim(x→0) (e^x - 1)/x equals:",["0","e","1","∞"],"1","hard"),
  Q("A vertical asymptote occurs when:",["the function equals zero","the limit is infinite","the function is continuous","the derivative is zero"],"the limit is infinite","medium"),
  Q("lim(x→π) cos(x) equals:",["0","1","-1","π"],"-1","easy"),
  Q("If f(x) = x² for x<2 and f(x) = 5 for x≥2, is f continuous at x=2?",["Yes","No, jump discontinuity","No, removable discontinuity","No, infinite discontinuity"],"No, jump discontinuity","hard"),
  Q("lim(x→0) x·sin(1/x) equals:",["1","0","∞","undefined"],"0","hard"),
  Q("The Intermediate Value Theorem applies to functions that are:",["differentiable","continuous on [a,b]","increasing","bounded"],"continuous on [a,b]","medium"),
],
("ap","math",1): [ # AP Calculus AB — Derivatives
  Q("The derivative of sin(x) is:",["cos(x)","-cos(x)","-sin(x)","tan(x)"],"cos(x)","easy"),
  Q("By the chain rule, d/dx[f(g(x))] =",["f'(x)g'(x)","f'(g(x))·g'(x)","f(g'(x))","f'(x)+g'(x)"],"f'(g(x))·g'(x)","medium"),
  Q("The derivative of e^x is:",["xe^(x-1)","e^x","e^(x-1)","ln(x)"],"e^x","easy"),
  Q("d/dx[ln(x)] =",["1/x","ln(x)","x","e^x"],"1/x","easy"),
  Q("The Power Rule states d/dx[xⁿ] =",["xⁿ","nxⁿ","nxⁿ⁻¹","(n-1)xⁿ⁻¹"],"nxⁿ⁻¹","easy"),
  Q("A critical point occurs where:",["f(x) = 0","f'(x) = 0 or undefined","f''(x) = 0","f is continuous"],"f'(x) = 0 or undefined","medium"),
  Q("The second derivative test: if f''(c) > 0 at a critical point, it is a:",["local maximum","local minimum","inflection point","saddle point"],"local minimum","medium"),
  Q("Implicit differentiation is used when:",["y is an explicit function of x","x and y are mixed in one equation","the derivative is undefined","the function is linear"],"x and y are mixed in one equation","medium"),
  Q("The Product Rule: d/dx[f·g] =",["f'g'","f'g + fg'","fg' - f'g","f/g"],"f'g + fg'","medium"),
  Q("d/dx[cos(x)] =",["sin(x)","-sin(x)","cos(x)","-cos(x)"],"-sin(x)","easy"),
  Q("A function is concave up where:",["f' > 0","f'' > 0","f'' < 0","f' < 0"],"f'' > 0","medium"),
  Q("The Quotient Rule: d/dx[f/g] =",["f'g - fg'","(f'g - fg')/g²","(fg' - f'g)/g²","f'g + fg'"],"(f'g - fg')/g²","hard"),
  Q("d/dx[tan(x)] =",["sin(x)","sec(x)","sec²(x)","cot(x)"],"sec²(x)","medium"),
  Q("Rolle's Theorem guarantees a c where f'(c)=0 when f is:",["differentiable everywhere","continuous on [a,b], diff on (a,b), f(a)=f(b)","a polynomial","strictly increasing"],"continuous on [a,b], diff on (a,b), f(a)=f(b)","hard"),
  Q("Related rates problems involve differentiating with respect to:",["x","y","time t","position"],"time t","medium"),
],
("ap","math",2): [ # AP Statistics — Data Analysis
  Q("The mean of {2,4,6,8,10} is:",["5","6","5.5","4"],"6","easy"),
  Q("A z-score measures:",["the median","how many SDs a value is from the mean","the variance","the range"],"how many SDs a value is from the mean","easy"),
  Q("Which is resistant to outliers?",["mean","standard deviation","median","range"],"median","medium"),
  Q("In a normal distribution, about what % of data falls within 1 SD of the mean?",["68%","95%","99.7%","50%"],"68%","medium"),
  Q("The interquartile range (IQR) is:",["Q3 - Q1","Q2 - Q1","max - min","mean - median"],"Q3 - Q1","easy"),
  Q("A scatterplot is used to display:",["a single quantitative variable","relationship between two quantitative variables","categorical data","frequency"],"relationship between two quantitative variables","easy"),
  Q("Correlation coefficient r = 0 indicates:",["strong positive relationship","no linear relationship","perfect negative correlation","moderate relationship"],"no linear relationship","medium"),
  Q("A histogram skewed right has:",["mean < median","mean = median","mean > median","no mode"],"mean > median","hard"),
  Q("Which plot shows five-number summary?",["histogram","bar chart","boxplot","stemplot"],"boxplot","easy"),
  Q("Standard deviation measures:",["center","spread","shape","skewness"],"spread","easy"),
  Q("An outlier by the 1.5×IQR rule is any point:",["below Q1","above Q3","below Q1-1.5(IQR) or above Q3+1.5(IQR)","within 2 SDs"],"below Q1-1.5(IQR) or above Q3+1.5(IQR)","hard"),
  Q("The mode is the value that:",["appears most frequently","is in the middle","equals the mean","has the highest z-score"],"appears most frequently","easy"),
  Q("A dataset with high standard deviation is:",["clustered tightly","very spread out","symmetric","uniform"],"very spread out","medium"),
  Q("Simpson's Paradox occurs when:",["data is normally distributed","a trend reverses when data is combined vs separated","correlation implies causation","sample size is too small"],"a trend reverses when data is combined vs separated","hard"),
  Q("Lurking variables cause problems in:",["experimental design","establishing causation from observational data","calculating the mean","drawing boxplots"],"establishing causation from observational data","hard"),
],
("ap","math",3): [ # AP Precalculus — Functions & Modeling
  Q("The domain of f(x) = √(x-3) is:",["x ≥ 0","x ≥ 3","x > 3","all reals"],"x ≥ 3","easy"),
  Q("A function f is one-to-one if:",["it passes the vertical line test","it passes the horizontal line test","f(0) = 0","it is linear"],"it passes the horizontal line test","medium"),
  Q("The inverse of f(x) = 2x+1 is:",["f⁻¹(x) = (x-1)/2","f⁻¹(x) = 2x-1","f⁻¹(x) = x/2","f⁻¹(x) = 1/(2x+1)"],"f⁻¹(x) = (x-1)/2","medium"),
  Q("An exponential function f(x) = a·bˣ grows if:",["b < 0","0 < b < 1","b > 1","a < 0"],"b > 1","easy"),
  Q("log₂(8) equals:",["2","3","4","1"],"3","easy"),
  Q("The period of sin(2x) is:",["2π","π","4π","π/2"],"π","medium"),
  Q("A vertical asymptote of f(x) = 1/(x-2) is at:",["x = 0","x = 1","x = 2","y = 0"],"x = 2","easy"),
  Q("Which transformation shifts f(x) right by 3?",["f(x+3)","f(x-3)","f(x)+3","f(x)-3"],"f(x-3)","medium"),
  Q("An even function satisfies:",["f(-x) = f(x)","f(-x) = -f(x)","f(x+a) = f(x)","f(0) = 0"],"f(-x) = f(x)","medium"),
  Q("The range of f(x) = x² is:",["all reals","x ≥ 0","y ≥ 0","y > 0"],"y ≥ 0","easy"),
  Q("ln(e³) equals:",["e","1","3","3e"],"3","easy"),
  Q("A rational function has a hole when:",["numerator = 0","denominator = 0","both cancel a common factor","leading coefficients equal"],"both cancel a common factor","hard"),
  Q("The amplitude of 3sin(x) is:",["3","1","π","3π"],"3","easy"),
  Q("Composition (f∘g)(x) means:",["f(x) + g(x)","f(x)·g(x)","f(g(x))","g(f(x))"],"f(g(x))","medium"),
  Q("Which regression model fits data that doubles at equal intervals?",["linear","quadratic","exponential","sinusoidal"],"exponential","hard"),
],
("ap","science",0): [ # AP Biology — Cell Biology & Genetics
  Q("Which organelle is the site of ATP production?",["ribosome","mitochondria","nucleus","golgi apparatus"],"mitochondria","easy"),
  Q("DNA replication is:",["conservative","semi-conservative","dispersive","random"],"semi-conservative","medium"),
  Q("Mendel's Law of Segregation states that:",["genes are inherited in pairs that separate during gamete formation","all offspring are identical","traits blend together","genes are linked on chromosomes"],"genes are inherited in pairs that separate during gamete formation","medium"),
  Q("A test cross involves crossing an organism of unknown genotype with:",["a homozygous dominant","a homozygous recessive","a heterozygote","an F1 offspring"],"a homozygous recessive","medium"),
  Q("Which phase of mitosis do chromosomes align at the cell's equator?",["prophase","anaphase","metaphase","telophase"],"metaphase","easy"),
  Q("The fluid mosaic model describes:",["DNA structure","cell membrane structure","enzyme activity","chromosome organization"],"cell membrane structure","medium"),
  Q("mRNA is produced during:",["translation","transcription","replication","transduction"],"transcription","easy"),
  Q("Codominance in genetics is shown by:",["Aa producing an intermediate phenotype","AB blood type showing both A and B antigens","recessive traits disappearing","all offspring identical"],"AB blood type showing both A and B antigens","hard"),
  Q("Crossing over occurs during:",["mitosis prophase","meiosis I","meiosis II","S phase"],"meiosis I","hard"),
  Q("Which is NOT a function of proteins?",["enzyme catalysis","structural support","energy storage via glycogen","signal transduction"],"energy storage via glycogen","hard"),
  Q("The cell cycle checkpoint at G1 monitors:",["DNA damage before replication","chromosome alignment","cytokinesis","spindle formation"],"DNA damage before replication","medium"),
  Q("Hardy-Weinberg equilibrium requires:",["natural selection","random mating and no evolution","genetic drift","mutation pressure"],"random mating and no evolution","hard"),
  Q("Which base pairs with adenine in DNA?",["guanine","cytosine","thymine","uracil"],"thymine","easy"),
  Q("Osmosis moves water toward:",["higher solute concentration","lower solute concentration","higher pressure","lower temperature"],"higher solute concentration","medium"),
  Q("A frameshift mutation results from:",["substitution of one base","insertion or deletion of bases","UV radiation only","point mutation"],"insertion or deletion of bases","medium"),
],
("ap","science",1): [ # AP Chemistry — Atomic Structure & Bonding
  Q("The atomic number represents the number of:",["neutrons","protons","electrons + protons","mass units"],"protons","easy"),
  Q("An ionic bond forms between:",["two nonmetals","a metal and nonmetal","two metals","carbon atoms"],"a metal and nonmetal","easy"),
  Q("Which quantum number describes an orbital's shape?",["n (principal)","l (angular momentum)","ml (magnetic)","ms (spin)"],"l (angular momentum)","hard"),
  Q("Electronegativity increases across a period because:",["atomic radius increases","nuclear charge increases","electron shielding increases","mass increases"],"nuclear charge increases","medium"),
  Q("A polar covalent bond has:",["equal sharing of electrons","unequal sharing of electrons","complete transfer of electrons","no electron interaction"],"unequal sharing of electrons","medium"),
  Q("The electron configuration of Na is:",["1s²2s²2p⁶3s¹","1s²2s²2p⁵","1s²2s²2p⁶","1s²2s¹"],"1s²2s²2p⁶3s¹","medium"),
  Q("VSEPR theory predicts:",["bond energies","molecular geometry","reaction rates","electronegativity"],"molecular geometry","easy"),
  Q("London dispersion forces exist between:",["only polar molecules","all molecules","only ionic compounds","only metals"],"all molecules","medium"),
  Q("Which has the highest first ionization energy?",["Na","Mg","Al","Ne"],"Ne","hard"),
  Q("A Lewis structure shows:",["3D molecular shape","valence electron arrangement","bond angles only","nuclear positions"],"valence electron arrangement","medium"),
  Q("The octet rule states atoms tend to have:",["8 protons","8 neutrons","8 valence electrons","8 bonds"],"8 valence electrons","easy"),
  Q("Isotopes differ in number of:",["protons","electrons","neutrons","bonds"],"neutrons","easy"),
  Q("sp³ hybridization produces what geometry?",["linear","trigonal planar","tetrahedral","octahedral"],"tetrahedral","medium"),
  Q("Which bond is strongest?",["single covalent","double covalent","triple covalent","ionic"],"triple covalent","medium"),
  Q("The Aufbau principle states electrons fill:",["highest energy orbitals first","lowest energy orbitals first","randomly","s orbitals last"],"lowest energy orbitals first","medium"),
],
("ap","science",2): [ # AP Physics 1 — Mechanics
  Q("Newton's 2nd Law states F =",["mv","ma","m/a","a/m"],"ma","easy"),
  Q("A projectile's horizontal velocity (ignoring air resistance) is:",["increasing","decreasing","zero","constant"],"constant","medium"),
  Q("Work is defined as:",["force × time","force × distance × cos(θ)","mass × acceleration","momentum × velocity"],"force × distance × cos(θ)","medium"),
  Q("The unit of energy is the:",["newton","joule","watt","pascal"],"joule","easy"),
  Q("Conservation of momentum applies when:",["net external force is zero","there is friction","kinetic energy is conserved","acceleration is constant"],"net external force is zero","medium"),
  Q("At the top of a pendulum's swing, the pendulum has:",["maximum KE","minimum PE","maximum PE","zero total energy"],"maximum PE","medium"),
  Q("In uniform circular motion, acceleration points:",["tangentially","outward from center","inward toward center","in direction of velocity"],"inward toward center","medium"),
  Q("Torque depends on force and:",["mass","speed","lever arm length","acceleration"],"lever arm length","easy"),
  Q("An elastic collision conserves:",["momentum only","kinetic energy only","both momentum and kinetic energy","neither"],"both momentum and kinetic energy","hard"),
  Q("Power is defined as:",["work/time","force × distance","mass × velocity","energy × time"],"work/time","easy"),
  Q("On a frictionless incline, what force causes acceleration?",["normal force","component of gravity parallel to slope","component of gravity perpendicular to slope","tension"],"component of gravity parallel to slope","medium"),
  Q("The slope of a velocity-time graph represents:",["displacement","speed","acceleration","force"],"acceleration","medium"),
  Q("Impulse equals:",["force × distance","change in momentum","mass × acceleration","work done"],"change in momentum","medium"),
  Q("Two objects with equal momentum but different masses have different:",["velocities","forces","positions","weights only"],"velocities","hard"),
  Q("Static friction is _____ kinetic friction.",["less than","equal to","greater than or equal to","independent of"],"greater than or equal to","hard"),
],
("ap","science",3): [ # AP Environmental Science — Ecosystems
  Q("Producers in an ecosystem are:",["herbivores","decomposers","photosynthetic organisms","carnivores"],"photosynthetic organisms","easy"),
  Q("The 10% rule in energy transfer means:",["10% of organisms survive","only 10% of energy passes to the next trophic level","10% of species are endangered","ecosystems are 10% efficient"],"only 10% of energy passes to the next trophic level","medium"),
  Q("Biodiversity is HIGHEST in:",["tundra","tropical rainforest","desert","polar ice"],"tropical rainforest","easy"),
  Q("A keystone species has:",["the largest population","disproportionately large ecosystem impact","the most offspring","no predators"],"disproportionately large ecosystem impact","medium"),
  Q("Bioaccumulation refers to:",["CO₂ buildup","toxins concentrating up the food chain","biodiversity accumulating over time","nutrient cycling"],"toxins concentrating up the food chain","medium"),
  Q("The nitrogen cycle includes which process converting N₂ to ammonia?",["nitrification","denitrification","nitrogen fixation","ammonification"],"nitrogen fixation","hard"),
  Q("Eutrophication is caused by excess:",["CO₂","nutrients (N and P)","sediment","heavy metals"],"nutrients (N and P)","medium"),
  Q("Primary succession begins on:",["burned forest","abandoned field","bare rock with no soil","flooded land"],"bare rock with no soil","medium"),
  Q("The greenhouse effect is caused by gases that:",["block incoming sunlight","trap outgoing infrared radiation","reflect UV rays","absorb nitrogen"],"trap outgoing infrared radiation","medium"),
  Q("An ecological niche describes an organism's:",["habitat only","role and position in its ecosystem","diet only","geographic range"],"role and position in its ecosystem","medium"),
  Q("Which is a renewable resource?",["coal","oil","solar energy","natural gas"],"solar energy","easy"),
  Q("Deforestation most directly contributes to:",["ocean acidification","increased atmospheric CO₂","ozone depletion","soil salinization"],"increased atmospheric CO₂","medium"),
  Q("The carrying capacity (K) is the:",["growth rate","maximum sustainable population size","minimum viable population","birth rate"],"maximum sustainable population size","medium"),
  Q("Which best describes a mutualistic relationship?",["one benefits, one harmed","both organisms benefit","one benefits, one unaffected","both are harmed"],"both organisms benefit","easy"),
  Q("Ocean acidification results from oceans absorbing:",["nitrogen","CO₂","methane","sulfur dioxide"],"CO₂","medium"),
],
("ap","ela",0): [ # AP English Language — Rhetoric & Argumentation
  Q("Ethos in rhetoric appeals to:",["emotion","logic","the speaker's credibility","shared values"],"the speaker's credibility","easy"),
  Q("A claim in argumentation is:",["supporting evidence","the main position being argued","a counterargument","background information"],"the main position being argued","easy"),
  Q("Anaphora is the repetition of:",["ending words","beginning words/phrases","similar sentence structures","rhyming sounds"],"beginning words/phrases","medium"),
  Q("A rhetorical question is asked:",["to gain information","for effect, not an answer","to challenge the audience","in formal debates only"],"for effect, not an answer","easy"),
  Q("Logos appeals to:",["credibility","emotion","logic and reason","shared culture"],"logic and reason","easy"),
  Q("A concession in argumentation is when the writer:",["ignores counterarguments","acknowledges a valid opposing point","restates the thesis","provides evidence"],"acknowledges a valid opposing point","medium"),
  Q("Synthesis in AP Lang means:",["summarizing one source","combining multiple sources to support an argument","comparing two texts only","quoting directly"],"combining multiple sources to support an argument","medium"),
  Q("Which is an example of a logical fallacy?",["using statistics","personal anecdote as universal proof","acknowledging counterarguments","citing an expert"],"personal anecdote as universal proof","hard"),
  Q("An author's purpose is best understood by examining:",["only the title","the diction, structure, and rhetorical choices together","the publication date","word count"],"the diction, structure, and rhetorical choices together","hard"),
  Q("Pathos appeals to:",["facts","the speaker's credentials","the audience's emotions","legal authority"],"the audience's emotions","easy"),
  Q("The rhetorical situation includes:",["speaker, audience, purpose, context","thesis only","evidence and claims","genre and format"],"speaker, audience, purpose, context","medium"),
  Q("A rebuttal directly:",["supports the main claim","addresses and counters a counterargument","introduces new evidence","summarizes the argument"],"addresses and counters a counterargument","medium"),
  Q("Parallel structure in argumentation creates:",["emotional appeal","rhythm and clarity","a logical fallacy","a concession"],"rhythm and clarity","medium"),
  Q("An ad hominem fallacy attacks:",["the argument's logic","the person making the argument","statistical evidence","the audience"],"the person making the argument","hard"),
  Q("Which best defines a nuanced argument?",["one that ignores complexity","one that acknowledges complexity and qualifies claims","a simple yes/no stance","an emotional appeal"],"one that acknowledges complexity and qualifies claims","hard"),
],
("ap","ela",1): [ # AP English Literature — Literary Analysis
  Q("The protagonist is the:",["villain","narrator","main character","antagonist's ally"],"main character","easy"),
  Q("A foil character serves to:",["replace the protagonist","highlight traits of another character by contrast","introduce the setting","resolve the conflict"],"highlight traits of another character by contrast","medium"),
  Q("Dramatic irony occurs when:",["the character knows something the audience doesn't","the audience knows something the character doesn't","the author uses sarcasm","two characters misunderstand each other"],"the audience knows something the character doesn't","medium"),
  Q("The bildungsroman genre follows:",["a romance story","a character's coming-of-age journey","a historical narrative","a tragic hero's downfall"],"a character's coming-of-age journey","medium"),
  Q("Catharsis in tragedy refers to:",["the climax","emotional purging in the audience","the protagonist's flaw","rising action"],"emotional purging in the audience","hard"),
  Q("An unreliable narrator is one who:",["tells the story in third person","cannot be fully trusted due to bias or limited knowledge","knows everything about all characters","narrates multiple storylines"],"cannot be fully trusted due to bias or limited knowledge","medium"),
  Q("Hubris is:",["excessive pride leading to downfall","humility","fear","a literary device for flashback"],"excessive pride leading to downfall","medium"),
  Q("The denouement is:",["rising action","the central conflict","resolution after the climax","the inciting incident"],"resolution after the climax","easy"),
  Q("Metafiction is fiction that:",["uses real historical events","is self-aware and draws attention to its fictional nature","follows a traditional plot structure","avoids symbolism"],"is self-aware and draws attention to its fictional nature","hard"),
  Q("An epithet is:",["a type of simile","a descriptive phrase regularly used for a person or thing","a form of irony","a plot device"],"a descriptive phrase regularly used for a person or thing","hard"),
  Q("Which literary period emphasized reason and order?",["Romanticism","Neoclassicism","Modernism","Postmodernism"],"Neoclassicism","hard"),
  Q("Stream of consciousness is a narrative technique that:",["uses dialogue exclusively","mimics the continuous flow of a character's thoughts","employs third-person omniscient narration","structures events chronologically"],"mimics the continuous flow of a character's thoughts","medium"),
  Q("In poetry, a volta is:",["a rhythmic pattern","a turn or shift in thought or argument","a type of rhyme scheme","the final couplet"],"a turn or shift in thought or argument","medium"),
  Q("An archetype is:",["a unique character","a universal pattern or symbol","a narrative device","a type of foreshadowing"],"a universal pattern or symbol","medium"),
  Q("Synecdoche uses:",["a part to represent the whole","the whole to represent a part","an unrelated comparison","sound devices"],"a part to represent the whole","hard"),
],
("ap","history",0): [ # AP US History — Colonial to Civil War
  Q("The Mayflower Compact (1620) established the principle of:",["religious freedom","self-governance","separation of church and state","free trade"],"self-governance","easy"),
  Q("The Great Awakening was primarily a:",["political movement","religious revival","economic reform","military campaign"],"religious revival","easy"),
  Q("The Articles of Confederation failed mainly because:",["they gave too much power to the president","Congress lacked power to tax","they allowed slavery","they excluded western states"],"Congress lacked power to tax","medium"),
  Q("Manifest Destiny was the belief that:",["the US should remain isolated","the US was destined to expand across the continent","states should govern themselves","democracy should spread globally"],"the US was destined to expand across the continent","easy"),
  Q("The Missouri Compromise (1820) addressed:",["tariffs","slavery in new territories","Native American rights","British impressment"],"slavery in new territories","medium"),
  Q("The Second Great Awakening influenced:",["industrialization directly","abolition and social reform movements","westward expansion mainly","foreign policy"],"abolition and social reform movements","medium"),
  Q("Which act extended slavery by allowing territories to decide for themselves?",["Missouri Compromise","Compromise of 1850","Kansas-Nebraska Act","Dred Scott Decision"],"Kansas-Nebraska Act","medium"),
  Q("Abolitionism in the antebellum period was primarily a:",["Southern movement","Northern movement with some Southern supporters","congressional initiative","government policy"],"Northern movement with some Southern supporters","hard"),
  Q("The Dred Scott decision ruled that:",["slavery was unconstitutional","African Americans were not citizens","Congress could ban slavery","slaves in free states were free"],"African Americans were not citizens","medium"),
  Q("The Nullification Crisis involved:",["states refusing to enforce federal tariffs","secession","banking regulation","land disputes"],"states refusing to enforce federal tariffs","medium"),
  Q("Which best describes Jacksonian democracy?",["expansion of rights to all people","expansion of voting rights for white men","equal rights for all races","a parliamentary system"],"expansion of voting rights for white men","hard"),
  Q("The Compromise of 1850 included:",["abolishing slavery in DC","admitting California as a free state","expanding slavery westward","repealing the Missouri Compromise"],"admitting California as a free state","hard"),
  Q("Lincoln's primary stated goal at the start of the Civil War was to:",["abolish slavery immediately","preserve the Union","punish the South","free all enslaved people"],"preserve the Union","medium"),
  Q("The Underground Railroad was:",["a literal railroad system","a network helping enslaved people escape North","a congressional initiative","a Southern transportation system"],"a network helping enslaved people escape North","easy"),
  Q("Which battle is considered the turning point of the Civil War?",["Bull Run","Antietam","Gettysburg","Fort Sumter"],"Gettysburg","medium"),
],
("ap","history",1): [ # AP World History — Global Connections
  Q("The Silk Road primarily facilitated:",["military conquest","cultural and commercial exchange","political alliances","agricultural expansion"],"cultural and commercial exchange","easy"),
  Q("The Black Death originated in:",["Europe","the Middle East","Central Asia","North Africa"],"Central Asia","medium"),
  Q("Mercantilism held that:",["free trade benefits all nations","wealth is fixed and colonies exist to enrich the mother country","industrialization is paramount","gold is worthless"],"wealth is fixed and colonies exist to enrich the mother country","medium"),
  Q("The Columbian Exchange refers to:",["a trade treaty","transfer of crops, animals, and diseases between hemispheres","Columbus's trade route","European colonization policies"],"transfer of crops, animals, and diseases between hemispheres","medium"),
  Q("The Ottoman Empire controlled which key trade route?",["Silk Road directly","eastern Mediterranean and routes to Asia","trans-Saharan trade","Atlantic trade"],"eastern Mediterranean and routes to Asia","hard"),
  Q("Which best describes the impact of the printing press?",["decreased literacy","spread of ideas and information rapidly","reduced religious conflict","slowed the Renaissance"],"spread of ideas and information rapidly","easy"),
  Q("The Industrial Revolution began in:",["France","Germany","Britain","United States"],"Britain","easy"),
  Q("Social Darwinism was used to justify:",["social welfare programs","imperialism and racial hierarchy","democratic revolutions","trade unions"],"imperialism and racial hierarchy","hard"),
  Q("The Treaty of Westphalia (1648) established:",["absolute monarchy","the concept of state sovereignty","free trade","religious unity"],"the concept of state sovereignty","hard"),
  Q("The Atlantic slave trade peaked during:",["the 1400s","the 1500s","the 1700s","the 1800s"],"the 1700s","medium"),
  Q("Nationalism in the 19th century primarily led to:",["global cooperation","unification and independence movements","colonial expansion","religious wars"],"unification and independence movements","medium"),
  Q("The Green Revolution of the 20th century involved:",["environmental protection","new agricultural technologies increasing crop yields","political revolutions","deforestation"],"new agricultural technologies increasing crop yields","medium"),
  Q("Which empire had the largest land area in history?",["Roman Empire","Mongol Empire","British Empire","Ottoman Empire"],"Mongol Empire","medium"),
  Q("Decolonization after WWII was driven by:",["economic prosperity in colonies","Cold War pressure and nationalist movements","voluntary withdrawal by empires","UN mandates exclusively"],"Cold War pressure and nationalist movements","hard"),
  Q("The Non-Aligned Movement during the Cold War sought:",["alliance with NATO","alliance with USSR","independence from both superpower blocs","economic isolation"],"independence from both superpower blocs","hard"),
],
("ap","history",2): [ # AP US Government — Constitution & Civil Liberties
  Q("The Bill of Rights consists of the first ___ amendments:",["5","10","15","20"],"10","easy"),
  Q("Judicial review was established by:",["the Constitution","Marbury v. Madison","Congress","the Bill of Rights"],"Marbury v. Madison","medium"),
  Q("The 1st Amendment protects:",["right to bear arms","freedom of speech, religion, press, assembly, petition","due process","equal protection"],"freedom of speech, religion, press, assembly, petition","easy"),
  Q("Federalism divides power between:",["the president and Congress","federal and state governments","courts and legislature","Republicans and Democrats"],"federal and state governments","easy"),
  Q("The Senate has ___ members:",["100","435","535","50"],"100","easy"),
  Q("Which clause requires states to honor other states' laws?",["Supremacy Clause","Full Faith and Credit Clause","Commerce Clause","Necessary and Proper Clause"],"Full Faith and Credit Clause","hard"),
  Q("An interest group primarily seeks to:",["win elections","influence public policy","govern directly","represent all citizens equally"],"influence public policy","medium"),
  Q("The Electoral College elects the:",["Congress","President","Supreme Court justices","Senate"],"President","easy"),
  Q("Due process rights are guaranteed by the ___ Amendment:",["1st","4th","5th","14th"],"14th","hard"),
  Q("The filibuster is used in the:",["House of Representatives","Senate","Supreme Court","White House"],"Senate","medium"),
  Q("Checks and balances ensure that:",["one branch dominates","no branch has unchecked power","the president controls Congress","courts write laws"],"no branch has unchecked power","easy"),
  Q("The Commerce Clause allows Congress to regulate:",["state elections","interstate commerce","the military only","tax rates"],"interstate commerce","medium"),
  Q("Political socialization is primarily shaped by:",["the media alone","family, school, peers, and media","the government","interest groups"],"family, school, peers, and media","medium"),
  Q("Incorporation doctrine extends Bill of Rights protections to:",["foreign nations","state governments via the 14th Amendment","federal agencies","Congress"],"state governments via the 14th Amendment","hard"),
  Q("Which best describes a unitary system of government?",["power shared between central and regional governments","central government holds supreme power","states are sovereign","no central authority exists"],"central government holds supreme power","hard"),
],
("ap","history",3): [ # AP Psychology — Behavior & Mental Processes
  Q("Classical conditioning was demonstrated by:",["Skinner","Watson","Pavlov","Freud"],"Pavlov","easy"),
  Q("In operant conditioning, reinforcement ___ a behavior.",["decreases","eliminates","increases","has no effect on"],"increases","easy"),
  Q("The id, ego, and superego are concepts from:",["behaviorism","cognitive psychology","psychoanalysis","humanism"],"psychoanalysis","easy"),
  Q("Long-term potentiation is associated with:",["sleep disorders","memory formation","hormonal changes","perception"],"memory formation","hard"),
  Q("The fight-or-flight response is controlled by the:",["parasympathetic nervous system","sympathetic nervous system","somatic nervous system","central nervous system only"],"sympathetic nervous system","medium"),
  Q("Which memory system holds information for seconds?",["long-term memory","semantic memory","sensory memory","procedural memory"],"sensory memory","medium"),
  Q("The heritability of a trait tells us:",["genes cause the trait","what proportion of variation in a population is due to genetics","the trait is entirely genetic","environment has no effect"],"what proportion of variation in a population is due to genetics","hard"),
  Q("Confirmation bias is the tendency to:",["seek information that confirms existing beliefs","change beliefs readily","ignore prior knowledge","accurately assess evidence"],"seek information that confirms existing beliefs","medium"),
  Q("The DSM-5 is used for:",["brain imaging","diagnosing mental disorders","prescribing medication","therapy techniques"],"diagnosing mental disorders","easy"),
  Q("Positive punishment involves:",["adding something pleasant","removing something unpleasant","adding something unpleasant","removing something pleasant"],"adding something unpleasant","hard"),
  Q("Which perspective emphasizes unconscious drives?",["behavioral","cognitive","psychodynamic","humanistic"],"psychodynamic","easy"),
  Q("The bystander effect states that people are less likely to help when:",["they are alone","others are present","the situation is clear","they know the victim"],"others are present","medium"),
  Q("Maslow's hierarchy places ___ at the top:",["safety","esteem","self-actualization","belonging"],"self-actualization","medium"),
  Q("Nature vs. nurture in psychology refers to:",["genetics vs. environment","brain vs. mind","conscious vs. unconscious","learning vs. instinct"],"genetics vs. environment","easy"),
  Q("An fMRI measures:",["electrical brain activity","brain blood flow and activity","neurotransmitter levels","hormone concentrations"],"brain blood flow and activity","medium"),
],
("ap","cs",0): [ # AP Computer Science A — Java Programming
  Q("In Java, which keyword creates an object?",["class","new","static","void"],"new","easy"),
  Q("An array of size n has valid indices from:",["1 to n","0 to n","0 to n-1","1 to n-1"],"0 to n-1","easy"),
  Q("Which is an example of inheritance in OOP?",["Dog class extends Animal","int x = 5","for loop","array declaration"],"Dog class extends Animal","easy"),
  Q("What does 'static' mean for a method?",["it can't be called","it belongs to the class, not instances","it returns nothing","it takes no parameters"],"it belongs to the class, not instances","medium"),
  Q("A recursive method must have:",["no parameters","a base case to stop recursion","a loop inside","only integer returns"],"a base case to stop recursion","medium"),
  Q("Which Java type stores true/false?",["int","String","boolean","char"],"boolean","easy"),
  Q("The ArrayList class differs from arrays in that:",["it has fixed size","it can grow dynamically","it stores only primitives","it cannot be iterated"],"it can grow dynamically","medium"),
  Q("Polymorphism allows:",["only one class to exist","a superclass reference to hold subclass objects","methods to be private","variables to be null"],"a superclass reference to hold subclass objects","hard"),
  Q("What is the output of System.out.println(10 % 3)?",["3","1","0","2"],"1","medium"),
  Q("A constructor in Java:",["returns a value","has the same name as the class","is always static","cannot take parameters"],"has the same name as the class","easy"),
  Q("Binary search requires the array to be:",["unsorted","sorted","of even length","of odd length"],"sorted","medium"),
  Q("Which loop guarantees at least one execution?",["for","while","do-while","enhanced for"],"do-while","medium"),
  Q("The keyword 'final' on a variable means:",["it's a method","it cannot be changed after initialization","it's public","it's an array"],"it cannot be changed after initialization","hard"),
  Q("What does the toString() method do?",["converts a number to int","returns a String representation of an object","deletes an object","compares two objects"],"returns a String representation of an object","medium"),
  Q("Big-O of O(n²) indicates:",["constant time","linear time","quadratic time","logarithmic time"],"quadratic time","hard"),
],
("ap","cs",1): [ # AP Computer Science Principles — Digital Concepts
  Q("Binary uses base:",["8","10","16","2"],"2","easy"),
  Q("The internet routes data using:",["circuit switching","packet switching","analog signals","direct connections"],"packet switching","medium"),
  Q("Lossy compression:",["preserves all data","discards some data to reduce file size","is used for text files","increases file size"],"discards some data to reduce file size","medium"),
  Q("An algorithm is:",["a programming language","a step-by-step procedure for solving a problem","a type of data","a computer component"],"a step-by-step procedure for solving a problem","easy"),
  Q("Metadata is:",["the main content of a file","data that describes other data","a type of encryption","program code"],"data that describes other data","medium"),
  Q("Crowdsourcing gathers contributions from:",["a single expert","a large group of people","only paid employees","automated systems"],"a large group of people","easy"),
  Q("Which is NOT a benefit of open-source software?",["free to use","community collaboration","proprietary restrictions","transparency"],"proprietary restrictions","medium"),
  Q("The domain name system (DNS) converts:",["IP addresses to binary","domain names to IP addresses","emails to packets","HTTP to HTTPS"],"domain names to IP addresses","medium"),
  Q("A virus differs from a worm in that a virus:",["spreads without user action","requires a host file to spread","is always harmful","only affects networks"],"requires a host file to spread","hard"),
  Q("Digital certificates are used for:",["data storage","verifying website identity","compressing files","routing packets"],"verifying website identity","medium"),
  Q("Which describes a DDoS attack?",["stealing passwords","overwhelming a server with traffic","encrypting files for ransom","phishing emails"],"overwhelming a server with traffic","medium"),
  Q("Abstraction in computing means:",["adding more details","hiding complexity behind simple interfaces","deleting unused code","optimizing algorithms"],"hiding complexity behind simple interfaces","medium"),
  Q("Moore's Law predicted that transistors on a chip would:",["decrease annually","double approximately every two years","remain constant","triple every decade"],"double approximately every two years","hard"),
  Q("Phishing attacks use:",["malware directly","deceptive messages to steal information","network breaches","physical theft"],"deceptive messages to steal information","easy"),
  Q("Which is an example of creative commons licensing?",["copyright — all rights reserved","public domain","proprietary software","trade secret"],"public domain","hard"),
],
}

# Now load tests.html and patch
html = open('/sessions/admiring-stoic-pascal/mnt/outputs/tests.html').read()

def find_end(text, start):
    depth=0; i=start; in_str=False; esc=False
    while i < len(text):
        c=text[i]
        if esc: esc=False
        elif c=='\\' and in_str: esc=True
        elif c=='"' and not esc: in_str=not in_str
        elif not in_str:
            if c=='{': depth+=1
            elif c=='}':
                depth-=1
                if depth==0: return i
        i+=1
    return -1

start = html.index('const TESTS = ') + len('const TESTS = ')
end = find_end(html, start)
tests = json.loads(html[start:end+1])

# Extend questions
for (grade, subj, unit_idx), extra_qs in EXTRA.items():
    tests[grade][subj][unit_idx]['questions'].extend(extra_qs)
    total = len(tests[grade][subj][unit_idx]['questions'])
    print(f"  {grade}/{subj}/u{unit_idx}: now {total} questions")

new_json = json.dumps(tests, ensure_ascii=False, separators=(',',':'))
new_html = html[:start] + new_json + html[end+1:]
open('/sessions/admiring-stoic-pascal/mnt/outputs/tests.html', 'w').write(new_html)
print(f"\nDone. File size: {len(new_html):,}")
