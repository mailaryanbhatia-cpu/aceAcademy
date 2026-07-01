const fs = require('fs');
const html = fs.readFileSync('/sessions/admiring-stoic-pascal/mnt/outputs/curriculum.html', 'utf8');
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];

// Extract PRACTICE block
const practStart = script.indexOf('const PRACTICE = {');
let depth = 0, inP = false, practEnd = practStart;
for (let i = practStart; i < script.length; i++) {
  if (script[i] === '{') { depth++; inP = true; }
  if (script[i] === '}') depth--;
  if (inP && depth === 0) { practEnd = i + 1; break; }
}

const subjStart = script.indexOf('const SUBJECTS');
const subjEnd = script.indexOf('];', subjStart) + 2;
const subjCode = script.slice(subjStart, subjEnd);
let currStart = script.indexOf('const CURRICULUM = {');
let depth2 = 0, inC = false, currEnd = currStart;
for (let i = currStart; i < script.length; i++) {
  if (script[i] === '{') { depth2++; inC = true; }
  if (script[i] === '}') depth2--;
  if (inC && depth2 === 0) { currEnd = i + 1; break; }
}

const fn = new Function(
  script.slice(practStart, practEnd) + ';' +
  subjCode +
  script.slice(currStart, currEnd) + ';' +
  'return {PRACTICE, SUBJECTS, CURRICULUM};'
);
const {PRACTICE, SUBJECTS, CURRICULUM} = fn();

// Helper
const u = (s1title, s1probs, s2title, s2probs) => [
  {title: s1title, problems: s1probs},
  {title: s2title, problems: s2probs}
];
const p = (q, ex, a) => ({q, ex, a});

// ── GRADE 6 ──
PRACTICE[6].ela[4] = u(
  'Oral Presentation Skills',
  [p('What are three key elements of an effective oral presentation?','Think: preparation, delivery, and audience',
     'Clear organization (intro, body, conclusion), engaging delivery (eye contact, pacing, volume), and audience awareness (appropriate vocabulary, engaging questions).'),
   p('How do you use body language effectively when presenting?','Think: what you do with your hands, eyes, and posture',
     'Maintain eye contact with the audience, stand or sit upright, use purposeful hand gestures to emphasize points, and avoid fidgeting or crossing your arms.'),
   p('What is the difference between formal and informal speaking? Give an example of each.','Think about your word choices and tone',
     'Formal: structured, professional language used in presentations or debates (e.g., "I would like to argue..."). Informal: casual, everyday language used with friends (e.g., "I think...").'),
   p('A classmate speaks too fast during a presentation. What specific advice would you give them?','Think: what helps listeners follow along',
     'Practice pausing between key points, use a timer during rehearsal, breathe deeply before starting, mark the script with pause symbols, and focus on speaking to listeners, not at them.')],
  'Active Listening & Discussion',
  [p('What does it mean to be an "active listener"? Name three strategies.','Think: what your body and mind are doing while listening',
     'Active listening means fully concentrating on the speaker. Strategies: maintain eye contact, take notes on key points, ask clarifying questions, and avoid interrupting.'),
   p('During a class discussion, a student says something you disagree with. How should you respond respectfully?','Think: acknowledge, then offer your perspective',
     'Acknowledge their point first ("I understand your view..."), then politely present your own ("However, I think... because..."). Avoid personal attacks and use evidence to support your position.'),
   p('What is the purpose of asking follow-up questions during a discussion?','Think: what questions do for conversations',
     'Follow-up questions deepen understanding, encourage elaboration, clarify meaning, and show engagement. They push discussion beyond surface-level responses.'),
   p('What is the difference between hearing and listening?','Think: one is passive, one is active',
     'Hearing is the physical process of receiving sound. Listening is the active mental process of interpreting and understanding that sound, including paying attention and making meaning.')]
);

// ── GRADE 7 ──
// science[2] = Life Science: Body Systems
PRACTICE[7].science[2] = u(
  'Major Body Systems',
  [p('What is the function of the circulatory system? Name its three main components.','Think: how does blood travel through the body?',
     'The circulatory system transports blood, oxygen, and nutrients. Components: the heart (pump), blood vessels (highways), and blood (transport medium).'),
   p('How do the respiratory and circulatory systems work together?','Think: what happens when you breathe in',
     'The respiratory system brings oxygen into the lungs; the circulatory system picks up that oxygen via the blood and delivers it to body cells, while returning CO₂ to the lungs to be exhaled.'),
   p('What is the role of the digestive system? Trace the path of food from mouth to intestine.','Think: breakdown, absorption, waste',
     'The digestive system breaks down food into nutrients. Path: mouth (chewing/saliva) → esophagus → stomach (acid digestion) → small intestine (nutrient absorption) → large intestine (water absorption) → rectum/anus.'),
   p('What is the difference between voluntary and involuntary muscles? Give one example of each.','Think: what you control vs. what happens automatically',
     'Voluntary muscles are controlled consciously (e.g., bicep). Involuntary muscles work automatically (e.g., heart, digestive tract muscles). Cardiac muscle is a special involuntary type found only in the heart.')],
  'Body System Interactions & Homeostasis',
  [p('What is homeostasis? Give one example of the body maintaining it.','Think: the body keeping itself in balance',
     'Homeostasis is the body\'s ability to maintain a stable internal environment. Example: when body temperature rises, sweat glands activate to cool it down through evaporation.'),
   p('How do the nervous and muscular systems work together when you touch something hot?','Think: signal, response, action',
     'Sensory neurons detect heat and send signals to the brain/spinal cord. The nervous system instantly sends a motor signal back to muscles, causing you to pull your hand away (reflex arc).'),
   p('How does the skeletal system support and protect the body? Name two specific examples.','Think: structure and protection',
     'The skeleton provides structure (bones support body weight) and protection (skull protects the brain, ribcage protects heart/lungs). It also works with muscles to enable movement.'),
   p('Why is the immune system important? Describe two ways it defends the body.','Think: first and second lines of defense',
     'The immune system protects against pathogens. Defenses: (1) physical barriers like skin and mucus trap germs; (2) white blood cells identify and destroy invaders. Antibodies also neutralize specific threats.')]
);

// science[3] = Earth Science
PRACTICE[7].science[3] = u(
  'Earth\'s Structure & Plate Tectonics',
  [p('What are the four layers of the Earth? Describe each briefly.','Think: crust, mantle, outer core, inner core',
     'Crust: thin, rocky outer layer. Mantle: thick layer of semi-solid rock that flows slowly. Outer core: liquid iron and nickel. Inner core: solid iron and nickel, extremely hot and dense.'),
   p('What is plate tectonics? Name the three types of plate boundaries.','Think: plates are like puzzle pieces that move',
     'Plate tectonics is the theory that Earth\'s crust is divided into moving plates. Boundaries: convergent (plates collide), divergent (plates pull apart), and transform (plates slide past each other).'),
   p('How do earthquakes form? Where are they most common?','Think: stored energy being released',
     'Earthquakes occur when tectonic plates suddenly slip, releasing stored elastic energy as seismic waves. Most common near plate boundaries, especially the "Ring of Fire" around the Pacific Ocean.'),
   p('What causes volcanic eruptions, and what are the two main types of volcanoes?','Think: pressure below the surface',
     'Magma from the mantle pushes up through cracks in the crust. Types: shield volcanoes (broad, gentle slopes, fluid lava) and composite/stratovolcanoes (steep, explosive, layered ash and lava).')],
  'Weather, Climate & the Water Cycle',
  [p('What is the difference between weather and climate?','Think: short-term vs. long-term atmospheric conditions',
     'Weather is the day-to-day atmospheric conditions (temperature, precipitation, wind) in a specific location. Climate is the average weather pattern in a region over a long period (30+ years).'),
   p('Describe the water cycle. Include at least four processes.','Think: evaporation, condensation, precipitation, collection',
     'Evaporation: water turns to vapor from oceans/lakes. Transpiration: plants release water vapor. Condensation: vapor cools and forms clouds. Precipitation: water falls as rain/snow. Collection: water gathers in oceans/rivers/groundwater.'),
   p('What causes the seasons on Earth?','Think: Earth\'s tilt, not its distance from the sun',
     'Seasons are caused by Earth\'s 23.5° axial tilt. When the Northern Hemisphere tilts toward the sun, it receives more direct sunlight → summer. When it tilts away → winter. Distance from the sun is NOT the cause.'),
   p('What is a biome? Name three biomes and their key characteristics.','Think: large ecological regions defined by climate',
     'A biome is a large region defined by its climate and dominant organisms. Examples: Tropical rainforest (hot, wet, high biodiversity); Desert (low precipitation, extreme temperatures); Temperate forest (seasonal, deciduous trees).')]
);

// ela[1] = Reading Informational Text
PRACTICE[7].ela[1] = u(
  'Main Idea & Text Structure',
  [p('What is the difference between a topic and a main idea?','Think: topic is the subject; main idea is the point being made',
     'Topic is the broad subject (e.g., "climate change"). Main idea is the specific point the author makes about that topic (e.g., "Human activity is the primary driver of climate change").'),
   p('A news article is organized by stating the conclusion first, then explaining the reasons. What text structure is this?','Think: how journalism structures information',
     'Inverted pyramid structure. This is common in journalism: the most important information (who, what, when, where, why) comes first, followed by supporting details and background in decreasing importance.'),
   p('What is a central claim, and how do you identify evidence that supports it?','Think: thesis vs. supporting details',
     'A central claim is the author\'s main argument or position. Supporting evidence includes: statistics, expert quotes, examples, case studies, and data that directly connect to and strengthen the claim.'),
   p('Read this topic sentence: "Social media has significantly changed the way teenagers communicate." Identify the topic and the controlling idea.','Think: topic = what; controlling idea = the angle taken',
     'Topic: social media and teenage communication. Controlling idea: social media has "significantly changed" it. The rest of the paragraph should explain HOW it has changed communication.')]  ,
  'Author\'s Purpose & Evidence',
  [p('What are the three main purposes an author can have? Give an example text type for each.','Think: PIE — Persuade, Inform, Entertain',
     'Persuade: editorial, opinion column. Inform: textbook, encyclopedia, news article. Entertain: short story, novel, poem. Some texts serve multiple purposes.'),
   p('What is the difference between a fact and an opinion? Give one example of each.','Think: can it be proven?',
     'Fact: verifiable statement (e.g., "The Amazon rainforest covers 5.5 million km²."). Opinion: a judgment or belief (e.g., "The Amazon rainforest is the most beautiful place on Earth."). Opinions often use words like "should," "best," or "believe."'),
   p('Why might an author include a counterargument in an informational text?','Think: what does addressing opposing views accomplish?',
     'To show fairness and credibility (ethos), to strengthen their own argument by refuting the opposing view, and to address potential objections readers might have before they arise.'),
   p('An author writing about factory farming uses only quotes from animal rights activists. What is the problem with this approach?','Think: what makes evidence strong?',
     'The evidence is biased — it presents only one perspective. Strong informational writing uses diverse, credible sources including experts from multiple viewpoints, data, and peer-reviewed research to give a balanced and accurate picture.')]
);

// ela[2] = Writing
PRACTICE[7].ela[2] = u(
  'Argumentative & Informational Writing',
  [p('What are the three components of a strong argument? Briefly define each.','Think: claim, evidence, reasoning',
     'Claim: your position or thesis. Evidence: facts, data, or quotes that support it. Reasoning (warrant): the explanation of HOW the evidence supports the claim. Without reasoning, evidence is just a list of facts.'),
   p('What is the purpose of a hook in an essay introduction? Write an example hook for an essay about online learning.','Think: capture attention immediately',
     'A hook grabs the reader\'s attention. Example: "Imagine attending school in your pajamas, learning at your own pace, anywhere in the world — that is the promise of online education." Hooks can be questions, surprising facts, quotes, or anecdotes.'),
   p('What is the difference between a formal and informal writing tone? Give an example of each for the same idea.','Think: word choice, sentence structure, contractions',
     'Formal: "Research indicates that exercise improves cognitive function." Informal: "Working out makes your brain work better!" Formal writing avoids contractions, slang, and personal pronouns; informal uses them freely.'),
   p('Rewrite this weak thesis: "This essay will be about the effects of homework." Make it argumentative.','Think: take a clear position with a reason',
     'Strong thesis example: "Excessive homework harms students\' mental health and should be limited to 30 minutes per night in middle school." It states a clear position and hints at the reasoning the essay will develop.')],
  'Writing Process & Revision',
  [p('What are the five stages of the writing process?','Think: prewriting through publishing',
     'Prewriting (brainstorm/plan), Drafting (write freely), Revising (improve content and structure), Editing (fix grammar and mechanics), Publishing (sharing the final piece).'),
   p('What is the difference between revising and editing?','Think: big picture vs. small details',
     'Revising focuses on content: strengthening arguments, reorganizing paragraphs, adding/removing details, improving clarity. Editing focuses on mechanics: grammar, spelling, punctuation, and formatting.'),
   p('A peer reviewer writes: "Your paragraph jumps between two ideas without clear connection." What revision strategy should you use?','Think: how do you link ideas smoothly?',
     'Add transition words and sentences (e.g., "Furthermore," "In contrast," "This connects to...") and make sure each sentence in the paragraph relates directly to the topic sentence. Consider splitting into two paragraphs if the ideas are truly distinct.'),
   p('Why is audience important when writing? How would you change an essay about climate change for (a) a scientist vs. (b) a 5th grader?','Think: vocabulary, assumptions, examples',
     'Audience determines vocabulary, examples, and depth. For a scientist: use technical terms, cite studies, assume background knowledge. For a 5th grader: use simple vocabulary, relatable analogies (like a blanket around Earth), and avoid jargon.')]
);

// ela[3] = Language & Grammar
PRACTICE[7].ela[3] = u(
  'Grammar & Mechanics',
  [p('What is the difference between a phrase and a clause? Give one example of each.','Think: does it have a subject and verb?',
     'A phrase is a group of words without a subject-verb pair (e.g., "in the morning"). A clause has a subject and verb (e.g., "when the sun rose"). An independent clause can stand alone; a dependent clause cannot.'),
   p('Identify the error and correct this sentence: "Me and my friend went to the store."','Think: subject pronouns vs. object pronouns',
     'Error: "Me" is an object pronoun used incorrectly as a subject. Corrected: "My friend and I went to the store." Tip: remove "my friend" — "Me went to the store" sounds wrong; "I went to the store" is correct.'),
   p('What is a comma splice? Correct this example: "I love soccer, it is my favorite sport."','Think: what makes a run-on sentence?',
     'A comma splice joins two independent clauses with only a comma. Corrections: (1) "I love soccer; it is my favorite sport." (2) "I love soccer. It is my favorite sport." (3) "I love soccer, and it is my favorite sport."'),
   p('What is an appositive phrase? Add an appositive phrase to this sentence: "My teacher helped me."','Think: a noun phrase that renames or describes another noun',
     'An appositive is a noun phrase that renames the noun beside it. Example: "My teacher, Ms. Rivera, a passionate writer, helped me." The appositive "a passionate writer" renames "Ms. Rivera."')],
  'Vocabulary in Context',
  [p('What are context clues? Name two types and give an example of each.','Think: how surrounding words help you understand unknown words',
     'Context clues are words/phrases nearby that help define unknown words. Types: (1) Definition clue — "The arborist, or tree doctor, pruned the oak." (2) Contrast clue — "Unlike her gregarious brother, she was shy and reclusive."'),
   p('The word "benevolent" comes from Latin bene (good) + volens (wishing). What does benevolent mean? Give a sentence using it correctly.','Think: break down the root meanings',
     'Benevolent means well-meaning and kindly, wanting good for others. Example: "The benevolent donor gave millions to fund schools in underserved communities."'),
   p('What is the difference between denotation and connotation? Give an example using the word "stubborn."','Think: dictionary meaning vs. emotional meaning',
     'Denotation: literal dictionary meaning ("stubborn" = refusing to change position). Connotation: emotional associations. "Stubborn" has a negative connotation, while "determined" has a positive one — even though they\'re similar in meaning.'),
   p('Read: "The politician\'s rhetoric was incendiary, sparking protests across the city." Using context, what does incendiary mean?','Think: what happened as a result of the speech?',
     'Incendiary means likely to cause anger or controversy (literally: "likely to cause fire"). The context clue is "sparking protests" — the speech caused an inflammatory, heated reaction in the public.')]
);

// history[1] = Renaissance & Reformation
PRACTICE[7].history[1] = u(
  'The Renaissance',
  [p('What does "Renaissance" mean, and where did it begin?','Think: rebirth of classical ideas',
     '"Renaissance" means "rebirth" in French. It began in Italy (Florence) in the 14th century as wealthy merchants and city-states patronized art and learning inspired by ancient Greece and Rome.'),
   p('What was humanism? How did it differ from medieval thinking?','Think: focus on human potential vs. religious focus',
     'Humanism valued human reason, achievement, and individual potential rather than focusing solely on religious devotion. Medieval thinking centered on God and the afterlife; humanism celebrated earthly life and human capability.'),
   p('Name two Renaissance artists and describe a major work or contribution from each.','Think: Leonardo, Michelangelo, Raphael, Botticelli...',
     'Leonardo da Vinci: painted the Mona Lisa and studied anatomy scientifically. Michelangelo: painted the Sistine Chapel ceiling and sculpted David. Both exemplified the Renaissance ideal of the universal person skilled in art, science, and philosophy.'),
   p('How did the printing press (invented by Gutenberg ~1440) change European society?','Think: books before and after the press',
     'Before: books were hand-copied and rare. After: books could be mass-produced cheaply. This spread literacy, enabled the Reformation (Luther\'s ideas spread rapidly), advanced science, and weakened the Church\'s information monopoly.')],
  'The Protestant Reformation',
  [p('What were Martin Luther\'s main criticisms of the Catholic Church?','Think: what was he protesting?',
     'Luther criticized the selling of indulgences (paying for forgiveness), corruption in the Church, and the pope\'s authority. His 95 Theses (1517) argued salvation comes through faith alone (sola fide), not works or payments.'),
   p('What were the long-term political effects of the Reformation in Europe?','Think: how did religious division affect kings and kingdoms?',
     'Religious wars broke out (Thirty Years\' War). Princes gained power over religion in their territories (Peace of Augsburg: "cuius regio, eius religio"). The Holy Roman Empire fragmented. Nation-states grew stronger relative to the Church.'),
   p('How did John Calvin\'s ideas differ from Luther\'s?','Think: predestination, theocracy',
     'Calvin believed in predestination (God chose who would be saved before birth) and set up a strict theocratic government in Geneva. Luther focused more on faith and scripture; Calvin emphasized God\'s absolute sovereignty and community discipline.'),
   p('What was the Counter-Reformation and what were its main goals?','Think: the Catholic Church\'s response',
     'The Catholic Church\'s reform movement in response to Protestantism. Goals: clarify Catholic doctrine (Council of Trent), combat heresy (Inquisition), spread Catholicism (Jesuits), and reform internal corruption. It reinvigorated Catholic faith globally.')]
);

