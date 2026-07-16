/* AcerAcademy -- SUBJECTS / AP_SUBJECTS / CURRICULUM (unit+topic outline), shared by both index.html and curriculum.html as of 2026-07-16. Previously each file kept its own independent copy of this data and they had drifted apart in 10 places (differing units/topics for a handful of grade+subject combinations); index.html's version was chosen as canonical per explicit user decision, and both pages now load this single file instead of maintaining separate inline copies. */
// CURRICULUM DATA
// ----------------------------------------------
const SUBJECTS = [
  { id: 'math',     label: 'Mathematics',       color: '#2563eb' },
  { id: 'science',  label: 'Science',            color: '#16a34a' },
  { id: 'ela',      label: 'English Language Arts', color: '#9333ea' },
  { id: 'history',  label: 'History & Social Studies', color: '#ea580c' },
  { id: 'cs',       label: 'Computer Science',   color: '#0891b2' },
  { id: 'health',   label: 'Health & PE',         color: '#dc2626' },
];

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

const CURRICULUM = {
  'k': {
    math: [
      { unit: "Counting & Number Sense", topics: ["Counting objects to 20","Number recognition 0-20","One-to-one correspondence","Counting on and counting back","Ordering numbers"] },
      { unit: "Comparing Numbers", topics: ["More, less, and equal","Comparing groups of objects","Comparing lengths and heights","Comparing weights"] },
      { unit: "Shapes & Spatial Sense", topics: ["2D shapes","3D shapes","Positional words","Sorting and classifying shapes"] },
      { unit: "Addition & Subtraction Within 10", topics: ["Combining sets (addition)","Taking away (subtraction)","Making 10","Addition and subtraction word problems"] },
      { unit: "Patterns, Data & Time", topics: ["Simple patterns (AB, ABC)","Picture graphs and counting data","Telling time basics (day parts)","Recognizing coins (penny, nickel, dime)"] },
    ],
    science: [
      { unit: "My Senses & My Body", topics: ["The five senses","Body parts basics"] },
      { unit: "Living Things: Animals", topics: ["Living vs. nonliving things","Animal needs","Animal babies, parents, and sounds","Animal habitats basics"] },
      { unit: "Living Things: Plants", topics: ["Plant parts","What plants need to grow","Plant life cycle basics"] },
      { unit: "Weather & Earth", topics: ["Weather types","Seasons and their signs","Day and night","The sun's light and heat","Push and pull forces","Materials and their properties","Caring for the Earth"] },
    ],
    ela: [
      { unit: "Letters & Sounds", topics: ["Uppercase letter names","Lowercase letter names","Letter sounds","Beginning sounds","Rhyming words"] },
      { unit: "Sight Words & Vocabulary", topics: ["Sight words: the, and, is, see","Sight words: a, I, my, like","Opposites"] },
      { unit: "Sentences & Print", topics: ["What a sentence is","Print concepts (left to right, top to bottom)","Letter formation"] },
      { unit: "Stories", topics: ["Story characters","Story setting","Beginning, middle, and end"] },
      { unit: "Sounds & Syllables", topics: ["Syllables (clapping words)","Blending sounds","Segmenting sounds","Ending sounds"] },
    ],
    history: [
      { unit: "Family & Community", topics: ["Family members and roles","Community helpers and their jobs","Rules at home and school"] },
      { unit: "Citizenship & Symbols", topics: ["The American flag","National holidays and their meaning","Being a good citizen/helper","Feelings and getting along with others","Sharing and taking turns"] },
      { unit: "Maps & Time", topics: ["What a map is","Comparing long ago and now","Needs vs. wants basics","Where we live"] },
    ],
    cs: [
      { unit: "Using a Computer", topics: ["Parts of a computer","What a computer can do","Turning a device on and off safely","Being kind when using a device"] },
      { unit: "Thinking Like a Computer", topics: ["Step-by-step directions (algorithms)","What a robot is","Patterns and sequences","Asking a grown-up before going online","Following instructions in order"] },
    ],
    health: [
      { unit: "Staying Healthy", topics: ["Handwashing","Brushing teeth","Healthy foods vs. treats","Staying active and exercise","Getting enough sleep"] },
      { unit: "Staying Safe", topics: ["Body parts","Safety rules","Naming feelings and emotions","Calling 911 for help"] },
    ],
  },
  1: {
    math: [
      { unit: "Addition & Subtraction Within 20", topics: ["Addition fact families","Doubles and near-doubles","Subtraction within 20","Addition and subtraction word problems","Counting to 120"] },
      { unit: "Place Value", topics: ["Tens and ones","Comparing two-digit numbers","Skip counting by 2s, 5s, and 10s","Comparing three numbers"] },
      { unit: "Measurement & Time", topics: ["Measuring length with nonstandard units","Measuring length with standard units","Telling time to the hour","Telling time to the half hour"] },
      { unit: "Geometry", topics: ["2D shapes and attributes","3D shapes","Simple fractions (halves and fourths)","Equal shares"] },
      { unit: "Money & Data", topics: ["Identifying coins","Coin values","Tally charts","Simple graphs"] },
    ],
    science: [
      { unit: "Plants", topics: ["Plant needs and parts","Plant life cycle","Parts of a seed"] },
      { unit: "Animals", topics: ["Animal life cycles","Animal habitats and adaptations","Animal coverings and body parts"] },
      { unit: "Matter & Energy", topics: ["States of matter","Sound: how it's made","Light and shadows","Push and pull forces","Magnets"] },
      { unit: "Weather & Sky", topics: ["Weather patterns and tools","How seasons affect living things","Day and night and the sun's path","The moon and stars"] },
    ],
    ela: [
      { unit: "Phonics", topics: ["Short vowel sounds","Long vowel sounds","Consonant blends","Consonant digraphs","R-controlled vowels basics"] },
      { unit: "Sight Words & Vocabulary", topics: ["Grade 1 sight words","Compound words","Contractions basics"] },
      { unit: "Grammar & Mechanics", topics: ["Nouns","Verbs","Complete sentences vs. fragments","Capitalization and punctuation basics"] },
      { unit: "Reading Comprehension", topics: ["Story elements: setting and character","Problem and solution","Main idea","Sequencing events"] },
      { unit: "Word Study", topics: ["Syllables","Rhyming word families","Prefixes basics"] },
    ],
    history: [
      { unit: "Communities", topics: ["Community helpers and their tools","Goods and services","Needs vs. wants","Rules and laws and consequences"] },
      { unit: "Maps & Symbols", topics: ["Map basics (map key and legend)","Globes vs. maps and simple directions","American symbols and landmarks"] },
      { unit: "Past & Present", topics: ["National holidays and their meaning","Transportation long ago vs. now","Communication long ago vs. now","School long ago vs. now","Being a good citizen"] },
    ],
    cs: [
      { unit: "Computers & Devices", topics: ["Computer hardware parts","Input vs. output devices","Basic keyboard/typing familiarity","What apps and programs do"] },
      { unit: "Thinking Like a Computer", topics: ["Following step-by-step directions","Sequencing events in order","Simple if/then decision thinking","Internet safety basics","Being a responsible digital citizen"] },
    ],
    health: [
      { unit: "Healthy Habits", topics: ["Food groups and healthy eating","Personal hygiene routines","Exercise and physical activity","Sleep habits","Dental care"] },
      { unit: "Safety & Feelings", topics: ["Safety rules (streets, bikes, fire)","Germs and staying healthy","Emotions and how to express them","The five senses and body parts review","Stranger safety"] },
    ],
  },
  2: {
    math: [
      { unit: "Addition & Subtraction Within 100", topics: ["Addition with regrouping","Subtraction with regrouping","Two-step word problems","3-digit addition/subtraction basics","Estimating sums and differences"] },
      { unit: "Place Value", topics: ["Place value to hundreds","Comparing three-digit numbers","Skip counting","Odd and even numbers"] },
      { unit: "Measurement, Money & Time", topics: ["Measuring length in inches and feet","Measuring length in centimeters and meters","Telling time to 5-minute intervals","Counting money and making change","Comparing amounts of money"] },
      { unit: "Geometry & Fractions", topics: ["2D and 3D shape attributes","Partitioning shapes into equal parts","Fractions of a whole and a set"] },
      { unit: "Multiplication Foundations & Data", topics: ["Arrays and repeated addition","Bar graphs","Picture graphs"] },
    ],
    science: [
      { unit: "Life Cycles & Habitats", topics: ["Life cycles of animals","Habitats around the world","Plant and animal adaptations for survival","Food chains basics"] },
      { unit: "Matter", topics: ["States of matter","Changes in matter (melting, freezing, evaporation)","Mixtures and solutions basics"] },
      { unit: "Earth Science", topics: ["Earth's materials (rocks, soil, water)","The water cycle basics","Weather instruments and patterns"] },
      { unit: "Forces, Energy & Machines", topics: ["Force and motion basics","Energy sources (sun, wind, water)","Simple machines: lever and pulley","Simple machines: inclined plane, wedge, and screw","Simple machines: wheel and axle"] },
    ],
    ela: [
      { unit: "Grammar", topics: ["Nouns, adjectives, and verbs","Plural nouns","Compound words","Contractions","Pronouns basics"] },
      { unit: "Vocabulary", topics: ["Synonyms and antonyms","Context clues basics","Prefixes and suffixes basics"] },
      { unit: "Spelling & Mechanics", topics: ["Long vowel teams","Silent e patterns","Capitalization and punctuation rules"] },
      { unit: "Reading Comprehension", topics: ["Story elements: plot and theme basics","Main idea and supporting details","Sequencing events","Fact vs. opinion","Comparing and contrasting characters"] },
      { unit: "Reading Strategies", topics: ["Predicting","Questioning while reading","Summarizing basics"] },
    ],
    history: [
      { unit: "Communities & Government", topics: ["Local government basics","Communities: urban, suburban, rural","Rules, laws, and citizenship","Immigration and diverse cultures basics","Being a responsible citizen"] },
      { unit: "Economics", topics: ["Goods and services","Producers and consumers","Needs vs. wants review"] },
      { unit: "Geography & Symbols", topics: ["Map skills: cardinal directions","Map key and compass rose","US symbols and monuments","National holidays and historical figures","Comparing communities around the world"] },
    ],
    cs: [
      { unit: "Computers & the Internet", topics: ["Input and output devices","Typing and keyboard basics","What the internet is","Software vs. hardware basics"] },
      { unit: "Coding & Safety", topics: ["Sequencing and algorithms","Loops as repeated steps","Debugging as fixing mistakes","Internet safety and digital citizenship","Saving and organizing files basics"] },
    ],
    health: [
      { unit: "Nutrition & Fitness", topics: ["Nutrition and food groups","Physical activity and exercise benefits","Body systems intro: skeleton and muscles","Personal hygiene"] },
      { unit: "Safety & Wellness", topics: ["Safety rules: bike and pedestrian","Fire and poison safety","Germs and disease prevention","Emotions and friendship skills","Sleep and rest importance"] },
    ],
  },
  3: {
    math: [
      { unit: "Multiplication & Division", topics: ["Multiplication facts 0-10","Multiplying by multiples of 10","Division facts and the relationship to multiplication","Multiplication word problems","Division word problems"] },
      { unit: "Fractions", topics: ["Understanding fractions as parts of a whole","Fractions on a number line","Equivalent fractions","Comparing fractions","Mixed numbers basics"] },
      { unit: "Place Value & Rounding", topics: ["Place value to thousands","Comparing multi-digit numbers","Rounding to the nearest 10","Rounding to the nearest 100"] },
      { unit: "Measurement & Geometry", topics: ["Area","Perimeter","Elapsed time","Liquid volume and mass","Classifying quadrilaterals"] },
      { unit: "Data & Patterns", topics: ["Bar graphs and pictographs","Patterns in numbers and tables","Line plots"] },
    ],
    science: [
      { unit: "Life Cycles & Ecosystems", topics: ["Life cycles and metamorphosis","Ecosystems and food chains","Plant and animal adaptations","Habitats and biomes"] },
      { unit: "Matter & Forces", topics: ["States of matter and physical changes","Forces and motion: gravity","Forces and motion: friction","Balanced and unbalanced forces"] },
      { unit: "Earth Science", topics: ["Weather vs. climate","The water cycle in detail","Earth's structure: layers","Rocks and minerals basics"] },
      { unit: "Space & Machines", topics: ["The solar system intro","Simple machines and mechanical advantage","Phases of the moon basics","Day and night causes"] },
    ],
    ela: [
      { unit: "Grammar", topics: ["Nouns, verbs, adjectives, adverbs","Pronouns","Subject-verb agreement basics","Types of sentences"] },
      { unit: "Vocabulary", topics: ["Context clues","Prefixes","Suffixes","Dictionary and glossary use"] },
      { unit: "Reading Comprehension", topics: ["Main idea and key details","Text structure: compare and contrast","Text structure: cause and effect","Summarizing","Point of view basics"] },
      { unit: "Figurative Language & Writing", topics: ["Simile and metaphor basics","Research skills basics","Writing a paragraph","Persuasive writing basics"] },
      { unit: "Mechanics", topics: ["Commas","Quotation marks basics","Capitalization review"] },
    ],
    history: [
      { unit: "Government & Citizenship", topics: ["Local government basics","State government basics","Citizenship rights and responsibilities"] },
      { unit: "Economics", topics: ["Goods and services review","Supply and demand intro","Scarcity","Opportunity cost intro"] },
      { unit: "Geography & Culture", topics: ["Map skills: latitude and longitude intro","Map scale","Regions of the United States","Colonial life basics","Cultures and traditions around the world","Natural resources and conservation"] },
    ],
    cs: [
      { unit: "Computer Basics", topics: ["Hardware vs. software","Basic typing skills","How the internet connects devices","Using search engines responsibly"] },
      { unit: "Coding Concepts", topics: ["Coding vocabulary: sequence, loop, algorithm","Debugging as a concept","Intro to block-based coding: sprites and blocks","Digital citizenship and online safety","Event-based programming basics"] },
    ],
    health: [
      { unit: "Body & Nutrition", topics: ["Nutrition and balanced meals","Digestive system basics","Respiratory system basics","Circulatory system basics"] },
      { unit: "Safety & Wellness", topics: ["Disease prevention: bacteria vs. viruses","Basic first aid","Physical fitness components","Personal hygiene","Emotional health and stress basics"] },
    ],
  },
  4: {
    math: [
      { unit: "Multiplication & Division", topics: ["Multi-digit multiplication","Multi-digit division","Interpreting remainders","Factors and multiples","Prime and composite numbers"] },
      { unit: "Fractions & Decimals", topics: ["Equivalent fractions","Fraction addition and subtraction with like denominators","Comparing fractions","Decimal place value","Comparing decimals","Relating fractions and decimals"] },
      { unit: "Geometry", topics: ["Angles and angle measurement","Classifying lines: parallel and perpendicular","Classifying triangles and quadrilaterals","Area and perimeter formulas","Symmetry basics"] },
      { unit: "Measurement & Data", topics: ["Customary unit conversions","Metric unit conversions","Line plots and interpreting data","Using data to solve problems"] },
      { unit: "Number Sense", topics: ["Rounding multi-digit numbers","Multi-step word problems","Multiplicative comparison"] },
    ],
    science: [
      { unit: "Ecosystems & Energy", topics: ["Ecosystems and food webs","Energy transfer in food webs","Producers, consumers, and decomposers review"] },
      { unit: "Matter & Energy", topics: ["States of matter and energy","Heat transfer and conduction","Light waves basics","Sound waves basics"] },
      { unit: "Earth Science", topics: ["The rock cycle","Erosion and weathering","The water cycle in depth","Weather patterns and climate zones"] },
      { unit: "Body Systems & Space", topics: ["Digestive, respiratory, and circulatory systems","Skeletal and muscular systems","Electricity basics","Magnetism basics","The solar system in depth","Moons and orbits"] },
    ],
    ela: [
      { unit: "Figurative Language", topics: ["Simile and metaphor","Personification","Idioms","Hyperbole basics","Onomatopoeia basics"] },
      { unit: "Text Structures", topics: ["Cause and effect","Compare and contrast","Sequence","Problem and solution"] },
      { unit: "Vocabulary", topics: ["Context clues","Greek and Latin roots intro","Prefixes and suffixes review","Multiple-meaning words"] },
      { unit: "Comprehension & Genre", topics: ["Main idea and theme","Narrative vs. informational text","Point of view basics","Summarizing longer texts","Comparing texts on the same topic"] },
      { unit: "Grammar & Writing", topics: ["Verb tenses","Subject-verb agreement","Commas in a series","Narrative writing","Opinion writing","Informative writing"] },
    ],
    history: [
      { unit: "Early America", topics: ["Age of Exploration","The 13 colonies","Colonial life and jobs","The American Revolution","Native American cultures before colonization"] },
      { unit: "Government", topics: ["Legislative branch","Executive branch","Judicial branch","US Constitution basics"] },
      { unit: "Geography", topics: ["US geography and regions","Regions and their resources","State history basics","Westward expansion intro"] },
      { unit: "Economics & Citizenship", topics: ["Scarcity and trade","Resources and supply/demand","Citizenship responsibilities"] },
    ],
    cs: [
      { unit: "Internet & Digital Citizenship", topics: ["Internet basics: websites and browsers","URLs and search engines","Online etiquette","Cyberbullying awareness","Hardware and software deep dive"] },
      { unit: "Coding Concepts", topics: ["Variables intro","Loops intro","Conditionals intro","Debugging strategies","Block-based programming: events and actions","Data and databases basics"] },
    ],
    health: [
      { unit: "Nutrition & Body Systems", topics: ["Reading food labels basics","Nervous system basics","Endocrine system basics","Immune system basics"] },
      { unit: "Safety & Wellness", topics: ["First aid: burns and cuts","First aid: choking basics","Physical fitness and goal setting","Stress management","Self-esteem","Tobacco and alcohol awareness","Personal hygiene and puberty intro"] },
    ],
  },
  5: {
    math: [
      { unit: "Fraction Operations", topics: ["Adding and subtracting fractions with unlike denominators","Multiplying fractions","Dividing fractions","Mixed number operations","Comparing and ordering fractions"] },
      { unit: "Decimal Operations", topics: ["Adding and subtracting decimals","Multiplying decimals","Dividing decimals","Estimating decimal computations"] },
      { unit: "Number Sense", topics: ["Order of operations (PEMDAS)","Prime and composite numbers","Factors, multiples, GCF, and LCM","Powers of 10 and exponents basics","Rounding decimals","Comparing large numbers"] },
      { unit: "Geometry & Measurement", topics: ["Volume of rectangular prisms","Coordinate plane: ordered pairs","Classifying 2D shapes by properties","Classifying triangles by angles"] },
      { unit: "Ratios & Percents", topics: ["Ratios intro","Rates and unit rates intro","Converting fractions, decimals, and percents intro"] },
      { unit: "Data", topics: ["Line plots with fractions","Interpreting data","Mean, median, mode, and range intro"] },
    ],
    science: [
      { unit: "Ecosystems", topics: ["Producers, consumers, and decomposers","Food webs and energy flow","Biomes and habitats review","Human impact on ecosystems"] },
      { unit: "Matter", topics: ["Physical vs. chemical changes","Chemical reactions basics","Mixtures and solutions","Properties of matter"] },
      { unit: "Earth & Space", topics: ["The solar system in depth","Phases of the moon","Causes of day and night","Causes of seasons","The water cycle and weather systems"] },
      { unit: "Body Systems & Method", topics: ["Nervous system","Endocrine system","Digestive, respiratory, and circulatory systems in depth","Forces and simple machines review","Scientific method: hypothesis and variables"] },
    ],
    ela: [
      { unit: "Figurative Language", topics: ["Simile and metaphor review","Personification","Hyperbole and idioms","Symbolism basics"] },
      { unit: "Text Structures & Nonfiction", topics: ["Nonfiction text features","Text structures review","Comparing informational texts","Author's purpose and perspective"] },
      { unit: "Comprehension", topics: ["Theme and central idea","Character analysis","Point of view","Drawing conclusions and inferences","Summarizing longer texts"] },
      { unit: "Vocabulary", topics: ["Greek and Latin roots","Affixes","Multiple-meaning words review","Context clues in complex texts","Denotation and connotation"] },
      { unit: "Grammar & Writing Process", topics: ["Clauses","Conjunctions","Pronoun and verb agreement","The writing process: drafting","The writing process: revising and editing","Writing types review"] },
    ],
    history: [
      { unit: "Founding of the Nation", topics: ["Causes of the American Revolution","Key events of the Revolution","Declaration of Independence basics","Founding documents","Key founding figures"] },
      { unit: "Government & Civics", topics: ["The US Constitution and Bill of Rights","Federal government branches","State and local government","Citizen responsibilities"] },
      { unit: "Colonial & Native History", topics: ["Colonial life and economy","Native American history and culture","Interactions between colonists and Native Americans","The 13 colonies review"] },
      { unit: "Geography & Economics", topics: ["Geography of North America","Supply and demand","Trade and entrepreneurship intro","Scarcity and resources"] },
    ],
    cs: [
      { unit: "Computational Thinking", topics: ["Decomposition","Pattern recognition","Abstraction","How the internet works: client and server basics","Data representation basics: binary intro"] },
      { unit: "Coding Concepts", topics: ["Variables","Loops","Conditionals","Functions intro","Debugging strategies","Block-based programming: sprites, events, sequences","Robotics and algorithms basics"] },
    ],
    health: [
      { unit: "Body & Nutrition", topics: ["Reading nutrition labels","Body systems review","Communicable vs. noncommunicable disease","Puberty and body changes basics"] },
      { unit: "Safety & Wellness", topics: ["Managing stress","Self-esteem and empathy","Safety and first aid review","Substance abuse prevention","Healthy relationships","Communication skills","Mental and emotional health","Setting personal health goals"] },
    ],
  },
  6: {
    math: [
      { unit: 'Ratios & Proportional Relationships', topics: ['Understanding ratios','Unit rates','Ratio tables','Proportional relationships','Percent problems'] },
      { unit: 'The Number System', topics: ['Division of fractions','Multi-digit arithmetic','Rational numbers on a number line','Absolute value','Ordering integers'] },
      { unit: 'Expressions & Equations', topics: ['Writing and evaluating expressions','Properties of operations','Solving one-step equations','Inequalities'] },
      { unit: 'Geometry', topics: ['Area of polygons','Surface area','Volume of rectangular prisms','Coordinate plane'] },
      { unit: 'Statistics & Probability', topics: ['Statistical questions','Dot plots & histograms','Box plots','Mean, median, mode, range','Data distributions'] },
    ],
    science: [
      { unit: 'Matter & Its Interactions', topics: ['Atoms and molecules','States of matter','Physical vs. chemical changes','Conservation of mass','Properties of materials'] },
      { unit: 'Earth & Space Systems', topics: ['Weathering and erosion','Rock cycle','Plate tectonics introduction','Earth\'s layers','Geologic time'] },
      { unit: 'Ecosystems', topics: ['Food webs and food chains','Energy flow','Biodiversity','Ecosystem services','Human impact on ecosystems'] },
      { unit: 'Life Science', topics: ['Cell structure and function','Photosynthesis basics','Reproduction','Heredity overview','Classification of organisms'] },
    ],
    ela: [
      { unit: 'Reading Literature', topics: ['Story elements: plot, setting, character','Theme and central message','Point of view','Comparing texts','Figurative language'] },
      { unit: 'Reading Informational Text', topics: ['Main idea and supporting details','Author\'s purpose','Text structure','Evidence and reasoning','Summarization'] },
      { unit: 'Writing', topics: ['Narrative writing','Informational/explanatory writing','Argument writing','Research process','Revision and editing'] },
      { unit: 'Language Conventions', topics: ['Parts of speech review','Sentence structure','Punctuation','Vocabulary development','Context clues'] },
      { unit: 'Speaking & Listening', topics: ['Collaborative discussion','Presentations','Evaluating speaker\'s arguments','Multimedia integration'] },
    ],
    history: [
      { unit: 'Early Civilizations', topics: ['Mesopotamia','Ancient Egypt','Ancient India and China','Ancient Greece','Ancient Rome'] },
      { unit: 'World Geography', topics: ['Reading maps and globes','Physical geography','Human geography','Regions of the world','Geographic tools'] },
      { unit: 'Government & Civics Intro', topics: ['Types of government','Laws and rules','Rights and responsibilities','Democratic principles','Local government'] },
    ],
    cs: [
      { unit: 'Digital Literacy', topics: ['Internet safety','Evaluating online sources','Digital citizenship','Privacy and security','Screen time awareness'] },
      { unit: 'Introduction to Coding', topics: ['Algorithms and flowcharts','Sequence, selection, iteration','Block-based coding (Scratch)','Debugging','Creating simple projects'] },
    ],
    health: [
      { unit: 'Personal Health', topics: ['Hygiene and self-care','Sleep and nutrition','Growth and development','Puberty education','Stress management'] },
      { unit: 'Physical Fitness', topics: ['Components of fitness','Aerobic exercise','Strength and flexibility','Team sports rules','Setting fitness goals'] },
    ],
  },

  7: {
    math: [
      { unit: 'Ratios & Proportional Relationships', topics: ['Proportional vs. non-proportional','Solving proportions','Percent increase and decrease','Simple interest','Scale drawings'] },
      { unit: 'The Number System', topics: ['Adding and subtracting rational numbers','Multiplying and dividing rational numbers','Rational number word problems','Converting fractions/decimals/percents'] },
      { unit: 'Expressions & Equations', topics: ['Linear expressions','Solving multi-step equations','Inequalities on a number line','Rewriting expressions'] },
      { unit: 'Geometry', topics: ['Angle relationships','Area and circumference of circles','Area of composite figures','Surface area and volume of 3D figures','Scale problems'] },
      { unit: 'Statistics & Probability', topics: ['Random sampling','Comparing populations','Probability of simple events','Probability of compound events','Simulations'] },
    ],
    science: [
      { unit: 'Structure & Properties of Matter', topics: ['Periodic table','Chemical vs. physical properties','Density','Mixtures and solutions','Atomic structure intro'] },
      { unit: 'Chemical Reactions', topics: ['Signs of a chemical reaction','Conservation of mass','Endothermic vs. exothermic','Everyday chemical reactions'] },
      { unit: 'Life Science: Body Systems', topics: ['Digestive system','Circulatory system','Respiratory system','Nervous system','Muscular and skeletal systems'] },
      { unit: 'Earth Science', topics: ['Atmosphere layers','Weather patterns','Climate vs. weather','Natural disasters','Human impact on atmosphere'] },
    ],
    ela: [
      { unit: 'Reading Literature', topics: ['Complex character analysis','Theme development','Narrative techniques','Poetry analysis','Comparing genres'] },
      { unit: 'Reading Informational Text', topics: ['Central idea development','Analyzing arguments','Text structure analysis','Primary vs. secondary sources','Evaluating evidence'] },
      { unit: 'Writing', topics: ['Argumentative writing','Research-based writing','Narrative techniques','Citation and plagiarism','Peer review process'] },
      { unit: 'Language & Grammar', topics: ['Phrases and clauses','Misplaced/dangling modifiers','Active vs. passive voice','Word choice and tone','Formal vs. informal register'] },
    ],
    history: [
      { unit: 'Medieval World', topics: ['Fall of Rome','Byzantine Empire','Islamic civilization','Medieval Europe','Feudal system'] },
      { unit: 'Renaissance & Reformation', topics: ['Italian Renaissance','Scientific Revolution','Protestant Reformation','Age of Exploration','Columbian Exchange'] },
      { unit: 'Early Americas', topics: ['Pre-Columbian civilizations','European colonization','Native American cultures','Colonial life','African slave trade'] },
    ],
    cs: [
      { unit: 'Programming Fundamentals', topics: ['Variables and data types','Conditionals','Loops','Functions and procedures','Input/output'] },
      { unit: 'Problem Solving', topics: ['Computational thinking','Decomposition','Pattern recognition','Algorithm design','Pseudocode'] },
    ],
    health: [
      { unit: 'Mental & Emotional Health', topics: ['Emotional intelligence','Coping with stress','Building resilience','Recognizing depression/anxiety','Getting help'] },
      { unit: 'Nutrition & Wellness', topics: ['Macronutrients','Reading nutrition labels','Healthy vs. unhealthy habits','Eating disorders awareness','Hydration'] },
    ],
  },

  8: {
    math: [
      { unit: 'The Number System', topics: ['Irrational numbers','Square and cube roots','Approximating irrational numbers','Scientific notation operations'] },
      { unit: 'Expressions & Equations', topics: ['Integer exponents','Linear equations with one solution','Systems of linear equations','Solving systems by substitution and elimination'] },
      { unit: 'Functions', topics: ['Defining functions','Linear vs. nonlinear functions','Slope and rate of change','Representing functions (tables, graphs, equations)','Comparing functions'] },
      { unit: 'Geometry', topics: ['Transformations (translations, rotations, reflections)','Congruence and similarity','Pythagorean theorem','Pythagorean theorem applications','Volume of cylinders, cones, spheres'] },
      { unit: 'Statistics & Probability', topics: ['Scatter plots','Line of best fit','Linear associations','Two-way frequency tables'] },
    ],
    science: [
      { unit: 'Force & Motion', topics: ['Newton\'s laws of motion','Gravity and friction','Speed, velocity, acceleration','Free body diagrams','Momentum'] },
      { unit: 'Energy', topics: ['Kinetic and potential energy','Conservation of energy','Forms of energy','Energy transfer and transformation','Renewable vs. nonrenewable energy'] },
      { unit: 'Waves & Electromagnetic Spectrum', topics: ['Wave properties','Sound waves','Light waves','Electromagnetic spectrum','Communication technology'] },
      { unit: 'Earth History & Space', topics: ['Evidence for plate tectonics','Fossil record','Natural selection intro','Solar system','Stars and galaxies'] },
    ],
    ela: [
      { unit: 'Reading Literature', topics: ['Analyzing dialogue and incidents','Universal themes','Allusion','Modern vs. classic texts','Drama and screenplay reading'] },
      { unit: 'Reading Informational Text', topics: ['Delineating and evaluating arguments','Conflicting information','Integrating multiple sources','Media literacy'] },
      { unit: 'Writing', topics: ['Argumentative essay structure','Counterarguments and rebuttals','Research paper writing','MLA/APA citation intro','Narrative craft'] },
      { unit: 'Language', topics: ['Verbals: gerunds, participles, infinitives','Comma use','Semicolons and colons','Nuances in word meanings','Etymology'] },
    ],
    history: [
      { unit: 'American Revolution & Founding', topics: ['Causes of the Revolution','Declaration of Independence','Revolutionary War','Articles of Confederation','Constitutional Convention'] },
      { unit: 'The Constitution & New Nation', topics: ['Structure of the Constitution','Bill of Rights','Federalism','Early political parties','Washington and Adams presidencies'] },
      { unit: 'Expansion & Reform', topics: ['Manifest Destiny','Westward expansion','Reform movements','Industrial Revolution in America','Immigration patterns'] },
      { unit: 'Civil War & Reconstruction', topics: ['Causes of the Civil War','Major battles and turning points','Emancipation Proclamation','Reconstruction plans','Impact of Reconstruction'] },
    ],
    cs: [
      { unit: 'Data & Analysis', topics: ['Data types and structures','Collecting and cleaning data','Spreadsheet skills','Data visualization','Drawing conclusions from data'] },
      { unit: 'Web Design Basics', topics: ['HTML structure','CSS styling','Accessibility principles','Publishing a webpage','Internet architecture'] },
    ],
    health: [
      { unit: 'Substance Use & Abuse', topics: ['Alcohol and tobacco effects','Drug classifications','Addiction science','Refusal skills','Community resources'] },
      { unit: 'Relationships & Communication', topics: ['Healthy vs. unhealthy relationships','Conflict resolution','Digital communication etiquette','Bullying and bystander effect','Consent basics'] },
    ],
  },

  9: {
    math: [
      { unit: 'Algebra I: Foundations', topics: ['Number properties review','Order of operations','Writing expressions and equations','Evaluating algebraic expressions','Translating word problems'] },
      { unit: 'Linear Relationships', topics: ['Slope-intercept form','Standard form','Point-slope form','Parallel and perpendicular lines','Graphing linear equations'] },
      { unit: 'Systems of Equations', topics: ['Graphing systems','Substitution method','Elimination method','Systems of inequalities','Real-world applications'] },
      { unit: 'Polynomials', topics: ['Adding and subtracting polynomials','Multiplying polynomials','Factoring GCF','Factoring trinomials','Special products'] },
      { unit: 'Quadratic Functions', topics: ['Graphing parabolas','Vertex form','Standard form','Factoring to solve quadratics','Quadratic formula'] },
      { unit: 'Exponential & Radical Functions', topics: ['Exponential growth and decay','Radical expressions','Simplifying radicals','Solving radical equations'] },
    ],
    science: [
      { unit: 'Biology: Cell Biology', topics: ['Cell theory','Prokaryotic vs. eukaryotic cells','Cell organelles','Cell membrane and transport','Cell cycle and mitosis'] },
      { unit: 'Genetics', topics: ['DNA structure and function','Protein synthesis','Mendelian genetics','Punnett squares','Mutations and genetic disorders'] },
      { unit: 'Evolution', topics: ['Evidence for evolution','Natural selection','Adaptation','Speciation','Human evolution overview'] },
      { unit: 'Ecology', topics: ['Population dynamics','Community interactions','Biomes','Nutrient cycles','Climate change and biodiversity'] },
    ],
    ela: [
      { unit: 'Reading Literature', topics: ['Literary analysis essays','Complex character development','Symbolism and allegory','Satire and irony','World literature introduction'] },
      { unit: 'Research & Informational Writing', topics: ['Evaluating source credibility','Synthesizing multiple sources','Research paper structure','In-text citations','Works cited page'] },
      { unit: 'Argumentative Writing', topics: ['Claim and evidence','Logical fallacies','Rhetorical devices','Audience and purpose','Formal essay conventions'] },
      { unit: 'Vocabulary & Language', topics: ['Academic vocabulary','Greek and Latin roots','Connotation vs. denotation','Figurative language mastery','Writing style development'] },
    ],
    history: [
      { unit: 'World History: Modern Era', topics: ['Age of Revolutions (French, Haitian)','Nationalism and imperialism','Industrial Revolution globally','World War I causes and effects','Treaty of Versailles'] },
      { unit: 'Global Economics Intro', topics: ['Supply and demand','Market structures','Economic systems','Trade and globalization','Personal finance basics'] },
      { unit: 'Government & Civics', topics: ['Federalism and separation of powers','Branches of US government','Electoral system','Civil liberties and civil rights','Comparative government systems'] },
    ],
    cs: [
      { unit: 'Python Programming', topics: ['Variables and data types','Control flow','Functions','Lists and dictionaries','File I/O basics'] },
      { unit: 'Cybersecurity Awareness', topics: ['Types of cyber threats','Password security','Encryption basics','Social engineering','Privacy laws and ethics'] },
    ],
    health: [
      { unit: 'Human Development & Sexuality', topics: ['Reproductive anatomy','STI prevention','Contraception methods','Consent and healthy relationships','Teen pregnancy statistics'] },
      { unit: 'First Aid & Safety', topics: ['CPR basics','AED use','Treating wounds','Emergency response','Sports injury prevention'] },
    ],
  },

  10: {
    math: [
      { unit: 'Geometry: Foundations', topics: ['Points, lines, planes','Angle pairs','Parallel lines and transversals','Triangle congruence (SSS, SAS, ASA)','Proofs introduction'] },
      { unit: 'Triangles & Trigonometry', topics: ['Pythagorean theorem applications','Special right triangles','Trigonometric ratios (sin, cos, tan)','Solving right triangles','Angles of elevation and depression'] },
      { unit: 'Circles', topics: ['Circle theorems','Arc length and sector area','Equations of circles','Chords, tangents, secants','Inscribed angles'] },
      { unit: 'Area, Surface Area & Volume', topics: ['Area of polygons and composite figures','Surface area of 3D figures','Volume of prisms, cylinders, pyramids, cones','Cavalieri\'s principle'] },
      { unit: 'Probability & Statistics', topics: ['Conditional probability','Permutations and combinations','Normal distributions','z-scores','Data analysis and interpretation'] },
    ],
    science: [
      { unit: 'Chemistry: Atomic Structure', topics: ['Bohr model','Electron configuration','Periodic trends','Ionic vs. covalent bonding','Lewis dot structures'] },
      { unit: 'Chemical Reactions', topics: ['Balancing equations','Types of reactions','Stoichiometry','Limiting reagents','Reaction rates and equilibrium intro'] },
      { unit: 'Solutions & Thermochemistry', topics: ['Molarity and concentration','Acids and bases (pH)','Solubility rules','Enthalpy and calorimetry','Hess\'s Law intro'] },
      { unit: 'Nuclear Chemistry', topics: ['Radioactive decay','Half-life','Fission vs. fusion','Applications of nuclear chemistry','Radiation safety'] },
    ],
    ela: [
      { unit: 'American Literature', topics: ['Puritan literature','Romantic era','Transcendentalism (Thoreau, Emerson)','Realism and Naturalism','Harlem Renaissance'] },
      { unit: 'Literary Analysis', topics: ['Critical lenses (feminist, historical, etc.)','Comparing authorial choices','Analyzing complex texts','Writing analytical essays','Oral presentation of analysis'] },
      { unit: 'Composition', topics: ['Advanced argument structure','Synthesis essays','Technical and professional writing','Timed writing strategies','Grammar and mechanics mastery'] },
    ],
    history: [
      { unit: 'World War II & Holocaust', topics: ['Rise of fascism','Major theaters of war','Holocaust history and causes','Home front','Post-war world order'] },
      { unit: 'Cold War Era', topics: ['Origins of the Cold War','Korean War','McCarthyism','Space Race','Vietnam War'] },
      { unit: 'Modern US History', topics: ['Civil Rights Movement','Women\'s liberation movement','1970s–1990s America','End of Cold War','September 11 and aftermath'] },
    ],
    cs: [
      { unit: 'Object-Oriented Programming', topics: ['Classes and objects','Inheritance','Encapsulation','Polymorphism','Building small applications'] },
      { unit: 'Databases', topics: ['Relational databases','SQL basics','Data modeling','CRUD operations','Database design principles'] },
    ],
    health: [
      { unit: 'Mental Health & Wellness', topics: ['Mental health disorders overview','Therapy approaches','Reducing stigma','Mindfulness practices','When and how to seek help'] },
      { unit: 'Community Health', topics: ['Public health systems','Epidemiology basics','Healthcare access','Advocacy and policy','Global health challenges'] },
    ],
  },

  11: {
    math: [
      { unit: 'Algebra II: Functions', topics: ['Function notation and operations','Inverse functions','Graphing transformations','Piecewise functions','Absolute value functions'] },
      { unit: 'Polynomial & Rational Functions', topics: ['Polynomial long division','Fundamental theorem of algebra','Rational functions and asymptotes','Partial fractions','Solving rational equations'] },
      { unit: 'Exponential & Logarithmic Functions', topics: ['Laws of logarithms','Natural log and e','Exponential growth/decay models','Solving logarithmic equations','Applications: compound interest'] },
      { unit: 'Sequences & Series', topics: ['Arithmetic sequences','Geometric sequences','Infinite geometric series','Sigma notation','Binomial theorem'] },
      { unit: 'Trigonometry', topics: ['Unit circle','Radian measure','Graphing sin, cos, tan','Trigonometric identities','Law of sines and cosines'] },
      { unit: 'Statistics (Pre-AP)', topics: ['Experimental design','Sampling methods','Regression analysis','Chi-squared tests intro','Interpreting statistical claims'] },
    ],
    science: [
      { unit: 'Physics: Motion & Forces', topics: ['Kinematics equations','Projectile motion','Newton\'s Laws in depth','Friction and normal force','Circular motion'] },
      { unit: 'Work, Energy & Momentum', topics: ['Work-energy theorem','Conservation of mechanical energy','Impulse-momentum theorem','Elastic and inelastic collisions','Power'] },
      { unit: 'Electricity & Magnetism', topics: ['Electric charge and fields','Circuits (series and parallel)','Ohm\'s Law','Magnetism','Electromagnetic induction'] },
      { unit: 'Waves, Light & Optics', topics: ['Wave superposition','Doppler effect','Reflection and refraction','Lenses and mirrors','Quantum basics'] },
    ],
    ela: [
      { unit: 'British Literature', topics: ['Anglo-Saxon period (Beowulf)','Chaucer and Middle Ages','Shakespeare','Romantic poets','Victorian and modern literature'] },
      { unit: 'Research & Rhetoric', topics: ['Rhetorical analysis essays','Evaluating and synthesizing sources','Annotated bibliography','AP-style essays','Timed analytical writing'] },
      { unit: 'Language & Style', topics: ['Diction and syntax analysis','Sentence variety and rhythm','Tone and voice','Style imitation exercises','Advanced grammar review'] },
    ],
    history: [
      { unit: 'US History: Gilded Age to WWII', topics: ['Industrialization and labor movement','Progressive Era','WWI US involvement','Roaring Twenties','Great Depression and New Deal'] },
      { unit: 'Contemporary Global Issues', topics: ['Globalization','Climate change policy','Immigration and migration','Human rights','International organizations (UN, NATO)'] },
      { unit: 'Economics', topics: ['Macroeconomics fundamentals','Fiscal and monetary policy','GDP and economic indicators','Unemployment and inflation','Global financial systems'] },
    ],
    cs: [
      { unit: 'Data Structures & Algorithms', topics: ['Arrays and linked lists','Stacks and queues','Sorting algorithms','Searching algorithms','Big-O notation'] },
      { unit: 'Intro to AI & Machine Learning', topics: ['What is AI?','Supervised vs. unsupervised learning','Training data and bias','AI ethics','Real-world AI applications'] },
    ],
    health: [
      { unit: 'Lifetime Fitness Planning', topics: ['Setting long-term fitness goals','Creating workout programs','Nutrition for performance','Injury prevention','Fitness tracking tools'] },
      { unit: 'Health Decision Making', topics: ['Risk assessment','Peer pressure and social norms','Media influence on health','Healthcare navigation','Insurance basics'] },
    ],
  },

  12: {
    math: [
      { unit: 'Pre-Calculus / Calculus Intro', topics: ['Limits and continuity','Derivative definition','Basic differentiation rules','Product, quotient, chain rules','Applications of derivatives'] },
      { unit: 'Integration', topics: ['Antiderivatives','Definite integrals','Fundamental theorem of calculus','Area under a curve','Basic integration techniques'] },
      { unit: 'Statistics (AP-level)', topics: ['Probability distributions','Confidence intervals','Hypothesis testing','Regression and correlation','Statistical inference'] },
      { unit: 'Discrete Mathematics', topics: ['Logic and proofs','Set theory','Combinatorics','Graph theory','Cryptography basics'] },
    ],
    science: [
      { unit: 'Advanced Biology / AP Bio', topics: ['Biochemistry review','Cell signaling','Gene expression regulation','Evolutionary mechanisms','Ecology and population biology'] },
      { unit: 'Advanced Chemistry / AP Chem', topics: ['Equilibrium constants','Acids, bases, and buffers','Electrochemistry','Thermodynamics','Kinetics'] },
      { unit: 'Environmental Science', topics: ['Earth\'s systems','Biodiversity threats','Resource management','Pollution types','Sustainability and policy'] },
    ],
    ela: [
      { unit: 'AP English Language', topics: ['Rhetorical analysis','Synthesis writing','Argumentative essay','AP exam strategies','Citing non-fiction sources'] },
      { unit: 'AP English Literature', topics: ['Poetry explication','Prose fiction analysis','Drama analysis','Open-ended essay','Thematic essays on major works'] },
      { unit: 'College Writing Preparation', topics: ['College essay writing','Personal statement strategies','Academic writing conventions','Research and citation mastery','Writing portfolios'] },
    ],
    history: [
      { unit: 'AP US History / Capstone', topics: ['Thematic analysis across eras','Primary source analysis','Long Essay Question (LEQ)','Document-Based Question (DBQ)','Historical causation and continuity'] },
      { unit: 'AP Government & Politics', topics: ['Constitutional underpinnings','Civil liberties and rights','Institutions of government','Political beliefs and behaviors','Public policy'] },
      { unit: 'Philosophy & Ethics Intro', topics: ['Branches of philosophy','Ethical theories (utilitarian, deontological)','Social contract theory','Applied ethics','Critical thinking and argumentation'] },
    ],
    cs: [
      { unit: 'Capstone Project', topics: ['Project planning and design','Software development lifecycle','User interface design','Testing and debugging','Presenting and deploying a project'] },
      { unit: 'Career & College Readiness in CS', topics: ['Tech career pathways','College CS programs','Portfolio building','Interview preparation','Open source contributions'] },
    ],
    health: [
      { unit: 'Adult Health & Wellness', topics: ['Preventive care habits','Understanding health insurance','Reproductive health and family planning','Managing chronic conditions','Mental health maintenance'] },
      { unit: 'Senior Capstone: Personal Wellness Plan', topics: ['Holistic health assessment','Creating a personal wellness plan','Community health advocacy','Reflecting on lifelong health goals'] },
    ],
  },

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

};