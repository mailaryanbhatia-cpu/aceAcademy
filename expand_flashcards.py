#!/usr/bin/env python3
"""Append comprehensive Math and ELA vocabulary to flashcards.html."""
import pathlib, re

def c(g, term, definition):
    t = term.replace('\\','\\\\').replace('"','\\"').replace("'","\\'")
    d = definition.replace('\\','\\\\').replace('"','\\"').replace("'","\\'")
    return f'    {{g:{g},term:"{t}",def:"{d}"}}'

# ── MATH ADDITIONS ─────────────────────────────────────────────────────────────
MATH_NEW = [
    # Grade 6 — Number & Operations
    c(6,'Factor','A number that divides evenly into another. Factors of 12: 1,2,3,4,6,12.'),
    c(6,'Multiple','The result of multiplying a number by any whole number. Multiples of 4: 4,8,12,16…'),
    c(6,'Prime Number','A whole number greater than 1 with exactly two factors: 1 and itself.'),
    c(6,'Composite Number','A whole number with more than two factors. 12 is composite (factors: 1,2,3,4,6,12).'),
    c(6,'GCF (Greatest Common Factor)','The largest factor shared by two or more numbers. GCF of 12 and 18 = 6.'),
    c(6,'LCM (Least Common Multiple)','The smallest multiple shared by two or more numbers. LCM of 4 and 6 = 12.'),
    c(6,'Numerator','The top number of a fraction — how many parts you have.'),
    c(6,'Denominator','The bottom number of a fraction — how many equal parts the whole is divided into.'),
    c(6,'Improper Fraction','A fraction where the numerator is greater than the denominator. E.g., 7/4.'),
    c(6,'Mixed Number','A whole number combined with a proper fraction. E.g., 1¾.'),
    c(6,'Equivalent Fractions','Fractions that represent the same value. ½ = 2/4 = 3/6.'),
    c(6,'Place Value','The value of a digit based on its position. In 3,472: 3 is thousands, 4 hundreds, 7 tens, 2 ones.'),
    c(6,'Coordinate Plane','A flat surface with x-axis and y-axis used to plot ordered pairs.'),
    c(6,'Ordered Pair','A pair of numbers (x, y) used to locate a point on a coordinate plane.'),
    c(6,'Quadrant','One of four sections of the coordinate plane, numbered I–IV counter-clockwise.'),
    c(6,'Perimeter','The total distance around a polygon. P = sum of all sides.'),
    c(6,'Area','The amount of surface inside a shape. Measured in square units.'),
    c(6,'Volume','The amount of 3D space inside a solid. Measured in cubic units.'),
    c(6,'Net (Geometry)','A flat pattern that can be folded to form a 3D solid.'),
    c(6,'Histogram','A bar graph showing the frequency of data within equal intervals.'),
    c(6,'Dot Plot','A graph where each data point is shown as a dot above a number line.'),
    c(6,'Interquartile Range (IQR)','The range of the middle 50% of data. IQR = Q3 − Q1.'),
    c(6,'Quartile','Values that split a data set into four equal parts: Q1, Q2 (median), Q3.'),
    c(6,'Box Plot','A graph showing the five-number summary: min, Q1, median, Q3, max.'),
    # Grade 7 — Ratios, Proportions, Algebra, Geometry
    c(7,'Percent Change','How much something increased or decreased relative to the original. % Change = (change/original) × 100.'),
    c(7,'Markup','The amount added to the cost price to get the selling price.'),
    c(7,'Discount','A reduction in price, usually shown as a percent off.'),
    c(7,'Rational Number','Any number that can be written as a fraction p/q where q ≠ 0. Includes integers, fractions, repeating decimals.'),
    c(7,'Adjacent Angles','Two angles that share a common side and vertex but don\'t overlap.'),
    c(7,'Vertical Angles','Opposite angles formed by two intersecting lines. They are always equal.'),
    c(7,'Circumference','The perimeter of a circle. C = 2πr or C = πd.'),
    c(7,'Pi (π)','The ratio of a circle\'s circumference to its diameter ≈ 3.14159. An irrational number.'),
    c(7,'Constant of Proportionality','The value k in a proportional relationship y = kx. Also called the unit rate.'),
    c(7,'Two-Step Equation','An equation requiring two operations to isolate the variable. E.g., 2x + 3 = 11.'),
    c(7,'Cross Product','In a proportion a/b = c/d, the cross products are ad and bc. They are equal.'),
    c(7,'Random Sample','A sample where every member of the population has an equal chance of being chosen.'),
    c(7,'Surface Area','The total area of all faces of a 3D solid. Measured in square units.'),
    # Grade 8 — Functions, Geometry, Statistics
    c(8,'Rate of Change','How much one quantity changes relative to another. In y=mx+b, rate of change = slope m.'),
    c(8,'X-intercept','The point where a line crosses the x-axis (when y = 0).'),
    c(8,'Parallel Lines','Lines in the same plane that never intersect; they have equal slopes.'),
    c(8,'Perpendicular Lines','Lines that intersect at a 90° angle; their slopes are negative reciprocals.'),
    c(8,'Transversal','A line that crosses two or more other lines, creating multiple angle pairs.'),
    c(8,'Alternate Interior Angles','Angles formed between two parallel lines on opposite sides of a transversal. They are equal.'),
    c(8,'Corresponding Angles','Angles in matching positions when a transversal crosses parallel lines. They are equal.'),
    c(8,'Scatter Plot','A graph plotting paired data as points to show the relationship between two variables.'),
    c(8,'Line of Best Fit','A straight line drawn through a scatter plot that best represents the trend in the data.'),
    c(8,'Correlation','The relationship between two variables. Positive, negative, or no correlation.'),
    c(8,'Volume of a Cylinder','V = πr²h. Pi times radius squared times height.'),
    c(8,'Volume of a Cone','V = ⅓πr²h. One-third the volume of a cylinder with the same base and height.'),
    c(8,'Volume of a Sphere','V = (4/3)πr³. Four-thirds times pi times radius cubed.'),
    c(8,'Square Root','A value that, when multiplied by itself, gives the original number. √25 = 5.'),
    c(8,'Perfect Square','A number that is the square of a whole number. 1, 4, 9, 16, 25… are perfect squares.'),
    # Grade 9 — Algebra
    c(9,'Monomial','An algebraic expression with exactly one term. E.g., 5x², −3, 7xy.'),
    c(9,'Binomial','An algebraic expression with exactly two terms. E.g., x + 4, 3x² − 7.'),
    c(9,'Trinomial','An algebraic expression with exactly three terms. E.g., x² + 5x + 6.'),
    c(9,'Polynomial','An expression with one or more terms with non-negative exponents.'),
    c(9,'FOIL Method','Multiply two binomials: First, Outer, Inner, Last. (x+2)(x+3) = x²+3x+2x+6 = x²+5x+6.'),
    c(9,'Zero Product Property','If a × b = 0, then a = 0 or b = 0. Used to solve factored equations.'),
    c(9,'Roots / Zeros','The x-values where a function equals zero (where the graph crosses the x-axis).'),
    c(9,'Vertex','The highest or lowest point of a parabola. At x = −b/(2a) in f(x) = ax²+bx+c.'),
    c(9,'Parabola','The U-shaped graph of a quadratic function.'),
    c(9,'Axis of Symmetry','The vertical line through the vertex of a parabola. x = −b/(2a).'),
    c(9,'Completing the Square','Rewriting ax²+bx+c by creating a perfect square trinomial. Used to solve quadratics.'),
    c(9,'Direct Variation','A relationship y = kx where y is proportional to x. Graph is a line through the origin.'),
    c(9,'Inverse Variation','A relationship y = k/x where y decreases as x increases.'),
    c(9,'Interval Notation','A way to express a set of numbers using brackets [ ] and parentheses ( ). [2,5) means 2 ≤ x < 5.'),
    c(9,'Absolute Value Equation','An equation containing |x|. |x| = 5 has two solutions: x = 5 and x = −5.'),
    c(9,'Piecewise Function','A function defined by different rules for different parts of the domain.'),
    c(9,'Parent Function','The simplest form of a function family. E.g., f(x) = x² is the parent quadratic.'),
    # Grade 10 — Geometry & Algebra 2
    c(10,'Theorem','A mathematical statement that has been proved to be true.'),
    c(10,'Postulate','A statement accepted as true without proof, used as a starting point in geometry.'),
    c(10,'SSS Congruence','Side-Side-Side: if all three sides of two triangles are equal, the triangles are congruent.'),
    c(10,'SAS Congruence','Side-Angle-Side: two sides and the included angle are equal → triangles are congruent.'),
    c(10,'ASA Congruence','Angle-Side-Angle: two angles and the included side are equal → triangles are congruent.'),
    c(10,'Similar Triangles','Triangles with the same shape but different size. Corresponding angles equal, sides proportional.'),
    c(10,'Midpoint Formula','The midpoint of (x₁,y₁) and (x₂,y₂) is ((x₁+x₂)/2, (y₁+y₂)/2).'),
    c(10,'Distance Formula','d = √[(x₂−x₁)² + (y₂−y₁)²]. The straight-line distance between two points.'),
    c(10,'Chord','A line segment connecting two points on a circle, not necessarily through the center.'),
    c(10,'Arc','A portion of the circumference of a circle.'),
    c(10,'Central Angle','An angle whose vertex is the center of a circle. Equals the arc it intercepts.'),
    c(10,'Inscribed Angle','An angle formed by two chords with the vertex on the circle. Half the intercepted arc.'),
    c(10,'Tangent Line (circle)','A line that touches a circle at exactly one point. Perpendicular to the radius at that point.'),
    c(10,'Sector','A pie-slice region of a circle bounded by two radii and an arc.'),
    c(10,'Law of Sines','a/sin A = b/sin B = c/sin C. Used to solve non-right triangles.'),
    c(10,'Imaginary Number','The square root of a negative number. i = √−1, i² = −1.'),
    c(10,'Complex Number','A number in the form a + bi, where a is real and bi is imaginary.'),
    c(10,'Rational Exponent','An exponent that is a fraction. x^(m/n) = the nth root of x^m.'),
    c(10,'Synthetic Division','A shortcut method for dividing a polynomial by a linear binomial.'),
    # Grade 11 — Pre-Calc, Trig, Stats
    c(11,'Amplitude','Half the vertical distance between the max and min of a trig function. In y = A sin x, amplitude = |A|.'),
    c(11,'Period','The horizontal length of one complete cycle of a trig function. Period of sin/cos = 2π.'),
    c(11,'Phase Shift','A horizontal shift of a trig function left or right.'),
    c(11,'Inverse Trig Function','A function that undoes a trig function. sin⁻¹(x), cos⁻¹(x), tan⁻¹(x).'),
    c(11,'Series','The sum of the terms of a sequence. Σ notation is used.'),
    c(11,'Sigma Notation (Σ)','A compact way to write the sum of a sequence. Σᵢ₌₁ⁿ aᵢ = a₁+a₂+…+aₙ.'),
    c(11,'Infinite Geometric Series','S = a/(1−r) when |r| < 1. The sum of infinitely many terms of a geometric sequence.'),
    c(11,'Normal Distribution','A bell-shaped probability distribution symmetric about the mean.'),
    c(11,'Z-Score','The number of standard deviations a value is from the mean. z = (x − μ)/σ.'),
    c(11,'Confidence Interval','A range of values likely to contain a population parameter, e.g., 95% CI.'),
    c(11,'Correlation Coefficient (r)','A value from −1 to 1 measuring strength and direction of a linear relationship.'),
    c(11,'Polynomial Long Division','Dividing one polynomial by another using a process similar to numeric long division.'),
    c(11,'Rational Function','A function that is the ratio of two polynomials. f(x) = p(x)/q(x).'),
    c(11,'End Behavior','What a function does as x → ∞ or x → −∞. Determined by leading term.'),
    # Grade 12 — Calculus & Advanced
    c(12,'Limit','The value a function approaches as the input approaches a specific value. lim(x→a) f(x).'),
    c(12,'Continuity','A function is continuous if its graph has no holes, jumps, or vertical asymptotes.'),
    c(12,'Product Rule','d/dx[f(x)g(x)] = f\'(x)g(x) + f(x)g\'(x). Rule for differentiating products.'),
    c(12,'Quotient Rule','d/dx[f/g] = (f\'g − fg\')/g². Rule for differentiating quotients.'),
    c(12,'Chain Rule','d/dx[f(g(x))] = f\'(g(x)) · g\'(x). Rule for differentiating composite functions.'),
    c(12,'Critical Point','A point where the derivative equals zero or is undefined. Potential max, min, or inflection.'),
    c(12,'Concavity','Whether a graph curves upward (concave up, f\'\'>0) or downward (concave down, f\'\'<0).'),
    c(12,'Inflection Point','A point where a function changes concavity.'),
    c(12,'Riemann Sum','An approximation of the area under a curve using rectangles.'),
    c(12,'Fundamental Theorem of Calculus','Connects differentiation and integration: ∫ₐᵇ f(x)dx = F(b) − F(a).'),
    c(12,'Antiderivative','A function F whose derivative is f. ∫f(x)dx = F(x) + C.'),
    c(12,'Dot Product','a · b = |a||b|cos θ. A scalar result from multiplying two vectors.'),
    c(12,'Eigenvalue','A scalar λ such that Av = λv for a matrix A and non-zero vector v.'),
    c(12,'Convergent Series','An infinite series whose sum approaches a finite number.'),
    c(12,'Divergent Series','An infinite series whose partial sums grow without bound — no finite sum.'),
]