// history[2] = Early Americas
PRACTICE[7].history[2] = u(
  'Pre-Columbian Civilizations',
  [p('Name three major pre-Columbian civilizations and one achievement of each.','Think: Maya, Aztec, Inca',
     'Maya: advanced writing (hieroglyphs), calendar, mathematics (zero), astronomy. Aztec: Tenochtitlán (floating city), complex trade networks. Inca: road system spanning 25,000 miles, terrace farming in the Andes, quipu record-keeping.'),
   p('How did geography shape the development of Native American cultures across North America?','Think: environment → lifestyle',
     'Pacific Northwest: abundance of salmon → fishing societies, totem poles. Great Plains: bison herds → nomadic hunting cultures. Southwest: arid climate → pueblo architecture, irrigation farming. Geography drove food sources, housing, trade, and culture.'),
   p('What was the significance of the Aztec capital Tenochtitlán?','Think: location, size, organization',
     'Built on an island in Lake Texcoco (modern Mexico City), it was one of the largest cities in the world (~200,000 people) with causeways, aqueducts, temples, and a sophisticated market system. It demonstrated advanced urban planning.'),
   p('What role did religion play in Aztec society?','Think: rituals, sacrifice, connection to governance',
     'Religion was central: gods controlled nature, war, and harvests. Priests held enormous power. Human sacrifice was practiced to honor gods and maintain cosmic order. Religious rituals aligned with the agricultural calendar and political authority.')],
  'European Contact & Colonization',
  [p('What was Columbus\'s impact on the Americas? Include both intended and unintended consequences.','Think: exploration goals vs. what actually happened',
     'Intended: find trade route to Asia. Unintended: triggered mass colonization. Impact: Columbian Exchange (new foods, animals, diseases spread globally), decimation of Indigenous populations through disease (90%+ in some areas), slavery, and permanent European settlements.'),
   p('What was the Columbian Exchange? Give two examples of goods exchanged in each direction.','Think: what moved between hemispheres',
     'The transfer of plants, animals, and diseases between the Americas and Europe/Africa/Asia. Americas → Europe: potatoes, tomatoes, corn, chocolate, tobacco. Europe → Americas: horses, cattle, wheat, smallpox (devastating to Indigenous people).'),
   p('How did the Spanish encomienda system work, and why was it criticized?','Think: labor, land, and Indigenous people',
     'Spanish colonizers were granted land and the labor of Indigenous people in exchange for "protecting" and Christianizing them. In practice, it was forced labor, causing mass deaths and abuse. Priests like Bartolomé de las Casas denounced it as cruel.'),
   p('Why were Indigenous populations devastated by European diseases?','Think: no immunity, no prior exposure',
     'Indigenous peoples had no immunity to European diseases like smallpox, measles, and typhus because they had never been exposed. These diseases spread faster than Europeans moved, killing up to 90% of some populations — far more than warfare.')]
);

console.log('Grade 6-7 done');

// ── GRADE 8 ──
// science[2] = Waves & Electromagnetic Spectrum
PRACTICE[8].science[2] = u(
  'Wave Properties',
  [p('What is a wave? What are the two main types of mechanical waves?','Think: energy transfer, not matter transfer',
     'A wave is a disturbance that transfers energy through matter or space. Mechanical wave types: transverse (particles move perpendicular to wave direction, e.g., light, rope waves) and longitudinal (particles move parallel, e.g., sound waves).'),
   p('Define amplitude, wavelength, and frequency. How are frequency and wavelength related?','Think: the three key descriptors of a wave',
     'Amplitude: height of the wave (related to energy). Wavelength: distance between two crests. Frequency: number of waves per second (Hz). Relationship: as frequency increases, wavelength decreases (inversely proportional) at a constant wave speed.'),
   p('A wave has a frequency of 200 Hz and a speed of 400 m/s. What is its wavelength?','Think: wave speed = frequency × wavelength',
     'Wavelength = speed ÷ frequency = 400 ÷ 200 = 2 meters. The formula is v = fλ, so λ = v/f.'),
   p('What is the difference between reflection, refraction, and diffraction of waves?','Think: bounce, bend, spread',
     'Reflection: wave bounces off a surface (mirror). Refraction: wave bends when it passes into a different medium (light in water). Diffraction: wave spreads out around obstacles or through openings (sound around corners).')],
  'The Electromagnetic Spectrum',
  [p('What is electromagnetic radiation? How does it differ from mechanical waves?','Think: does it need a medium?',
     'Electromagnetic radiation is energy transmitted as oscillating electric and magnetic fields. Unlike mechanical waves, it does NOT need a medium and can travel through a vacuum at the speed of light (3×10⁸ m/s).'),
   p('List the 7 types of electromagnetic waves in order from longest to shortest wavelength.','Think: Radio, Micro, Infrared, Visible, UV, X-ray, Gamma',
     'Radio waves → Microwaves → Infrared → Visible light → Ultraviolet → X-rays → Gamma rays. As wavelength decreases, frequency and energy increase.'),
   p('Why is ultraviolet radiation harmful while visible light is generally not?','Think: energy levels and biological effects',
     'UV radiation has shorter wavelengths and higher energy than visible light, enough to break chemical bonds in DNA and damage skin cells, potentially causing mutations and cancer. Visible light has lower energy that does not damage DNA.'),
   p('Give one practical application each for: radio waves, X-rays, and microwaves.','Think: everyday uses of the EM spectrum',
     'Radio waves: broadcasting music and TV, cell phone communication. X-rays: medical imaging to see bones and detect tumors. Microwaves: cooking food (heat water molecules), satellite communication, radar.')]
);

// science[3] = Earth History & Space
PRACTICE[8].science[3] = u(
  'Earth\'s History & Geologic Time',
  [p('What is geologic time? Why do scientists need it?','Think: Earth is 4.6 billion years old',
     'Geologic time is the timescale used to describe Earth\'s history from formation (~4.6 billion years ago) to present. Scientists need it to study the sequence of rock layers, evolution of life, and major geological events over vast timescales.'),
   p('How does the law of superposition help scientists read rock layers?','Think: which layer is oldest?',
     'The law of superposition states that in undisturbed rock layers, older rocks are on the bottom and younger rocks are on top. Scientists read rock layers like pages of a history book to determine the relative age of fossils and events.'),
   p('What is a fossil? Describe two types of fossils and what they tell us about Earth\'s past.','Think: preserved remains or evidence',
     'A fossil is preserved remains or evidence of ancient life. Types: body fossils (bones, shells) preserve the organism itself; trace fossils (footprints, burrows) preserve behavior. Together they reveal past environments, evolution, and extinction events.'),
   p('What caused the mass extinction at the end of the Cretaceous period (~66 million years ago)?','Think: asteroid impact + its effects',
     'A massive asteroid (~10 km wide) struck Earth near the Yucatán Peninsula. It triggered fires, dust clouds blocking sunlight, global cooling, and collapse of food chains. About 75% of species, including non-avian dinosaurs, went extinct.')],
  'The Solar System & Universe',
  [p('Describe the order of the 8 planets from the sun. How are inner and outer planets different?','Think: rocky vs. gas giants',
     'Mercury, Venus, Earth, Mars (inner — rocky, smaller, fewer moons) | Jupiter, Saturn, Uranus, Neptune (outer — gas/ice giants, larger, many moons, ring systems). The asteroid belt separates the two groups.'),
   p('What is the difference between a star, a planet, and a moon?','Think: size, what they orbit, do they produce light',
     'Star: massive, produces energy via nuclear fusion, its own light (e.g., the Sun). Planet: orbits a star, large enough to have cleared its orbital path (e.g., Earth). Moon: natural satellite orbiting a planet, lit by reflected sunlight.'),
   p('Explain why we experience seasons and lunar phases. Are they caused by the same thing?','Think: two different phenomena',
     'Seasons: caused by Earth\'s axial tilt (23.5°) — not distance from the sun. Lunar phases: caused by the Moon\'s orbital position relative to Earth and the Sun, changing how much of the Moon\'s lit side we see. They are caused by different factors.'),
   p('What is the Big Bang theory? What evidence supports it?','Think: origin of the universe',
     'The Big Bang theory states the universe began ~13.8 billion years ago from an extremely hot, dense point and has been expanding ever since. Evidence: cosmic microwave background radiation (afterglow of the Big Bang), redshift of galaxies (universe expanding), abundance of hydrogen and helium.')]
);

// ela[1] = Reading Informational Text
PRACTICE[8].ela[1] = u(
  'Analyzing Arguments in Text',
  [p('What is a central argument? How do you distinguish it from a supporting claim?','Think: main point vs. reasons that back it up',
     'Central argument: the author\'s overall thesis or position. Supporting claims: specific reasons or sub-points that back it up. Example: Central — "School uniforms benefit students." Supporting — "They reduce bullying" and "They lower clothing costs."'),
   p('What is the difference between relevant and irrelevant evidence? Give an example.','Think: does it directly support the claim?',
     'Relevant evidence directly supports the claim. Irrelevant evidence does not connect to the argument. Example claim: "Electric cars are more eco-friendly." Relevant: "EVs emit zero tailpipe emissions." Irrelevant: "EVs can be expensive to buy."'),
   p('What are logical fallacies? Identify the fallacy in: "If we allow cellphones in school, next students will want to do whatever they want."','Think: flawed reasoning patterns',
     'Logical fallacies are errors in reasoning. This example is a slippery slope fallacy — assuming one event inevitably causes a series of increasingly extreme consequences without logical justification.'),
   p('How does an author use rhetorical appeals? Define logos, ethos, and pathos with one example each.','Think: logic, credibility, emotion',
     'Logos: appeal to logic/evidence ("Studies show 80% of students sleep less than 8 hours"). Ethos: appeal to credibility ("Dr. Smith, a neuroscientist, states..."). Pathos: appeal to emotion ("Imagine a child unable to learn because they\'re too tired").')],
  'Text Structures & Author\'s Craft',
  [p('Name five common informational text structures and explain when each is used.','Think: how is the text organized?',
     'Description: explains characteristics. Sequence/chronological: events in time order. Compare/contrast: shows similarities and differences. Cause/effect: explains why things happen. Problem/solution: states a problem and offers solutions.'),
   p('What is point of view in informational text, and how can you detect bias?','Think: who is speaking, and who benefits?',
     'Point of view is the author\'s perspective or stance. Detect bias by: checking credentials and affiliations, looking for missing perspectives, noticing emotionally charged language, and comparing with other sources on the same topic.'),
   p('How do domain-specific vocabulary and technical language function in informational text?','Think: precision vs. accessibility',
     'Domain-specific vocabulary provides precision (exact meaning). It signals expertise but can limit accessibility. Authors must balance technical accuracy with clarity for their audience, often defining terms in context.'),
   p('What is the purpose of headings, sidebars, graphs, and captions in informational text?','Think: text features serve the reader',
     'Headings organize content and help readers navigate. Sidebars provide supplementary information. Graphs visualize data for comparison. Captions explain visuals. All text features help readers locate, understand, and retain information.')]
);

// ela[2] = Writing
PRACTICE[8].ela[2] = u(
  'Research & Informational Writing',
  [p('What makes a source credible? Name four criteria for evaluating sources.','Think: CRAAP test — Currency, Relevance, Authority, Accuracy, Purpose',
     'Credible sources are: Current (recently published or updated), Relevant (directly related to your topic), Authoritative (written by an expert or reputable organization), Accurate (facts are verifiable), and Purpose is informative, not purely promotional.'),
   p('What is paraphrasing? How is it different from summarizing and quoting?','Think: restating vs. condensing vs. exact words',
     'Paraphrasing: restate a passage in your own words, similar length to original. Summarizing: condense the main ideas into a shorter version. Quoting: use the author\'s exact words in quotation marks. All three require proper citation.'),
   p('What is plagiarism? Why is it academic dishonesty even if unintentional?','Think: using someone\'s ideas without credit',
     'Plagiarism is presenting someone else\'s words or ideas as your own. Even accidental plagiarism is dishonest because it misrepresents who did the thinking. It violates academic integrity and harms the original creator.'),
   p('Write a strong thesis for this prompt: "Should homework be banned?" Use the format: [Position] because [reason 1] and [reason 2]','Think: take a clear, specific, arguable position',
     'Example: "Homework should be limited to 30 minutes per night because excessive assignments increase student anxiety and reduce time for creative, independent learning." Your thesis should be debatable and preview your main arguments.')],
  'Argumentative Writing',
  [p('What is a counterclaim? Why is addressing one important in argumentative writing?','Think: opposing view, then rebuttal',
     'A counterclaim is the opposing side\'s strongest argument. Addressing it shows you\'ve considered multiple perspectives, strengthens your credibility, and allows you to directly refute the opposition — making your argument more persuasive overall.'),
   p('What is the PEEL paragraph structure? Apply it briefly to argue that exercise improves academic performance.','Think: Point, Evidence, Explain, Link',
     'Point: "Regular exercise improves students\' academic performance." Evidence: "A Harvard study found aerobic exercise increases brain volume in areas related to memory." Explain: "Better memory leads to stronger learning and retention." Link: "Schools should therefore prioritize physical activity alongside academics."'),
   p('How does word choice (diction) affect the persuasiveness of an argument? Give an example.','Think: precision and connotation matter',
     'Word choice shapes how readers perceive an argument. "Students are struggling" is neutral. "Students are suffering under impossible workloads" is more emotionally charged and persuasive. Precise, specific language signals authority; vague language weakens credibility.'),
   p('What is the difference between a primary and secondary source? Give an example of each for a research paper about the Civil War.','Think: original vs. analysis of original',
     'Primary source: created at the time of the event (e.g., a soldier\'s diary, Lincoln\'s speeches, photographs). Secondary source: later analysis or interpretation (e.g., a history textbook, scholarly article). Primary sources provide direct evidence; secondary sources offer context and analysis.')]
);

// ela[3] = Language
PRACTICE[8].ela[3] = u(
  'Vocabulary & Word Choice',
  [p('What are affixes? Give one example of a prefix and one suffix and explain how they change a word\'s meaning.','Think: morphemes attached to root words',
     'Affixes are word parts added to roots to change meaning. Prefix example: "un-" + "happy" = "unhappy" (not happy). Suffix example: "teach" + "-er" = "teacher" (one who teaches). Learning common affixes helps decode unfamiliar words.'),
   p('What is the difference between synonyms and antonyms? Why does word choice matter even among synonyms?','Think: same meaning vs. opposite meaning; nuance matters',
     'Synonyms have similar meanings; antonyms have opposite meanings. Among synonyms, connotation differs: "slender," "thin," and "scrawny" all mean slim, but carry different emotional tones. Choosing the right synonym shapes tone and meaning precisely.'),
   p('What is a euphemism? Give an example and explain why people use them.','Think: softened language for difficult topics',
     'A euphemism is a mild or indirect expression used instead of a harsh one. Example: "passed away" instead of "died." People use them to soften difficult topics, show politeness, or avoid discomfort — but they can also obscure truth.'),
   p('The word "circumspect" comes from Latin circum (around) + specere (to look). What does it mean? Write a sentence using it correctly.','Think: look around before acting',
     '"Circumspect" means wary and cautious, considering all circumstances carefully. Example: "The new principal was circumspect in her decisions, consulting teachers and parents before making any major changes."')],
  'Grammar for Clarity & Style',
  [p('What is the difference between active and passive voice? Rewrite this in active voice: "The experiment was conducted by the students."','Think: who is doing the action?',
     'Active voice: subject performs the action ("The students conducted the experiment"). Passive voice: the subject receives the action. Active voice is usually clearer and more direct. Passive is useful when the actor is unknown or less important.'),
   p('What is a misplaced modifier? Correct this example: "Running down the street, the dog was chased by the boy."','Think: the modifier should be next to what it describes',
     'A misplaced modifier is a descriptive phrase placed too far from the word it modifies, creating confusion. Corrected: "Running down the street, the boy chased the dog." Now "running" correctly modifies "the boy."'),
   p('What is parallel structure in writing? Fix this sentence: "She likes hiking, to swim, and reading."','Think: matching grammatical forms in a series',
     'Parallel structure means using the same grammatical form for items in a series. Fixed: "She likes hiking, swimming, and reading." (all gerunds) OR "She likes to hike, swim, and read." (all infinitives).'),
   p('When should you use a semicolon? Write one example showing its correct use.','Think: connects two closely related independent clauses',
     'A semicolon joins two closely related independent clauses without a conjunction. Example: "The test was difficult; however, most students finished on time." Also used in lists with internal commas: "I visited Paris, France; Rome, Italy; and Athens, Greece."')]
);

console.log('Grade 8 ELA done');

// history[1] = The Constitution & New Nation
PRACTICE[8].history[1] = u(
  'The Constitution',
  [p('What are the three branches of the U.S. federal government and their main functions?','Think: legislative, executive, judicial',
     'Legislative (Congress): makes laws. Executive (President): enforces laws, commands military, foreign policy. Judicial (Supreme Court): interprets laws and the Constitution. Each branch has distinct powers to prevent concentration of power.'),
   p('What is the system of checks and balances? Give one example for each branch checking another.','Think: each branch limits the others',
     'Congress checks President: can override a veto with 2/3 vote. President checks Congress: can veto legislation. Supreme Court checks both: can declare laws unconstitutional (judicial review). President checks Supreme Court: nominates justices.'),
   p('What is the Bill of Rights? Name three amendments and explain each.','Think: first 10 amendments protecting individual rights',
     '1st: Freedom of speech, religion, press, assembly, petition. 4th: Protection against unreasonable searches and seizures. 6th: Right to a speedy, public trial and legal counsel. The Bill of Rights limits government power and protects individual freedoms.'),
   p('What is federalism? How does it divide power between state and federal governments?','Think: shared power, not one central authority',
     'Federalism divides power between the national and state governments. Federal powers (enumerated): declare war, coin money, regulate interstate commerce. State powers (reserved): education, local law enforcement. Concurrent powers (shared): taxation, infrastructure.')],
  'The Early Republic',
  [p('What were the major challenges facing the U.S. under the Articles of Confederation?','Think: why did it fail?',
     'No power to tax → no funding. No national army. No power to regulate trade between states. No executive or judicial branch. Each state had equal vote regardless of size. These weaknesses led to Shays\' Rebellion and the 1787 Constitutional Convention.'),
   p('What was the Louisiana Purchase and why was it significant?','Think: doubling the size of the U.S.',
     'In 1803, President Jefferson purchased ~828,000 sq miles from France for $15 million, doubling the U.S. territory. It opened vast lands for expansion westward, though it came at great cost to Native American peoples already living there.'),
   p('What was the significance of the Supreme Court case Marbury v. Madison (1803)?','Think: establishing a major judicial power',
     'Established the principle of judicial review — the Supreme Court\'s power to strike down laws it deems unconstitutional. This made the judiciary a truly co-equal branch and is one of the most important legal precedents in U.S. history.'),
   p('What was the Monroe Doctrine (1823) and why did it matter?','Think: U.S. foreign policy statement about the Western Hemisphere',
     'President Monroe declared that European powers should not colonize or interfere in the Americas, and the U.S. would stay out of European affairs. It established U.S. dominance in the Western Hemisphere and became a cornerstone of American foreign policy for over a century.')]
);

// history[2] = Expansion & Reform
PRACTICE[8].history[2] = u(
  'Westward Expansion',
  [p('What was Manifest Destiny? How did it affect Native Americans?','Think: belief in inevitable expansion + its human cost',
     'Manifest Destiny was the belief that the U.S. was divinely destined to expand across the continent to the Pacific. It led to wars, forced removal (Trail of Tears), and near-destruction of Native American cultures and populations.'),
   p('What was the Indian Removal Act (1830) and what were its consequences?','Think: forced relocation of Native peoples',
     'Signed by President Jackson, it authorized the forced relocation of Native Americans east of the Mississippi to territories west of it. The Cherokee\'s forced march became the "Trail of Tears" (1838–1839), killing thousands. It violated Supreme Court rulings and treaties.'),
   p('What was the Missouri Compromise (1820) and why was it needed?','Think: balancing slave and free states',
     'Missouri entering as a slave state threatened the balance of free and slave states in Congress. The compromise admitted Missouri (slave) and Maine (free) simultaneously, and banned slavery north of 36°30\' latitude — temporarily preventing sectional crisis.'),
   p('How did the Mexican-American War (1846–1848) change U.S. territory?','Think: Texas, California, Southwest',
     'The U.S. declared war after a border dispute with Mexico over Texas. Victory resulted in the Treaty of Guadalupe Hidalgo: Mexico ceded California, Nevada, Utah, Arizona, New Mexico, and Colorado — adding over 500,000 square miles of territory.')],
  'Reform Movements',
  [p('What was the abolitionist movement? Name two key abolitionists and their contributions.','Think: ending slavery before the Civil War',
     'Abolitionism sought to end slavery. Frederick Douglass: formerly enslaved, powerful orator and author of Narrative of the Life; edited The North Star newspaper. William Lloyd Garrison: founded The Liberator newspaper, co-founded the American Anti-Slavery Society.'),
   p('What was the Seneca Falls Convention (1848)? What did the Declaration of Sentiments demand?','Think: beginning of the women\'s rights movement',
     'The first women\'s rights convention, organized by Elizabeth Cady Stanton and Lucretia Mott. The Declaration of Sentiments (modeled on the Declaration of Independence) demanded equal rights for women, including the right to vote.'),
   p('What was the temperance movement? How did it connect to other 19th-century reform efforts?','Think: alcohol, family, social problems',
     'The temperance movement sought to reduce or eliminate alcohol consumption, which reformers linked to poverty, domestic violence, and crime. It connected to broader reform movements (women\'s rights, abolitionism) as many reformers were active in multiple causes.'),
   p('What was the Second Great Awakening and how did it fuel social reform?','Think: religious revival → moral responsibility → activism',
     'A Protestant religious revival in the early 19th century that emphasized personal salvation and moral improvement. It inspired believers to reform society — leading to the abolitionist, temperance, and education reform movements, as well as the establishment of many colleges.')]
);

