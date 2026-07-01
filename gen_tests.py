#!/usr/bin/env python3
"""
gen_tests.py
Creates tests.html — one 20-question unit test for every unit in the curriculum.
Question mix per unit: 10 MC · 6 Short Answer · 4 Show Work
Run: python3 gen_tests.py
"""
import json, pathlib, random, math
random.seed(7)

def mc(q, choices, correct, exp):
    return {"type":"mc","q":q,"choices":choices,"correct":correct,"exp":exp}
def sa(q, ans, exp):
    return {"type":"sa","q":q,"ans":str(ans),"exp":exp}
def sw(q, ans, exp):
    return {"type":"sw","q":q,"ans":str(ans),"exp":exp}

# ── Helper: generate template-based questions when hand-writing not done ──────
def math_mc_set(topic, grade):
    """Return 10 MC + 6 SA + 4 SW template questions for a math topic."""
    nums = [random.randint(2,9) for _ in range(8)]
    a,b,c,d,e,f,g,h = nums

    # Ratio question: construct p*k : q*k so GCF > 1 and it always simplifies
    rp, rq, rk = (a % 4)+2, (b % 3)+2, (c % 3)+2
    rbig1, rbig2 = rp*rk, rq*rk
    rgcf = math.gcd(rbig1, rbig2)
    rs1, rs2 = rbig1//rgcf, rbig2//rgcf

    qs = [
        mc(f"Which expression represents '{topic}' correctly?",
           [f"{a}x + {b}", f"{a}x − {b}", f"{b}x + {a}", f"x + {a+b}"], 0,
           f"The standard form for {topic} uses the first expression."),
        mc(f"Evaluate: {a} × {b} + {c}",
           [str(a*b+c), str(a*b-c), str(a*(b+c)), str(a+b+c)], 0,
           f"Multiply first (order of operations): {a}×{b}={a*b}, then +{c} = {a*b+c}."),
        mc(f"Simplify: {a*b}⁄{a}",
           [str(b), str(a), str(a*b), str(a+b)], 0,
           f"Divide top and bottom by {a}: {a*b}÷{a} = {b}."),
        mc(f"Which value of x satisfies {a}x = {a*c}?",
           [str(c), str(a*c), str(a+c), str(c-a)], 0,
           f"Divide both sides by {a}: x = {a*c}÷{a} = {c}."),
        mc(f"What is {b*c} ÷ {b}?",
           [str(c), str(b*c+b), str(b+c), str(b*c-b)], 0,
           f"{b*c} ÷ {b} = {c}."),
        mc(f"Which inequality is equivalent to x + {a} > {a+d}?",
           [f"x > {d}", f"x > {a+d}", f"x < {d}", f"x ≥ {d}"], 0,
           f"Subtract {a} from both sides: x > {a+d}-{a} = {d}."),
        mc(f"What is {a}% of {b*10}?",
           [str(a*b//10) if (a*b)%10==0 else f"{a*b/10:.1f}", str(a*b), str(b*10-a), str(a+b*10)], 0,
           f"{a}% = {a}/100; multiply by {b*10}: {a}×{b*10}/100 = {a*b/10}."),
        mc(f"Simplify the ratio {rbig1}:{rbig2}.",
           [f"{rs1}:{rs2}", f"{rbig1}:{rbig2}", f"{rbig1*2}:{rbig2*2}", f"{rs2}:{rs1}"], 0,
           f"GCF of {rbig1} and {rbig2} is {rgcf}. Divide both: {rbig1}÷{rgcf}={rs1}, {rbig2}÷{rgcf}={rs2}. Simplified: {rs1}:{rs2}."),
        mc(f"Round {a*111 + b*10 + c} to the nearest hundred.",
           [str(round(a*111+b*10+c, -2)), str(a*111+b*10+c+10), str(a*111), str(a*100+c*10)], 0,
           f"Look at the tens digit to round {a*111+b*10+c} to the nearest hundred."),
        mc(f"What is the mean of {a}, {b}, {c}, and {d}?",
           [str(round((a+b+c+d)/4,1)), str(a+b+c+d), str(max(a,b,c,d)), str(min(a,b,c,d))], 0,
           f"Sum = {a+b+c+d}; mean = {a+b+c+d}/4 = {(a+b+c+d)/4}."),
        sa(f"Solve: {a}x + {b} = {a*c+b}", c, f"Subtract {b}: {a}x = {a*c}; divide by {a}: x = {c}."),
        sa(f"What is {b*d} ÷ {d}?", b, f"{b*d} ÷ {d} = {b}."),
        sa(f"Calculate {a*100 + b*10 + c} + {d*100 + e*10 + f}.",
           a*100+b*10+c+d*100+e*10+f, f"Add column by column: {a*100+b*10+c} + {d*100+e*10+f} = {a*100+b*10+c+d*100+e*10+f}."),
        sa(f"What is {a*b} − {b*c}?", a*b-b*c, f"{a*b} − {b*c} = {a*b-b*c}."),
        sa(f"Find the area of a rectangle with length {a+b} and width {c}.", (a+b)*c,
           f"Area = length × width = {a+b} × {c} = {(a+b)*c}."),
        sa(f"What percent of {b*10} is {a*b}?", a*10,
           f"{a*b}/{b*10} × 100 = {a*10}%."),
        sw(f"A car travels at {a*10} mph for {b} hours and then {c*10} mph for {d} hours. Find total distance.",
           a*10*b + c*10*d,
           f"Distance₁ = {a*10}×{b} = {a*10*b}. Distance₂ = {c*10}×{d} = {c*10*d}. Total = {a*10*b+c*10*d} miles."),
        sw(f"Solve step-by-step: {a}x − {b} = {a*e - b}", e,
           f"Add {b} to both sides: {a}x = {a*e}. Divide by {a}: x = {e}."),
        sw(f"A store sells {a} items at ${b} each and {c} items at ${d} each. What is the total revenue?",
           a*b + c*d,
           f"Revenue = {a}×${b} + {c}×${d} = ${a*b} + ${c*d} = ${a*b+c*d}."),
        sw(f"Find the perimeter and area of a rectangle: length = {a+c}, width = {b}.",
           f"P={2*(a+c+b)}, A={(a+c)*b}",
           f"P = 2({a+c}+{b}) = {2*(a+c+b)}. A = {a+c}×{b} = {(a+c)*b}."),
    ]
    return qs

def sci_mc_set(unit_title, topics, grade):
    t0,t1,t2 = (topics+topics)[:3]
    return [
        mc(f"What best describes '{t0}'?",
           [f"The study and process of {t0}",f"A type of organism",f"A physical location",f"A measurement tool"],0,
           f"{t0} refers to its scientific definition in this unit."),
        mc(f"Which is an example of {t1}?",
           [f"A real-world instance of {t1}",f"An unrelated concept",f"The opposite of {t1}",f"A tool used only in labs"],0,
           f"The first option best represents a concrete example of {t1}."),
        mc(f"What happens during {t2}?",
           [f"The main process of {t2} occurs",f"Nothing changes",f"The reverse happens",f"It only applies underground"],0,
           f"During {t2}, the primary mechanism or change described in the unit takes place."),
        mc(f"Which statement about {t0} is TRUE?",
           [f"{t0} is a key concept in this unit",f"{t0} only applies to plants",f"{t0} was discovered last year",f"{t0} has no real-world use"],0,
           f"{t0} is a foundational concept with broad scientific relevance."),
        mc(f"Scientists study {t1} because:",
           [f"It explains important natural phenomena",f"It is easy to ignore",f"It has no effect on living things",f"It was recently disproved"],0,
           f"Understanding {t1} helps explain key processes in the natural world."),
        mc(f"How does {t0} relate to {t1}?",
           [f"They are connected concepts in {unit_title}",f"They are unrelated",f"One cancels out the other",f"Only one is real"],0,
           f"Both are interconnected concepts within the study of {unit_title}."),
        mc(f"Which tool would best help you observe {t2}?",
           ["The appropriate scientific instrument","A ruler only","A calculator","A thermometer only"],0,
           f"The right instrument depends on the scale and nature of {t2}."),
        mc(f"The unit '{unit_title}' is part of which branch of science?",
           [f"The branch that includes {unit_title}","Mathematics","History","Literature"],0,
           f"{unit_title} is studied within its relevant scientific field."),
        mc(f"What would happen if {t0} stopped occurring?",
           [f"Major consequences for related systems",f"Nothing would change",f"The universe would expand",f"Only art would be affected"],0,
           f"Without {t0}, connected biological or physical systems would be significantly disrupted."),
        mc(f"Which correctly sequences the steps involved in {t1}?",
           [f"Input → Process → Output",f"Output → Input → Process",f"Random order",f"Process only"],0,
           f"Scientific processes follow a logical sequence: inputs lead to a process that produces outputs."),
        sa(f"Name the main topic studied in the unit '{unit_title}'.",
           t0, f"The first key topic in {unit_title} is {t0}."),
        sa(f"In one word or phrase, describe what {t1} produces or results in.",
           "See unit notes", f"Refer to your notes on {t1} for the specific outcome."),
        sa(f"How many key topics are in this unit?", str(len(topics)),
           f"This unit covers {len(topics)} main topics."),
        sa(f"True or False: {t0} is relevant to everyday life.", "true",
           f"True — {t0} has real-world applications in daily life."),
        sa(f"What unit does {t2} belong to?", unit_title,
           f"{t2} is a topic within '{unit_title}'."),
        sa(f"List one real-world example related to {t0}.",
           "Various valid examples", f"Any concrete, relevant example demonstrates understanding of {t0}."),
        sw(f"Explain the relationship between {t0} and {t1} in 2–3 sentences.",
           f"See explanation", f"{t0} and {t1} are related concepts in {unit_title} — describe how one leads to or affects the other."),
        sw(f"Describe the process of {t2} step by step.",
           "Step-by-step explanation", f"List each step of {t2} in logical scientific order."),
        sw(f"Design a simple experiment to test something related to {t0}. Include hypothesis, materials, and procedure.",
           "See experiment design", f"Hypothesis: state a testable prediction about {t0}. Materials: list what you need. Procedure: give steps."),
        sw(f"Compare and contrast {t0} and {t1}. Give at least two similarities and two differences.",
           "Comparison paragraph", f"Use a graphic organizer or Venn diagram approach to compare {t0} and {t1}."),
    ]

def ela_mc_set(unit_title, topics, grade):
    t0,t1,t2 = (topics+topics)[:3]
    return [
        mc(f"What is the definition of '{t0}'?",
           [f"The literary/writing concept of {t0}",f"A type of punctuation",f"A historical event",f"A math operation"],0,
           f"{t0} is a core literary or writing term in this unit."),
        mc(f"Which sentence best demonstrates '{t1}'?",
           [f"A sentence using {t1} correctly",f"A sentence with no literary devices",f"A list of words",f"A math equation"],0,
           f"The first option correctly uses {t1} in context."),
        mc(f"An author uses {t2} to:",
           [f"Create a specific effect on the reader",f"Make the story shorter",f"Remove adjectives",f"Confuse the audience"],0,
           f"Authors use {t2} deliberately to affect how readers interpret or feel about the text."),
        mc(f"Which is NOT an example of {t0}?",
           [f"Something that doesn't fit {t0}",f"A classic example of {t0}",f"A simple instance of {t0}",f"A complex use of {t0}"],0,
           f"The first option falls outside the definition of {t0}."),
        mc(f"In the sentence 'The moon was a silver coin,' the author is using:",
           ["Metaphor","Simile","Onomatopoeia","Personification"],0,
           "The moon is described as being a coin without using 'like' or 'as' — that's a metaphor."),
        mc(f"What is the purpose of {t1} in writing?",
           [f"To enhance the reader's understanding or experience",f"To confuse the reader",f"To shorten the text",f"To add math problems"],0,
           f"{t1} serves to deepen meaning and engage readers."),
        mc(f"A text organized in chronological order uses which structure?",
           ["Sequence/time order","Cause and effect","Compare and contrast","Problem and solution"],0,
           "Chronological = time order = sequence structure."),
        mc(f"Which best describes {t2} in informational writing?",
           [f"A technique for organizing or supporting ideas",f"A type of fictional character",f"A grammar rule",f"A punctuation mark"],0,
           f"{t2} is a key strategy in effective writing."),
        mc(f"The theme of a story is best described as:",
           ["The central message about life","The main character's name","The setting of the story","The conflict only"],0,
           "Theme = the deeper message or universal idea the story conveys."),
        mc(f"Which is an example of first-person point of view?",
           ["'I felt a chill run down my spine.'","'She stared at the ceiling.'","'The dog barked loudly.'","'Everyone stood still.'"],0,
           "First person uses 'I/me/my' — the narrator IS in the story."),
        sa(f"Name the literary term that means comparing two things using 'like' or 'as'.",
           "simile", "A simile compares using 'like' or 'as.'"),
        sa(f"What is the opposite of a protagonist?", "antagonist",
           "The antagonist opposes the protagonist."),
        sa(f"In one word: what is the struggle in a story called?", "conflict",
           "Conflict is the central struggle driving the plot."),
        sa(f"What part of speech does an adverb modify?", "verb",
           "Adverbs modify verbs, adjectives, or other adverbs."),
        sa(f"True or False: A summary should include your personal opinion.", "false",
           "A summary restates the author's ideas — not your opinion."),
        sa(f"What is the term for the main idea of a paragraph?", "topic sentence",
           "The topic sentence states the main idea at the start of a paragraph."),
        sw(f"Write a paragraph that demonstrates {t0}. Include at least two examples.",
           "See original paragraph", f"Write original sentences using {t0} with clear examples."),
        sw(f"Analyze: how does {t1} affect the meaning of a text? Use a specific example.",
           "See analysis", f"Explain what {t1} is, show it in context, and describe its effect on the reader."),
        sw(f"Revise this weak sentence using {t2}: 'It was a nice day and things were good.'",
           "Revised sentence", f"Use {t2} to add specific detail, imagery, or stronger word choice."),
        sw(f"Write a {unit_title.lower()} piece of at least 5 sentences on a topic of your choice.",
           "See writing sample", f"Apply the conventions and techniques of {unit_title} to your writing."),
    ]

def hist_mc_set(unit_title, topics, grade):
    t0,t1,t2 = (topics+topics)[:3]
    return [
        mc(f"What is {t0}?",
           [f"A key event or concept in {unit_title}",f"A type of geography",f"A modern invention",f"An unrelated topic"],0,
           f"{t0} is a foundational concept in the study of {unit_title}."),
        mc(f"When did events related to {unit_title} primarily occur?",
           [f"The historically accurate time period",f"Yesterday",f"The distant future",f"Before Earth existed"],0,
           f"{unit_title} occurred during its historically significant period."),
        mc(f"What was a major CAUSE of events in {unit_title}?",
           [f"A documented historical cause",f"A random accident",f"No cause — it just happened",f"Technology"],0,
           f"Multiple factors caused the events in {unit_title}."),
        mc(f"What was a major EFFECT of {t0}?",
           [f"A lasting historical consequence",f"Nothing changed",f"Only local effects",f"It reversed immediately"],0,
           f"{t0} had significant and lasting effects on societies and governments."),
        mc(f"Which best describes {t1}?",
           [f"An accurate description of {t1}",f"A fictional story",f"A modern technology",f"A sports term"],0,
           f"{t1} is accurately described by the first option."),
        mc(f"Who were the most important people involved in {unit_title}?",
           [f"Key historical figures of the era",f"Only military generals",f"No one important",f"Fictional characters"],0,
           f"Multiple historical figures shaped the events of {unit_title}."),
        mc(f"How did geography influence {unit_title}?",
           [f"Location and terrain shaped events and decisions",f"Geography had no effect",f"Only the weather mattered",f"Geography didn't exist then"],0,
           "Geography — rivers, mountains, coastlines — always shapes historical events."),
        mc(f"Which primary source would best help you study {unit_title}?",
           [f"A document, letter, or artifact from that era",f"A modern textbook",f"A social media post",f"A math textbook"],0,
           "Primary sources from the era provide direct evidence."),
        mc(f"What is the significance of {t2}?",
           [f"It changed political, social, or economic conditions",f"It had no impact",f"It only affected one person",f"It was quickly forgotten"],0,
           f"{t2} had lasting significance in the historical record."),
        mc(f"How does {unit_title} connect to events that came AFTER it?",
           [f"It laid the groundwork for later developments",f"It had no connection",f"It reversed all prior history",f"Only future technology mattered"],0,
           "Historical events form a chain — each shapes what follows."),
        sa(f"In what century did the main events of {unit_title} occur?",
           "See notes", f"Refer to your class notes for the specific century."),
        sa(f"Name one key person associated with {t0}.",
           "See notes", f"Key historical figures in {t0} are covered in your notes."),
        sa(f"True or False: Primary sources are written after the events they describe.", "false",
           "False — primary sources are created during or immediately after the event."),
        sa(f"What does 'cause and effect' mean in history?",
           "events lead to consequences", "An event (cause) produces a result (effect) — central to historical thinking."),
        sa(f"Name one country or civilization central to {unit_title}.",
           "See notes", f"Refer to your notes for the key nation or civilization in {unit_title}."),
        sa(f"What does 'chronological order' mean?", "time order",
           "Chronological = arranged from earliest to latest."),
        sw(f"Explain the causes and effects of {t0} in 3–4 sentences.",
           "Cause-effect paragraph", f"State at least two causes and two effects of {t0} with evidence."),
        sw(f"Compare {t1} and {t2}. What are two similarities and two differences?",
           "Comparison", f"Use a Venn diagram or paragraph to compare {t1} and {t2}."),
        sw(f"Imagine you lived during {unit_title}. Write a journal entry describing your daily life.",
           "Creative journal entry", f"Use historical details about {unit_title} to make your entry accurate."),
        sw(f"Was {unit_title} more positive or negative for people of the time? Support with evidence.",
           "Historical argument", f"Make a claim and support it with at least two historical facts."),
    ]

def cs_mc_set(unit_title, topics, grade):
    t0,t1,t2 = (topics+topics)[:3]
    return [
        mc(f"What does '{t0}' mean in computer science?",
           [f"The CS definition of {t0}",f"A type of food",f"A weather pattern",f"A musical note"],0,
           f"{t0} is a fundamental CS concept."),
        mc(f"Which correctly describes {t1}?",
           [f"An accurate CS description of {t1}",f"A hardware component",f"A programming language only",f"An internet protocol"],0,
           f"{t1} is accurately defined by the first option."),
        mc(f"In what order do computers execute instructions?",
           ["Sequentially (one at a time, top to bottom)","Randomly","In alphabetical order","Backwards"],0,
           "Computers execute instructions sequentially unless told otherwise."),
        mc(f"What is a variable in programming?",
           ["A named storage location for data","A type of computer","A file on your desktop","An internet address"],0,
           "A variable stores a value that can change — like a labeled box."),
        mc(f"Which is an example of {t2}?",
           [f"A concrete CS use case of {t2}",f"An unrelated concept",f"Only hardware",f"Only software"],0,
           f"{t2} appears in many real-world computing applications."),
        mc(f"A 'bug' in programming is:",
           ["An error in code that causes incorrect behavior","A small insect","A feature","A type of computer chip"],0,
           "Bugs are errors — debugging is the process of fixing them."),
        mc(f"What does an if-statement do?",
           ["Executes code only if a condition is true","Runs code randomly","Repeats code forever","Defines a variable"],0,
           "An if-statement is a conditional — it checks a condition and runs code only if true."),
        mc(f"What is the internet?",
           ["A global network of connected computers","A single large computer","A type of software","A wireless signal"],0,
           "The internet is a worldwide network connecting billions of devices."),
        mc(f"What does 'loop' mean in programming?",
           ["Repeating a block of code","A circular shape","A data type","A keyboard shortcut"],0,
           "A loop repeats instructions — 'for' and 'while' are common loops."),
        mc(f"Why is {t0} important in computing?",
           [f"It solves real problems efficiently",f"It's only for fun",f"It has no practical use",f"Only experts care about it"],0,
           f"{t0} is important because it directly addresses computing challenges."),
        sa(f"What is the output of: print(3 + 4 * 2) in Python?", "11",
           "Order of operations: 4*2=8 first, then 3+8=11."),
        sa(f"Name the three main control structures in programming.", "sequence selection iteration",
           "Sequence (order), selection (if), iteration (loops)."),
        sa(f"What does HTML stand for?", "hypertext markup language",
           "HTML = HyperText Markup Language — used to structure web pages."),
        sa(f"True or False: A computer can understand natural language like English directly.", "false",
           "False — computers use machine code; programs translate human languages."),
        sa(f"What does 'input' mean in a computer program?", "data given to the program",
           "Input is data the program receives from the user or another source."),
        sa(f"What keyword starts an if-statement in most languages?", "if",
           "The keyword 'if' starts a conditional statement."),
        sw(f"Write pseudocode for a program that finds the largest of three numbers A, B, and C.",
           "if A>B and A>C: largest=A elif B>C: largest=B else: largest=C",
           "Compare A to B and C, then B to C — the largest wins."),
        sw(f"Explain how {t0} works step-by-step in plain English.",
           "Step-by-step explanation", f"Describe the process of {t0} clearly enough for a non-programmer to understand."),
        sw(f"Trace this code and show the output step by step:\nfor i in range(1, 4):\n    print(i * 2)",
           "2\n4\n6",
           "i=1: 1×2=2. i=2: 2×2=4. i=3: 3×2=6."),
        sw(f"Design a program that uses {t1}. Describe its purpose, inputs, and outputs.",
           "Program design", f"State what the program does, what data it needs (inputs), and what it produces (outputs)."),
    ]

def health_mc_set(unit_title, topics, grade):
    t0,t1,t2 = (topics+topics)[:3]
    return [
        mc(f"What does {t0} mean for personal health?",
           [f"A health behavior or concept related to {t0}",f"A type of sport",f"A math formula",f"A historical term"],0,
           f"{t0} is a key health concept in this unit."),
        mc(f"How many hours of sleep do teenagers typically need per night?",
           ["8–10 hours","4–5 hours","12+ hours","2–3 hours"],0,
           "Teens need 8–10 hours for proper rest and development."),
        mc(f"Which is a healthy response to stress?",
           ["Exercise and talking to someone","Skipping meals","Sleeping 15 hours","Ignoring it completely"],0,
           "Healthy coping includes physical activity and social support."),
        mc(f"What does {t1} involve?",
           [f"Key health behaviors related to {t1}",f"Nothing important",f"Only medical doctors",f"Only dieting"],0,
           f"{t1} involves specific health practices and behaviors."),
        mc(f"Why is nutrition important?",
           ["It provides energy and nutrients for body functions","It's only for athletes","It only affects weight","It's optional"],0,
           "Proper nutrition fuels every body system and supports growth."),
        mc(f"What is a BMI used for?",
           ["Estimating body fat relative to height and weight","Measuring athletic speed","Calculating grades","Tracking emotions"],0,
           "BMI = Body Mass Index — a screening tool using height and weight."),
        mc(f"Which is NOT a component of physical fitness?",
           ["Memorization speed","Cardiovascular endurance","Muscular strength","Flexibility"],0,
           "The five fitness components are cardiovascular endurance, muscular strength/endurance, flexibility, and body composition."),
        mc(f"What does {t2} help with?",
           [f"Improving health outcomes related to {t2}",f"Nothing",f"Only professional athletes",f"Only older adults"],0,
           f"{t2} contributes to overall well-being."),
        mc(f"What is mental health?",
           ["Emotional, psychological, and social well-being","Only a medical diagnosis","Physical fitness","Nutrition"],0,
           "Mental health encompasses emotional, psychological, and social well-being."),
        mc(f"Which is an example of a healthy boundary?",
           ["Saying 'no' when you're uncomfortable","Always doing what others want","Ignoring your feelings","Keeping secrets"],0,
           "Healthy boundaries protect your well-being and are communicated clearly."),
        sa(f"Name two healthy coping strategies for stress.", "exercise talk to someone",
           "Exercise, journaling, deep breathing, and talking to someone are all effective."),
        sa(f"What does 'hydration' mean?", "drinking enough water",
           "Hydration = maintaining adequate fluid levels in the body."),
        sa(f"True or False: Mental health and physical health are completely separate.", "false",
           "False — they are deeply connected; physical health affects mental health and vice versa."),
        sa(f"Name one food high in protein.", "chicken",
           "Protein sources: chicken, fish, eggs, beans, tofu, dairy."),
        sa(f"What does 'consent' mean in relationships?", "freely given agreement",
           "Consent = a freely given, reversible, informed, enthusiastic, specific agreement."),
        sa(f"How many minutes of physical activity should teens get daily?", "60",
           "The CDC recommends 60 minutes of moderate-to-vigorous activity per day for teens."),
        sw(f"Create a one-week healthy meal plan. Include breakfast, lunch, and dinner for three days.",
           "Meal plan", "Include all food groups — grains, protein, dairy, fruits, vegetables — in balanced portions."),
        sw(f"Describe a stressful situation and three healthy ways to respond to it.",
           "Stress response plan", "State the scenario, then list three specific, actionable coping strategies."),
        sw(f"Explain the connection between {t0} and overall wellness. Give two examples.",
           "Wellness connection", f"Describe how {t0} affects physical, mental, or social health with two specific examples."),
        sw(f"Design a 30-day personal wellness challenge. Include goals for nutrition, exercise, and mental health.",
           "Wellness challenge", "Set SMART goals for each area: what specifically will you do, how often, and how will you measure success?"),
    ]

# ── Full curriculum structure ─────────────────────────────────────────────────
CURRICULUM = {
  6: {
    "math": [
      {"unit":"Ratios & Proportional Relationships","topics":["Understanding ratios","Unit rates","Ratio tables","Proportional relationships","Percent problems"]},
      {"unit":"The Number System","topics":["Division of fractions","Multi-digit arithmetic","Rational numbers on a number line","Absolute value","Ordering integers"]},
      {"unit":"Expressions & Equations","topics":["Writing and evaluating expressions","Properties of operations","Solving one-step equations","Inequalities"]},
      {"unit":"Geometry","topics":["Area of polygons","Surface area","Volume of rectangular prisms","Coordinate plane"]},
      {"unit":"Statistics & Probability","topics":["Statistical questions","Dot plots & histograms","Box plots","Mean, median, mode, range","Data distributions"]},
    ],
    "science": [
      {"unit":"Matter & Its Interactions","topics":["Atoms and molecules","States of matter","Physical vs. chemical changes","Conservation of mass","Properties of materials"]},
      {"unit":"Earth & Space Systems","topics":["Weathering and erosion","Rock cycle","Plate tectonics introduction","Earth's layers","Geologic time"]},
      {"unit":"Ecosystems","topics":["Food webs and food chains","Energy flow","Biodiversity","Ecosystem services","Human impact on ecosystems"]},
      {"unit":"Life Science","topics":["Cell structure and function","Photosynthesis basics","Reproduction","Heredity overview","Classification of organisms"]},
    ],
    "ela": [
      {"unit":"Reading Literature","topics":["Story elements: plot, setting, character","Theme and central message","Point of view","Comparing texts","Figurative language"]},
      {"unit":"Reading Informational Text","topics":["Main idea and supporting details","Author's purpose","Text structure","Evidence and reasoning","Summarization"]},
      {"unit":"Writing","topics":["Narrative writing","Informational/explanatory writing","Argument writing","Research process","Revision and editing"]},
      {"unit":"Language Conventions","topics":["Parts of speech review","Sentence structure","Punctuation","Vocabulary development","Context clues"]},
      {"unit":"Speaking & Listening","topics":["Collaborative discussion","Presentations","Evaluating speaker's arguments","Multimedia integration"]},
    ],
    "history": [
      {"unit":"Early Civilizations","topics":["Mesopotamia","Ancient Egypt","Ancient India and China","Ancient Greece","Ancient Rome"]},
      {"unit":"World Geography","topics":["Reading maps and globes","Physical geography","Human geography","Regions of the world","Geographic tools"]},
      {"unit":"Government & Civics Intro","topics":["Types of government","Laws and rules","Rights and responsibilities","Democratic principles","Local government"]},
    ],
    "cs": [
      {"unit":"Digital Literacy","topics":["Internet safety","Evaluating online sources","Digital citizenship","Privacy and security","Screen time awareness"]},
      {"unit":"Introduction to Coding","topics":["Algorithms and flowcharts","Sequence, selection, iteration","Block-based coding (Scratch)","Debugging","Creating simple projects"]},
    ],
    "health": [
      {"unit":"Personal Health","topics":["Hygiene and self-care","Sleep and nutrition","Growth and development","Puberty education","Stress management"]},
      {"unit":"Physical Fitness","topics":["Components of fitness","Aerobic exercise","Strength and flexibility","Team sports rules","Setting fitness goals"]},
    ],
  },
  7: {
    "math": [
      {"unit":"Ratios & Proportional Relationships","topics":["Proportional vs. non-proportional","Solving proportions","Percent increase and decrease","Simple interest","Scale drawings"]},
      {"unit":"The Number System","topics":["Adding and subtracting rational numbers","Multiplying and dividing rational numbers","Rational number word problems","Converting fractions/decimals/percents"]},
      {"unit":"Expressions & Equations","topics":["Linear expressions","Solving multi-step equations","Inequalities on a number line","Rewriting expressions"]},
      {"unit":"Geometry","topics":["Angle relationships","Area and circumference of circles","Area of composite figures","Surface area and volume of 3D figures","Scale problems"]},
      {"unit":"Statistics & Probability","topics":["Random sampling","Comparing populations","Probability of simple events","Probability of compound events","Simulations"]},
    ],
    "science": [
      {"unit":"Structure & Properties of Matter","topics":["Periodic table","Chemical vs. physical properties","Density","Mixtures and solutions","Atomic structure intro"]},
      {"unit":"Chemical Reactions","topics":["Signs of a chemical reaction","Conservation of mass","Endothermic vs. exothermic","Everyday chemical reactions"]},
      {"unit":"Life Science: Body Systems","topics":["Digestive system","Circulatory system","Respiratory system","Nervous system","Muscular and skeletal systems"]},
      {"unit":"Earth Science","topics":["Atmosphere layers","Weather patterns","Climate vs. weather","Natural disasters","Human impact on atmosphere"]},
    ],
    "ela": [
      {"unit":"Reading Literature","topics":["Complex character analysis","Theme development","Narrative techniques","Poetry analysis","Comparing genres"]},
      {"unit":"Reading Informational Text","topics":["Central idea development","Analyzing arguments","Text structure analysis","Primary vs. secondary sources","Evaluating evidence"]},
      {"unit":"Writing","topics":["Argumentative writing","Research-based writing","Narrative techniques","Citation and plagiarism","Peer review process"]},
      {"unit":"Language & Grammar","topics":["Phrases and clauses","Misplaced/dangling modifiers","Active vs. passive voice","Word choice and tone","Formal vs. informal register"]},
    ],
    "history": [
      {"unit":"Medieval World","topics":["Fall of Rome","Byzantine Empire","Islamic civilization","Medieval Europe","Feudal system"]},
      {"unit":"Renaissance & Reformation","topics":["Italian Renaissance","Scientific Revolution","Protestant Reformation","Age of Exploration","Columbian Exchange"]},
      {"unit":"Early Americas","topics":["Pre-Columbian civilizations","European colonization","Native American cultures","Colonial life","African slave trade"]},
    ],
    "cs": [
      {"unit":"Programming Fundamentals","topics":["Variables and data types","Conditionals","Loops","Functions and procedures","Input/output"]},
      {"unit":"Problem Solving","topics":["Computational thinking","Decomposition","Pattern recognition","Algorithm design","Pseudocode"]},
    ],
    "health": [
      {"unit":"Mental & Emotional Health","topics":["Emotional intelligence","Coping with stress","Building resilience","Recognizing depression/anxiety","Getting help"]},
      {"unit":"Nutrition & Wellness","topics":["Macronutrients","Reading nutrition labels","Healthy vs. unhealthy habits","Eating disorders awareness","Hydration"]},
    ],
  },
  8: {
    "math": [
      {"unit":"The Number System","topics":["Irrational numbers","Square and cube roots","Approximating irrational numbers","Scientific notation operations"]},
      {"unit":"Expressions & Equations","topics":["Integer exponents","Linear equations with one solution","Systems of linear equations","Solving systems by substitution and elimination"]},
      {"unit":"Functions","topics":["Defining functions","Linear vs. nonlinear functions","Slope and rate of change","Representing functions (tables, graphs, equations)","Comparing functions"]},
      {"unit":"Geometry","topics":["Transformations (translations, rotations, reflections)","Congruence and similarity","Pythagorean theorem","Pythagorean theorem applications","Volume of cylinders, cones, spheres"]},
      {"unit":"Statistics & Probability","topics":["Scatter plots","Line of best fit","Linear associations","Two-way frequency tables"]},
    ],
    "science": [
      {"unit":"Force & Motion","topics":["Newton's laws of motion","Gravity and friction","Speed, velocity, acceleration","Free body diagrams","Momentum"]},
      {"unit":"Energy","topics":["Kinetic and potential energy","Conservation of energy","Forms of energy","Energy transfer and transformation","Renewable vs. nonrenewable energy"]},
      {"unit":"Waves & Electromagnetic Spectrum","topics":["Wave properties","Sound waves","Light waves","Electromagnetic spectrum","Communication technology"]},
      {"unit":"Earth History & Space","topics":["Evidence for plate tectonics","Fossil record","Natural selection intro","Solar system","Stars and galaxies"]},
    ],
    "ela": [
      {"unit":"Reading Literature","topics":["Analyzing dialogue and incidents","Universal themes","Allusion","Modern vs. classic texts","Drama and screenplay reading"]},
      {"unit":"Reading Informational Text","topics":["Delineating and evaluating arguments","Conflicting information","Integrating multiple sources","Media literacy"]},
      {"unit":"Writing","topics":["Argumentative essay structure","Counterarguments and rebuttals","Research paper writing","MLA/APA citation intro","Narrative craft"]},
      {"unit":"Language","topics":["Verbals: gerunds, participles, infinitives","Comma use","Semicolons and colons","Nuances in word meanings","Etymology"]},
    ],
    "history": [
      {"unit":"American Revolution & Founding","topics":["Causes of the Revolution","Declaration of Independence","Revolutionary War","Articles of Confederation","Constitutional Convention"]},
      {"unit":"The Constitution & New Nation","topics":["Structure of the Constitution","Bill of Rights","Federalism","Early political parties","Washington and Adams presidencies"]},
      {"unit":"Expansion & Reform","topics":["Manifest Destiny","Westward expansion","Reform movements","Industrial Revolution in America","Immigration patterns"]},
      {"unit":"Civil War & Reconstruction","topics":["Causes of the Civil War","Major battles and turning points","Emancipation Proclamation","Reconstruction plans","Impact of Reconstruction"]},
    ],
    "cs": [
      {"unit":"Data & Analysis","topics":["Data types and structures","Collecting and cleaning data","Spreadsheet skills","Data visualization","Drawing conclusions from data"]},
      {"unit":"Web Design Basics","topics":["HTML structure","CSS styling","Accessibility principles","Publishing a webpage","Internet architecture"]},
    ],
    "health": [
      {"unit":"Substance Use & Abuse","topics":["Alcohol and tobacco effects","Drug classifications","Addiction science","Refusal skills","Community resources"]},
      {"unit":"Relationships & Communication","topics":["Healthy vs. unhealthy relationships","Conflict resolution","Digital communication etiquette","Bullying and bystander effect","Consent basics"]},
    ],
  },
  9: {
    "math": [
      {"unit":"Algebra I: Foundations","topics":["Number properties review","Order of operations","Writing expressions and equations","Evaluating algebraic expressions","Translating word problems"]},
      {"unit":"Linear Relationships","topics":["Slope-intercept form","Standard form","Point-slope form","Parallel and perpendicular lines","Graphing linear equations"]},
      {"unit":"Systems of Equations","topics":["Graphing systems","Substitution method","Elimination method","Systems of inequalities","Real-world applications"]},
      {"unit":"Polynomials","topics":["Adding and subtracting polynomials","Multiplying polynomials","Factoring GCF","Factoring trinomials","Special products"]},
      {"unit":"Quadratic Functions","topics":["Graphing parabolas","Vertex form","Standard form","Factoring to solve quadratics","Quadratic formula"]},
      {"unit":"Exponential & Radical Functions","topics":["Exponential growth and decay","Radical expressions","Simplifying radicals","Solving radical equations"]},
    ],
    "science": [
      {"unit":"Biology: Cell Biology","topics":["Cell theory","Prokaryotic vs. eukaryotic cells","Cell organelles","Cell membrane and transport","Cell cycle and mitosis"]},
      {"unit":"Genetics","topics":["DNA structure and function","Protein synthesis","Mendelian genetics","Punnett squares","Mutations and genetic disorders"]},
      {"unit":"Evolution","topics":["Evidence for evolution","Natural selection","Adaptation","Speciation","Human evolution overview"]},
      {"unit":"Ecology","topics":["Population dynamics","Community interactions","Biomes","Nutrient cycles","Climate change and biodiversity"]},
    ],
    "ela": [
      {"unit":"Reading Literature","topics":["Literary analysis essays","Complex character development","Symbolism and allegory","Satire and irony","World literature introduction"]},
      {"unit":"Research & Informational Writing","topics":["Evaluating source credibility","Synthesizing multiple sources","Research paper structure","In-text citations","Works cited page"]},
      {"unit":"Argumentative Writing","topics":["Claim and evidence","Logical fallacies","Rhetorical devices","Audience and purpose","Formal essay conventions"]},
      {"unit":"Vocabulary & Language","topics":["Academic vocabulary","Greek and Latin roots","Connotation vs. denotation","Figurative language mastery","Writing style development"]},
    ],
    "history": [
      {"unit":"World History: Modern Era","topics":["Age of Revolutions (French, Haitian)","Nationalism and imperialism","Industrial Revolution globally","World War I causes and effects","Treaty of Versailles"]},
      {"unit":"Global Economics Intro","topics":["Supply and demand","Market structures","Economic systems","Trade and globalization","Personal finance basics"]},
      {"unit":"Government & Civics","topics":["Federalism and separation of powers","Branches of US government","Electoral system","Civil liberties and civil rights","Comparative government systems"]},
    ],
    "cs": [
      {"unit":"Python Programming","topics":["Variables and data types","Control flow","Functions","Lists and dictionaries","File I/O basics"]},
      {"unit":"Cybersecurity Awareness","topics":["Types of cyber threats","Password security","Encryption basics","Social engineering","Privacy laws and ethics"]},
    ],
    "health": [
      {"unit":"Human Development & Sexuality","topics":["Reproductive anatomy","STI prevention","Contraception methods","Consent and healthy relationships","Teen pregnancy statistics"]},
      {"unit":"First Aid & Safety","topics":["CPR basics","AED use","Treating wounds","Emergency response","Sports injury prevention"]},
    ],
  },
  10: {
    "math": [
      {"unit":"Geometry: Foundations","topics":["Points, lines, planes","Angle pairs","Parallel lines and transversals","Triangle congruence (SSS, SAS, ASA)","Proofs introduction"]},
      {"unit":"Triangles & Trigonometry","topics":["Pythagorean theorem applications","Special right triangles","Trigonometric ratios (sin, cos, tan)","Solving right triangles","Angles of elevation and depression"]},
      {"unit":"Circles","topics":["Circle theorems","Arc length and sector area","Equations of circles","Chords, tangents, secants","Inscribed angles"]},
      {"unit":"Area, Surface Area & Volume","topics":["Area of polygons and composite figures","Surface area of 3D figures","Volume of prisms, cylinders, pyramids, cones","Cavalieri's principle"]},
      {"unit":"Probability & Statistics","topics":["Conditional probability","Permutations and combinations","Normal distributions","z-scores","Data analysis and interpretation"]},
    ],
    "science": [
      {"unit":"Chemistry: Atomic Structure","topics":["Bohr model","Electron configuration","Periodic trends","Ionic vs. covalent bonding","Lewis dot structures"]},
      {"unit":"Chemical Reactions","topics":["Balancing equations","Types of reactions","Stoichiometry","Limiting reagents","Reaction rates and equilibrium intro"]},
      {"unit":"Solutions & Thermochemistry","topics":["Molarity and concentration","Acids and bases (pH)","Solubility rules","Enthalpy and calorimetry","Hess's Law intro"]},
      {"unit":"Nuclear Chemistry","topics":["Radioactive decay","Half-life","Fission vs. fusion","Applications of nuclear chemistry","Radiation safety"]},
    ],
    "ela": [
      {"unit":"American Literature","topics":["Puritan literature","Romantic era","Transcendentalism (Thoreau, Emerson)","Realism and Naturalism","Harlem Renaissance"]},
      {"unit":"Literary Analysis","topics":["Critical lenses (feminist, historical, etc.)","Comparing authorial choices","Analyzing complex texts","Writing analytical essays","Oral presentation of analysis"]},
      {"unit":"Composition","topics":["Advanced argument structure","Synthesis essays","Technical and professional writing","Timed writing strategies","Grammar and mechanics mastery"]},
    ],
    "history": [
      {"unit":"World War II & Holocaust","topics":["Rise of fascism","Major theaters of war","Holocaust history and causes","Home front","Post-war world order"]},
      {"unit":"Cold War Era","topics":["Origins of the Cold War","Korean War","McCarthyism","Space Race","Vietnam War"]},
      {"unit":"Modern US History","topics":["Civil Rights Movement","Women's liberation movement","1970s-1990s America","End of Cold War","September 11 and aftermath"]},
    ],
    "cs": [
      {"unit":"Object-Oriented Programming","topics":["Classes and objects","Inheritance","Encapsulation","Polymorphism","Building small applications"]},
      {"unit":"Databases","topics":["Relational databases","SQL basics","Data modeling","CRUD operations","Database design principles"]},
    ],
    "health": [
      {"unit":"Mental Health & Wellness","topics":["Mental health disorders overview","Therapy approaches","Reducing stigma","Mindfulness practices","When and how to seek help"]},
      {"unit":"Community Health","topics":["Public health systems","Epidemiology basics","Healthcare access","Advocacy and policy","Global health challenges"]},
    ],
  },
  11: {
    "math": [
      {"unit":"Algebra II: Functions","topics":["Function notation and operations","Inverse functions","Graphing transformations","Piecewise functions","Absolute value functions"]},
      {"unit":"Polynomial & Rational Functions","topics":["Polynomial long division","Fundamental theorem of algebra","Rational functions and asymptotes","Partial fractions","Solving rational equations"]},
      {"unit":"Exponential & Logarithmic Functions","topics":["Laws of logarithms","Natural log and e","Exponential growth/decay models","Solving logarithmic equations","Applications: compound interest"]},
      {"unit":"Sequences & Series","topics":["Arithmetic sequences","Geometric sequences","Infinite geometric series","Sigma notation","Binomial theorem"]},
      {"unit":"Trigonometry","topics":["Unit circle","Radian measure","Graphing sin, cos, tan","Trigonometric identities","Law of sines and cosines"]},
      {"unit":"Statistics (Pre-AP)","topics":["Experimental design","Sampling methods","Regression analysis","Chi-squared tests intro","Interpreting statistical claims"]},
    ],
    "science": [
      {"unit":"Physics: Motion & Forces","topics":["Kinematics equations","Projectile motion","Newton's Laws in depth","Friction and normal force","Circular motion"]},
      {"unit":"Work, Energy & Momentum","topics":["Work-energy theorem","Conservation of mechanical energy","Impulse-momentum theorem","Elastic and inelastic collisions","Power"]},
      {"unit":"Electricity & Magnetism","topics":["Electric charge and fields","Circuits (series and parallel)","Ohm's Law","Magnetism","Electromagnetic induction"]},
      {"unit":"Waves, Light & Optics","topics":["Wave superposition","Doppler effect","Reflection and refraction","Lenses and mirrors","Quantum basics"]},
    ],
    "ela": [
      {"unit":"British Literature","topics":["Anglo-Saxon period (Beowulf)","Chaucer and Middle Ages","Shakespeare","Romantic poets","Victorian and modern literature"]},
      {"unit":"Research & Rhetoric","topics":["Rhetorical analysis essays","Evaluating and synthesizing sources","Annotated bibliography","AP-style essays","Timed analytical writing"]},
      {"unit":"Language & Style","topics":["Diction and syntax analysis","Sentence variety and rhythm","Tone and voice","Style imitation exercises","Advanced grammar review"]},
    ],
    "history": [
      {"unit":"US History: Gilded Age to WWII","topics":["Industrialization and labor movement","Progressive Era","WWI US involvement","Roaring Twenties","Great Depression and New Deal"]},
      {"unit":"Contemporary Global Issues","topics":["Globalization","Climate change policy","Immigration and migration","Human rights","International organizations (UN, NATO)"]},
      {"unit":"Economics","topics":["Macroeconomics fundamentals","Fiscal and monetary policy","GDP and economic indicators","Unemployment and inflation","Global financial systems"]},
    ],
    "cs": [
      {"unit":"Data Structures & Algorithms","topics":["Arrays and linked lists","Stacks and queues","Sorting algorithms","Searching algorithms","Big-O notation"]},
      {"unit":"Intro to AI & Machine Learning","topics":["What is AI?","Supervised vs. unsupervised learning","Training data and bias","AI ethics","Real-world AI applications"]},
    ],
    "health": [
      {"unit":"Lifetime Fitness Planning","topics":["Setting long-term fitness goals","Creating workout programs","Nutrition for performance","Injury prevention","Fitness tracking tools"]},
      {"unit":"Health Decision Making","topics":["Risk assessment","Peer pressure and social norms","Media influence on health","Healthcare navigation","Insurance basics"]},
    ],
  },
  12: {
    "math": [
      {"unit":"Pre-Calculus / Calculus Intro","topics":["Limits and continuity","Derivative definition","Basic differentiation rules","Product, quotient, chain rules","Applications of derivatives"]},
      {"unit":"Integration","topics":["Antiderivatives","Definite integrals","Fundamental theorem of calculus","Area under a curve","Basic integration techniques"]},
      {"unit":"Statistics (AP-level)","topics":["Probability distributions","Confidence intervals","Hypothesis testing","Regression and correlation","Statistical inference"]},
      {"unit":"Discrete Mathematics","topics":["Logic and proofs","Set theory","Combinatorics","Graph theory","Cryptography basics"]},
    ],
    "science": [
      {"unit":"Advanced Biology / AP Bio","topics":["Biochemistry review","Cell signaling","Gene expression regulation","Evolutionary mechanisms","Ecology and population biology"]},
      {"unit":"Advanced Chemistry / AP Chem","topics":["Equilibrium constants","Acids, bases, and buffers","Electrochemistry","Thermodynamics","Kinetics"]},
      {"unit":"Environmental Science","topics":["Earth's systems","Biodiversity threats","Resource management","Pollution types","Sustainability and policy"]},
    ],
    "ela": [
      {"unit":"AP English Language","topics":["Rhetorical analysis","Synthesis writing","Argumentative essay","AP exam strategies","Citing non-fiction sources"]},
      {"unit":"AP English Literature","topics":["Poetry explication","Prose fiction analysis","Drama analysis","Open-ended essay","Thematic essays on major works"]},
      {"unit":"College Writing Preparation","topics":["College essay writing","Personal statement strategies","Academic writing conventions","Research and citation mastery","Writing portfolios"]},
    ],
    "history": [
      {"unit":"AP US History / Capstone","topics":["Thematic analysis across eras","Primary source analysis","Long Essay Question (LEQ)","Document-Based Question (DBQ)","Historical causation and continuity"]},
      {"unit":"AP Government & Politics","topics":["Constitutional underpinnings","Civil liberties and rights","Institutions of government","Political beliefs and behaviors","Public policy"]},
      {"unit":"Philosophy & Ethics Intro","topics":["Branches of philosophy","Ethical theories (utilitarian, deontological)","Social contract theory","Applied ethics","Critical thinking and argumentation"]},
    ],
    "cs": [
      {"unit":"Capstone Project","topics":["Project planning and design","Software development lifecycle","User interface design","Testing and debugging","Presenting and deploying a project"]},
      {"unit":"Career & College Readiness in CS","topics":["Tech career pathways","College CS programs","Portfolio building","Interview preparation","Open source contributions"]},
    ],
    "health": [
      {"unit":"Adult Health & Wellness","topics":["Preventive care habits","Understanding health insurance","Reproductive health and family planning","Managing chronic conditions","Mental health maintenance"]},
      {"unit":"Senior Capstone: Personal Wellness Plan","topics":["Holistic health assessment","Creating a personal wellness plan","Community health advocacy","Reflecting on lifelong health goals"]},
    ],
  },
}

SUBJ_GEN = {
    "math": math_mc_set,
    "science": sci_mc_set,
    "ela": ela_mc_set,
    "history": hist_mc_set,
    "cs": cs_mc_set,
    "health": health_mc_set,
}

# ── Build TESTS data ──────────────────────────────────────────────────────────
TESTS = {}
total = 0
for grade, subjects in CURRICULUM.items():
    TESTS[grade] = {}
    for subj, units in subjects.items():
        gen = SUBJ_GEN[subj]
        TESTS[grade][subj] = []
        for unit in units:
            topics = unit["topics"]
            if subj == "math":
                qs = gen(unit["unit"], grade)
            else:
                qs = gen(unit["unit"], topics, grade)
            TESTS[grade][subj].append({
                "title": unit["unit"],
                "questions": qs
            })
            total += 1

print(f"Generated {total} unit tests ({total*20} questions total)")

# ── Build tests.html ──────────────────────────────────────────────────────────
tests_json = json.dumps(TESTS, ensure_ascii=False)

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Unit Tests — aceAcademy</title>
<style>
:root{
  --bg:#f7f8fa;--sidebar:#fff;--card:#fff;
  --accent:#4f46e5;--accent2:#7c3aed;
  --text:#1e1b4b;--muted:#6b7280;--border:#e5e7eb;
  --hover:#f0f0ff;--green:#059669;--red:#dc2626;--amber:#d97706;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;display:flex;flex-direction:column}

/* ── NAV ── */
.topnav{background:#fff;border-bottom:1px solid var(--border);padding:0 24px;display:flex;align-items:center;gap:16px;height:56px;position:sticky;top:0;z-index:100;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.topnav .logo{font-weight:800;font-size:1.15rem;color:var(--accent);text-decoration:none;letter-spacing:-.5px}
.topnav .logo span{color:var(--accent2)}
.topnav a.nav-link{font-size:.85rem;color:var(--muted);text-decoration:none;padding:4px 10px;border-radius:6px;transition:all .15s}
.topnav a.nav-link:hover,.topnav a.nav-link.active{background:var(--hover);color:var(--accent)}
.topnav .spacer{flex:1}
.topnav h1{font-size:1rem;font-weight:600;color:var(--text);margin-left:4px}

/* ── GRADE BAR ── */
.grade-bar{background:#fff;border-bottom:1px solid var(--border);padding:10px 24px;display:flex;gap:8px;flex-wrap:wrap}
.grade-btn{padding:6px 16px;border-radius:20px;border:1.5px solid var(--border);background:#fff;color:var(--muted);font-size:.85rem;font-weight:600;cursor:pointer;transition:all .15s}
.grade-btn:hover{border-color:var(--accent);color:var(--accent)}
.grade-btn.active{background:var(--accent);border-color:var(--accent);color:#fff}

/* ── LAYOUT ── */
.layout{display:flex;flex:1;min-height:0}
.sidebar{width:290px;background:var(--sidebar);border-right:1px solid var(--border);overflow-y:auto;padding:16px 0;flex-shrink:0}
.main{flex:1;overflow-y:auto;padding:32px}

/* ── SIDEBAR ── */
.subj-header{display:flex;align-items:center;gap:8px;padding:9px 20px;cursor:pointer;font-size:.875rem;font-weight:700;color:var(--text);transition:background .12s;user-select:none}
.subj-header:hover{background:var(--hover)}
.subj-icon{font-size:1.1rem}
.subj-arrow{margin-left:auto;font-size:.7rem;color:var(--muted);transition:transform .2s}
.subj-header.open .subj-arrow{transform:rotate(90deg)}
.subj-body{display:none;padding-left:12px}
.subj-body.open{display:block}
.unit-item{padding:7px 16px;font-size:.82rem;color:var(--muted);cursor:pointer;border-radius:6px;margin:2px 4px;transition:background .12s;line-height:1.4;display:flex;align-items:center;gap:6px}
.unit-item:hover{background:var(--hover);color:var(--text)}
.unit-item.active{background:#eef2ff;color:var(--accent);font-weight:600}
.unit-badge{font-size:.65rem;background:var(--border);color:var(--muted);padding:1px 6px;border-radius:8px;flex-shrink:0}
.unit-item.done .unit-badge{background:#d1fae5;color:var(--green)}

/* ── EMPTY STATE ── */
.empty-state{display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;min-height:400px;color:var(--muted);text-align:center;gap:12px}
.empty-state .icon{font-size:3rem}
.empty-state h2{font-size:1.2rem;font-weight:600;color:var(--text)}

/* ── TEST WRAP ── */
.test-wrap{display:none;max-width:820px}
.test-wrap.visible{display:block}
.test-header{margin-bottom:24px}
.test-breadcrumb{font-size:.8rem;color:var(--muted);margin-bottom:6px}
.test-breadcrumb span{color:var(--accent)}
.test-title{font-size:1.5rem;font-weight:800;margin-bottom:4px}
.test-meta{font-size:.85rem;color:var(--muted);display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.tag{background:#f0f0ff;color:var(--accent);padding:3px 10px;border-radius:12px;font-weight:600;font-size:.78rem}

/* ── SECTION DIVIDER ── */
.section-label{font-size:.75rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);padding:18px 0 8px;border-top:1px solid var(--border);margin-top:12px}
.section-label:first-child{border-top:none;padding-top:0}

/* ── QUESTION CARD ── */
.q-card{background:#fff;border:1px solid var(--border);border-radius:12px;padding:20px 22px;margin-bottom:14px;transition:border-color .2s}
.q-card.correct{border-color:var(--green);background:#f0fdf4}
.q-card.wrong{border-color:var(--red);background:#fef2f2}
.q-num{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;background:var(--accent);color:#fff;border-radius:50%;font-size:.78rem;font-weight:700;margin-bottom:10px;flex-shrink:0}
.q-card.correct .q-num{background:var(--green)}
.q-card.wrong .q-num{background:var(--red)}
.q-text{font-size:.97rem;font-weight:500;line-height:1.6;margin-bottom:14px;white-space:pre-wrap}

/* MC */
.choices{display:flex;flex-direction:column;gap:8px}
.choice-label{display:flex;align-items:flex-start;gap:10px;cursor:pointer;padding:10px 14px;border-radius:8px;border:1.5px solid var(--border);transition:all .15s;font-size:.9rem;line-height:1.5}
.choice-label:hover{border-color:var(--accent);background:var(--hover)}
.choice-label input{margin-top:3px;accent-color:var(--accent);flex-shrink:0}
.choice-label.selected{border-color:var(--accent);background:#eef2ff}
.choice-label.graded-correct{border-color:var(--green);background:#f0fdf4;font-weight:600}
.choice-label.graded-wrong{border-color:var(--red);background:#fef2f2}

/* SA */
.sa-input{width:100%;padding:10px 14px;border:1.5px solid var(--border);border-radius:8px;font-size:.9rem;font-family:inherit;transition:border-color .2s}
.sa-input:focus{outline:none;border-color:var(--accent)}
.sa-input.correct{border-color:var(--green);background:#f0fdf4}
.sa-input.wrong{border-color:var(--red);background:#fef2f2}

/* SW */
.sw-work{width:100%;min-height:80px;padding:10px 14px;border:1.5px solid var(--border);border-radius:8px;font-size:.9rem;font-family:inherit;resize:vertical;background:#fafafa;transition:border-color .2s}
.sw-work:focus{outline:none;border-color:var(--accent)}
.sw-ans-row{display:flex;align-items:center;gap:10px;margin-top:10px}
.sw-ans-label{font-size:.82rem;font-weight:600;color:var(--muted);white-space:nowrap}
.sw-ans-input{flex:1;padding:9px 14px;border:1.5px solid var(--border);border-radius:8px;font-size:.9rem;font-family:inherit;transition:border-color .2s}
.sw-ans-input:focus{outline:none;border-color:var(--accent)}
.sw-ans-input.correct{border-color:var(--green);background:#f0fdf4}
.sw-ans-input.wrong{border-color:var(--red);background:#fef2f2}

/* Feedback */
.feedback{margin-top:12px;padding:10px 14px;border-radius:8px;font-size:.85rem;line-height:1.5;display:none}
.feedback.show{display:block}
.feedback.correct{background:#f0fdf4;color:#065f46;border-left:3px solid var(--green)}
.feedback.wrong{background:#fef2f2;color:#991b1b;border-left:3px solid var(--red)}

/* ── SUBMIT / RESULTS ── */
.submit-row{margin:28px 0;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
.submit-btn{background:var(--accent);color:#fff;border:none;padding:12px 32px;border-radius:10px;font-size:1rem;font-weight:700;cursor:pointer;transition:background .15s}
.submit-btn:hover{background:var(--accent2)}
.submit-btn:disabled{background:#9ca3af;cursor:not-allowed}
.retake-btn{background:#fff;color:var(--accent);border:2px solid var(--accent);padding:12px 28px;border-radius:10px;font-size:1rem;font-weight:700;cursor:pointer;transition:all .15s}
.retake-btn:hover{background:var(--hover)}

/* Score card */
.score-card{background:#fff;border:2px solid var(--border);border-radius:16px;padding:28px;margin-bottom:28px;text-align:center}
.score-ring{font-size:3rem;font-weight:900;margin-bottom:6px}
.score-ring.a{color:var(--green)}
.score-ring.b{color:#0ea5e9}
.score-ring.c{color:var(--amber)}
.score-ring.d{color:var(--red)}
.score-label{font-size:1rem;color:var(--muted);margin-bottom:16px}
.score-bars{display:flex;gap:16px;justify-content:center;flex-wrap:wrap}
.score-bar-item{text-align:center;font-size:.8rem;color:var(--muted)}
.score-bar-item strong{display:block;font-size:1.1rem;font-weight:800;color:var(--text)}
.progress-bar-outer{height:8px;background:var(--border);border-radius:4px;margin-top:12px;overflow:hidden}
.progress-bar-inner{height:100%;border-radius:4px;background:var(--accent);transition:width .6s ease}
</style>
</head>
<body>
<nav class="topnav">
  <a href="index.html" class="logo">ace<span>Academy</span></a>
  <a href="curriculum.html" class="nav-link">📚 Curriculum</a>
  <a href="worksheets.html" class="nav-link">📄 Worksheets</a>
  <a href="tests.html" class="nav-link active">✏️ Tests</a>
  <a href="tutor.html" class="nav-link">🤖 Tutor</a>
  <div class="spacer"></div>
  <h1>Unit Tests</h1>
</nav>

<div class="grade-bar">
  <button class="grade-btn active" onclick="selectGrade(6,this)">Grade 6</button>
  <button class="grade-btn" onclick="selectGrade(7,this)">Grade 7</button>
  <button class="grade-btn" onclick="selectGrade(8,this)">Grade 8</button>
  <button class="grade-btn" onclick="selectGrade(9,this)">Grade 9</button>
  <button class="grade-btn" onclick="selectGrade(10,this)">Grade 10</button>
  <button class="grade-btn" onclick="selectGrade(11,this)">Grade 11</button>
  <button class="grade-btn" onclick="selectGrade(12,this)">Grade 12</button>
</div>

<div class="layout">
  <div class="sidebar" id="sidebar"></div>
  <div class="main" id="main">
    <div class="empty-state" id="emptyState">
      <div class="icon">✏️</div>
      <h2>Select a unit to start your test</h2>
      <p>Choose a grade, subject, and unit from the sidebar. Each test has 20 questions — multiple choice, short answer, and show-your-work.</p>
    </div>
    <div class="test-wrap" id="testWrap"></div>
  </div>
</div>

<script>
const TESTS = """ + tests_json + r""";

const SUBJECTS = {
  math:    {label:"Mathematics",  icon:"📐"},
  science: {label:"Science",      icon:"🔬"},
  ela:     {label:"English / ELA",icon:"📚"},
  history: {label:"History",      icon:"🌍"},
  cs:      {label:"Computer Sci.",icon:"💻"},
  health:  {label:"Health & PE",  icon:"🏃"},
};

let currentGrade = 6;
let currentTest = null; // {grade,subj,unitIdx}
const scores = {}; // key → score

function scoreKey(g,s,u){ return `${g}-${s}-${u}`; }

function selectGrade(grade,btn){
  currentGrade = grade;
  document.querySelectorAll('.grade-btn').forEach(b=>b.classList.remove('active'));
  btn.classList.add('active');
  clearTest();
  buildSidebar(grade);
}

function buildSidebar(grade){
  const sidebar = document.getElementById('sidebar');
  const gradeData = TESTS[grade];
  if(!gradeData){ sidebar.innerHTML='<p style="padding:20px;color:var(--muted);font-size:.85rem">No tests for this grade yet.</p>'; return; }
  let html = '';
  for(const [subj, meta] of Object.entries(SUBJECTS)){
    const units = gradeData[subj];
    if(!units||!units.length) continue;
    const sId = `s-${grade}-${subj}`;
    html += `<div>
      <div class="subj-header" id="${sId}-h" onclick="toggleSubj('${sId}')">
        <span class="subj-icon">${meta.icon}</span>
        <span>${meta.label}</span>
        <span class="subj-arrow">▶</span>
      </div>
      <div class="subj-body" id="${sId}-b">`;
    units.forEach((unit,ui)=>{
      const key = scoreKey(grade,subj,ui);
      const sc = scores[key];
      const done = sc !== undefined;
      const pct = done ? Math.round(sc.correct/sc.total*100) : null;
      const badge = done ? `${pct}%` : '20q';
      html += `<div class="unit-item${done?' done':''}" id="ui-${grade}-${subj}-${ui}" onclick="openTest(${grade},'${subj}',${ui})">
        <span>${unit.title}</span>
        <span class="unit-badge">${badge}</span>
      </div>`;
    });
    html += `</div></div>`;
  }
  sidebar.innerHTML = html;
}

function toggleSubj(id){
  document.getElementById(id+'-h').classList.toggle('open');
  document.getElementById(id+'-b').classList.toggle('open');
}

function openTest(grade,subj,unitIdx){
  document.querySelectorAll('.unit-item').forEach(e=>e.classList.remove('active'));
  const el = document.getElementById(`ui-${grade}-${subj}-${unitIdx}`);
  if(el) el.classList.add('active');

  currentTest = {grade,subj,unitIdx};
  const unit = TESTS[grade][subj][unitIdx];
  renderTest(grade,subj,unitIdx,unit);
}

function renderTest(grade,subj,unitIdx,unit){
  document.getElementById('emptyState').style.display='none';
  const wrap = document.getElementById('testWrap');
  wrap.classList.add('visible');

  const meta = SUBJECTS[subj];
  const qs = unit.questions;

  // Group by type
  const mcQs=[], saQs=[], swQs=[];
  qs.forEach((q,i)=>{
    if(q.type==='mc') mcQs.push({q,i});
    else if(q.type==='sa') saQs.push({q,i});
    else swQs.push({q,i});
  });

  let qNum = 0;

  function renderMC({q,i}){
    qNum++;
    const n = qNum;
    return `<div class="q-card" id="qc-${i}">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
        <div class="q-num" id="qnum-${i}">${n}</div>
        <span style="font-size:.72rem;font-weight:700;color:var(--muted);letter-spacing:.06em">MULTIPLE CHOICE</span>
      </div>
      <div class="q-text">${q.q}</div>
      <div class="choices" id="choices-${i}">
        ${q.choices.map((c,ci)=>`<label class="choice-label" id="cl-${i}-${ci}">
          <input type="radio" name="q${i}" value="${ci}" onchange="selectChoice(${i},${ci})"> ${c}
        </label>`).join('')}
      </div>
      <div class="feedback" id="fb-${i}"></div>
    </div>`;
  }

  function renderSA({q,i}){
    qNum++;
    const n = qNum;
    return `<div class="q-card" id="qc-${i}">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
        <div class="q-num" id="qnum-${i}">${n}</div>
        <span style="font-size:.72rem;font-weight:700;color:var(--muted);letter-spacing:.06em">SHORT ANSWER</span>
      </div>
      <div class="q-text">${q.q}</div>
      <input class="sa-input" id="sa-${i}" type="text" placeholder="Type your answer here…" autocomplete="off"/>
      <div class="feedback" id="fb-${i}"></div>
    </div>`;
  }

  function renderSW({q,i}){
    qNum++;
    const n = qNum;
    return `<div class="q-card" id="qc-${i}">
      <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
        <div class="q-num" id="qnum-${i}">${n}</div>
        <span style="font-size:.72rem;font-weight:700;color:var(--muted);letter-spacing:.06em">SHOW YOUR WORK</span>
      </div>
      <div class="q-text">${q.q}</div>
      <textarea class="sw-work" id="sw-work-${i}" placeholder="Show your work here…"></textarea>
      <div class="sw-ans-row">
        <span class="sw-ans-label">Final Answer:</span>
        <input class="sw-ans-input" id="sw-ans-${i}" type="text" placeholder="Write your final answer…" autocomplete="off"/>
      </div>
      <div class="feedback" id="fb-${i}"></div>
    </div>`;
  }

  qNum = 0;
  let html = `<div class="test-header">
    <div class="test-breadcrumb">Grade ${grade} &rsaquo; <span>${meta.label}</span></div>
    <div class="test-title">${unit.title}</div>
    <div class="test-meta">
      <span class="tag">Grade ${grade}</span>
      <span class="tag">${meta.icon} ${meta.label}</span>
      <span class="tag">20 Questions</span>
    </div>
    <div class="progress-bar-outer" style="margin-top:12px">
      <div class="progress-bar-inner" id="progressBar" style="width:0%"></div>
    </div>
  </div>
  <div id="scoreCard" style="display:none"></div>`;

  if(mcQs.length){
    html += `<div class="section-label">📝 Section A — Multiple Choice</div>`;
    mcQs.forEach(item=>{ html += renderMC(item); });
  }
  if(saQs.length){
    html += `<div class="section-label">✏️ Section B — Short Answer</div>`;
    saQs.forEach(item=>{ html += renderSA(item); });
  }
  if(swQs.length){
    html += `<div class="section-label">🔢 Section C — Show Your Work</div>`;
    swQs.forEach(item=>{ html += renderSW(item); });
  }

  html += `<div class="submit-row">
    <button class="submit-btn" id="submitBtn" onclick="gradeTest()">Submit Test</button>
    <span id="unansweredMsg" style="font-size:.85rem;color:var(--muted)"></span>
  </div>`;

  wrap.innerHTML = html;
  wrap.scrollTop = 0;
  updateProgress();
}

function selectChoice(qi, ci){
  document.querySelectorAll(`label[id^="cl-${qi}-"]`).forEach(l=>l.classList.remove('selected'));
  document.getElementById(`cl-${qi}-${ci}`)?.classList.add('selected');
  updateProgress();
}

function updateProgress(){
  const qs = TESTS[currentTest?.grade]?.[currentTest?.subj]?.[currentTest?.unitIdx]?.questions;
  if(!qs) return;
  let answered = 0;
  qs.forEach((q,i)=>{
    if(q.type==='mc' && document.querySelector(`input[name="q${i}"]:checked`)) answered++;
    else if(q.type==='sa' && document.getElementById(`sa-${i}`)?.value.trim()) answered++;
    else if(q.type==='sw' && document.getElementById(`sw-ans-${i}`)?.value.trim()) answered++;
  });
  const pct = Math.round(answered/qs.length*100);
  const bar = document.getElementById('progressBar');
  if(bar) bar.style.width = pct+'%';
}

function normalize(s){ return String(s).trim().toLowerCase().replace(/[.,!?]/g,''); }
function numClose(a,b){ const na=parseFloat(a),nb=parseFloat(b); return !isNaN(na)&&!isNaN(nb)&&Math.abs(na-nb)<0.01; }

function gradeTest(){
  const {grade,subj,unitIdx} = currentTest;
  const qs = TESTS[grade][subj][unitIdx].questions;
  let correct=0, total=qs.length;

  qs.forEach((q,i)=>{
    const card = document.getElementById(`qc-${i}`);
    const fb   = document.getElementById(`fb-${i}`);
    let isCorrect = false;

    if(q.type==='mc'){
      const sel = document.querySelector(`input[name="q${i}"]:checked`);
      const chosen = sel ? parseInt(sel.value) : -1;
      isCorrect = chosen === q.correct;
      // colour choices
      q.choices.forEach((_,ci)=>{
        const lbl = document.getElementById(`cl-${i}-${ci}`);
        if(!lbl) return;
        lbl.querySelector('input').disabled = true;
        if(ci === q.correct) lbl.classList.add('graded-correct');
        else if(ci === chosen && !isCorrect) lbl.classList.add('graded-wrong');
      });
    } else if(q.type==='sa'){
      const inp = document.getElementById(`sa-${i}`);
      if(inp){
        inp.disabled=true;
        const userVal = inp.value.trim();
        isCorrect = normalize(userVal)===normalize(q.ans) || numClose(userVal,q.ans) ||
                    normalize(q.ans).includes(normalize(userVal)) ||
                    normalize(userVal).includes(normalize(q.ans));
        inp.classList.add(isCorrect?'correct':'wrong');
      }
    } else { // sw
      const inp = document.getElementById(`sw-ans-${i}`);
      const work = document.getElementById(`sw-work-${i}`);
      if(inp){
        inp.disabled=true;
        if(work) work.disabled=true;
        const userVal = inp.value.trim();
        const expected = String(q.ans);
        isCorrect = normalize(userVal)===normalize(expected) || numClose(userVal,expected);
        inp.classList.add(isCorrect?'correct':'wrong');
      }
    }

    if(card){
      card.classList.add(isCorrect?'correct':'wrong');
      document.getElementById(`qnum-${i}`)?.classList.add(isCorrect?'correct':'wrong');
    }
    if(fb){
      fb.classList.add('show',isCorrect?'correct':'wrong');
      fb.innerHTML = isCorrect
        ? `✅ <strong>Correct!</strong> ${q.exp}`
        : `❌ <strong>Incorrect.</strong> ${q.exp} <br><em>Correct answer: ${q.type==='mc'?q.choices[q.correct]:q.ans}</em>`;
    }
    if(isCorrect) correct++;
  });

  // Score card
  const pct = Math.round(correct/total*100);
  let grade_letter = pct>=90?'a':pct>=80?'b':pct>=70?'c':'d';
  let emoji = pct>=90?'🏆':pct>=80?'⭐':pct>=70?'👍':'📖';
  let msg = pct>=90?'Excellent work!':pct>=80?'Great job!':pct>=70?'Good effort — review the red questions.':'Keep studying — you\'ll get it!';

  const sc = document.getElementById('scoreCard');
  sc.style.display='block';
  sc.innerHTML = `<div class="score-card">
    <div class="score-ring ${grade_letter}">${emoji} ${pct}%</div>
    <div class="score-label">${correct} / ${total} correct — ${msg}</div>
    <div class="score-bars">
      <div class="score-bar-item"><strong>${correct}</strong>Correct</div>
      <div class="score-bar-item"><strong>${total-correct}</strong>Incorrect</div>
      <div class="score-bar-item"><strong>${pct}%</strong>Score</div>
    </div>
  </div>`;
  sc.scrollIntoView({behavior:'smooth', block:'start'});

  // Update progress bar to 100% and record score
  const bar = document.getElementById('progressBar');
  if(bar){ bar.style.width='100%'; bar.style.background = pct>=70?'var(--green)':'var(--red)'; }
  document.getElementById('submitBtn').innerHTML = `✅ Submitted — ${pct}%`;
  document.getElementById('submitBtn').disabled = true;

  // Add retake button
  const row = document.querySelector('.submit-row');
  if(row){
    const rb = document.createElement('button');
    rb.className = 'retake-btn';
    rb.textContent = '🔄 Retake Test';
    rb.onclick = ()=> openTest(currentTest.grade, currentTest.subj, currentTest.unitIdx);
    row.appendChild(rb);
  }

  // Store score & refresh sidebar badge
  scores[scoreKey(grade,subj,unitIdx)] = {correct,total};
  buildSidebar(grade);
  document.getElementById(`ui-${grade}-${subj}-${unitIdx}`)?.classList.add('active');
}

function clearTest(){
  document.getElementById('emptyState').style.display='';
  const wrap=document.getElementById('testWrap');
  wrap.classList.remove('visible');
  wrap.innerHTML='';
  currentTest=null;
}

// ── INIT ──────────────────────────────────────────────────────────────────────
buildSidebar(6);

// Auto-update progress as user types
document.getElementById('testWrap').addEventListener('input', updateProgress);
</script>
</body>
</html>"""

out = pathlib.Path("/sessions/admiring-stoic-pascal/mnt/outputs/tests.html")
out.write_text(HTML, encoding="utf-8")
print(f"tests.html written ({out.stat().st_size//1024} KB)")