# ── ELA ADDITIONS ──────────────────────────────────────────────────────────────
ELA_NEW = [
    # Grammar — Grade 6
    c(6,'Noun','A word naming a person, place, thing, or idea. Can be common (dog) or proper (Fluffy).'),
    c(6,'Verb','A word expressing action (run, write) or state of being (is, seems).'),
    c(6,'Adjective','A word that modifies (describes) a noun or pronoun. "The tall building."'),
    c(6,'Adverb','A word that modifies a verb, adjective, or other adverb. Often ends in -ly.'),
    c(6,'Pronoun','A word that replaces a noun. I, you, he, she, it, we, they, me, him, her, them.'),
    c(6,'Preposition','A word showing relationship between a noun and another word. In, on, under, with, between.'),
    c(6,'Conjunction','A word joining words, phrases, or clauses. Coordinating: for, and, nor, but, or, yet, so (FANBOYS).'),
    c(6,'Interjection','A word or phrase expressing emotion, not grammatically connected. Wow! Ouch! Oh no!'),
    c(6,'Subject','The noun or pronoun a sentence is about — who or what does the action.'),
    c(6,'Predicate','The part of a sentence containing the verb that tells what the subject does or is.'),
    c(6,'Sentence Fragment','An incomplete sentence missing a subject, verb, or complete thought.'),
    c(6,'Run-On Sentence','Two or more independent clauses incorrectly joined without proper punctuation.'),
    c(6,'Plot','The sequence of events in a story: exposition, rising action, climax, falling action, resolution.'),
    c(6,'Setting','The time and place where a story occurs.'),
    c(6,'Conflict','The central struggle in a story. Can be internal (within a character) or external (against forces outside).'),
    c(6,'Rising Action','The series of events that build tension and lead to the climax.'),
    c(6,'Climax','The turning point — the moment of highest tension in a story.'),
    c(6,'Falling Action','Events after the climax that lead toward resolution.'),
    c(6,'Resolution','The conclusion of the story where conflicts are resolved.'),
    c(6,'Exposition','The opening of a story introducing characters, setting, and situation.'),
    c(6,'Dialogue','Conversation between characters, indicated by quotation marks.'),
    c(6,'Imagery','Descriptive language that appeals to the five senses to create vivid pictures.'),
    c(6,'Personification','Giving human qualities to non-human things. "The wind whispered through the trees."'),
    c(6,'Hyperbole','An extreme exaggeration not meant to be taken literally. "I have a million things to do."'),
    c(6,'Onomatopoeia','Words that imitate the sound they describe. Buzz, crash, hiss, sizzle.'),
    # Grade 7 — Grammar & Literary Terms
    c(7,'Independent Clause','A group of words with a subject and verb that forms a complete sentence.'),
    c(7,'Dependent Clause','A clause with a subject and verb that CANNOT stand alone as a sentence.'),
    c(7,'Compound Sentence','Two independent clauses joined by a coordinating conjunction or semicolon.'),
    c(7,'Complex Sentence','An independent clause joined with one or more dependent clauses.'),
    c(7,'Active Voice','The subject performs the action. "The dog bit the man." Clear and direct.'),
    c(7,'Passive Voice','The subject receives the action. "The man was bitten by the dog."'),
    c(7,'Tone','The author\'s attitude toward the subject or audience (e.g., serious, humorous, bitter).'),
    c(7,'Mood','The feeling or atmosphere a text creates in the reader.'),
    c(7,'Symbolism','Using an object, person, or event to represent a larger idea or concept.'),
    c(7,'Static Character','A character who does not change significantly over the course of the story.'),
    c(7,'Dynamic Character','A character who undergoes significant internal change during the story.'),
    c(7,'Flat Character','A simple character with only one or two traits; not fully developed.'),
    c(7,'Round Character','A complex, fully developed character with multiple traits and motivations.'),
    c(7,'Foil','A character who contrasts with another character to highlight certain qualities.'),
    c(7,'Oxymoron','A figure of speech combining two contradictory terms. "Deafening silence," "living death."'),
    c(7,'Paradox','A statement that seems contradictory but reveals a deeper truth. "Less is more."'),
    c(7,'Allusion','An indirect reference to a person, event, place, or work of art. "He was a real Romeo."'),
    c(7,'Assonance','Repetition of vowel sounds in nearby words. "The rain in Spain stays mainly in the plain."'),
    c(7,'Consonance','Repetition of consonant sounds in nearby words, especially at the end. "He strikes a bright, white light."'),
    c(7,'Anaphora','Repetition of a word or phrase at the beginning of successive clauses. "I have a dream…"'),
    c(7,'Apostrophe (literary)','Addressing an absent person or abstract idea directly. "O Death, where is thy sting?"'),
    # Grade 8 — Writing & Rhetoric
    c(8,'Topic Sentence','The sentence that states the main idea of a paragraph, usually the first sentence.'),
    c(8,'Transition','Words or phrases that connect ideas within and between paragraphs. (However, Therefore, In addition).'),
    c(8,'Paraphrase','Restating someone else\'s ideas in your own words. Must still be cited.'),
    c(8,'Summarize','Briefly restating only the main points of a text in your own words.'),
    c(8,'Annotate','Making notes, questions, or marks in the margins of a text while reading.'),
    c(8,'Plagiarism','Using someone else\'s words or ideas without giving proper credit.'),
    c(8,'Diction','An author\'s word choice. Formal diction vs. colloquial diction shape tone and meaning.'),
    c(8,'Syntax','The arrangement of words and phrases to create sentences. Short vs. long sentences create different effects.'),
    c(8,'Juxtaposition','Placing two contrasting ideas side by side to highlight their differences.'),
    c(8,'Euphemism','A mild or indirect word used in place of one that might be harsh. "Passed away" instead of "died."'),
    c(8,'Antithesis','Placing opposite ideas in parallel structure for contrast. "To be or not to be."'),
    c(8,'Chiasmus','A reversal of grammatical structure in successive clauses. "Ask not what your country can do for you…"'),
    # Grade 9 — Poetry & Drama
    c(9,'Stanza','A group of lines in a poem, similar to a paragraph in prose.'),
    c(9,'Couplet','A stanza of two lines, usually rhyming.'),
    c(9,'Quatrain','A stanza of four lines, often with a rhyme scheme like ABAB or ABBA.'),
    c(9,'Free Verse','Poetry without a regular rhyme scheme or meter.'),
    c(9,'Blank Verse','Unrhymed poetry written in iambic pentameter. Used by Shakespeare.'),
    c(9,'Rhyme Scheme','The pattern of end rhymes in a poem, labeled with letters (ABAB, AABB, etc.).'),
    c(9,'Meter','The rhythmic pattern of stressed and unstressed syllables in poetry.'),
    c(9,'Ode','A lyric poem expressing admiration or praise for a person, place, or thing.'),
    c(9,'Elegy','A sad poem lamenting the death of someone or mourning a loss.'),
    c(9,'Ballad','A narrative poem meant to be sung, often telling a dramatic story with repeated refrains.'),
    c(9,'Epic','A long narrative poem celebrating a heroic figure. Examples: The Iliad, The Odyssey.'),
    c(9,'Haiku','A Japanese poem with three lines of 5, 7, and 5 syllables.'),
    c(9,'Tragic Flaw (Hamartia)','A weakness or error in judgment that leads to a tragic hero\'s downfall.'),
    c(9,'Catharsis','The emotional release or purification an audience feels at the end of a tragedy.'),
    c(9,'Hubris','Excessive pride or arrogance that leads to a character\'s ruin in a tragedy.'),
    # Grade 10 — Advanced Literary Analysis
    c(10,'Motif','A recurring element — image, phrase, or symbol — that develops the work\'s theme.'),
    c(10,'Satire','Using humor, irony, or exaggeration to criticize society or human behavior.'),
    c(10,'Allegory','A narrative where characters and events represent abstract ideas or morals.'),
    c(10,'Ambiguity','When a text can be interpreted in more than one way, intentionally or not.'),
    c(10,'Subtext','The underlying meaning beneath the surface of dialogue or action.'),
    c(10,'Archetype','A universal pattern or character type found across cultures. The Hero, the Mentor, the Shadow.'),
    c(10,'Gothic Literature','A genre featuring dark settings, mystery, death, and the supernatural.'),
    c(10,'Dystopia','An imaginary society characterized by oppression, suffering, and totalitarian control.'),
    c(10,'Utopia','An ideally perfect society — or a satire of the impossible dream of perfection.'),
    c(10,'Frame Narrative','A story within a story. An outer narrative frames an inner one (e.g., Canterbury Tales).'),
    c(10,'In Media Res','Beginning a narrative in the middle of the action, then filling in backstory.'),
    c(10,'Denouement','The final part of a play or narrative in which the strands of the plot are resolved.'),
    # Grade 11 — Modernism & Research
    c(11,'Modernism','Early 20th-century movement rejecting traditional forms in favor of experimentation.'),
    c(11,'Stream of Consciousness','Writing mirroring a character\'s flowing, unfiltered thoughts. Used by Virginia Woolf, James Joyce.'),
    c(11,'Epistolary Novel','A novel told through letters, diary entries, or other documents.'),
    c(11,'Unreliable Narrator','A narrator whose credibility is compromised — biased, mistaken, or deceptive.'),
    c(11,'Bildungsroman','A coming-of-age novel following a protagonist\'s moral and psychological growth. (Great Expectations, Jane Eyre).'),
    c(11,'Magical Realism','A style blending realistic narrative with magical elements, treated as normal. (Gabriel García Márquez).'),
    c(11,'Intertextuality','The relationship between texts — how one text references, echoes, or transforms another.'),
    c(11,'Primary Source','A first-hand account or original document from the period being studied.'),
    c(11,'Secondary Source','An interpretation or analysis of primary sources, written after the fact.'),
    c(11,'MLA Citation','A standardized format for crediting sources in academic writing (Modern Language Association).'),
    # Grade 12 — Post-modernism & Synthesis
    c(12,'Postmodernism','A literary movement questioning grand narratives, using irony, self-reference, and fragmentation.'),
    c(12,'Deconstruction','A critical approach revealing hidden contradictions and assumptions in a text.'),
    c(12,'Synthesis','Combining ideas from multiple sources to build a new, unified argument.'),
    c(12,'Hegemony','Dominance of one group over others through cultural influence rather than force.'),
    c(12,'Feminist Literary Criticism','Analyzing texts through the lens of gender roles, power, and women\'s representation.'),
    c(12,'New Historicism','Interpreting a text by placing it within the historical context of its time.'),
    c(12,'Ambivalence','Having mixed or contradictory feelings about something — often a theme in literature.'),
    c(12,'Polyphony','Multiple independent voices or perspectives within a single narrative.'),
    c(12,'Tragic Hero','A protagonist of high status brought down by a combination of hubris and fate.'),
    c(12,'Peripeteia','A sudden reversal of fortune, especially in a tragedy.'),
    c(12,'Anagnorisis','The moment a character makes a critical discovery, often their own identity or true situation.'),
]