// history[3] = Civil War & Reconstruction
PRACTICE[8].history[3] = u(
  'Causes & Course of the Civil War',
  [p('What were the four main causes of the Civil War?','Think: STEM — Slavery, Territorial expansion, Economic differences, Missouri/Compromise breakdown',
     'Slavery (moral and economic debate); territorial expansion (should new states allow slavery?); economic differences (industrial North vs. agricultural slave South); and the breakdown of political compromise (Kansas-Nebraska Act, Bleeding Kansas, Dred Scott decision).'),
   p('What was the significance of Lincoln\'s Emancipation Proclamation (1863)?','Think: what it did AND what it didn\'t do',
     'It declared enslaved people in Confederate states "forever free." It did NOT free slaves in border states still in the Union. Militarily, it redefined the war as a fight to end slavery, discouraged European support for the Confederacy, and allowed Black men to enlist in the Union Army.'),
   p('Why was the Battle of Gettysburg (1863) a turning point in the Civil War?','Think: the war\'s bloodiest battle; Confederate high water mark',
     'Lee\'s invasion of Pennsylvania failed with massive Confederate casualties (28,000+). Pickett\'s Charge was repulsed. Combined with the fall of Vicksburg the same day (July 4), it ended Confederate offensive capability and shifted momentum firmly to the Union.'),
   p('What roles did African Americans play in the Civil War?','Think: before and after the Emancipation Proclamation',
     'Before 1863: enslaved people sabotaged Confederate war effort, fled to Union lines. After 1863: ~180,000 Black men served in the Union Army (USCT), including the famous 54th Massachusetts Infantry. They fought for freedom and citizenship despite facing discrimination in pay and treatment.')],
  'Reconstruction Era',
  [p('What were the 13th, 14th, and 15th Amendments? Why are they called the Reconstruction Amendments?','Think: end of slavery, citizenship, voting rights',
     '13th (1865): abolished slavery. 14th (1868): granted citizenship and equal protection to all born in the U.S. 15th (1870): granted Black men the right to vote. Called Reconstruction Amendments because they reshaped U.S. society after the Civil War.'),
   p('What was "Radical Reconstruction" and why did Southern states resist it?','Think: Congressional plan vs. Presidential plan',
     'Congress imposed military rule on former Confederate states, requiring them to ratify the 14th Amendment and write new constitutions guaranteeing Black voting rights before readmission. Southern whites resisted through violence (KKK), intimidation, and eventually Black Codes and Jim Crow laws.'),
   p('What was the Freedmen\'s Bureau and what did it accomplish?','Think: transitioning from slavery to freedom',
     'A federal agency (1865–1872) that helped formerly enslaved people transition to freedom. Accomplishments: established thousands of schools (including HBCUs like Howard University), provided food and medical care, helped negotiate labor contracts, and mediated legal disputes.'),
   p('Why did Reconstruction end in 1877, and what were its long-term consequences?','Think: Compromise of 1877 + the century that followed',
     'The Compromise of 1877 resolved a disputed election: Republicans kept the White House; Union troops withdrew from the South. Without federal protection, Southern states imposed Jim Crow laws, sharecropping, poll taxes, and literacy tests — enforcing racial inequality for nearly another century until the Civil Rights Movement.')]
);

// cs[1] = Web Design Basics
PRACTICE[8].cs[1] = u(
  'HTML & CSS Fundamentals',
  [p('What is the difference between HTML and CSS? What does each do?','Think: structure vs. style',
     'HTML (HyperText Markup Language) defines the structure and content of a webpage (headings, paragraphs, links, images). CSS (Cascading Style Sheets) controls the visual appearance (colors, fonts, layout, spacing). HTML is the skeleton; CSS is the clothing.'),
   p('What is a CSS selector? Write a rule that makes all <h1> tags blue and 24px in size.','Think: target the element, then apply styles',
     'A selector targets HTML elements to apply styles. Example: h1 { color: blue; font-size: 24px; } The selector "h1" targets all heading-1 elements; inside the curly braces are property-value pairs.'),
   p('What is the CSS box model? Name its four components.','Think: content, padding, border, margin',
     'Every HTML element is a box: Content (actual text/image), Padding (space between content and border), Border (the line around the element), Margin (space outside the border separating it from other elements). Total width = content + padding + border + margin.'),
   p('What is the difference between a class and an ID in HTML/CSS? When would you use each?','Think: reusable vs. unique',
     'Class (.classname): can be applied to multiple elements; used for shared styles. ID (#idname): must be unique on a page; used for a specific single element. Use classes for repeated styling patterns; use IDs for page navigation anchors or unique elements like a logo.')],
  'Web Design Principles & Accessibility',
  [p('What are the three core principles of good web design?','Think: usability, aesthetics, accessibility',
     'Usability: easy to navigate and find information. Aesthetics: visually appealing and consistent design (color, typography, whitespace). Accessibility: usable by people with disabilities (screen readers, keyboard navigation, sufficient color contrast, alt text for images).'),
   p('What is responsive web design? Why is it important?','Think: works on all screen sizes',
     'Responsive web design means a webpage adapts its layout to different screen sizes (desktop, tablet, mobile). Important because over 60% of web traffic is on mobile devices. CSS techniques include flexible grids, media queries, and flexible images.'),
   p('What is semantic HTML? Give two examples of semantic vs. non-semantic elements.','Think: meaningful tags vs. generic containers',
     'Semantic HTML uses tags that describe their content\'s meaning. Semantic: <header>, <nav>, <article>, <footer>, <section>. Non-semantic: <div>, <span> (generic containers with no inherent meaning). Semantic HTML improves accessibility and SEO.'),
   p('What should every image on a webpage include, and why?','Think: alt attribute and accessibility',
     'Every <img> tag should include an alt attribute: <img src="dog.jpg" alt="A golden retriever puppy sitting in the grass">. It describes the image for screen reader users (visually impaired) and displays as text if the image fails to load. Omitting alt text is a common accessibility failure.')]
);

console.log('Grade 8 history/CS done');

// ── GRADE 9 ──
// math[5] = Exponential & Radical Functions
PRACTICE[9].math[5] = u(
  'Exponential Growth & Decay',
  [p('What is an exponential function? Write the general form and identify each part.','Think: y = a·bˣ',
     'y = a·bˣ. a = initial value (y-intercept), b = base/growth factor (b > 1 = growth, 0 < b < 1 = decay), x = exponent (usually time). Example: y = 500·(1.06)ˣ models money growing at 6% per year from $500.'),
   p('A population of 2,000 bacteria doubles every 3 hours. Write an equation and find the population after 12 hours.','Think: doubling = b=2; time period in exponent',
     'P = 2000 · 2^(t/3). At t = 12: P = 2000 · 2^(12/3) = 2000 · 2⁴ = 2000 · 16 = 32,000 bacteria.'),
   p('A car worth $25,000 depreciates at 15% per year. Write the equation and find its value after 4 years.','Think: decay — subtract the rate from 1',
     'V = 25000 · (1 − 0.15)^t = 25000 · (0.85)⁴ = 25000 · 0.522 ≈ $13,050 after 4 years.'),
   p('What is the difference between linear and exponential growth? Give a real-world example of each.','Think: constant rate vs. percent rate',
     'Linear: grows by the same AMOUNT each period (e.g., saving $200/month → +$200, +$200...). Exponential: grows by the same PERCENT each period (e.g., investment growing 8% annually → multiplies repeatedly). Exponential growth eventually far outpaces linear.')],
  'Radical Expressions & Equations',
  [p('Simplify: √72. Show each step.','Think: factor out perfect squares',
     '√72 = √(36 · 2) = √36 · √2 = 6√2. Factor out the largest perfect square (36) from 72, then simplify each radical.'),
   p('Solve: √(2x + 5) = 7. Check your answer.','Think: isolate the radical, then square both sides',
     'Square both sides: 2x + 5 = 49. Subtract 5: 2x = 44. Divide by 2: x = 22. Check: √(2·22 + 5) = √49 = 7 ✓'),
   p('Simplify: ∛(27x⁶). Show steps.','Think: cube root of coefficient and cube root of variable',
     '∛27 = 3 (since 3³ = 27). ∛(x⁶) = x^(6/3) = x². Answer: 3x².'),
   p('What is an extraneous solution? Solve √(x+3) = x−1 and identify any extraneous solutions.','Think: check all solutions back in original',
     'Square both sides: x+3 = (x−1)² = x²−2x+1. Rearrange: x²−3x−2 = 0... wait: x²−3x−2+0... Let me redo: x+3 = x²−2x+1 → x²−3x−2=0. Using quadratic formula or factoring: x²−3x−2=0, discriminant = 9+8=17, x=(3±√17)/2. Check x=(3+√17)/2 ≈ 3.56: √(3.56+3)≈2.56, 3.56−1=2.56 ✓. Check x=(3−√17)/2 ≈ −0.56: √(−0.56+3)=√2.44≈1.56, −0.56−1=−1.56 ✗. x≈−0.56 is extraneous (negative result for right side). An extraneous solution arises from squaring and doesn\'t satisfy the original equation.')]
);

// science[2] = Evolution
PRACTICE[9].science[2] = u(
  'Natural Selection & Adaptation',
  [p('What are Darwin\'s four conditions required for natural selection to occur?','Think: variation, inheritance, selection pressure, differential reproduction',
     'Variation: individuals differ in traits. Heredity: traits are inherited by offspring. Selection pressure: environment favors some traits over others. Differential reproduction: individuals with favorable traits survive and reproduce more. All four must be present.'),
   p('What is an adaptation? Give one structural and one behavioral adaptation and explain how each helps survival.','Think: inherited trait that increases fitness',
     'Structural: polar bear\'s white fur — camouflage in snow helps it hunt prey. Behavioral: birds migrating south in winter — avoids cold temperatures and food scarcity. Both increase the organism\'s fitness (survival and reproductive success).'),
   p('Explain the peppered moth example of natural selection.','Think: industrial melanism — environment changed, so did the population',
     'Before industrialization: light-colored moths blended with light tree bark; dark moths were eaten by birds. After: soot darkened trees; dark moths survived, light moths were eaten. Dark moths increased in population — demonstrating natural selection in real time.'),
   p('What is the difference between artificial selection and natural selection?','Think: who does the selecting?',
     'Natural selection: the environment selects which traits survive. Artificial selection: humans deliberately select traits by breeding animals/plants with desired characteristics. Examples: dog breeds (humans), antibiotic-resistant bacteria (natural selection by antibiotics).')],
  'Evidence of Evolution',
  [p('What are four types of evidence scientists use to support evolution?','Think: fossils, anatomy, genetics, biogeography',
     '(1) Fossil record: shows change in organisms over time. (2) Comparative anatomy: homologous structures (same bones, different species) show common ancestry. (3) Molecular biology: DNA similarities between species. (4) Biogeography: related species found near each other geographically.'),
   p('What are homologous structures? Give one example and explain what they tell us.','Think: same structure, different function = common ancestor',
     'Homologous structures have the same underlying anatomy but different functions, suggesting common ancestry. Example: human arm, whale flipper, bat wing, and dog foreleg all have the same bone structure (humerus, radius, ulna, carpals) adapted for different uses.'),
   p('What is the role of mutations in evolution?','Think: source of new genetic variation',
     'Mutations are random changes in DNA. Most are neutral or harmful, but some may provide a survival advantage in certain environments. Beneficial mutations that increase fitness can spread through a population over generations via natural selection.'),
   p('What is speciation? Describe one way it can occur.','Think: one species becoming two',
     'Speciation is the process by which one species splits into two or more species. Geographic (allopatric) speciation: a population is physically separated (by a mountain range or ocean). The two groups evolve independently until they can no longer interbreed — they become distinct species.')]
);

// science[3] = Ecology
PRACTICE[9].science[3] = u(
  'Ecosystems & Energy Flow',
  [p('What is the difference between a food chain and a food web?','Think: linear vs. network of feeding relationships',
     'Food chain: a single linear sequence of who eats whom (grass→grasshopper→frog→snake→hawk). Food web: a complex network of interconnected food chains showing all feeding relationships in an ecosystem. Food webs are more accurate representations of real ecosystems.'),
   p('What is the 10% rule in energy transfer? What happens to the other 90%?','Think: trophic levels and energy loss',
     'Only ~10% of energy is transferred from one trophic level to the next. The other 90% is lost as heat (cellular respiration), used by the organism for its own functions, or not consumed. This limits the number of trophic levels and explains why there are fewer apex predators.'),
   p('What are producers, consumers, and decomposers? Give an example of each.','Think: the ecological roles in an ecosystem',
     'Producer: makes its own food via photosynthesis (e.g., grass, algae). Consumer: eats other organisms — herbivore (deer), carnivore (lion), omnivore (bear). Decomposer: breaks down dead organic matter, returning nutrients to soil (e.g., fungi, bacteria).'),
   p('What is the difference between a biotic and abiotic factor? Give two examples of each.','Think: living vs. nonliving components of an ecosystem',
     'Biotic (living): plants, animals, bacteria, fungi. Abiotic (nonliving): temperature, sunlight, water, soil type, wind, pH. Both interact to shape an ecosystem. Abiotic factors determine what biotic factors can survive in an area.')],
  'Biodiversity & Human Impact',
  [p('What is biodiversity? Why is it important to ecosystems?','Think: variety of life = ecosystem resilience',
     'Biodiversity is the variety of life in an area — diversity of genes, species, and ecosystems. Important because: high biodiversity increases ecosystem stability and resilience, provides resources (food, medicine), maintains clean air/water, and supports ecosystem services humans rely on.'),
   p('What is a keystone species? Give one example and explain its effect on the ecosystem.','Think: disproportionate impact relative to abundance',
     'A keystone species has a disproportionately large impact on its ecosystem. Example: sea otters eat sea urchins; without otters, urchins overgraze kelp forests, collapsing the entire ecosystem. Removing a keystone species triggers cascading effects.'),
   p('What are three major human impacts on ecosystems?','Think: habitat destruction, pollution, climate change',
     'Habitat destruction: deforestation, urbanization eliminate species\' homes. Pollution: chemical runoff, plastic waste harm organisms and water quality. Climate change: rising temperatures shift habitats, alter migration patterns, cause coral bleaching. Invasive species and overexploitation are also major threats.'),
   p('What is the difference between conservation and preservation? Give an example of each.','Think: use wisely vs. protect entirely',
     'Conservation: managed, sustainable use of natural resources (e.g., sustainable forestry, regulated fishing). Preservation: protecting nature from human use entirely (e.g., wilderness areas, national parks with no resource extraction). Both aim to protect nature but differ in whether human use is allowed.')]
);

console.log('Grade 9 science done');

// Grade 9 ELA
PRACTICE[9].ela[1] = u(
  'Research Skills & Source Evaluation',
  [p('What is a research question? How does it differ from a topic?','Think: topic is broad; research question is focused and arguable',
     'A topic is general ("climate change"). A research question is specific and investigable ("How has climate change affected coral reef biodiversity in the past 30 years?"). A good research question is focused, complex enough to require research, and not answerable with a simple yes/no.'),
   p('What is the CRAAP test? Apply it to evaluate a blog post about COVID vaccines written by an anonymous author in 2019.','Think: Currency, Relevance, Authority, Accuracy, Purpose',
     'Currency: 2019 pre-dates COVID vaccines (not current). Relevance: depends on your topic. Authority: anonymous = no authority. Accuracy: cannot verify. Purpose: unknown, possibly misleading. Verdict: FAIL — do not use this source.'),
   p('What is the difference between a primary, secondary, and tertiary source? Give one example of each for a history paper on WWI.','Think: original vs. analysis vs. reference',
     'Primary: created at the time (soldier\'s diary, government orders, photographs). Secondary: later analysis (history textbook, scholarly article). Tertiary: compiled reference (encyclopedia, Wikipedia). In research papers, use primary and secondary sources; tertiary sources help orient initial research.'),
   p('What is an annotated bibliography? What does each annotation typically include?','Think: more than just a citation',
     'An annotated bibliography lists sources with a brief paragraph for each. Each annotation includes: a summary (what the source argues), an evaluation (credibility and quality), and a reflection (how it connects to your research question). It demonstrates that you\'ve read and understood your sources.')]  ,
  'Informational & Explanatory Writing',
  [p('What is the difference between an explanatory and an argumentative essay?','Think: explain vs. persuade',
     'Explanatory: objectively explains, analyzes, or informs without taking a side (e.g., "How does photosynthesis work?"). Argumentative: takes a clear position and uses evidence to persuade (e.g., "Solar energy should replace fossil fuels"). Explanatory uses neutral tone; argumentative is persuasive.'),
   p('What makes a strong introductory paragraph in an informational essay?','Think: hook, context, thesis',
     'Hook: engages the reader (startling fact, question, anecdote). Context: provides necessary background. Thesis: states the specific focus or central idea. A strong intro tells the reader WHAT you will explain and WHY it matters.'),
   p('What is synthesis in research writing? How is it different from summarizing?','Think: weaving multiple sources together',
     'Summarizing restates one source\'s ideas. Synthesis combines ideas from multiple sources to build your own insight. Example: Sources A and B both show economic inequality; Source C shows educational gaps — you synthesize to argue these are interconnected. Synthesis shows critical thinking.'),
   p('What are in-text citations and why are they required in research papers?','Think: giving credit within the text',
     'In-text citations identify which source a piece of information came from, placed directly after the borrowed material. They prevent plagiarism, allow readers to verify information, and give credit to original authors. Format varies: MLA uses author-page (Smith 45); APA uses author-year (Smith, 2019).')]
);

PRACTICE[9].ela[2] = u(
  'Building Arguments',
  [p('What is the Toulmin model of argument? Name all six components.','Think: claim, grounds, warrant, backing, qualifier, rebuttal',
     'Claim: your position. Grounds: evidence/data. Warrant: logic connecting evidence to claim. Backing: support for the warrant. Qualifier: limits to your claim ("in most cases"). Rebuttal: addressing counterarguments. Toulmin model creates a rigorous, complete argument structure.'),
   p('What is the difference between an ethical (moral), practical, and logical argument? Give an example of each for the topic of capital punishment.','Think: three angles on the same issue',
     'Ethical: "Capital punishment violates the inherent dignity of human life." Practical: "Capital punishment costs more than life imprisonment." Logical: "Since innocent people have been executed, capital punishment creates irreversible injustice." Each uses a different type of reasoning.'),
   p('Why is evidence quality crucial in argumentative writing? Rank these from most to least credible: Wikipedia article, peer-reviewed study, news article, personal anecdote.','Think: how was the information verified?',
     'Most credible: peer-reviewed study (expert-reviewed, methodology scrutinized) → news article (professional journalism, editorial standards) → Wikipedia (crowd-sourced, can be edited by anyone, but has citations) → personal anecdote (subjective, not generalizable). Use peer-reviewed research when possible.'),
   p('What is a logical fallacy? Identify the fallacy: "Everyone is buying this supplement, so it must work."','Think: why reasoning fails here',
     'A logical fallacy is flawed reasoning. This is an ad populum (appeal to popularity) fallacy — something is not true merely because many people believe it. Effective arguments are built on verifiable evidence and sound logic, not popularity.')]  ,
  'Counterargument & Rebuttal',
  [p('Why is addressing counterarguments a strength, not a weakness, in argumentative writing?','Think: credibility and thoroughness',
     'Acknowledging counterarguments demonstrates intellectual honesty, builds credibility (ethos), and shows the writer has considered multiple perspectives. It also preemptively answers objections readers might have, making the argument more persuasive and harder to refute.'),
   p('What is the difference between refuting and conceding a counterargument? Give an example of each.','Think: fully reject vs. partially acknowledge',
     'Refute: completely disprove ("While some argue vaccines cause autism, this claim was debunked — the original study was retracted for fraud"). Concede: partially acknowledge truth, then redirect ("Admittedly, solar panels have high upfront costs; however, they save money over a 25-year lifespan").'),
   p('What is a straw man fallacy? How can you avoid it when addressing counterarguments?','Think: misrepresenting the opposing side',
     'A straw man fallacy misrepresents the opponent\'s argument to make it easier to attack. Avoid it by researching and representing the strongest version of the opposing argument (steelmanning). Only then refute it to show your position holds up against the best counterarguments.'),
   p('Rewrite this weak rebuttal to make it stronger: "Some people think social media is bad, but they\'re wrong."','Think: acknowledge, then refute with evidence',
     'Stronger: "While critics argue that social media harms teen mental health, a 2023 meta-analysis in JAMA found that the effect is small and depends heavily on how social media is used — passive scrolling is linked to depression, but active, social use shows neutral or positive effects."')]
);

PRACTICE[9].ela[3] = u(
  'Academic Vocabulary Strategies',
  [p('What is a morpheme? How does breaking words into morphemes help with vocabulary?','Think: smallest unit of meaning',
     'A morpheme is the smallest unit of meaning in language. "Unhappiness" has three: un- (not) + happy (content) + -ness (state of). Breaking words into root, prefix, and suffix helps decode unfamiliar words by understanding their components.'),
   p('The word "omnivorous" comes from Latin omnis (all) + vorare (to eat). Define it and identify a related word using the same root.','Think: what do the parts mean?',
     '"Omnivorous" means eating both plant and animal food. Related words: "voracious" (consuming large amounts), "carnivorous" (meat-eating), "herbivorous" (plant-eating) — all share the Latin root vorare.'),
   p('What is the difference between connotation and denotation? Give two words with the same denotation but different connotations.','Think: dictionary meaning vs. emotional meaning',
     'Denotation: literal, dictionary definition. Connotation: emotional or cultural associations. Example: "politician" (neutral denotation) vs. "statesman" (positive connotation) — both refer to a political figure but carry different feelings.'),
   p('What strategies can you use when you encounter an unknown word in a text? Name three.','Think: context clues, word parts, reference tools',
     '(1) Context clues: look at surrounding sentences for definition, contrast, or example clues. (2) Word parts: break into prefix, root, suffix. (3) Reference: use a dictionary or glossary. Try strategies in order — context first, then word parts, then look it up.')]  ,
  'Figurative Language & Connotation',
  [p('Define metaphor, simile, and personification. Give an original example of each.','Think: comparisons and human-like qualities',
     'Simile: comparison using "like" or "as" ("Her voice was like velvet"). Metaphor: direct comparison ("The classroom was a battlefield"). Personification: giving human traits to non-human things ("The wind whispered through the trees"). Each creates vivid imagery.'),
   p('What is irony? Distinguish between verbal, situational, and dramatic irony with an example of each.','Think: the gap between what is and what seems',
     'Verbal: saying the opposite of what you mean ("Oh great, another Monday"). Situational: outcome is opposite of what\'s expected (a fire station burns down). Dramatic: audience knows something characters don\'t (we know the killer is in the house; the character does not).'),
   p('What is allusion? Give an example of a literary allusion and explain its effect.','Think: reference to a well-known person, event, or text',
     'An allusion is an indirect reference to something outside the text. Example: "This classroom is my Waterloo" alludes to Napoleon\'s decisive defeat — implying the speaker is overwhelmed and about to fail. Allusions add depth and connect to shared cultural knowledge.'),
   p('A poet writes: "Hope is the thing with feathers / That perches in the soul." What device is this, and what does it suggest about hope?','Think: Emily Dickinson — what animal does hope resemble?',
     'This is an extended metaphor (also personification). Hope is compared to a bird: fragile yet persistent, ever-present within us, capable of lifting our spirits (feathers = flight = elevation). The sustained comparison across multiple lines creates a rich emotional image.')]
);

// Grade 9 History
PRACTICE[9].history[1] = u(
  'Economic Systems & Global Trade',
  [p('What are the four main types of economic systems? Briefly describe each.','Think: who controls the economy?',
     'Traditional: based on customs/habits (subsistence farming). Command: government controls production and distribution (North Korea, Cuba). Market: supply and demand; private ownership (U.S.). Mixed: blend of market and government involvement (most modern economies).'),
   p('What is comparative advantage? How does it explain international trade?','Think: produce what you\'re relatively better at',
     'Comparative advantage means a country should produce goods at which it has the lowest opportunity cost. Even if one country is better at everything, both benefit from trade by specializing. Example: Country A makes cars efficiently; Country B makes electronics efficiently — both benefit from trading.'),
   p('What is the difference between imports and exports? How do they affect a country\'s GDP and trade balance?','Think: buying vs. selling internationally',
     'Exports: goods/services sold to other countries (adds to GDP). Imports: goods/services bought from other countries (subtracts from GDP). Trade surplus: exports > imports. Trade deficit: imports > exports. GDP = C + I + G + (X - M) where X=exports, M=imports.'),
   p('What is globalization? Name one benefit and one drawback.','Think: interconnected world economy',
     'Globalization: increasing economic, cultural, and political integration across countries. Benefit: lower prices for consumers, more jobs in developing nations, cultural exchange. Drawback: job loss in developed nations (outsourcing), exploitation of cheap labor, environmental damage from increased production.')]  ,
  'Government & Political Systems',
  [p('What is the difference between a democracy, an oligarchy, and an autocracy?','Think: who holds power?',
     'Democracy: power held by the people through elections (direct or representative). Oligarchy: power held by a small, privileged group (military, wealthy elite). Autocracy: power held by a single individual with unlimited authority (dictatorship, absolute monarchy). Most modern governments are mixed systems.'),
   p('What are civil liberties vs. civil rights? Give one example of each.','Think: freedom from government vs. equal treatment under law',
     'Civil liberties: freedoms protecting individuals FROM government interference (freedom of speech, religion, privacy). Civil rights: rights ensuring EQUAL treatment regardless of race, gender, religion (voting rights, equal access to public accommodations). Civil liberties = negative rights; civil rights = positive protections.'),
   p('What is the rule of law? Why is it fundamental to democracy?','Think: no one is above the law',
     'The rule of law means everyone — including government officials — is subject to the law. It prevents arbitrary use of power, ensures equal justice, and protects individual rights. Without it, governments can abuse citizens without legal accountability.'),
   p('What is the difference between federal, unitary, and confederal systems of government?','Think: where does power rest?',
     'Federal: power divided between national and state/regional governments (U.S., Germany). Unitary: power concentrated in central government; local units are subordinate (France, UK). Confederal: loose association of sovereign states; central authority is weak (early U.S. under Articles of Confederation).')]
);

console.log('Grade 9 ELA/History done');

// ── GRADE 10 ──
// math[4] = Probability & Statistics
PRACTICE[10].math[4] = u(
  'Probability Fundamentals',
  [p('What is the difference between theoretical and experimental probability? Give an example of each for flipping a coin.','Think: expected vs. actual results',
     'Theoretical: based on logic — P(heads) = 1/2 = 0.5. Experimental: based on actual trials — flip 100 times, get 47 heads → P(heads) = 47/100 = 0.47. As the number of trials increases, experimental probability approaches theoretical probability (Law of Large Numbers).'),
   p('A bag has 4 red, 3 blue, 2 green marbles. Find P(red), P(blue or green), and P(not red).','Think: favorable outcomes ÷ total outcomes',
     'Total = 9. P(red) = 4/9. P(blue or green) = (3+2)/9 = 5/9. P(not red) = 5/9. Note: P(not red) = 1 − P(red) = 1 − 4/9 = 5/9. These events are complementary.'),
   p('What is the difference between independent and dependent events? Give an example of each.','Think: does the first draw affect the second?',
     'Independent: first event does not affect second (flipping a coin twice — each flip is independent). Dependent: first event changes the probability of the second (drawing cards without replacement — removing one card changes the deck).'),
   p('A card is drawn from a standard deck. What is P(red card AND a face card)?','Think: multiply probabilities for AND; add for OR',
     '26 red cards in a 52-card deck. 6 red face cards (J, Q, K of hearts and diamonds). P(red AND face) = 6/52 = 3/26 ≈ 0.115. Alternatively: P(red) × P(face | red) = 26/52 × 6/26 = 6/52 = 3/26.')]  ,
  'Statistics & Data Analysis',
  [p('What is the difference between mean, median, and mode? When is each most useful?','Think: which measure best represents the data?',
     'Mean: average — best for symmetric distributions without outliers. Median: middle value — best when data has outliers (e.g., median income). Mode: most frequent value — best for categorical data (most popular shoe size). Outliers skew the mean but not the median.'),
   p('A dataset: 12, 15, 15, 18, 20, 95. How does the outlier (95) affect mean vs. median?','Think: calculate both and compare',
     'Without 95: mean = 16, median = 16.5. With 95: mean = (12+15+15+18+20+95)/6 = 175/6 ≈ 29.2, median = (15+18)/2 = 16.5. The mean jumps dramatically; the median is nearly unchanged. This shows why median better represents skewed data.'),
   p('What is standard deviation? What does a higher standard deviation tell you about a dataset?','Think: how spread out the data is around the mean',
     'Standard deviation measures how spread out values are from the mean. Low SD: values are clustered close to the mean (consistent). High SD: values are widely spread (variable). Example: test scores of 70, 71, 70, 69 have low SD; scores of 30, 55, 80, 95 have high SD.'),
   p('A scatterplot shows a strong positive correlation between hours studied and test scores. Does this mean studying causes higher scores? Explain.','Think: correlation ≠ causation',
     'Not necessarily. Correlation means the two variables tend to change together. Causation means one directly causes the other. A third variable (e.g., student motivation) could cause both. To establish causation, a controlled experiment is needed, not just correlation.')]
);

// Grade 10 science[2] = Solutions & Thermochemistry
PRACTICE[10].science[2] = u(
  'Solutions & Concentration',
  [p('What is a solution? What are the solute and solvent? Give an example.','Think: what dissolves in what?',
     'A solution is a homogeneous mixture where one substance (solute) dissolves in another (solvent). Example: salt water — salt (solute) dissolves in water (solvent). Water is called the "universal solvent" because it dissolves more substances than any other liquid.'),
   p('What is molarity (M)? A chemist dissolves 58.5g of NaCl (molar mass = 58.5 g/mol) in water to make 500mL of solution. What is the molarity?','Think: moles of solute ÷ liters of solution',
     'Molarity = moles of solute / liters of solution. Moles NaCl = 58.5g ÷ 58.5 g/mol = 1 mol. Volume = 500 mL = 0.5 L. M = 1 mol / 0.5 L = 2 M (2 molar).'),
   p('How do temperature and pressure affect the solubility of solids and gases in water?','Think: fizzy drinks go flat when warm',
     'For most solids: solubility increases with temperature (more dissolves when hot). For gases: solubility decreases with temperature (CO₂ escapes faster from warm soda) and increases with pressure (soda carbonated under pressure). This is why deep-sea fish die when brought to the surface.'),
   p('What is the difference between a dilute, concentrated, saturated, and supersaturated solution?','Think: how much solute can dissolve?',
     'Dilute: small amount of solute relative to solvent. Concentrated: large amount of solute. Saturated: maximum amount of solute dissolved at that temperature — no more can dissolve. Supersaturated: contains more solute than normally possible (unstable — excess crystallizes with disturbance).')]  ,
  'Thermochemistry & Energy in Reactions',
  [p('What is the difference between exothermic and endothermic reactions? Give one example of each.','Think: heat released vs. heat absorbed',
     'Exothermic: releases heat energy (ΔH < 0) — combustion, hand warmers, neutralization reactions. Endothermic: absorbs heat (ΔH > 0) — photosynthesis, ice packs, cooking. In exothermic reactions, products have less energy than reactants; in endothermic, products have more.'),
   p('What is Hess\'s Law? Why is it useful?','Think: enthalpy changes add up regardless of path',
     'Hess\'s Law states that the total enthalpy change for a reaction is the same regardless of the pathway taken. Useful because we can calculate ΔH for reactions that can\'t be measured directly by adding together enthalpy changes of individual steps.'),
   p('A reaction releases 450 J of heat when 0.05 mol of substance reacts. What is the molar enthalpy change (ΔH)?','Think: J per mol',
     'ΔH = heat released / moles = −450 J / 0.05 mol = −9,000 J/mol = −9 kJ/mol. Negative because heat is released (exothermic). The molar enthalpy tells you energy per mole of reaction.'),
   p('What is specific heat capacity? Why does water have such a high specific heat capacity and why does it matter?','Think: how much heat per gram per degree',
     'Specific heat capacity is the energy needed to raise 1g of a substance by 1°C. Water\'s is 4.18 J/(g·°C) — one of the highest. This matters because: water moderates Earth\'s climate (oceans absorb and release heat slowly), regulates body temperature, and makes water useful for cooling systems.')]
);

// Grade 10 science[3] = Nuclear Chemistry
PRACTICE[10].science[3] = u(
  'Radioactivity & Nuclear Decay',
  [p('What is radioactivity? What causes an atom to be radioactive?','Think: unstable nuclei seeking stability',
     'Radioactivity is the spontaneous emission of particles or energy from an unstable atomic nucleus. Atoms are radioactive when their nucleus has too many protons or neutrons — the nucleus releases particles/energy to reach a stable configuration.'),
   p('Compare alpha, beta, and gamma radiation in terms of particle, charge, penetrating power, and shielding required.','Think: three types, very different properties',
     'Alpha (α): helium nucleus (2p, 2n), +2 charge, low penetration — stopped by paper or skin. Beta (β): electron (or positron), −1/+1 charge, medium penetration — stopped by aluminum foil. Gamma (γ): high-energy photon, no charge, high penetration — stopped by lead or thick concrete.'),
   p('What is half-life? A sample of carbon-14 (half-life = 5,730 years) starts with 200g. How much remains after 17,190 years?','Think: how many half-lives have passed?',
     '17,190 ÷ 5,730 = 3 half-lives. After each half-life, the amount halves: 200 → 100 → 50 → 25g. After 3 half-lives, 25g of C-14 remains.'),
   p('What is radioactive dating and how is it used to determine the age of materials?','Think: using known half-lives as a clock',
     'Radioactive dating compares the current ratio of a radioactive isotope to its decay product against the known half-life. Carbon-14 dating works for organisms up to ~50,000 years. Uranium-lead dating works for rocks billions of years old. Each isotope\'s half-life determines which materials it can date.')]  ,
  'Nuclear Reactions & Applications',
  [p('What is the difference between nuclear fission and nuclear fusion?','Think: splitting vs. combining nuclei',
     'Fission: a heavy nucleus (U-235, Pu-239) splits into smaller nuclei, releasing enormous energy. Used in nuclear power plants and atomic bombs. Fusion: light nuclei (hydrogen isotopes) combine to form a heavier nucleus, releasing even more energy. Powers the sun; still being developed for energy use on Earth.'),
   p('How do nuclear power plants generate electricity? What is the role of a chain reaction?','Think: controlled fission → heat → steam → turbine',
     'Fission releases heat, which boils water into steam, driving turbines that generate electricity. A chain reaction occurs when each fission releases neutrons that trigger more fissions. Control rods (graphite, boron) absorb neutrons to keep the reaction controlled. If uncontrolled → meltdown.'),
   p('What are the benefits and risks of nuclear energy compared to fossil fuels?','Think: no CO₂ vs. radioactive waste',
     'Benefits: low CO₂ emissions, high energy density, reliable baseload power. Risks: radioactive waste (remains dangerous for thousands of years), rare but catastrophic accidents (Chernobyl, Fukushima), high construction cost, uranium mining impacts. Nuclear produces ~10% of world electricity.'),
   p('What is nuclear medicine? Give two specific examples of how radioactive isotopes are used in healthcare.','Think: diagnostics and treatment',
     '(1) PET scans: patients ingest radioactive glucose (F-18); cancer cells absorb more → visible as bright spots on scan. (2) Radiation therapy: targeted gamma/X-ray beams destroy cancer cells. (3) Iodine-131: treats thyroid cancer — thyroid absorbs iodine, radiation destroys cancer cells.')]
);

console.log('Grade 10 done so far');

// Grade 10 ELA[1] = Literary Analysis
PRACTICE[10].ela[1] = u(
  'Analyzing Theme & Character',
  [p('What is a theme? How is it different from the subject or topic of a text?','Think: what the author is saying ABOUT the topic',
     'Subject/topic: what the text is about ("war"). Theme: the deeper message or insight about that topic ("War destroys the innocence of those who fight in it"). Themes are stated as complete ideas, not single words. A text can have multiple themes.'),
   p('What is a dynamic character vs. a static character? Give an example of each from literature you know.','Think: do they change over the course of the story?',
     'Dynamic: undergoes significant change in personality, beliefs, or values (e.g., Ebenezer Scrooge in A Christmas Carol — transforms from miser to generous). Static: remains essentially the same (e.g., a mentor figure who is wise and stable throughout). Both serve important narrative purposes.'),
   p('Analyze how conflict drives character development. Use a specific example.','Think: external vs. internal conflict → change in character',
     'External conflict (character vs. nature/society) and internal conflict (character vs. self) force characters to make choices that reveal and change them. Example: In The Hunger Games, Katniss\'s internal conflict (survival vs. humanity) and external conflict (Capitol vs. districts) transforms her from survivor to symbol of rebellion.'),
   p('What is irony in literature? Describe how situational irony can reinforce a theme.','Think: the gap between expectation and reality serves the author\'s message',
     'Situational irony occurs when what happens is the opposite of what was expected. Example: In "The Gift of the Magi," each spouse sacrifices their most prized possession to buy a gift for the other — making the gifts useless. This reinforces the theme that true love is about sacrifice, not material gifts.')]  ,
  'Literary Devices & Textual Analysis',
  [p('What is symbolism? Identify a common symbol in literature and explain its typical meaning.','Think: objects/characters/settings that represent larger ideas',
     'Symbolism is when an object/person/place represents something beyond its literal meaning. Common examples: the green light in The Great Gatsby = Gatsby\'s dreams and the unattainable American Dream. A dove = peace. Darkness = evil or ignorance. Light = knowledge or hope.'),
   p('What is a foil character? How does using a foil help readers understand the protagonist?','Think: contrasting characters highlight each other\'s traits',
     'A foil is a character whose traits contrast sharply with the protagonist\'s, highlighting the protagonist\'s qualities by comparison. Example: Hermione (rule-following, studious) is a foil to Fred and George (rule-breaking, comedic) — making each character\'s traits more pronounced.'),
   p('What is the difference between first-person, third-person limited, and third-person omniscient narration? How does point of view affect the reader\'s experience?','Think: who is telling the story, and what do they know?',
     'First-person: narrator is a character ("I") — intimate but limited and potentially unreliable. Third limited: follows one character\'s perspective but uses "he/she/they" — some distance. Omniscient: all-knowing narrator can access all characters\' thoughts — broader but less intimate. Each shapes what readers know and trust.'),
   p('What is "close reading"? What specific elements do you analyze when you close read a passage?','Think: careful, detailed analysis of the text itself',
     'Close reading is carefully analyzing a short passage for meaning, structure, and technique. Elements: word choice (diction), sentence structure (syntax), imagery, figurative language, tone, rhythm, shifts in mood, patterns, and ambiguity. The goal is to understand HOW the text creates meaning, not just WHAT it says.')]
);