# ── PATCH ──────────────────────────────────────────────────────────────────────
def find_bracket_end(text, start):
    depth, i, in_str, sc = 0, start, False, None
    while i < len(text):
        c = text[i]
        if in_str:
            if c == '\\': i += 2; continue
            if c == sc: in_str = False
        else:
            if c in ('"', "'", '`'): in_str = True; sc = c
            elif c == '[': depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0: return i
        i += 1
    return -1

p = pathlib.Path('/sessions/admiring-stoic-pascal/mnt/outputs/flashcards.html')
html = p.read_text(encoding='utf-8')

def append_to_subject(html, subject_key, new_entries):
    marker = f'{subject_key}: ['
    pos = html.find(marker)
    if pos == -1:
        print(f'ERROR: {subject_key} not found'); return html
    bracket_start = html.find('[', pos)
    bracket_end = find_bracket_end(html, bracket_start)
    if bracket_end == -1:
        print(f'ERROR: no closing ] for {subject_key}'); return html
    insertion = ',\n' + ',\n'.join(new_entries)
    html = html[:bracket_end] + insertion + '\n  ]' + html[bracket_end+1:]
    print(f'{subject_key}: added {len(new_entries)} cards')
    return html

html = append_to_subject(html, 'math', MATH_NEW)
html = append_to_subject(html, 'ela', ELA_NEW)

p.write_text(html, encoding='utf-8')
print(f'\nDone. File size: {p.stat().st_size // 1024} KB')