// Grade 10 ELA[2] = Composition
PRACTICE[10].ela[2] = u(
  'Expository & Analytical Writing',
  [p('What is an analytical essay? How does it differ from a summary?','Think: interpret and argue vs. retell',
     'An analytical essay interprets and makes an argument about a text — explaining HOW and WHY something works, not just WHAT happened. A summary retells content. Example: summary = "Hamlet hesitates to kill Claudius." Analysis = "Hamlet\'s hesitation reveals his paralysis when faced with moral complexity."'),
   p('What is a topic sentence? Write a strong topic sentence for a body paragraph about symbolism in Lord of the Flies.','Think: mini-thesis for one paragraph',
     'A topic sentence states the paragraph\'s central claim and connects to the thesis. Example: "Golding uses the conch shell as a symbol of democratic order, contrasting its gradual destruction with the boys\' descent into savagery." Every sentence in the paragraph should support this claim.'),
   p('What does it mean to "embed" a quotation? Rewrite this awkward quote: "In chapter 3, "The beast is real" is said."','Think: integrate the quote naturally into your sentence',
     'Embedding means integrating a quotation smoothly into your own sentence. Rewritten: "When Ralph warns that \'the beast is real,\' Golding signals the psychological terror that will consume the group." The quote flows within the sentence and is followed by analysis.'),
   p('What is the ICE method for using evidence in academic writing?','Think: Introduce, Cite, Explain',
     'Introduce: provide context for the quote (who says it, when). Cite: include the quotation or paraphrase with a citation. Explain: analyze HOW the evidence supports your claim. The E (explain) is most important — without it, you\'ve just added quotes without showing their significance.')]  ,
  'Revision, Style & Voice',
  [p('What is the difference between revision and proofreading? Which should you do first and why?','Think: big picture first, then details',
     'Revision: improving content, organization, argument, and clarity (big-picture changes). Proofreading: fixing grammar, spelling, and punctuation (surface-level). Always revise first — there\'s no point perfecting a paragraph you might later cut. Proofreading is the final step.'),
   p('What is "hedging" language in academic writing? Give an example of when to use it and when not to.','Think: qualifying claims with appropriate certainty',
     'Hedging uses words like "may," "suggests," "appears to," or "it could be argued" to qualify claims and show appropriate uncertainty. Use when: presenting interpretations or uncertain findings. Avoid when: stating clear facts. Over-hedging weakens arguments; under-hedging overstates certainty.'),
   p('What is voice in writing? How can a student develop a distinct academic voice?','Think: personality + precision + confidence',
     'Voice is the writer\'s distinctive personality expressed through word choice, sentence variety, and tone. Develop it by: reading widely (absorb different voices), taking clear positions (avoid hedging everything), using precise word choice, varying sentence structure, and being willing to say something specific rather than vague.'),
   p('A student\'s essay has this feedback: "Too much plot summary; not enough analysis." What specific revision strategy should they use?','Think: show, don\'t tell — analyze, don\'t retell',
     'For every plot point mentioned, add analysis: ask "So what? What does this reveal? How does this support my thesis?" Replace sentences that describe WHAT happened with sentences that explain WHY it matters. A good ratio: 1 sentence of context/quote, 2–3 sentences of analysis.')]
);

// Grade 10 History[1] = Cold War Era
PRACTICE[10].history[1] = u(
  'Origins & Ideology of the Cold War',
  [p('Why did the Cold War begin after World War II? What fundamental differences divided the U.S. and USSR?','Think: wartime allies → peacetime rivals',
     'The U.S. and USSR emerged from WWII as superpowers with opposing ideologies: U.S. (capitalism, liberal democracy) vs. USSR (communism, totalitarian state). Mutual distrust, the nuclear monopoly, and disagreements over postwar Europe (especially Germany) triggered rapid confrontation.'),
   p('What was the Truman Doctrine (1947)? Why was it significant?','Think: containment of communism',
     'President Truman pledged U.S. support (military and economic aid) to any nation threatened by communism, specifically Greece and Turkey. It established the policy of containment — preventing communism from spreading further — which guided U.S. Cold War strategy for decades.'),
   p('What was the Marshall Plan? How did it serve U.S. strategic interests while rebuilding Europe?','Think: economic aid as anti-communist strategy',
     'The U.S. provided ~$13 billion to rebuild Western European economies after WWII. Strategic interests: stable, prosperous democracies were less likely to turn communist; it also created trading partners for U.S. goods. The USSR rejected it and formed Comecon for Eastern Europe.'),
   p('What was NATO? Why did its formation matter in the Cold War?','Think: collective defense',
     'NATO (North Atlantic Treaty Organization, 1949): military alliance of Western democracies agreeing that an attack on one is an attack on all. It formalized U.S. commitment to European defense and was the West\'s answer to Soviet expansion. The USSR responded with the Warsaw Pact (1955).')]  ,
  'Cold War Conflicts & the End',
  [p('What was the Korean War (1950–53)? Why is it called the "Forgotten War"?','Think: first hot war of the Cold War',
     'After North Korea (communist, Soviet-backed) invaded South Korea, the U.S. led a UN force to defend it. After three years and 5+ million casualties, it ended in an armistice — approximately restoring the original border at the 38th parallel. Called "forgotten" because it had no clear victory and was overshadowed by WWII and Vietnam.'),
   p('What was the Cuban Missile Crisis (1962)? How close did the world come to nuclear war?','Think: 13 days, October 1962',
     'The USSR placed nuclear missiles in Cuba; the U.S. demanded removal. For 13 days, both nations were on the brink of nuclear war. Resolution: USSR removed missiles; U.S. publicly pledged not to invade Cuba (secretly removed missiles from Turkey). It was the closest the Cold War came to nuclear conflict.'),
   p('What was the Vietnam War\'s significance in Cold War terms? How did it affect American society?','Think: containment failed; domestic backlash',
     'The U.S. fought to prevent communist North Vietnam from taking South Vietnam. Despite massive military effort, the U.S. withdrew in 1973; Saigon fell in 1975. It was the first U.S. war lost. Domestically: massive anti-war movement, erosion of public trust in government (credibility gap), 58,000 American deaths.'),
   p('Why and how did the Cold War end? Who should get credit?','Think: Gorbachev\'s reforms + Reagan + internal Soviet collapse',
     'The USSR collapsed due to economic stagnation, military overstretch (Afghanistan), and Gorbachev\'s reforms (glasnost = openness; perestroika = restructuring). Reagan\'s arms buildup pressured the Soviet economy. Eastern European revolutions (1989), fall of the Berlin Wall, and dissolution of the USSR (1991) ended the Cold War.')]
);

// Grade 10 History[2] = Modern US History
PRACTICE[10].history[2] = u(
  'Civil Rights & Social Movements',
  [p('What were the key strategies of the Civil Rights Movement? Name two events where each was used.','Think: legal challenges, nonviolent direct action, economic pressure',
     'Legal: NAACP challenged segregation in courts (Brown v. Board, 1954). Nonviolent direct action: Montgomery Bus Boycott (1955), sit-ins at Woolworth\'s (1960), Birmingham marches (1963). Economic pressure: boycotts. These tactics exposed the brutality of racism and forced national attention.'),
   p('What did the Civil Rights Act of 1964 and Voting Rights Act of 1965 accomplish?','Think: end of legal discrimination',
     'Civil Rights Act (1964): banned racial discrimination in public accommodations (restaurants, hotels), employment, and federally funded programs. Voting Rights Act (1965): outlawed literacy tests and other discriminatory voting barriers; authorized federal oversight of elections in states with history of discrimination.'),
   p('What was the women\'s liberation movement of the 1960s–70s? What major legislation resulted?','Think: second-wave feminism',
     'The second-wave feminist movement fought for workplace equality, reproductive rights, and ending gender discrimination. Key result: Title IX (1972) prohibited sex discrimination in federally funded education programs; Equal Pay Act (1963); Roe v. Wade (1973). NOW (National Organization for Women) was a key organizing body.'),
   p('What is the significance of Roe v. Wade (1973) and its 2022 overturn (Dobbs v. Jackson)?','Think: constitutional right → state decision',
     'Roe (1973): Supreme Court held that the Constitution protects a woman\'s right to abortion under the right to privacy. Dobbs (2022): overturned Roe, returning abortion regulation entirely to states. This created a patchwork of laws — some states banned abortion; others protected it. One of the most contested Supreme Court decisions in history.')]  ,
  'Contemporary America',
  [p('What were the major causes and effects of the 2008 financial crisis?','Think: housing bubble, bank failures, recession',
     'Causes: risky mortgage lending (subprime loans), financial deregulation, complex financial instruments (CDOs, credit default swaps). Effects: housing market collapse, major bank failures (Lehman Brothers), $700B government bailout (TARP), worst recession since the Great Depression, 8+ million jobs lost.'),
   p('What is income inequality? How has it changed in the U.S. since the 1970s?','Think: Gini coefficient, CEO-to-worker ratio',
     'Income inequality measures the gap between high and low earners. Since the 1970s: the top 1% share of income rose from ~10% to ~20%; CEO pay grew ~940% while worker pay grew ~12%. Causes: automation, decline of unions, globalization, tax policy changes. The Gini coefficient (0=perfect equality, 1=total inequality) has risen significantly.'),
   p('What was the 9/11 attack and how did it reshape U.S. domestic and foreign policy?','Think: event + Patriot Act + wars in Afghanistan and Iraq',
     '2001 Al-Qaeda attacks killed ~3,000 people. Response: creation of Dept. of Homeland Security, PATRIOT Act (expanded surveillance), wars in Afghanistan (2001) and Iraq (2003). Lasting effects: airport security, military spending surge, debates over civil liberties vs. security, 20+ years of war in Afghanistan.'),
   p('What is partisanship and how has political polarization increased in modern America?','Think: division between political parties',
     'Partisanship: strong loyalty to a political party. Polarization increased due to: media fragmentation (partisan news), social media echo chambers, geographic sorting (like-minded people cluster), gerrymandering, and declining bipartisan compromise. Congress is more divided than at any point since the Civil War era.')]
);

// Grade 10 CS[1] = Databases
PRACTICE[10].cs[1] = u(
  'Database Fundamentals',
  [p('What is a database? How does a relational database differ from a flat file?','Think: organized data storage; related tables vs. one big table',
     'A database is an organized collection of structured data. Flat file: all data in one table (like a spreadsheet) — leads to redundancy. Relational database: multiple related tables linked by keys, reducing redundancy. Example: Students table + Courses table linked by StudentID.'),
   p('What are primary keys and foreign keys? Give an example of each.','Think: unique identifier vs. link between tables',
     'Primary key: a unique identifier for each record in a table (e.g., StudentID in a Students table — each student has a unique ID). Foreign key: a field in one table that references the primary key of another (e.g., StudentID in an Enrollments table — links students to their courses).'),
   p('What are the four main types of relationships in a relational database?','Think: one-to-one, one-to-many, many-to-many',
     'One-to-one: one record in Table A relates to exactly one in Table B (person → passport). One-to-many: one record in A relates to many in B (teacher → students). Many-to-many: multiple records in A relate to multiple in B (students → courses) — requires a junction/bridge table.'),
   p('What does CRUD stand for? Give a real-world example of each operation in a student database.','Think: Create, Read, Update, Delete',
     'Create: add a new student record. Read: look up a student\'s grades. Update: change a student\'s address. Delete: remove a graduated student\'s enrollment. CRUD operations are the four basic functions of persistent data storage and the foundation of most applications.')]  ,
  'SQL Queries',
  [p('Write a SQL query to retrieve all student names from a Students table where Grade = 10.','Think: SELECT ... FROM ... WHERE',
     'SELECT Name FROM Students WHERE Grade = 10; — SELECT specifies columns to retrieve, FROM specifies the table, WHERE filters rows by condition. To get all columns: SELECT * FROM Students WHERE Grade = 10;'),
   p('What does the JOIN clause do in SQL? Write a query joining Students and Enrollments on StudentID.','Think: combining data from two tables',
     'JOIN combines rows from two tables based on a related column. SELECT Students.Name, Enrollments.CourseName FROM Students INNER JOIN Enrollments ON Students.StudentID = Enrollments.StudentID; — INNER JOIN returns only rows with matches in both tables.'),
   p('What is the difference between WHERE and HAVING in SQL?','Think: filter rows vs. filter groups',
     'WHERE filters individual rows BEFORE grouping. HAVING filters groups AFTER a GROUP BY clause. Example: WHERE Grade = 10 (filters students). HAVING COUNT(*) > 5 (filters groups — e.g., courses with more than 5 students). You cannot use aggregate functions (SUM, COUNT) in WHERE.'),
   p('What does GROUP BY do? Write a query counting students per grade level.','Think: aggregate functions on groups',
     'GROUP BY groups rows that have the same values in specified columns. SELECT Grade, COUNT(*) AS StudentCount FROM Students GROUP BY Grade ORDER BY Grade; — This returns the number of students in each grade, sorted by grade level.')]
);

// Grade 10 Health[1] = Community Health
PRACTICE[10].health[1] = u(
  'Public Health Systems',
  [p('What is public health? How does it differ from personal/individual health?','Think: population-level vs. individual-level',
     'Public health focuses on protecting and improving the health of entire communities and populations through education, policy, and prevention. Individual health focuses on personal wellness. Examples of public health: vaccination programs, water sanitation, food safety regulations, anti-smoking campaigns.'),
   p('What are the social determinants of health? Name four and explain how they affect health outcomes.','Think: conditions where people live, work, and learn',
     'Income and wealth: poverty limits food, housing, healthcare access. Education: higher education linked to better health decisions. Environment: pollution, safe housing, clean water. Social support: isolation worsens health; strong relationships protect it. These upstream factors drive most health disparities between groups.'),
   p('What is the difference between disease prevention and health promotion?','Think: avoiding illness vs. building wellness',
     'Prevention: actions to avoid disease (vaccinations, safe sex, sunscreen). Health promotion: positive actions to build overall wellness (exercise programs, nutrition education, mental health resources, community parks). Prevention focuses on avoiding harm; promotion focuses on enhancing wellbeing.'),
   p('What role do local, state, and federal governments play in public health?','Think: different levels of authority and responsibility',
     'Local (health departments): inspect restaurants, manage local disease outbreaks, run clinics. State: license healthcare workers, set public health laws, run Medicaid. Federal (CDC, FDA, NIH): track national disease data, regulate food/drugs, fund research, coordinate national emergencies like pandemics.')]  ,
  'Environmental Health',
  [p('What is environmental health? Give two examples of environmental factors that affect human health.','Think: how the physical environment impacts wellbeing',
     'Environmental health studies how physical, chemical, and biological factors in the environment affect human health. Examples: air pollution (linked to asthma, lung cancer); contaminated water (lead pipes → neurological damage; Flint, Michigan crisis). Also: pesticides, noise pollution, heat.'),
   p('What is the relationship between climate change and public health?','Think: heatwaves, disease vectors, air quality, food security',
     'Climate change worsens public health through: more frequent heatwaves (heat stroke, death); expanded range of mosquitoes spreading malaria and dengue; increased air pollution (wildfires); extreme weather events; food/water insecurity. Communities of color and low-income communities face disproportionate impacts.'),
   p('What is the Precautionary Principle in environmental health? When is it applied?','Think: better safe than sorry in public health policy',
     'If a substance or action is suspected to harm the public or environment, precautionary measures should be taken even if full scientific certainty doesn\'t yet exist. Applied when: introducing new chemicals, GMOs, technologies. The burden of proof shifts to showing safety, not waiting for harm to be proven.'),
   p('What is environmental justice? Give one historical example of environmental injustice.','Think: who bears the burden of pollution?',
     'Environmental justice is the fair treatment of all people regarding environmental policies — no group should bear a disproportionate burden of pollution. Example: "Cancer Alley" in Louisiana — predominantly Black communities located along a petrochemical corridor have significantly higher cancer rates than state and national averages.')]
);

console.log('Grade 10 complete');

// ── GRADE 11 ──
// science[2] = Electricity & Magnetism
PRACTICE[11].science[2] = u(
  'Electric Circuits & Forces',
  [p('What is electric charge? What are the two types and the law governing their interactions?','Think: positive and negative; like charges repel',
     'Electric charge is a fundamental property of matter. Positive (+): protons. Negative (−): electrons. Coulomb\'s Law: like charges repel; opposite charges attract. The force = k·q₁·q₂/r² (increases with charge magnitude, decreases with distance squared).'),
   p('What is Ohm\'s Law? A 12V battery is connected to a 4Ω resistor. Find the current.','Think: V = IR',
     'Ohm\'s Law: V = IR (voltage = current × resistance). Current I = V/R = 12V / 4Ω = 3 amperes. This means 3 coulombs of charge flow per second through the circuit.'),
   p('What is the difference between series and parallel circuits? Give an advantage of each.','Think: one path vs. multiple paths',
     'Series: components in a single loop — same current flows through all; if one fails, all fail. Voltage divides. Parallel: multiple paths — same voltage across all branches; current divides; if one fails, others continue. Homes use parallel (each outlet independent). Series: simpler circuits, battery packs.'),
   p('What is electric power? Calculate the power used by a 120V device drawing 5A of current.','Think: P = IV',
     'Power = Current × Voltage = P = IV = 5A × 120V = 600 watts. Also P = I²R = V²/R. Power is the rate of energy use. 600W means 600 joules of energy used per second. Your electricity bill is based on kilowatt-hours (kWh = kW × hours).')]  ,
  'Magnetism & Electromagnetic Induction',
  [p('What causes magnetism? How is a permanent magnet different from an electromagnet?','Think: moving electrons create magnetic fields',
     'Magnetism arises from the motion of electric charges (electrons). In permanent magnets, unpaired electrons in iron/nickel/cobalt align in the same direction. Electromagnets: electric current through a wire coil creates a magnetic field — field disappears when current stops. Electromagnets can be switched on/off.'),
   p('State Faraday\'s Law of electromagnetic induction.','Think: changing magnetic field → current',
     'Faraday\'s Law: a changing magnetic field induces an electromotive force (EMF) in a conductor. The induced voltage is proportional to the rate of change of magnetic flux. This is the principle behind generators (mechanical motion → electricity) and transformers (AC voltage change).'),
   p('How does an electric generator work? Connect it to Faraday\'s Law.','Think: spin a coil in a magnetic field → electricity',
     'A generator converts mechanical energy to electrical energy. A wire coil rotates within a magnetic field — as the coil moves, the magnetic flux through it changes, inducing current (Faraday\'s Law). Turbines (steam, wind, water) spin the coil. This is how all power plants generate electricity.'),
   p('What is the difference between AC and DC current? Which does your home use and why?','Think: direction of flow',
     'DC (Direct Current): electrons flow in one direction (batteries). AC (Alternating Current): electrons oscillate back and forth at 60 Hz. Homes use AC because it can be efficiently transformed to different voltages for long-distance transmission and is safer for high-power appliances.')]
);

// science[3] = Waves, Light & Optics
PRACTICE[11].science[3] = u(
  'Wave Behavior & Properties',
  [p('What is the principle of superposition? What are constructive and destructive interference?','Think: waves adding together',
     'Superposition: when two waves occupy the same space, the resulting displacement equals the sum of their individual displacements. Constructive interference: waves add (crests align → bigger wave). Destructive interference: waves cancel (crest meets trough → smaller/no wave). Used in noise-canceling headphones.'),
   p('What is the Doppler Effect? Give one example in sound and one in light.','Think: apparent frequency change due to relative motion',
     'The Doppler Effect: when a wave source moves relative to an observer, the observed frequency changes. Sound: an ambulance siren sounds higher-pitched as it approaches and lower as it moves away. Light: stars moving away show redshift (lower frequency); approaching stars show blueshift. Used in radar guns and measuring star movement.'),
   p('What is resonance? Give one practical example and one dangerous example.','Think: driving something at its natural frequency',
     'Resonance occurs when an object is driven at its natural (resonant) frequency, causing large amplitude oscillations. Practical: guitar strings resonate to amplify sound. Dangerous: Tacoma Narrows Bridge (1940) — wind at bridge\'s natural frequency caused resonant oscillations until it collapsed.'),
   p('A wave has a speed of 300 m/s and a wavelength of 0.5 m. Find its frequency and period.','Think: v = fλ; T = 1/f',
     'Frequency: f = v/λ = 300/0.5 = 600 Hz. Period: T = 1/f = 1/600 ≈ 0.00167 seconds (1.67 milliseconds). The wave completes 600 full cycles per second, each lasting about 1.67 ms.')]  ,
  'Light, Optics & Spectra',
  [p('What is the law of reflection? What is the law of refraction (Snell\'s Law)?','Think: angle in = angle out; bending due to speed change',
     'Reflection: angle of incidence = angle of reflection (both measured from the normal to the surface). Refraction (Snell\'s Law): n₁ sin θ₁ = n₂ sin θ₂ — light bends when it crosses from one medium to another due to a change in speed. It bends toward normal when slowing down.'),
   p('What is total internal reflection? Where is it used in everyday technology?','Think: light bouncing inside glass',
     'When light travels from a denser to less dense medium at an angle greater than the critical angle, it reflects completely instead of refracting. Used in: fiber optic cables (light bounces along the fiber core, transmitting data at near light speed) and diamond cutting (maximizes internal reflection for sparkle).'),
   p('What is a converging (convex) lens vs. a diverging (concave) lens? What does each do to parallel rays of light?','Think: brings together vs. spreads apart',
     'Converging (convex) lens: thicker in the middle — bends parallel rays toward the focal point. Used in: cameras, magnifying glasses, the human eye. Diverging (concave) lens: thinner in the middle — spreads parallel rays apart (appears to come from a virtual focal point). Used in: glasses for nearsightedness.'),
   p('What is the electromagnetic spectrum? Why do different wavelengths produce different colors of visible light?','Think: wavelength → color',
     'Visible light is the narrow band of the EM spectrum (400–700nm) humans can see. Shorter wavelengths → higher energy → blue/violet light. Longer wavelengths → lower energy → red light. White light contains all wavelengths; a prism separates them by refracting different wavelengths at different angles (dispersion).')]
);

// Grade 11 ELA[1] = Research & Rhetoric
PRACTICE[11].ela[1] = u(
  'Research Methods & Source Analysis',
  [p('What is a literature review? How does it differ from a research paper?','Think: surveying existing knowledge vs. creating new knowledge',
     'A literature review synthesizes existing research on a topic, identifying key findings, debates, and gaps. A research paper may include original analysis, experiments, or arguments. Literature reviews show what is already known; they set the context for new research.'),
   p('What is the difference between qualitative and quantitative research? Give an example of each.','Think: words vs. numbers',
     'Quantitative: numerical data, statistical analysis (e.g., survey of 500 students, results analyzed statistically). Qualitative: non-numerical data — observations, interviews, case studies (e.g., in-depth interviews with 10 teachers about teaching methods). Each answers different research questions.'),
   p('What is the difference between correlation and causation in research? Why does it matter?','Think: two things moving together vs. one causing the other',
     'Correlation: two variables change together (ice cream sales and drowning rates both rise in summer). Causation: one causes the other (swimming, not ice cream, is the common factor). Misinterpreting correlation as causation leads to false conclusions and bad policies.'),
   p('When evaluating a scientific study, what questions should you ask about methodology?','Think: sample size, control group, peer review, replication',
     'Key questions: Was the sample large and representative enough? Was there a control group? Was it blinded? Were results peer-reviewed? Has it been replicated? Who funded it (conflicts of interest)? A single study rarely proves anything — look for consensus across multiple well-designed studies.')]  ,
  'Rhetorical Analysis & Persuasion',
  [p('What is rhetorical analysis? What are the key elements you examine?','Think: HOW does the text persuade?',
     'Rhetorical analysis examines HOW a text persuades its audience. Elements: rhetorical situation (speaker, audience, purpose, context), appeals (logos, ethos, pathos), tone, structure, word choice (diction), figurative language, and evidence. Goal: understand the choices the author made and why.'),
   p('What is kairos in rhetoric? Give an example of how timing affects the persuasiveness of an argument.','Think: the right moment to make the argument',
     'Kairos is the opportune moment for an argument — context makes it more or less persuasive. Example: arguing for stricter gun laws is more persuasive immediately after a mass shooting (emotional salience, public attention) than in a period of low gun violence. Timing is a rhetorical tool.'),
   p('What is the difference between deductive and inductive reasoning? Give an example of each in an argument.','Think: general to specific vs. specific to general',
     'Deductive: starts from a general principle, applies to a specific case. "All humans are mortal; Socrates is human; therefore Socrates is mortal." Inductive: draws a general conclusion from specific observations. "Every swan I\'ve seen is white; therefore all swans are white" (note: inductive conclusions can be wrong).'),
   p('Analyze this sentence rhetorically: "We will not rest until every child has access to clean water." Who is the speaker likely addressing, and what appeals are at work?','Think: ethos, pathos, logos + audience',
     'Pathos: "every child" is emotionally compelling. Ethos: "We will not rest" signals commitment and authority. The absolute language ("every child," "will not rest") conveys urgency. Audience: likely the public, voters, or policymakers — those who can demand or fund action. The sentence is designed to inspire and mobilize.')]
);

// Grade 11 ELA[2] = Language & Style
PRACTICE[11].ela[2] = u(
  'Syntax & Diction for Effect',
  [p('What is syntax in writing? How can varying sentence structure improve writing quality?','Think: arrangement of words; short vs. long sentences',
     'Syntax is the arrangement of words and phrases to create sentences. Varying sentence structure creates rhythm, emphasis, and interest. Short sentences: create urgency, emphasis ("He was gone. Forever."). Long, complex sentences: show elaboration and relationship between ideas. Monotonous syntax (all same length) dulls the reader.'),
   p('What is anaphora? How does it function in rhetoric and literature? Give an example.','Think: repetition at the beginning of successive clauses',
     'Anaphora is the repetition of a word/phrase at the beginning of successive clauses. It creates rhythm, emphasis, and emotional force. Example: MLK\'s "I Have a Dream" speech — "I have a dream that..." repeated. Churchill: "We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields..."'),
   p('What is the difference between formal, semi-formal, and informal register? Give an example of each for the same message.','Think: audience and purpose determine register',
     'Formal: "The committee has reviewed and approved the proposal." Semi-formal: "We\'ve decided to go ahead with the proposal." Informal: "Yeah, they said yes to the plan." Register is shaped by audience, purpose, and context. Academic and professional writing require formal register.'),
   p('What is periodic vs. cumulative sentence structure? Write one of each.','Think: suspense-building vs. elaborating',
     'Periodic: main clause comes at the end, building suspense ("Despite the rain, the cold, and the exhaustion, she crossed the finish line"). Cumulative (loose): main clause comes first, then elaborating phrases ("She crossed the finish line, gasping for breath, tears streaming down her face, arms raised in triumph").')]  ,
  'Grammar & AP Language Strategies',
  [p('What is a gerund phrase vs. a participial phrase? Give an example of each used in a sentence.','Think: both use -ing, but one is a noun, one is a modifier',
     'Gerund phrase: functions as a noun ("Running every morning improves endurance"). Participial phrase: modifies a noun ("Running every morning, she improved her endurance"). The gerund IS the subject; the participial DESCRIBES the subject.'),
   p('What are absolute phrases? How do they add sophistication to writing?','Think: noun + participle; not attached to a main clause but modifying the whole sentence',
     'An absolute phrase consists of a noun + participle (+ modifiers) that modifies the entire sentence. "Her face pale with fear, she opened the envelope." Absolute phrases add descriptive detail and allow writers to pack multiple ideas into one sentence without a separate clause.'),
   p('What is the subjunctive mood? When do you use it in English?','Think: wishes, hypotheticals, demands',
     'The subjunctive expresses wishes, hypothetical conditions, demands, or suggestions — using "were" instead of "was," or base verb form. Examples: "If I were president..." (hypothetical). "The teacher demanded that he be quiet" (demand). "I wish it were summer" (wish).'),
   p('What is the AP Language and Composition exam\'s "SOAPS" strategy for analyzing a text?','Think: Speaker, Occasion, Audience, Purpose, Subject',
     'Speaker: who is speaking? What are their credentials/biases? Occasion: what event/context prompted the piece? Audience: who is the intended audience and how does that shape choices? Purpose: what is the author trying to accomplish? Subject: what is the text literally about? SOAPS grounds rhetorical analysis in context.')]
);

console.log('Grade 11 sci/ELA done');

// Grade 11 History[1] = Contemporary Global Issues
PRACTICE[11].history[1] = u(
  'Climate & Environmental Policy',
  [p('What is the scientific consensus on climate change? What evidence supports it?','Think: temperature records, CO₂, sea level, ice cores',
     '97%+ of climate scientists agree human activity is the primary driver of current climate change. Evidence: global temperature rise of ~1.1°C since pre-industrial era, atmospheric CO₂ at highest levels in 800,000 years (ice cores), rising sea levels, shrinking Arctic ice, shifting seasons, and more frequent extreme weather events.'),
   p('What was the Paris Agreement (2015)? What are its goals and limitations?','Think: international climate treaty',
     'International treaty signed by 196 parties committing to limit global warming to 1.5–2°C above pre-industrial levels. Each country sets its own targets (NDCs). Limitations: voluntary commitments, no enforcement mechanism, current pledges are insufficient to meet 1.5°C goal. Key milestone in international climate cooperation.'),
   p('What is the difference between climate mitigation and climate adaptation?','Think: prevent vs. prepare',
     'Mitigation: reducing or preventing greenhouse gas emissions to slow climate change (renewable energy, energy efficiency, reforestation). Adaptation: adjusting to current or expected climate impacts (sea walls, drought-resistant crops, cooling centers, updated building codes). Both are necessary; adaptation is needed because some change is already locked in.'),
   p('What are the key drivers of deforestation globally, and why is it a climate issue?','Think: forests as carbon sinks',
     'Key drivers: agricultural expansion (soy, palm oil, cattle), logging, mining, urban development. Climate impact: forests absorb ~30% of human CO₂ emissions. Deforestation releases stored carbon AND eliminates future absorption. The Amazon alone stores ~150 billion tons of carbon. It also destroys biodiversity and displaces Indigenous communities.')]  ,
  'Human Rights & International Conflict',
  [p('What is the Universal Declaration of Human Rights (UDHR)? When was it adopted and what does it establish?','Think: 1948, UN, fundamental rights',
     'Adopted by the UN General Assembly in 1948 after WWII atrocities. The UDHR establishes 30 articles covering civil, political, economic, social, and cultural rights — including life, liberty, freedom of expression, education, and work. Not legally binding but has influenced international law and national constitutions.'),
   p('What is the difference between a refugee, an asylum seeker, and an internally displaced person (IDP)?','Think: who they are and where they are',
     'Refugee: fled their country due to persecution, war, or disaster; granted international protection. Asylum seeker: in another country, seeking refugee status (status not yet determined). IDP: forced from home but still within their own country — not covered by the same international protections as refugees. All are displaced people.'),
   p('What are war crimes and crimes against humanity? Name one historical example of each.','Think: specific military violations vs. widespread civilian attacks',
     'War crimes: violations of laws of war (targeting civilians, using prohibited weapons, torture of prisoners). Example: My Lai Massacre (Vietnam). Crimes against humanity: widespread or systematic attacks on civilians (murder, enslavement, apartheid). Example: apartheid in South Africa. Both are prosecuted by the International Criminal Court (ICC).'),
   p('What is the "Responsibility to Protect" (R2P) doctrine? What are the debates around it?','Think: when does the international community intervene to protect civilians?',
     'R2P (2005 UN Summit): states have a responsibility to protect their citizens from genocide, war crimes, ethnic cleansing, and crimes against humanity. If they fail, the international community has the right to intervene. Debate: when is intervention justified vs. violating sovereignty? Libya (2011) and Syria illustrate the tensions.')]
);

// Grade 11 History[2] = Economics
PRACTICE[11].history[2] = u(
  'Macro & Microeconomics',
  [p('What is the difference between macroeconomics and microeconomics? Give one example topic from each.','Think: big picture vs. individual actors',
     'Macroeconomics: studies the economy as a whole (GDP, inflation, unemployment, monetary policy). Microeconomics: studies individual actors — consumers, firms, markets (supply and demand for a specific product, firm pricing strategy, consumer behavior).'),
   p('What is GDP? What four components make it up? Which is largest in the U.S.?','Think: Gross Domestic Product = C + I + G + NX',
     'GDP measures total value of goods and services produced in a country in a year. C = Consumer spending (largest, ~70% of U.S. GDP). I = Investment (business spending on equipment, construction). G = Government spending. NX = Net exports (exports − imports). Higher GDP generally indicates a growing economy.'),
   p('What is inflation? What causes it, and what tools does the Federal Reserve use to control it?','Think: too much money chasing too few goods',
     'Inflation: general rise in prices over time. Causes: demand-pull (too much spending), cost-push (production costs rise), expansion of money supply. Fed tools: raise interest rates (makes borrowing more expensive, reducing spending), reduce money supply (open market operations — selling bonds to remove money from circulation).'),
   p('What is the law of supply and demand? Draw a verbal description of what happens to price when demand increases but supply stays the same.','Think: equilibrium price and quantity',
     'Law of demand: as price rises, quantity demanded falls (inverse). Law of supply: as price rises, quantity supplied rises (direct). Equilibrium: where supply = demand. If demand increases (shifts right) while supply is unchanged: shortage occurs at old price → price rises until a new, higher equilibrium is reached.')]  ,
  'Economic Policy & Personal Finance',
  [p('What is fiscal policy? What are the two main tools governments use?','Think: government taxing and spending',
     'Fiscal policy: how the government uses taxation and spending to influence the economy. Expansionary (stimulate growth): increase spending or cut taxes. Contractionary (slow inflation): decrease spending or raise taxes. Used during recessions (stimulus packages like 2008-09 TARP) and inflation.'),
   p('What is the difference between a stock and a bond? Which is generally higher risk and higher reward?','Think: ownership vs. loan',
     'Stock: ownership share in a company; value rises and falls with company performance (higher risk, higher potential return). Bond: a loan to a government or corporation; pays fixed interest (lower risk, lower return). A diversified portfolio includes both. Stocks: long-term growth. Bonds: stability and income.'),
   p('What is compound interest? Calculate the balance after 10 years if $1,000 is invested at 7% annual interest compounded annually.','Think: A = P(1 + r)ⁿ',
     'A = 1000 × (1.07)¹⁰ = 1000 × 1.9672 = $1,967.15. Compound interest earns interest on previous interest — dramatically outpacing simple interest over time. Starting early is the key: the same investment at age 25 vs. 35 can result in double the final amount.'),
   p('What is an emergency fund? Why do personal finance experts recommend having 3–6 months of expenses saved?','Think: financial safety net',
     'An emergency fund is liquid savings set aside for unexpected expenses (job loss, medical emergency, car repair). 3–6 months of living expenses provides a buffer to avoid going into high-interest debt during a crisis. Keeps you from liquidating investments at a loss. First priority in any personal finance plan.')]
);

// Grade 11 CS[1] = Intro to AI & Machine Learning
PRACTICE[11].cs[1] = u(
  'AI Concepts & Machine Learning Basics',
  [p('What is artificial intelligence? What is the difference between narrow AI and general AI?','Think: specific task vs. broadly intelligent',
     'AI: systems that perform tasks normally requiring human intelligence. Narrow AI: excels at one specific task (chess, image recognition, translation). General AI (AGI): hypothetical system with human-like intelligence across any domain — does not yet exist. Current AI is all narrow AI.'),
   p('What is machine learning? How does it differ from traditional programming?','Think: learning from data vs. following explicit rules',
     'Traditional programming: programmer writes explicit rules → computer follows them. Machine learning: system learns patterns from data without being explicitly programmed. It improves with experience. Example: spam filters learn from email data rather than following hand-coded rules.'),
   p('What are the three main types of machine learning? Give a real-world example of each.','Think: supervised, unsupervised, reinforcement',
     'Supervised: trained on labeled data (email → spam/not spam). Unsupervised: finds patterns in unlabeled data (customer segmentation). Reinforcement: agent learns by trial and error with rewards/penalties (game-playing AI, robotics). Most practical ML is supervised learning.'),
   p('What is a neural network? How is it inspired by the human brain?','Think: layers of nodes that process information',
     'A neural network consists of interconnected nodes (neurons) organized in layers: input layer (receives data), hidden layers (process and transform data), output layer (produces result). Like the brain, connections between neurons are weighted and adjusted during training. Deep neural networks (many layers) power image recognition, language models, and more.')]  ,
  'Ethics of AI & Applications',
  [p('What is algorithmic bias? Give one real-world example of harm it has caused.','Think: AI inherits human biases from training data',
     'Algorithmic bias: AI systems that produce systematically unfair outcomes for certain groups, usually because training data reflects historical biases. Example: facial recognition systems have been shown to misidentify people of color at significantly higher rates, leading to wrongful arrests. Bias in hiring algorithms has screened out women and minority candidates.'),
   p('What is the "black box" problem in AI? Why does it matter for high-stakes decisions?','Think: we can\'t explain why the AI decided what it decided',
     'Many AI models (especially deep learning) make decisions through processes humans can\'t fully explain or interpret. This matters in healthcare (AI diagnoses a cancer — why?), criminal justice (AI recommends a sentence — on what basis?), and lending (AI rejects a loan — how?). Explainability is crucial for accountability.'),
   p('What is generative AI? How do large language models (LLMs) work at a basic level?','Think: AI that creates content',
     'Generative AI creates new content (text, images, music, code). LLMs are trained on massive text datasets to predict the next word/token given the input. Through this training, they develop representations of language patterns, grammar, facts, and reasoning. They don\'t "understand" — they predict based on statistical patterns in training data.'),
   p('What are three ethical frameworks for thinking about AI development and deployment?','Think: who benefits, who decides, who is harmed',
     '(1) Consequentialist: evaluate AI by its outcomes — does it produce more benefit than harm overall? (2) Rights-based: does AI respect fundamental human rights (privacy, due process, freedom)? (3) Justice/equity: does AI treat all groups fairly or does it entrench inequalities? Organizations like the EU and IEEE are developing AI ethics guidelines.')]
);

// Grade 11 Health[1] = Health Decision Making
PRACTICE[11].health[1] = u(
  'Evaluating Health Information',
  [p('How do you evaluate the credibility of health information online? Name four criteria.','Think: who wrote it, when, why, and what evidence?',
     '(1) Author credentials: is the author a qualified health professional? (2) Source type: peer-reviewed journal vs. blog? (3) Currency: is it recent (health science changes)? (4) Evidence: does it cite scientific studies? Red flags: miracle claims, sponsored content, emotional testimonials, no citations. Trust: CDC, NIH, WHO, Mayo Clinic.'),
   p('What is the difference between anecdotal evidence and scientific evidence in health claims?','Think: one person\'s experience vs. rigorous study',
     'Anecdotal: one person\'s personal story ("This supplement cured my arthritis!"). Scientific: controlled, peer-reviewed studies on large samples with statistical analysis. Anecdotal evidence is unreliable because placebo effects, coincidence, and confirmation bias can make treatments seem effective when they\'re not.'),
   p('What is a placebo effect? Why do randomized controlled trials (RCTs) control for it?','Think: believing you\'re being treated can itself cause improvement',
     'Placebo effect: improvement in condition due to a patient\'s belief that they are receiving treatment, even if they receive an inert substance. RCTs address this by randomly assigning patients to treatment or placebo groups — neither patients nor researchers know who got what (double-blind). This isolates the actual drug/treatment effect.'),
   p('What is health literacy? Why is it important for individuals and society?','Think: understanding health information to make good decisions',
     'Health literacy is the ability to find, understand, and use health information to make informed decisions. Low health literacy leads to: medication errors, delayed treatment, worse chronic disease management, and vulnerability to health misinformation. Higher health literacy → better health outcomes across populations.')]  ,
  'Healthcare Systems & Advocacy',
  [p('What is the difference between Medicare and Medicaid in the U.S.?','Think: elderly vs. low-income; federal vs. federal/state',
     'Medicare: federal program for people 65+ and some disabled individuals (regardless of income). Medicaid: joint federal-state program providing health coverage to low-income individuals and families. Eligibility, coverage, and costs differ. The ACA (2010) expanded Medicaid eligibility in participating states.'),
   p('What is preventive care? Give three examples and explain why it is cost-effective.','Think: staying healthy is cheaper than treating disease',
     'Preventive care: services to prevent disease before it occurs. Examples: annual physicals, vaccinations, cancer screenings (mammograms, colonoscopies). Cost-effective because: catching diseases early (or preventing them) is far cheaper than treating advanced illness. Example: a colonoscopy costs far less than treating stage 4 colon cancer.'),
   p('What does it mean to be a health advocate? Name three ways a person can advocate for their own health.','Think: be informed, speak up, know your rights',
     '(1) Prepare questions before doctor appointments and write down answers. (2) Request explanations of diagnoses and treatment options in plain language. (3) Seek a second opinion for major diagnoses. (4) Know your insurance coverage and appeal denials. (5) Keep personal medical records. Advocacy ensures you receive informed, quality care.'),
   p('What is mental health parity? Why has it been a healthcare advocacy issue?','Think: mental health treated equally to physical health',
     'Mental health parity requires that insurance coverage for mental health and substance use disorders be no more restrictive than for physical health conditions. The Mental Health Parity and Addiction Equity Act (2008) mandated this. Historically, mental health was heavily restricted in insurance plans, making treatment inaccessible. Enforcement remains inconsistent.')]
);

console.log('Grade 11 complete');

// ── GRADE 12 ──
// math[2] = Statistics (AP-level)
PRACTICE[12].math[2] = u(
  'Probability Distributions',
  [p('What is a normal distribution? What is the empirical rule (68-95-99.7)?','Think: bell curve; where do most values fall?',
     'A normal distribution is a symmetric, bell-shaped distribution where data clusters around the mean. Empirical rule: 68% of data falls within 1 standard deviation of the mean; 95% within 2 SD; 99.7% within 3 SD. Used in statistics, natural phenomena, test scores, heights, etc.'),
   p('What is a z-score? A student scores 85 on a test with mean 75 and standard deviation 10. What is the z-score and what does it mean?','Think: how many standard deviations from the mean?',
     'z = (x − μ) / σ = (85 − 75) / 10 = 1.0. This means the student scored 1 standard deviation above the mean — better than approximately 84.1% of test-takers (using the z-table).'),
   p('What is a binomial distribution? What conditions must be met for it to apply?','Think: fixed n, two outcomes, constant p',
     'Binomial distribution models number of successes in n independent trials where each trial has two outcomes (success/failure) with constant probability p. Conditions: fixed number of trials (n), independent trials, two outcomes, constant probability. Example: flipping a coin 10 times, counting heads.'),
   p('What is the difference between a parameter and a statistic? Give an example of each.','Think: population vs. sample',
     'Parameter: a number describing a population (often unknown). Example: μ = true mean height of all 18-year-olds. Statistic: a number describing a sample (used to estimate the parameter). Example: x̄ = mean height of 200 sampled 18-year-olds = 5\'9". Statistics are used to infer parameters.')]  ,
  'Statistical Inference & Significance Testing',
  [p('What is a hypothesis test? Define null and alternative hypotheses.','Think: assume nothing is happening, then test it',
     'A hypothesis test uses sample data to decide whether to reject a null hypothesis. H₀ (null): assumes no effect/difference (e.g., "The new drug has no effect"). Hₐ (alternative): what you\'re trying to find evidence for (e.g., "The new drug reduces symptoms"). You either reject H₀ or fail to reject it — you never "prove" Hₐ.'),
   p('What is a p-value? If p = 0.03, what does it mean at α = 0.05?','Think: probability of seeing results this extreme if H₀ were true',
     'The p-value is the probability of getting results as extreme as observed, assuming H₀ is true. At α = 0.05: if p < 0.05, reject H₀ (results are statistically significant). p = 0.03 < 0.05 → reject H₀. This means there\'s only a 3% chance of getting these results by random chance if H₀ were true.'),
   p('What is a confidence interval? Interpret: "We are 95% confident the true mean lies between 42 and 56."','Think: range of plausible values for the parameter',
     'A confidence interval is a range of values likely to contain the true population parameter. Interpretation: if we repeated this study 100 times, 95 of the resulting intervals would capture the true mean. It does NOT mean there\'s a 95% probability the true mean is in this specific interval.'),
   p('What is Type I vs. Type II error in hypothesis testing?','Think: false positive vs. false negative',
     'Type I (α): rejecting H₀ when it\'s actually true — a false positive. Example: concluding a drug works when it doesn\'t. Type II (β): failing to reject H₀ when it\'s actually false — a false negative. Example: concluding a drug doesn\'t work when it does. Reducing Type I increases Type II risk.')]
);

// math[3] = Discrete Mathematics
PRACTICE[12].math[3] = u(
  'Combinatorics & Graph Theory',
  [p('What is the difference between a permutation and a combination? When do you use each?','Think: does order matter?',
     'Permutation (order matters): P(n,r) = n!/(n−r)!. Combination (order doesn\'t matter): C(n,r) = n!/(r!(n−r)!). Use permutations for: arrangements, passwords. Use combinations for: choosing team members, lottery tickets. Example: choosing 3 from 10 people → C(10,3) = 120 (committee) or P(10,3) = 720 (ranked positions).'),
   p('How many ways can 8 runners finish 1st, 2nd, 3rd in a race?','Think: permutation — order matters',
     'P(8,3) = 8!/(8−3)! = 8!/5! = 8×7×6 = 336 ways. For first place: 8 choices. Second: 7 remaining. Third: 6. Multiply: 8 × 7 × 6 = 336.'),
   p('What is a graph in mathematics? Define vertex, edge, degree, and path.','Think: network of points and connections',
     'A graph is a set of vertices (nodes) connected by edges (lines/arcs). Degree: number of edges connected to a vertex. Path: sequence of vertices where each consecutive pair is connected by an edge. Graphs model networks: social networks, maps, internet connections.'),
   p('What is the Handshaking Lemma? In a graph with 6 vertices where each vertex has degree 3, how many edges are there?','Think: sum of degrees = 2 × number of edges',
     'Handshaking Lemma: sum of all vertex degrees = 2 × number of edges (each edge contributes 2 to the total degree). Sum of degrees = 6 × 3 = 18. Number of edges = 18/2 = 9 edges.')]  ,
  'Logic & Proof Techniques',
  [p('What is a proposition in logic? What are the basic logical connectives?','Think: true/false statement + and, or, not, if-then',
     'A proposition is a statement that is either true or false (not both). Basic connectives: ∧ (AND: both true), ∨ (OR: at least one true), ¬ (NOT: negation), → (conditional: if-then), ↔ (biconditional: if and only if). Truth tables systematically evaluate logical expressions.'),
   p('What is the difference between a direct proof, a proof by contradiction, and a proof by induction?','Think: three fundamental proof strategies',
     'Direct proof: assume hypothesis is true, use logical steps to reach conclusion. Contradiction: assume the negation is true, derive a contradiction, conclude the original must be true. Induction: prove for base case, assume true for k, prove true for k+1 — therefore true for all natural numbers.'),
   p('What is a tautology? Give an example. What is a contradiction? Give an example.','Think: always true vs. always false',
     'Tautology: a logical expression always true regardless of truth values of its variables. Example: p ∨ ¬p ("It is raining or it is not raining" — always true). Contradiction: always false. Example: p ∧ ¬p ("It is raining and it is not raining" — impossible, always false).'),
   p('Prove by contradiction that √2 is irrational.','Think: assume it IS rational, then derive a contradiction',
     'Assume √2 = a/b (fully reduced, a,b integers, no common factors). Then 2 = a²/b², so a² = 2b² → a² is even → a is even → a = 2k. Then (2k)² = 2b² → 4k² = 2b² → b² = 2k² → b is even. But then a and b are both even, contradicting our assumption that a/b was fully reduced. Therefore √2 is irrational. ∎')]
);

// Grade 12 Science[2] = Environmental Science
PRACTICE[12].science[2] = u(
  'Ecosystems & Sustainability',
  [p('What are ecosystem services? Give two examples and explain why they have economic value.','Think: benefits humans get from nature',
     'Ecosystem services: benefits that healthy ecosystems provide to humans. Examples: (1) Pollination by bees — essential for ~75% of food crops, worth $200B+ annually. (2) Wetlands as flood buffers — a wetland acre can absorb millions of gallons of floodwater, saving billions in flood damage. Losing ecosystems = losing free services.'),
   p('What is the tragedy of the commons? Give one environmental example.','Think: shared resources being overused because individuals act in self-interest',
     'When a shared resource (commons) is freely accessible, individuals tend to overuse it because personal benefit is immediate while costs are shared. Example: overfishing — each fishing boat has incentive to catch as much as possible, but collectively this depletes fish stocks for everyone. Solutions: regulation, quotas, privatization, or community management.'),
   p('What is the difference between renewable and nonrenewable resources? Give two examples of each.','Think: can nature replenish it in a human timeframe?',
     'Renewable: replenished naturally at a rate humans can sustain (solar energy, wind, timber from managed forests, freshwater from rainfall). Nonrenewable: finite stocks that take millions of years to form (oil, coal, natural gas, many minerals). Sustainability requires transitioning from nonrenewable to renewable resources.'),
   p('What is a carbon footprint? What are the three biggest contributors for an average American?','Think: total GHG emissions from an individual or organization',
     'A carbon footprint is the total greenhouse gas emissions (in CO₂ equivalent) caused by an individual, organization, or product. Three biggest contributors for an average American: (1) Transportation (driving, flying) — ~29%. (2) Home energy (heating, electricity) — ~25%. (3) Food (meat production especially) — ~13%.')]  ,
  'Environmental Policy & Global Issues',
  [p('What is the Environmental Protection Agency (EPA)? Name two major environmental laws it enforces.','Think: federal environmental regulator',
     'The EPA is the U.S. federal agency responsible for protecting human health and the environment. Key laws: Clean Air Act (1970): regulates air pollution, sets National Ambient Air Quality Standards. Clean Water Act (1972): regulates discharge of pollutants into U.S. waters. Also enforces Superfund for toxic waste site cleanup.'),
   p('What is biodiversity loss? Name three major causes and explain one in detail.','Think: habitat destruction, invasive species, pollution, climate change, overexploitation',
     'Biodiversity loss is the reduction in variety of life on Earth. Causes: (1) Habitat destruction — deforestation/urban sprawl eliminates species\' homes (primary cause globally). (2) Invasive species — introduced species outcompete natives. (3) Climate change — shifting habitats faster than species can adapt. We are in the 6th mass extinction, losing species 1,000× natural background rate.'),
   p('What is the Kyoto Protocol vs. the Paris Agreement? How do they differ?','Think: binding vs. voluntary targets',
     'Kyoto (1997): legally binding emission reduction targets for developed nations only; U.S. never ratified. Paris (2015): all nations set their own targets (NDCs); voluntary but with transparency mechanism; broader participation (195 parties). Paris is more inclusive but relies on national commitment rather than enforcement.'),
   p('What is sustainable development? How does the UN\'s SDG framework operationalize it?','Think: meeting today\'s needs without compromising the future',
     'Sustainable development: meeting present needs without compromising future generations\' ability to meet theirs (Brundtland Report, 1987). The UN\'s 17 Sustainable Development Goals (2015) operationalize this across: poverty, hunger, health, education, gender equality, clean water, clean energy, climate action, and more — with 169 specific targets and indicators.')]
);

// Grade 12 ELA[1] = AP English Literature
PRACTICE[12].ela[1] = u(
  'Close Reading & Literary Analysis',
  [p('What is the difference between explication and interpretation in literary analysis?','Think: explain the text vs. argue a meaning',
     'Explication: close, detailed explanation of what a text says line-by-line or passage-by-passage. Interpretation: arguing what the text means, what theme it explores, or what effect it achieves. Good AP essays do both — they explain HOW the text works while arguing WHAT it means.'),
   p('Analyze the effect of the following opening: "It was the best of times, it was the worst of times" (Dickens, A Tale of Two Cities). What devices are present?','Think: multiple literary devices; consider what they accomplish',
     'Devices: antithesis (opposing ideas in parallel structure), anaphora (repetition of "It was the..."), paradox (best and worst simultaneously), parallelism. Effect: immediately establishes thematic tension (revolution as both liberating and destructive), engages the reader with contradiction, and establishes Dickens\'s grand, rhetorical style.'),
   p('What is the difference between a symbol and a motif in literature?','Think: one thing with deeper meaning vs. recurring pattern',
     'Symbol: a specific object, person, or event that represents something beyond itself (e.g., the green light in Gatsby = unattainable dreams). Motif: a recurring element (image, phrase, idea) that develops a theme throughout a work (e.g., imprisonment/freedom motif in Jane Eyre). Symbols can become motifs if repeated.'),
   p('What is the "unreliable narrator"? Identify the signs of unreliability in a narrator.','Think: can we trust what the narrator tells us?',
     'An unreliable narrator cannot be fully trusted — their account may be biased, mistaken, or deliberately deceptive. Signs: contradictions in their account, other characters disagreeing with them, information withheld, self-serving justifications, limited understanding of events. Examples: Nick in Gatsby, Stevens in Remains of the Day.')]  ,
  'AP Literature Essay Writing',
  [p('What is the AP Literature exam\'s "Q3" free response (open question)? How should you approach it?','Think: choose your own text, argue a theme',
     'Q3 is an open-ended prompt asking you to use a literary work of your choice to argue a complex idea. Approach: choose a text you know deeply (usually a novel or play), identify a specific thematic argument, use textual evidence with analysis. Judges are looking for sophisticated argument and specific, accurate literary analysis — not plot summary.'),
   p('What makes an AP Literature thesis "sophisticated" vs. "acceptable"?','Think: complexity, nuance, tension',
     'Acceptable thesis: "In Hamlet, Shakespeare shows that revenge is destructive." Sophisticated: "Though Hamlet frames his revenge as justice, Shakespeare reveals that his delay exposes a deeper paralysis — not moral scruple, but a self-destructive inability to act that makes him complicit in the tragedy he seeks to prevent." Sophistication = acknowledge complexity and tension.'),
   p('What is the "so what?" question in literary analysis? How do you ensure your essay answers it?','Think: why does this matter? what\'s the larger significance?',
     'The "so what?" question asks: why does this theme/technique/character matter beyond this text? What does it reveal about human experience, society, or a universal truth? Answer it by: connecting your analysis to a broader idea in your thesis and conclusion. "This shows not just what Hamlet does, but what Shakespeare believed about the human capacity for self-deception."'),
   p('What is the difference between a prose analysis essay and a poetry analysis essay on the AP exam?','Think: both use close reading but have different forms',
     'Prose: longer passage, analyze narrator\'s choices, characterization, structure, dialogue. Poetry: shorter text, analyze voice, sound (rhyme, meter, assonance), syntax (line breaks, enjambment), imagery, and figurative language. Both require a central argument about the effect/meaning, not line-by-line paraphrase. Poetry analysis must address form as meaning.')]
);

// Grade 12 ELA[2] = College Writing Preparation
PRACTICE[12].ela[2] = u(
  'The College Essay & Personal Statement',
  [p('What makes a strong Common App personal statement? What should it definitely NOT do?','Think: specific, genuine, reflective',
     'Strong elements: specific narrative (not general claims), reveals genuine personality, shows growth or self-awareness, uses vivid detail, has a clear "so what?" reflection. Should NOT: summarize your resume, list achievements without story, exaggerate, use clichés ("I want to be a doctor to help people"), or try to impress with vocabulary.'),
   p('What is "showing vs. telling" in college essays? Rewrite: "I am a hardworking and dedicated student."','Think: demonstrate through story, not assertion',
     '"Showing" demonstrates qualities through specific story, action, and detail rather than stating them. Rewrite example: "At 2am, after my fifth attempt to debug the same loop error, I finally traced it to a misplaced semicolon — and felt more satisfied than I ever had on a graded assignment." This shows dedication without claiming it.'),
   p('What are supplemental essays? What common types do colleges ask for?','Think: school-specific essays after the main application',
     'Supplemental essays are additional essays required by specific colleges beyond the main application. Common types: "Why this college?" (demonstrate genuine interest and research), "Why this major?" (explain your intellectual journey), Community/identity essays, Creative/unusual prompts. Each requires genuine research and specificity.'),
   p('What is a "pivot" in a college essay? Why is it important?','Think: the shift from story to reflection',
     'The pivot is the moment in the essay where the writer shifts from narrating an experience to reflecting on what it reveals about them — the "so what?" moment. It connects the specific story to universal significance or growth. Essays without a strong pivot feel like anecdotes; pivots turn them into meaningful self-revelations.')]  ,
  'Academic Writing & Citation',
  [p('What is MLA format? When do you use it and what are its key elements?','Think: Modern Language Association — humanities',
     'MLA format is used in humanities (English, history, arts). Key elements: 12pt Times New Roman, 1" margins, last name + page number header, centered title, double-spaced, Works Cited (not References) page. In-text citations: (Author page#) — e.g., (Smith 45). No comma between author and page.'),
   p('What is APA format? When do you use it and how does it differ from MLA?','Think: American Psychological Association — sciences and social sciences',
     'APA format is used in social sciences, sciences, education, psychology. Key differences from MLA: Reference list (not Works Cited), in-text citations include year (Smith, 2021, p. 45), abstract page, running head. APA emphasizes publication date because currency matters more in sciences. Title page required.'),
   p('What is a thesis-driven argument in academic writing? How does it differ from a topic-based paper?','Think: argument vs. overview',
     'A thesis-driven paper takes a specific, arguable position and defends it with evidence throughout. A topic-based paper summarizes information about a subject without arguing a specific point. College-level writing requires thesis-driven work: "Social media algorithms are designed to maximize engagement at the expense of users\' mental health" vs. "This paper is about social media."'),
   p('What is a "scholarly conversation" and how do college papers enter it?','Think: academic writing responds to existing scholarship',
     'Academic scholarship is ongoing — scholars respond to, build on, and challenge each other\'s work. A college paper enters the conversation by: citing relevant scholarship (showing you know the field), identifying a gap or disagreement in the literature, and contributing your own argument that responds to existing positions. You\'re not writing in a vacuum — you\'re adding to the dialogue.')]
);

// Grade 12 History[1] = AP Government & Politics
PRACTICE[12].history[1] = u(
  'Constitutional Foundations & Institutions',
  [p('What are the five key principles of the U.S. Constitution? Briefly explain each.','Think: popular sovereignty, limited government, separation of powers, checks and balances, federalism',
     'Popular sovereignty: government power comes from the people. Limited government: government can only do what the Constitution permits. Separation of powers: power divided among three branches. Checks and balances: each branch limits the others. Federalism: power shared between national and state governments.'),
   p('What is judicial review? Where does it come from, and why is it significant?','Think: Marbury v. Madison (1803)',
     'Judicial review: the Supreme Court\'s power to strike down laws that violate the Constitution. Established in Marbury v. Madison (1803) by Chief Justice John Marshall — not explicitly in the Constitution itself. Significance: makes the judiciary a co-equal branch and ultimate interpreter of the Constitution, giving it enormous long-term power.'),
   p('What is the difference between expressed, implied, and reserved powers?','Think: enumerated vs. necessary and proper vs. 10th Amendment',
     'Expressed (enumerated): powers explicitly listed in the Constitution (Congress can declare war, coin money). Implied: powers not stated but reasonably inferred via Necessary and Proper Clause (Congress can create a national bank). Reserved: powers not granted to the federal government belong to states (10th Amendment) — education, criminal law, elections.'),
   p('How does the Electoral College work? What are the main criticisms of the system?','Think: winner-take-all states; 270 to win',
     'Each state gets electoral votes equal to its Congressional representation. Most states use winner-take-all: the candidate winning the state\'s popular vote gets all electoral votes. 270 of 538 needed to win. Criticisms: candidates focus only on swing states, popular vote winner can lose (2000, 2016), small states have disproportionate power, faithless electors.')]  ,
  'Political Participation & Public Policy',
  [p('What factors affect voter turnout in the U.S.? Why is U.S. turnout lower than in other democracies?','Think: registration, barriers, education, interest',
     'Factors affecting turnout: education (more educated → higher turnout), registration requirements (U.S. requires prior registration; other nations auto-register), voter ID laws, Election Day (Tuesday vs. holiday), civic engagement. U.S. turnout (~55–60% in presidential years) is lower than most established democracies.'),
   p('What is the role of interest groups in U.S. politics? How do they differ from political parties?','Think: organized advocacy vs. political organization',
     'Interest groups: organizations advocating for specific policies (AARP, NRA, Sierra Club). They lobby Congress, donate to campaigns (PACs, Super PACs), and mobilize voters. Unlike parties, they don\'t run candidates. Parties: broad coalitions that run candidates and seek to control government. Interest groups can influence both parties.'),
   p('What is the difference between distributive, regulatory, and redistributive public policy? Give one example of each.','Think: who gets what, who is controlled, who pays for whom',
     'Distributive: benefits distributed to many groups (highway construction, farm subsidies, research grants). Regulatory: government sets rules limiting certain behaviors (Clean Air Act, FDA drug approval). Redistributive: transfers resources from one group to another (Social Security, Medicaid, progressive taxation).'),
   p('What is the iron triangle in U.S. policymaking? Give one example.','Think: agencies, committees, interest groups in a closed policymaking loop',
     'Iron triangle: a stable relationship among a congressional committee, a federal agency, and an interest group that together control policy in a specific area. Example: The Senate Agriculture Committee + USDA + farm lobbies (American Farm Bureau) coordinate to craft farm policy that benefits agriculture — largely insulated from public scrutiny.')]
);

// Grade 12 History[2] = Philosophy & Ethics Intro
PRACTICE[12].history[2] = u(
  'Major Ethical Theories',
  [p('What is utilitarianism? Who are its key founders? Apply it to one ethical dilemma.','Think: greatest good for greatest number',
     'Utilitarianism (Bentham, Mill): an action is right if it maximizes overall happiness/welfare. Applied to trolley problem: pull the lever to divert the trolley — kill 1 to save 5. Utilitarian calculus: 5 lives outweigh 1. Criticisms: can justify harming minorities for majority benefit; hard to calculate consequences.'),
   p('What is Kantian ethics (deontology)? What is the Categorical Imperative?','Think: duty-based; act on universal principles',
     'Kant: morality is based on duty and universal rules, not consequences. Categorical Imperative: (1) Universal Law: "Act only according to maxims you could will to be universal laws." (2) Humanity Formula: "Always treat people as ends in themselves, never merely as means." Applied to lying: lying cannot be universalized → always wrong, even to save a life.'),
   p('What is virtue ethics? How does it differ from utilitarianism and Kantian ethics?','Think: focus on character, not acts or consequences',
     'Virtue ethics (Aristotle): morality is about developing virtuous character traits (courage, honesty, justice, temperance). Not "what should I do?" but "what kind of person should I be?" Differs from utilitarianism (focuses on consequences) and Kant (focuses on duty). A virtuous person will naturally make good moral decisions.'),
   p('What is John Rawls\'s "veil of ignorance"? How does it help design a just society?','Think: design society without knowing your place in it',
     'Rawls: to design a just society, imagine you don\'t know your position — your race, class, gender, talents, or birth circumstances. From behind this "veil of ignorance," rational people would choose principles ensuring fairness for the worst-off, since they might be in that position. Leads to the Difference Principle: inequalities are acceptable only if they benefit the least advantaged.')]  ,
  'Applied Ethics & Moral Reasoning',
  [p('What is bioethics? Name two bioethical dilemmas and the ethical theories most relevant to each.','Think: ethics applied to medicine and biology',
     'Bioethics applies ethical reasoning to biology and medicine. (1) Euthanasia/physician-assisted dying: autonomy rights (libertarian/Kantian) vs. sanctity of life (deontological) vs. reducing suffering (utilitarian). (2) Genetic engineering of embryos: benefits to future generations (utilitarian) vs. playing God concerns (deontological) vs. justice (who has access?).'),
   p('What is the difference between moral relativism and moral universalism? Which better explains human rights?','Think: morality as cultural vs. morality as objective',
     'Moral relativism: moral truths are relative to culture or individual — no universal standards. Moral universalism: some moral truths apply to all humans regardless of culture (e.g., genocide is always wrong). Human rights theory requires universalism — rights derive from humanity, not cultural agreement. Relativism risks excusing human rights abuses as "culturally appropriate."'),
   p('What is civil disobedience? Using Rawls, King, or Thoreau, explain when it is justified.','Think: deliberate law-breaking to protest injustice',
     'Civil disobedience: deliberate, nonviolent violation of law to protest injustice. Thoreau (1849): unjust laws have no moral authority; conscience must override law. King (Letter from Birmingham Jail): openly, nonviolently break unjust laws and accept punishment to demonstrate injustice. Rawls: civil disobedience is justified in a nearly just society when legal channels are exhausted and injustice is substantial.'),
   p('What is the "trolley problem"? What does it reveal about the difference between consequentialist and deontological ethics?','Think: classic ethical thought experiment',
     'Trolley problem: a runaway trolley will kill 5 people; you can divert it to kill 1. Most pull the lever (utilitarian — save more lives). But many refuse to push a large man off a bridge to stop the trolley, even though it would also save 5. This distinction reveals: utilitarianism permits using people as means; deontology (Kant) forbids it regardless of outcome.')]
);

// Grade 12 CS[1] = Career & College Readiness in CS
PRACTICE[12].cs[1] = u(
  'CS Career Paths & Portfolio',
  [p('What are five distinct career paths in computer science? Describe each in one sentence.','Think: beyond "software engineer"',
     '(1) Software Engineer: designs and builds software applications. (2) Data Scientist: analyzes complex data to extract insights. (3) Cybersecurity Analyst: protects systems from attacks. (4) AI/ML Engineer: builds intelligent systems. (5) UX/Product Designer: designs user experience and interfaces. (6) Systems Administrator: manages IT infrastructure.'),
   p('What should a strong computer science portfolio include? Why is GitHub important?','Think: evidence of skills and learning',
     '3–5 projects with well-documented code and clear READMEs, a GitHub profile with active contributions and commit history, evidence of problem-solving (HackerRank, LeetCode), and a personal website. GitHub is the industry-standard platform for sharing code — employers use it to assess coding skills, collaboration, and work habits.'),
   p('What is the difference between a computer science degree and a coding bootcamp? When might you choose one over the other?','Think: depth vs. speed; theory vs. application',
     'CS degree (4 years): covers theory (algorithms, data structures, systems, math) alongside practical skills. Best for: research, systems engineering, wanting maximum flexibility, graduate school. Bootcamp (3–6 months): intensive, practical, focuses on web development. Best for: career change, faster entry to software roles, entrepreneurship. Both are valid paths.'),
   p('What are the three most important soft skills for a CS professional, and why?','Think: beyond coding ability',
     '(1) Communication: explain technical concepts to non-technical stakeholders; write clear documentation. (2) Collaboration: most software is built in teams using Git — teamwork and code review skills are essential. (3) Problem decomposition: breaking complex problems into manageable parts is the core cognitive skill of engineering. Technical ability alone is insufficient in professional settings.')]  ,
  'Technical Interview & CS Fundamentals Review',
  [p('What is Big O notation? Give the Big O of: accessing an array element, linear search, binary search, and bubble sort.','Think: measure of algorithmic efficiency',
     'Big O describes how an algorithm\'s time/space scales with input size. Array access: O(1) — constant. Linear search: O(n) — grows linearly. Binary search: O(log n) — very efficient on sorted data. Bubble sort: O(n²) — inefficient for large datasets. Technical interviews commonly ask candidates to identify and optimize Big O.'),
   p('What is the difference between a stack and a queue? Give one real-world analogy for each.','Think: LIFO vs. FIFO',
     'Stack: Last In, First Out (LIFO). Analogy: stack of plates — you add and remove from the top. Used in: function call stacks, undo operations, recursion. Queue: First In, First Out (FIFO). Analogy: line at a grocery store — first in is first served. Used in: print queues, BFS graph traversal, scheduling.'),
   p('What is recursion? Write a recursive function (in pseudocode) to compute n factorial.','Think: function calling itself with a base case',
     'Recursion: a function that calls itself with a simpler version of the problem. Base case prevents infinite recursion. Pseudocode: function factorial(n): if n == 0 return 1; else return n * factorial(n-1). factorial(5) = 5 × 4 × 3 × 2 × 1 = 120. Each call reduces n by 1 until reaching base case 0.'),
   p('What is an API? How does it enable software applications to communicate?','Think: Application Programming Interface — a contract between systems',
     'An API is a set of defined rules specifying how software components communicate. A REST API uses HTTP requests (GET, POST, PUT, DELETE) to retrieve or modify data. Example: when you log in with Google, the app calls Google\'s OAuth API. APIs allow different systems to work together without exposing internal code.')]
);

// Grade 12 Health[1] = Senior Capstone
PRACTICE[12].health[1] = u(
  'Designing a Personal Wellness Plan',
  [p('What are the 8 dimensions of wellness? Give one action step for each.','Think: holistic health beyond physical',
     'Physical: exercise 150 min/week. Emotional: journal daily. Social: schedule weekly time with friends. Intellectual: read or learn something new daily. Spiritual: meditate or reflect on values. Environmental: reduce single-use plastic. Occupational: align work with strengths. Financial: create a monthly budget. Wellness is multidimensional.'),
   p('What is a SMART goal? Write one SMART wellness goal for yourself.','Think: Specific, Measurable, Achievable, Relevant, Time-bound',
     'SMART goal example: "I will walk 30 minutes at least 4 days per week for the next 8 weeks to improve my cardiovascular fitness, starting this Monday." Generic goal ("I want to exercise more") fails because it lacks measurement, timeline, and specificity. SMART goals dramatically increase follow-through.'),
   p('What is the difference between intrinsic and extrinsic motivation in health behavior change? Which is more sustainable?','Think: internal vs. external reward',
     'Extrinsic: motivated by external rewards (lose weight to look good, exercise to win a bet). Intrinsic: motivated by internal satisfaction (exercise because you enjoy it and feel energized). Research consistently shows intrinsic motivation leads to more sustained behavior change. Find the "why" that is meaningful to YOU.'),
   p('What are two evidence-based strategies for managing chronic stress?','Think: proven, not just popular',
     'Evidence-based strategies: (1) Mindfulness-based stress reduction (MBSR): structured program combining meditation and body awareness — shown to reduce cortisol and anxiety in multiple meta-analyses. (2) Regular aerobic exercise: reduces stress hormones, increases endorphins, improves sleep quality. Both require practice and consistency, not quick fixes.')]  ,
  'Health Advocacy & Community Wellness',
  [p('What is community health advocacy? Give one example of a student-level advocacy action.','Think: speaking up for health at the community level',
     'Community health advocacy involves working to improve health conditions, policies, or resources for a community — beyond individual behaviors. Student example: researching mental health resource gaps at school, presenting findings to administrators, and proposing a peer support program. Start local: school, neighborhood, or city council.'),
   p('What is health equity? How is it different from health equality?','Think: same treatment vs. what each person needs',
     'Equality: everyone gets the same resources. Equity: everyone gets what they need to achieve the same outcome. A short person and tall person both need to see over a fence — giving them both the same size box (equality) doesn\'t work; the short person needs a bigger box (equity). Health equity addresses systemic disparities in health access and outcomes.'),
   p('Describe one major public health achievement in the 20th century and explain how it improved population health.','Think: vaccines, sanitation, tobacco reduction, seat belts...',
     'Vaccination programs: smallpox (eradicated 1980), polio (near-eradicated globally), and routine childhood vaccines dramatically reduced childhood mortality worldwide. Before vaccines, measles killed ~2.6 million annually; now deaths are rare in countries with high vaccination rates. This is one of the greatest public health achievements in human history.'),
   p('As you graduate, what is one health habit you want to maintain and one you want to change? How will you use the SMART framework to do so?','Think: self-reflection + concrete planning',
     'Personal answer — but structure matters: For the habit to MAINTAIN: identify what makes it stick (schedule, social support, enjoyment) and commit to protecting it during life transitions. For the habit to CHANGE: write a SMART goal identifying: specific change, how to measure it, realistic target, personal importance, and deadline. Revisit monthly.')]
);

console.log('Grade 12 complete — all 51 done!');

// Now verify all missing entries are filled
const grades = [6,7,8,9,10,11,12];
const SUBJECTS2 = [{id:'math'},{id:'science'},{id:'ela'},{id:'history'},{id:'cs'},{id:'health'}];
let stillMissing = 0;
grades.forEach(g => {
  SUBJECTS2.forEach(s => {
    const practUnits = (PRACTICE[g]?.[s.id] || []).length;
    const currUnits = (CURRICULUM[g][s.id] || []).length;
    if (practUnits < currUnits) {
      stillMissing++;
      console.log(`  STILL MISSING: Grade ${g} ${s.id} - has ${practUnits}, needs ${currUnits}`);
    }
  });
});
if (stillMissing === 0) console.log('All units covered!');

// Fix: Grade 9 history[1] was combining two separate units
// Split into history[1] (Global Economics) and history[2] (Government & Civics)
PRACTICE[9].history[1] = u(
  'Economic Systems & Trade',
  [p('What are the four main types of economic systems? Briefly describe each.','Think: who controls the economy?',
     'Traditional: based on customs/habits (subsistence farming). Command: government controls production and distribution. Market: supply and demand drives private decisions (U.S.). Mixed: blend of market and government involvement (most modern economies blend the two).'),
   p('What is comparative advantage? How does it explain why countries trade?','Think: produce what you\'re relatively best at, even if not absolutely best',
     'Comparative advantage: a country should produce goods at which it has the lowest opportunity cost, even if another country is absolutely better at producing everything. Example: If Country A is better at cars and electronics, but relatively much better at cars, it should specialize in cars and trade for electronics.'),
   p('What is the difference between imports and exports? How do they affect a country\'s trade balance?','Think: buying vs. selling internationally',
     'Exports: goods/services sold to other countries. Imports: goods/services bought from other countries. Trade surplus: exports > imports (net seller). Trade deficit: imports > exports (net buyer). The U.S. runs a persistent trade deficit, buying more from the world than it sells.'),
   p('What is globalization? Describe one benefit and one criticism.','Think: interconnected world economy',
     'Globalization: increasing economic, cultural, and political interconnection across countries. Benefit: lower prices for consumers, access to global markets, cross-cultural exchange. Criticism: job outsourcing to low-wage countries, exploitation of workers in developing nations, weakening of local cultures and industries.')],
  'International Economic Organizations',
  [p('What is the World Trade Organization (WTO)? What does it do?','Think: global rule-setter for international trade',
     'The WTO is an international organization that sets the rules for global trade, settles trade disputes between nations, and works to reduce trade barriers (tariffs, quotas). It has 164 member nations representing 98% of global trade. Critics: too favorable to wealthy nations; undermines labor and environmental standards.'),
   p('What is the International Monetary Fund (IMF)? When do countries turn to it?','Think: global financial crisis lender',
     'The IMF monitors the global economy, provides financial assistance to countries in economic crisis (balance of payments problems), and offers technical advice. Countries turn to the IMF when they cannot pay debts or stabilize their currency. IMF loans often come with conditions requiring economic reforms (austerity).'),
   p('What is the difference between free trade and protectionism? What are the arguments for each?','Think: open vs. restricted trade',
     'Free trade: no barriers to international trade (WTO goal). Arguments: lower prices, efficiency, innovation. Protectionism: tariffs, quotas, subsidies to protect domestic industries. Arguments: protects jobs, safeguards strategic industries (defense), prevents unfair foreign competition (dumping). Most nations practice a mix of both.'),
   p('What are tariffs and how do they affect consumers and domestic producers?','Think: tax on imports; winners and losers',
     'A tariff is a tax on imported goods. Effect on consumers: higher prices (they pay more for imported goods). Effect on domestic producers: protected from foreign competition → may keep their prices high but keep their jobs/market share. Tariffs redistribute wealth from consumers to producers and government.')]
);

PRACTICE[9].history[2] = u(
  'Types of Government',
  [p('What is the difference between a democracy, an oligarchy, and an autocracy?','Think: who holds power?',
     'Democracy: power held by the people (direct or representative). Oligarchy: small elite group holds power (military, wealthy, single party). Autocracy: one person holds unlimited power (dictator, absolute monarch). Most modern governments combine elements — e.g., a republic is a representative democracy with constitutional limits.'),
   p('What are the key features of a constitutional democracy?','Think: rule of law, rights, elections, separation of powers',
     'Constitutional democracy features: written constitution limiting government power, regular free and fair elections, protection of individual rights, rule of law (no one above the law), separation of powers, independent judiciary, and free press. These features together prevent tyranny and protect citizens.'),
   p('What is totalitarianism? How does it differ from authoritarianism?','Think: total control vs. political control',
     'Authoritarianism: government controls political life but may allow some economic freedom and private life. Totalitarianism: government seeks to control ALL aspects of life — politics, economy, culture, religion, family, thought. Examples: North Korea (total), Putin\'s Russia (authoritarian). Totalitarianism requires active participation in state ideology.'),
   p('What is the difference between a federal and unitary system of government?','Think: where does power reside?',
     'Federal: power is constitutionally divided between central and regional governments (U.S., Germany, India). Unitary: power is concentrated in the central government; regional units are subordinate and can be created/dissolved by the center (France, UK, Japan). Federal systems protect regional diversity; unitary systems ensure national uniformity.')],
  'Rights, Responsibilities & Civic Participation',
  [p('What is the difference between civil liberties and civil rights?','Think: freedom from government interference vs. equal protection',
     'Civil liberties: negative freedoms protecting individuals FROM government interference (free speech, privacy, due process). Civil rights: positive rights ensuring EQUAL treatment regardless of race, gender, religion, disability (voting rights, equal access to services). The Bill of Rights protects civil liberties; the 14th Amendment and civil rights laws protect civil rights.'),
   p('What are the responsibilities of citizenship in a democracy?','Think: it\'s not just rights; it\'s duties',
     'Voting: informed participation in elections. Jury duty: serving when called. Paying taxes: funding public services. Obeying laws. Staying informed about public issues. Serving in the military if required. Optional but important: community service, civic engagement, advocating for change through legal means. Rights require responsibilities.'),
   p('What is the rule of law? Why is it the foundation of democracy?','Think: no one — not even the government — is above the law',
     'Rule of law: all people and institutions are subject to and accountable under the law, equally applied and independently adjudicated. It prevents arbitrary government power, ensures equal justice, protects individual rights, and creates predictability. Without it, government becomes tyranny — leaders can act without legal accountability.'),
   p('How can citizens participate in government beyond voting? Name three methods.','Think: democracy is more than elections',
     '(1) Contacting elected representatives (calls, letters, town halls). (2) Joining community organizations or interest groups. (3) Running for local office or serving on boards. (4) Peaceful protest and civil disobedience. (5) Signing/creating petitions. (6) Community organizing. Engaged citizens strengthen democracy between elections.')]
);

// Re-verify
const grades2 = [6,7,8,9,10,11,12];
const SUBJECTS3 = [{id:'math'},{id:'science'},{id:'ela'},{id:'history'},{id:'cs'},{id:'health'}];
let stillMissing2 = 0;
grades2.forEach(g => {
  SUBJECTS3.forEach(s => {
    const practUnits = (PRACTICE[g]?.[s.id] || []).length;
    const currUnits = (CURRICULUM[g][s.id] || []).length;
    if (practUnits < currUnits) {
      stillMissing2++;
      console.log(`  STILL MISSING: Grade ${g} ${s.id} - has ${practUnits}, needs ${currUnits}`);
    }
  });
});
if (stillMissing2 === 0) console.log('ALL 51+ UNITS COVERED!');


// Serialize PRACTICE back to JS source
function serializeProblems(problems) {
  return problems.map(p => {
    const q = JSON.stringify(p.q);
    const ex = JSON.stringify(p.ex);
    const a = JSON.stringify(p.a);
    return `        {q:${q},ex:${ex},a:${a}}`;
  }).join(',\n');
}

function serializeSheet(sheet) {
  return `{title:${JSON.stringify(sheet.title)},problems:[\n${serializeProblems(sheet.problems)},\n      ]}`;
}

function serializeUnit(sheets) {
  return `[${sheets.map(s => serializeSheet(s)).join(',')}]`;
}

function serializeSubject(units) {
  return units.map((u, i) => `    /* unit${i+1} */ ${serializeUnit(u)}`).join(',\n');
}

let output = 'const PRACTICE = {\n';
[6,7,8,9,10,11,12].forEach(g => {
  output += `  ${g}: {\n`;
  ['math','science','ela','history','cs','health'].forEach(s => {
    output += `    ${s}:[\n`;
    output += serializeSubject(PRACTICE[g][s]);
    output += `\n    ],\n`;
  });
  output += `  },\n`;
});
output += '};';

// Replace PRACTICE section in HTML
const practStart2 = html.indexOf('\nconst PRACTICE = {');
let depth3 = 0, inP3 = false, practEnd3 = practStart2;
for (let i = practStart2 + 1; i < html.length; i++) {
  if (html[i] === '{') { depth3++; inP3 = true; }
  if (html[i] === '}') depth3--;
  if (inP3 && depth3 === 0) { practEnd3 = i + 1; break; }
}

// Find exact start (skip the leading newline)
const newHtml = html.slice(0, practStart2 + 1) + output + html.slice(practEnd3);
fs.writeFileSync('/sessions/admiring-stoic-pascal/mnt/outputs/curriculum.html', newHtml);
console.log('File written. Size:', Math.round(newHtml.length / 1024), 'KB');
