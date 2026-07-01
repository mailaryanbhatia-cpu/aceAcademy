import json

def s(title, probs):
    return {"title": title, "problems": [{"q": q, "ex": ex, "a": a} for q, ex, a in probs]}

P = {}  # the new PRACTICE object

# ══════════════════════════════════════════════
# GRADE 6
# ══════════════════════════════════════════════
P[6] = {}

P[6]["math"] = [
  # U1: Ratios & Proportional Relationships
  [
    s("Understanding Ratios", [
      ("A class has 12 boys and 16 girls. Write the ratio of boys to girls in simplest form three ways.", "Think: part-to-part in fraction, colon, and word form", "12:16 simplifies to 3:4. Written as: 3 to 4, 3:4, or 3/4."),
      ("A recipe uses 2 cups flour for every 3 cups oats. You use 8 cups flour. How many cups of oats?", "Think: scale the ratio proportionally", "Scale factor = 8/2 = 4. Oats = 3 × 4 = 12 cups."),
      ("What is the difference between a part-to-part and a part-to-whole ratio? Use 5 red and 3 blue marbles.", "Think: comparing pieces vs. comparing a piece to the total", "Part-to-part: red to blue = 5:3. Part-to-whole: red to total = 5:8. Part-to-whole can be written as a fraction of the group."),
      ("Are 4:6 and 10:15 equivalent? How do you check?", "Think: simplify both to lowest terms", "4:6 ÷ 2 = 2:3. 10:15 ÷ 5 = 2:3. Yes, they are equivalent."),
    ]),
    s("Unit Rates", [
      ("A car travels 240 miles in 4 hours. What is the unit rate?", "Think: divide total by count", "240 ÷ 4 = 60 miles per hour."),
      ("Store A: 5 notebooks for $6.25. Store B: 3 for $4.05. Which is the better deal?", "Think: find price per 1 item", "Store A: $1.25 each. Store B: $1.35 each. Store A is better."),
      ("A faucet drips 18 gallons in 6 hours. How many gallons per minute?", "Think: hours → minutes requires an extra step", "3 gal/hr ÷ 60 = 0.05 gallons per minute."),
      ("What is a unit rate and why is it useful for comparing quantities?", "Think: 'per 1' makes comparison easy", "A unit rate has denominator 1 (e.g., $1.25 per item, 60 mph). It standardizes quantities so you can compare things on the same scale."),
    ]),
    s("Ratio Tables", [
      ("Complete the ratio table for 3:5 — fill in: 6→?, 9→?, ?→20", "Think: multiply both parts by the same number", "6:10, 9:15, 12:20."),
      ("Ratio table: Gallons 2,4,6 | Miles 54,108,?. Find the missing value.", "Think: find the unit rate first", "Unit rate: 27 miles/gallon. 6 × 27 = 162 miles."),
      ("A ratio table shows cats:dogs = 1:3. There are 21 dogs. How many cats?", "Think: scale factor from dogs", "Scale factor = 21/3 = 7. Cats = 1 × 7 = 7."),
      ("How do ratio tables help solve proportional problems?", "Think: organize and extend proportional patterns", "Ratio tables organize equivalent ratios. By identifying the scale factor, you can find any missing value in a proportional relationship."),
    ]),
    s("Proportional Relationships", [
      ("Is this proportional? Hours: 1,2,3,4 | Pay: $9,$18,$27,$36", "Think: check if y/x is constant", "9/1=9, 18/2=9, 27/3=9, 36/4=9. Yes, constant of proportionality = $9/hr."),
      ("Why does a proportional relationship graph always pass through (0,0)?", "Think: what does zero input mean?", "Zero input → zero output. If you work 0 hours, you earn $0. This is the defining property of proportional relationships."),
      ("Write the equation: 4 pounds of apples costs $7.", "Think: y = kx where k = constant", "k = 7/4 = 1.75. Equation: cost = 1.75 × pounds."),
      ("Is this proportional? Minutes: 5,10,15 | Calories: 45,90,136", "Think: are all ratios equal?", "45/5=9, 90/10=9, 136/15≈9.07. Not perfectly proportional — ratios are not all equal."),
    ]),
    s("Percent Problems", [
      ("What is 35% of 120?", "Think: decimal × whole", "0.35 × 120 = 42."),
      ("15 is what percent of 60?", "Think: part ÷ whole × 100", "15/60 = 0.25 = 25%."),
      ("A shirt costs $40, 25% off. What is the sale price?", "Think: subtract the discount", "Discount = $10. Sale price = $30. Or: 75% × $40 = $30."),
      ("25 students; 60% passed. How many passed and how many failed?", "Think: multiply then subtract", "Passed: 0.6 × 25 = 15. Failed: 10."),
    ]),
  ],
  # U2: The Number System
  [
    s("Division of Fractions", [
      ("Divide: 3/4 ÷ 1/2. Use keep, change, flip.", "Think: multiply by the reciprocal", "3/4 × 2/1 = 6/4 = 3/2 = 1½."),
      ("You have 5 cups of trail mix; each serving = 2/3 cup. How many servings?", "Think: 5 ÷ 2/3", "5 × 3/2 = 15/2 = 7½ servings."),
      ("A recipe needs 3/4 cup butter for the full batch. You make 2/3 of the recipe. How much butter?", "Think: multiply fractions — taking a fraction of an amount", "(2/3) × (3/4) = 6/12 = 1/2 cup."),
      ("Why does dividing by a fraction give a larger result? Use 6 ÷ 1/3.", "Think: how many thirds fit in 6?", "6 ÷ 1/3 = 18. There are 3 thirds in every whole, so 6 × 3 = 18. Dividing by a number < 1 always gives a larger quotient."),
    ]),
    s("Multi-Digit Arithmetic", [
      ("Multiply: 3.14 × 2.5. Show work.", "Think: multiply as integers, then place decimal", "314 × 25 = 7850. Three decimal places → 7.850 = 7.85."),
      ("Divide: 4.56 ÷ 0.12", "Think: multiply both by 100 to clear the divisor decimal", "456 ÷ 12 = 38."),
      ("Find: 2.03 × 0.04", "Think: 203 × 4, then place 4 decimal places", "812 → 0.0812."),
      ("6 identical packages each weigh 3.75 lbs. Total weight?", "Think: multiply decimal by whole number", "3.75 × 6 = 22.50 lbs."),
    ]),
    s("Rational Numbers on a Number Line", [
      ("Order from least to greatest: −3, 1.5, −1/2, 0, 2", "Think: negatives left, positives right", "−3, −1/2, 0, 1.5, 2."),
      ("Which is greater: −4 or −1? Explain using a number line.", "Think: further right = greater", "−1 is greater. It is to the right of −4, closer to zero."),
      ("What is the opposite of −7? Of 3.5?", "Think: same distance from zero, other side", "Opposite of −7 is 7. Opposite of 3.5 is −3.5."),
      ("Describe the location of −2½ on a number line.", "Think: between which integers?", "Between −3 and −2, halfway. It is 2½ units to the left of zero."),
    ]),
    s("Absolute Value", [
      ("Find |−8| and |5|. What does absolute value mean?", "Think: distance from zero", "|−8| = 8. |5| = 5. Absolute value = distance from zero — always ≥ 0."),
      ("Submarine at −150 ft; fish at −75 ft. Which is farther from the surface?", "Think: compare absolute values", "|−150| = 150 > |−75| = 75. The submarine is farther."),
      ("Solve: |x| = 9. How many solutions?", "Think: two values are 9 units from zero", "x = 9 or x = −9. Two solutions."),
      ("A company lost $200, then gained $150. What are the absolute values and what do they mean?", "Think: magnitude without direction", "|−200| = 200 (size of loss). |150| = 150 (size of gain). Absolute value shows magnitude regardless of direction."),
    ]),
    s("Ordering Integers", [
      ("Order from greatest to least: −10, 4, −3, 0, 7, −1", "Think: positives > 0 > negatives; larger negative = smaller", "7, 4, 0, −1, −3, −10."),
      ("Temperatures: Mon −5°, Tue 3°, Wed −8°, Thu 1°, Fri −2°. Rank coldest to warmest.", "Think: smallest number = coldest", "−8°, −5°, −2°, 1°, 3°."),
      ("True or false: −100 > −1. Explain.", "Think: which is further right on the number line?", "False. −100 is far to the left of −1. Greater absolute value in a negative = smaller value."),
      ("Fill in >, <, =: −4 ___ −9 ; 0 ___ −1 ; |−6| ___ 6", "Think: number line and absolute value rules", "−4 > −9; 0 > −1; |−6| = 6."),
    ]),
  ],
  # U3: Expressions & Equations
  [
    s("Writing and Evaluating Expressions", [
      ("Write an expression: '7 more than twice a number n'", "Think: 'twice' = ×2, 'more than' = +", "2n + 7"),
      ("Evaluate 3x² − 2x + 5 when x = 4", "Think: substitute, then order of operations", "3(16) − 8 + 5 = 48 − 8 + 5 = 45."),
      ("Parking: $3 base + $2/hr. Expression and value for 5 hours.", "Think: fixed + variable", "3 + 2h; at h=5: $13."),
      ("What is the difference between an expression and an equation?", "Think: one has an equals sign", "Expression: 2x+5 (no = sign, just a phrase). Equation: 2x+5=11 (a statement that is true or false)."),
    ]),
    s("Properties of Operations", [
      ("Name the property: 5 × (3 + 7) = 5 × 3 + 5 × 7", "Think: distributing multiplication over addition", "Distributive Property."),
      ("Simplify: 4 + (x + 9)", "Think: regroup constants using the Associative Property", "(4+9) + x = 13 + x."),
      ("Are 8 × (2 × y) and (8 × 2) × y equal? Which property proves it?", "Think: changing grouping in multiplication", "Yes, both = 16y. Associative Property of Multiplication."),
      ("Use the Distributive Property to mentally calculate 7 × 98.", "Think: break 98 into 100 − 2", "7(100−2) = 700−14 = 686."),
    ]),
    s("Solving One-Step Equations", [
      ("Solve: x + 14 = 31", "Think: subtract 14 from both sides", "x = 17. Check: 17+14=31 ✓"),
      ("Solve: 5y = 75", "Think: divide both sides by 5", "y = 15. Check: 5×15=75 ✓"),
      ("A number divided by 6 equals 9. Write and solve.", "Think: n/6=9 → multiply both sides by 6", "n = 54. Check: 54÷6=9 ✓"),
      ("Solve: m − 23 = 47", "Think: add 23 to both sides", "m = 70. Check: 70−23=47 ✓"),
    ]),
    s("Inequalities", [
      ("Write and graph: 'x is at least 5'", "Think: 'at least' means ≥", "x ≥ 5. Closed circle at 5, arrow right."),
      ("Solve and graph: 3x < 18", "Think: divide both sides by 3", "x < 6. Open circle at 6, arrow left."),
      ("A bag holds at most 30 lbs. Already have 18 lbs. Write an inequality for additional weight w.", "Think: total ≤ 30", "18 + w ≤ 30 → w ≤ 12 lbs."),
      ("What is the difference between x > 3 and x ≥ 3 on a graph?", "Think: open vs. closed circle", "x > 3: open circle (3 not included). x ≥ 3: closed circle (3 included)."),
    ]),
  ],
  # U4: Geometry
  [
    s("Area of Polygons", [
      ("Area of a triangle: base 10 cm, height 7 cm.", "Think: A = ½bh", "A = ½ × 10 × 7 = 35 cm²."),
      ("Area of a parallelogram: base 8 m, height 5 m.", "Think: A = bh", "A = 40 m²."),
      ("Trapezoid: parallel sides 6 ft and 10 ft, height 4 ft.", "Think: A = ½(b₁+b₂)h", "A = ½(16)(4) = 32 ft²."),
      ("Yard: rectangle 20m × 15m with triangular garden (base 6m, height 5m) removed. Remaining area?", "Think: total minus triangle", "300 − 15 = 285 m²."),
    ]),
    s("Surface Area", [
      ("Surface area of rectangular prism: 5 cm × 3 cm × 4 cm.", "Think: SA = 2(lw+lh+wh)", "2(15+20+12) = 94 cm²."),
      ("Cube with side 6 inches. Surface area?", "Think: 6 square faces", "6 × 36 = 216 in²."),
      ("What is surface area and name two real-world uses.", "Think: total outer area of a 3D object", "Total area of all faces. Used for: amount of paint needed, wrapping paper, packaging material."),
      ("A can of soup is a cylinder. Why does surface area matter to the manufacturer?", "Think: material cost for the can", "The manufacturer needs enough metal to cover the entire outer surface (top, bottom, and curved side). Minimizing surface area reduces material cost."),
    ]),
    s("Volume of Rectangular Prisms", [
      ("Volume of: 8 cm × 5 cm × 3 cm", "Think: V = lwh", "V = 120 cm³."),
      ("Fish tank: 60 cm × 30 cm × 40 cm. How many liters? (1 L = 1000 cm³)", "Think: find cm³ then convert", "72,000 cm³ ÷ 1000 = 72 liters."),
      ("Box volume = 360 in³, length = 12 in, width = 6 in. Find height.", "Think: rearrange V = lwh", "h = 360 ÷ 72 = 5 in."),
      ("What is the difference between area (cm²) and volume (cm³)?", "Think: 2D vs. 3D", "Area = flat space (length × width). Volume = 3D space (length × width × height). Different dimensions, different units."),
    ]),
    s("Coordinate Plane", [
      ("Plot: A(3,4), B(−2,1), C(−4,−3), D(0,−5). Identify each quadrant or axis.", "Think: x is horizontal, y vertical", "A: Q I. B: Q II. C: Q III. D: negative y-axis."),
      ("Distance between (−3, 2) and (5, 2).", "Think: same y → just subtract x-values", "|5−(−3)| = 8 units."),
      ("Name the four quadrants and the signs of (x,y) in each.", "Think: start at Q I, go counterclockwise", "Q I: (+,+). Q II: (−,+). Q III: (−,−). Q IV: (+,−)."),
      ("Rectangle corners: (1,1),(1,5),(4,5),(4,1). Find perimeter and area.", "Think: count units between corners", "Width=3, Height=4. Perimeter=14 units. Area=12 sq units."),
    ]),
  ],
  # U5: Statistics & Probability
  [
    s("Statistical Questions", [
      ("Which is statistical? (A) How old am I? (B) How old are students in my class?", "Think: one answer vs. many answers", "(B). It expects varied answers — a distribution of ages. (A) has exactly one answer for any person."),
      ("Write a statistical question about 6th graders' sleep habits.", "Think: must expect varied answers", "Example: 'How many hours of sleep do 6th graders get on school nights?' Expects a range of answers."),
      ("Classify: 'Today's temperature?' vs. 'Temperatures recorded last month?'", "Think: single value vs. distribution", "First: non-statistical (one answer). Second: statistical (many measurements to analyze)."),
      ("Why must a statistical question anticipate variability?", "Think: purpose of statistics", "Statistics analyzes patterns in varied data. If there's no variability, there's nothing to analyze. Statistical questions need a dataset to answer them."),
    ]),
    s("Dot Plots & Histograms", [
      ("Dot plot: 7 students scored 80, 3 scored 85, 5 scored 90. Describe the distribution.", "Think: shape, center, spread", "Peak at 80. Range: 10 points. Most scores are at the lower end."),
      ("What is the difference between a dot plot and a histogram?", "Think: individual vs. grouped", "Dot plot: shows each data point; good for small datasets. Histogram: groups data into intervals with bars; better for larger datasets."),
      ("Histogram: intervals 0–10, 10–20, 20–30 with frequencies 5,12,8. Where is most data?", "Think: tallest bar", "Interval 10–20 (frequency 12) has the most data."),
      ("Create a dot plot from: 3,5,3,7,5,3,8,5", "Think: number line + stacked dots", "Number line 3–8. Above 3: ●●●. Above 5: ●●●. Above 7: ●. Above 8: ●. Clusters at 3 and 5."),
    ]),
    s("Box Plots", [
      ("Data: 10,15,20,25,30,35,40. Find Q1, Median, Q3, IQR.", "Think: median splits data; Q1/Q3 split each half", "Median=25. Q1=15. Q3=35. IQR=20."),
      ("What five numbers make a box plot?", "Think: five-number summary", "Minimum, Q1, Median, Q3, Maximum."),
      ("Box plot: Min=2, Q1=5, Median=9, Q3=14, Max=20. Find IQR and explain.", "Think: IQR = Q3 − Q1", "IQR = 9. The middle 50% of data spans 9 units."),
      ("Why are box plots useful for comparing datasets?", "Think: quick visual comparison", "They show center, spread, range, and outliers at a glance — allowing quick comparison between groups."),
    ]),
    s("Mean, Median, Mode, Range", [
      ("Find mean, median, mode, range: 4,7,7,9,13", "Think: average, middle, most frequent, max−min", "Mean=8. Median=7. Mode=7. Range=9."),
      ("How does adding an outlier (10) to {85,92,78,96,92,74} affect mean vs. median?", "Think: mean is sensitive to outliers", "Mean drops from ~86 to ~75. Median barely changes from 88.5 to 85. Mean is far more affected."),
      ("When is the median a better measure than the mean?", "Think: skewed data or outliers", "When data is skewed or has outliers — e.g., median income better represents typical earnings than mean income inflated by billionaires."),
      ("A dataset has no mode; another has two modes. What does each suggest?", "Think: frequency patterns", "No mode: all values equally frequent. Two modes (bimodal): two equally most-common values — often suggests two subgroups in the data."),
    ]),
    s("Data Distributions", [
      ("Describe a skewed-right distribution.", "Think: where is the tail?", "Most data clusters at lower values; tail extends right toward high values. Mean > median. Example: income data."),
      ("What does a symmetric distribution look like?", "Think: mirror image around center", "Both sides mirror each other. Mean ≈ median ≈ mode. Bell-shaped curves are symmetric."),
      ("Two datasets: same mean of 50. Range A=10, Range B=80. What does this tell you?", "Think: same center, different spread", "Same average but very different variability. A is tightly clustered; B is widely spread. Range measures variability."),
      ("A student says 'the most popular value is the mean.' Is this correct?", "Think: mode vs. mean", "No. The most frequent value is the MODE. The mean is the arithmetic average. These are usually different."),
    ]),
  ],
]

print("G6 math complete")

P[6]["science"] = [
  # U1: Matter
  [
    s("Atoms and Molecules",[
      ("What is an atom? Name its three subatomic particles and their charges.","Think: protons, neutrons, electrons","Atom = smallest unit of an element. Protons (+) and neutrons (neutral) in nucleus; electrons (−) orbit outside. Number of protons = atomic number = the element."),
      ("What is a molecule? Give two examples.","Think: two or more atoms bonded","H₂O (water: 2H+1O), CO₂ (2O+1C). A molecule is two or more atoms chemically bonded together."),
      ("What is the difference between an element and a compound?","Think: one type vs. two or more types bonded","Element: one type of atom (gold, oxygen). Compound: two or more elements chemically bonded (water H₂O, salt NaCl). Compounds have completely different properties than their component elements."),
      ("Water puts out fires, yet hydrogen and oxygen are both reactive/flammable. What does this illustrate?","Think: compounds vs. their elements","Compounds have entirely different properties than the elements that form them. Chemical bonding creates new substances with new characteristics — this is why H₂O is so different from H₂ and O₂."),
    ]),
    s("States of Matter",[
      ("What are the four states of matter? Describe particle arrangement in each.","Think: solid, liquid, gas, plasma","Solid: tightly packed, fixed positions. Liquid: close, can flow. Gas: far apart, fill container. Plasma: high-energy ionized gas (stars, lightning)."),
      ("What happens to water molecules as you heat ice from −10°C to 110°C?","Think: solid → liquid → gas; energy goes into phase change","Ice: molecules vibrate in place. At 0°C: melt — molecules flow. At 100°C: boil — molecules escape as steam. Temperature pauses during each phase change."),
      ("What is the difference between evaporation and boiling?","Think: surface vs. bulk","Evaporation: surface molecules escape at any temperature. Boiling: molecules throughout the liquid gain enough energy to escape at the boiling point. Both convert liquid to gas."),
      ("Why does a gas fill its container but a solid doesn't?","Think: particle motion and forces","Gas particles move fast and have no strong attractions — they spread to fill all available space. Solid particles are held tightly by intermolecular forces and vibrate in fixed positions."),
    ]),
    s("Physical vs. Chemical Changes",[
      ("Classify: cutting paper, burning wood, melting ice, rusting iron, dissolving sugar.","Think: same substance = physical; new substance = chemical","Physical: cutting paper, melting ice, dissolving sugar. Chemical: burning wood, rusting iron. New substances with different properties = chemical change."),
      ("What are four signs a chemical change has occurred?","Think: evidence of new substance formation","Color change, gas production (bubbles), temperature change, precipitate formation, or odor change. Multiple signs = strong evidence of chemical change."),
      ("Why is dissolving sugar a physical change?","Think: can you recover the original substance?","Sugar molecules are still intact — just dispersed in water. Evaporate the water and sugar remains. No new substance formed. Physical changes are reversible."),
      ("A student mixes baking soda and vinegar. What observations indicate a chemical change?","Think: what happens when they react?","Bubbles (CO₂ produced), temperature change, new substances formed (sodium acetate, water, CO₂). Multiple signs confirm a chemical change."),
    ]),
    s("Conservation of Mass",[
      ("What is the Law of Conservation of Mass?","Think: matter cannot be created or destroyed","Total mass before a chemical reaction = total mass after. Atoms rearrange into new molecules but the total count of each atom stays the same. Proposed by Lavoisier (1789)."),
      ("Before reaction: 80g total. After: 40g solid + 30g gas. Is mass conserved?","Think: add up all products including gases","40g + 30g = 70g ≠ 80g. If the gas escaped, mass appears lost. All products must be captured. If all products collected, mass is conserved (missing 10g was additional gas)."),
      ("A candle burns and the wax disappears. Where did the mass go?","Think: combustion products are gases","Carbon and hydrogen in the wax reacted with oxygen to form CO₂ and water vapor, which dispersed into the air. The mass didn't disappear — it became gases. Total mass is conserved."),
      ("Why is conservation of mass useful for chemists?","Think: predicting amounts in reactions","Allows prediction of how much product forms from given reactants, or how much reactant is needed for a desired amount of product. It is the foundation of quantitative chemistry (stoichiometry)."),
    ]),
    s("Properties of Materials",[
      ("What is the difference between a physical and a chemical property? Give two examples of each.","Think: observable without changing vs. describes reactivity","Physical: color, density, melting point, conductivity. Chemical: flammability, reactivity with acid, ability to rust. Chemical properties describe how a substance changes into a new one."),
      ("A material is: flexible, conducts electricity, high melting point, shiny. What material?","Think: what has all four properties?","These describe metals (e.g., copper, aluminum). Metals are ductile, electrically conductive, have high melting points, and have metallic luster."),
      ("Why is density useful for identifying materials?","Think: density is constant for pure substances","Every pure substance has a unique density at a given temperature. Measuring density can identify an unknown substance and explains why some materials float and others sink."),
      ("What is the difference between hardness and brittleness? Can something be both?","Think: resistance to scratch vs. tendency to crack","Hardness: resists scratching (diamond = hardest). Brittleness: tendency to crack without bending (glass). Yes — diamond is very hard but brittle; it can shatter from a sharp impact."),
    ]),
  ],
  # U2: Earth & Space
  [
    s("Weathering and Erosion",[
      ("What is the difference between weathering and erosion?","Think: breaking down vs. moving away","Weathering: breaking rock in place (physical or chemical). Erosion: movement of weathered rock/sediment by water, wind, ice, or gravity. Weathering first; erosion moves the material."),
      ("Give one example each of physical and chemical weathering.","Think: mechanics vs. chemistry","Physical: freeze-thaw (water enters cracks, freezes, expands, breaks rock). Chemical: acid rain dissolving limestone, iron oxidizing (rust). Physical changes shape; chemical changes composition."),
      ("How does running water cause both weathering and erosion?","Think: water abrades and transports","Water abrades rock surfaces (physical weathering), chemically weathers with dissolved acids, and transports sediment (erosion). The Grand Canyon was formed primarily by water erosion over millions of years."),
      ("What is deposition and how does it relate to erosion?","Think: erosion picks up; deposition drops","Deposition: eroded sediment is dropped when the transporting agent loses energy. River deltas form where rivers slow down at the ocean and deposit sediment. Erosion and deposition are two parts of the same process."),
    ]),
    s("Rock Cycle",[
      ("What are the three rock types and how is each formed?","Think: igneous, sedimentary, metamorphic","Igneous: cooled magma/lava. Sedimentary: compressed sediment layers. Metamorphic: existing rock changed by heat and pressure."),
      ("How can igneous rock become sedimentary? Trace the steps.","Think: follow the rock cycle","Igneous exposed at surface → weathered into sediment → transported → deposited in layers → buried, compressed, cemented → sedimentary rock."),
      ("Why is it called a 'cycle'?","Think: no beginning or end","Any rock type can transform into any other. Weathering, erosion, heat, pressure, and melting continuously recycle Earth's materials. No rock is permanent."),
      ("What is the difference between magma and lava?","Think: location matters","Both are molten rock. Magma: below Earth's surface. Lava: magma that has reached the surface through volcanic activity."),
    ]),
    s("Plate Tectonics Introduction",[
      ("What is the theory of plate tectonics?","Think: Earth's crust in moving pieces","Earth's lithosphere is divided into plates that float on the asthenosphere and move ~centimeters per year. Their movement causes earthquakes, volcanoes, and mountain building."),
      ("What are the three plate boundary types and features formed at each?","Think: converge, diverge, transform","Convergent: mountains, trenches, volcanoes. Divergent: mid-ocean ridges, rift valleys. Transform: fault lines, earthquakes."),
      ("Name three pieces of evidence supporting plate tectonics.","Think: multiple independent lines of evidence","Matching coastlines of continents, matching fossils across oceans, matching rock formations, magnetic striping on ocean floors (seafloor spreading), GPS measurements of plates moving today."),
      ("What drives tectonic plate movement?","Think: heat from Earth's interior","Convection currents in the mantle (hot rock rises, cools, sinks) create slow churning that moves plates. Ridge push and slab pull also contribute."),
    ]),
    s("Earth's Layers",[
      ("Name Earth's four layers from outside to center and describe each.","Think: crust, mantle, outer core, inner core","Crust: thin rocky outer layer. Mantle: thick semi-solid rock (~2,900 km). Outer core: liquid iron and nickel. Inner core: solid iron and nickel (~5,100°C)."),
      ("Why is the inner core solid even though it's extremely hot?","Think: pressure vs. temperature","Enormous pressure from the weight of all layers above compresses the iron into a solid despite temperatures high enough to melt iron at normal pressure."),
      ("How do scientists know what's inside Earth if they've never drilled that deep?","Think: seismic wave analysis","Seismic waves (P and S waves) from earthquakes change speed/direction based on density and state of materials. S-waves can't travel through liquids — this revealed the liquid outer core."),
      ("What is the difference between the lithosphere and asthenosphere?","Think: rigid vs. flowing","Lithosphere: rigid outer layer (crust + upper mantle) divided into tectonic plates. Asthenosphere: partially molten zone just below where rock can flow slowly. Plates 'float' on the asthenosphere."),
    ]),
    s("Geologic Time",[
      ("How old is Earth and how do scientists know?","Think: radiometric dating","~4.6 billion years old. Scientists use radiometric dating (measuring radioactive isotope decay, e.g., uranium-lead) of the oldest rocks and meteorites."),
      ("What is the law of superposition?","Think: older layers are deeper","In undisturbed rock layers, older rocks are at the bottom and younger rocks at the top. Scientists read rock strata like pages of a history book."),
      ("What are the major divisions of geologic time from largest to smallest?","Think: Eon → Era → Period → Epoch","Eon → Era → Period → Epoch. Divisions mark major changes in the fossil record (mass extinctions, new life forms)."),
      ("What does a fossil tell us about geologic time?","Think: biological timestamps in rock","Fossils record what organisms lived during specific rock layers. Index fossils (found in specific time periods) help date rock layers. The sequence of fossils through strata shows the history of life on Earth."),
    ]),
  ],
  # U3: Ecosystems
  [
    s("Food Webs and Food Chains",[
      ("What is the difference between a food chain and a food web?","Think: linear vs. network","Food chain: linear sequence (grass→grasshopper→frog→hawk). Food web: overlapping network of many food chains. Food webs are more realistic."),
      ("In: grass→rabbit→fox→eagle. Identify the producer and each consumer level.","Think: producers make food; consumers eat","Producer: grass. Primary consumer: rabbit. Secondary: fox. Tertiary: eagle."),
      ("What would happen to the fox population if rabbit populations crashed?","Think: energy flows up the chain","Fox numbers decrease — less food. Eagle numbers also decrease. Disruptions cascade through food webs."),
      ("Why are there typically fewer top predators than plants?","Think: 10% energy rule","Only ~10% of energy transfers between trophic levels. 1000 lbs of grass → 100 lbs of rabbits → 10 lbs of foxes. Energy loss limits higher trophic level populations."),
    ]),
    s("Energy Flow",[
      ("What is the 10% rule in ecosystems?","Think: how much energy passes upward","Only ~10% of energy at one trophic level transfers to the next. The other 90% is used for metabolism, released as heat, or remains in unconsumed parts."),
      ("Describe an energy pyramid. What does each level represent?","Think: wider = more energy","Base: producers (most energy). Level 2: primary consumers. Level 3: secondary consumers. Apex: top predators (least energy). Each level has less energy and fewer organisms."),
      ("Why do ecosystems have more plants than animals?","Think: energy availability at each level","Producers capture solar energy directly. Each consumer level has less available energy. More energy supports more organisms — so the base of the pyramid is widest."),
      ("What is the original energy source for almost all food chains?","Think: what powers photosynthesis?","The Sun. Plants capture solar energy via photosynthesis, converting it to chemical energy (glucose) that flows through the ecosystem as organisms eat one another."),
    ]),
    s("Biodiversity",[
      ("What is biodiversity and why is it important?","Think: variety of life = ecosystem resilience","Biodiversity = variety of species, genes, and ecosystems. High biodiversity increases ecosystem stability, provides resources, and maintains ecosystem services (clean air, water)."),
      ("What is a keystone species? Give one example.","Think: disproportionate impact relative to abundance","A keystone species has outsized effect on its ecosystem. Example: sea otters eat sea urchins; without otters, urchins destroy kelp forests, collapsing the ecosystem."),
      ("Why does habitat loss threaten biodiversity most severely?","Think: species need space to survive","Habitat destruction eliminates living space, food, shelter, and breeding grounds. Even small habitat fragments may not support viable populations. It is the #1 cause of extinction worldwide."),
      ("What is an invasive species? Give one example and its impact.","Think: non-native species disrupting native ecosystems","Species introduced outside its native range that spreads aggressively. Example: kudzu vine in the southeastern U.S. — covers and kills native plants by blocking sunlight. Without natural predators, invasives often dominate."),
    ]),
    s("Ecosystem Services",[
      ("What are ecosystem services? Name four types.","Think: benefits healthy ecosystems provide to humans","Provisioning (food, water), Regulating (clean air/water, climate), Cultural (recreation, spiritual), Supporting (soil formation, photosynthesis, nutrient cycling)."),
      ("How do wetlands provide ecosystem services? Give two examples.","Think: what do wetlands do for free?","Flood control: absorb excess water like a sponge. Water purification: filter pollutants. Also: wildlife habitat, storm surge protection, carbon storage."),
      ("Why is pollination an ecosystem service? What if pollinators disappeared?","Think: fruit and seed production depends on them","~75% of flowering plants need animal pollinators. Without them: most fruits, vegetables, and nuts would decline dramatically, threatening food security and entire food chains."),
      ("Why is it important to assign economic value to ecosystem services?","Think: what would it cost to replace them?","Recognizing their economic value (estimated $125+ trillion/year globally) helps decision-makers understand the true cost of environmental destruction and justify conservation investment."),
    ]),
    s("Human Impact on Ecosystems",[
      ("What are three major ways humans negatively impact ecosystems?","Think: habitat, pollution, climate","(1) Habitat destruction. (2) Pollution (chemical runoff, plastic, air). (3) Climate change (rising temperatures disrupt ecosystems). Also: overfishing, invasive species introduction."),
      ("Give one example each of air, water, and land pollution.","Think: three different environments","Air: CO₂/methane from fossil fuels. Water: agricultural runoff (fertilizers) entering streams. Land: plastic waste in landfills, toxic industrial waste."),
      ("What is deforestation and what are its consequences?","Think: cutting forests cascades through systems","Habitat loss, carbon release (climate change), soil erosion, disrupted water cycle, loss of biodiversity and ecosystem services."),
      ("Give one example of a human action that positively impacts ecosystems.","Think: conservation and restoration","Reforestation, creation of national parks/marine reserves, pollution cleanup, sustainable fishing regulations, wetland restoration, banning harmful pesticides."),
    ]),
  ],
  # U4: Life Science
  [
    s("Cell Structure and Function",[
      ("State the three principles of cell theory.","Think: the foundational theory of biology","(1) All living things are made of cells. (2) The cell is the basic unit of life. (3) All cells come from pre-existing cells."),
      ("What three structures are found in ALL cells?","Think: universal cell components","Cell membrane (controls entry/exit), cytoplasm (fluid interior), and DNA (genetic material). These are present in every cell — plant, animal, or bacteria."),
      ("What is the function of the cell membrane?","Think: selective gatekeeper","Controls what enters and exits the cell (selectively permeable). Allows needed substances (nutrients, oxygen) in and wastes out, maintaining stable internal conditions (homeostasis)."),
      ("Name three structures in plant cells but NOT animal cells and their functions.","Think: what extra needs do plants have?","(1) Cell wall: rigid support and protection. (2) Chloroplasts: photosynthesis. (3) Large central vacuole: stores water, maintains turgor pressure keeping the plant upright."),
    ]),
    s("Photosynthesis Basics",[
      ("Write the overall equation for photosynthesis in words.","Think: inputs and outputs with light","Carbon dioxide + Water + Light energy → Glucose + Oxygen."),
      ("Where does photosynthesis occur and what captures light?","Think: organelle and pigment","In chloroplasts. Chlorophyll (the green pigment) captures light energy — absorbs red and blue light, reflects green (why plants look green)."),
      ("Why is photosynthesis important for nearly all life on Earth?","Think: foundation of food chains and oxygen","It converts solar energy into chemical energy (glucose) — the base of almost all food chains. It also produces the oxygen most organisms breathe."),
      ("A plant is kept in a dark room for a week. What happens to its photosynthesis?","Think: what does photosynthesis require?","Photosynthesis stops — it requires light. The plant uses stored glucose but can't make new glucose. Eventually leaves yellow and the plant weakens. All three inputs (CO₂, water, light) are required."),
    ]),
    s("Reproduction",[
      ("What is the difference between sexual and asexual reproduction?","Think: one parent vs. two; identical vs. varied offspring","Asexual: one parent, genetically identical offspring. Sexual: two parents combine genetic material, producing genetically varied offspring. Sexual reproduction increases diversity."),
      ("Give two examples of asexual reproduction in plants.","Think: runners, cuttings, budding, spores","(1) Runners: strawberry plants send stems that root and form new plants. (2) Cuttings: a plant branch rooted in soil grows into a new plant. Both produce clones of the parent."),
      ("Why is genetic diversity from sexual reproduction important for species survival?","Think: variation = insurance against change","If all individuals are genetically identical (asexual), a new disease could wipe out the entire population. Genetic variation means some individuals may have resistance — allowing the species to survive."),
      ("What is fertilization?","Think: union of two sex cells","The joining of sperm (male) and egg (female) to form a zygote. The zygote has genetic material from both parents. In plants, pollen fertilizes the egg in the ovule, forming a seed."),
    ]),
    s("Heredity Overview",[
      ("What is heredity? What carries hereditary information?","Think: passing traits via DNA","Heredity = passing traits from parents to offspring. DNA carries genetic information in genes. Each gene has instructions for a specific trait."),
      ("What is a gene? What is a chromosome?","Think: instruction vs. thread of instructions","Gene: a segment of DNA coding for a specific trait/protein. Chromosome: a long coiled DNA strand containing many genes. Humans have 46 chromosomes (23 pairs) in each body cell."),
      ("What is the difference between inherited traits and learned behaviors?","Think: coded in DNA vs. acquired through experience","Inherited: eye color, blood type (genetic). Learned: riding a bike, speaking a language (acquired through experience, not genetic). Both shape who we are."),
      ("Why do siblings look similar but not identical (unless identical twins)?","Think: random gene combination","Siblings inherit from the same two parents, but which genes each sibling receives is random. The unique combination produces unique individuals. Identical twins come from one fertilized egg — same DNA."),
    ]),
    s("Classification of Organisms",[
      ("What is taxonomy? List the taxonomic ranks from broadest to most specific.","Think: organizing life by shared characteristics","Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species. Memory: Dear King Philip Came Over For Good Soup."),
      ("What are the three domains of life? Give one example from each.","Think: Bacteria, Archaea, Eukarya","Bacteria: E. coli. Archaea: methanogens (extremophiles). Eukarya: all plants, animals, fungi, and protists (cells with a nucleus)."),
      ("What defines a species?","Think: ability to interbreed and produce fertile offspring","A species is a group of organisms that can interbreed and produce fertile offspring. Horses and donkeys can breed but produce sterile mules — they are different species."),
      ("Why do scientists use binomial nomenclature instead of common names?","Think: universal vs. language-specific","Scientific names (genus + species in Latin) are universal — the same worldwide. 'Mountain lion' = 'cougar' = 'puma' — all the same animal (Puma concolor). Scientific names prevent confusion."),
    ]),
  ],
]
print("G6 science complete")

P[6]["ela"] = [
  # U1 Reading Literature
  [
    s("Story elements: plot, setting, character",[
      ("What are the five parts of a plot diagram?","Think: exposition through resolution","Exposition (introduces characters/setting), Rising Action (builds tension), Climax (turning point), Falling Action (tension decreases), Resolution (conflict resolved)."),
      ("What is the difference between the setting and mood of a story?","Think: where/when vs. emotional atmosphere","Setting: time and place of the story. Mood: emotional atmosphere created by setting, word choice, and events (eerie, joyful, tense). Setting often creates mood."),
      ("What is a round character vs. a flat character?","Think: complex vs. one-dimensional","Round: complex, shows many traits, changes over the story. Flat: one-dimensional, doesn't change. Both serve important narrative purposes."),
      ("How does first-person vs. third-person point of view affect how we read a story?","Think: who tells the story and what they know","First-person ('I'): intimate but limited to one perspective, may be unreliable. Third-person omniscient: narrator knows all characters' thoughts — broadest view. Point of view shapes what readers know and trust."),
    ]),
    s("Theme and central message",[
      ("What is a theme? How is it different from the subject?","Think: topic vs. author's message about that topic","Subject: what the book is about (friendship). Theme: the deeper message ('True friendship requires sacrifice'). Themes are complete ideas, not single words."),
      ("Write two common themes as complete statements.","Think: universal truths about human experience","'Courage means doing what's right even when it's hard.' 'Power corrupts those who seek it for the wrong reasons.' Themes connect stories to real human experiences."),
      ("How does a character's decisions reveal theme?","Think: theme shown through consequences of choices","Authors reveal theme through what characters choose and what happens as a result. If a character learns honesty matters more than winning, the theme might be 'honesty has greater value than victory.'"),
      ("Can one story have multiple themes?","Think: complex stories explore several ideas","Yes. Harry Potter explores: friendship, love as powerful force, choices defining us, and the importance of standing up to authority. Complex stories weave multiple themes together."),
    ]),
    s("Point of view",[
      ("Identify POV: 'I walked into the room and froze. Something was wrong.'","Think: which pronoun?","First-person — 'I' shows the narrator is a character. We only know what this character sees, thinks, and feels."),
      ("What is the difference between first-person and third-person limited?","Think: 'I' vs. 'he/she' following one character","First-person: narrator IS a character, uses 'I.' Third-person limited: outside the story, uses 'he/she,' but follows only one character's thoughts. Both limit us to one perspective."),
      ("How would a story about a fire differ if told by the firefighter vs. the homeowner?","Think: same event, different emotional focus","Firefighter: technical challenge, professional danger. Homeowner: personal loss, fear. Same event produces different stories depending on who tells it."),
      ("Why might an author choose an unreliable narrator?","Think: strategic limitation","To create suspense or dramatic irony, to explore how perception differs from reality, or to show biased/limited understanding. Unreliable narrators make readers question what is 'really' happening."),
    ]),
    s("Comparing texts",[
      ("What do you look for when comparing two texts on the same topic?","Think: similarities and differences across multiple dimensions","Author's purpose, point of view, evidence and support, tone, structure, and conclusion. Comparison reveals different values and approaches."),
      ("Two articles about wolf reintroduction — one from a rancher, one from a biologist. How might they differ?","Think: perspective shapes emphasis","Rancher: livestock losses, economic harm. Biologist: ecological benefits, scientific data. Same event — opposite perspectives based on interests and expertise."),
      ("What is the difference between comparing themes and comparing authors' purposes?","Think: what the text says vs. why it was written","Theme: the central message about life. Purpose: why the author wrote it (inform, persuade, entertain). A news article and a novel can share a theme but have completely different purposes."),
      ("How do you write a strong comparison essay?","Think: point-by-point or block method","Address how both texts are similar and different on the same points (subject, tone, evidence). Use transitions: 'similarly,' 'in contrast,' 'both authors.' A strong comparison makes a clear argument about what the comparison reveals."),
    ]),
    s("Figurative language",[
      ("What is the difference between simile and metaphor? Give one original example of each.","Think: simile uses 'like' or 'as'","Simile: 'Her laugh was like music.' Metaphor: 'Her laugh was music.' Both compare unlike things; metaphors are more direct."),
      ("What is personification? Give an original example.","Think: giving human qualities to non-human things","'The old oak tree stretched its arms toward the sky.' Creates vivid imagery by attributing human traits to objects."),
      ("What is hyperbole? Why do authors use it?","Think: extreme exaggeration not meant literally","'I've told you a million times!' Used for humor, emphasis, and conveying strong emotion more powerfully than literal language."),
      ("Identify the device and effect: 'The thunder rumbled its warning.'","Think: what human quality does thunder have?","Personification. Thunder is given the human ability to 'warn,' creating an ominous, threatening mood. The storm feels intentional and dangerous."),
    ]),
  ],
  # U2 Informational Text
  [
    s("Main idea and supporting details",[
      ("What is the difference between a main idea and a topic sentence?","Think: whole text vs. one paragraph","Topic sentence: main point of one paragraph. Main idea: central point of the entire text. Topic sentences support the main idea; the main idea emerges from all of them."),
      ("What is the main idea? 'Sea turtles face many threats: poaching, plastic pollution, and rising temperatures affecting hatchlings.'","Think: what one point do all details support?","Sea turtles face multiple serious threats to their survival. Every detail supports this central claim."),
      ("What is the difference between a main idea and a summary?","Think: one sentence vs. condensed overview","Main idea: one sentence capturing the central point. Summary: condensed version covering all major points. A summary supports and expands on the main idea."),
      ("How do you identify relevant vs. irrelevant supporting details?","Think: do they directly support the main idea?","Relevant: directly explain, prove, or illustrate the main idea. Test each: 'Does this help me understand WHY the main idea is true?' Irrelevant details mention the topic but don't support the central claim."),
    ]),
    s("Author's purpose",[
      ("What are the three main author's purposes? Give one text type for each.","Think: PIE — Persuade, Inform, Entertain","Persuade: editorial, opinion piece. Inform: textbook, news article. Entertain: novel, short story. Most texts serve multiple purposes simultaneously."),
      ("How do you identify an author's purpose?","Think: look at word choice, evidence, format, tone","Opinions + emotional language = Persuade. Objective facts = Inform. Story with literary techniques = Entertain. Purpose shapes every author choice."),
      ("What is the difference between author's purpose and author's point of view?","Think: why they wrote it vs. their perspective","Purpose: reason the text was written (inform, persuade, entertain). Point of view: the author's perspective or stance. An informational text can have a clear point of view."),
      ("'Every student should have a school garden. Gardens teach responsibility, nutrition, and science.' What is the purpose and how do you know?","Think: opinion + reasons = persuade","Purpose: persuade. Clues: 'Every student should' (opinion), followed by reasons. Persuasive writing states a claim and supports it with reasoning."),
    ]),
    s("Text structure",[
      ("Name five common informational text structures.","Think: HOW is information organized?","Description, Sequence/Chronological, Compare/Contrast, Cause/Effect, Problem/Solution."),
      ("'Tigers faced habitat loss, poaching, and conflict. As a result, only ~3,900 remain.' What structure?","Think: signal words and logic","Cause/Effect. Signal words: 'As a result.' Explains what caused population decline and the resulting outcome."),
      ("What signal words indicate compare/contrast structure?","Think: similarity vs. difference signals","Similarities: similarly, likewise, both, also. Differences: however, in contrast, unlike, whereas, but, on the other hand."),
      ("Why does understanding text structure help comprehension?","Think: structure = map for reading","Knowing the structure helps you predict what's coming next and understand how ideas relate. Problem/solution structure tells you to look for the problem first, then solutions."),
    ]),
    s("Evidence and reasoning",[
      ("What is the difference between a claim and evidence?","Think: what you argue vs. what proves it","Claim: an assertion requiring support ('Schools should start later'). Evidence: facts, data, research, or examples that support the claim."),
      ("Name three types of evidence an author might use.","Think: what makes an argument convincing?","Statistics/data, expert quotes, examples/case studies, logical cause-and-effect reasoning. Strong arguments use multiple types."),
      ("How do you evaluate whether evidence is strong?","Think: relevant, credible, and sufficient","Strong evidence is: relevant (directly supports the claim), credible (reliable source), current (recent), and sufficient (enough to be convincing)."),
      ("Identify circular reasoning: 'School uniforms are good because uniforms are beneficial.'","Think: using the claim as its own evidence","The claim ('uniforms are good') is used as its own evidence ('uniforms are beneficial') — just restated in different words. No actual reasoning provided for why they are beneficial."),
    ]),
    s("Summarization",[
      ("What is the difference between a summary and a paraphrase?","Think: whole text vs. one passage","Summary: condenses the entire text to its most important points. Paraphrase: restates a specific passage in your own words at similar length. Both require rephrasing, not copying."),
      ("What should you include and exclude in a summary?","Think: main ideas yes; minor details no","Include: main idea, major supporting points, conclusion. Exclude: minor details, most examples, direct quotes, personal opinions."),
      ("What is plagiarism in summarizing and how do you avoid it?","Think: using someone's ideas without credit","Plagiarism: using others' ideas as your own. Avoid by: rephrasing (don't just swap synonyms), cite the source, focus on main ideas rather than copying sentence structure."),
      ("Summarize in one sentence: 'Exercise reduces anxiety and depression. It also improves sleep and boosts self-esteem.'","Think: combine all points into one statement","Regular exercise significantly improves mental health by reducing anxiety and depression while enhancing sleep quality and self-esteem."),
    ]),
  ],
  # U3 Writing (5 topics)
  [
    s("Narrative writing",[
      ("What are the five key elements of a strong narrative?","Think: building blocks every story needs","(1) Engaging hook. (2) Well-developed characters. (3) Descriptive setting. (4) Conflict and rising action. (5) Satisfying resolution."),
      ("What is 'showing vs. telling'? Rewrite: 'Maria was nervous.'","Think: specific sensory details vs. labels","'Maria's hands trembled as she smoothed her notes for the fourth time. Her mouth had gone completely dry.' Show actions, sensory details, body language — don't just name the feeling."),
      ("What is a narrative hook and why is it important?","Think: opening that grabs the reader","A hook immediately engages the reader. Types: action (plunge into the scene), question, dialogue, or description. Without a hook, readers may disengage before the story develops."),
      ("What are the rules for writing dialogue?","Think: punctuation and paragraph conventions","Quotation marks enclose spoken words. Punctuation goes inside closing quotes. New speaker = new paragraph. Include a dialogue tag or action beat to identify the speaker."),
    ]),
    s("Informational/explanatory writing",[
      ("What is the purpose of informational writing?","Think: explain vs. tell a story","Explains, describes, or analyzes a topic to inform the reader using facts, examples, and evidence — not story elements. Objective, not personal."),
      ("What makes a strong informational thesis statement?","Think: topic + specific controlling idea","States what you're writing about AND the specific point you'll make. Weak: 'This essay is about recycling.' Strong: 'Recycling reduces waste, conserves resources, and creates economic benefits that outweigh the inconvenience.'"),
      ("What is the difference between facts and opinions?","Think: provable vs. personal view","Fact: verifiable ('The Great Wall stretches 13,000+ miles'). Opinion: personal judgment ('It is the most impressive structure ever built'). Informational writing relies on facts."),
      ("How should body paragraphs in an informational essay be organized?","Think: one main idea per paragraph","Each paragraph: (1) topic sentence stating the main point, (2) supporting evidence, (3) explanation of how the evidence supports the point, (4) transition to the next paragraph."),
    ]),
    s("Argument writing",[
      ("What are the three key components of a strong argument?","Think: claim + evidence + reasoning","Claim: your clear position. Evidence: facts, data, or examples supporting it. Reasoning: explains HOW the evidence supports the claim. Without reasoning, evidence is just a list of facts."),
      ("What is a counterargument and why include one?","Think: the opposing side's best point","A counterargument is the strongest opposing view. Including and refuting it shows intellectual honesty, builds credibility, and strengthens your argument."),
      ("Identify the logical fallacy: 'Everyone eats at Taco Bell — it must be the best restaurant.'","Think: popularity doesn't prove quality","Ad populum (appeal to popularity) fallacy. Many people doing/believing something doesn't make it good or true."),
      ("What is the difference between persuasive and argument writing?","Think: emotion vs. evidence-based reasoning","Persuasive: may use emotional appeals and one-sided reasoning. Argument: uses evidence, logic, and acknowledges counterarguments. Academic argument is closer to debate writing than emotional persuasion."),
    ]),
    s("Research process",[
      ("What are the steps of the research process?","Think: from question to finished product","(1) Choose topic/question. (2) Gather sources. (3) Evaluate credibility. (4) Take notes. (5) Outline. (6) Write and revise. (7) Cite sources."),
      ("What makes a source credible? Name four criteria.","Think: how do you decide to trust it?","Authority (expert/credible org), Accuracy (verifiable facts), Currency (recently published), Purpose (informative, not commercial). .gov and .edu sites are generally more reliable."),
      ("What is the difference between a primary and secondary source?","Think: original vs. analysis of original","Primary: firsthand, from the time period (diary, speech, original research). Secondary: analyzes primary sources (textbook, biography). Both are useful — primary gives direct evidence; secondary provides analysis."),
      ("What is plagiarism and how do you avoid it?","Think: using someone's work without credit","Plagiarism = presenting others' words or ideas as your own. Avoid: always cite sources, paraphrase (restate in your own words), use quotation marks for direct quotes."),
    ]),
    s("Revision and editing",[
      ("What is the difference between revising and editing?","Think: big picture vs. small details","Revising: improve content, organization, argument, and clarity. Editing: fix grammar, spelling, punctuation. Always revise first — no point perfecting a sentence you might cut."),
      ("What questions should you ask when revising your own writing?","Think: content, organization, clarity, audience","Does my opening hook the reader? Is my thesis clear? Does each paragraph have a clear main idea? Is my evidence convincing? Is my conclusion strong?"),
      ("What is a peer review and how do you give useful feedback?","Think: specific, constructive, balanced","Peer review = evaluating a classmate's writing. Useful feedback is specific ('Your thesis doesn't state your argument' not just 'confusing'), balanced (strengths AND areas to improve), and respectful."),
      ("Name three common grammar mistakes in 6th grade writing.","Think: errors specific to this level","(1) Run-on sentences. (2) Comma splices. (3) Subject-verb disagreement ('Everyone in the teams are...'). All three can be caught in the editing phase."),
    ]),
  ],
  # U4 Language Conventions (4 topics)
  [
    s("Parts of speech review",[
      ("Name the 8 parts of speech and give one example of each.","Think: noun, pronoun, verb, adjective, adverb, preposition, conjunction, interjection","Noun (school), Pronoun (they), Verb (run), Adjective (bright), Adverb (quickly), Preposition (under), Conjunction (but), Interjection (wow!)."),
      ("Identify each word's part of speech: 'She quickly ran through the park.'","Think: label each word's grammatical function","She (pronoun), quickly (adverb), ran (verb), through (preposition), park (noun)."),
      ("What is the difference between an adjective and an adverb?","Think: what does each modify?","Adjective: modifies a noun ('tall building'). Adverb: modifies a verb, adjective, or adverb — often ends -ly ('ran quickly'). Adjectives answer 'what kind?' Adverbs answer 'how?' 'when?' 'where?'"),
      ("What is a conjunction? Give one coordinating and one subordinating example.","Think: joining words and clauses","Coordinating (FANBOYS): 'I like pizza and pasta.' Subordinating: 'Although it rained, we played outside.' Coordinating joins equals; subordinating creates dependent relationships."),
    ]),
    s("Sentence structure",[
      ("What is the difference between simple, compound, and complex sentences?","Think: number and type of clauses","Simple: one independent clause. Compound: two independent clauses joined by conjunction/semicolon. Complex: one independent + one dependent clause."),
      ("What is a run-on sentence? Correct: 'I went to the store I bought milk.'","Think: improperly joined clauses","Two sentences without proper connection. Corrections: (1) Add a period. (2) Add 'and'. (3) Use a semicolon."),
      ("What is a sentence fragment? Correct: 'Running through the park on a sunny afternoon.'","Think: missing subject, verb, or complete thought","Fragment: missing a main clause. Fixed: 'Running through the park on a sunny afternoon, she felt free.'"),
      ("Why is sentence variety important?","Think: monotony vs. engagement","Mixing short and long sentences, varying beginnings, combining simple/compound/complex creates rhythm and keeps readers engaged. Monotonous sentence length dulls the reader."),
    ]),
    s("Punctuation",[
      ("When do you use a comma in a list?","Think: serial/Oxford comma","Use a comma after each item in a series of three or more: 'apples, oranges, and grapes.' The Oxford comma before 'and' prevents ambiguity."),
      ("When do you use a comma with a coordinating conjunction?","Think: FANBOYS joining two independent clauses","Place a comma before a coordinating conjunction when joining two independent clauses: 'I wanted to go, but it was raining.'"),
      ("When do you use an apostrophe? Give one example of each use.","Think: possession or contraction — NOT plurals","Contraction: don't (do not), it's (it is). Possession: Maria's notebook. Common error: using apostrophe for plurals ('three cat's' is wrong)."),
      ("What are the rules for quotation marks in dialogue?","Think: punctuation placement, paragraph rules","Enclose exact spoken words. Punctuation goes INSIDE closing quotes. New speaker = new paragraph. Tag or action beat identifies the speaker."),
    ]),
    s("Vocabulary development",[
      ("What are context clues? Name three types with examples.","Think: clues in surrounding text","(1) Definition: 'The geologist, or rock scientist, ...' (2) Synonym: 'She was elated, thrilled beyond words.' (3) Contrast: 'Unlike her gregarious brother, she was shy.'"),
      ("What is connotation? Give a word with positive and negative connotations.","Think: emotional associations beyond literal meaning","'Slender' (positive), 'scrawny' (negative) — both mean thin but feel different. Connotation shapes tone and character perception."),
      ("What are prefixes and suffixes? Give two examples of each.","Think: morphemes added to root words","Prefix: un- (unhappy), re- (rewrite). Suffix: -ness (happiness), -er (teacher). Learning common affixes helps decode thousands of unfamiliar words."),
      ("What is denotation? How does it differ from connotation?","Think: dictionary meaning vs. emotional meaning","Denotation: literal, dictionary definition. Connotation: emotional associations. 'Home' and 'house' have similar denotations but different connotations — 'home' implies warmth and belonging."),
    ]),
    s("Context clues",[
      ("What are context clues and why are they useful?","Think: surrounding text that hints at meaning","Words and phrases near an unfamiliar word that help readers infer its meaning without stopping to look it up, allowing smoother comprehension."),
      ("Define 'benevolent' from context: 'The benevolent donor gave millions to fund schools for children in need.'","Think: what does someone who gives millions to schools seem like?","Benevolent: kind and generous, wishing good for others. Clue: giving millions to help children describes someone generous and caring."),
      ("'The arid desert received less than 2 inches of rain per year.' What does 'arid' mean?","Think: what kind of climate gets almost no rain?","Arid means extremely dry. The context clue is '2 inches of rain per year' — clearly a very dry environment."),
      ("What is the difference between definition and contrast context clues?","Think: the text either explains or shows the opposite","Definition: text defines the word ('The omnivore, an animal that eats both plants and meat, ...'). Contrast: shows an opposite ('Unlike the calm lake, the turbulent river crashed'). Both help infer meaning from context."),
    ]),
  ],
  # U5 Speaking & Listening (4 topics)
  [
    s("Collaborative discussion",[
      ("What are three norms for productive collaborative discussion?","Think: how groups work effectively","Listen actively (don't interrupt), build on others' ideas, support opinions with evidence, ask clarifying questions, disagree respectfully."),
      ("What does it mean to 'build on someone's comment'? Give an example.","Think: connect your contribution to what was just said","Adding to or extending someone's point. 'I agree with Maya about pollution, and I'd add that plastic also harms sea turtles, which connects to what we studied about food chains.'"),
      ("How do you politely disagree with a classmate in discussion?","Think: acknowledge, then offer your view","'I see your point, but I think...' or 'I understand why you feel that way; however...' Acknowledge their perspective first; use 'I' statements; offer evidence."),
      ("Why is asking clarifying questions important in discussion?","Think: what do questions do for understanding?","Clarifying questions ensure correct understanding, encourage elaboration, and deepen discussion beyond surface responses. 'Can you explain what you mean by...?'"),
    ]),
    s("Presentations",[
      ("What are three key elements of an effective oral presentation?","Think: content, delivery, engagement","(1) Clear organization (intro, body, conclusion). (2) Strong delivery (eye contact, appropriate volume and pace). (3) Audience engagement (relevant content, invite questions, effective visuals)."),
      ("What is the difference between formal and informal speaking?","Think: occasion, audience, word choice","Formal: professional vocabulary, structured delivery, no slang (class presentation). Informal: casual language, contractions, conversational tone (talking to a friend). Context determines appropriateness."),
      ("How do you use body language effectively during a presentation?","Think: what your body communicates","Maintain eye contact (connect with audience), upright posture, natural purposeful gestures. Avoid fidgeting, crossed arms, or reading directly from notes."),
      ("A classmate speaks too fast. What specific advice would you give?","Think: what slows speakers down?","Pause after key points, breathe deeply before starting, mark the script with pause symbols, rehearse with a timer, and focus on speaking TO the audience not at them."),
    ]),
    s("Evaluating speaker's arguments",[
      ("What questions evaluate the strength of a speaker's argument?","Think: claim, evidence, logic, credibility","Is the claim clear? Is evidence credible and relevant? Does reasoning logically connect evidence to claim? Are there logical fallacies? Does the speaker acknowledge opposing views?"),
      ("What is the difference between evaluating content and evaluating delivery?","Think: what they say vs. how they say it","Content: claims, evidence, reasoning, organization. Delivery: clarity, pace, volume, eye contact, body language. Strong presentations have both strong content AND effective delivery."),
      ("'You should exercise daily because all my friends do it and feel great.' What is weak?","Think: what type of evidence is this?","Anecdotal evidence + ad populum fallacy (appeal to popularity). Strong arguments require credible research and data, not just personal experience of a small group."),
      ("How do you take useful notes while listening to a speaker?","Think: capture structure, not every word","Write the main claim first, then key supporting points. Use abbreviations. Don't try to transcribe everything. Note questions that arise. Review immediately after."),
    ]),
    s("Multimedia integration",[
      ("What types of multimedia enhance presentations? Give two examples.","Think: visual, audio, digital elements","Slides (visuals), charts/graphs (show data), videos (demonstrate processes), images (illustrate concepts). Multimedia clarifies and enhances when chosen to serve the message."),
      ("When is a visual aid helpful vs. distracting?","Think: does it add value or compete?","Helpful: explains something difficult verbally (diagram), or shows data clearly (bar chart). Distracting: too many words on slides (audience reads instead of listens), irrelevant images, technology that fails."),
      ("What is the '6×6 rule' for slides?","Think: keep slides simple and readable","No more than 6 bullet points per slide, no more than 6 words per bullet. Forces the speaker to explain rather than read. Slides should SUPPORT the speaker, not replace them."),
      ("How does multimedia choice affect the audience's experience?","Think: format must match content","A video of a cell dividing is more powerful than a description. A chart is clearer than a paragraph of numbers. Wrong format choices confuse or bore audiences. Match the tool to the content."),
    ]),
  ],
]
print("G6 ELA complete")

P[6]["history"] = [
  # U1: Early Civilizations (5 topics)
  [
    s("Mesopotamia",[
      ("What does 'Mesopotamia' mean and where was it located?","Think: geographic context","'Land between the rivers' (Greek). Located between the Tigris and Euphrates rivers in modern-day Iraq. The fertile soil there allowed the first permanent farming settlements."),
      ("What was the significance of Hammurabi's Code?","Think: first written legal code","One of the earliest written law codes (~1754 BCE). 282 laws carved in stone, publicly displayed. Established the principle that laws apply to all — even if punishments were unequal by class. 'Eye for an eye' principle."),
      ("What were the major contributions of Mesopotamian civilizations?","Think: firsts in human history","Writing (cuneiform — first writing system), the wheel, the plow, organized city-states, ziggurats (temple towers), early astronomy and math (base-60 system — we still use it for hours/minutes)."),
      ("Why did Mesopotamia develop one of the earliest civilizations?","Think: geography and agriculture","The fertile floodplain between two rivers allowed reliable agriculture → food surplus → population growth → specialization of labor → cities. Geography drove civilization development."),
    ]),
    s("Ancient Egypt",[
      ("What was the significance of the Nile River to ancient Egyptian civilization?","Think: the gift of the Nile","Annual flooding deposited rich silt, making farmland incredibly fertile. The Nile provided water, food (fish), transportation, and trade routes. Without the Nile, Egypt would be desert."),
      ("What were the three kingdoms of ancient Egypt and what characterized each?","Think: Old, Middle, New Kingdoms","Old Kingdom: pyramid building, strong pharaonic power (Sphinx, pyramids at Giza). Middle Kingdom: expansion of trade, increased rights. New Kingdom: empire building, height of power (Ramesses II, Tutankhamun, Cleopatra at its very end)."),
      ("What was the role of the pharaoh in ancient Egypt?","Think: political + religious ruler","Pharaoh was both political ruler and living god — believed to be the son of Ra (sun god). This divine status meant absolute authority. After death, pharaohs were mummified to preserve their body for the afterlife."),
      ("What contributions did ancient Egypt make to world civilization?","Think: lasting innovations","Hieroglyphics (writing system), papyrus (early paper), calendar (365-day solar calendar), monumental architecture (pyramids), advances in medicine, and the concept of a centralized state."),
    ]),
    s("Ancient India and China",[
      ("What was the Indus Valley Civilization and what made it remarkable?","Think: India's first major urban civilization (~2500 BCE)","Located along the Indus River (modern Pakistan/India). Remarkable for: advanced city planning (grid streets, sewage systems), standardized weights/measures, no evidence of kings or armies — possibly a more equal society."),
      ("What were the major contributions of ancient China's early dynasties?","Think: innovations from China's early history","Writing (oracle bone script), silk production, bronze casting, the concept of the Mandate of Heaven (divine approval to rule), paper, and early civil service examinations for government positions."),
      ("What is the Mandate of Heaven and how did it legitimize Chinese rulers?","Think: divine right to rule — but conditional","The belief that the gods gave rulers (emperors) the right to rule, but ONLY if they governed justly. Natural disasters or rebellions were signs the Mandate had been lost, justifying the overthrow of a dynasty."),
      ("How were the Indus Valley and ancient Egyptian civilizations similar?","Think: compare two early civilizations","Both: located on river systems (Indus, Nile), had organized urban centers, developed writing, engaged in trade, and were agricultural. Both thrived when geography provided resources and trade routes."),
    ]),
    s("Ancient Greece",[
      ("What was the significance of the Greek city-state (polis)?","Think: the basic unit of Greek political life","Each polis was an independent city with its own government, laws, military, and culture. Athens and Sparta were the most powerful, with very different systems. The polis gave citizens direct involvement in governance."),
      ("What is direct democracy and how did Athens practice it?","Think: citizens vote directly on laws","Athens (~5th century BCE) allowed male citizens to vote directly on laws and policies in the Assembly. Not a true representative democracy — women, slaves, and foreigners were excluded. Still foundational to Western democratic thought."),
      ("What were the major contributions of ancient Greece?","Think: philosophy, democracy, science, arts","Philosophy (Socrates, Plato, Aristotle), democracy, theater (comedy and tragedy), the Olympic Games, advances in mathematics and geometry (Euclid, Pythagoras), medicine (Hippocrates), and epic poetry (Homer's Iliad and Odyssey)."),
      ("What was the difference between Athens and Sparta as city-states?","Think: intellect and democracy vs. military and discipline","Athens: prized education, arts, philosophy, democracy, and commerce. Sparta: militaristic society; boys trained as soldiers from age 7; focused on discipline, strength, and state loyalty. Two opposing models of Greek society."),
    ]),
    s("Ancient Rome",[
      ("What were the main characteristics of the Roman Republic?","Think: representative government with checks","(509–27 BCE) Two consuls (co-executives), Senate (aristocratic advisory body), and assemblies representing citizens. Concept of vetoes (one consul could block the other). Basis for many modern government systems."),
      ("How did the Roman Empire expand and how did it maintain control?","Think: military + administration + culture","Military conquest, roads (connected the empire), standardized laws (Roman law), Latin language, Roman citizenship as an incentive, and local governors. 'All roads lead to Rome' — ~50,000 miles of roads facilitated trade and control."),
      ("What were Rome's major contributions to Western civilization?","Think: lasting impacts on law, language, and architecture","Roman law (foundation of legal systems worldwide), Latin (root of Romance languages), architecture (arches, concrete, aqueducts), calendar (basis of our calendar), and the spread of Christianity through the empire."),
      ("Why did the Western Roman Empire fall in 476 CE?","Think: multiple causes over centuries","Political instability (constant civil wars), economic problems (overtaxation, trade decline), military pressure from Germanic tribes (Visigoths, Vandals), overextension, and reliance on mercenary armies. Rarely one cause — a combination of pressures."),
    ]),
  ],
  # U2: World Geography (5 topics)
  [
    s("Reading maps and globes",[
      ("What is the difference between a map and a globe? When is each more useful?","Think: flat vs. sphere; accuracy vs. portability","Globe: accurate 3D representation; best for true sizes and shapes. Map: flat, portable, can focus on one region; inevitably distorts size/shape/distance (map projections). Maps are more practical for most uses."),
      ("What are latitude and longitude? How do you use them to find a location?","Think: grid system on Earth's surface","Latitude: horizontal lines measuring degrees north/south of the equator (0° to 90°). Longitude: vertical lines measuring degrees east/west of prime meridian (0° to 180°). Together they create a coordinate system for any location."),
      ("What is a map projection? Why are all map projections imperfect?","Think: flattening a sphere always distorts something","A map projection transfers Earth's curved surface to a flat map. Every projection distorts at least one of: area, shape, distance, or direction. The Mercator projection (common in classrooms) exaggerates the size of high-latitude areas."),
      ("What are the five essential elements of a map?","Think: what makes a map useful?","Title (what the map shows), Legend/Key (explains symbols), Scale (shows distance), Compass Rose/Direction indicator, Source/Date (tells who made it and when). Without these, a map is incomplete."),
    ]),
    s("Physical geography",[
      ("What is the difference between a continent and a country?","Think: physical vs. political divisions","Continent: large landmass defined by geography (7 continents). Country: political unit with defined borders, government, and sovereignty. One continent can contain dozens of countries (e.g., Africa has 54 countries)."),
      ("Name and describe five types of landforms.","Think: major physical features of Earth's surface","Mountain: elevated land with steep sides. Valley: low area between mountains. Plateau: flat-topped elevated land. Plain: large flat area at low elevation. Peninsula: land nearly surrounded by water. Island: land fully surrounded by water."),
      ("What factors influence a region's climate?","Think: location + elevation + proximity to water","Latitude (distance from equator), elevation (higher = colder), proximity to large bodies of water (moderate climate), ocean currents, prevailing winds, and mountain ranges (rain shadow effect)."),
      ("What is the rain shadow effect?","Think: mountains blocking moisture","When moist air rises over a mountain, it cools and drops precipitation on the windward side. The leeward side (opposite) receives little rain — creating a 'rain shadow' desert. Example: the Sierra Nevada and Nevada's Great Basin."),
    ]),
    s("Human geography",[
      ("What is human geography? How does it differ from physical geography?","Think: people vs. physical features","Physical geography: studies Earth's natural features (mountains, rivers, climate). Human geography: studies how people interact with and organize space (cities, cultures, economies, political boundaries)."),
      ("What is population density? How is it calculated?","Think: people per unit of area","Population density = total population ÷ area (usually km² or mi²). High density: crowded cities (Tokyo, Mumbai). Low density: remote areas (Alaska, Sahara). Useful for comparing how crowded different regions are."),
      ("What is urbanization? What are its causes and effects?","Think: shift from rural to urban living","Urbanization: increasing percentage of people living in cities. Causes: economic opportunity, industrialization, agricultural mechanization. Effects: growth of cities, strain on infrastructure, loss of farmland, cultural change."),
      ("What is cultural diffusion? Give two examples.","Think: spread of cultural elements between groups","Cultural diffusion: the spread of cultural elements (ideas, foods, music, technology) from one group to another. Examples: pizza becoming popular worldwide from Italy; Buddhism spreading from India across Asia; the internet spreading globally."),
    ]),
    s("Regions of the world",[
      ("What is a region in geography? Name the two main types.","Think: areas defined by shared characteristics","A region is an area defined by common characteristics. Formal (physical or political): defined by measurable criteria (climate, language, borders). Functional: organized around a central node (metropolitan area). Vernacular: perceptual regions based on cultural identity (the 'South')."),
      ("Describe the major world regions and give one characteristic of each.","Think: seven to ten major world regions","North America (democratic, diverse), Latin America (Spanish/Portuguese heritage), Europe (welfare states, EU), Sub-Saharan Africa (youngest population, most biodiversity), Middle East/North Africa (arid, oil-rich), South Asia (most populous region), East Asia (manufacturing hub), Southeast Asia (diverse islands), Central Asia (landlocked), Oceania (island cultures)."),
      ("What are the major biomes of the world and where are they found?","Think: large ecological regions defined by climate and vegetation","Tropical rainforest (near equator), Desert (subtropical bands), Temperate forest (mid-latitudes), Grassland/Savanna (continental interiors), Tundra (Arctic), Taiga/Boreal forest (sub-Arctic), Tropical dry forest, Mediterranean shrubland."),
      ("What is the difference between a developing and a developed country?","Think: economic and social indicators","Developed: high GDP per capita, strong infrastructure, high life expectancy, low infant mortality (e.g., U.S., Germany). Developing: lower GDP, less infrastructure, lower life expectancy. Terms are contested — 'Global North/South' is also used."),
    ]),
    s("Geographic tools",[
      ("What is a GIS (Geographic Information System) and how is it used?","Think: layering geographic data on maps","GIS is digital technology that captures, stores, analyzes, and displays geographically referenced data. Used for: urban planning, disaster response, environmental monitoring, navigation (GPS). Layers of data (roads, population, elevation) can be combined."),
      ("What is the difference between a thematic and a reference map?","Think: general location vs. specific data","Reference map: shows general geographic features (roads, cities, borders). Thematic map: shows specific data about one theme (population density, rainfall, election results, language distribution). Each serves different purposes."),
      ("What does a topographic map show and how do you read contour lines?","Think: elevation shown on a 2D map","A topographic map shows elevation using contour lines — lines connecting points of equal elevation. Closely spaced lines = steep terrain. Widely spaced = gradual slope. Circular patterns with increasing numbers = hill or mountain."),
      ("What is remote sensing and what can it tell us?","Think: gathering data from a distance","Remote sensing: gathering data about Earth's surface from aircraft or satellites. Used to: monitor deforestation, track weather patterns, map land use, assess flood damage, study glacial retreat. Tools include radar, infrared, and multispectral imaging."),
    ]),
  ],
  # U3: Government & Civics Intro (5 topics)
  [
    s("Types of government",[
      ("What are the four main types of government? Give one modern example of each.","Think: who holds power?","Democracy: U.S., France (citizens). Oligarchy: China (Communist Party leadership). Autocracy/Dictatorship: North Korea (single leader). Theocracy: Iran (religious leaders hold power). Many governments blend features."),
      ("What is the difference between a direct and representative democracy?","Think: citizens vote directly vs. through elected representatives","Direct: citizens vote on laws themselves (ancient Athens; some Swiss referendums). Representative: citizens elect representatives who make laws on their behalf (U.S. Congress, UK Parliament). Most modern democracies are representative."),
      ("What is an authoritarian government?","Think: concentrated power, limited rights","Authoritarianism: government maintains strong control over citizens with limited political freedoms. May allow some economic freedom (unlike totalitarianism). Examples: military dictatorships, absolute monarchies. Citizens have little say in governance."),
      ("What is a constitutional monarchy and how does it differ from an absolute monarchy?","Think: limited vs. unlimited royal power","Constitutional monarchy: monarch's power is limited by a constitution; elected government holds real power (UK, Sweden). Absolute monarchy: monarch has unchecked authority over all government functions. Most modern monarchies are constitutional."),
    ]),
    s("Laws and rules",[
      ("What is the difference between a rule and a law?","Think: informal vs. formal; consequence differs","Rule: informal guideline for a specific context (school rules, sports rules); limited consequences. Law: official legal standard enforceable by government with formal consequences (fines, imprisonment). Laws apply to everyone in a jurisdiction."),
      ("Why does society need laws?","Think: order, safety, and rights protection","Laws maintain public order, protect individual rights, resolve disputes fairly, provide predictable standards of behavior, and define consequences for harmful actions. Without laws, society would rely on power and force to settle conflicts."),
      ("What is the difference between criminal and civil law?","Think: crimes vs. disputes between individuals","Criminal law: offenses against society/the state (murder, theft) — prosecution by government; can result in imprisonment. Civil law: disputes between individuals or organizations (contracts, property) — no imprisonment; usually results in financial settlement."),
      ("What is due process of law and why is it important?","Think: fair legal procedures protect everyone","Due process ensures fair treatment through the legal system: right to know charges, right to a hearing, right to an attorney, presumed innocent until proven guilty. Protects against arbitrary government action."),
    ]),
    s("Rights and responsibilities",[
      ("What are rights? What are responsibilities? Give two examples of each.","Think: what you're entitled to vs. what you're obligated to do","Rights: freedom of speech, fair trial. Responsibilities: obeying laws, paying taxes, jury duty. Rights and responsibilities exist together — exercising rights requires accepting responsibilities."),
      ("What is the Bill of Rights? Name three rights it protects.","Think: first 10 amendments to the U.S. Constitution","The Bill of Rights (1791) protects individual rights from government overreach. Examples: 1st Amendment (speech, religion, press), 4th Amendment (unreasonable searches), 6th Amendment (speedy trial, legal counsel)."),
      ("What is the difference between a right and a privilege?","Think: inherent vs. granted","Right: a freedom or entitlement that belongs to all people (free speech, fair trial). Privilege: a special advantage granted under certain conditions that can be taken away (driver's license, voting — requires registration and meeting age requirements)."),
      ("What is civic responsibility? Why is voting important?","Think: obligations of citizenship in a democracy","Civic responsibilities include voting, jury duty, paying taxes, and staying informed. Voting is essential because democracy works only when citizens participate — elected officials represent voters, and low turnout shifts power to smaller, more active groups."),
    ]),
    s("Democratic principles",[
      ("What are the core principles of democracy?","Think: what makes a government democratic?","Popular sovereignty (power from the people), majority rule with minority rights, rule of law, separation of powers, free and fair elections, protection of individual rights, free press. All are necessary for functioning democracy."),
      ("What is the rule of law? Why is it essential?","Think: no one is above the law — including government","Rule of law: all people — including government officials — are subject to and accountable under the law, fairly applied. Prevents tyranny, ensures equal justice, and creates predictability. Without it, whoever has power makes arbitrary decisions."),
      ("What is separation of powers? Why was it built into U.S. government?","Think: preventing concentration of power","Divides government into three branches (legislative, executive, judicial) each with distinct powers. Prevents any one person or group from having absolute power — a direct response to colonial experience under an absolute monarch."),
      ("What are checks and balances? Give one example for each branch.","Think: each branch limits the others","Congress checks President: can override vetoes. President checks Congress: vetoes legislation. Supreme Court checks both: can declare laws unconstitutional. Each branch has tools to prevent the others from overreaching."),
    ]),
    s("Local government",[
      ("What are the three levels of government in the U.S.? Name a power held by each.","Think: federal, state, local","Federal: declares war, regulates interstate commerce. State: manages education, license drivers. Local: manages zoning, fire departments, local roads. Power is shared across all three levels (federalism)."),
      ("What does a local government actually do? Name four services.","Think: what services do you interact with daily?","Manages local roads, public schools, fire/police departments, parks, water/sewer systems, zoning, waste collection. Most day-to-day services people use are managed by local government."),
      ("What is a mayor and what does a city council do?","Think: executive vs. legislative at the local level","Mayor: executive leader of a city; implements local laws, manages city departments, represents the city. City council: local legislative body; creates local ordinances (laws), approves the budget, sets local policy."),
      ("How can a citizen participate in local government?","Think: democracy is most direct at the local level","Attend city council meetings (public comment), vote in local elections (where individual votes matter most), contact local representatives, serve on local boards/commissions, organize community meetings, or run for local office."),
    ]),
  ],
  # U-CS: digital literacy (2 topics)
]

P[6]["cs"] = [
  [
    s("Internet safety",[
      ("What are three rules for staying safe online?","Think: personal information, strangers, passwords","(1) Never share personal info (address, phone, school) with strangers online. (2) Use strong, unique passwords for each account. (3) Tell a trusted adult if anything online makes you uncomfortable. (4) Think before you post — the internet is permanent."),
      ("What is a phishing scam? How do you identify one?","Think: fake messages tricking you into giving information","Phishing: fake emails/messages pretending to be from a trusted source (your bank, Google) to steal passwords or personal information. Signs: urgent language, misspelled URLs, asks for passwords, generic greeting ('Dear User')."),
      ("What is cyberbullying and what should you do if you experience it?","Think: harassment using technology","Cyberbullying: using technology to harass, intimidate, or harm others (hurtful messages, sharing embarrassing photos, spreading rumors online). If experienced: don't respond, block the bully, save evidence, and tell a trusted adult. It is serious and often illegal."),
      ("Why is your digital footprint important?","Think: permanent record of your online activity","Your digital footprint is the trail of data you leave online (posts, comments, searches, photos). It can be seen by colleges, employers, and others. Once posted, content can be very difficult to remove — always consider the long-term impact."),
    ]),
    s("Evaluating online sources",[
      ("What makes an online source reliable? Name four criteria.","Think: CRAAP — Currency, Relevance, Authority, Accuracy, Purpose","Currency: recently updated. Authority: written by an expert or credible organization. Accuracy: facts verifiable from other sources. Purpose: informative (not commercial or misleading). .gov and .edu are generally more reliable."),
      ("Why is Wikipedia not a primary source, and how should you use it?","Think: crowd-sourced, can be edited","Wikipedia can be edited by anyone and may contain errors. Use it to get a general overview and find better sources (use the References section). Never cite Wikipedia as a primary source in academic work."),
      ("What is confirmation bias and how does it affect how we evaluate sources?","Think: tendency to seek information that confirms what we already believe","Confirmation bias: we tend to accept information that confirms our existing beliefs and reject information that challenges them. Overcome it by actively seeking out credible sources that represent multiple perspectives."),
      ("How do you tell the difference between a news article, an opinion piece, and an advertisement?","Think: look for labels, tone, and purpose","News: objective reporting of facts, sourced quotes. Opinion: clearly labeled, uses 'I think/believe,' subjective language. Advertisement: promotes a product/service, often labeled 'Sponsored' or 'Ad.' All three may appear online — look carefully."),
    ]),
    s("Digital citizenship",[
      ("What is digital citizenship?","Think: responsible, ethical behavior online","Responsible and ethical participation in the digital world: respecting others online, protecting your privacy, thinking critically about information, using technology responsibly, and understanding the impact of your digital actions."),
      ("What is the difference between copyright and fair use?","Think: protection vs. permitted use","Copyright: legal protection for creators' original work — others cannot use it without permission. Fair use: limited exceptions allowing copyrighted material to be used for education, commentary, or criticism without permission. When in doubt, cite the source."),
      ("How does online communication differ from face-to-face communication?","Think: missing cues, permanence, audience scale","Online: lacks tone of voice and body language (meaning gets lost), messages are permanent and can spread widely, audience can be far larger than intended. This makes misunderstandings more common and the impact of hurtful messages greater."),
      ("What does it mean to have a positive online presence?","Think: what you want others to see when they search your name","Creating content that reflects positively on you: thoughtful comments, contributions to knowledge, professional or creative work. Avoid: offensive content, aggressive arguments, inappropriate images. Future employers and colleges may look."),
    ]),
    s("Privacy and security",[
      ("What is personal information? What should you never share online?","Think: information that identifies you","Personal information: full name, address, phone number, school name, birthday, passwords, social security number, photos showing your location. Never share these with strangers or on public websites."),
      ("What is a strong password? Create one example.","Think: length, complexity, uniqueness","Long (12+ characters), mixes uppercase, lowercase, numbers, and symbols, not based on personal info, unique for each account. Example: 'BlueSky$7Rainy!23' — easy to remember but hard to guess. Use a password manager for multiple accounts."),
      ("What is two-factor authentication (2FA) and why should you use it?","Think: second layer of security","2FA requires two forms of identification to log in: your password plus a code sent to your phone or generated by an app. Even if someone steals your password, they can't access your account without the second factor."),
      ("What are the privacy risks of social media?","Think: who sees what you post?","Privacy risks: sharing your location (check-ins, geotagged photos), oversharing personal info, apps accessing your data (contacts, camera, location), data collection for advertising, and content being visible to more people than intended. Review privacy settings regularly."),
    ]),
    s("Screen time awareness",[
      ("What are some negative effects of excessive screen time?","Think: physical, mental, and social impacts","Eye strain, disrupted sleep (blue light affects melatonin), reduced physical activity, decreased face-to-face social skills, increased anxiety/depression linked to social media comparison, reduced attention span."),
      ("What is a healthy approach to managing screen time?","Think: balance, not elimination","Set daily limits, take regular breaks (20-20-20 rule: every 20 minutes look 20 feet away for 20 seconds), no screens 1 hour before bed, prioritize face-to-face time and physical activity, choose intentional use over mindless scrolling."),
      ("What is the difference between passive and active screen time?","Think: consumer vs. creator; mindless vs. purposeful","Passive: watching videos, scrolling social media (consuming). Active: coding, creating videos, learning a skill, video chatting (creating or connecting). Active screen time generally has more educational and social value than passive consumption."),
      ("How does social media affect mental health in young people?","Think: comparison culture, validation-seeking, anxiety","Research links heavy social media use to increased anxiety and depression, especially when use involves social comparison ('everyone else's life is better'). However, intentional use for connecting with friends shows more neutral or positive effects. Quality of use matters more than quantity."),
    ]),
  ],
  [
    s("Algorithms and flowcharts",[
      ("What is an algorithm?","Think: step-by-step instructions for solving a problem","A precise, ordered set of instructions for solving a problem or completing a task. Algorithms must be: clear (unambiguous), finite (have an end), and correct (produce the right output for any valid input)."),
      ("Create a simple algorithm for making a peanut butter sandwich. Why must instructions be precise?","Think: what happens if a robot follows your instructions literally?","1. Get bread, peanut butter, knife. 2. Open bread bag, take out 2 slices. 3. Open peanut butter jar. 4. Use knife to spread peanut butter on one face of one slice. 5. Press other slice on top. Precision matters: 'spread peanut butter on the bread' without specifics would confuse a robot."),
      ("What is a flowchart and what symbols does it use?","Think: visual representation of an algorithm","A flowchart is a diagram representing an algorithm visually. Symbols: oval (start/end), rectangle (process/action), diamond (decision — yes/no), arrow (flow direction). Flowcharts make complex processes easier to understand."),
      ("What is the difference between an algorithm and a program?","Think: instructions vs. instructions in a specific language","Algorithm: a general, language-independent set of steps. Program (code): an algorithm written in a specific programming language (Python, Java) that a computer can execute. The algorithm comes before the program."),
    ]),
    s("Sequence, selection, iteration",[
      ("What are the three fundamental programming structures?","Think: the building blocks of all programs","Sequence: instructions executed one after another in order. Selection (conditional): if/else — different paths based on a condition. Iteration (loop): repeating a block of code while or until a condition is met. All programs use these three structures."),
      ("Give an example of selection (if/else) in everyday life.","Think: a decision with two paths","IF it is raining: bring an umbrella. ELSE: leave it at home. Selection allows a program to make decisions based on conditions — creating different outcomes for different inputs."),
      ("What is an iteration (loop)? Give an everyday example.","Think: repeating something multiple times","Iteration: repeating an action. Example: brushing teeth = move brush back and forth (repeat 120 times, or repeat FOR 2 minutes). Loops avoid writing the same instruction many times and allow programs to process large amounts of data efficiently."),
      ("What is the order of operations in a sequence? Why does it matter?","Think: order changes outcome","Instructions execute in exactly the order written. 'Put on shoes, then put on socks' produces a different result than the correct order. Computers follow sequence exactly — wrong order = wrong result (or an error)."),
    ]),
    s("Block-based coding (Scratch)",[
      ("What is Scratch and why is it used to teach coding?","Think: visual coding for beginners","Scratch is a free, block-based visual programming language where users drag and snap code blocks together. Used to teach coding because it eliminates syntax errors, allowing learners to focus on logic and problem-solving rather than memorizing exact code syntax."),
      ("What is a 'sprite' in Scratch and how does it differ from the 'stage'?","Think: characters vs. background","Sprite: a character or object in the project that can move, speak, and respond to events. Stage: the background — it cannot move but can have scripts and costumes. Multiple sprites can interact on the same stage."),
      ("What is an event in Scratch? Give two examples.","Think: what triggers a script to run?","An event is a trigger that starts running a script. Examples: 'When green flag clicked' (starts the program), 'When this sprite is clicked' (click triggers action), 'When I receive [message]' (communication between sprites)."),
      ("What is the 'forever' block in Scratch used for?","Think: continuous iteration","The 'forever' block creates an infinite loop — the code inside runs continuously until the program is stopped. Used for: continuous movement, background music, constantly checking conditions (game collision detection)."),
    ]),
    s("Debugging",[
      ("What is debugging in programming?","Think: finding and fixing errors in code","Debugging is the process of identifying and removing errors (bugs) from code. Essential skill — even professional programmers spend significant time debugging. The term comes from Grace Hopper finding an actual moth in a computer relay (1947)."),
      ("What are the three types of programming errors?","Think: syntax, logic, runtime","Syntax: code doesn't follow language rules (missing comma, wrong spelling). Runtime: code runs but crashes (dividing by zero). Logic: code runs without crashing but produces wrong output. Logic errors are often the hardest to find."),
      ("What is a debugging strategy when your code doesn't work?","Think: systematic problem-solving","(1) Read error messages carefully. (2) Check your code line by line. (3) Add print statements to see what values variables hold. (4) Comment out sections to narrow down where the bug is. (5) Explain your code to someone else (rubber duck debugging)."),
      ("Why is debugging an important skill beyond programming?","Think: problem-solving applies everywhere","Debugging develops systematic problem-solving, patience, attention to detail, and logical thinking — skills valuable in science, mathematics, writing, and everyday life. Learning to persist through frustration is itself a valuable outcome."),
    ]),
    s("Creating simple projects",[
      ("What makes a good coding project for a beginner?","Think: scope, clear goal, achievable","A good beginner project: has a clear, specific goal, is small enough to complete in reasonable time, uses concepts already learned (sequence, selection, iteration), and has personal interest. Examples: simple game, animated story, quiz, art generator."),
      ("What is a sprite's costume in Scratch and how is it used for animation?","Think: different appearances of the same sprite","A costume is an alternate image/appearance for a sprite. Switching between costumes rapidly creates the illusion of animation (like a flipbook). Example: a walking character alternates between left-foot-forward and right-foot-forward costumes."),
      ("What is the purpose of comments in code?","Think: explanation within the code itself","Comments are notes added to code (ignored by the computer) that explain what sections do and why. They make code readable to others (and to yourself later). Essential for collaboration and debugging. Good code is well-commented."),
      ("What is iteration in project development (not the loop)?","Think: improving a project through multiple versions","In project development, iteration means: build a basic version, test it, get feedback, improve, test again, and repeat. Professional developers use this cycle constantly. Your first version doesn't need to be perfect — improvement comes through repeated cycles."),
    ]),
  ],
]
print("G6 CS complete")

P[6]["health"] = [
  [
    s("Hygiene and self-care",[
      ("What are the daily hygiene habits that protect health?","Think: basic self-care routine","Daily: brushing teeth (2x, 2 min each), washing hands frequently (before eating, after bathroom), bathing/showering, clean clothes, deodorant. These habits prevent the spread of bacteria, viruses, and body odor."),
      ("Why is handwashing the single most effective way to prevent illness?","Think: how diseases spread via hands","Hands touch hundreds of surfaces and then touch our face, mouth, and food. Handwashing with soap for 20 seconds removes 99%+ of harmful bacteria and viruses. More effective than hand sanitizer for many germs."),
      ("What is oral health and why does it affect overall health?","Think: mouth health connects to whole body health","Oral health = healthy teeth, gums, and mouth. Poor oral hygiene causes cavities, gum disease, and tooth loss. Research links gum disease to heart disease, diabetes, and respiratory illness. Good oral health: brush 2x/day, floss daily, regular dental checkups."),
      ("What is acne and what are healthy ways to manage it?","Think: common during puberty; manageable with good habits","Acne: skin condition caused by clogged pores (oil, dead skin cells, bacteria). Common during puberty when hormones increase oil production. Management: wash face gently 2x/day with mild soap, don't pick or squeeze, see a doctor for persistent acne, avoid touching your face."),
    ]),
    s("Sleep and nutrition",[
      ("How much sleep do 6th graders need and why is it important?","Think: recommended hours and functions of sleep","Ages 11–13 need 9–11 hours of sleep per night. During sleep: brain consolidates memories, body repairs tissue, hormones regulate growth, and immune system strengthens. Sleep deprivation impairs concentration, mood, and athletic performance."),
      ("What are the six major nutrient groups and what does each do?","Think: carbs, proteins, fats, vitamins, minerals, water","Carbohydrates: main energy source. Proteins: build and repair tissue. Fats: long-term energy, brain function. Vitamins: regulate body processes. Minerals: bone strength, nerve function (calcium, iron). Water: every cell function. All six are essential."),
      ("What is MyPlate and how does it guide healthy eating?","Think: USDA's visual guide to portion balance","MyPlate shows a divided plate: half fruits and vegetables, quarter grains (half whole grains), quarter protein (lean), plus dairy on the side. It emphasizes variety, balance, and proper proportions rather than strict calorie counting."),
      ("Why is sugar-sweetened beverage consumption a health concern?","Think: empty calories and health effects","Sodas, energy drinks, and juices often contain large amounts of added sugar with little nutritional value. High sugar intake is linked to obesity, type 2 diabetes, tooth decay, and heart disease. Water and low-fat milk are better choices."),
    ]),
    s("Growth and development",[
      ("What is adolescence and approximately when does it begin?","Think: transition from childhood to adulthood","Adolescence: the developmental stage between childhood and adulthood, typically beginning around ages 10–14 for girls and 12–16 for boys (varies widely). Characterized by puberty (physical changes) and significant cognitive and emotional development."),
      ("What are growth spurts and why do different students grow at different rates?","Think: rapid growth periods driven by hormones","Growth spurts: periods of rapid height and weight gain triggered by hormones during puberty. Genetics primarily determines when and how much a person grows. Different people experience puberty at different ages — all variations within the normal range."),
      ("What is the difference between physical, emotional, and social development during adolescence?","Think: three interconnected dimensions of growth","Physical: puberty changes, growth spurts. Emotional: greater self-awareness, mood changes, forming identity. Social: importance of peer relationships grows, developing independence from parents. These dimensions interact and influence each other."),
      ("Why do teens often experience mood swings during adolescence?","Think: hormones, brain development, and social pressures","Hormonal changes during puberty affect brain chemistry. The prefrontal cortex (decision-making, emotion regulation) is still developing until age 25. Increased social awareness and peer pressure add emotional complexity. Mood swings are normal but should not be extreme or persistent."),
    ]),
    s("Puberty education",[
      ("What is puberty and what triggers it?","Think: physical changes marking sexual maturation","Puberty: the process of physical changes making a child's body capable of sexual reproduction. Triggered by hormonal changes (estrogen, testosterone, growth hormone). Normal range: ages 8–16 for girls; 9–17 for boys. Wide variation is normal."),
      ("What are common physical changes during puberty for both males and females?","Think: shared and distinct changes","Both: growth spurt, body hair, skin changes (acne), body odor, increased sweating. Females: breast development, menstruation, hip widening. Males: voice deepening, facial hair, muscle development, external genital growth."),
      ("What is menstruation and what should someone know about it?","Think: monthly cycle in females","Menstruation: monthly shedding of the uterine lining when pregnancy does not occur. Typically lasts 3–7 days. Cycles average 21–35 days. May be irregular at first — this is normal. Products used: pads, tampons, menstrual cups. Cramping is common; severe pain warrants a doctor visit."),
      ("What is a healthy attitude toward the changes that happen during puberty?","Think: normal, individual, and manageable","Puberty is a normal, universal process that everyone experiences at their own pace. It can feel awkward or overwhelming but is not harmful. Talk to a trusted adult with questions. Comparing yourself to others is unhelpful — everyone develops differently and on their own timeline."),
    ]),
    s("Stress management",[
      ("What is stress? What are common sources of stress for middle schoolers?","Think: response to challenges or demands","Stress: mental/emotional strain from difficult or demanding situations. Common sources: academic pressure (tests, grades), social conflicts (friendships, peer pressure), family issues, extracurricular demands, social media, and uncertainty about the future."),
      ("What is the difference between healthy and unhealthy stress?","Think: eustress vs. distress","Healthy stress (eustress): motivates performance — mild anxiety before a test or game can enhance focus. Unhealthy stress (distress): chronic, overwhelming stress that impairs function — sleep problems, physical symptoms, persistent anxiety. The distinction matters for how we respond."),
      ("Name five healthy stress management strategies.","Think: evidence-based coping methods","(1) Physical exercise (releases endorphins). (2) Deep breathing or meditation. (3) Talking to a trusted adult or friend. (4) Getting enough sleep. (5) Time management and planning. (6) Creative outlets (art, music, journaling). Avoid: suppressing feelings, unhealthy escapes."),
      ("When is stress a signal that you need to seek help?","Think: when normal coping isn't enough","Seek help when: stress persists for more than two weeks, affects sleep or appetite significantly, causes thoughts of self-harm, prevents school attendance or daily function, or feels impossible to manage alone. Talking to a counselor or doctor is a sign of strength."),
    ]),
  ],
  [
    s("Components of fitness",[
      ("What are the five components of physical fitness?","Think: CSMFE","Cardiovascular endurance, Muscular strength, Muscular endurance, Flexibility, and Body composition. All five together constitute overall physical fitness — training for only one creates an imbalanced fitness level."),
      ("What is the difference between muscular strength and muscular endurance?","Think: how hard vs. how long","Muscular strength: maximum force a muscle can exert in a single effort (one-rep max bench press). Muscular endurance: ability of a muscle to perform repeated contractions for an extended period (push-ups, plank hold). Both are important for daily activities."),
      ("What is cardiovascular endurance and why is it important?","Think: heart and lungs' ability to sustain activity","Ability of the heart, lungs, and blood vessels to deliver oxygen during sustained exercise. Important because: reduces risk of heart disease, improves stamina, boosts mood, improves sleep, and is the strongest predictor of long-term health."),
      ("What is body composition and why is it a better health indicator than weight alone?","Think: fat vs. lean mass — not just total weight","Body composition: the ratio of fat mass to lean mass (muscle, bone, organs). Two people can weigh the same but have very different health — one may have high lean mass (healthier) while the other has high fat mass. BMI has similar limitations."),
    ]),
    s("Aerobic exercise",[
      ("What is aerobic exercise? Give four examples.","Think: sustained activity that uses oxygen for energy","Aerobic = 'with oxygen.' Activities sustained for long periods using the aerobic energy system: running, swimming, cycling, brisk walking, dancing, rowing. Heart rate is elevated but sustainable for 20+ minutes."),
      ("What does the American Heart Association recommend for physical activity for middle schoolers?","Think: specific, evidence-based recommendations","60 minutes of moderate-to-vigorous physical activity DAILY, including aerobic exercise 5+ days/week, muscle-strengthening 3+ days/week, and bone-strengthening 3+ days/week. Most 6th graders fall short of this guideline."),
      ("What is the target heart rate zone and how do you calculate it?","Think: optimal training range","Target heart rate zone = 50–85% of maximum heart rate. Max HR estimate = 220 − your age. For a 12-year-old: max HR = 208; target zone = 104–177 bpm. Exercising in this zone maximizes cardiovascular benefits."),
      ("What are the short-term and long-term benefits of regular aerobic exercise?","Think: immediate vs. cumulative benefits","Short-term: better mood (endorphins), increased energy, better concentration, reduced stress. Long-term: stronger heart, lower blood pressure, healthy weight, reduced risk of type 2 diabetes and heart disease, improved bone density, longer life expectancy."),
    ]),
    s("Strength and flexibility",[
      ("What is flexibility and why is it important?","Think: range of motion at a joint","Flexibility: the ability to move joints through their full range of motion. Important for: injury prevention, posture, balance, and performance. Decreases with age without stretching. Best improved through regular static and dynamic stretching."),
      ("What is the difference between static and dynamic stretching?","Think: hold still vs. move through range","Static: hold a stretch position for 15–60 seconds (e.g., touching toes and holding). Best after exercise when muscles are warm. Dynamic: controlled movements through full range of motion (leg swings, arm circles). Best before exercise as a warm-up."),
      ("What are the principles of safe strength training for 6th graders?","Think: safety, form, and appropriate intensity","Use proper form before adding weight. Start with body weight (push-ups, squats, lunges). Avoid maximal lifting with heavy weights until fully developed. Warm up before, cool down after. Rest 48 hours between strength workouts for the same muscle group."),
      ("What is the FITT principle for designing a fitness program?","Think: Frequency, Intensity, Time, Type","Frequency: how often you exercise. Intensity: how hard (heart rate, weight). Time: duration of each session. Type: what kind of exercise. FITT provides a framework for creating balanced, progressive fitness programs for any goal."),
    ]),
    s("Team sports rules",[
      ("Why are rules important in sports?","Think: fairness, safety, and enjoyment","Rules ensure: fair competition (everyone follows the same standards), player safety, consistent expectations, and enjoyment for all participants. Without rules, competition would devolve into chaos or be decided by size and strength alone."),
      ("What is sportsmanship and why does it matter?","Think: how you play, win, and lose","Sportsmanship: treating opponents, teammates, officials, and the game itself with respect. Includes: accepting losses gracefully, not gloating over wins, following rules even when no one is watching, encouraging teammates. Poor sportsmanship undermines the purpose of sport."),
      ("What is the role of a referee or official in sports?","Think: impartial enforcer of the rules","Officials interpret and enforce rules, make binding decisions on rule violations, ensure player safety, and maintain fair play. Players are expected to accept officials' decisions even when they disagree, though professional leagues have replay review systems."),
      ("How do team sports teach life skills beyond athletic ability?","Think: transferable skills from sport to life","Teamwork (collaborating toward a common goal), communication, leadership, dealing with failure and success, time management (balancing practice with school), persistence through difficulty, and following rules. These skills transfer directly to academics and careers."),
    ]),
    s("Setting fitness goals",[
      ("What is a SMART fitness goal? Write one example.","Think: Specific, Measurable, Achievable, Relevant, Time-bound","SMART: 'I will run 1 mile in under 10 minutes by the end of the 8-week fitness unit by running 3 times per week.' Vague goal ('I want to get in shape') is unmeasurable — SMART goals create clear targets and paths."),
      ("What is the difference between an outcome goal and a process goal?","Think: what you want to achieve vs. how you'll get there","Outcome goal: the end result ('Win the race'). Process goal: behaviors that lead to the outcome ('Run 30 minutes, 4 days/week'). Process goals are more controllable and motivating day-to-day than outcome goals, which depend on factors outside your control."),
      ("Why is tracking your fitness progress important?","Think: measurement enables improvement","Tracking shows whether you are improving, helps you adjust your plan if progress stalls, provides motivation when you see gains, and helps identify what is and isn't working. Methods: fitness log, fitness apps, benchmark tests (1-mile run, push-up test)."),
      ("What should you do if you're not reaching your fitness goal?","Think: systematic troubleshooting","Reassess the goal (is it realistic?), analyze what's working or not, adjust the plan (frequency, intensity, type), seek guidance (coach, teacher), or break the goal into smaller steps. Failing to reach a goal is information, not failure."),
    ]),
  ],
]
print("G6 health complete")

# ─── GRADE 7 ───
P[7] = {"math":[], "science":[], "ela":[], "history":[], "cs":[], "health":[]}

P[7]["math"] = [
  # U1: Rational Numbers
  [
    s("Adding and subtracting integers",[
      ("Calculate: -14 + 9","Think: same sign or different signs?","-5. Different signs: subtract (14-9=5), take sign of larger absolute value (negative)."),
      ("Calculate: -7 - (-3)","Think: subtracting a negative = adding","−7 − (−3) = −7 + 3 = −4."),
      ("The temperature was -6°F and dropped 8 more degrees. What is the new temperature?","Think: dropping = subtracting","-6 − 8 = -14°F."),
      ("Is -(-5) positive or negative?","Think: double negative","Positive. Negating a negative gives positive: -(-5) = +5."),
    ]),
    s("Multiplying and dividing integers",[
      ("Calculate: (-6) × (-4)","Think: negative × negative = positive","24. Same signs → positive product."),
      ("Calculate: -35 ÷ 7","Think: different signs → negative result","-5. Negative ÷ positive = negative."),
      ("What rule determines the sign of a product/quotient?","Think: same signs vs. different signs","Same signs (both + or both −) → positive result. Different signs → negative result."),
      ("If a submarine descends 15 feet per minute, what is its total change after 6 minutes?","Think: rate × time, both negative","(-15) × 6 = -90 feet (90 feet deeper)."),
    ]),
    s("Fractions and decimals",[
      ("Convert 5/8 to a decimal.","Think: divide numerator by denominator","5 ÷ 8 = 0.625."),
      ("Which is larger: 3/7 or 5/11?","Think: convert to decimals or common denominator","3/7 ≈ 0.4286; 5/11 ≈ 0.4545. So 5/11 is larger."),
      ("Calculate: 2/3 + 3/4","Think: LCD = 12","8/12 + 9/12 = 17/12 = 1 5/12."),
      ("Calculate: 2.4 × 0.05","Think: multiply, then count decimal places","0.120. (2.4 × 5 = 12; total 3 decimal places → 0.120)."),
    ]),
    s("Rational number operations",[
      ("What is a rational number?","Think: p/q where p and q are integers, q≠0","Any number expressible as a fraction of two integers (q≠0). Examples: 3/4, -5, 0.75, -2.5."),
      ("Is 0 rational? Is √2 rational?","Think: can they be expressed as fractions?","0 is rational (0/1). √2 is irrational — its decimal is non-terminating and non-repeating."),
      ("Evaluate: (-3/4) ÷ (3/2)","Think: dividing = multiplying by reciprocal","(-3/4) × (2/3) = -6/12 = -1/2."),
      ("Order from least to greatest: -1.5, 3/4, -2/3, 0","Think: convert to decimals then order","-1.5 = -1.5; -2/3 ≈ -0.667; 0 = 0; 3/4 = 0.75. Order: -1.5, -2/3, 0, 3/4."),
    ]),
    s("Absolute value and number line",[
      ("What does |−8| equal?","Think: absolute value = distance from zero","8. Absolute value is always non-negative."),
      ("What is the distance between -5 and 3 on a number line?","Think: distance = |a − b|","|−5 − 3| = |−8| = 8."),
      ("Solve: |x| = 6","Think: what numbers are 6 from zero?","x = 6 or x = -6."),
      ("Which is colder, -15°C or -9°C?","Think: on the number line, which is further left?","-15°C is colder — it is a smaller (more negative) value."),
    ]),
  ],
  # U2: Proportional Relationships
  [
    s("Ratios and rates",[
      ("A recipe uses 2 cups of flour for 3 cups of oats. What is the ratio of flour to oats?","Think: part to part","2:3 or 2/3."),
      ("A car travels 240 miles in 4 hours. What is the unit rate?","Think: divide to get per-unit","60 miles per hour."),
      ("What is the difference between a ratio and a rate?","Think: same units vs. different units","Ratio: compares same-unit quantities. Rate: compares different-unit quantities (miles per hour, price per pound)."),
      ("If 5 pounds of apples costs $8.75, what is the cost per pound?","Think: divide total by units","$8.75 / 5 = $1.75 per pound."),
    ]),
    s("Proportions",[
      ("Solve: 3/5 = x/20","Think: cross-multiply","3 × 20 = 5x → 60 = 5x → x = 12."),
      ("A map uses a scale of 1 inch = 50 miles. Two cities are 3.5 inches apart. What is the actual distance?","Think: set up a proportion","1/50 = 3.5/x → x = 175 miles."),
      ("Are 4/6 and 10/15 proportional?","Think: cross-multiply or simplify both","4 × 15 = 60; 6 × 10 = 60. Yes, they are proportional. Both simplify to 2/3."),
      ("What does it mean for two ratios to be proportional?","Think: equivalent fractions","Two ratios are proportional if they simplify to the same fraction or if their cross products are equal."),
    ]),
    s("Unit rates and percentages",[
      ("What is 35% of 120?","Think: percent × whole / 100","35/100 × 120 = 42."),
      ("A jacket costs $80 and is 25% off. What is the sale price?","Think: discount = 25% of $80","Discount = 0.25 × 80 = $20. Sale price = $80 - $20 = $60."),
      ("A store raises a price from $40 to $52. What is the percent increase?","Think: change/original × 100","(52 - 40)/40 × 100 = 12/40 × 100 = 30% increase."),
      ("What is the unit rate: $12.60 for 3 pounds?","Think: divide total by quantity","$4.20 per pound."),
    ]),
    s("Proportional relationships in graphs",[
      ("What does a proportional relationship look like on a graph?","Think: straight line through the origin","A straight line that passes through the origin (0,0)."),
      ("How do you find the constant of proportionality (k) from a table?","Think: y/x ratio","k = y/x. Divide any y-value by its corresponding x-value. If this is constant for all pairs, the relationship is proportional."),
      ("Is the relationship proportional? x: 2, 4, 6; y: 5, 10, 15","Think: check y/x ratio","y/x: 5/2=2.5, 10/4=2.5, 15/6=2.5. Constant ratio yes, proportional. k = 2.5."),
      ("A graph passes through (3,12). What is the equation of this proportional relationship?","Think: y = kx where k = y/x","k = 12/3 = 4. Equation: y = 4x."),
    ]),
    s("Scale drawings",[
      ("A blueprint uses a scale of 1 cm = 4 m. A room is 5 cm on the blueprint. How wide is the real room?","Think: scale × measurement","5 × 4 = 20 meters."),
      ("A model car is 1/24 the size of the real car. If the real car is 4.8 m long, how long is the model?","Think: multiply by scale factor","4.8 / 24 = 0.2 m = 20 cm."),
      ("What is the scale factor of a drawing where 3 inches represents 18 feet?","Think: simplify ratio","3 in : 18 ft = 1 in : 6 ft. Scale factor = 1:6."),
      ("Two cities are 300 km apart. On a map with scale 1 cm = 50 km, how far apart are they on the map?","Think: divide actual by km per cm","300 / 50 = 6 cm."),
    ]),
  ],
  # U3: Expressions, Equations, Inequalities
  [
    s("Writing and evaluating expressions",[
      ("Evaluate 3x^2 - 2x + 1 for x = -2.","Think: substitute and follow order of operations","3(-2)^2 - 2(-2) + 1 = 3(4) + 4 + 1 = 12 + 4 + 1 = 17."),
      ("Write an expression for: five more than twice a number n","Think: translate words to symbols","2n + 5."),
      ("What is the difference between an expression and an equation?","Think: expression vs. equation","Expression: has no equal sign (3x + 5). Equation: has an equal sign and can be solved (3x + 5 = 17)."),
      ("Simplify: 4(2x - 3) + 5x","Think: distribute, then combine like terms","8x - 12 + 5x = 13x - 12."),
    ]),
    s("Solving one-step equations",[
      ("Solve: x + 15 = -3","Think: subtract 15 from both sides","x = -18."),
      ("Solve: -4x = 28","Think: divide both sides by -4","x = -7."),
      ("What is the goal when solving an equation?","Think: isolate the variable","Isolate the variable — get it alone on one side. Use inverse operations applied equally to both sides."),
      ("Check if x = 5 is a solution to 3x - 7 = 8.","Think: substitute and verify","3(5) - 7 = 15 - 7 = 8. Yes, x = 5 is a solution."),
    ]),
    s("Solving two-step equations",[
      ("Solve: 2x + 7 = -3","Think: undo addition first, then multiplication","2x = -10 → x = -5."),
      ("Solve: x/3 - 4 = 2","Think: undo subtraction first, then division","x/3 = 6 → x = 18."),
      ("A number tripled and decreased by 5 equals 13. Write and solve.","Think: 3n - 5 = 13","3n = 18 → n = 6."),
      ("Solve: -3(x + 2) = 9","Think: distribute or divide first","-3x - 6 = 9 → -3x = 15 → x = -5."),
    ]),
    s("Inequalities",[
      ("What is the difference between < and ≤?","Think: strict vs. inclusive inequality","< means strictly less than (open circle on graph). ≤ means less than OR equal to (closed circle)."),
      ("Solve and graph: 2x - 3 > 7","Think: solve like equation, flip sign when dividing by negative","2x > 10 → x > 5. Open circle at 5, arrow pointing right."),
      ("Solve: -4x ≤ 20","Think: flip inequality when dividing by negative","x ≥ -5. (Dividing by negative flips inequality.)"),
      ("Write an inequality for: At least 35 people must attend.","Think: at least = greater than or equal to","p ≥ 35."),
    ]),
    s("Real-world equations",[
      ("You buy x books at $12 each and pay $4 for shipping. You spend $52 total. Write and solve.","Think: 12x + 4 = 52","12x = 48 → x = 4 books."),
      ("A phone plan charges $25 per month plus $0.10 per text. You pay $31. How many texts?","Think: 25 + 0.10t = 31","0.10t = 6 → t = 60 texts."),
      ("You need at least $200 for a trip. You have $65 and earn $15/hour. How many hours?","Think: 65 + 15h ≥ 200","15h ≥ 135 → h ≥ 9. At least 9 hours."),
      ("What are the steps for writing an equation from a word problem?","Think: systematic approach","(1) Identify the unknown (let x = ?). (2) Identify the relationship. (3) Write the equation. (4) Solve. (5) Check in the original context."),
    ]),
  ],
  # U4: Geometry
  [
    s("Scale and similar figures",[
      ("What makes two figures similar?","Think: same shape, not necessarily same size","Same angles, corresponding sides proportional. Written ABC ~ DEF."),
      ("Two similar triangles have sides 6 and 9. What is the scale factor?","Think: ratio of corresponding sides","6/9 = 2/3. Scale factor = 2:3."),
      ("If a triangle has sides 4, 6, 8 and is similar to a triangle with longest side 24, find the other sides.","Think: multiply by scale factor (24/8 = 3)","4×3=12; 6×3=18; 8×3=24. Sides: 12, 18, 24."),
      ("How is scale factor used in real life?","Think: maps, models, blueprints","Architects use scale drawings, map makers use scale factors to represent large objects proportionally."),
    ]),
    s("Area of polygons",[
      ("What is the formula for the area of a triangle?","Think: A = (1/2)bh","Area = (1/2) × base × height. The height must be perpendicular to the base."),
      ("Find the area of a parallelogram with base 9 cm and height 6 cm.","Think: A = base × height","A = 9 × 6 = 54 cm squared."),
      ("A trapezoid has bases 5 m and 9 m, and height 4 m. Find its area.","Think: A = (1/2)(b1+b2)h","A = (1/2)(5 + 9)(4) = (1/2)(14)(4) = 28 m squared."),
      ("A composite figure has a rectangle (8x5) and a triangle on top (base 8, height 3). Find total area.","Think: add the areas","Rectangle: 40; Triangle: (1/2)(8)(3)=12. Total = 52."),
    ]),
    s("Circles",[
      ("What are the formulas for circumference and area of a circle?","Think: C = 2 pi r; A = pi r squared","Circumference = 2*pi*r or pi*d. Area = pi*r*r. Both use pi ≈ 3.14159."),
      ("A circle has radius 7 cm. Find circumference and area (use pi ≈ 3.14).","Think: apply formulas","C = 2(3.14)(7) = 43.96 cm. A = 3.14 × 49 = 153.86 cm squared."),
      ("What is the difference between radius, diameter, and circumference?","Think: r, d=2r, C=pi*d","Radius: center to edge. Diameter: all the way across (= 2r). Circumference: distance around the circle."),
      ("A circular garden has area 78.5 m squared. Find the radius (pi ≈ 3.14).","Think: A = pi*r*r, solve for r","78.5 = 3.14*r*r → r squared = 25 → r = 5 m."),
    ]),
    s("3D figures: surface area",[
      ("What is surface area?","Think: total area of all faces of a 3D figure","The total area of every face of a 3D shape. Measured in square units."),
      ("Find the surface area of a rectangular prism: 4×3×2 cm.","Think: 2(lw + lh + wh)","2(4×3 + 4×2 + 3×2) = 2(12 + 8 + 6) = 2(26) = 52 cm squared."),
      ("A cube has side length 5 cm. Find its surface area.","Think: 6 equal square faces","6 × 5 × 5 = 6 × 25 = 150 cm squared."),
      ("What is the surface area of a triangular prism with triangular face area 6, perimeter of triangle 12, and prism height 10?","Think: 2(triangle area) + (perimeter × height)","SA = 2(6) + 12(10) = 12 + 120 = 132 square units."),
    ]),
    s("3D figures: volume",[
      ("What is the formula for the volume of a rectangular prism?","Think: V = length × width × height","V = l × w × h. Volume is measured in cubic units."),
      ("Find the volume of a cube with edge length 6 cm.","Think: V = s cubed","V = 6 × 6 × 6 = 216 cm cubed."),
      ("A triangular prism has triangular cross-section area 12 cm squared and length 8 cm. Find the volume.","Think: V = base area × length","V = 12 × 8 = 96 cm cubed."),
      ("A box is 5 m × 3 m × 2 m. How many 1 m cubed crates fit inside?","Think: volume = maximum crates","V = 5 × 3 × 2 = 30 m cubed. 30 crates."),
    ]),
  ],
  # U5: Statistics and Probability
  [
    s("Mean, median, mode, range",[
      ("Find the mean of: 8, 12, 7, 15, 10, 6.","Think: sum divided by count","Sum = 58; Mean = 58/6 ≈ 9.67."),
      ("Find the median of: 3, 7, 9, 14, 21, 25.","Think: middle values when even count","Middle two: 9 and 14. Median = (9+14)/2 = 11.5."),
      ("What measure of center is best when a dataset has extreme outliers?","Think: which measure resists outliers?","Median — it is not influenced by extreme values. Mean is pulled toward outliers."),
      ("Salaries: $40K, $42K, $44K, $45K, $300K. How does mean vs. median describe the typical salary?","Think: outlier effect","Mean ≈ $94.2K (distorted by $300K). Median = $44K. Median is more representative here."),
    ]),
    s("Data displays",[
      ("What is a stem-and-leaf plot? What does it show?","Think: displays actual data while showing distribution","Organizes data by place value: stem = leading digit(s), leaf = last digit. Preserves individual values while showing shape of distribution."),
      ("What is the difference between a histogram and a bar graph?","Think: continuous data vs. categories","Histogram: bars touch; shows frequency distribution of continuous data. Bar graph: bars have gaps; compares categorical data."),
      ("What is a box-and-whisker plot? Name its five components.","Think: 5-number summary visualized","Minimum, Q1, Median (Q2), Q3, Maximum. The box spans Q1 to Q3 (interquartile range)."),
      ("What is the interquartile range (IQR) and why is it useful?","Think: spread of the middle 50%","IQR = Q3 - Q1. Measures spread of the middle 50% of data. Resistant to outliers unlike range."),
    ]),
    s("Probability basics",[
      ("What is probability? What values can it take?","Think: likelihood expressed as a number","Probability measures how likely an event is. Values range from 0 (impossible) to 1 (certain)."),
      ("A bag has 4 red and 6 blue marbles. What is P(red)?","Think: favorable / total","P(red) = 4/(4+6) = 4/10 = 2/5 = 0.4 = 40%."),
      ("What is the complement of an event?","Think: everything that is NOT the event","Complement of event A = all outcomes that are NOT A. P(not A) = 1 - P(A)."),
      ("A die is rolled. P(not 6) = ?","Think: complement rule","P(6) = 1/6. P(not 6) = 1 - 1/6 = 5/6."),
    ]),
    s("Compound probability",[
      ("What is the difference between independent and dependent events?","Think: does one affect the other?","Independent: outcome of one does not affect the other (coin flips). Dependent: outcome of one changes probabilities of the next (drawing without replacement)."),
      ("A coin is flipped and a die is rolled. What is P(heads AND 4)?","Think: multiply probabilities for independent events","P(heads) × P(4) = 1/2 × 1/6 = 1/12."),
      ("A bag has 3 red and 5 blue marbles. P(red then blue) without replacement?","Think: dependent events — update denominator","P(red) = 3/8. Given red drawn, P(blue) = 5/7. P(both) = 3/8 × 5/7 = 15/56."),
      ("What is a sample space? Create one for flipping two coins.","Think: all possible outcomes","Sample space: all possible outcomes. Two coins: HH, HT, TH, TT. P(exactly one head) = 2/4 = 1/2."),
    ]),
    s("Statistical sampling",[
      ("What is the difference between a population and a sample?","Think: whole group vs. a subset","Population: all members of a group. Sample: a smaller subset chosen to represent the population."),
      ("What is a random sample and why is it important?","Think: every member has an equal chance of selection","A random sample gives every member an equal chance of selection. Reduces bias and makes the sample representative."),
      ("What is sampling bias? Give one example.","Think: systematic error in who is selected","Sampling bias: sample is not representative. Example: surveying food preferences only in the cafeteria excludes students who do not eat there."),
      ("A survey of 50 students found 60% prefer science. Can you conclude 60% of all students prefer science?","Think: sample size and representativeness","The sample is small. If randomly selected it gives an estimate, but could vary significantly with another sample of 50. Larger random samples give more reliable estimates."),
    ]),
  ],
]
print("G7 math complete")

P[7]["science"] = [
  # U1: Cells and Life
  [
    s("Cell theory and cell structure",[
      ("State the three principles of cell theory.","Think: foundational biology","(1) All living things are made of cells. (2) Cells are the basic unit of life. (3) All cells come from pre-existing cells."),
      ("What are the key differences between prokaryotic and eukaryotic cells?","Think: nucleus or no nucleus","Prokaryotic: no membrane-bound nucleus, no organelles (bacteria, archaea). Eukaryotic: has a nucleus and membrane-bound organelles (plants, animals, fungi)."),
      ("What is the function of the cell membrane?","Think: control what enters and exits","Regulates what enters and exits the cell (selective permeability). Composed of a phospholipid bilayer with embedded proteins."),
      ("Name four organelles and their functions.","Think: mitochondria, nucleus, ribosomes, vacuoles","Mitochondria: produces ATP. Nucleus: stores DNA. Ribosomes: synthesize proteins. Vacuole: stores water and materials."),
    ]),
    s("Photosynthesis",[
      ("Write the overall equation for photosynthesis.","Think: inputs and outputs","6CO2 + 6H2O + light energy gives C6H12O6 + 6O2."),
      ("Where does photosynthesis occur in a plant cell?","Think: which organelle?","In the chloroplast, specifically in the thylakoid membranes (light reactions) and the stroma (Calvin cycle)."),
      ("What role does chlorophyll play in photosynthesis?","Think: absorbing light energy","Chlorophyll is the green pigment that absorbs light energy (primarily red and blue wavelengths) to power photosynthesis."),
      ("Why is photosynthesis essential for life on Earth?","Think: food webs and oxygen","Photosynthesis produces the oxygen we breathe and is the entry point of energy into nearly every food web on Earth."),
    ]),
    s("Cellular respiration",[
      ("Write the overall equation for cellular respiration.","Think: opposite of photosynthesis","C6H12O6 + 6O2 gives 6CO2 + 6H2O + ATP energy."),
      ("How are photosynthesis and cellular respiration related?","Think: they cycle the same molecules","Products of one are reactants of the other. Together they cycle carbon and oxygen through ecosystems."),
      ("What is ATP and why does the cell need it?","Think: cellular energy currency","ATP (adenosine triphosphate) is the cell energy currency. Energy from food is converted to ATP, which powers virtually every cellular process."),
      ("What is the difference between aerobic and anaerobic respiration?","Think: with or without oxygen","Aerobic: uses oxygen, produces about 36-38 ATP per glucose. Anaerobic: no oxygen, produces only about 2 ATP; produces lactic acid or ethanol plus CO2."),
    ]),
    s("Plant and animal cells",[
      ("Name three structures found in plant cells but NOT animal cells.","Think: what is unique to plants?","(1) Cell wall. (2) Chloroplasts. (3) Large central vacuole."),
      ("What is the cell wall and what does it do?","Think: rigid outer layer of plant cells","A rigid layer outside the cell membrane, made of cellulose. Provides structural support and protection."),
      ("Why do not animal cells have chloroplasts?","Think: animals eat food; plants make food","Animals obtain energy by consuming food. Only organisms that photosynthesize need chloroplasts."),
      ("What is diffusion? How do substances move across the cell membrane?","Think: movement from high to low concentration","Diffusion: movement of particles from high to low concentration, requiring no energy (passive transport). Osmosis: diffusion of water across a semipermeable membrane."),
    ]),
    s("Mitosis",[
      ("What is mitosis? Why do cells undergo it?","Think: cell division for growth and repair","Mitosis: division of one cell into two genetically identical daughter cells. Purpose: growth, tissue repair, and asexual reproduction."),
      ("Name and describe the four phases of mitosis in order.","Think: PMAT","Prophase: chromosomes condense, spindle forms. Metaphase: chromosomes align at center. Anaphase: chromosomes pulled to opposite poles. Telophase: nuclear envelopes reform."),
      ("What is the result of mitosis?","Think: 1 parent gives 2 identical daughters","One parent cell gives two genetically identical daughter cells, each with the same chromosome number as the parent."),
      ("What happens if cells divide uncontrollably?","Think: cancer","Uncontrolled cell division can cause cancer. Tumors form when cells ignore normal signals to stop dividing."),
    ]),
  ],
  # U2: Earth's Systems
  [
    s("Rock cycle",[
      ("What are the three types of rocks and how does each form?","Think: igneous, sedimentary, metamorphic","Igneous: cooled magma or lava. Sedimentary: compressed and cemented sediment layers. Metamorphic: existing rock transformed by heat and pressure without melting."),
      ("Describe two pathways in the rock cycle.","Think: how do rocks change from one type to another?","(1) Igneous to Sedimentary: erosion creates sediment then compaction and cementation. (2) Sedimentary to Metamorphic: burial increases heat and pressure. Any rock can melt to become igneous."),
      ("What is the difference between intrusive and extrusive igneous rock?","Think: slow cooling vs. fast cooling","Intrusive: magma cools slowly underground, gives large crystals (granite). Extrusive: lava cools quickly at surface, gives small or no crystals (basalt, obsidian)."),
      ("Why does limestone often contain fossils?","Think: how do sedimentary rocks preserve organisms?","Limestone is a sedimentary rock formed from accumulated shells and marine organisms. Organic material gets preserved between sediment layers, forming fossils."),
    ]),
    s("Earth's layers",[
      ("Name Earth's four internal layers from outside to inside.","Think: crust, mantle, outer core, inner core","Crust (rigid, thinnest), Mantle (semi-solid rock, largest layer), Outer Core (liquid iron and nickel), Inner Core (solid iron and nickel, hottest)."),
      ("Why is Earth's outer core liquid while the inner core is solid?","Think: pressure vs. temperature","Both have similar high temperatures. The inner core is solid because the immense pressure forces atoms into a solid arrangement despite the extreme heat."),
      ("What evidence do scientists use to study Earth's interior?","Think: we cannot drill that deep","Seismic waves: S-waves cannot travel through liquids, confirming the outer core is liquid. P-waves refract at layer boundaries. Also volcanic material and magnetic field patterns."),
      ("What causes Earth's magnetic field?","Think: outer core convection","The movement of liquid iron in the outer core generates electrical currents, which create Earth's magnetic field. This field protects Earth from harmful solar wind."),
    ]),
    s("Plate tectonics",[
      ("What is the theory of plate tectonics?","Think: Earth's outer shell moves","Earth's lithosphere is divided into tectonic plates that move on the semi-molten asthenosphere. Their movement causes earthquakes, volcanoes, and mountain building."),
      ("Name and describe the three types of plate boundaries.","Think: divergent, convergent, transform","Divergent: plates move apart (new crust created). Convergent: plates collide (mountains, trenches). Transform: plates slide past each other (earthquakes)."),
      ("What happens at a subduction zone?","Think: oceanic plate dives under continental plate","A denser oceanic plate dives under a lighter continental plate. Creates deep ocean trenches, volcanic mountain ranges, and frequent earthquakes."),
      ("What is the evidence for continental drift?","Think: Wegener's clues","Matching fossil species on different continents, matching rock formations, coastlines that fit like puzzle pieces, and paleoclimatic evidence."),
    ]),
    s("Weathering and erosion",[
      ("What is the difference between weathering and erosion?","Think: breaking down vs. moving","Weathering: breaking down rocks in place. Erosion: transportation of weathered material by wind, water, ice, or gravity."),
      ("What is the difference between chemical and physical weathering?","Think: composition changes vs. shape changes","Physical: breaks rocks into smaller pieces without changing chemical composition (freeze-thaw, abrasion). Chemical: changes the mineral composition (oxidation, acid rain dissolving limestone)."),
      ("How does freeze-thaw weathering work?","Think: water expands when it freezes","Water enters rock cracks, freezes and expands about 9%, widening the crack. Repeated cycles fracture rock. Common in areas with temperatures that cross freezing regularly."),
      ("What factors affect the rate of weathering and erosion?","Think: climate, rock type, surface area, vegetation","Climate (wet and warm speeds chemical weathering), rock hardness, surface area (smaller pieces weather faster), vegetation, and slope."),
    ]),
  ],
  # U3: Matter and Energy
  [
    s("Atoms and elements",[
      ("What are the three main subatomic particles? Where is each located?","Think: proton, neutron, electron","Proton: nucleus, positive charge. Neutron: nucleus, no charge. Electron: orbits nucleus, negative charge."),
      ("What defines an element?","Think: atomic number is unique to each element","The number of protons (atomic number) defines an element. All atoms of carbon have 6 protons."),
      ("What is the difference between atomic number and mass number?","Think: protons vs. protons plus neutrons","Atomic number = number of protons. Mass number = protons + neutrons. Example: Carbon-12 has atomic number 6 and mass 12."),
      ("What are isotopes?","Think: same protons, different neutrons","Atoms of the same element with different numbers of neutrons. Example: Carbon-12 and Carbon-14. Same chemical properties, different masses."),
    ]),
    s("Periodic table",[
      ("How is the periodic table organized?","Think: rows = periods; columns = groups","Rows (periods): elements in increasing atomic number. Columns (groups or families): elements with similar properties and same number of valence electrons."),
      ("What is a period vs. a group in the periodic table?","Think: horizontal row vs. vertical column","Period: horizontal row; same number of electron shells. Group: vertical column; same number of valence electrons and similar chemical behavior."),
      ("What are the main categories of elements on the periodic table?","Think: metals, nonmetals, metalloids","Metals: left and center (shiny, conductive, malleable). Nonmetals: upper right (poor conductors). Metalloids: staircase line (properties of both)."),
      ("What are valence electrons and why do they matter?","Think: outermost electrons determine reactivity","Valence electrons: electrons in the outermost shell. They determine chemical properties and bonding behavior. Atoms react to achieve 8 valence electrons (octet rule)."),
    ]),
    s("Physical vs. chemical changes",[
      ("What is the difference between a physical and a chemical change?","Think: composition changes vs. only form changes","Physical: form or state changes but substance identity is the same (cutting paper, melting ice). Chemical: new substances with different properties are formed (burning, rusting)."),
      ("Name four signs that a chemical change has occurred.","Think: observable evidence","(1) Color change. (2) Gas produced (bubbles). (3) Precipitate forms. (4) Energy released or absorbed (heat or light)."),
      ("Is dissolving salt in water a physical or chemical change?","Think: can you get the salt back?","Physical change. The salt dissolves but no new substance forms. Evaporate the water and the salt crystals reappear."),
      ("What evidence indicates burning wood is a chemical change?","Think: apply all four signs","Color change (black charcoal), gas produced (CO2 and smoke), heat and light released, and the wood cannot become wood again — irreversible."),
    ]),
    s("Conservation of mass",[
      ("State the Law of Conservation of Mass.","Think: matter cannot be created or destroyed","In any physical or chemical change, matter is neither created nor destroyed. The total mass of reactants equals the total mass of products."),
      ("25 g of sodium + 38.5 g of chlorine react completely. What is the mass of NaCl produced?","Think: mass is conserved","25 + 38.5 = 63.5 g of NaCl."),
      ("A student burns 10 g of wood and finds only 1 g of ash. Is mass conserved?","Think: where did the rest go?","Yes — mass is conserved. 9 g escaped as gases (CO2, water vapor, smoke). Collecting all products gives total mass of 10 g."),
      ("How does conservation of mass support the particle model of matter?","Think: atoms are rearranged, not created or destroyed","In chemical reactions, atoms are rearranged into new combinations. No atom is created or destroyed. This is evidence that matter is made of indestructible particles."),
    ]),
  ],
  # U4: Ecosystems
  [
    s("Food webs and energy flow",[
      ("What is the 10% rule in energy transfer?","Think: energy lost as heat at each trophic level","Only about 10% of energy transfers from one trophic level to the next. 90% is lost as heat. This is why food chains rarely have more than 5 levels."),
      ("What is the difference between a food chain and a food web?","Think: single path vs. interconnected network","Food chain: single linear path of energy flow. Food web: interconnected network of all food chains in an ecosystem — more accurately represents feeding relationships."),
      ("What are producers, consumers, and decomposers?","Think: how they get energy","Producers: make own food via photosynthesis. Consumers: eat other organisms. Decomposers: break down dead organic matter and return nutrients to soil."),
      ("Why would removing wolves from a food web affect plant populations?","Think: trophic cascade","Without wolves, deer and elk populations increase, they overgraze, and plant populations decline. Removing one species ripples through the entire ecosystem."),
    ]),
    s("Biomes",[
      ("Name four terrestrial biomes and one key characteristic of each.","Think: major land ecosystems","Tropical rainforest: high rainfall and biodiversity. Desert: less than 25 cm rain per year. Temperate forest: deciduous trees and four seasons. Tundra: permafrost and very cold."),
      ("What determines which biome exists in a region?","Think: climate = temperature + precipitation","Primarily temperature and precipitation. Latitude and proximity to oceans also determine climate, which determines which organisms can survive there."),
      ("How are organisms adapted to survive in the desert?","Think: minimizing water loss, surviving heat","Cacti have thick waxy skin and water-storing stems. Desert animals are nocturnal, produce concentrated urine, and burrow. Many adaptations conserve water."),
      ("What is biodiversity and why is it important?","Think: variety of life; ecosystem stability","Biodiversity: the variety of life in an area. Greater biodiversity makes ecosystems more resilient — if one species declines, others can fill its role."),
    ]),
    s("Nutrient cycles",[
      ("Describe the water cycle.","Think: evaporation, condensation, precipitation, collection","Water evaporates from oceans and lakes, rises as vapor, condenses into clouds, falls as precipitation, collects in rivers or seeps underground. Powered by solar energy."),
      ("What is the carbon cycle? Why is it important?","Think: how carbon moves through ecosystems","Carbon moves through photosynthesis (CO2 into plants), consumption, respiration (CO2 released), and decomposition. Burning fossil fuels adds extra CO2, warming the atmosphere."),
      ("What is the nitrogen cycle? Why do plants need nitrogen?","Think: nitrogen from atmosphere to soil to organisms","Nitrogen gas is fixed by bacteria into forms plants can absorb. Plants use it for proteins and DNA. Animals get nitrogen by eating plants. Decomposers return nitrogen to soil."),
      ("How do human activities disrupt nutrient cycles?","Think: fertilizers, burning, deforestation","Excess fertilizer causes runoff and eutrophication. Burning fossil fuels adds excess CO2. Deforestation disrupts carbon and water cycles."),
    ]),
    s("Human impacts on ecosystems",[
      ("What is habitat destruction and why is it the leading cause of biodiversity loss?","Think: species need specific environments to survive","Habitat destruction: clearing or degrading natural habitats. Species lose their food, shelter, and breeding sites, leading to population decline or extinction."),
      ("What are invasive species and why can they be harmful?","Think: non-native species without natural predators","Invasive species introduced to new ecosystems can outcompete native species, disrupt food webs, and reduce biodiversity. Examples: kudzu vine, cane toads, zebra mussels."),
      ("What is pollution and what are three types?","Think: contamination that harms ecosystems","(1) Air pollution: CO2, smog, acid rain. (2) Water pollution: chemical runoff, sewage, plastics. (3) Soil pollution: pesticides, heavy metals."),
      ("What can individuals do to reduce their environmental impact?","Think: reduce, reuse, recycle, and beyond","Reduce consumption, reuse materials, recycle, choose plant-based foods, reduce car use, conserve water and energy, and support conservation policies."),
    ]),
  ],
]
print("G7 science complete")

P[7]["ela"] = [
  # U1: Reading Fiction
  [
    s("Character analysis",[
      ("What is character motivation and how does it drive plot?","Think: why characters do what they do","Character motivation: the reason behind a character's actions and goals. Motivations drive decisions, which create plot. Understanding motivation helps predict behavior and understand themes."),
      ("What is the difference between direct and indirect characterization?","Think: told vs. shown","Direct: author tells you the trait (She was stubborn). Indirect: shown through speech, actions, appearance, thoughts, and others' reactions (STEAL method)."),
      ("How does a character change across a novel?","Think: who they are at the start vs. the end","Compare the character's beliefs, values, behaviors, and relationships at the beginning and end. What caused the change? Significant change = dynamic character. No change = static."),
      ("What is internal vs. external conflict?","Think: within the character vs. with outside forces","Internal: character vs. self (guilt, fear, indecision). External: character vs. character, nature, society, or technology. Most stories have both."),
    ]),
    s("Plot structure",[
      ("What is the difference between the climax and the turning point?","Think: they are often the same thing","The climax is the highest point of tension where the central conflict is confronted. The turning point is the moment the outcome becomes inevitable. They often coincide."),
      ("What is foreshadowing? Give an example.","Think: early clues about future events","Foreshadowing: hints about what will happen later. Example: A storm gathering as two characters argue foreshadows their relationship breakdown. Builds tension and rewards re-reading."),
      ("What is a flashback and why do authors use it?","Think: interrupting forward narrative with past events","A scene that shifts to events before the story's current time. Used to reveal character backstory, explain motivations, or provide context for current events."),
      ("What is the narrative arc and how does it create emotional impact?","Think: tension builds then releases","Rising action builds tension. The climax delivers the emotional payoff. Falling action allows processing. Resolution provides closure. This arc creates a satisfying story."),
    ]),
    s("Theme and symbolism",[
      ("What is a symbol in literature? How do you identify one?","Think: object, person, or place that represents something beyond itself","A symbol is something concrete that represents an abstract idea. Identify by: it appears repeatedly, given unusual attention, characters interact with it meaningfully."),
      ("How does analyzing symbols help you understand theme?","Think: symbols embody the theme","What a symbol represents often points to the theme. A caged bird symbolizing trapped freedom suggests a theme about the desire for freedom and the reality of oppression."),
      ("How can the title of a novel be symbolic?","Think: title often hints at theme or central symbol","Authors choose titles deliberately. The Great Gatsby — how great is he really (irony). To Kill a Mockingbird — the mockingbird symbolizes innocence. Analyzing the title often reveals thematic intent."),
      ("What is the difference between a symbol and a motif?","Think: single image vs. recurring pattern","Symbol: a specific object or image with deeper meaning. Motif: a recurring element throughout the work that contributes to theme. A symbol can become a motif if it recurs."),
    ]),
    s("Point of view and narrator",[
      ("What is an unreliable narrator? Name one example.","Think: narrator whose account we should question","A narrator whose credibility is compromised — biased, mentally unstable, too young to understand, or deliberately deceptive. Example: Holden Caulfield in Catcher in the Rye."),
      ("What is dramatic irony?","Think: audience knows what characters do not","Dramatic irony: reader or audience knows something the character does not. Creates tension, suspense, or dark humor."),
      ("How does first-person narration limit what the reader knows?","Think: restricted perspective","We only know what the narrator observes, thinks, and feels. Cannot know what happens when they are not there or what other characters truly think."),
      ("How do third-person omniscient and third-person limited differ?","Think: all-knowing vs. limited to one mind","Omniscient: narrator knows thoughts and feelings of all characters. Limited: narrator follows only one character's inner experience but uses he or she rather than I."),
    ]),
    s("Literary devices",[
      ("What is imagery? Give an example of visual imagery.","Think: language that appeals to the senses","Imagery: language appealing to the senses. Visual: The crimson sun sank below the jagged peaks. Auditory: The creek chattered over smooth stones. Imagery makes writing vivid and immersive."),
      ("What is irony? Name the three types.","Think: difference between expectation and reality","Verbal: saying the opposite of what you mean (sarcasm). Situational: outcome is opposite of what is expected. Dramatic: audience knows what characters do not."),
      ("What is allusion and how does it enrich a text?","Think: reference to another work or historical event","An allusion is an indirect reference to a person, work, event, or myth. She had a Midas touch alludes to Greek mythology — the reader understands instantly without further explanation."),
      ("What is the effect of diction choices on tone?","Think: word choice creates the author's attitude","Diction (word choice) shapes tone (the author's attitude). The old man shuffled vs. The elderly gentleman strolled — same action, very different tone."),
    ]),
  ],
  # U2: Nonfiction
  [
    s("Text structure",[
      ("How does identifying text structure improve reading comprehension?","Think: structure tells you HOW to read the text","Knowing the structure tells you what to look for. Cause and effect: look for causes and results. Compare and contrast: look for similarities and differences. Structure guides active reading."),
      ("What signal words indicate a cause-and-effect structure?","Think: because, therefore, as a result","Because, since, due to, causes, leads to, therefore, as a result, consequently. These signal that one thing is causing or producing another."),
      ("How can the same content be organized using different text structures?","Think: same information, different emphasis","Information about climate change could use: problem and solution, cause and effect, or compare and contrast. Structure affects emphasis and reader takeaway."),
      ("What is the function of headings, subheadings, and topic sentences?","Think: signposts for the reader","Headings and subheadings organize sections and signal topic shifts. Topic sentences state the main point of each paragraph. Together they create a readable, well-organized text."),
    ]),
    s("Evaluating arguments",[
      ("What is a logical fallacy? Name two examples.","Think: flawed reasoning that appears valid","Ad hominem: attacking the person instead of the argument. False dichotomy: presenting only two options when more exist. Straw man: misrepresenting the opponent's argument to attack it more easily."),
      ("What is the difference between fact and opinion in an argument?","Think: verifiable vs. personal judgment","Fact: can be verified (The Earth orbits the sun). Opinion: personal judgment not directly verifiable (The Earth's landscape is beautiful). Strong arguments use facts as evidence."),
      ("How do you evaluate the credibility of a source?","Think: who wrote it, who published it, what evidence","Consider: author's expertise, publisher, date (is it current?), purpose (informative vs. selling something), and evidence (cited sources vs. unsupported claims)."),
      ("What is the difference between a strong and weak argument?","Think: clear claim, relevant evidence, valid reasoning","Strong: clear claim, relevant and credible evidence, logical reasoning, acknowledges counterarguments. Weak: vague claim, unsupported opinions, logical fallacies, ignores opposing evidence."),
    ]),
    s("Summarizing nonfiction",[
      ("What belongs in a good summary of a nonfiction article?","Think: main idea plus major supporting points","The central claim, major supporting points (not minor details), and the conclusion. Written in your own words without personal opinions."),
      ("What is paraphrasing and how does it differ from summarizing?","Think: restating vs. condensing","Paraphrase: restate a specific passage in your own words at approximately the same length. Summary: condense the entire piece to its essential points."),
      ("How do you identify what is and is not important in an article?","Think: main idea test","Important: directly supports the main claim, appears in topic sentences, repeated. Less important: examples, minor statistics, tangential details."),
      ("Why should you avoid including personal opinions in a summary?","Think: summary reports the author's ideas, not yours","A summary represents what the author said objectively. Adding your opinion distorts the author's meaning."),
    ]),
    s("Multimedia and text",[
      ("How can a graph or diagram add to an informational article?","Think: visual data communicates differently than words","Visuals can show patterns at a glance, clarify spatial relationships, and provide evidence. They should directly support the article's claims."),
      ("What should you look for when analyzing a graph or chart?","Think: title, labels, scale, source","Title (what it shows), axis labels (what is measured), scale (is it manipulated?), source (is data credible?), and trend (what pattern does it show?)."),
      ("Can the same information look different in a chart vs. a graph? Give an example.","Think: type of data determines best visual","A table shows exact numbers. A bar graph makes comparisons easier at a glance. A line graph shows trends over time. The choice affects what the reader focuses on."),
      ("What is misleading about a graph with a y-axis that does not start at zero?","Think: visual distortion of data","Starting a y-axis at a number other than zero exaggerates visual differences. Small differences look large, misleading readers about the magnitude of change."),
    ]),
    s("Cite evidence",[
      ("What does it mean to cite evidence from a text?","Think: point to specific passages to support your claim","Quoting or paraphrasing specific passages from the text to support your analysis — not just vaguely saying the author says something. Evidence must be relevant to your claim."),
      ("What is the difference between a direct quote and a paraphrase as evidence?","Think: exact words vs. restated meaning","Direct quote: exact words in quotation marks. Paraphrase: author's idea restated in your own words without quotation marks. Both require citation."),
      ("How do you introduce evidence in a paragraph?","Think: introduce, insert, explain","(1) Introduce: who said it and context. (2) Insert: quote or paraphrase. (3) Explain: connect the evidence to your claim. This is the three-part evidence sandwich."),
      ("Why is it not enough to just quote evidence without explaining it?","Think: the so what question","Evidence alone does not argue — analysis does. You must explain how and why the evidence supports your claim. Without explanation, the reader must make the connection themselves."),
    ]),
  ],
  # U3: Writing
  [
    s("Narrative craft",[
      ("What is the difference between scene and summary in narrative writing?","Think: showing moment-by-moment vs. condensing time","Scene: shows action in real-time with dialogue and sensory detail (slows the story). Summary: condenses longer time periods quickly. Strong writers balance both."),
      ("How do you write a compelling opening scene?","Think: plunge the reader into action or intrigue","Start in media res (in the middle of action), with vivid sensory detail, a character with a problem, or an intriguing opening line. Avoid lengthy exposition at the start."),
      ("What is the difference between showing emotions vs. telling emotions?","Think: actions and physical responses vs. label","Telling: She was angry. Showing: Her jaw tightened. She picked up her keys and slammed the door. Showing creates emotional connection because the reader experiences the emotion."),
      ("How do you write authentic dialogue?","Think: natural, character-specific, and functional","Read dialogue aloud — if it sounds unnatural, revise. Dialogue should reveal character, advance plot, or create conflict. Use tags and action beats strategically."),
    ]),
    s("Argument writing",[
      ("What is a claim and how is it different from a thesis?","Think: in argument writing, claim equals thesis","In argument writing these terms are often interchangeable. Both state your position. A claim specifically asserts a stance that requires evidence and reasoning to prove."),
      ("What are counterclaims and why must you address them?","Think: opposing arguments you need to refute","A counterclaim is the strongest argument against your position. Addressing it shows intellectual honesty, builds credibility, and prevents your argument from seeming one-sided."),
      ("How do you rebut a counterclaim?","Think: acknowledge, then refute or concede","(1) Acknowledge: While some argue... (2) Refute: However, evidence shows... OR Concede and pivot: This is true, but... followed by why your position still holds."),
      ("What is the difference between a logical appeal (logos) and an emotional appeal (pathos)?","Think: evidence vs. feelings","Logos: reasoning and evidence (statistics, research, examples). Pathos: appeals to emotion (stories, vivid imagery). Academic arguments rely primarily on logos. Ethos = credibility of the author."),
    ]),
    s("Research and citations",[
      ("What is MLA format for citing a book?","Think: author last name, first name, Title in Italics","Author Last, First Name. Title of Book. Publisher, Year. Example: Rowling, J.K. Harry Potter and the Sorcerer's Stone. Scholastic, 1998."),
      ("What is the difference between a Works Cited page and an in-text citation?","Think: full citation vs. brief reference","In-text citation: brief parenthetical note within the paper (Author, page). Works Cited: full citation information at the end of the paper. Both are required in MLA."),
      ("Why is plagiarism serious even if unintentional?","Think: it is about giving credit for others' intellectual work","Plagiarism is taking credit for someone else's work. It is dishonest, disrespects the original creator, and undermines academic integrity. Always cite sources to avoid unintentional plagiarism."),
      ("What are the steps for integrating a quote smoothly into your own writing?","Think: sandwich method","(1) Introduce: context and attribution. (2) Insert: the quote in quotation marks. (3) Analyze: explain its significance and connect to your claim."),
    ]),
    s("Revision strategies",[
      ("What is reverse outlining and how does it help revision?","Think: outline the draft after writing to reveal structure","After drafting, write a one-sentence summary of each paragraph. Check: Does each paragraph have a clear main idea? Are they in logical order? Do they all support the thesis?"),
      ("What is the difference between higher-order concerns and lower-order concerns in revision?","Think: big picture vs. surface level","Higher-order: thesis, argument, organization, evidence, analysis. Lower-order: grammar, punctuation, spelling. Always address higher-order first."),
      ("How do you identify and fix a weak paragraph?","Think: what makes a paragraph fail?","Weak paragraphs: lack a clear topic sentence, drift off-topic, have evidence without analysis, or are too short. Fix by writing a clear topic sentence, removing off-topic sentences, and adding analysis after evidence."),
      ("What does concision mean in writing? Rewrite this wordy sentence: Due to the fact that it was raining outside, we made the decision to stay in our house.","Think: say the same thing in fewer words","Because it was raining, we stayed home. Eliminate phrases like due to the fact that (because) and made the decision to (decided to)."),
    ]),
    s("Grammar for effect",[
      ("What is the Oxford comma and why do some argue it matters?","Think: comma before and in a list","The Oxford comma comes before and in a list of three or more items. It prevents ambiguity: I love my parents, Maya and Alex could mean Maya and Alex are my parents. Adding the Oxford comma — I love my parents, Maya, and Alex — clearly means four people."),
      ("What is the difference between active and passive voice?","Think: subject acts vs. subject receives action","Active: subject performs the action (The student wrote the essay). Passive: subject receives the action (The essay was written by the student). Active is generally clearer and more direct."),
      ("What is a misplaced modifier? Correct this: Running down the street, the trees blurred past her.","Think: modifier must be next to the word it describes","Running down the street appears to describe trees. Fixed: Running down the street, she watched the trees blur past."),
      ("What is parallel structure and why does it matter?","Think: matching grammatical forms in a series","Items in a series should use the same grammatical form. Wrong: She enjoys hiking, to swim, and reading. Correct: She enjoys hiking, swimming, and reading. Parallel structure makes writing clearer and more elegant."),
    ]),
  ],
  # U4: Language and Media Literacy
  [
    s("Connotation and word choice",[
      ("What is the difference between denotation and connotation?","Think: dictionary meaning vs. emotional associations","Denotation: the literal dictionary definition. Connotation: emotional associations beyond the definition. Cheap and economical have similar denotations but very different connotations."),
      ("How does connotation affect persuasion?","Think: emotionally loaded words manipulate or resonate","Word choice can make readers feel positively or negatively without presenting facts. Freedom fighters vs. rebels — same people, very different emotional response. Recognizing connotation helps identify bias."),
      ("What is euphemism and how is it used?","Think: milder word for something unpleasant","Euphemism: replacing a harsh term with a gentler one. Passed away for died. Sometimes appropriate (sensitivity), sometimes used to obscure truth (collateral damage for civilian casualties)."),
      ("How does diction change depending on audience and purpose?","Think: formal vs. informal; technical vs. accessible","Scientists write for colleagues using technical jargon. That same scientist writes for a general audience using accessible analogies and no jargon. Same topic — very different diction based on who is reading."),
    ]),
    s("Media literacy",[
      ("What is media literacy and why is it a 21st-century essential skill?","Think: ability to access, analyze, evaluate, and create media","Media literacy: the ability to critically analyze and evaluate the messages we encounter in all forms of media. Essential because media shapes opinions and values — uncritical consumption leaves us vulnerable to manipulation."),
      ("What is confirmation bias and how does it affect how we consume news?","Think: we tend to seek information that confirms existing beliefs","We tend to accept information that confirms what we already believe and reject contradicting information. News feed algorithms amplify this by showing us more of what we already engage with — creating echo chambers."),
      ("What is the difference between a news article, an editorial, and a feature story?","Think: purpose and subjectivity differ","News article: objective reporting of facts, minimal opinion. Editorial: explicitly argues a position and is labeled opinion. Feature story: in-depth narrative journalism on a topic, more stylistic than basic news."),
      ("How can you tell if an image has been manipulated or taken out of context?","Think: reverse image search and context clues","Use reverse image search, look for visual inconsistencies, check source credibility, and verify with other sources. Images are frequently taken out of context to support misleading narratives."),
    ]),
    s("Analyzing visual media",[
      ("How do you read an advertisement?","Think: identify the target audience, message, and techniques","Ask: Who is the audience? What is being sold? What message is conveyed? What techniques are used (celebrity endorsement, emotional appeal, humor)? What is NOT shown?"),
      ("What are common persuasion techniques in advertising?","Think: emotional appeals, authority, social proof","Bandwagon (everyone does it), Authority (experts recommend), Testimonial (celebrity endorses), Fear (buy this or bad thing happens), Repetition, Scarcity (limited time offer)."),
      ("How does camera angle affect meaning in a film or photograph?","Think: perspective creates power relationships","Low angle (camera looks up): subject appears powerful. High angle (camera looks down): subject appears small and vulnerable. Eye level: neutral and equal. Directors use these deliberately."),
      ("What does it mean to consider whose perspective is centered in media?","Think: whose stories are told and whose are missing","Media historically represented the world from particular perspectives while excluding others. Recognizing whose viewpoint is centered helps develop more critical media consumption and awareness of representation."),
    ]),
    s("Spelling and conventions",[
      ("What are the most commonly confused word pairs? Give three examples.","Think: homophones and near-homophones","Their, there, they're; affect, effect; its, it's; your, you're; to, too, two; accept, except; then, than. Proofreading specifically for these prevents common errors."),
      ("What is the difference between affect and effect?","Think: verb vs. noun (usually)","Affect: usually a verb (The rain affected our plans). Effect: usually a noun (The effect was significant). Memory trick: RAVEN — Remember Affect Verb Effect Noun."),
      ("What is the difference between it's and its?","Think: contraction vs. possessive","It's = it is or it has (contraction). Its = belonging to it (possessive pronoun — no apostrophe). Possessive pronouns never use apostrophes (his, her, its, theirs, yours)."),
      ("When do you use a semicolon vs. a colon?","Think: joining vs. introducing","Semicolon: joins two independent clauses that are closely related (She studied; she passed). Colon: introduces a list, explanation, or quotation after an independent clause (She needed three things: pen, paper, patience)."),
    ]),
  ],
]
print("G7 ELA complete")

P[7]["history"] = [
  # U1: Medieval World
  [
    s("Feudalism",[
      ("What was feudalism and what problem did it solve?","Think: decentralized system for order in unstable times","Feudalism: a hierarchical social and political system in medieval Europe. It solved the problem of weak central authority and raids by organizing protection and land management locally."),
      ("What was the feudal hierarchy from top to bottom?","Think: monarch, nobles, knights, serfs","King or Queen, Lords and Nobles (received fiefs, owed military service), Knights (owed military service, received land), Serfs and Peasants (farmed the land, owed labor and produce)."),
      ("What were the mutual obligations in the lord-vassal relationship?","Think: exchange of land for service and loyalty","Lord provided: land (fief), protection, and justice. Vassal (knight) provided: military service (usually 40 days per year), loyalty, and counsel."),
      ("How did feudalism limit the power of kings?","Think: power was distributed, not centralized","Kings needed nobles' military forces and could not rule without their support. Nobles had their own territories and armies. Magna Carta (1215) explicitly limited royal power."),
    ]),
    s("The role of the Church",[
      ("Why was the Catholic Church so powerful in medieval Europe?","Think: spiritual, political, and economic power","The Church controlled salvation (excommunication was a powerful threat), education, land (owned about 30% of European land), political appointments, and canon law. Religion permeated every aspect of life."),
      ("What were the Crusades? What were two long-term effects?","Think: military campaigns to control the Holy Land","The Crusades (1095–1291): military expeditions to recapture Jerusalem. Long-term effects: (1) Increased trade as Europeans wanted Eastern goods. (2) Cultural exchange as Islamic math, science, and philosophy entered Europe."),
      ("What was the Great Schism of 1054?","Think: split of Christianity into two branches","The split of Christianity into Roman Catholic (west) and Eastern Orthodox (east). Divided over the Pope's authority, use of icons, and theological disagreements. Still separated today."),
      ("What role did monasteries play in medieval society?","Think: preservation of knowledge and social services","Monasteries were centers of learning (preserved Greek and Roman texts), healthcare (many ran hospitals), agricultural innovation, and hospitality. Monks copied manuscripts, preserving Classical knowledge."),
    ]),
    s("Islamic Golden Age",[
      ("What was the Islamic Golden Age and when did it occur?","Think: 8th to 13th century Islamic civilization's flourishing","Approximately 750 to 1258 CE, centered in Baghdad under the Abbasid Caliphate. Islamic scholars made major advances in mathematics, astronomy, medicine, chemistry, and philosophy."),
      ("Name three specific contributions of Islamic scholars during the Golden Age.","Think: algebra, hospitals, astronomy","(1) Al-Khwarizmi: algebra and algorithms. (2) Ibn Sina (Avicenna): Canon of Medicine, a medical textbook used in Europe for 600 years. (3) Al-Haytham: optics and the scientific method."),
      ("Why did Islamic scholars translate Greek works? What impact did this have?","Think: House of Wisdom in Baghdad","The Abbasid caliphs established the House of Wisdom to translate Greek, Persian, and Indian works. This preserved Classical knowledge. When later translated into Latin, these works helped spark the European Renaissance."),
      ("How did Islamic trade networks spread knowledge and culture?","Think: Silk Road and Indian Ocean trade routes","Islamic merchants controlled major trade routes connecting Europe, Africa, and Asia. Mathematical concepts, technologies, crops, and philosophies spread along these routes."),
    ]),
    s("Black Death",[
      ("What was the Black Death and what caused it?","Think: bubonic plague — bacterium Yersinia pestis","The Black Death (1347–1351): a catastrophic pandemic caused by the bacterium Yersinia pestis, spread primarily by fleas on rats. Killed 30–60% of Europe's population — 25–50 million people."),
      ("What were the social effects of the Black Death?","Think: labor shortage leads to social upheaval and change","Massive labor shortage gave surviving peasants increased bargaining power and wages rose. Church authority was questioned. Social upheaval and scapegoating of Jews followed."),
      ("Why did the Black Death spread so rapidly through medieval cities?","Think: sanitation, density, trade routes","Medieval cities had poor sanitation, high population density, no understanding of disease transmission, and no public health infrastructure. Trade routes spread the disease along with commerce."),
      ("How did the Black Death contribute to the end of the feudal system?","Think: labor shortage changed power dynamics","With 30–60% of the population dead, lords could not find enough workers. Surviving serfs demanded wages and better conditions. Some fled to cities. Feudalism declined over the following century."),
    ]),
    s("The Renaissance",[
      ("What does Renaissance mean and what ideas characterized it?","Think: rebirth of Classical learning and focus on humanity","Renaissance means rebirth in French (14th to 17th centuries, began in Italy). Characterized by humanism (focus on human potential), revival of Greek and Roman arts and learning, individualism, and realistic art."),
      ("What is humanism and how did it differ from the medieval worldview?","Think: earthly human life matters, not just afterlife","Medieval worldview: focused on God, afterlife, and spiritual matters. Humanist worldview: human achievement, dignity, and earthly life have value. Study of classical texts including history, poetry, grammar, rhetoric, and ethics."),
      ("Name three major Renaissance artists or thinkers and their contributions.","Think: Leonardo, Michelangelo, Gutenberg","Leonardo da Vinci: Mona Lisa, The Last Supper, anatomy notebooks. Michelangelo: Sistine Chapel ceiling, David. Gutenberg: printing press around 1440, which transformed the spread of information."),
      ("Why did the Renaissance begin in Italian city-states?","Think: wealthy merchant class, classical ruins, and trade","Italian city-states had wealthy merchant families (Medici) who funded artists, access to Greek texts, Classical ruins inspiring artists, and thriving trade that introduced diverse ideas."),
    ]),
  ],
  # U2: Age of Exploration
  [
    s("Causes of exploration",[
      ("What were the main motivations for European exploration in the 15th and 16th centuries?","Think: God, Glory, Gold and trade routes","(1) Economic: find new trade routes to Asia. (2) Religious: spread Christianity. (3) Political: national prestige. (4) Technological: improved maps, compass, astrolabe, and caravel ship design."),
      ("Why were Europeans seeking new trade routes to Asia in the 1400s?","Think: fall of Constantinople (1453) disrupted land routes","The Ottoman Empire captured Constantinople in 1453, blocking or taxing overland Silk Road trade. European merchants needed sea routes to Asian spices and goods directly."),
      ("What technological innovations made long-distance sea exploration possible?","Think: navigation and ship design","(1) Caravel: maneuverable ship that could sail into the wind. (2) Magnetic compass: determined direction. (3) Astrolabe: determined latitude. (4) Improved maps (portolan charts)."),
      ("How did Prince Henry the Navigator contribute to exploration?","Think: establishing a Portuguese school of exploration","Henry (1394–1460) established a school of navigation, funded expeditions along the African coast, and collected geographic knowledge. His work laid the foundation for Vasco da Gama's route to India (1498)."),
    ]),
    s("Columbian Exchange",[
      ("What was the Columbian Exchange?","Think: transfer of organisms between Old and New Worlds","The massive transfer of plants, animals, diseases, ideas, and people between the Americas and Afro-Eurasia following Columbus's 1492 voyage. Permanently transformed diets, ecosystems, and populations on both sides of the Atlantic."),
      ("Name three crops that went from the Americas to Europe and explain their impact.","Think: tomato, potato, corn or maize","Potato: became a staple in Europe, supporting population growth. Maize (corn): spread to Africa, Asia, and Europe. Tomato: transformed Italian and Mediterranean cuisine. These crops dramatically changed Old World diets."),
      ("Why did European diseases devastate Indigenous American populations?","Think: no prior exposure means no immunity","European colonizers brought smallpox, measles, and other diseases. Indigenous Americans had no immunity. Epidemics killed an estimated 50–90% of the Indigenous population — the greatest demographic catastrophe in human history."),
      ("What did Europe send to the Americas that harmed Indigenous populations?","Think: diseases, colonists, and later enslaved Africans","Disease (catastrophic population collapse), colonial settlers who took land, and later the forced transportation of enslaved Africans. The Columbian Exchange was deeply unequal in its harms and benefits."),
    ]),
    s("Colonization effects",[
      ("What was the encomienda system?","Think: Spanish labor system for Indigenous people","A Spanish colonial institution granting colonizers the labor and tribute of a group of Indigenous people. In practice it was forced labor under brutal conditions and contributed massively to Indigenous population collapse."),
      ("What was the transatlantic slave trade?","Think: forced migration of Africans to the Americas","European colonizers forcibly transported approximately 12.5 million Africans to the Americas between 1500 and 1900. Enslaved Africans were forced to work on sugar, tobacco, and cotton plantations."),
      ("How did colonization affect the political structures of Indigenous societies?","Think: displacement, destruction, forced assimilation","European colonization dismantled existing Indigenous political structures, destroyed cities, installed colonial governments, used divide-and-conquer tactics, and later imposed forced assimilation."),
      ("What were the long-term economic effects of colonization on colonized regions?","Think: extraction economy leads to underdevelopment","Colonies were organized to extract resources for European benefit. Local manufacturing was discouraged. This created economic dependency that persisted after independence, contributing to today's global economic inequalities."),
    ]),
  ],
  # U3: Early Modern World
  [
    s("Scientific Revolution",[
      ("What was the Scientific Revolution and when did it occur?","Think: 16th to 17th century shift in understanding nature","Approximately 1543 to 1687. A fundamental change in how European thinkers understood nature — from accepting ancient authorities to testing ideas through observation and experiment. Laid the foundation for modern science."),
      ("What was the heliocentric theory and why was it controversial?","Think: Sun at center contradicted Church teaching","Heliocentrism: the Earth and planets orbit the Sun (Copernicus, 1543). Contradicted the geocentric model supported by Aristotle and the Church. Galileo's telescopic evidence confirmed Copernicus and he was tried by the Inquisition for heresy."),
      ("What is the scientific method and who helped develop it?","Think: hypothesis, experiment, observation, conclusion","A systematic approach: (1) Question, (2) Hypothesis, (3) Experiment, (4) Observe and collect data, (5) Conclusion, (6) Peer review. Francis Bacon (empiricism) and Rene Descartes (reason and skepticism) helped formalize it."),
      ("Name two scientists of the Scientific Revolution and their contributions.","Think: Galileo, Newton, Kepler, Harvey","Galileo: telescopic observations confirmed heliocentrism and studied motion. Isaac Newton: Laws of Motion and Universal Gravitation — connected terrestrial and celestial mechanics and invented calculus."),
    ]),
    s("Enlightenment",[
      ("What was the Enlightenment? What were its core beliefs?","Think: reason, individual rights, progress, questioning authority","The Enlightenment (18th century): an intellectual movement emphasizing reason, individual rights, separation of church and state, and the ability of humans to improve society through rational thought."),
      ("Name three Enlightenment thinkers and their key ideas.","Think: Locke, Rousseau, Montesquieu, Voltaire","John Locke: natural rights (life, liberty, property) and government by consent. Montesquieu: separation of powers. Rousseau: social contract and popular sovereignty. Voltaire: religious tolerance and freedom of speech."),
      ("How did Enlightenment ideas influence the American and French Revolutions?","Think: natural rights, consent of the governed, popular sovereignty","American Declaration of Independence drew directly on Locke. U.S. Constitution used Montesquieu's separation of powers. French Revolution drew on Rousseau's social contract. Enlightenment gave revolutionaries their philosophical foundation."),
      ("What is the social contract theory?","Think: government legitimacy comes from citizens' consent","Government's authority comes from an agreement with the citizens. If the government violates the social contract, citizens have the right to overthrow it. Foundation of modern democratic theory."),
    ]),
    s("Revolutions",[
      ("What were the key causes of the American Revolution?","Think: taxation without representation and Enlightenment ideals","(1) No representation in British Parliament despite being taxed. (2) Enlightenment beliefs in natural rights. (3) British economic restrictions. (4) Growing colonial identity separate from Britain. (5) Precipitants: Boston Massacre, Boston Tea Party, Intolerable Acts."),
      ("What were the key causes of the French Revolution?","Think: inequality, financial crisis, Enlightenment","(1) Extreme economic inequality: Third Estate bore all taxes. (2) France's bankruptcy. (3) Enlightenment ideas about rights and government. (4) Food shortages. (5) Weak King Louis XVI."),
      ("What was the Declaration of Independence's philosophical foundation?","Think: Locke's natural rights theory applied","Drew on Locke: all men created equal, endowed with unalienable rights (life, liberty, pursuit of happiness). When government violates these rights, the people have the right to alter or abolish it."),
      ("How were the American and French Revolutions similar and different?","Think: shared causes, very different outcomes","Similar: both inspired by Enlightenment, fought for rights, overthrew existing political order. Different: American Revolution produced stable constitutional democracy. French Revolution was far more violent, cycled through governments, and ended in Napoleon's dictatorship."),
    ]),
  ],
]
print("G7 history complete")

P[7]["cs"] = [
  [
    s("Data types and variables",[
      ("What are the four basic data types in most programming languages?","Think: integer, float, string, boolean","Integer: whole numbers (5, -3). Float: decimal numbers (3.14). String: text (Hello). Boolean: True or False. Each type determines what operations are possible."),
      ("What is a variable? Why do we use them?","Think: named storage location that can change","A variable is a named container for storing data that can change during program execution. Variables allow programs to work with different data without rewriting the code."),
      ("What is the difference between declaring and assigning a variable?","Think: creating vs. giving it a value","Declaration: tells the program the variable exists. Assignment: gives it a value (x = 5). In Python, declaration and assignment happen simultaneously."),
      ("What happens if you try to add a string and an integer in Python?","Think: type error","TypeError — Python cannot add different types without conversion. Convert first: int('5') + 3 = 8, or str(3) + '5' = '35'."),
    ]),
    s("Functions",[
      ("What is a function and why do we write them?","Think: reusable block of code with a name","A function is a named, reusable block of code that performs a specific task. Functions avoid repetition (DRY — Do not Repeat Yourself), make code readable and organized, and allow reuse with different inputs."),
      ("What is the difference between a parameter and an argument?","Think: placeholder vs. actual value","Parameter: variable in the function definition that accepts input (def greet(name):). Argument: actual value passed when calling the function (greet('Alice')). name is the parameter; Alice is the argument."),
      ("What is a return value? Write a function that returns the sum of two numbers.","Think: output of a function","def add(a, b): return a + b. The return statement sends a value back to the caller. Without return, the function performs an action but sends nothing back."),
      ("What is the difference between a function that returns a value and one that just prints?","Think: output vs. side effect","A function that returns a value can be used in expressions: result = add(3,4). A function that only prints produces visible output but the result cannot be stored or used further."),
    ]),
    s("Lists and loops",[
      ("What is a list in Python? Give an example.","Think: ordered collection of items","A list is an ordered, mutable collection of items: fruits = ['apple', 'banana', 'cherry']. Items are accessed by index (fruits[0] = 'apple')."),
      ("Write a for loop that prints every item in a list.","Think: iterate over each element","for item in fruits: print(item) — iterates over each element in fruits, assigning it to item one at a time."),
      ("What is a while loop? When should you use it instead of a for loop?","Think: repeat while condition is true","while condition: [code]. Use a while loop when you do not know how many iterations are needed in advance. Use a for loop when iterating over a known sequence."),
      ("What is an index? What happens if you use an out-of-range index?","Think: position in a list, starting from 0","Index: the position of an item, starting at 0. Negative indices count from the end (fruits[-1] = last item). An out-of-range index causes IndexError."),
    ]),
    s("Conditionals and logic",[
      ("What are the comparison operators in Python?","Think: ==, !=, <, >, <=, >=","== (equal), != (not equal), < (less than), > (greater than), <= (less than or equal), >= (greater than or equal). Note: == tests equality while = assigns a value — a very common error."),
      ("What are the logical operators and how do they work?","Think: and, or, not","and: True only if BOTH conditions are True. or: True if AT LEAST ONE condition is True. not: reverses the boolean value. Example: if age >= 13 and age <= 17: (teenager check)."),
      ("Write an if/elif/else statement for a grade system.","Think: multiple conditions","if score >= 90: grade = 'A' elif score >= 80: grade = 'B' elif score >= 70: grade = 'C' else: grade = 'F'. elif means else if and allows multiple conditions to be checked in order."),
      ("What is a nested conditional? When should you use one?","Think: if inside an if","A conditional inside another conditional. Use when one condition is only relevant if another is already true. Avoid deep nesting — consider using and or refactoring into functions."),
    ]),
    s("Input and output",[
      ("How do you get user input in Python?","Think: input() function","name = input('Enter your name: '). The input() function always returns a string — convert for numeric input: age = int(input('Enter your age: '))."),
      ("What is the difference between print() and return in a function?","Think: display vs. send back","print(): outputs text to the screen — a side effect, not stored. return: sends a value back to the caller — can be stored in a variable or used in expressions."),
      ("Write a complete program that asks a user's name and age, then prints a greeting.","Think: input, process, output","name = input('What is your name? ') / age = int(input('How old are you? ')) / print('Hello', name + '! You are', age, 'years old.')"),
      ("What is string formatting? Show two ways to format a string in Python.","Think: f-string and .format()","f-string: f'Hello, {name}!' (cleaner, modern). .format(): 'Hello, {}!'.format(name). f-strings are preferred in modern Python for their readability."),
    ]),
  ],
  [
    s("Web design basics",[
      ("What is the difference between HTML, CSS, and JavaScript?","Think: structure, style, behavior","HTML: defines structure and content. CSS: controls visual presentation. JavaScript: adds interactivity and behavior. Together they build every website."),
      ("What is an HTML tag? Give two examples.","Think: markup that defines an element","HTML tags define elements: p defines a paragraph, h1 is a heading. Tags come in pairs (opening and closing): paragraph Text here end-paragraph. Some are self-closing."),
      ("What is a CSS selector? Write a rule that makes all paragraphs blue.","Think: selector targets elements","p { color: blue; } — the selector p targets all paragraph elements. Selectors can target elements, classes (.className), or IDs (#idName)."),
      ("What is responsive design?","Think: adapts to different screen sizes","Responsive design uses CSS techniques (flexible grids, media queries) to make websites look good on screens of all sizes. Essential because more than 50% of web traffic comes from mobile devices."),
    ]),
    s("Problem solving and decomposition",[
      ("What is computational thinking?","Think: four pillars of CS problem-solving","Decomposition: break large problems into smaller parts. Pattern recognition: identify recurring patterns. Abstraction: focus on essential information. Algorithm design: create step-by-step solutions. Together these make complex problems solvable."),
      ("What is abstraction in computer science?","Think: hiding complexity behind a simpler interface","Hiding implementation details and exposing only what is necessary. You use functions without knowing exactly how they work internally. Abstraction manages complexity."),
      ("What is decomposition? Apply it to building a calculator app.","Think: break the big problem into smaller problems","(1) Get user input. (2) Parse the operation. (3) Perform the calculation. (4) Display the result. (5) Handle errors. Each part can be designed and tested independently."),
      ("What is pseudocode and why is it useful?","Think: English-like description of an algorithm before coding","Pseudocode: describing an algorithm in plain language, structured but not in any programming language. Useful for planning logic before worrying about syntax and communicating algorithms to non-programmers."),
    ]),
    s("Binary and data",[
      ("What is binary and why do computers use it?","Think: base-2 number system; transistors are on or off","Binary: number system with only 0 and 1. Computers use it because electronic circuits naturally have two states: on (1) and off (0). Every number, letter, image, and sound is stored as binary digits (bits)."),
      ("How do you convert a small binary number to decimal?","Think: positional value — powers of 2","Each position represents a power of 2, from right to left: 1, 2, 4, 8, 16. Binary 1011 = 1x8 + 0x4 + 1x2 + 1x1 = 8+0+2+1 = 11."),
      ("What is a bit? What is a byte? How many bytes are in a kilobyte?","Think: single binary digit, 8 bits, 1024 bytes","Bit: single binary digit (0 or 1). Byte: 8 bits. Kilobyte (KB) = 1,024 bytes. Megabyte (MB) = 1,024 KB. Gigabyte (GB) = 1,024 MB."),
      ("What is ASCII and what problem does it solve?","Think: standard encoding of characters as numbers","ASCII assigns a unique number to each character (A=65, a=97, space=32). Solves how computers (which only store numbers) represent text. Modern standard is Unicode, which covers all world languages."),
    ]),
    s("Cybersecurity",[
      ("What is encryption and why is it important?","Think: converting data into unreadable form without a key","Encryption: transforming readable data into unreadable code. Only someone with the correct key can decrypt it. Essential for protecting passwords, financial transactions (HTTPS), and private messages."),
      ("What is HTTPS and what does it indicate?","Think: secure, encrypted web connection","HTTPS (HyperText Transfer Protocol Secure): the secure version of HTTP. The S means the connection is encrypted. Look for the padlock icon — especially important when entering passwords or payment information."),
      ("What is social engineering in cybersecurity?","Think: manipulating people rather than hacking systems","Attacking the human element rather than technical systems. Types: phishing (fake emails), pretexting (inventing a scenario), baiting. The most effective attacks often target human psychology rather than software."),
      ("What are three principles of good password security?","Think: length, complexity, uniqueness","(1) Long (12+ characters). (2) Complex (uppercase, lowercase, numbers, symbols). (3) Unique for each account. (4) Not based on personal info. Use a password manager and enable two-factor authentication."),
    ]),
    s("Careers in technology",[
      ("What is the difference between a software engineer and a data scientist?","Think: building systems vs. analyzing data","Software engineer: designs, builds, and maintains software systems. Data scientist: analyzes large datasets to find patterns and insights using statistics and machine learning. Both require coding but focus on different problems."),
      ("What is UX and UI design?","Think: user experience and user interface","UX (User Experience): the overall experience of using a product — is it easy and intuitive? UI (User Interface): the visual design of the screens. A product can have beautiful UI but terrible UX. Good design requires both."),
      ("What skills are most important for a career in technology?","Think: technical and soft skills","Technical: coding, problem-solving, data analysis. Soft: communication (explaining technical concepts to non-technical people), teamwork, creativity, adaptability, and persistence through debugging."),
      ("What are some ways to explore technology careers as a middle schooler?","Think: accessible pathways to tech experience","Code.org, Scratch, robotics clubs, app design, game development, hackathons, and interviewing people in tech jobs. The best way to explore is by building things that interest you."),
    ]),
  ],
]
print("G7 CS complete")

P[7]["health"] = [
  [
    s("Mental health awareness",[
      ("What is mental health and why does it matter as much as physical health?","Think: WHO definition and functional impact","Mental health: emotional, psychological, and social well-being. It affects how we think, feel, and act, how we handle stress, and how we relate to others. Mental health problems are the leading cause of disability worldwide."),
      ("What is the difference between a mental health disorder and just feeling sad or anxious?","Think: severity, duration, and functional impairment","Normal emotions: temporary responses that do not significantly impair daily function. Mental health disorder: persistent, severe symptoms that significantly impair school, relationships, or daily life and typically require professional support."),
      ("Name three common mental health conditions and one key symptom of each.","Think: depression, anxiety, ADHD","Depression: persistent sadness and loss of interest for 2 or more weeks. Anxiety disorder: excessive, uncontrollable worry. ADHD: difficulty sustaining attention, impulsivity, and hyperactivity. All are treatable."),
      ("What is stigma in mental health and why is it harmful?","Think: negative attitudes that prevent people from getting help","Mental health stigma: negative stereotypes toward people with mental health conditions. Harmful because it prevents people from seeking help, causes shame and isolation, and perpetuates inaccurate beliefs."),
    ]),
    s("Social and emotional learning",[
      ("What are the five core SEL competencies?","Think: self-awareness, self-management, social awareness, relationship skills, responsible decision-making","Self-awareness: knowing your emotions and strengths. Self-management: regulating emotions and behaviors. Social awareness: understanding others' perspectives. Relationship skills: building healthy connections. Responsible decision-making: ethical choices."),
      ("What is self-regulation and how do you practice it?","Think: managing emotions and behaviors in difficult situations","Self-regulation: the ability to manage your emotions, thoughts, and behaviors effectively. Practice: identify the emotion before reacting (pause), use calming strategies (breath, count to 10), think about consequences before acting."),
      ("What is empathy and how is it different from sympathy?","Think: feeling with vs. feeling for","Sympathy: feeling sorry FOR someone from the outside. Empathy: understanding and sharing someone's feelings — seeing the world from their perspective. Empathy requires connecting to the feeling rather than just acknowledging the situation."),
      ("How do social relationships affect mental health?","Think: humans are social — connection is essential","Strong, positive relationships are among the strongest predictors of mental health. Social isolation is as harmful as smoking 15 cigarettes a day according to research. Healthy relationships provide support, belonging, and purpose."),
    ]),
    s("Substance prevention",[
      ("What are the short-term and long-term effects of alcohol on the adolescent brain?","Think: adolescent brains are more vulnerable","Short-term: impaired judgment, slowed reaction time, memory impairment. Long-term for adolescents: the developing brain is more vulnerable to permanent damage — impaired memory, learning, impulse control, and higher addiction risk."),
      ("What is a gateway drug? Is this concept supported by science?","Think: the gateway hypothesis is contested","Gateway drug theory: using one substance leads to using harder drugs. Science: most people who try alcohol or marijuana do not go on to use harder drugs. However, early substance use is associated with higher risk."),
      ("What are three internal and three external factors that influence substance use decisions?","Think: personal traits and social environment","Internal: self-esteem, stress level, mental health, coping skills, values. External: peer pressure, family attitudes, media portrayal, availability, and community norms."),
      ("What are three effective ways to refuse substances when offered?","Think: specific, assertive refusal strategies","(1) Direct refusal: No thanks. (2) Give a reason: I do not drink. (3) Suggest an alternative: Want to go shoot hoops? (4) Leave the situation. Practicing refusal skills out loud makes them easier in real situations."),
    ]),
    s("Healthy relationships",[
      ("What are the characteristics of a healthy vs. unhealthy relationship?","Think: respect, communication, boundaries vs. control, fear","Healthy: mutual respect, honest communication, trust, and supporting each other's goals. Unhealthy: control, jealousy, manipulation, pressure, disrespect, and isolation from friends or family."),
      ("What is a boundary in a relationship? How do you set one?","Think: limits that define what you are comfortable with","Boundaries: personal limits — what you are and are not comfortable with. Setting: (1) Know your limits. (2) Communicate clearly: I am not comfortable with... (3) Be consistent. Others must respect your boundaries."),
      ("What is peer pressure and what types exist?","Think: spoken and unspoken pressure from peers","Direct: explicit request or demand. Indirect: seeing others do something and feeling compelled to join. Internal: pressure you put on yourself to fit in. The most powerful peer pressure is often unspoken."),
      ("What makes online friendships similar to and different from in-person friendships?","Think: connection is real; context is different","Similar: genuine emotional connection, support, shared interests. Different: harder to read tone, easier to misrepresent yourself, public posts can damage reputation, harder to resolve conflicts."),
    ]),
    s("Personal safety",[
      ("What is the difference between a safe and unsafe touch? What should you do about unsafe touch?","Think: consent and comfort","Safe touch: both people are comfortable and it is consensual. Unsafe touch: makes you uncomfortable, violates your privacy, or is against your wishes. If it happens: say No if you can, leave, and tell a trusted adult."),
      ("What is consent and why is it important in all relationships?","Think: agreement freely given, reversible, informed","Consent: a clear, freely given, informed agreement to an action. Important in all relationships. Can be withdrawn at any time. Without consent it is a violation of the other person's rights."),
      ("What should you do if you feel unsafe at school or in your community?","Think: tell, act, seek help","Tell a trusted adult immediately (teacher, counselor, parent). If in immediate danger: find a safe place and call 911. Anonymous tip lines allow reporting without identification."),
      ("What is conflict resolution and what are three strategies?","Think: de-escalating and solving disputes non-violently","(1) Use I statements (I feel hurt when...). (2) Active listening — really hear the other person's perspective. (3) Focus on the problem, not the person. (4) Find compromise. (5) Involve a mediator if needed."),
    ]),
  ],
  [
    s("Puberty and reproduction",[
      ("What hormones drive puberty? What do they do?","Think: estrogen/progesterone and testosterone","Testosterone: drives puberty in males (muscle growth, voice deepening, facial hair). Estrogen and progesterone: drive puberty in females (breast development, menstruation, hip widening). Both sexes produce both hormones at different levels."),
      ("What is the reproductive system's function?","Think: producing offspring and hormones","The reproductive system produces sex cells (sperm and eggs), provides for fertilization, and creates the hormones that regulate sexual development. It is not fully mature until puberty is complete."),
      ("What is the menstrual cycle and how long does it typically last?","Think: monthly preparation for possible pregnancy","Average cycle: 28 days (range: 21–35 days). Phases: menstruation (lining sheds), follicular phase (egg develops), ovulation (egg released), luteal phase (prepares for possible fertilization)."),
      ("What is important to know about the emotional side of puberty?","Think: identity development, emotional intensity, peer relationships","Puberty brings increased emotional intensity, identity exploration, greater peer influence, and self-consciousness. These are normal but can feel overwhelming. Talking to trusted adults and building emotional skills helps navigate this period."),
    ]),
    s("Nutrition and fitness",[
      ("What are the macronutrients and why does each matter?","Think: carbohydrates, proteins, fats","Carbohydrates: primary energy source (whole grains, fruits, vegetables preferred). Proteins: build and repair muscle and tissue. Fats: brain function, hormone production, fat-soluble vitamins. All three are essential."),
      ("What is the difference between aerobic and anaerobic exercise?","Think: sustained vs. short intense bursts","Aerobic (with oxygen): sustained moderate activity using fat and glucose (running, swimming, cycling). Anaerobic (without oxygen): short, high-intensity bursts (sprinting, weight lifting) using ATP and glucose quickly."),
      ("What does the body need before and after intense exercise?","Think: fuel in, recovery out","Before: complex carbohydrates 1 to 3 hours before and hydration. After: protein (muscle repair), carbohydrates (replenish glycogen), and fluids and electrolytes to replace sweat losses."),
      ("How does sleep affect athletic performance and physical health?","Think: growth hormone released during sleep; recovery happens at night","During deep sleep: growth hormone releases (muscle repair and growth) and the immune system strengthens. Sleep deprivation impairs reaction time, judgment, mood, and physical recovery."),
    ]),
    s("First aid basics",[
      ("What are the steps for responding to an emergency?","Think: CHECK, CALL, CARE","(1) CHECK: survey the scene for safety. (2) CALL: call 911 or have someone else call. (3) CARE: provide appropriate first aid while waiting for help. Never put yourself in danger when trying to help."),
      ("How do you treat a minor cut or scrape?","Think: clean, protect, monitor","(1) Wash hands. (2) Apply gentle pressure to stop bleeding. (3) Clean with running water. (4) Apply antibiotic ointment. (5) Cover with a sterile bandage. Change daily and see a doctor if signs of infection appear."),
      ("What is the recovery position and when is it used?","Think: unconscious but breathing person","Recovery position: placing an unconscious but breathing person on their side to keep the airway clear and prevent choking if they vomit. Used when someone is unconscious but breathing and has no suspected spinal injury."),
      ("What should you do if someone is choking?","Think: Heimlich maneuver if they cannot cough","If they can cough or speak: encourage coughing. If they cannot breathe: call 911, then give 5 back blows between shoulder blades, then 5 abdominal thrusts. Repeat until object is dislodged or help arrives."),
    ]),
    s("Chronic disease prevention",[
      ("What are the most common chronic diseases in the U.S. and what do they have in common?","Think: heart disease, diabetes, cancer — lifestyle-related","Heart disease, type 2 diabetes, obesity, and certain cancers are leading causes of death — and all are significantly influenced by lifestyle factors. Many chronic diseases are largely preventable."),
      ("What lifestyle choices significantly reduce risk of chronic disease?","Think: big four lifestyle factors","(1) Regular physical activity. (2) Healthy diet (fruits, vegetables, whole grains, limiting processed foods). (3) Not smoking. (4) Limiting alcohol. Getting enough sleep and managing stress also reduce risk."),
      ("What is type 2 diabetes and how is it related to lifestyle?","Think: insulin resistance linked to obesity and inactivity","Type 2 diabetes: the body does not use insulin effectively, causing high blood sugar. Strongly linked to obesity, physical inactivity, and poor diet. Unlike Type 1 (autoimmune), Type 2 can often be prevented or managed with lifestyle changes."),
      ("What is cardiovascular disease and what habits protect heart health?","Think: diseases of heart and blood vessels","Cardiovascular disease: umbrella term for heart and blood vessel diseases (heart attack, stroke, hypertension). Protective habits: regular aerobic exercise, low-sodium diet, not smoking, and managing stress."),
    ]),
    s("Environmental health",[
      ("What is environmental health?","Think: how the environment affects human health","Environmental health: the branch of public health focusing on how the natural and built environment affects human health. Includes air quality, water quality, food safety, climate, chemical exposures, and urban design."),
      ("What are the health effects of air pollution?","Think: respiratory and cardiovascular impacts","Air pollution causes respiratory illness (asthma, COPD), cardiovascular disease, lung cancer, and developmental problems in children. Particle pollution (PM2.5) is particularly dangerous — particles small enough to reach deep in the lungs."),
      ("What is clean water access and why is it a global health issue?","Think: water-borne diseases kill millions","Approximately 1 billion people lack access to clean water. Contaminated water causes diarrheal diseases (cholera, typhoid, dysentery) — killing hundreds of thousands of children annually. Clean water access is among the most impactful public health interventions."),
      ("What can you personally do to reduce environmental health risks?","Think: individual and community level action","Individual: reduce chemical use, conserve energy, choose sustainable foods, filter water if needed. Community: advocate for clean air and water policies, support local green spaces, and participate in environmental advocacy."),
    ]),
  ],
]
print("G7 health complete")

# ─── GRADE 8 ───
P[8] = {"math":[], "science":[], "ela":[], "history":[], "cs":[], "health":[]}

P[8]["math"] = [
  # U1: Linear Equations
  [
    s("Slope and rate of change",[
      ("What is slope and how do you calculate it from two points?","Think: rise over run","Slope (m) = (y2 - y1) / (x2 - x1). It measures the steepness and direction of a line. Positive slope: rises left to right. Negative slope: falls left to right."),
      ("Find the slope through (2, 5) and (6, 13).","Think: apply the slope formula","m = (13 - 5) / (6 - 2) = 8 / 4 = 2."),
      ("What does a slope of 0 mean? What does an undefined slope mean?","Think: horizontal vs. vertical lines","Slope = 0: horizontal line (no rise). Undefined slope: vertical line (no run — division by zero). Horizontal lines have equation y = constant; vertical lines have equation x = constant."),
      ("A car travels 150 miles in 3 hours. What is the rate of change (slope)?","Think: slope = change in distance / change in time","150 / 3 = 50 miles per hour. Slope represents the rate of change — here, speed."),
    ]),
    s("Slope-intercept form",[
      ("What is slope-intercept form? Identify slope and y-intercept in y = -3x + 7.","Think: y = mx + b","y = mx + b where m = slope, b = y-intercept. Here: slope = -3, y-intercept = 7 (the line crosses the y-axis at (0,7))."),
      ("Write an equation for a line with slope 4 and y-intercept -2.","Think: substitute into y = mx + b","y = 4x - 2."),
      ("A line passes through (0, 3) and (2, 9). Write the equation.","Think: find slope, then use y = mx + b","m = (9-3)/(2-0) = 3. b = 3. Equation: y = 3x + 3."),
      ("Graph y = 2x - 1. Describe two points on the line.","Think: use y-intercept then slope to find next point","y-intercept: (0, -1). Use slope 2 (rise 2, run 1): (1, 1). Plot these and draw the line."),
    ]),
    s("Solving multi-step equations",[
      ("Solve: 3(x - 4) + 2x = 13","Think: distribute, combine like terms, isolate x","3x - 12 + 2x = 13 → 5x - 12 = 13 → 5x = 25 → x = 5."),
      ("Solve: (2x + 6) / 4 = 5","Think: multiply both sides by 4 first","2x + 6 = 20 → 2x = 14 → x = 7."),
      ("Solve: 5x - 3 = 2x + 12","Think: get variables on one side","3x = 15 → x = 5."),
      ("What does it mean when solving an equation gives 0 = 0? Or 5 = 0?","Think: infinitely many solutions vs. no solution","0 = 0 (always true): infinitely many solutions — the equations are identical. 5 = 0 (never true): no solution — the lines are parallel."),
    ]),
    s("Systems of equations",[
      ("What is a system of equations? What are the three possible outcomes?","Think: two equations, find where they intersect","A system is two or more equations with the same variables. Outcomes: (1) One solution (lines intersect at one point). (2) No solution (parallel lines). (3) Infinitely many solutions (same line)."),
      ("Solve by substitution: y = 2x + 1 and 3x + y = 11","Think: substitute first equation into second","3x + (2x + 1) = 11 → 5x + 1 = 11 → 5x = 10 → x = 2. Then y = 2(2) + 1 = 5. Solution: (2, 5)."),
      ("Solve by elimination: 2x + 3y = 12 and 4x - 3y = 6","Think: add the equations to cancel y","Adding: 6x = 18 → x = 3. Sub back: 2(3) + 3y = 12 → 3y = 6 → y = 2. Solution: (3, 2)."),
      ("Two numbers sum to 20 and differ by 4. Find them.","Think: x + y = 20 and x - y = 4","Add equations: 2x = 24 → x = 12. Then y = 8."),
    ]),
    s("Functions",[
      ("What is a function? How is it different from a relation?","Think: each input has exactly one output","A function: each input (x) maps to exactly one output (y). A relation: any pairing of inputs and outputs (can have one input to multiple outputs). Vertical line test: if a vertical line hits the graph more than once, it is not a function."),
      ("Is this a function? {(1,2), (3,4), (1,5)}","Think: does any x repeat with different y?","Not a function — input 1 maps to both 2 and 5 (two different outputs for the same input)."),
      ("Evaluate f(x) = 2x^2 - 3x + 1 for x = -1.","Think: substitute x = -1","f(-1) = 2(1) - 3(-1) + 1 = 2 + 3 + 1 = 6."),
      ("What is the domain and range of a function?","Think: inputs vs. outputs","Domain: all valid input values (x). Range: all resulting output values (y). Example: f(x) = sqrt(x) has domain x >= 0 (cannot take square root of negative) and range y >= 0."),
    ]),
  ],
  # U2: Geometry
  [
    s("Pythagorean theorem",[
      ("State the Pythagorean theorem and identify what a, b, and c represent.","Think: right triangle relationship","In a right triangle: a^2 + b^2 = c^2. a and b are legs (sides forming the right angle); c is the hypotenuse (longest side, opposite the right angle)."),
      ("Find the hypotenuse if legs are 6 and 8.","Think: 6^2 + 8^2 = c^2","36 + 64 = c^2 → c^2 = 100 → c = 10. (This is a 6-8-10 Pythagorean triple.)"),
      ("A ladder 13 ft long leans against a wall. The base is 5 ft from the wall. How high does it reach?","Think: 5^2 + b^2 = 13^2","25 + b^2 = 169 → b^2 = 144 → b = 12 ft."),
      ("Is a triangle with sides 7, 24, 25 a right triangle?","Think: check if a^2 + b^2 = c^2","7^2 + 24^2 = 49 + 576 = 625 = 25^2. Yes, it is a right triangle."),
    ]),
    s("Transformations",[
      ("Name the four types of rigid transformations.","Think: moves that preserve size and shape","Translation (slide), Reflection (flip), Rotation (turn), and Dilation (scale — changes size, so not rigid). The first three are rigid (congruence preserved)."),
      ("A point at (3, -2) is reflected over the x-axis. What is the new coordinate?","Think: x stays, y changes sign","(3, 2). Reflecting over x-axis: (x, y) → (x, -y)."),
      ("A point at (4, 1) is translated by (-3, 5). What is the new coordinate?","Think: add the translation vector","(4 + (-3), 1 + 5) = (1, 6)."),
      ("What is the difference between congruent and similar figures?","Think: same size vs. same shape","Congruent: same size AND shape (rigid transformations only). Similar: same shape but different size (dilation involved). Congruent figures are always similar; similar figures are not always congruent."),
    ]),
    s("Angle relationships",[
      ("What are complementary and supplementary angles?","Think: add to 90 vs. 180","Complementary: two angles summing to 90 degrees. Supplementary: two angles summing to 180 degrees."),
      ("Two parallel lines are cut by a transversal. Name three angle relationship pairs.","Think: corresponding, alternate interior, co-interior","Corresponding angles: equal. Alternate interior angles: equal (Z-angles). Co-interior (same-side interior) angles: supplementary (add to 180)."),
      ("Find x if two angles are (3x + 10) and (5x - 6) and are vertical angles.","Think: vertical angles are equal","3x + 10 = 5x - 6 → 16 = 2x → x = 8."),
      ("What is the sum of interior angles of a triangle? Of a quadrilateral?","Think: triangle = 180; quadrilateral = 360","Triangle: 180 degrees. Quadrilateral: 360 degrees. General polygon with n sides: (n - 2) × 180 degrees."),
    ]),
    s("Volume of 3D shapes",[
      ("What is the formula for the volume of a cylinder?","Think: V = pi r^2 h","V = pi × r^2 × h. Base area (pi r^2) times height."),
      ("A cylinder has radius 4 cm and height 10 cm. Find its volume (pi ≈ 3.14).","Think: V = pi r^2 h","V = 3.14 × 16 × 10 = 502.4 cm cubed."),
      ("What is the formula for the volume of a cone? How does it relate to a cylinder?","Think: cone = (1/3) cylinder","V = (1/3) pi r^2 h. A cone is exactly one-third the volume of a cylinder with the same base and height."),
      ("A sphere has radius 6 cm. Find its volume (pi ≈ 3.14).","Think: V = (4/3) pi r^3","V = (4/3) × 3.14 × 216 = 904.32 cm cubed."),
    ]),
    s("Exponents and scientific notation",[
      ("What is scientific notation? Convert 0.000047 to scientific notation.","Think: coefficient between 1 and 10, times 10 to a power","Scientific notation: a × 10^n where 1 ≤ a < 10. 0.000047 = 4.7 × 10^-5."),
      ("Convert 6.3 × 10^4 to standard form.","Think: move decimal right for positive exponent","63,000."),
      ("Multiply: (3 × 10^4) × (2 × 10^3)","Think: multiply coefficients, add exponents","(3 × 2) × 10^(4+3) = 6 × 10^7."),
      ("Simplify: x^5 / x^2 and (y^3)^4","Think: subtraction and multiplication of exponents","x^5 / x^2 = x^3. (y^3)^4 = y^12."),
    ]),
  ],
  # U3: Statistics
  [
    s("Scatter plots",[
      ("What is a scatter plot used for?","Think: displaying relationship between two variables","A scatter plot shows the relationship (correlation) between two quantitative variables. Each point represents one data pair. Used to identify trends and patterns."),
      ("What is positive, negative, and no correlation?","Think: direction of the pattern","Positive: as x increases, y increases (upward trend). Negative: as x increases, y decreases (downward trend). No correlation: no clear pattern — points scattered randomly."),
      ("What is a line of best fit (trend line)?","Think: line that best represents the data","A line drawn through a scatter plot that best represents the overall trend. Used to make predictions. About half the points should be above and half below the line."),
      ("A scatter plot shows hours studied vs. test scores. What correlation would you expect?","Think: more study generally means higher scores","Positive correlation — as hours studied increase, test scores tend to increase. Not perfectly linear (other factors affect scores) but a positive trend exists."),
    ]),
    s("Two-way tables",[
      ("What is a two-way table?","Think: organizes data for two categorical variables","A two-way table (contingency table) displays counts or percentages for two categorical variables simultaneously. Rows = one variable; columns = another."),
      ("In a two-way table, what is a marginal frequency?","Think: row totals and column totals","Marginal frequencies are the row totals and column totals — they show the distribution of one variable ignoring the other."),
      ("100 students: 40 play sports (25 boys, 15 girls), 60 do not (20 boys, 40 girls). What percent of girls play sports?","Think: girls who play / total girls","Girls who play: 15. Total girls: 15 + 40 = 55. Percent: 15/55 ≈ 27%."),
      ("What is the difference between joint and marginal frequency in a two-way table?","Think: cell vs. total","Joint frequency: count in a specific cell (intersection of row and column). Marginal frequency: total for a row or column."),
    ]),
    s("Probability models",[
      ("What is the difference between theoretical and experimental probability?","Think: expected vs. observed","Theoretical: calculated based on equally likely outcomes (P(heads) = 1/2). Experimental: based on actual trials (you flipped 48 heads in 100 flips, so P(heads) ≈ 0.48). They should converge with more trials."),
      ("A spinner has 4 equal sections: red, blue, green, yellow. You spin 200 times and get red 62 times. Compare theoretical vs. experimental P(red).","Think: theoretical = 1/4 = 0.25; experimental = 62/200 = 0.31","Theoretical: 0.25 (25%). Experimental: 0.31 (31%). Difference due to chance — more trials would bring them closer."),
      ("What is the Law of Large Numbers?","Think: more trials means closer to theoretical probability","As the number of trials increases, the experimental probability gets closer to the theoretical probability. This is why casinos always win in the long run even if individual players sometimes win."),
      ("What is a simulation? Why are simulations useful in probability?","Think: modeling random events to estimate probability","A simulation uses random processes (dice, coins, random number generators) to model a real-world scenario. Useful when the theoretical probability is hard to calculate or the actual experiment is impractical."),
    ]),
    s("Data analysis",[
      ("What is a bivariate data set?","Think: two variables measured on each subject","Bivariate: two variables measured on each individual. Example: height and weight for each person. Univariate: one variable. Bivariate analysis explores relationships between the two."),
      ("How do outliers affect the mean vs. the median?","Think: mean is sensitive; median is resistant","Outliers pull the mean toward them. The median is resistant — an extreme value at one end changes the mean significantly but barely affects the median. This is why median income is often more informative than mean income."),
      ("What is the difference between causation and correlation?","Think: correlation does not equal causation","Correlation: two variables tend to change together. Causation: one variable directly causes the other to change. Correlation does not prove causation — ice cream sales and drowning rates are correlated (both increase in summer) but one does not cause the other."),
      ("A study finds that students with more books at home get higher test scores. Does this prove books cause higher scores?","Think: confounding variables","No — correlation, not causation. Confounding variable: wealth. Wealthier families have more books AND better educational opportunities (tutors, better schools, less stress). The books themselves may not be the cause."),
    ]),
    s("Sampling methods",[
      ("Name four sampling methods and briefly describe each.","Think: random, stratified, systematic, convenience","Simple random: every member has equal chance. Stratified: divide into subgroups, randomly sample each. Systematic: every nth member. Convenience: whoever is easiest to reach (most biased). Cluster: randomly select whole groups."),
      ("Why is convenience sampling considered the weakest method?","Think: systematic bias in who is selected","Convenience sampling selects whoever is easiest to reach, which almost always produces a non-representative sample. Example: surveying only your friends about school lunch produces results biased toward one social group."),
      ("What is the margin of error and what does it tell you?","Think: range of uncertainty around an estimate","Margin of error: the range above and below a sample estimate within which the true population value likely falls. A poll showing 52% ± 3% means the true value is likely between 49% and 55%."),
      ("A school wants to survey students about the cafeteria. Design a stratified random sample.","Think: divide by grade, then randomly select from each","(1) Divide students into grade levels (strata). (2) Determine what proportion each grade represents. (3) Randomly select that proportion from each grade. This ensures all grades are fairly represented."),
    ]),
  ],
  # U4: Number Theory
  [
    s("Real numbers",[
      ("What are the different sets of numbers in the real number system?","Think: natural, whole, integers, rational, irrational, real","Natural (1,2,3...), Whole (0,1,2...), Integers (...-2,-1,0,1,2...), Rational (fractions and terminating/repeating decimals), Irrational (non-terminating non-repeating like pi and sqrt(2)), Real (all of the above)."),
      ("Is sqrt(16) rational or irrational? Is sqrt(7)?","Think: perfect square vs. non-perfect square","sqrt(16) = 4 (rational — a whole number). sqrt(7) ≈ 2.6457... (irrational — non-terminating, non-repeating decimal)."),
      ("What is a perfect square? List the first 10.","Think: integer times itself","A perfect square is n^2 for integer n: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100."),
      ("Estimate sqrt(50) to the nearest tenth without a calculator.","Think: it falls between sqrt(49) = 7 and sqrt(64) = 8","sqrt(49) = 7, sqrt(50) is just above. 7.0^2 = 49, 7.1^2 = 50.41. So sqrt(50) ≈ 7.1."),
    ]),
    s("Exponents and roots",[
      ("What is the meaning of a negative exponent? Simplify 2^-3.","Think: negative exponent = reciprocal","x^-n = 1/x^n. So 2^-3 = 1/2^3 = 1/8."),
      ("Simplify: (3^2 × 3^4) / 3^3","Think: add exponents when multiplying, subtract when dividing","3^(2+4-3) = 3^3 = 27."),
      ("What is x^0 for any nonzero x? Why?","Think: any nonzero number to the zero power","x^0 = 1 for any x ≠ 0. Reason: x^n / x^n = 1 and using exponent rules = x^(n-n) = x^0, so x^0 must equal 1."),
      ("Simplify: sqrt(72)","Think: factor out perfect square","sqrt(72) = sqrt(36 × 2) = 6 × sqrt(2)."),
    ]),
    s("Patterns and sequences",[
      ("What is an arithmetic sequence? Give an example and find the next term.","Think: constant difference between terms","Arithmetic: each term is found by adding a constant (common difference). Example: 3, 7, 11, 15... (d = 4). Next term: 19."),
      ("What is a geometric sequence? Give an example.","Think: constant ratio between terms","Geometric: each term is found by multiplying by a constant ratio. Example: 2, 6, 18, 54... (r = 3). Next term: 162."),
      ("Write a formula for the nth term of an arithmetic sequence with first term 5 and common difference 3.","Think: a_n = a_1 + (n-1)d","a_n = 5 + (n-1)(3) = 5 + 3n - 3 = 3n + 2."),
      ("A bacteria colony doubles every hour. Starting with 50, how many after 6 hours?","Think: geometric sequence with r = 2","50 × 2^6 = 50 × 64 = 3,200 bacteria."),
    ]),
    s("Financial math",[
      ("What is simple interest? Calculate: $2,000 at 5% for 3 years.","Think: I = P × r × t","I = 2000 × 0.05 × 3 = $300. Total: $2,300."),
      ("What is compound interest and how does it differ from simple interest?","Think: interest on interest","Compound interest: interest is calculated on the principal AND previously earned interest. It grows faster than simple interest. Formula: A = P(1 + r/n)^(nt)."),
      ("What is a budget? What are fixed vs. variable expenses?","Think: income vs. planned spending","Budget: plan for how to allocate money. Fixed expenses: same every month (rent, loan payment). Variable expenses: change month to month (groceries, gas, entertainment). Budgeting means spending less than you earn."),
      ("What is the difference between gross pay and net pay?","Think: before vs. after deductions","Gross pay: total earnings before deductions. Net pay (take-home pay): gross pay minus taxes and other deductions (health insurance, retirement contributions). Net pay is what you actually receive."),
    ]),
    s("Proportional reasoning",[
      ("What is a unit rate and how is it used in real life?","Think: rate per one unit","Unit rate: how much per one unit. Examples: miles per gallon (fuel efficiency), price per ounce (unit price), calories per serving. Unit rates allow comparison between different-sized options."),
      ("If 8 pounds of fertilizer covers 400 square feet, how much is needed for 1,250 square feet?","Think: set up a proportion","8/400 = x/1250 → x = (8 × 1250)/400 = 25 pounds."),
      ("What is a percent proportion? Solve: what percent is 18 of 72?","Think: part/whole = percent/100","18/72 = x/100 → x = 25. So 18 is 25% of 72."),
      ("A map has scale 2 cm = 15 km. Two cities are 7 cm apart. What is the actual distance?","Think: unit rate then multiply","Unit rate: 15/2 = 7.5 km per cm. Distance: 7 × 7.5 = 52.5 km."),
    ]),
  ],
  # U5: Intro to Algebra II concepts
  [
    s("Quadratic intro",[
      ("What is a quadratic function? What is its graph called?","Think: y = ax^2 + bx + c; parabola","A quadratic function has the form y = ax^2 + bx + c (highest power is 2). Its graph is a parabola — a symmetric U-shape. Opens up if a > 0; opens down if a < 0."),
      ("What is the vertex of a parabola?","Think: the highest or lowest point","The vertex is the turning point — the minimum (if a > 0) or maximum (if a < 0) of the parabola. The axis of symmetry passes through the vertex."),
      ("For y = x^2 - 4x + 3, find the x-intercepts by factoring.","Think: factor and set equal to zero","Factor: (x - 1)(x - 3) = 0. x = 1 or x = 3. These are where the parabola crosses the x-axis."),
      ("What are the zeros of a function?","Think: where f(x) = 0 (x-intercepts)","The zeros (roots) are the x-values where the function equals zero — the x-intercepts of the graph. A quadratic can have 0, 1, or 2 real zeros."),
    ]),
    s("Exponential functions",[
      ("What is an exponential function? Give an example.","Think: variable in the exponent","An exponential function has the form y = a × b^x where b > 0 and b ≠ 1. Example: y = 2 × 3^x. The variable is in the exponent, unlike polynomial functions where the variable is in the base."),
      ("What is the difference between exponential growth and decay?","Think: b > 1 vs. 0 < b < 1","Growth: b > 1 (population growth, compound interest, viral spread). Decay: 0 < b < 1 (radioactive decay, depreciation). Both follow the same general form but one increases and one decreases."),
      ("A population starts at 500 and doubles every 10 years. Write the equation.","Think: y = 500 × 2^(t/10)","y = 500 × 2^(t/10) where t is years. After 20 years: y = 500 × 2^2 = 2,000."),
      ("How is exponential growth different from linear growth?","Think: constant addition vs. constant multiplication","Linear: grows by a constant amount each period (adding the same number). Exponential: grows by a constant factor each period (multiplying by the same number). Exponential growth eventually far outpaces linear growth."),
    ]),
    s("Polynomial operations",[
      ("What is a polynomial? Give an example of degree 3.","Think: sum of terms with whole-number exponents","A polynomial is an expression with one or more terms of the form ax^n. Example of degree 3: 2x^3 - 4x^2 + x - 7."),
      ("Add: (3x^2 + 2x - 5) + (x^2 - 4x + 8)","Think: combine like terms","(3+1)x^2 + (2-4)x + (-5+8) = 4x^2 - 2x + 3."),
      ("Multiply: (x + 3)(x - 2)","Think: FOIL","First: x×x = x^2. Outer: x×(-2) = -2x. Inner: 3×x = 3x. Last: 3×(-2) = -6. Result: x^2 + x - 6."),
      ("Factor: x^2 + 5x + 6","Think: find two numbers that multiply to 6 and add to 5","2 × 3 = 6 and 2 + 3 = 5. Factored: (x + 2)(x + 3)."),
    ]),
    s("Graphing and interpreting functions",[
      ("What is a linear function vs. a nonlinear function?","Think: straight line vs. curved graph","Linear: graph is a straight line; constant rate of change; form y = mx + b. Nonlinear: graph curves (quadratic, exponential, etc.); rate of change is not constant."),
      ("How do you determine if a function is linear from a table of values?","Think: check if differences in y are constant","Calculate the first differences (change in y for each 1-unit change in x). If constant: linear. If not constant, check second differences or ratios for quadratic or exponential."),
      ("What does the y-intercept of a function represent in context?","Think: the starting value when x = 0","The y-intercept is the value of the function when x = 0. In context: the starting amount (initial population, initial account balance, initial height)."),
      ("A graph shows a company's profits: rises steeply, then levels off. Is this linear or nonlinear? What might explain this?","Think: nonlinear — diminishing returns","Nonlinear. The leveling off suggests diminishing returns — rapid growth early (new market) slowing as the market saturates. This is characteristic of logistic or logarithmic growth, not linear."),
    ]),
  ],
]
print("G8 math complete")

P[8]["science"] = [
  # U1: Physical Science
  [
    s("Newton's laws of motion",[
      ("State Newton's First Law of Motion.","Think: law of inertia","An object at rest stays at rest, and an object in motion stays in motion at constant velocity, unless acted upon by an unbalanced external force. Objects resist changes to their state of motion (inertia)."),
      ("State Newton's Second Law. Write the formula.","Think: F = ma","Net force = mass × acceleration (F = ma). Greater force produces greater acceleration; greater mass requires greater force for the same acceleration."),
      ("State Newton's Third Law and give an everyday example.","Think: equal and opposite reactions","For every action, there is an equal and opposite reaction. Examples: rocket exhaust pushes down → rocket moves up. You push back on a wall → wall pushes you forward. Swimming: hands push water back → water pushes you forward."),
      ("A 5 kg box accelerates at 3 m/s squared. What is the net force?","Think: F = ma","F = 5 × 3 = 15 Newtons."),
    ]),
    s("Forces and motion",[
      ("What is the difference between speed, velocity, and acceleration?","Think: magnitude only vs. magnitude and direction vs. change in velocity","Speed: how fast (scalar — magnitude only). Velocity: speed with direction (vector). Acceleration: rate of change of velocity (includes speeding up, slowing down, or changing direction)."),
      ("What is friction and what factors affect it?","Think: resistance to sliding motion","Friction: force resisting relative motion between surfaces. Affected by: normal force (how hard surfaces press together) and surface roughness. Friction converts kinetic energy to heat."),
      ("What is the difference between balanced and unbalanced forces?","Think: net force zero vs. nonzero","Balanced: net force = 0; no change in motion (object remains at rest or moves at constant velocity). Unbalanced: net force ≠ 0; causes acceleration (change in speed or direction)."),
      ("A car brakes suddenly. Using Newton's laws, explain what happens to the driver.","Think: inertia — First Law","The driver's body has inertia and tends to stay in motion (First Law). When the car decelerates due to braking force, the driver continues forward until the seatbelt applies a force to decelerate them too. Without a seatbelt, the driver would continue forward into the windshield."),
    ]),
    s("Energy transformations",[
      ("What is the difference between kinetic and potential energy?","Think: energy of motion vs. stored energy","Kinetic energy (KE): energy of motion — KE = (1/2)mv^2. Potential energy (PE): stored energy due to position or condition — gravitational PE = mgh. A ball at the top of a ramp has max PE; at the bottom, max KE."),
      ("State the Law of Conservation of Energy.","Think: energy cannot be created or destroyed","Energy cannot be created or destroyed — only converted from one form to another. Total energy of a closed system is constant. Real-world conversions are never 100% efficient — some energy becomes heat (entropy)."),
      ("Describe the energy transformations when a light bulb converts electricity to light.","Think: trace through the conversions","Electrical energy → (through the filament) → heat energy + light energy. Only about 5% becomes visible light in incandescent bulbs. LED bulbs are more efficient (~50% light)."),
      ("A roller coaster starts at the top of a 50-meter hill. What happens to PE and KE as it descends?","Think: PE converts to KE","At top: max PE, near-zero KE. As it descends: PE decreases, KE increases. At bottom: min PE, max KE. Ignoring friction: total mechanical energy (PE + KE) is constant throughout."),
    ]),
    s("Waves",[
      ("What is a wave? What do waves transfer?","Think: disturbance that transfers energy","A wave is a disturbance that travels through a medium (or space) and transfers energy without transferring matter. The medium itself does not travel — only the energy moves."),
      ("What is the difference between transverse and longitudinal waves?","Think: perpendicular vs. parallel vibration","Transverse: particles vibrate perpendicular to the direction of wave travel (light, water surface waves). Longitudinal (compression): particles vibrate parallel to wave travel (sound waves — compressions and rarefactions)."),
      ("Define wavelength, frequency, and amplitude.","Think: spatial, temporal, and height measures","Wavelength: distance between consecutive crests (or troughs). Frequency: number of complete waves per second (Hz). Amplitude: maximum displacement from rest position — determines wave energy and intensity."),
      ("How are wave speed, wavelength, and frequency related?","Think: v = f × lambda","Wave speed = frequency × wavelength. Example: sound at 343 m/s with frequency 440 Hz has wavelength = 343/440 ≈ 0.78 m."),
    ]),
    s("Electricity and magnetism",[
      ("What is an electric circuit? Name three components.","Think: closed path for current flow","An electric circuit is a closed path through which electric current flows. Components: power source (battery), conductor (wire), and load (lightbulb, motor). The circuit must be closed (complete) for current to flow."),
      ("What is the difference between series and parallel circuits?","Think: single path vs. multiple paths","Series: all components on one path — if one fails, all fail. Current is the same throughout. Parallel: multiple paths — if one fails, others still work. Voltage is the same across each branch. Household wiring is parallel."),
      ("What is Ohm's Law?","Think: V = IR","Voltage (V) = Current (I) × Resistance (R). Increasing voltage increases current; increasing resistance decreases current. Used to calculate any of the three if the other two are known."),
      ("How do magnets and electric currents interact?","Think: electromagnetism","A moving electric charge (current) creates a magnetic field. Conversely, a changing magnetic field creates an electric current (electromagnetic induction — basis of generators and transformers). This is the foundation of all electric motors and generators."),
    ]),
  ],
  # U2: Life Science (4 topics)
  [
    s("DNA and heredity",[
      ("What is DNA and what is its structure?","Think: double helix, base pairs","DNA (deoxyribonucleic acid): the molecule carrying genetic information. Structure: double helix — two sugar-phosphate strands connected by base pairs (A-T and G-C). Each strand is complementary to the other."),
      ("What is a gene? How do genes relate to traits?","Think: sequence of DNA that codes for a protein","A gene is a specific sequence of DNA bases that codes for a protein. Proteins determine traits (eye color, enzyme production, etc.). Most traits are influenced by multiple genes and the environment."),
      ("What is the difference between DNA, genes, and chromosomes?","Think: nested levels of organization","DNA is the molecule. Genes are specific functional segments of DNA. Chromosomes are tightly coiled structures of DNA + protein. Humans have 46 chromosomes (23 pairs) containing approximately 20,000–25,000 genes."),
      ("What is the difference between dominant and recessive alleles?","Think: Mendel's observations","Dominant allele: expressed even when only one copy is present (written as capital letter). Recessive allele: expressed only when two copies are present (written as lowercase). Dominant masks recessive in heterozygous individuals."),
    ]),
    s("Genetics and Punnett squares",[
      ("What is a Punnett square? Set up a cross between two Tt parents.","Think: shows probability of offspring genotypes","Punnett square shows possible genotype combinations. Tt × Tt: T T / T → TT. T t / T → Tt. T T / t → Tt. T t / t → tt. Ratio: 1 TT : 2 Tt : 1 tt (3 tall : 1 short phenotype)."),
      ("What is the difference between genotype and phenotype?","Think: genetic makeup vs. observable trait","Genotype: actual allele combination (TT, Tt, tt). Phenotype: observable characteristic (tall or short). Same phenotype can have different genotypes (TT and Tt both appear tall)."),
      ("What is the difference between homozygous and heterozygous?","Think: same alleles vs. different alleles","Homozygous: two identical alleles (TT or tt). Heterozygous: two different alleles (Tt). A heterozygous individual for a dominant trait will appear dominant phenotypically."),
      ("A pea plant with purple flowers (Pp) crosses with a white-flowered plant (pp). What are the expected phenotype ratios?","Think: Pp × pp cross","Pp and pp offspring: 50% Pp (purple), 50% pp (white). This is a testcross — used to determine unknown genotype."),
    ]),
    s("Evolution and natural selection",[
      ("What is Darwin's theory of natural selection?","Think: variation + heritability + differential survival","Organisms with heritable variations that improve survival and reproduction in their environment produce more offspring. Over generations, these favorable traits become more common in the population (evolution)."),
      ("What are the four requirements for natural selection to occur?","Think: VHSD","(1) Variation: individuals differ in traits. (2) Heritability: traits pass to offspring. (3) Struggle for survival: more offspring born than survive. (4) Differential survival: some variants survive and reproduce more."),
      ("What is fossil evidence for evolution?","Think: gradual changes in the fossil record","Fossils show: transitional forms between ancestral and modern species, changes in complexity over time, extinct species that link modern groups. The fossil record is incomplete but provides strong directional evidence for evolution."),
      ("What is the difference between evolution and adaptation?","Think: population over time vs. trait in an individual","Evolution: change in allele frequencies in a population over generations. Adaptation: a heritable trait that increases fitness in a particular environment. Adaptations accumulate through natural selection, producing evolutionary change."),
    ]),
    s("Ecosystems and sustainability",[
      ("What is ecological succession? Name the two types.","Think: gradual change in community over time","Ecological succession: predictable change in species composition over time. Primary: starts on bare rock with no soil (after lava flow or glacier retreat). Secondary: recovery after disturbance with soil intact (after fire, logging)."),
      ("What are ecosystem services? Name four examples.","Think: benefits humans get from ecosystems","Provisioning: food, water, medicine. Regulating: climate regulation, flood control, water purification. Cultural: recreation, aesthetic value. Supporting: nutrient cycling, soil formation. These are often undervalued until lost."),
      ("What is the difference between renewable and nonrenewable resources?","Think: replenishment rate","Renewable: replenished naturally at a rate that can sustain use (solar, wind, sustainably managed forests, water). Nonrenewable: formed over millions of years, depleted faster than replenished (fossil fuels, many minerals)."),
      ("What is biodiversity's role in ecosystem resilience?","Think: more species = more stable ecosystem","Greater biodiversity provides more functional redundancy — if one species declines, others can fill its role. Diverse ecosystems recover better from disturbances. Monocultures (low diversity) are vulnerable to single threats (one pest or disease can wipe them out)."),
    ]),
  ],
  # U3: Chemistry
  [
    s("Chemical bonds",[
      ("What are the two main types of chemical bonds?","Think: ionic and covalent","Ionic: electrons transferred from one atom to another (between metals and nonmetals). Covalent: electrons shared between atoms (between nonmetals). A third type is metallic bonding (shared electron sea in metals)."),
      ("What is an ionic bond? Give one example.","Think: electron transfer creates oppositely charged ions that attract","Ionic bond: a metal loses electrons (becomes positive cation) and a nonmetal gains electrons (becomes negative anion). Electrostatic attraction holds them together. Example: NaCl — Na loses 1 electron, Cl gains 1."),
      ("What is a covalent bond? What is a molecule?","Think: sharing electrons between nonmetals","Covalent bond: two atoms share pairs of electrons. A molecule is formed when two or more atoms are covalently bonded. Examples: H2O (water), CO2, O2. Covalent bonds are generally stronger than ionic bonds."),
      ("What is an ion? Give one positive and one negative example.","Think: atom with unequal protons and electrons","Ion: atom or group of atoms with a net electric charge. Positive ion (cation): lost electrons (Na+ has 11 protons, 10 electrons). Negative ion (anion): gained electrons (Cl- has 17 protons, 18 electrons)."),
    ]),
    s("Chemical reactions",[
      ("What is a chemical reaction? What are reactants and products?","Think: substances transform into new substances","A chemical reaction: reactants → products (new substances with different properties). Reactants: starting materials. Products: substances formed. Evidence: color change, gas produced, precipitate, energy change."),
      ("What are the five types of chemical reactions?","Think: synthesis, decomposition, single replacement, double replacement, combustion","Synthesis: A + B → AB. Decomposition: AB → A + B. Single replacement: A + BC → AC + B. Double replacement: AB + CD → AD + CB. Combustion: fuel + O2 → CO2 + H2O + energy."),
      ("Balance: H2 + O2 → H2O","Think: count atoms on each side","Unbalanced: 2H + 2O → 2H + O (oxygen has 2, product has 1). Balanced: 2H2 + O2 → 2H2O. Both sides: 4H and 2O."),
      ("What is the difference between exothermic and endothermic reactions?","Think: energy released vs. energy absorbed","Exothermic: releases energy (heat, light) — products have less energy than reactants. Examples: combustion, respiration, hand warmers. Endothermic: absorbs energy — products have more energy than reactants. Examples: photosynthesis, melting, baking soda + vinegar."),
    ]),
    s("Acids and bases",[
      ("What is the pH scale and what does it measure?","Think: 0 to 14; 7 = neutral","pH: measures hydrogen ion concentration. Scale 0–14. pH < 7: acidic (more H+ ions). pH = 7: neutral (pure water). pH > 7: basic/alkaline (more OH- ions). Each unit = 10x change in concentration (logarithmic scale)."),
      ("Give two examples of common acids and bases.","Think: everyday acids and bases","Acids: vinegar (acetic acid, pH ~3), lemon juice (citric acid, pH ~2), battery acid (sulfuric acid, pH ~1). Bases: baking soda (sodium bicarbonate, pH ~8.3), bleach (sodium hypochlorite, pH ~13), ammonia (pH ~11)."),
      ("What is neutralization? Write a general equation.","Think: acid + base → salt + water","When an acid and base react, they neutralize each other to form salt and water. HCl + NaOH → NaCl + H2O. The pH of the resulting solution depends on whether the acid or base is stronger."),
      ("Why is pH important in living organisms?","Think: enzymes are pH-sensitive","Enzymes (biological catalysts) work only within specific pH ranges. Human blood: pH 7.35–7.45 — outside this range, proteins denature and organs fail. Stomach: pH 1.5–3.5 to digest proteins. pH regulation is critical to life."),
    ]),
    s("The mole and measurement",[
      ("What is density and how is it calculated?","Think: mass per unit volume","Density = mass / volume. A measure of how much mass is packed into a given volume. Units: g/cm^3 or g/mL for solids and liquids. Dense objects sink in less dense fluids; less dense objects float."),
      ("A substance has mass 45 g and volume 15 cm^3. Calculate density. Will it float in water (density 1 g/cm^3)?","Think: D = m/v; compare to water","D = 45/15 = 3 g/cm^3. Since 3 > 1, it sinks in water."),
      ("What are physical properties vs. chemical properties?","Think: can observe without changing vs. describes reactions","Physical: observable without changing composition (color, density, melting point, solubility). Chemical: describes how a substance reacts to form new substances (flammability, reactivity with acid, corrosiveness)."),
      ("What is a pure substance vs. a mixture?","Think: uniform composition vs. variable composition","Pure substance: uniform composition throughout — cannot be separated by physical means. Either an element (one type of atom) or compound (chemically bonded elements). Mixture: two or more substances not chemically bonded — can be separated physically."),
    ]),
  ],
  # U4: Earth Science
  [
    s("Climate change",[
      ("What is the difference between weather and climate?","Think: short-term vs. long-term patterns","Weather: atmospheric conditions at a specific place and time (today's rain). Climate: average weather patterns over 30+ years for a region. Climate change: long-term shifts in these averages globally."),
      ("What is the greenhouse effect and how do human activities enhance it?","Think: natural process amplified by emissions","Greenhouse effect: naturally, greenhouse gases (CO2, H2O vapor, CH4) trap heat, keeping Earth warm enough for life. Human burning of fossil fuels increases CO2 concentrations, trapping more heat and warming the planet beyond natural levels."),
      ("What is the evidence for human-caused climate change?","Think: multiple independent lines of evidence","(1) CO2 levels highest in 800,000 years (ice cores). (2) Global average temperature rising 1.1°C since pre-industrial. (3) Sea levels rising. (4) Arctic ice shrinking. (5) Isotopic signature of CO2 matches fossil fuel burning, not natural sources."),
      ("What are two effects of climate change on ecosystems?","Think: species range shifts, coral bleaching, phenology changes","(1) Species shifting ranges toward poles/higher elevations as temperatures warm. (2) Coral bleaching: warming oceans stress corals to expel algae, causing bleaching and death. (3) Timing mismatches: flowers bloom before pollinators arrive."),
    ]),
    s("Astronomy basics",[
      ("What is the difference between rotation and revolution for Earth?","Think: spin vs. orbit","Rotation: Earth spinning on its axis (once every 24 hours) — causes day and night. Revolution: Earth orbiting the Sun (once every 365.25 days) — related to the calendar year."),
      ("What causes Earth's seasons?","Think: tilt of axis, not distance from Sun","Earth's axis is tilted 23.5 degrees. When the Northern Hemisphere tilts toward the Sun (summer): more direct sunlight and longer days. When tilted away (winter): less direct sunlight and shorter days. Distance from Sun is NOT the primary cause."),
      ("What is the difference between a solar and lunar eclipse?","Think: which body casts a shadow on which","Solar eclipse: Moon passes between Earth and Sun, casting its shadow on Earth (Moon blocks sunlight). Lunar eclipse: Earth passes between Sun and Moon, casting its shadow on the Moon (Earth blocks sunlight to the Moon)."),
      ("How do we know the age of the universe and solar system?","Think: radiometric dating and cosmic microwave background","Universe: ~13.8 billion years (cosmic microwave background radiation, expansion rate). Solar system: ~4.6 billion years (radiometric dating of meteorites — oldest known solar system material)."),
    ]),
    s("Water cycle and weather",[
      ("What drives the water cycle?","Think: solar energy evaporates water; gravity pulls it back","Solar energy evaporates water from oceans, lakes, and plants (transpiration). Water vapor condenses into clouds (condensation). Precipitation (rain, snow) falls. Water flows back to oceans via rivers or percolates into groundwater."),
      ("What is the difference between condensation and precipitation?","Think: vapor becomes liquid vs. falls from atmosphere","Condensation: water vapor cools and becomes liquid water droplets (clouds, dew). Precipitation: water falls from the atmosphere (rain, snow, sleet, hail) when droplets become heavy enough."),
      ("What causes different types of precipitation (rain vs. snow)?","Think: temperature at which water falls","Rain: liquid droplets form or frozen particles melt before reaching the ground. Snow: temperatures remain below freezing all the way down — ice crystals don't melt. Sleet: freezes after forming as rain. Hail: updrafts carry ice pellets repeatedly through clouds."),
      ("What is a weather front and what happens at a cold front?","Think: boundary between air masses","A front is the boundary between two air masses with different temperatures and humidity. Cold front: cold air mass pushes under warm air → warm air rises rapidly → thunderstorms, heavy precipitation, temperature drop after front passes."),
    ]),
    s("Earth's history",[
      ("What is geological time and how is it organized?","Think: eons, eras, periods, epochs","Geological time divides Earth's 4.6-billion-year history into: Eons (largest — Phanerozoic, Proterozoic), Eras (Paleozoic, Mesozoic, Cenozoic), Periods (Jurassic, Cretaceous), Epochs (Holocene). Boundaries are defined by major extinction events or geological changes."),
      ("What is radiometric dating and how does it determine age?","Think: radioactive decay as a clock","Radioactive isotopes decay at constant, known rates (half-life). By measuring the ratio of parent isotope to daughter isotope in a rock, scientists calculate how long the decay has been occurring — the rock's age. Accurate over billions of years."),
      ("What is a mass extinction? Name one example.","Think: sudden loss of large percentage of species","Mass extinction: rapid, widespread loss of a large percentage of species. Example: End-Cretaceous (K-Pg) event 66 million years ago — asteroid impact likely triggered climate change, killing ~75% of species including all non-avian dinosaurs."),
      ("How do index fossils help geologists date rock layers?","Think: distinctive species lived in specific time periods","Index fossils: fossils of organisms that lived in a specific, short time period and were geographically widespread. When found in rock layers, they indicate the layer's age. Allow correlation of rock layers across different locations."),
    ]),
  ],
]
print("G8 science complete")

P[8]["ela"] = [
  [
    s("Analyzing literary texts",[
      ("How does an author use conflict to develop theme?","Think: conflict forces characters to reveal values","Conflict forces characters to make choices that reveal their values and beliefs. How they respond to conflict — and the consequences — embodies the theme. A character who chooses honesty over self-interest in a conflict may point to a theme about integrity."),
      ("What is an allegory? Give one example.","Think: extended metaphor where characters/events represent abstract ideas","An allegory is a narrative where characters, settings, and events represent abstract concepts. Example: Animal Farm (Orwell) — the farm and animals represent Soviet communism; Napoleon = Stalin; Snowball = Trotsky. Every element operates on two levels."),
      ("What is the difference between theme and moral?","Think: implicit vs. explicit message","Moral: an explicit lesson stated in the text (Aesop's fables often state the moral directly). Theme: an implicit, complex idea explored throughout — not a simple rule but a nuanced observation about life. Literary themes rarely offer simple answers."),
      ("How does analyzing multiple texts on the same theme deepen understanding?","Think: different perspectives illuminate different facets","Each author approaches the theme through different characters, settings, and events. Comparing reveals: What do they agree on? What do they differ on? Where one text is ambiguous, another may offer clarity or productive contrast."),
    ]),
    s("Textual evidence and inference",[
      ("What is the difference between explicit and implicit information?","Think: stated vs. implied","Explicit: directly stated in the text. Implicit: suggested but not stated directly — reader must infer from clues, diction, or context. Strong literary analysis often focuses on what is implied rather than what is stated."),
      ("What is a valid inference? How do you support one?","Think: logical conclusion grounded in textual evidence","A valid inference: a logical conclusion not directly stated but strongly supported by evidence. Support by: quoting relevant text, explaining the logical connection between evidence and inference, and ruling out alternative interpretations."),
      ("What is the difference between inference and assumption?","Think: evidence-based vs. unfounded","Inference: conclusion drawn from evidence in the text. Assumption: a conclusion drawn without evidence, based on personal belief or stereotype. Academic reading requires inferences, not assumptions."),
      ("How do you cite textual evidence in a paragraph effectively?","Think: introduce, integrate, explain","Introduce the context (who/what/when in the text), integrate the quote or paraphrase smoothly, then explain how it supports your claim. Never drop a quote without analysis — every piece of evidence needs your interpretive commentary."),
    ]),
    s("Author's craft",[
      ("What is narrative distance and how does an author control it?","Think: how close the narrator is to the action and characters","Narrative distance: how emotionally and physically close the narrator is to the story. Close: intimate, first-person or close third — we know the character's every thought. Distant: objective, detached — we observe from outside. Authors shift distance deliberately for effect."),
      ("What is pacing in a narrative and how do authors control it?","Think: speed at which the story moves","Pacing: the speed of the narrative. Fast: short sentences, action, minimal description (creates urgency). Slow: long sentences, detailed description, internal reflection (creates tension or emotional depth). Authors slow down for important moments."),
      ("What is tone and how does diction create it?","Think: author's attitude expressed through word choices","Tone: the author's attitude toward the subject or audience. Diction creates tone — formal vs. informal, Latinate vs. Anglo-Saxon words, positive vs. negative connotations. Tone shapes how the reader responds to content."),
      ("What is the effect of syntax (sentence structure) on meaning and mood?","Think: sentence length and structure creates rhythm and emphasis","Short sentences: urgency, emphasis, speed. Long, complex sentences: contemplation, complexity, elegance. Fragments: abruptness, emphasis. Cumulative sentences (details added after main clause): a sense of accumulation. Authors use syntax as a rhetorical tool."),
    ]),
    s("Argument and rhetoric",[
      ("What are the three rhetorical appeals? Define each.","Think: ethos, logos, pathos","Ethos: appeal to credibility (why should we trust you?). Logos: appeal to logic and evidence (data, reasoning, examples). Pathos: appeal to emotion (stories, vivid language, values). Effective arguments typically use all three."),
      ("What is a rhetorical device? Give two examples.","Think: techniques that make writing more persuasive or memorable","Anaphora: repetition of a word or phrase at the beginning of successive clauses (I have a dream...). Rhetorical question: a question asked for effect, not to receive an answer (Is this the kind of country we want?). Many others: antithesis, hyperbole, parallelism."),
      ("How do you identify an author's purpose and audience in an argument?","Think: clues in diction, evidence choices, structure","Purpose: what the author wants you to think, believe, feel, or do. Audience: who the author is writing for (experts vs. general public, political allies vs. opponents). Clues: vocabulary level, types of evidence used, assumptions made, emotional appeals chosen."),
      ("What is the difference between a strong and a weak claim in argument writing?","Think: specific, arguable, and supportable","Strong: specific, takes a clear position, not merely a fact or observation, supportable with evidence. Weak: too broad (Everything has pros and cons), merely factual (Pollution exists), or so extreme it cannot be supported (Everyone agrees...)."),
    ]),
    s("Writing literary analysis",[
      ("What is a literary analysis essay? How is it structured?","Think: making an argument about a literary text","A literary analysis essay makes an argument about how a literary text works and what it means. Structure: introduction with a specific arguable thesis, body paragraphs each making one point supported by textual evidence and analysis, conclusion that extends beyond summary."),
      ("What makes a literary analysis thesis strong?","Think: arguable, specific, and insightful","Strong thesis: makes a specific, arguable claim about the text (not just a summary or observation). Weak: The novel is about friendship. Strong: Through Lennie's relationship with George, Steinbeck argues that true friendship requires sacrifice of one's own interests."),
      ("What is the difference between plot summary and analysis in a literary essay?","Think: retelling vs. interpreting","Plot summary: restates what happens. Analysis: explains WHY it happens, WHAT it means, and HOW the author achieves the effect. Literary analysis assumes the reader knows the plot — focus entirely on interpretation and argument."),
      ("How do you write a strong analytical body paragraph?","Think: topic sentence, evidence, analysis","(1) Topic sentence: states the paragraph's argument (not a plot summary). (2) Evidence: specific textual quote or paraphrase. (3) Analysis: explains how the evidence supports the topic sentence and thesis. (4) Connection: links back to the thesis or transitions to the next paragraph."),
    ]),
  ],
  [
    s("Research skills",[
      ("What is a research question and how do you develop a good one?","Think: specific, arguable, and answerable","A research question guides your inquiry. Good qualities: specific (not too broad), arguable (not a simple yes/no fact), researchable (evidence exists), and interesting (worth investigating). Weak: What is climate change? Strong: How have Pacific Island nations responded to climate-related displacement?"),
      ("What is the difference between a primary and secondary source? Give one example of each.","Think: firsthand vs. analysis of firsthand","Primary: original source from the time period or event (diary, speech, original research study, photograph). Secondary: analyzes or interprets primary sources (textbook chapter, biography, literary criticism). Both are valuable for different purposes."),
      ("How do you evaluate a website for credibility?","Think: SIFT method — Stop, Investigate, Find better coverage, Trace claims","SIFT: Stop before sharing or believing. Investigate the source (who wrote it?). Find better coverage (what do other credible sources say?). Trace claims to original sources. Also check: when was it published? What is the site's purpose?"),
      ("What is the difference between paraphrasing and patchwriting?","Think: genuine restatement vs. superficial synonym substitution","Paraphrase: restate the idea completely in your own words and sentence structure — shows genuine understanding. Patchwriting: swap a few words with synonyms while keeping the original structure — academically dishonest and shows poor understanding. Always cite both."),
    ]),
    s("Grammar and style",[
      ("What is a dangling modifier? Correct this: Having studied all night, the exam was easy.","Think: modifier must attach to the correct noun","The modifier Having studied all night attaches to exam (which cannot study). Fixed: Having studied all night, she found the exam easy. The subject performing the modified action must immediately follow the modifier."),
      ("What is the difference between restrictive and non-restrictive clauses? Use commas correctly.","Think: essential vs. non-essential information","Restrictive (no commas): essential to meaning — removing it changes the meaning. The student who studied passed. (Specifies which student.) Non-restrictive (commas): non-essential — could be removed without changing core meaning. Maya, who had studied all night, passed."),
      ("What is subjunctive mood and when do you use it?","Think: hypothetical, wishes, suggestions","Subjunctive: used for hypothetical or contrary-to-fact situations, wishes, and suggestions. If I were taller (not was — subjunctive). The teacher suggested that he be excused (not is). Formal academic writing uses subjunctive correctly."),
      ("What is a semicolon used for? Give two examples of correct use.","Think: joining related independent clauses; also in complex lists","(1) Joining two closely related independent clauses: She finished her essay; he had not even started. (2) Separating items in a list when items themselves contain commas: We visited Paris, France; London, England; and Rome, Italy."),
    ]),
    s("Poetry analysis",[
      ("What is meter in poetry? What is iambic pentameter?","Think: pattern of stressed and unstressed syllables","Meter: the rhythmic pattern of stressed and unstressed syllables. Iambic pentameter: five iambs per line (iamb = unstressed + stressed, da-DUM). Shakespeare's sonnets and plays use iambic pentameter: Shall I compare thee to a summer's day?"),
      ("What is the difference between a metaphor and an extended metaphor (conceit)?","Think: brief comparison vs. sustained metaphor throughout a poem","Metaphor: direct comparison without like or as. Extended metaphor (conceit): a metaphor that continues throughout a poem or significant portion, developing multiple points of comparison. Donne's A Valediction Forbidding Mourning compares two souls to a compass throughout."),
      ("How does a poet use enjambment vs. end-stopped lines?","Think: line break continues vs. line break pauses","End-stopped: line ends at a natural grammatical pause (comma, period). Enjambment: line runs over into next without pause — the reader is pulled forward, creating urgency or surprise. The meaning of the enjambed line often shifts with the next line."),
      ("What is the difference between the speaker of a poem and the poet?","Think: persona vs. author","The speaker (persona) is the voice in the poem — it may or may not reflect the poet's own views. The speaker is a character the poet creates. Even in first-person poems, we cannot assume the speaker's experience is the poet's autobiographical experience."),
    ]),
    s("Vocabulary in context",[
      ("How do you determine the meaning of an unfamiliar word using multiple context clues?","Think: combine multiple clue types","Look for: definition (explains the word in the text), example (gives an instance), synonym (similar word nearby), antonym (opposite word with a contrast signal), and general context (overall meaning of the passage). Multiple clues together give more reliable meaning."),
      ("What is etymology and how does it help vocabulary building?","Think: word origins reveal meaning patterns","Etymology: the history and origin of words. Knowing Latin and Greek roots unlocks thousands of words. Root bio (life): biology, biography, antibiotic. Root chrono (time): chronology, chronic, synchronize. Learning roots is more efficient than memorizing individual words."),
      ("What are academic vocabulary words and why are they important?","Think: Tier 2 words — high-frequency academic terms","Academic vocabulary (Tier 2): words common across all academic subjects that signal relationships, qualifications, and analysis (analyze, contrast, infer, justify, evaluate, synthesize, implicit). Mastering these words is essential for academic reading and writing."),
      ("How does a word's connotation differ from its denotation in a persuasive text?","Think: dictionary meaning vs. emotional associations used strategically","Authors in persuasive texts choose words for their connotations — the emotional associations that go beyond the dictionary definition. Identifying loaded language (words with strong connotations) helps readers recognize when an author is trying to influence emotion rather than inform."),
    ]),
  ],
  [
    s("Speeches and rhetoric",[
      ("What is the difference between deductive and inductive reasoning?","Think: general to specific vs. specific to general","Deductive: starts with a general principle and applies it to a specific case (All mammals breathe air. Whales are mammals. Therefore whales breathe air.). Inductive: observes specific cases and draws a general conclusion (Every swan I have seen is white. Therefore all swans are white — can be disproven by one black swan)."),
      ("What is a rhetorical situation?","Think: writer + purpose + audience + context + medium","The rhetorical situation is the context in which communication occurs: Who is speaking (ethos)? To whom (audience)? For what purpose? In what context (political moment, cultural moment)? Through what medium (speech, essay, advertisement)? All of these shape effective rhetoric."),
      ("How do you analyze a historical speech?","Think: SOAPS — Speaker, Occasion, Audience, Purpose, Subject","SOAPS: Speaker (who, their credibility and position), Occasion (when and why the speech was given), Audience (who was it for, what did they believe?), Purpose (what did the speaker want to achieve?), Subject (what is the speech literally about?). Then analyze the rhetorical strategies used."),
      ("What makes a speech memorable? Identify one technique from a famous speech.","Think: specific rhetorical device that creates resonance","Anaphora creates memorable rhythm and emphasis: I have a dream... (MLK). Chiasmus creates a satisfying reversal: Ask not what your country can do for you... (JFK). Vivid, concrete language makes abstract ideas tangible and emotionally resonant."),
    ]),
    s("Drama and reading plays",[
      ("How does reading a play differ from reading a novel?","Think: no narrator, stage directions, only dialogue","A play has no narrator to explain characters' thoughts — all characterization comes through dialogue, action, and stage directions. The reader must infer subtext (what is meant but not said) from what characters do and say."),
      ("What is subtext in drama?","Think: what is meant beneath what is said","Subtext: the implicit meaning beneath the surface of dialogue. Characters rarely say exactly what they mean — especially in conflict. Analyzing subtext means asking: What does this character REALLY want? What are they NOT saying? Why?"),
      ("What are dramatic conventions? Name two.","Think: theatrical devices audiences accept","Dramatic conventions: techniques that audiences accept as theatrical reality. Soliloquy: character speaks thoughts aloud to the audience when alone. Aside: character briefly speaks to the audience while other characters supposedly cannot hear. Both share private information with the audience."),
      ("How does dramatic irony create tension in a play?","Think: audience knows what characters do not","Dramatic irony: the audience knows something the characters don't. This creates tension — we watch characters make decisions based on false information, knowing the consequences they cannot see. Classic example: Romeo does not know Juliet is only sleeping."),
    ]),
  ],
  [
    s("Argument vs. persuasion",[
      ("What is the difference between argument and persuasion?","Think: logical evidence-based vs. emotional appeals","Argument: relies on logic, evidence, and reasoning to convince. Acknowledges counterarguments. Persuasion: may use emotional appeals, one-sided framing, and rhetorical techniques. Academic writing is closer to argument; advertising is persuasion."),
      ("How do you identify emotional manipulation vs. emotional appeal?","Think: legitimate emotional connection vs. bypassing reason","Legitimate emotional appeal: uses emotion to illustrate a point supported by evidence (a story that makes data concrete). Manipulation: uses emotion to REPLACE evidence or to provoke fear, anger, or disgust without logical support. Ask: Is the emotional content supported by evidence?"),
      ("What is a straw man fallacy?","Think: misrepresenting the opponent's position","Straw man: misrepresenting or oversimplifying an opponent's argument to make it easier to attack. Example: Opponent argues for stricter gun regulations. Straw man response: They want to take all guns from everyone! Effective argument engages with the strongest version of the opposing position."),
      ("What is the difference between a fact, an inference, and a judgment?","Think: provable vs. concluded vs. valued","Fact: verifiable by direct observation or reliable measurement. Inference: conclusion drawn from facts (logical but not directly observable). Judgment: evaluation involving values (good, bad, should, ought). Strong arguments are clear about which type of claim is being made."),
    ]),
  ],
]
print("G8 ELA complete")

P[8]["history"] = [
  [
    s("Industrial Revolution",[
      ("What were the major causes of the Industrial Revolution starting in Britain?","Think: coal, water power, colonies, enclosure, labor","(1) Coal and iron deposits. (2) River systems for water power and transport. (3) Colonial markets and raw materials. (4) Agricultural enclosure movement freed rural labor for factories. (5) Political stability supporting investment and innovation."),
      ("How did the Industrial Revolution change working conditions and urban life?","Think: child labor, factory conditions, urbanization","Factory work replaced agricultural labor: long hours (12-16 hr/day), dangerous machinery, child labor common, no safety regulations. Rapid urbanization created overcrowded cities with poor sanitation — cholera epidemics were frequent. Working class emerged as a new social force."),
      ("What were the major inventions of the Industrial Revolution? Name three.","Think: steam engine, spinning jenny, telegraph","Steam engine (Watt): powered factories, trains, ships. Spinning jenny and power loom (Hargreaves, Cartwright): mechanized textile production. Interchangeable parts (Whitney): enabled mass production. Telegraph (Morse): revolutionized communication."),
      ("How did the Industrial Revolution contribute to social inequality?","Think: wealth concentrated among factory owners; workers impoverished","Industrial capitalism created enormous wealth for factory owners while workers lived in poverty. This stark inequality inspired Karl Marx's critique of capitalism and the rise of labor movements (unions) demanding better wages and working conditions."),
    ]),
    s("Imperialism",[
      ("What is imperialism? Why did European nations pursue it in the 1800s?","Think: control of other territories for economic and political gain","Imperialism: a stronger nation's control over weaker nations politically, economically, or culturally. Motivations: (1) Raw materials for factories. (2) Markets for manufactured goods. (3) Social Darwinism (belief in racial hierarchy). (4) Strategic military positioning. (5) Nationalism and competition."),
      ("What was the Berlin Conference of 1884-85 and why is it significant?","Think: European powers divided Africa without African consent","European powers (no African nations were present) divided Africa among themselves to regulate colonization and avoid conflict among Europeans. By 1914, only Ethiopia and Liberia remained independent. Set the boundary lines that still create conflict today."),
      ("What were the effects of British imperialism in India?","Think: economic exploitation + cultural disruption + resistance","British rule: (1) Drained India's wealth to Britain. (2) Destroyed traditional Indian textile industries. (3) Built railroads to extract resources, not develop India. (4) Created administrative class of English-educated Indians. (5) The 1857 Sepoy Mutiny showed resistance. Led ultimately to independence movement."),
      ("What was Social Darwinism and how was it misused to justify imperialism?","Think: misapplication of Darwin's ideas to society","Social Darwinism: applying natural selection to human societies — the idea that stronger nations dominating weaker ones was natural and inevitable. Misused Darwin's biological theory to justify racism and imperialism as natural hierarchy rather than political choice. Used to claim colonization benefited the colonized."),
    ]),
    s("Nationalism and revolution",[
      ("What is nationalism and how did it reshape Europe in the 1800s?","Think: shared identity creating political movements","Nationalism: the belief that people sharing a language, culture, and history should form their own nation-state. Reshaped Europe: (1) German unification (1871 — Bismarck). (2) Italian unification (Risorgimento). (3) Dissolution of multi-ethnic empires (Ottoman, Austro-Hungarian). (4) Inspired revolutionary movements."),
      ("What were the main causes of World War I?","Think: MAIN — Militarism, Alliance System, Imperialism, Nationalism","Militarism: arms race (especially Germany vs. Britain). Alliance System: Triple Alliance (Germany, Austria-Hungary, Italy) vs. Triple Entente (France, Russia, Britain) — one conflict triggered all. Imperialism: competition for colonies created tensions. Nationalism: in the Balkans especially. Assassination of Archduke Franz Ferdinand was the spark."),
      ("What was the significance of the Treaty of Versailles?","Think: punitive peace that sowed seeds of WWII","Blamed Germany for the war (War Guilt Clause), imposed massive reparations ($33 billion), stripped Germany of territory and colonies, limited its military, and humiliated Germany's people — fueling resentment that Adolf Hitler exploited to rise to power."),
      ("What was the Russian Revolution and what caused it?","Think: 1917, WWI + inequality + weak tsar","Czar Nicholas II: autocratic and incompetent. Russia suffering massive WWI casualties and food shortages. The 1917 February Revolution overthrew the Tsar. The October Revolution (Bolsheviks under Lenin) overthrew the provisional government, establishing the world's first communist state."),
    ]),
    s("World Wars",[
      ("What were the major turning points of World War II?","Think: Stalingrad, D-Day, Midway, atomic bomb","Battle of Stalingrad (1942-43): Germany's defeat in USSR was the turning point in Europe. Battle of Midway (1942): US destroyed Japan's carrier fleet — turning point in the Pacific. D-Day (June 6, 1944): Allied invasion of France opened Western Front. Atomic bombs on Hiroshima and Nagasaki (August 1945): forced Japan's surrender."),
      ("What was the Holocaust? How many people were killed?","Think: systematic genocide of Jews and others by Nazi Germany","The Holocaust: the systematic, state-sponsored murder of approximately 6 million Jews (two-thirds of European Jewry) and 5-6 million others (Roma, disabled people, Soviet POWs, homosexuals, political opponents) by Nazi Germany from 1933-1945. Industrialized killing using concentration and extermination camps."),
      ("What was the United Nations and why was it created after World War II?","Think: prevent future world wars through cooperation","Founded 1945: 51 original members. Goals: maintain international peace and security, develop friendly relations among nations, promote human rights. Replaced the failed League of Nations. Created mechanisms like the Security Council for collective security. Limitations: great power veto on the Security Council."),
      ("What caused the Cold War between the US and Soviet Union?","Think: competing ideologies and postwar power vacuum","After WWII, two superpowers remained with competing ideologies: US (democracy and capitalism) vs. USSR (communism). Disagreements over postwar Europe's organization (Soviet domination of Eastern Europe), nuclear weapons competition, and global influence created decades of tension without direct military conflict."),
    ]),
  ],
  [
    s("Civil Rights and Human Rights",[
      ("What were the major goals and strategies of the US Civil Rights Movement?","Think: end legal segregation and secure voting rights","Goals: end racial segregation (Jim Crow laws), secure voting rights, achieve economic equality. Strategies: nonviolent direct action (sit-ins, marches), legal challenges (NAACP legal strategy — Brown v. Board), economic pressure (Montgomery Bus Boycott), and political organizing. Led to Civil Rights Act (1964) and Voting Rights Act (1965)."),
      ("What is the Universal Declaration of Human Rights?","Think: 1948 UN document defining fundamental rights","Adopted by the UN General Assembly in 1948 after WWII and the Holocaust. Defines fundamental rights owed to all humans regardless of nationality, ethnicity, sex, or religion: right to life, liberty, freedom of expression, education, and freedom from torture. Not legally binding but highly influential."),
      ("How did decolonization movements in Africa and Asia connect to human rights ideas?","Think: self-determination as a human right","After WWII, independence movements challenged colonial powers using Enlightenment and human rights language. If all humans have equal rights, colonized people have the right to self-determination. India (1947), Ghana (1957), many African nations in the 1960s won independence by connecting their struggle to universal human rights principles."),
      ("What is the difference between civil rights and human rights?","Think: rights under a state vs. universal rights","Civil rights: rights guaranteed to citizens by their own government (right to vote, equal treatment under law). Human rights: universal rights inherent to all humans regardless of citizenship, including rights governments may violate. Human rights apply even when governments deny civil rights."),
    ]),
    s("Cold War",[
      ("What was the policy of containment and how was it applied?","Think: Truman Doctrine — stop spread of communism","Containment (George Kennan, 1946): US policy to prevent Soviet communism from spreading. Applied through: Marshall Plan (economic aid to rebuild Europe), NATO alliance, Korean War intervention (1950-53), Vietnam War (1955-75), CIA covert operations supporting anti-communist governments worldwide."),
      ("What was the Cuban Missile Crisis and why is it significant?","Think: closest the world came to nuclear war","October 1962: US discovered Soviet nuclear missiles in Cuba (90 miles from Florida). 13-day standoff: Kennedy demanded removal; Khrushchev threatened war. Resolved: Soviets removed missiles; US secretly agreed not to invade Cuba and removed missiles from Turkey. Showed how nuclear brinkmanship risked catastrophic war."),
      ("How did the space race reflect Cold War competition?","Think: technological superiority as ideological proof","The US and USSR competed in space as a proxy for ideological superiority. Sputnik (1957 — first satellite) shocked Americans. Yuri Gagarin (1961 — first human in space) was a Soviet triumph. Apollo 11 (1969 — first Moon landing) was America's most important victory. Space race drove enormous technological innovation."),
      ("What caused the end of the Cold War?","Think: Soviet economic failure + Gorbachev's reforms + popular uprisings","(1) Soviet economy stagnating under military spending burden. (2) Gorbachev's reforms (glasnost — openness; perestroika — restructuring) unleashed political change. (3) Popular uprisings in Eastern Europe (1989) — Berlin Wall fell. (4) Soviet republics declared independence. USSR formally dissolved December 25, 1991."),
    ]),
    s("Contemporary world",[
      ("What is globalization? What are its benefits and challenges?","Think: increasing economic, cultural, and political interconnection","Globalization: the increasing integration of economies, cultures, and governments worldwide. Benefits: economic growth, technology spread, cultural exchange, reduced extreme poverty. Challenges: inequality between and within nations, cultural homogenization, environmental degradation, vulnerability to global financial crises and pandemics."),
      ("What was 9/11 and how did it change US foreign policy?","Think: September 11, 2001 terrorist attacks and the War on Terror","On September 11, 2001, al-Qaeda terrorists hijacked four planes, crashing two into the World Trade Center, one into the Pentagon, one into a Pennsylvania field. ~3,000 killed. Led to: US invasion of Afghanistan (2001), Iraq War (2003), Patriot Act expanding surveillance, creation of Homeland Security, debate about civil liberties vs. security."),
      ("What is the Israeli-Palestinian conflict?","Think: competing claims to the same land","Roots: After WWI, British controlled Palestine (promised land to both Jews and Arabs). 1947 UN partition plan. 1948 Israeli independence + Arab-Israeli war (Palestinians call it Nakba — catastrophe). Core issues: borders of a Palestinian state, status of Jerusalem, Palestinian refugees' right of return. One of the most complex and persistent conflicts in the world."),
      ("What are the United Nations' Sustainable Development Goals?","Think: 17 goals for 2030 addressing global challenges","Adopted 2015, 17 goals including: End poverty and hunger, Good health, Quality education, Gender equality, Clean water, Clean energy, Decent work, Reduced inequality, Sustainable cities, Climate action, Life below water, Peace and justice. A shared global framework addressing humanity's greatest challenges."),
    ]),
  ],
  [
    s("US History: Reconstruction to WWI",[
      ("What was Reconstruction? Why did it fail?","Think: rebuilding the South after Civil War, 1865-1877","Reconstruction: federal program to reintegrate Confederate states and protect freed Black Americans. Achievements: 13th Amendment (abolished slavery), 14th (equal protection), 15th (Black male suffrage), Black elected officials. Failure: withdrawal of federal troops (1877), rise of KKK, Black Codes, share-cropping replaced slavery economically."),
      ("What was the Gilded Age and what were its characteristics?","Think: rapid industrialization, extreme inequality, political corruption","1870s-1890s. Mark Twain's term for the glittering surface hiding inequality. Characterized by: rapid industrialization, rise of robber barons (Rockefeller, Carnegie, Morgan), extreme wealth inequality, political corruption (Tammany Hall), and a growing labor movement responding to exploitation."),
      ("What was the Progressive Era and what reforms did it produce?","Think: early 20th century reform movement responding to Gilded Age problems","1890s-1920s. Reformers responded to industrialization's problems. Achievements: Sherman Antitrust Act (broke up monopolies), Pure Food and Drug Act (FDA origins), 17th Amendment (direct election of senators), 19th Amendment (women's suffrage), child labor regulations, journalists exposed corruption (muckrakers like Upton Sinclair's The Jungle)."),
      ("What was the significance of the Spanish-American War (1898)?","Think: US emerged as an imperial power","US defeated Spain in four months. Gained: Puerto Rico, Guam, Philippines (purchased for $20 million). Cuba gained nominal independence but under US influence. Signaled US emergence as a global power and sparked debate about American imperialism — was it consistent with American values?"),
    ]),
    s("Economics and government",[
      ("What is the difference between capitalism, socialism, and communism?","Think: private ownership, mixed, state ownership","Capitalism: private ownership of means of production; profit motive; market sets prices. Socialism: mix — some public ownership, social safety net, government regulates key industries. Communism: state owns all means of production, aims for classless society. In practice, no pure forms exist — all economies are mixed."),
      ("What is the role of government in a mixed economy?","Think: providing public goods and correcting market failures","Government roles in mixed economies: provide public goods (defense, roads), regulate to prevent market failures (monopolies, pollution), social safety net (unemployment, healthcare), enforce contracts, stabilize economy (Federal Reserve). The proper extent of government's role is a central political debate."),
      ("What is supply and demand? How do they determine price?","Think: buyer behavior and seller behavior interact","Supply: quantity sellers will offer at each price (higher price → more supply). Demand: quantity buyers want at each price (higher price → less demand). Equilibrium: where supply equals demand, determining the market price. Shifts in supply or demand change the equilibrium price."),
      ("What is inflation and what causes it?","Think: general rise in the price level","Inflation: a general increase in prices across the economy, reducing purchasing power. Causes: (1) Too much money in circulation (monetary inflation). (2) Demand-pull: high demand exceeds supply. (3) Cost-push: production costs rise, passed to consumers. Central banks (Federal Reserve) control inflation mainly through interest rates."),
    ]),
    s("Civic participation",[
      ("What are the three branches of US government and their key powers?","Think: legislative, executive, judicial","Legislative (Congress): makes laws, controls budget, declares war. Executive (President): enforces laws, commands military, appoints officials, vetoes legislation. Judicial (Supreme Court and federal courts): interprets laws and Constitution, can declare laws unconstitutional (judicial review)."),
      ("What is judicial review and where does it come from?","Think: Marbury v. Madison (1803)","Judicial review: the Supreme Court's power to declare laws unconstitutional. Established in Marbury v. Madison (1803) — Chief Justice Marshall ruled a law unconstitutional for the first time, establishing this critical check on legislative and executive power. Not explicitly in the Constitution — implied."),
      ("How does a bill become a law?","Think: committee, floor vote, conference, presidential signature","(1) Introduced in House or Senate. (2) Referred to committee for review. (3) Debated and amended on the floor. (4) Voted on — must pass both chambers in identical form. (5) Conference committee if versions differ. (6) Sent to President: sign (law), veto (returned to Congress), or pocket veto. Congress can override veto with two-thirds majority."),
      ("What are three ways citizens can participate in American democracy beyond voting?","Think: forms of civic engagement","Contact elected representatives (letters, calls, meetings), attend local government meetings (city council, school board), volunteer for campaigns or political organizations, participate in peaceful protest or civil disobedience, serve on a jury, run for local office, vote in local elections (where individual votes have the most impact)."),
    ]),
    s("Geography and identity",[
      ("What is the difference between a nation, a state, and a nation-state?","Think: cultural group, political entity, and their overlap","Nation: a group sharing culture, language, history, and sense of collective identity (the Kurdish nation, the Palestinian nation). State: a political entity with defined territory, government, and sovereignty. Nation-state: when a nation and state coincide — most nations are not perfectly aligned with states (many stateless nations; many multi-national states)."),
      ("How does geography influence political and economic power?","Think: location, resources, and physical features","Landlocked countries struggle with trade. Coastal nations with natural harbors dominate trade. Nations with oil dominate energy markets. Mountains, rivers, and deserts form natural boundaries. Physical geography influenced where civilizations formed and which grew powerful — though technology now reduces but does not eliminate geographic advantages."),
      ("What is cultural identity and how does it interact with national identity?","Think: layers of identity that may or may not align with national boundaries","Cultural identity: membership in cultural, ethnic, religious, or linguistic groups. National identity: citizenship and belonging to a political state. These often align but can conflict — minority cultures within a state may feel torn between cultural and national identity. Immigration and globalization create new layers of hybrid identity."),
      ("What are the push and pull factors of migration?","Think: what drives people away vs. what attracts them","Push factors: conditions driving people to leave (poverty, violence, natural disasters, political persecution, climate change). Pull factors: conditions attracting people to a destination (economic opportunity, safety, family networks, political freedom). Migration is rarely purely voluntary or purely forced — usually a mix of push and pull."),
    ]),
  ],
  [
    s("Critical thinking about history",[
      ("What is historical perspective-taking?","Think: understanding past actors in their historical context","Historical perspective-taking: understanding why historical actors thought and behaved as they did within their own context — without applying modern values uncritically. Avoids presentism (judging the past by modern standards). Does not mean approving of historical actions, but understanding their context and logic."),
      ("What is historical bias in primary sources?","Think: all sources have a perspective","All primary sources reflect the perspective, position, and purpose of their creator. A plantation owner's diary reflects very different reality than an enslaved person's testimony. Historians use multiple sources to triangulate reality and understand whose perspectives are missing."),
      ("What is the difference between history and historiography?","Think: the past vs. how historians write about the past","History: what actually happened in the past. Historiography: the study of how history has been written — how historians' methods, questions, and perspectives have changed over time. Example: historians once ignored women's history; women's history became a major field from the 1960s onward."),
      ("How do historians use evidence to construct historical arguments?","Think: source analysis, corroboration, contextualization, close reading","Historians: analyze sources (who created them, why, when), corroborate claims across multiple independent sources, contextualize (place source in historical context), read closely for explicit and implicit meaning. Historical arguments are interpretations supported by evidence — not simply facts."),
    ]),
  ],
]
print("G8 history complete")

P[8]["cs"] = [
  [
    s("Object-oriented programming",[
      ("What is object-oriented programming (OOP)?","Think: organizing code around objects with data and methods","OOP: a programming paradigm organizing code around objects — entities combining data (attributes) and behavior (methods). Real-world modeling: a Dog object has attributes (name, breed, age) and methods (bark(), fetch()). Java, Python, and C++ support OOP."),
      ("What is a class? What is an object (instance)?","Think: blueprint vs. specific thing made from blueprint","Class: the blueprint or template defining attributes and methods. Object (instance): a specific thing created from the class. Example: Dog is the class; myDog = Dog('Rex', 'Labrador', 3) creates an instance called myDog."),
      ("What is the difference between an attribute and a method?","Think: data vs. behavior","Attribute: data stored in an object (myDog.name = 'Rex', myDog.age = 3). Method: a function belonging to the object that defines its behavior (myDog.bark() prints 'Woof'). Attributes store state; methods define behavior."),
      ("What is inheritance in OOP?","Think: child class inherits attributes and methods from parent class","Inheritance: a child class automatically has all attributes and methods of its parent class, and can add or override them. Example: class GoldenRetriever(Dog): — GoldenRetriever inherits bark() and fetch() but can add its own methods. Promotes code reuse."),
    ]),
    s("Sorting and searching",[
      ("What is the difference between linear search and binary search?","Think: sequential vs. divide and conquer","Linear search: check each element one by one — works on unsorted data — O(n) time. Binary search: divide sorted list in half repeatedly — much faster — O(log n) time. Binary search requires the list to be sorted first."),
      ("What is Big O notation and what does O(n) vs O(n^2) mean?","Think: how time scales with input size","Big O: describes how an algorithm's time grows with input size n. O(n): linear — doubles if input doubles. O(n^2): quadratic — quadruples if input doubles (common in nested loops). O(log n): logarithmic — very efficient (binary search). O(1): constant — same time regardless of input size."),
      ("Describe the bubble sort algorithm.","Think: compare adjacent elements, swap if out of order, repeat","Bubble sort: repeatedly step through the list, compare adjacent elements, and swap if they are in the wrong order. Pass through the list until no swaps are needed. Simple but inefficient: O(n^2) — not practical for large datasets."),
      ("Why does algorithm efficiency matter?","Think: small inputs are forgiving; large inputs reveal inefficiency","For small inputs, most algorithms are fast enough. For large inputs (millions of records), efficiency is critical. A database with 1 million records searched linearly takes 1 million operations; binary search takes only about 20. Efficient algorithms are essential at scale."),
    ]),
    s("Data structures",[
      ("What is a data structure? Name three common ones.","Think: organized way to store and access data","Data structure: a way to organize data for efficient access and modification. Array/List: ordered, indexed. Dictionary/HashMap: key-value pairs. Stack: LIFO (last in, first out). Queue: FIFO (first in, first out). Tree: hierarchical relationships. Each optimized for different operations."),
      ("What is the difference between a list and a dictionary in Python?","Think: ordered indexed vs. key-value pairs","List: ordered, accessed by numeric index (list[0]). Dictionary: accessed by key (dict['name']) — unordered (in older Python), fast lookup by key. Use a list when order matters; use a dictionary when you need to look things up by meaningful name."),
      ("What is a stack and what is the LIFO principle?","Think: plates in a cafeteria","Stack: a data structure where items are added and removed from the same end (top). LIFO: Last In, First Out — the last item added is the first removed. Used in: function call stacks, undo operations, browser history (back button). Operations: push (add), pop (remove)."),
      ("What is a queue and what is the FIFO principle?","Think: line at a store","Queue: items added at one end (back) and removed from the other (front). FIFO: First In, First Out — the first item added is the first removed. Used in: print queues, task scheduling, customer service systems. Operations: enqueue (add), dequeue (remove)."),
    ]),
    s("APIs and the internet",[
      ("What is an API? How is it used?","Think: application programming interface — a contract for software communication","API (Application Programming Interface): a set of rules allowing software programs to communicate. Example: a weather app uses a weather service's API to get data. APIs allow apps to use others' data and services without knowing their internal code. REST APIs use HTTP requests."),
      ("What happens when you type a URL and hit Enter?","Think: DNS lookup, HTTP request, server response, rendering","(1) Browser looks up the domain name via DNS (translates to IP address). (2) Browser sends an HTTP(S) request to the server. (3) Server processes request and sends back HTML, CSS, and JavaScript. (4) Browser parses and renders the page."),
      ("What is the difference between a client and a server?","Think: requester vs. responder","Client: a device or program that requests services or resources (your browser). Server: a program that provides services or resources in response to requests (web server hosting a website). The client-server model underlies most of the internet."),
      ("What is open source software?","Think: freely available source code that anyone can use and modify","Open source: software whose source code is publicly available — anyone can view, use, modify, and distribute it. Examples: Linux, Firefox, Python. Contrasts with proprietary (closed source) software where code is secret. Open source drives innovation through collaboration."),
    ]),
    s("Ethics in computing",[
      ("What is algorithmic bias? Give one example.","Think: algorithms can reflect and amplify human biases","Algorithmic bias: when an algorithm produces systematically unfair results for certain groups, often because training data reflects existing biases. Example: facial recognition systems trained mostly on light-skinned faces have higher error rates for darker-skinned faces — with real consequences if used for policing."),
      ("What is data privacy and why is it an important issue?","Think: control over personal information","Data privacy: individuals' right to control their own personal information — who collects it, how it is used, and who can access it. Important because: data can reveal sensitive personal information, be used to manipulate behavior (targeted advertising), be sold without consent, or be breached (identity theft)."),
      ("What is the digital divide and why does it matter?","Think: unequal access to technology and the internet","Digital divide: the gap between those who have access to modern information and communication technology and those who do not. Matters because: access to education, healthcare, economic opportunity, and civic participation increasingly requires internet access — lack of access deepens existing inequalities."),
      ("Who is responsible when an autonomous system makes a harmful decision?","Think: complex question of liability and accountability in AI","This is an active ethical and legal debate. Candidates: the programmer who wrote the code, the company that deployed the system, the user who deployed it in a specific context, or the person who was harmed (if they accepted risk). Responsible AI design requires considering who is accountable before deploying systems."),
    ]),
  ],
  [
    s("Machine learning basics",[
      ("What is machine learning?","Think: systems that learn from data rather than explicit programming","Machine learning: a subfield of AI where systems improve at tasks through experience (training data) rather than being explicitly programmed with rules. The system finds patterns in data and uses them to make predictions or decisions on new data."),
      ("What is the difference between supervised and unsupervised learning?","Think: labeled vs. unlabeled data","Supervised: training data includes correct answers (labels) — the model learns to predict labels for new data (spam detection, image classification). Unsupervised: training data has no labels — the model finds patterns or clusters on its own (customer segmentation, recommendation systems)."),
      ("What is overfitting and why is it a problem?","Think: model memorizes training data but fails on new data","Overfitting: the model learns the training data too specifically — including its noise — and fails to generalize to new data. Like a student who memorizes answers without understanding and fails when questions are slightly different. Prevented by: more training data, simpler models, regularization."),
      ("Give two examples of machine learning in everyday life.","Think: systems you interact with that use ML","Spam filters (classify email as spam/not spam). Recommendation systems (Netflix, Spotify, Amazon). Voice assistants (recognize speech). Fraud detection (flag unusual credit card transactions). Medical image analysis (detect cancer in X-rays). Social media feeds (decide what to show you)."),
    ]),
    s("Creative computing",[
      ("What is generative AI and how does it work?","Think: AI that creates new content","Generative AI: AI systems that create new content (text, images, audio, video) by learning patterns from large datasets. Large Language Models (like GPT) predict the most likely next word repeatedly to generate text. Image generators create images by learning to reconstruct images from noise."),
      ("What are some creative uses of computing?","Think: digital art, music generation, game design","Digital art and generative art, music composition (algorithmic music), game development and level design, film visual effects and animation, interactive narrative and storytelling, architectural design, fashion design. Computing is a creative medium as much as a practical one."),
      ("What is computational creativity?","Think: can computers be creative?","Computational creativity: the study of whether and how computers can exhibit creative behavior — producing novel, valuable, and surprising outputs. Ongoing debate: is AI creativity genuinely creative or sophisticated pattern recombination? Does the distinction matter? The field raises fundamental questions about the nature of creativity."),
      ("What is version control and why do developers use it?","Think: tracking changes to code over time","Version control (e.g., Git): a system tracking every change made to code over time. Allows: reverting to earlier versions, seeing who made which changes, working on different features simultaneously (branching), merging changes from multiple developers. Essential for team software development."),
    ]),
    s("Networks and protocols",[
      ("What is a network protocol?","Think: agreed-upon rules for communication between devices","Protocol: a standardized set of rules for data communication. Examples: HTTP (web pages), HTTPS (secure web), SMTP (email), FTP (file transfer), TCP/IP (foundational internet protocol). Protocols ensure devices from different manufacturers can communicate."),
      ("What is the difference between TCP and UDP?","Think: reliable delivery vs. fast delivery","TCP (Transmission Control Protocol): reliable — confirms each packet is received, resends if dropped. Used for: web browsing, email (accuracy critical). UDP (User Datagram Protocol): fast, no confirmation — packets can be lost. Used for: video streaming, gaming, video calls (speed more important than perfect accuracy)."),
      ("What is a firewall and what does it do?","Think: security barrier between networks","A firewall: a security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. Acts as a gatekeeper — blocks unauthorized access while allowing legitimate traffic. Can be hardware, software, or both."),
      ("What is the difference between the internet and the World Wide Web?","Think: infrastructure vs. service running on it","Internet: the global network of connected computers and devices (physical infrastructure — cables, routers, protocols). World Wide Web: one service running on the internet — websites and web pages connected by hyperlinks, accessed via browsers using HTTP. Email and file transfers also use the internet but are not the Web."),
    ]),
    s("Software development process",[
      ("What is the software development life cycle (SDLC)?","Think: phases of creating software","SDLC phases: (1) Requirements gathering (what should the software do?). (2) Design (architecture, database, UI). (3) Implementation (coding). (4) Testing. (5) Deployment. (6) Maintenance and updates. Most modern teams use Agile (iterative) rather than waterfall (sequential) approaches."),
      ("What is Agile development?","Think: iterative, flexible development in short cycles","Agile: an iterative approach to software development working in short cycles (sprints, typically 2 weeks). Each sprint produces working software. Team adapts based on feedback. Contrasts with waterfall (plan everything first). Agile is the dominant methodology in industry today."),
      ("What is testing in software development?","Think: verifying software does what it should","Types: Unit testing (testing individual functions). Integration testing (testing how components work together). User acceptance testing (real users test the product). Automated testing (code that tests other code — runs with every change). Good testing prevents bugs from reaching users."),
      ("What is the difference between a bug and a feature?","Think: unintended behavior vs. intended behavior","Bug: unintended behavior that causes errors or incorrect results. Feature: intended functionality. The line can blur — sometimes bugs become features (serendipitous discovery of unexpected useful behavior). In software development, the question is always: is this what we intended?"),
    ]),
  ],
]
print("G8 CS complete")

P[8]["health"] = [
  [
    s("Disease prevention",[
      ("What is the difference between infectious and noninfectious disease?","Think: caused by pathogens vs. caused by other factors","Infectious: caused by pathogens (bacteria, viruses, fungi, parasites) and can spread from person to person. Noninfectious: not caused by pathogens and not contagious (heart disease, diabetes, cancer, asthma). Most chronic diseases are noninfectious."),
      ("What are vaccines and how do they work?","Think: training the immune system with a safe version","Vaccines introduce a weakened, killed, or partial version of a pathogen (or instructions to make a protein from it). The immune system responds by creating antibodies and memory cells. If exposed to the real pathogen later, the immune system responds rapidly and effectively."),
      ("What is herd immunity and why does it matter?","Think: enough people immune to protect those who cannot be vaccinated","Herd immunity: when a sufficiently large percentage of a population is immune to a disease (through vaccination or prior infection), the disease cannot spread easily — protecting those who cannot be vaccinated (newborns, immunocompromised individuals). Required percentage varies by disease."),
      ("What are the major ways infectious diseases spread? Name four.","Think: routes of transmission","(1) Respiratory droplets (flu, COVID-19 — coughing, sneezing). (2) Direct contact (skin infections, STIs). (3) Fecal-oral route (E. coli — contaminated food or water). (4) Vector-borne (malaria — mosquito bite). (5) Bloodborne (HIV, hepatitis B — blood or bodily fluid contact)."),
    ]),
    s("Mental health treatment",[
      ("What are the main approaches to treating mental health conditions?","Think: therapy, medication, lifestyle, community","(1) Psychotherapy (talk therapy): CBT, DBT, psychodynamic. (2) Medication: antidepressants, anti-anxiety, mood stabilizers. (3) Lifestyle: exercise, sleep, nutrition, stress reduction. (4) Social support and community. Most conditions respond best to a combination of approaches."),
      ("What is Cognitive Behavioral Therapy (CBT)?","Think: changing unhelpful thought patterns","CBT: evidence-based therapy identifying and changing unhelpful thought patterns and behaviors. Based on the idea that thoughts, feelings, and behaviors are interconnected. Teaches: identifying cognitive distortions (all-or-nothing thinking, catastrophizing), challenging them, and replacing them with more balanced thoughts."),
      ("When should someone seek professional help for mental health?","Think: when it impairs daily function or persists","Seek help when: symptoms last more than two weeks, significantly affect school, work, relationships, or daily activities, involve thoughts of self-harm or harm to others, or feel impossible to manage alone. Early intervention improves outcomes. Mental health professionals include therapists, counselors, psychologists, and psychiatrists."),
      ("What is the difference between a psychologist, psychiatrist, and counselor?","Think: education, focus, and prescribing ability","Psychiatrist: medical doctor (MD) who diagnoses and can prescribe medication. Psychologist: doctoral-level (PhD/PsyD) trained in therapy and psychological assessment — usually cannot prescribe. Counselor/Therapist: master's-level professional providing talk therapy. Often work together."),
    ]),
    s("Substance abuse",[
      ("What is addiction? What makes it different from dependence?","Think: compulsive use despite harm vs. physical adaptation","Addiction: compulsive substance use despite negative consequences — a brain disorder affecting the reward, motivation, and memory circuits. Dependence: the body adapts to a substance and withdrawal symptoms occur without it. Can have dependence without addiction (pain medication); addiction usually includes dependence."),
      ("How does addiction affect the brain?","Think: hijacking the reward system","Substances flood the brain with dopamine (pleasure chemical), far exceeding natural rewards. The brain adapts by reducing dopamine receptors — making everything feel less pleasurable. This creates craving for the substance as the only source of pleasure and drives compulsive use."),
      ("What are the signs of substance abuse?","Think: behavioral, physical, and social changes","Using more than intended, failed attempts to stop, spending lots of time getting/using/recovering, cravings, failing to meet obligations, giving up activities, continuing despite harm to health and relationships, withdrawal symptoms when not using."),
      ("What treatment options exist for substance abuse?","Think: medical, behavioral, and community support","(1) Medically assisted detox (supervised withdrawal). (2) Medication-assisted treatment (methadone, buprenorphine for opioids). (3) Behavioral therapy (CBT, motivational interviewing). (4) Support groups (AA, NA). (5) Residential treatment. (6) Long-term recovery support. Relapse is common and should be seen as part of recovery, not failure."),
    ]),
    s("Reproductive health",[
      ("What is abstinence and why is it considered the most effective prevention?","Think: complete avoidance of sexual activity","Abstinence: choosing not to engage in sexual activity. It is the only method that is 100% effective at preventing pregnancy and STIs when consistently practiced. It is one option; comprehensive health education covers multiple methods of prevention."),
      ("What are common STIs and how are they prevented?","Think: sexually transmitted infections","Common STIs: chlamydia, gonorrhea, syphilis, herpes, HPV, HIV. Prevention: abstinence (most effective), consistent condom use (reduces but does not eliminate risk for most STIs), HPV vaccination, regular testing, mutual monogamy with a tested partner, PrEP (for HIV prevention)."),
      ("What is the importance of regular health screenings?","Think: early detection improves outcomes for many conditions","Many diseases are most treatable when caught early — before symptoms appear. Important screenings include: annual physical, dental checkups, eye exams, and age-appropriate cancer screenings (Pap smear, mammogram, colonoscopy). Normalize regular medical care as health maintenance, not just sick visits."),
      ("What is consent and how does it apply to healthy relationships?","Think: freely given, reversible, informed, enthusiastic, specific","Consent for any physical intimacy must be: freely given (no coercion), reversible (can be withdrawn at any time), informed (both parties understand what they are agreeing to), enthusiastic (not just absence of no), and specific (agreeing to one thing is not agreeing to everything). Legal definitions of consent vary by state."),
    ]),
    s("Healthy aging and habits",[
      ("What habits established in adolescence most affect long-term health?","Think: decisions made young have lasting effects","(1) Regular physical activity — reduces lifelong disease risk. (2) Healthy eating — prevents obesity, diabetes. (3) Not starting smoking — nearly impossible to develop lung disease from never smoking. (4) Wearing sunscreen — UV damage accumulates over lifetime. (5) Healthy sleep habits. (6) Not starting substance use — adolescent brain more vulnerable to addiction."),
      ("What is the relationship between stress and physical health?","Think: chronic stress has measurable biological effects","Chronic stress elevates cortisol, which suppresses immune function, increases inflammation, raises blood pressure, disrupts sleep, and impairs memory and decision-making. The mind-body connection is well-established — mental health directly affects physical health."),
      ("What is body image and how does media affect it?","Think: perception of one's own body vs. idealized media images","Body image: how you see and feel about your own body. Media presents heavily edited, narrowly defined ideals of beauty. Research links heavy media consumption to negative body image, especially for girls and young women — associated with disordered eating and low self-esteem. Social media amplifies this effect."),
      ("What is a healthy relationship with food?","Think: nourishment vs. moralization of eating","A healthy relationship with food: eating for nourishment and enjoyment, without excessive guilt or restriction. No foods are inherently good or bad — variety, moderation, and balance. Warning signs of disordered eating: obsessive thinking about food, restricting, bingeing, purging, excessive exercise to compensate for eating."),
    ]),
  ],
  [
    s("Community health",[
      ("What is public health?","Think: population-level health promotion and disease prevention","Public health: the science and practice of protecting and improving the health of communities through education, policy, research, and health services. Focuses on populations rather than individuals. Examples: vaccination programs, water fluoridation, food safety regulations, anti-tobacco policies."),
      ("What is the difference between primary, secondary, and tertiary prevention?","Think: before, during, and after","Primary: prevent disease before it occurs (vaccination, education). Secondary: early detection and treatment (cancer screenings, HIV testing). Tertiary: managing existing disease to prevent further decline (cardiac rehab, diabetes management). All three levels are necessary for comprehensive public health."),
      ("How do social determinants of health affect wellness?","Think: conditions of daily life shape health","Social determinants: non-medical factors influencing health — income, education, neighborhood, social support, access to healthy food, safe housing. These factors account for 30-55% of health outcomes. A person living in poverty in a food desert with high stress has dramatically worse health prospects than someone with opposite conditions."),
      ("What is health equity?","Think: everyone having a fair opportunity to be as healthy as possible","Health equity: the idea that everyone should have a fair and just opportunity to be as healthy as possible — requiring removing obstacles created by discrimination, poverty, and lack of access. Health equity differs from health equality (giving everyone the same) — equity gives people what they need to achieve equal outcomes."),
    ]),
    s("Self-advocacy in health",[
      ("What does it mean to be a health literate person?","Think: ability to obtain, understand, and use health information","Health literacy: the ability to find, understand, and use health information to make good decisions. Includes: reading medication labels, understanding medical instructions, researching health conditions, communicating symptoms clearly to providers, and critically evaluating health claims online."),
      ("What questions should you ask a healthcare provider at an appointment?","Think: informed patient participation","Key questions: What is my diagnosis? What are my treatment options? What are the benefits and risks of each? What happens if I wait? Are there lifestyle changes that would help? When should I follow up? What symptoms should prompt immediate care? Informed patients get better care."),
      ("How do you evaluate health information found online?","Think: look for credentials, currency, and lack of bias","Check: Who wrote it? (Credentials?) Who published it? (Reputable organization like Mayo Clinic, CDC, NIH?) When? (Current?) Does it cite sources? Is it trying to sell something? Does it acknowledge complexity? Avoid: anonymous sources, miracle claims, sites without credentials."),
      ("What is the difference between a symptom and a sign?","Think: subjective experience vs. objective observation","Symptom: what the patient experiences and reports (pain, nausea, fatigue — only the patient knows). Sign: what can be objectively measured or observed by others (fever measured at 102 F, rash visible, elevated blood pressure). Both are important for diagnosis."),
    ]),
    s("Physical education skills",[
      ("What is the overload principle in fitness training?","Think: stress beyond current capacity leads to adaptation","Overload principle: to improve fitness, you must exercise beyond your current capacity. The body adapts to stress and becomes stronger, faster, or more enduring. Once adapted, you must progressively overload again (progressive overload) to continue improving."),
      ("What is the specificity principle?","Think: train for the specific fitness component you want to improve","Specificity: training adaptations are specific to the type of exercise performed. Running improves running, not swimming. Strength training builds strength, not cardiovascular endurance. Training programs must specifically target the desired fitness component."),
      ("What is rest and recovery and why is it as important as training?","Think: adaptation happens during rest, not during exercise","The body gets stronger during recovery, not during exercise. Training breaks down tissue; recovery builds it back stronger. Inadequate rest leads to overtraining — decreased performance, increased injury risk, and burnout. Sleep, active recovery, and rest days are essential training components."),
      ("What are the long-term health benefits of maintaining physical fitness throughout life?","Think: reduced disease risk + quality of life + longevity","Regular lifetime exercise: reduces risk of heart disease, type 2 diabetes, several cancers, osteoporosis, cognitive decline, and depression. Maintains mobility and independence in older age. Extends healthy life expectancy. The single most impactful behavioral health intervention available."),
    ]),
    s("First aid and emergency response",[
      ("What is the purpose of CPR and when should it be performed?","Think: maintain blood flow when heart stops","CPR (Cardiopulmonary Resuscitation): performed when someone's heart has stopped (cardiac arrest) and they are not breathing. Chest compressions maintain blood flow to the brain. Early CPR dramatically increases survival — brain damage begins within 4-6 minutes without oxygen. Call 911 first, then begin CPR."),
      ("How does an AED work?","Think: automated external defibrillator analyzes heart rhythm and delivers shock","AED (Automated External Defibrillator): analyzes the heart's rhythm and delivers an electric shock if needed to restore normal rhythm. Designed for non-medical users — voice prompts guide the user. AEDs are in many public places. Using an AED doubles or triples survival rates from cardiac arrest."),
      ("What is the universal sign of choking and how do you respond?","Think: hands to throat; cannot speak or cough","Universal sign: hands clutched to the throat. If the person cannot speak, cough, or breathe: perform the Heimlich maneuver (abdominal thrusts). Stand behind the person, make a fist above the navel, grab with other hand, give quick inward-upward thrusts. Repeat until object is expelled or person loses consciousness."),
      ("When should you call 911 vs. other emergency resources?","Think: life-threatening vs. urgent vs. non-emergency","Call 911: life-threatening emergencies (chest pain, difficulty breathing, unconsciousness, severe bleeding, suspected stroke, fire, serious accident). Urgent care or doctor: non-life-threatening but time-sensitive (minor broken bone, high fever, deep cut needing stitches). Primary care: routine issues. Poison Control: 1-800-222-1222."),
    ]),
  ],
]
print("G8 health complete")

# ─── GRADE 9 ───
P[9] = {"math":[], "science":[], "ela":[], "history":[], "cs":[], "health":[]}

P[9]["math"] = [
  # U1: Algebra fundamentals
  [
    s("Variables and expressions",[
      ("Simplify: 2(3x - 4) - 3(x + 2)","Think: distribute then combine like terms","6x - 8 - 3x - 6 = 3x - 14."),
      ("Evaluate: -2a^2 + 3b for a = -3, b = 4","Think: substitute carefully, watch signs","-2(9) + 3(4) = -18 + 12 = -6."),
      ("What is a coefficient? Identify in: 5x^3 - 7x + 2","Think: the number multiplying the variable","5 is the coefficient of x^3; -7 is the coefficient of x; 2 is the constant term."),
      ("Factor out the GCF: 12x^3 - 8x^2 + 4x","Think: largest factor common to all terms","GCF = 4x. Result: 4x(3x^2 - 2x + 1)."),
    ]),
    s("Solving linear equations",[
      ("Solve: 4(2x - 1) = 3x + 11","Think: distribute, collect variables on one side","8x - 4 = 3x + 11 → 5x = 15 → x = 3."),
      ("Solve: (x+3)/2 - (x-1)/4 = 2","Think: multiply through by LCD = 4","2(x+3) - (x-1) = 8 → 2x+6-x+1 = 8 → x+7 = 8 → x = 1."),
      ("A number increased by 15% equals 92. Find the number.","Think: n × 1.15 = 92","n = 92/1.15 = 80."),
      ("Two friends share $240 in ratio 3:5. How much does each get?","Think: 3+5=8 parts; each part = $30","3 parts = $90; 5 parts = $150."),
    ]),
    s("Inequalities and absolute value",[
      ("Solve and graph: -3x + 7 > 22","Think: subtract 7, divide by -3, flip","x < -5. Open circle at -5, arrow left."),
      ("Solve the compound inequality: -4 < 2x + 2 ≤ 10","Think: subtract 2, then divide by 2","-3 < x ≤ 4. Open circle at -3, closed at 4."),
      ("Solve: |2x - 5| = 9","Think: two cases: inside = 9 or inside = -9","2x - 5 = 9 → x = 7; or 2x - 5 = -9 → x = -2."),
      ("Solve: |x + 3| < 7","Think: -7 < x + 3 < 7","-10 < x < 4."),
    ]),
    s("Systems of linear equations",[
      ("Solve by graphing: y = x + 2 and y = -x + 4","Think: find intersection point","Both equations: x + 2 = -x + 4 → 2x = 2 → x = 1, y = 3. Point: (1,3)."),
      ("Solve by substitution: 3x - y = 7 and y = 2x - 3","Think: substitute y","3x - (2x-3) = 7 → x + 3 = 7 → x = 4, y = 5."),
      ("Solve by elimination: 2x + 5y = 16 and 3x - 5y = 9","Think: add to eliminate y","5x = 25 → x = 5; y = (16-10)/5 = 6/5."),
      ("A boat travels 60 mi downstream in 3 hrs and 60 mi upstream in 5 hrs. Find boat speed and current speed.","Think: d = rt; downstream: b+c=20; upstream: b-c=12","b+c=20 and b-c=12. Adding: 2b=32 → b=16 mph; c=4 mph."),
    ]),
    s("Functions and relations",[
      ("What is function notation? Evaluate f(x) = 3x^2 - 2 at x = -2.","Think: substitute x = -2","f(-2) = 3(4) - 2 = 10."),
      ("Find the domain: f(x) = sqrt(x - 3)","Think: radicand must be ≥ 0","x - 3 ≥ 0 → x ≥ 3. Domain: [3, ∞)."),
      ("What does it mean for a function to be one-to-one?","Think: each output corresponds to exactly one input","One-to-one: no two inputs map to the same output. Passes the horizontal line test. Required for the function to have an inverse."),
      ("Find the inverse of f(x) = 2x + 6","Think: swap x and y, solve for y","y = 2x + 6 → x = 2y + 6 → y = (x-6)/2. Inverse: f^-1(x) = (x-6)/2."),
    ]),
    s("Polynomials and factoring",[
      ("Factor: x^2 - 9","Think: difference of squares","(x+3)(x-3)."),
      ("Factor completely: 2x^3 - 8x","Think: factor out GCF first","2x(x^2 - 4) = 2x(x+2)(x-2)."),
      ("Factor: x^2 + 7x + 12","Think: find two numbers multiplying to 12, adding to 7","(x+3)(x+4). Check: 3×4=12, 3+4=7."),
      ("Factor: 3x^2 - 7x - 6","Think: AC method — 3×(-6)=-18; find factors of -18 adding to -7","Factors: -9 and 2. Rewrite: 3x^2 - 9x + 2x - 6 = 3x(x-3) + 2(x-3) = (3x+2)(x-3)."),
    ]),
  ],
  # U2: Geometry
  [
    s("Proofs and logic",[
      ("What is a mathematical proof?","Think: logical sequence from given facts to a conclusion","A proof is a logical sequence of statements, each justified by a definition, postulate, or previously proven theorem, leading to a conclusion. Proofs establish that something is always true, not just in specific cases."),
      ("What is the difference between inductive and deductive reasoning?","Think: pattern observation vs. logical guarantee","Inductive: observing specific cases to reach a general conclusion (may be wrong). Deductive: applying general rules to reach a specific conclusion (guaranteed if premises are true). Proofs use deductive reasoning."),
      ("What is a conditional statement? What is its converse?","Think: if-then; reverse hypothesis and conclusion","Conditional: If p, then q. Converse: If q, then p. The converse of a true statement is not necessarily true. Contrapositive (If not q, then not p) always has the same truth value as the original."),
      ("In a two-column proof, what goes in each column?","Think: statements on the left; justifications on the right","Left column: statements (mathematical equations or geometric facts). Right column: reasons (definitions, postulates, theorems, or previously proven statements) that justify each statement."),
    ]),
    s("Triangles",[
      ("What are the triangle congruence shortcuts?","Think: SSS, SAS, ASA, AAS, HL","SSS (3 sides), SAS (2 sides and included angle), ASA (2 angles and included side), AAS (2 angles and non-included side), HL (hypotenuse-leg, right triangles only). If any of these conditions are met, triangles are congruent."),
      ("What is the Triangle Inequality Theorem?","Think: the sum of any two sides must exceed the third","Any two sides of a triangle must sum to more than the third side. Check all three combinations. If any fails, the triangle is impossible."),
      ("Find the missing angle of a triangle with angles 47° and 83°.","Think: angles sum to 180°","180 - 47 - 83 = 50°."),
      ("What is an isosceles triangle? State the isosceles triangle theorem.","Think: two equal sides; base angles are equal","Isosceles: at least two equal sides. Theorem: the base angles (angles opposite the equal sides) are equal. Converse: if two angles are equal, the opposite sides are equal."),
    ]),
    s("Quadrilaterals and polygons",[
      ("Name five types of quadrilaterals and one defining property of each.","Think: square, rectangle, rhombus, parallelogram, trapezoid","Parallelogram: opposite sides parallel. Rectangle: all right angles. Rhombus: all sides equal. Square: all sides equal and all right angles. Trapezoid: exactly one pair of parallel sides."),
      ("What properties do all parallelograms share?","Think: sides, angles, diagonals","Opposite sides are parallel and equal. Opposite angles are equal. Consecutive angles are supplementary. Diagonals bisect each other."),
      ("Find the sum of interior angles of a heptagon (7 sides).","Think: (n-2) × 180","(7-2) × 180 = 5 × 180 = 900°."),
      ("What is the measure of each interior angle of a regular hexagon?","Think: sum / number of sides","Sum = (6-2)×180 = 720°. Each angle = 720/6 = 120°."),
    ]),
    s("Circles",[
      ("What is the relationship between inscribed angle and central angle?","Think: inscribed angle = half the central angle","An inscribed angle is half the central angle that subtends the same arc. If the central angle is 80°, the inscribed angle subtending the same arc is 40°."),
      ("A chord 8 cm long is 3 cm from the center of a circle. Find the radius.","Think: chord + perpendicular + radius forms right triangle","Half chord = 4 cm; distance from center = 3 cm. r^2 = 4^2 + 3^2 = 25. r = 5 cm."),
      ("Two tangents from an external point form an angle of 70°. Find the arc between them.","Think: angle = (far arc - near arc)/2; far + near = 360°","Let far arc = x. Near = 360 - x. 70 = (x - (360-x))/2 → 140 = 2x - 360 → x = 250°. Near arc = 110°."),
      ("What is a tangent to a circle? State the key theorem about tangents.","Think: line touching at exactly one point; perpendicular to radius","Tangent: a line touching a circle at exactly one point. Theorem: a tangent line is perpendicular to the radius drawn to the point of tangency."),
    ]),
    s("Area and volume",[
      ("A sector has radius 10 cm and central angle 72°. Find its area.","Think: fraction of full circle area","Fraction = 72/360 = 1/5. Area = (1/5) × pi × 100 = 20pi ≈ 62.8 cm^2."),
      ("Find the lateral surface area of a cone with radius 5 and slant height 13.","Think: LSA = pi × r × l","pi × 5 × 13 = 65pi ≈ 204.2 square units."),
      ("A sphere and a cylinder have the same radius r and the cylinder's height equals 2r. Compare their volumes.","Think: V_sphere = (4/3)pi r^3; V_cyl = pi r^2 × 2r = 2pi r^3","V_sphere / V_cyl = (4/3)/2 = 2/3. The sphere's volume is 2/3 of the cylinder's."),
      ("How does volume scale when linear dimensions are doubled?","Think: volume scales as cube of scale factor","If all linear dimensions are doubled, volume increases by 2^3 = 8 times. Surface area increases by 2^2 = 4 times."),
    ]),
  ],
  # U3: Statistics and Probability
  [
    s("Descriptive statistics",[
      ("What is the five-number summary?","Think: min, Q1, median, Q3, max","Minimum, First Quartile (Q1 = 25th percentile), Median (Q2 = 50th), Third Quartile (Q3 = 75th), Maximum. Together they describe the center and spread of a dataset."),
      ("Dataset: 5,8,9,10,12,15,18,20. Find Q1, Q3, and IQR.","Think: split at median; Q1 and Q3 are medians of halves","Median splits at 10 and 12. Q1 = median of 5,8,9,10 = 8.5. Q3 = median of 12,15,18,20 = 16.5. IQR = 16.5 - 8.5 = 8."),
      ("How do you identify outliers using the IQR method?","Think: more than 1.5 × IQR beyond Q1 or Q3","Lower fence = Q1 - 1.5×IQR. Upper fence = Q3 + 1.5×IQR. Any value outside these fences is an outlier."),
      ("What is standard deviation? What does a larger standard deviation indicate?","Think: average distance from the mean","Standard deviation measures how spread out values are from the mean. Larger SD: more variability, more spread. Smaller SD: values cluster closely around the mean."),
    ]),
    s("Probability rules",[
      ("What are the Addition and Multiplication Rules of probability?","Think: P(A or B) and P(A and B)","Addition: P(A or B) = P(A) + P(B) - P(A and B). Multiplication (independent): P(A and B) = P(A) × P(B). If A and B are mutually exclusive, P(A or B) = P(A) + P(B)."),
      ("P(A) = 0.4, P(B) = 0.3, P(A and B) = 0.1. Find P(A or B).","Think: apply addition rule","P(A or B) = 0.4 + 0.3 - 0.1 = 0.6."),
      ("A bag has 4 red and 6 blue. Two drawn without replacement. P(both red)?","Think: dependent events","P(red) = 4/10. P(2nd red | 1st red) = 3/9. P(both) = 4/10 × 3/9 = 12/90 = 2/15."),
      ("What is conditional probability? Write the formula.","Think: P(A|B) = P(A and B) / P(B)","P(A|B): probability of A given B has occurred = P(A and B) / P(B). Restricts sample space to cases where B occurred."),
    ]),
    s("Data distributions",[
      ("What is a normal distribution? Describe its shape.","Think: bell curve — symmetric, mean=median=mode","Normal distribution: symmetric, bell-shaped curve. Mean = median = mode (all equal). The empirical rule: 68% of data within 1 SD, 95% within 2 SD, 99.7% within 3 SD of the mean."),
      ("What is a z-score and what does it tell you?","Think: number of standard deviations from the mean","z = (x - mean) / SD. Tells how many standard deviations a data point is from the mean. z = 2 means 2 SDs above average. Allows comparing values from different distributions."),
      ("Test score mean 72, SD 8. What z-score for a score of 88?","Think: z = (88-72)/8","z = 16/8 = 2. The score is 2 standard deviations above the mean."),
      ("What is the difference between a skewed left and skewed right distribution?","Think: tail direction = direction of skew","Right (positive) skew: tail extends to the right; mean > median (high outliers pull mean up). Left (negative) skew: tail extends to the left; mean < median (low outliers pull mean down)."),
    ]),
    s("Sampling and inference",[
      ("What is a hypothesis test?","Think: testing a claim about a population using sample data","Hypothesis test: a statistical procedure for making decisions about a population parameter using sample data. Null hypothesis (H0): assumes no effect or no difference. Alternative hypothesis (Ha): the claim being tested."),
      ("What does a p-value represent?","Think: probability of getting results as extreme as observed if H0 is true","P-value: probability of observing results as extreme as the sample data IF the null hypothesis is true. Small p-value (< 0.05): evidence against H0. Large p-value: insufficient evidence to reject H0."),
      ("What is a confidence interval?","Think: range likely to contain the true population parameter","A confidence interval is a range of values, constructed from sample data, that we believe contains the true population parameter with a specified level of confidence (e.g., 95%). Example: 95% CI for mean = (45, 55) means we are 95% confident the true mean is between 45 and 55."),
      ("What is the difference between a parameter and a statistic?","Think: population vs. sample measure","Parameter: numerical value describing a population (true mean — often unknown). Statistic: numerical value describing a sample (sample mean — calculated from data). Statistics are used to estimate parameters."),
    ]),
  ],
  # U4: Trigonometry
  [
    s("Right triangle trig",[
      ("What are the definitions of sin, cos, and tan in a right triangle?","Think: SOH-CAH-TOA","sin = opposite/hypotenuse. cos = adjacent/hypotenuse. tan = opposite/adjacent. These ratios are the same for all similar right triangles."),
      ("In a right triangle, the angle is 35° and the hypotenuse is 10. Find the opposite side.","Think: sin(35°) = opposite/10","opposite = 10 × sin(35°) ≈ 10 × 0.574 ≈ 5.74."),
      ("What are the exact trig values for 30°, 45°, and 60°?","Think: from 30-60-90 and 45-45-90 triangles","sin30°=1/2, cos30°=sqrt(3)/2, tan30°=1/sqrt(3). sin45°=sqrt(2)/2, cos45°=sqrt(2)/2, tan45°=1. sin60°=sqrt(3)/2, cos60°=1/2, tan60°=sqrt(3)."),
      ("A tree casts a shadow 20 m long. The angle of elevation of the sun is 40°. Find the tree's height.","Think: tan(40°) = height/20","height = 20 × tan(40°) ≈ 20 × 0.839 ≈ 16.8 m."),
    ]),
    s("The unit circle",[
      ("What is the unit circle?","Think: circle of radius 1 centered at origin","A circle with radius 1 centered at the origin. Points on the circle are (cos θ, sin θ) where θ is the angle from the positive x-axis. Used to extend trig functions beyond acute angles to all real numbers."),
      ("What are the coordinates of the point at 270° on the unit circle?","Think: sin(270°) = -1, cos(270°) = 0","(cos 270°, sin 270°) = (0, -1)."),
      ("In what quadrant is sin negative and cos positive?","Think: consider the unit circle quadrants","Quadrant IV (x positive, y negative). sin = y-coordinate (negative), cos = x-coordinate (positive)."),
      ("What is the period of sin x? What does period mean?","Think: how long before the pattern repeats","Period = 2pi. The function repeats every 2pi radians (360°). After a full rotation around the unit circle, all values repeat."),
    ]),
    s("Law of sines and cosines",[
      ("State the Law of Sines.","Think: ratios of sides to opposite angles are equal","a/sin(A) = b/sin(B) = c/sin(C). Used when you know: two angles and a side (AAS or ASA), or two sides and an angle opposite one of them (SSA — ambiguous case)."),
      ("State the Law of Cosines and when to use it.","Think: generalization of Pythagorean theorem","c^2 = a^2 + b^2 - 2ab×cos(C). Use when: you know three sides (SSS) or two sides and the included angle (SAS)."),
      ("In triangle ABC: A = 30°, B = 70°, a = 8. Find side b.","Think: Law of Sines: b/sin(B) = a/sin(A)","b = 8 × sin(70°)/sin(30°) = 8 × 0.940/0.5 ≈ 15.04."),
      ("In triangle, sides 5, 7, and 9. Find the largest angle.","Think: Law of Cosines with largest side opposite the angle","Largest side = 9 (opposite largest angle C). 81 = 25 + 49 - 2(5)(7)cos(C). cos(C) = (25+49-81)/70 = -7/70 ≈ -0.1. C ≈ 95.7°."),
    ]),
    s("Radians and arc length",[
      ("What is a radian? How do you convert degrees to radians?","Think: angle where arc length = radius","1 radian is the angle where the arc length equals the radius. Convert: multiply degrees by pi/180. Examples: 180° = pi, 90° = pi/2, 360° = 2pi."),
      ("Convert 240° to radians.","Think: multiply by pi/180","240 × pi/180 = 4pi/3."),
      ("Find the arc length of a sector with radius 6 and central angle 2pi/3.","Think: arc length = r × theta","arc = 6 × 2pi/3 = 4pi ≈ 12.57 units."),
      ("Convert 5pi/4 radians to degrees.","Think: multiply by 180/pi","5pi/4 × 180/pi = 5 × 45 = 225°."),
    ]),
    s("Trig identities",[
      ("State the Pythagorean identity.","Think: sin^2 + cos^2 = 1","sin^2(x) + cos^2(x) = 1. This follows from the unit circle definition (x^2 + y^2 = 1 where x = cos, y = sin). Also leads to: tan^2(x) + 1 = sec^2(x) and 1 + cot^2(x) = csc^2(x)."),
      ("Verify: (1 - cos^2 x)/sin x = sin x","Think: replace 1 - cos^2 x with sin^2 x","sin^2 x / sin x = sin x. Identity verified."),
      ("What are the reciprocal trig identities?","Think: reciprocals of sin, cos, tan","csc = 1/sin, sec = 1/cos, cot = 1/tan. These arise naturally in many trig expressions and simplifications."),
      ("Simplify: (sin x × cos x) / cos^2 x","Think: cancel and use tan","sin x / cos x = tan x."),
    ]),
  ],
  # U5: Advanced Algebra
  [
    s("Quadratic formula",[
      ("State the quadratic formula and what it finds.","Think: x = (-b ± sqrt(b^2-4ac)) / 2a","For ax^2 + bx + c = 0: x = (-b ± sqrt(b^2 - 4ac)) / (2a). Finds the zeros (x-intercepts) of any quadratic. Always works — unlike factoring which requires integer roots."),
      ("Solve: 2x^2 - 4x - 6 = 0 using the quadratic formula.","Think: a=2, b=-4, c=-6","Discriminant: 16 + 48 = 64. x = (4 ± 8)/4. x = 3 or x = -1."),
      ("What is the discriminant and what does it tell you?","Think: b^2 - 4ac determines number of real solutions","b^2 - 4ac > 0: two real solutions. = 0: one real solution (repeated root). < 0: no real solutions (two complex solutions). The discriminant tells you how many x-intercepts the parabola has."),
      ("Solve: x^2 + 4x + 7 = 0","Think: discriminant = 16-28 = -12 < 0","No real solutions. x = (-4 ± sqrt(-12))/2 = -2 ± i*sqrt(3). Complex solutions."),
    ]),
    s("Exponential and logarithmic functions",[
      ("What is a logarithm? Rewrite log_3(81) = 4 in exponential form.","Think: log_b(x) = y means b^y = x","A logarithm answers: what exponent gives this result? log_3(81) = 4 means 3^4 = 81."),
      ("What is the natural logarithm (ln)?","Think: logarithm with base e","ln(x) = log_e(x). Base e ≈ 2.718 (Euler's number). Natural logarithm arises naturally in calculus and continuous growth/decay. ln(e) = 1; ln(1) = 0."),
      ("Solve: 5^x = 125","Think: write 125 as power of 5","5^x = 5^3, so x = 3."),
      ("Solve: log(x) + log(x+3) = 1 (base 10)","Think: log(a) + log(b) = log(ab)","log(x(x+3)) = 1 → x(x+3) = 10 → x^2 + 3x - 10 = 0 → (x+5)(x-2) = 0. x = 2 (x = -5 rejected — log undefined for negative)."),
    ]),
    s("Sequences and series",[
      ("What is the formula for the sum of an arithmetic series?","Think: S_n = n/2 × (first + last)","S_n = n(a_1 + a_n)/2. Alternative: S_n = n/2 × (2a_1 + (n-1)d). Derived by pairing terms from each end."),
      ("Find the sum of the first 20 even positive integers.","Think: 2+4+6+...+40; arithmetic series","a_1=2, a_20=40, n=20. S = 20(2+40)/2 = 20×21 = 420."),
      ("What is the formula for the sum of a geometric series?","Think: S_n = a_1(1-r^n)/(1-r)","S_n = a_1(1 - r^n)/(1 - r) for r ≠ 1. Where r is the common ratio."),
      ("What is an infinite geometric series? When does it converge?","Think: |r| < 1 required for convergence","Infinite geometric series: sum of all terms when there are infinitely many. Converges (has a finite sum) when |r| < 1. S = a_1/(1-r). Example: 1 + 1/2 + 1/4 + ... = 1/(1-1/2) = 2."),
    ]),
  ],
  # U6: Pre-Calculus Preview
  [
    s("Limits intro",[
      ("What is a limit? What does lim(x→2) f(x) mean?","Think: the value f approaches as x gets close to 2","A limit describes the value a function approaches as the input approaches a specific value — even if the function is not defined there. lim(x→2) means: what value does f(x) get arbitrarily close to as x gets closer and closer to 2?"),
      ("Evaluate: lim(x→3) (x^2 - 9)/(x - 3)","Think: factor and cancel","(x-3)(x+3)/(x-3) = x+3. As x→3: 3+3 = 6."),
      ("What is a one-sided limit?","Think: approaching from left vs. right","Left-hand limit: lim(x→a^-) approaches a from values less than a. Right-hand limit: lim(x→a^+) approaches from above. The two-sided limit exists only if both one-sided limits are equal."),
      ("What does it mean for a function to be continuous at a point?","Think: three conditions must hold","f(a) is defined, lim(x→a) exists, and lim(x→a) = f(a). Informally: you can draw the function at that point without lifting your pencil."),
    ]),
    s("Rates of change intro",[
      ("What is average rate of change and how is it calculated?","Think: slope of secant line between two points","Average rate of change = (f(b) - f(a))/(b - a). This is the slope of the line connecting two points on the function — a secant line."),
      ("What is instantaneous rate of change?","Think: slope of tangent line at a single point","The rate of change at a specific moment — the slope of the tangent line at that point. As the interval shrinks to zero, average rate of change approaches instantaneous rate of change. This is the derivative in calculus."),
      ("Find the average rate of change of f(x) = x^2 from x=1 to x=3.","Think: (f(3)-f(1))/(3-1)","(9-1)/(3-1) = 8/2 = 4."),
      ("Why is the concept of rate of change important beyond mathematics?","Think: applications in science, economics, medicine","Velocity (rate of change of position), acceleration (rate of change of velocity), marginal cost (rate of change of total cost), population growth rate, reaction rate in chemistry. Rate of change thinking underlies all of science and economics."),
    ]),
    s("Composite and inverse functions",[
      ("What is function composition? Evaluate (f ∘ g)(3) if f(x) = x+1 and g(x) = x^2.","Think: f(g(3))","g(3) = 9. f(9) = 10. (f ∘ g)(3) = 10."),
      ("What is (f ∘ g)(x) vs. (g ∘ f)(x)?","Think: order matters","(f ∘ g)(x) = f(g(x)) — apply g first, then f. (g ∘ f)(x) = g(f(x)) — apply f first, then g. These are generally not equal."),
      ("Find the inverse of f(x) = (x-3)/2 and verify.","Think: swap x and y, solve for y","y = (x-3)/2 → x = (y-3)/2 → y = 2x+3. Verify: f(f^-1(x)) = ((2x+3)-3)/2 = 2x/2 = x. Correct."),
      ("What is the graphical relationship between a function and its inverse?","Think: reflection over the line y = x","The graph of f^-1 is the reflection of f over the line y = x. If (a,b) is on f, then (b,a) is on f^-1. This is because the roles of x and y are swapped."),
    ]),
  ],
]
print("G9 math complete")

P[9]["science"] = [
  # U1: Biology
  [
    s("Cell division and meiosis",[
      ("What is the difference between mitosis and meiosis?","Think: growth/repair vs. sexual reproduction","Mitosis: produces 2 genetically identical diploid cells (growth, repair). Meiosis: produces 4 genetically unique haploid cells (sex cells — sperm and eggs). Meiosis includes two rounds of division."),
      ("What happens during meiosis I vs. meiosis II?","Think: homologs separate vs. sister chromatids separate","Meiosis I: homologous chromosomes separate (diploid → haploid). Meiosis II: sister chromatids separate (like mitosis). Result: 4 haploid daughter cells, each genetically unique due to crossing over and independent assortment."),
      ("What is crossing over and why is it important?","Think: exchange of genetic material between homologs","Crossing over: homologous chromosomes exchange segments during meiosis I prophase. Creates new combinations of alleles not found in either parent — generates genetic variation. This is why siblings are not identical (unless twins)."),
      ("What is the significance of haploid sex cells?","Think: fertilization restores diploid number","If sex cells were diploid, fertilization would double the chromosome number each generation. By producing haploid sex cells, meiosis ensures fertilization restores the correct diploid number (46 in humans)."),
    ]),
    s("Genetics: complex inheritance",[
      ("What is incomplete dominance? Give an example.","Think: heterozygote shows intermediate phenotype","Incomplete dominance: neither allele is fully dominant; the heterozygote shows an intermediate phenotype. Example: red × white snapdragons → pink offspring (Rr)."),
      ("What is codominance? Give an example.","Think: both alleles expressed simultaneously","Codominance: both alleles expressed fully in heterozygote. Example: AB blood type — both A and B antigens present on red blood cells. Neither masks the other."),
      ("What is sex-linked inheritance?","Think: genes on the X or Y chromosome","Sex-linked genes are located on sex chromosomes (usually X). Males (XY) have only one X chromosome — if they inherit a recessive X-linked allele, they express it (no second X to mask it). Examples: color blindness, hemophilia."),
      ("A color-blind father (X^bY) and carrier mother (X^B X^b) have children. What fraction of sons will be color-blind?","Think: sons get Y from father, X from mother","Mother's X chromosomes: X^B or X^b (50/50). Sons get Y from father, so sons are X^B Y (normal) or X^b Y (color-blind). 50% of sons are color-blind."),
    ]),
    s("Molecular biology",[
      ("What is the central dogma of molecular biology?","Think: DNA → RNA → Protein","DNA → (transcription) → mRNA → (translation) → Protein. Genetic information flows from DNA to RNA to protein. Proteins do the work of the cell; DNA stores the instructions; RNA carries the message."),
      ("What is transcription?","Think: making mRNA from DNA template","Transcription: the enzyme RNA polymerase reads the DNA template strand and synthesizes a complementary mRNA strand. Occurs in the nucleus. A → U (instead of T in RNA), T → A, G → C, C → G."),
      ("What is translation?","Think: ribosomes read mRNA to build a protein","Translation: ribosomes read the mRNA sequence in triplets (codons). Each codon codes for a specific amino acid. tRNA brings the matching amino acid. The ribosome links amino acids into a polypeptide chain — a protein."),
      ("What is a mutation? Give one example of each type.","Think: change in DNA sequence","Point mutation: change in single base pair (substitution — may change amino acid; insertion or deletion — frameshift shifts all downstream codons). Chromosomal mutation: large changes (deletion, duplication, inversion of chromosome segment). Mutations can be harmful, neutral, or rarely beneficial."),
    ]),
    s("Evolution mechanisms",[
      ("What are the five mechanisms of evolution?","Think: MAGES — Mutation, Assortative mating, Genetic drift, emigration/immigration, Selection","Mutation: new alleles arise. Gene flow (migration): alleles move between populations. Genetic drift: random changes in allele frequency (more powerful in small populations). Natural selection: differential survival and reproduction. Non-random mating: alters genotype frequencies."),
      ("What is genetic drift?","Think: random change in allele frequencies due to chance sampling","Random fluctuations in allele frequency, especially powerful in small populations. Bottleneck effect: population greatly reduced (earthquake, disease) — survivors may not represent original allele frequencies. Founder effect: small group starts new population — founder alleles overrepresented."),
      ("What is the difference between microevolution and macroevolution?","Think: changes within a species vs. above the species level","Microevolution: changes in allele frequencies within a population (can be observed in real time — antibiotic resistance). Macroevolution: evolutionary changes above the species level — speciation, extinction, origins of new body plans. Macroevolution is the cumulative result of microevolution over long time."),
      ("What is the Hardy-Weinberg principle?","Think: allele frequencies constant in the absence of evolution","In a population NOT evolving: p^2 + 2pq + q^2 = 1 (where p and q are allele frequencies). Used as a null model — deviations indicate evolution is occurring. Requires: large population, random mating, no mutation, no migration, no natural selection."),
    ]),
  ],
  # U2: Chemistry
  [
    s("Atomic structure and electron configuration",[
      ("What is an electron orbital? Name the four types.","Think: regions where electrons are likely to be found","Orbital: a region of space where there is high probability of finding an electron. Types: s (spherical, 1 orientation), p (dumbbell, 3 orientations), d (complex, 5), f (complex, 7). Each can hold 2 electrons (Pauli exclusion principle)."),
      ("Write the electron configuration for carbon (atomic number 6).","Think: fill orbitals in order of increasing energy","1s^2 2s^2 2p^2. Carbon has 6 electrons: 2 in 1s, 2 in 2s, 2 in 2p."),
      ("What are valence electrons and why do they determine chemical behavior?","Think: outermost shell electrons participate in bonding","Valence electrons: electrons in the outermost energy level. They are involved in chemical bonding. Atoms react to achieve a stable configuration (usually 8 valence electrons — octet rule). Number of valence electrons = group number for main group elements."),
      ("What are the quantum numbers and what does each describe?","Think: n, l, ml, ms","Principal (n): energy level (1,2,3...). Angular momentum (l): orbital shape (0=s,1=p,2=d). Magnetic (ml): orbital orientation (-l to +l). Spin (ms): electron spin (+1/2 or -1/2). Each electron has a unique set of four quantum numbers."),
    ]),
    s("Chemical bonding",[
      ("What determines whether a bond is ionic, polar covalent, or nonpolar covalent?","Think: electronegativity difference","Electronegativity difference > 1.7: ionic. 0.4 to 1.7: polar covalent (electrons shared unequally). < 0.4: nonpolar covalent (electrons shared equally). The greater the difference, the more ionic character."),
      ("What is a Lewis structure?","Think: dot diagram showing valence electrons and bonds","Lewis structure shows valence electrons as dots and covalent bonds as lines between atoms. Purpose: show how electrons are arranged in a molecule. Each line = shared pair (covalent bond); dots = lone pair (non-bonding electrons)."),
      ("Draw the Lewis structure for water (H2O).","Think: O has 6 valence electrons; 2 bonds to H, 2 lone pairs","Oxygen in the center with one bond to each hydrogen. Two lone pairs on oxygen. Structure: H-O-H with 2 pairs of dots on O. This bent shape gives water its polar character."),
      ("What is VSEPR theory?","Think: electron pairs repel, creating molecular geometry","Valence Shell Electron Pair Repulsion: electron pairs (bonding and lone pairs) arrange themselves to minimize repulsion. Predicts molecular geometry: 2 groups = linear, 3 = trigonal planar, 4 = tetrahedral, etc. Explains why water is bent (109.5° adjusted for lone pair repulsion → 104.5°)."),
    ]),
    s("Stoichiometry",[
      ("What is a mole? What is Avogadro's number?","Think: 6.022 × 10^23 particles","The mole is the SI unit for amount of substance. 1 mole = 6.022 × 10^23 particles (Avogadro's number). Just like 'dozen' = 12, 'mole' = 6.022 × 10^23. Allows chemists to count atoms by weighing."),
      ("What is molar mass and how do you find it?","Think: mass of one mole; from the periodic table","Molar mass = sum of atomic masses of all atoms in a formula (in g/mol). Example: H2O = 2(1.008) + 16.00 = 18.016 g/mol. This is the mass of one mole of water."),
      ("How many molecules are in 2 moles of CO2?","Think: 2 × Avogadro's number","2 × 6.022 × 10^23 = 1.204 × 10^24 molecules."),
      ("In the reaction N2 + 3H2 → 2NH3: If 14 g of N2 reacts, how many grams of NH3 form?","Think: molar mass N2 = 28; NH3 = 17; mole ratio 1:2","14 g N2 = 0.5 mol N2. 0.5 mol N2 × (2 mol NH3/1 mol N2) = 1 mol NH3 = 17 g NH3."),
    ]),
    s("Gas laws",[
      ("State Boyle's Law. Write the formula.","Think: pressure and volume inversely related at constant T","At constant temperature and amount: P1V1 = P2V2. If pressure doubles, volume halves. Gas particles collide more often in smaller volume, increasing pressure."),
      ("State Charles's Law.","Think: volume and temperature directly related at constant P","At constant pressure: V1/T1 = V2/T2 (T must be in Kelvin). Gas expands as temperature increases — particles move faster and need more space."),
      ("A gas at 2 atm and 4 L is compressed to 1 L. Find the new pressure (constant T).","Think: Boyle's Law","P1V1 = P2V2 → 2 × 4 = P2 × 1 → P2 = 8 atm."),
      ("What is the Ideal Gas Law and when does it apply?","Think: PV = nRT","PV = nRT. P = pressure (atm), V = volume (L), n = moles, R = 0.0821 L·atm/mol·K, T = temperature (Kelvin). Applies best to real gases at low pressure and high temperature (where intermolecular forces are negligible)."),
    ]),
  ],
  # U3: Physics
  [
    s("Kinematics",[
      ("What are the four kinematic equations?","Think: equations relating displacement, velocity, acceleration, time","v = v0 + at. d = v0t + (1/2)at^2. v^2 = v0^2 + 2ad. d = (v+v0)/2 × t. These apply when acceleration is constant."),
      ("A ball is thrown upward at 20 m/s. How high does it go?","Think: v=0 at max height; v^2 = v0^2 - 2gd","0 = 400 - 2(10)d → d = 20 m."),
      ("What is the difference between distance and displacement?","Think: total path vs. net change in position","Distance: total path length traveled (scalar). Displacement: change in position from start to end — magnitude and direction (vector). Running a full lap: distance = 400m, displacement = 0."),
      ("A car decelerates from 30 m/s to 0 in 6 seconds. Find deceleration.","Think: a = (v - v0)/t","a = (0 - 30)/6 = -5 m/s^2. Deceleration of 5 m/s^2."),
    ]),
    s("Newton's laws applied",[
      ("What is the difference between mass and weight?","Think: intrinsic property vs. gravitational force","Mass: amount of matter (kg) — constant regardless of location. Weight: gravitational force on the mass (N) — W = mg. On the Moon, mass stays the same but weight is 1/6 of Earth weight."),
      ("A 70 kg person stands on a scale in an elevator accelerating upward at 2 m/s^2. What does the scale read?","Think: apparent weight = m(g+a) when accelerating upward","Normal force = 70 × (9.8 + 2) = 70 × 11.8 = 826 N (heavier than usual)."),
      ("What is friction? Calculate: coefficient of kinetic friction = 0.3, normal force = 50 N.","Think: f = mu × N","Friction force = 0.3 × 50 = 15 N. This force opposes the direction of motion."),
      ("A 5 kg box on a frictionless surface is pushed by a 20 N force. Find acceleration.","Think: F = ma","a = F/m = 20/5 = 4 m/s^2."),
    ]),
    s("Work and energy",[
      ("What is work in physics? What conditions must be met?","Think: force × displacement in the direction of force","Work = F × d × cos(θ). θ = angle between force and displacement. Work is done only when a force moves an object through a displacement in the direction of the force. Units: Joules (N·m)."),
      ("A 200 N force pushes a box 5 m horizontally. Calculate work.","Think: W = Fd (force and displacement parallel)","W = 200 × 5 = 1000 J."),
      ("What is the work-energy theorem?","Think: net work = change in kinetic energy","Net work done on an object equals its change in kinetic energy: W_net = ΔKE = (1/2)mv_f^2 - (1/2)mv_i^2."),
      ("A 2 kg ball is dropped from 10 m. Find its speed just before hitting the ground.","Think: PE lost = KE gained","mgh = (1/2)mv^2 → gh = v^2/2 → v = sqrt(2×10×10) = sqrt(200) ≈ 14.1 m/s."),
    ]),
    s("Waves and sound",[
      ("What is the Doppler effect?","Think: change in frequency due to relative motion","When a sound source moves toward you, waves bunch together — higher frequency (higher pitch). Moving away: waves spread out — lower frequency (lower pitch). Explains: ambulance siren changes pitch as it passes. Also applies to light (redshift/blueshift)."),
      ("What is resonance?","Think: natural frequency matches driving frequency","Resonance: a system vibrates at maximum amplitude when driven at its natural frequency. Examples: pushing a swing at its natural frequency, Tacoma Narrows Bridge collapse (wind matched bridge's natural frequency), musical instruments (strings and air columns resonate)."),
      ("How does the speed of sound change with temperature?","Think: warmer air → faster molecular motion → faster sound","Sound travels faster in warmer air (at 0°C: ~331 m/s; at 20°C: ~343 m/s). Speed also depends on medium: faster in denser materials (steel ≈ 5,100 m/s, water ≈ 1,480 m/s) because particles are closer together."),
      ("What is constructive vs. destructive interference?","Think: waves combining to create larger or smaller amplitude","Constructive interference: two waves aligned in phase — amplitudes add (louder, brighter). Destructive interference: waves aligned out of phase — amplitudes cancel (quieter, darker). Basis of noise-canceling headphones and many optical effects."),
    ]),
  ],
  # U4: Earth Science
  [
    s("Climate systems",[
      ("What are the major climate zones and what determines them?","Think: tropical, temperate, polar — determined by latitude and more","Tropical (0-23.5°): hot year-round, high rainfall. Temperate (23.5-66.5°): four seasons. Polar (66.5-90°): cold year-round, low precipitation. Proximity to oceans moderates climate; elevation, prevailing winds, and ocean currents modify these patterns."),
      ("What is the greenhouse effect and what gases are responsible?","Think: CO2, methane, water vapor trap heat","Greenhouse gases absorb and re-emit infrared radiation, keeping Earth warm. Main gases: CO2, CH4 (methane), N2O, and water vapor. Human activities increase CO2 and CH4 significantly, amplifying the natural greenhouse effect."),
      ("What is El Niño and how does it affect global weather?","Think: periodic warming of Pacific that disrupts normal weather patterns","El Niño: irregular warming of central and eastern Pacific every 2-7 years. Effects: droughts in Australia and South Asia, floods in South America, disrupted monsoons, more intense hurricanes in the Pacific, milder winters in the US. El Niño is part of the ENSO (El Niño-Southern Oscillation) cycle."),
      ("What are feedback loops in the climate system? Give one positive example.","Think: self-amplifying vs. self-limiting cycles","Positive feedback: a change amplifies further change (destabilizing). Example: Arctic ice melts → darker ocean absorbs more heat → more melting → more heat absorption. Negative feedback: a change suppresses further change (stabilizing). Earth's climate has both types."),
    ]),
    s("Earth's resources",[
      ("What is the difference between renewable and nonrenewable energy sources?","Think: replenishment rate relative to use","Renewable: replenished naturally on human timescales (solar, wind, hydro, geothermal, biomass). Nonrenewable: formed over millions of years, depleted far faster than formed (coal, oil, natural gas, uranium). The world is transitioning toward renewables due to climate change and finite fossil fuels."),
      ("What are the environmental impacts of fossil fuel use?","Think: air pollution, climate change, habitat destruction","Burning fossil fuels releases: CO2 (greenhouse gas), SO2 (acid rain), NOx (smog), particulate matter (respiratory illness). Extraction causes: oil spills, habitat destruction, water contamination (fracking), mountaintop removal. These are among the largest drivers of climate change."),
      ("What is the rock cycle and how does it relate to Earth's resources?","Think: rocks form, transform, and reform continuously","The rock cycle transforms rocks through: igneous (cooling magma), sedimentary (sediment compaction), and metamorphic (heat/pressure). Resources formed through these cycles: coal and oil from ancient organisms (sedimentary), metals from igneous/metamorphic processes, limestone from marine shells."),
      ("What is soil and why is it a critical resource?","Think: living system supporting agriculture and ecosystem function","Soil: a complex mixture of minerals, organic matter (humus), water, air, and living organisms. Takes hundreds of years to form. Supports: plant growth, water filtration, carbon storage, nutrient cycling. Threats: erosion, compaction, contamination, salinization from over-irrigation."),
    ]),
    s("Astronomy",[
      ("What is the life cycle of a star?","Think: depends on mass — main sequence, then red giant, then death","Low-mass stars: main sequence → red giant → planetary nebula → white dwarf → black dwarf. High-mass stars: main sequence → supergiant → supernova → neutron star or black hole. Our Sun is a medium-mass star with ~5 billion years remaining."),
      ("What is a black hole and how does one form?","Think: region of space with gravity so strong not even light escapes","Black hole: forms when a massive star (>20 solar masses) collapses in a supernova. The core is so dense that gravity becomes infinite at the singularity. The event horizon is the point of no return — even light cannot escape. Cannot be seen directly — detected by effects on nearby matter."),
      ("What is the Big Bang theory?","Think: universe began as an extremely hot, dense point ~13.8 billion years ago","The universe began in an extremely hot, dense state and has been expanding and cooling ever since. Evidence: cosmic microwave background radiation (afterglow of the Big Bang), redshift of galaxies (universe expanding), and the abundance of light elements (hydrogen and helium)."),
      ("What are the four forces of nature and briefly describe each?","Think: gravity, electromagnetism, strong nuclear, weak nuclear","Gravity: weakest, infinite range, always attractive, governs large-scale structure. Electromagnetism: infinite range, governs atoms and chemistry. Strong nuclear: short range, holds nucleus together (overcomes electromagnetic repulsion of protons). Weak nuclear: very short range, governs radioactive decay."),
    ]),
  ],
]
print("G9 science complete")

P[9]["ela"] = [
  [
    s("Literary analysis — American literature",[
      ("What is the American Dream and how do authors interrogate it?","Think: ideal of upward mobility through hard work","The American Dream: the belief that through hard work and determination, anyone can achieve success and prosperity. Authors like Fitzgerald (The Great Gatsby), Steinbeck (Of Mice and Men), and Miller (Death of a Salesman) reveal its darker side: the dream as illusion, as available only to some, as a destructive obsession."),
      ("What is naturalism in American literature?","Think: characters shaped by forces they cannot control","Naturalism: literary movement depicting characters as determined by heredity, environment, and social forces beyond their control. Humans are shown as animals subject to the same forces as nature. Authors: Stephen Crane, Jack London, Theodore Dreiser. Contrasts with Romanticism's belief in individual freedom and heroism."),
      ("What is the difference between realism and idealism in literature?","Think: depicting reality as it is vs. as it should be","Realism: depicts life as it is — unglamorous, complicated, morally ambiguous. Idealism: depicts life as it should or could be — often more heroic or morally clear. Most complex literature holds tension between the two — characters with idealistic dreams confronting realistic obstacles."),
      ("How does setting function as more than background in a novel?","Think: setting reflects theme and creates meaning","Setting can: embody social forces affecting characters (the Valley of Ashes in Gatsby), create mood (fog in Great Expectations), limit or enable character choices (physical environment as character), and symbolize abstract themes. Active analysis asks how setting shapes and reflects the story's meaning."),
    ]),
    s("Extended nonfiction",[
      ("What is a memoir and how does it differ from autobiography?","Think: both are true first-person, but different focus","Autobiography: comprehensive account of one's whole life, chronological. Memoir: focused account of a specific period, event, or theme in a life — not comprehensive. Memoirs may use literary techniques (scenes, dialogue, symbolism) more intensively than autobiography."),
      ("What is the rhetorical triangle?","Think: speaker, audience, purpose — all interact","The rhetorical triangle: speaker (ethos — credibility, who is speaking), message (logos — content, reasoning), audience (pathos — emotional connection, who is being addressed). All three must be considered to analyze or produce effective communication."),
      ("How do you synthesize information from multiple nonfiction sources?","Think: find agreements, contradictions, gaps, and patterns","Synthesis: identifying what multiple sources agree on, where they disagree, what each source uniquely adds, and what gaps remain. A synthesis creates new understanding that goes beyond any single source. Use transitional language to show relationships: both, in contrast, however, building on X's claim, Y adds..."),
      ("What is bias in nonfiction writing? How do you identify it?","Think: slanted presentation — even without lying","Bias: systematic tendency to present information in a way that supports one perspective. Identify through: word choice (connotative vs. denotative), what information is included vs. omitted, how sources are selected, who benefits from the reader believing the argument."),
    ]),
    s("Shakespearean drama",[
      ("What is blank verse and why did Shakespeare use it?","Think: unrhymed iambic pentameter","Blank verse: unrhymed iambic pentameter. Shakespeare used it for noble characters speaking formal dialogue. Prose used for lower-class characters and comic scenes. The verse form mirrors social hierarchy and emotional register — shifts between verse and prose are deliberate and meaningful."),
      ("What is the tragic flaw (hamartia) in Shakespearean tragedy?","Think: the hero's internal quality leading to downfall","Hamartia: a character flaw or error in judgment that leads to a tragic hero's downfall. Examples: Hamlet's indecision, Macbeth's ambition, Othello's jealousy, Lear's pride. The tragedy is that the same quality that makes the hero great also destroys them."),
      ("How does Shakespeare use comic relief in tragedies?","Think: strategic humor to release tension and highlight contrast","Comic relief: humorous scenes or characters inserted into tragic plays. Functions: releases audience tension, provides contrast that makes surrounding tragedy more intense, offers alternative perspective on events. The gravediggers in Hamlet; the Porter in Macbeth."),
      ("What is the difference between a Shakespearean and Petrarchan sonnet?","Think: structure and where the turn (volta) occurs","Petrarchan: octave (8 lines, ABBAABBA) + sestet (6 lines, CDECDE); turn after line 8. Shakespearean: three quatrains (ABAB CDCD EFEF) + couplet (GG); turn before the final couplet which delivers the poem's conclusion."),
    ]),
    s("Writing: research and argument",[
      ("What is an annotated bibliography?","Think: citation + summary + evaluation of each source","Annotated bibliography: list of sources with a brief summary and evaluation of each entry. Purpose: track your research, demonstrate engagement with sources, and evaluate each source's relevance, credibility, and usefulness to your argument."),
      ("What is the difference between an argument and a research paper?","Think: advancing a position vs. investigating a question","Argument: advances a specific position with evidence and reasoning. Research paper: investigates a question using evidence, may or may not argue a position. Academic writing often combines both: a research paper argues a thesis using research as evidence."),
      ("What is an academic citation and why is it important ethically and practically?","Think: credit and accountability","Citations: (1) Give credit to original thinkers (ethical). (2) Allow readers to verify claims (intellectual accountability). (3) Show you have engaged with existing scholarship. (4) Protect you from plagiarism charges. In academic writing, every claim that is not common knowledge or your own original analysis requires a citation."),
      ("What is revision at the global level vs. local level?","Think: big picture argument vs. sentence-level polish","Global revision: reconsidering thesis, argument structure, evidence quality, and organization. Local revision: improving sentence clarity, word choice, transitions, and grammar. Always revise globally first — there is no point perfecting a sentence you will cut."),
    ]),
    s("Vocabulary and language",[
      ("What are Greek and Latin roots? Give four examples with words derived from them.","Think: common academic vocabulary origins","Greek: bio (life: biology, biography), geo (earth: geology, geography), philo (love: philosophy, philanthropy). Latin: port (carry: transport, portable), rupt (break: interrupt, rupture), scrib (write: describe, prescription). Knowing roots unlocks thousands of unfamiliar words."),
      ("What is syntax and how does it affect meaning?","Think: sentence structure creates emphasis and tone","Syntax: the arrangement of words and phrases to create well-formed sentences. Varying syntax creates rhythm, emphasis, and tone. Placing a word at the end of a sentence (the position of emphasis) creates different effect than placing it at the beginning. Syntax is a writer's tool."),
      ("What is diction and how does register affect communication?","Think: word choice and formal vs. informal registers","Diction: word choice. Register: level of formality. Academic register: formal, precise, avoids contractions and slang. Informal register: casual, may include contractions, idioms, colloquialisms. Matching register to context is a fundamental communication skill."),
      ("How do you determine a word's meaning in context when it is unfamiliar?","Think: use multiple clue types and then verify","(1) Look for definition or restatement clues. (2) Look for synonyms or antonyms. (3) Analyze word structure (roots, prefixes, suffixes). (4) Infer from overall passage meaning. (5) When uncertain, look it up — and remember it in context for better retention."),
    ]),
  ],
  [
    s("Close reading",[
      ("What is close reading?","Think: slow, careful analysis of every word and structural choice","Close reading: reading a short passage carefully and deeply, analyzing how specific word choices, sentence structures, rhetorical devices, and patterns create meaning. Unlike general comprehension — close reading asks HOW and WHY rather than just WHAT."),
      ("What is the difference between annotation and highlighting?","Think: active vs. passive engagement with text","Highlighting: passive marking. Annotation: active engagement — writing notes, questions, observations, connections, and analysis IN the margins. Annotation externalizes your thinking process and makes your engagement with the text visible."),
      ("What are signal words and how do they help with reading comprehension?","Think: linguistic cues about structure and relationships","Signal words indicate: contrast (however, although, conversely), addition (furthermore, moreover), cause (because, therefore, thus), sequence (first, subsequently, finally), emphasis (indeed, most importantly). Recognizing signals helps readers navigate complex texts efficiently."),
      ("How do you read a dense paragraph of argument?","Think: identify claim, evidence, and reasoning","(1) Find the topic sentence (claim). (2) Identify supporting evidence. (3) Trace the logical reasoning connecting evidence to claim. (4) Note qualifications, concessions, or limitations the author acknowledges. (5) Evaluate: Is the claim supported? Is the reasoning valid?"),
    ]),
    s("Contemporary literature",[
      ("What is a coming-of-age narrative? What are its common elements?","Think: Bildungsroman — protagonist's growth from youth to maturity","Bildungsroman (German for formation novel): follows a protagonist's psychological and moral growth from youth to adulthood. Common elements: loss of innocence, conflict with society or family, search for identity, experiences of failure and learning, eventual integration into society — often with ambivalence about what is lost."),
      ("How do contemporary authors handle unreliable narrators differently from earlier literature?","Think: postmodern self-awareness and experimentation","Contemporary literature often makes the narrator's unreliability more explicit, more self-aware, or more systematic. The narrative voice may comment on its own limitations. Postmodern works may have multiple competing narrators, all unreliable, making absolute truth impossible to determine."),
      ("What is intertextuality?","Think: a text's relationship to other texts","Intertextuality: the relationship between a text and other texts it references, alludes to, or responds to. Contemporary literature often consciously alludes to classical texts — creating layers of meaning. Reading intertextually asks: what other text does this reference, and what does that reference add?"),
      ("What is a frame narrative?","Think: a story within a story","Frame narrative: an outer story that frames an inner story (or stories). Examples: The Canterbury Tales (pilgrims tell stories), Wuthering Heights (multiple narrators), The Princess Bride. The frame narrative affects how we interpret the inner story — through whose eyes are we seeing it?"),
    ]),
    s("Media analysis",[
      ("What is the difference between medium and message?","Think: McLuhan — the medium itself shapes the message","Marshall McLuhan: the medium through which a message is delivered shapes and changes the message itself. A news event covered by a 30-second video, a 3,000-word article, and a tweet carries fundamentally different information and creates different understanding — even with the same basic facts."),
      ("How do you analyze a political advertisement?","Think: target audience, emotional appeals, factual claims","Analyze: Who is the target audience? What emotional appeals are used (fear, pride, nostalgia)? What factual claims are made — are they verifiable? What is shown vs. not shown? What music, imagery, and tone are deployed? Are any logical fallacies used?"),
      ("What is framing in journalism?","Think: how the way a story is told shapes how audiences understand it","Framing: the choice of what to include, emphasize, and omit in presenting news. The same event can be framed differently: as a crime story, an economic story, or a social justice story — with very different implications. Framing analysis asks: whose perspective is centered and what is left out?"),
      ("How does social media change the production and consumption of news?","Think: gatekeepers removed, speed increased, filter bubbles created","Traditional media had editors (gatekeepers) who filtered information. Social media: anyone can publish, information spreads instantly, algorithms create filter bubbles (showing you content you already agree with), emotionally engaging (outrage) content spreads fastest regardless of accuracy."),
    ]),
    s("Writing to argue",[
      ("What is Toulmin argumentation?","Think: claim, data, warrant, backing, qualifier, rebuttal","Toulmin model: Claim (position), Data (evidence), Warrant (assumption connecting data to claim), Backing (support for warrant), Qualifier (degree of certainty), Rebuttal (conditions under which claim does not hold). More nuanced than simple claim-evidence structure."),
      ("How do you write a nuanced argument that acknowledges complexity?","Think: concessions, qualifications, and multiple perspectives","Use: concession + rebuttal (While X is true, Y outweighs it because...), qualifiers (in most cases, under certain conditions), acknowledgment of counterevidence, and recognition of what is not yet known. Nuanced argument is more credible and more convincing to skeptical readers."),
      ("What is the difference between summary, analysis, and evaluation?","Think: restate, interpret, judge","Summary: restates what was said or done. Analysis: examines HOW it works — what techniques are used and how they create meaning. Evaluation: makes a judgment about quality, value, or effectiveness with criteria. Academic writing requires all three — but never confuses them."),
      ("What is hedging language and when should you use it?","Think: qualifying claims to match certainty of evidence","Hedging: language that qualifies the certainty of a claim (may, tends to, suggests, in many cases, generally). Use when: evidence does not definitively prove the claim, acknowledging uncertainty is intellectually honest, or when making a claim about complex human behavior. Avoid over-hedging (saying nothing decisively) and under-hedging (claiming more certainty than evidence supports)."),
    ]),
  ],
  [
    s("Nonfiction analysis",[
      ("What is ethos in nonfiction writing? How do authors establish it?","Think: credibility and trustworthiness","Ethos: the author's credibility. Established through: demonstrating expertise (credentials, evidence of research), fair treatment of opposing views, transparent acknowledgment of uncertainty, appropriate use of sources, professional tone. A writer who misrepresents the opposition undermines their ethos."),
      ("What is the difference between deductive and inductive structure in nonfiction?","Think: thesis first vs. thesis last","Deductive: thesis stated at the beginning; essay proves it. Most academic writing uses this structure. Inductive: builds through evidence and examples, with thesis emerging at the end. More common in essays, opinion pieces, and journalism. Inductive can be more engaging for skeptical readers."),
      ("How do you evaluate a scientific study reported in the popular press?","Think: what details matter for validity","Ask: Was it peer-reviewed? How large was the sample? Was it a randomized controlled trial or an observational study? Did it show correlation or causation? Was it replicated? What did the researchers actually say vs. how the headline presents it? One study rarely overturns established science."),
      ("What is the difference between informing, persuading, and manipulating?","Think: intent and transparency of methods","Informing: sharing accurate information transparently. Persuading: making an honest case for a position using evidence and reasoning. Manipulating: using deceptive or psychologically exploitative techniques — false information, emotional exploitation, misleading framing — to change beliefs or behavior without fair reasoning."),
    ]),
    s("Independent reading and response",[
      ("What is reader response theory?","Think: meaning is co-created by text and reader","Reader response theory: literary meaning is not fixed in the text alone but is created in the interaction between the text and the reader. Different readers bring different experiences, cultural contexts, and knowledge — producing different but equally valid readings. Contrasts with close reading that seeks the 'correct' meaning."),
      ("How do you write a reading response that goes beyond summary?","Think: personal connection + textual evidence + analytical question","A strong reading response: connects the text to your own experience or understanding (but with intellectual distance), raises a genuine analytical question the text creates, uses specific textual evidence, and offers an interpretive insight that is not obvious. It is a conversation with the text."),
      ("What is the difference between a book review and a literary analysis?","Think: evaluative vs. analytical purpose","Book review: evaluates the work for potential readers — is it good? Does it achieve what it sets out to do? Would you recommend it? Literary analysis: analyzes how the text creates meaning — not primarily whether it succeeds, but how it works. Reviews are more evaluative; analyses are more analytical."),
      ("How can you connect literature to historical and cultural context without reducing it to social document?","Think: context illuminates but does not exhaust literary meaning","Historical context helps explain choices, references, and blind spots. But literature exceeds its historical moment — that's why it endures. Connect: show how historical forces shaped the work without claiming the work is ONLY about those forces or that understanding context is the same as understanding the work."),
    ]),
    s("Grammar and style at the advanced level",[
      ("What is cohesion and how do you create it in academic writing?","Think: the flow connecting sentences and paragraphs","Cohesion: the sense that a text holds together as a unified whole. Created through: transitional words, echo structure (end one sentence with a term, begin next with it), pronoun reference, parallel structure, and consistent argument thread. Cohesive writing guides readers without them noticing."),
      ("What are common sentence-level issues in advanced writing?","Think: wordiness, passivity, nominalization","Wordiness: using more words than necessary. Passivity: overuse of passive voice where active is clearer. Nominalization: turning verbs into nouns (investigation = investigate, utilization = use) — makes prose unnecessarily dense. Good academic style is precise and clear, not artificially complex."),
      ("What is punctuation for style vs. punctuation for grammar?","Think: dashes, colons, semicolons as tools","Grammar: comma splices are errors. Style: dashes (em dashes) create emphasis and informal energy. Colons introduce (formally). Semicolons link related independent clauses without full stop. Parentheses aside. A sophisticated writer chooses punctuation deliberately for rhetorical effect."),
      ("What is voice in writing and how do you develop yours?","Think: the distinctive personality expressed through style choices","Voice: the personality, tone, and perspective expressed through writing — word choice, sentence rhythm, level of formality, characteristic concerns. Developed through: wide reading, writing regularly, revising toward clarity and specificity, developing genuine opinions, and resisting generic academic prose conventions."),
    ]),
  ],
]
print("G9 ELA complete")

P[9]["history"] = [
  [
    s("Ancient civilizations foundations",[
      ("What are the common features of early civilizations?","Think: agriculture, cities, writing, government, religion, specialization","Eight features: (1) Stable food supply (agriculture). (2) Social structure (classes). (3) Government. (4) Religion/cosmology. (5) Arts and architecture. (6) Public works (irrigation, roads). (7) Writing. (8) Trade. These features emerged independently in multiple locations."),
      ("What is historiography and why does it matter?","Think: how history has been written and interpreted","Historiography: the study of how history has been recorded, interpreted, and revised over time. Matters because: all historical accounts reflect the perspective and context of who wrote them. Understanding historiography helps evaluate sources and recognize that historical interpretation changes as new evidence and perspectives emerge."),
      ("What is primary vs. secondary vs. tertiary source?","Think: original vs. analysis vs. compilation","Primary: original document, artifact, or account from the period (Magna Carta, diary, census data). Secondary: analysis or interpretation of primary sources (biography, textbook chapter). Tertiary: compilation of secondary sources (encyclopedias, databases). Historians rely on primary sources but use secondary sources for context."),
      ("What is the difference between historical fact and historical interpretation?","Think: what happened vs. what it means","Historical fact: verifiable events (Rome fell to Germanic tribes in 476 CE). Historical interpretation: the meaning, causes, and significance of events — these change as historians ask different questions. Most historical debates are about interpretation, not facts."),
    ]),
    s("Greek and Roman legacy",[
      ("What was direct democracy in Athens? Who was excluded?","Think: direct participation, but for a narrow group","Direct democracy: citizens voted directly on laws and policies (not through representatives). In Athens (~450 BCE): only adult male citizens could participate. Women, enslaved people, and resident foreigners (metics) were excluded — approximately 10-15% of the population held democratic rights."),
      ("What was the Roman Republic's system of government?","Think: consuls, Senate, assemblies, checks and balances","Two consuls (elected annually, could veto each other). Senate: advised consuls, controlled finances. Popular assemblies: could elect magistrates and pass laws. This mixed constitution influenced the US Founders directly — Madison's Republic is consciously modeled on Rome."),
      ("How did Greco-Roman culture influence Western civilization?","Think: democracy, philosophy, law, architecture, language","Democracy (Athens), philosophy (Socrates, Plato, Aristotle), Roman law (foundation of legal systems in most of Europe and the Americas), architecture (columns, domes, arches), Latin (root of Romance languages and scientific vocabulary), literature (Homer, Virgil, Cicero)."),
      ("What led to the fall of the Western Roman Empire?","Think: multiple overlapping causes over centuries","Political instability (50+ emperors in 50 years at one point), military overextension, economic problems (currency devaluation, trade decline), reliance on mercenary armies, pressure from Germanic tribes and Huns, disease, and administrative division (East/West). Historians debate relative weight of each cause."),
    ]),
    s("Global economics",[
      ("What is mercantilism and how did it shape colonial empires?","Think: maximize exports, minimize imports; colonies supply raw materials","Mercantilism: economic theory that wealth is finite and nations should maximize exports and accumulate gold. Colonies existed to: supply cheap raw materials to the mother country, buy manufactured goods from the mother country, and enrich the colonizing nation. Led to strict trade regulations and exploitation of colonial economies."),
      ("What is the difference between a market economy, command economy, and mixed economy?","Think: who controls economic decisions","Market: private individuals and businesses make economic decisions through price mechanisms (supply and demand). Command: government centrally plans and controls production and distribution. Mixed: combines elements of both — most modern economies are mixed. Pure forms of either market or command economies do not exist in practice."),
      ("What are the factors of production?","Think: land, labor, capital, entrepreneurship","Land: natural resources. Labor: human effort. Capital: tools, machinery, buildings used in production (physical capital) and education and skills (human capital). Entrepreneurship: the ability to combine the other factors innovatively to create value. All production requires some combination of these four."),
      ("What is comparative advantage and how does it explain international trade?","Think: specialize in what you produce most efficiently relative to others","Comparative advantage: a country should specialize in producing goods for which it has the lowest opportunity cost (even if another country is absolutely better at producing everything). Trade allows both countries to consume more than if each produced everything domestically."),
    ]),
  ],
  [
    s("Government and civics",[
      ("What is federalism and how does it work in the United States?","Think: power shared between national and state governments","Federalism: a system dividing governmental authority between a central government and constituent units (states). US federalism: federal government has enumerated powers (declared war, coin money, regulate interstate commerce). States have reserved powers (education, police, licensing). Shared powers: taxes, courts. Necessary and proper clause expands federal power."),
      ("What is the difference between civil liberties and civil rights?","Think: freedom from government vs. protection from discrimination","Civil liberties: protections from government overreach (First Amendment freedoms, Fourth Amendment against unreasonable search). Civil rights: protection from discrimination by government and private actors — right to equal treatment regardless of race, sex, religion. Both protected by Constitution and federal law."),
      ("What are the major political ideologies in the United States?","Think: liberal/progressive, conservative, libertarian, socialist","Liberal/progressive: active government role in social welfare and equality; regulate markets. Conservative: limited government, traditional values, free markets, strong national defense. Libertarian: maximum individual liberty, minimal government in both economic and social spheres. Democratic socialist: government ownership or strong regulation of key industries with strong social safety net. Most Americans hold complex, mixed positions."),
      ("What is the role of political parties in American democracy?","Think: coordinate political activity, connect voters to government","Political parties: recruit and support candidates, organize government (majority/minority caucuses), mobilize voters, develop platforms (policy positions). Two-party system reinforced by winner-take-all elections. Critics: parties prioritize winning over governing; partisan polarization gridlocks government."),
    ]),
    s("Contemporary issues",[
      ("What is income inequality and how is it measured?","Think: Gini coefficient; wealth concentrated at the top","Income inequality: the unequal distribution of income across a population. Measured by: Gini coefficient (0 = perfect equality, 1 = one person has everything), income shares (top 1% or 10% of income), or wealth distribution. US income inequality is among the highest of wealthy nations and has increased significantly since the 1970s."),
      ("What are the arguments for and against immigration?","Think: economic benefits vs. labor competition; cultural arguments","For: economic growth (immigrants start businesses, fill labor shortages, pay taxes, drive innovation), humanitarian obligations, cultural enrichment, demographic replacement of aging population. Against: competition for low-wage jobs, cultural change, strain on public services, national security concerns. Evidence generally supports net economic benefits from immigration."),
      ("What is climate justice?","Think: unequal distribution of climate change burdens","Climate justice: the recognition that climate change disproportionately affects those who contributed least to it — low-income countries, indigenous communities, coastal populations, and future generations. The wealthiest nations (who emitted most historically) face less immediate threat than poorer, more vulnerable nations."),
      ("What is the debate around free speech vs. harmful speech?","Think: First Amendment limits vs. real-world harms","Free speech principle: governments should not restrict speech based on content (even offensive speech). Limits: the First Amendment only restricts government, not private actors. Some argue harmful speech (hate speech, incitement) causes real harm. Others argue restricting speech is more dangerous than the speech itself. The debate involves competing values: liberty vs. equality vs. safety."),
    ]),
    s("Historical thinking skills",[
      ("What is chronological reasoning?","Think: understanding change and continuity over time","Chronological reasoning: understanding when events happened, how long processes took, and how causation operates over time. Includes: periodization (how we divide history into eras and why), continuity and change (what persists vs. what transforms), and historical causation (immediate, proximate, and underlying causes)."),
      ("What is the difference between causation and correlation in historical analysis?","Think: one event causing another vs. two events occurring together","Historians must distinguish: correlation (two events occurring together — rising CO2 and rising temperatures) from causation (one causing the other). Historical causation requires: temporal priority (cause precedes effect), correlation, and elimination of alternative causes. Multiple causes are almost always present."),
      ("What is historical empathy and why is it important?","Think: understanding past people in their own context","Historical empathy: understanding why historical actors made the decisions they did within their own context — not the same as sympathy or approval. Avoids presentism (judging the past by today's standards). Helps explain rather than simply condemn. Essential for understanding why reasonable people in the past believed and did things we now recognize as wrong."),
      ("What are the 5 Cs of historical thinking?","Think: Change, Causality, Context, Contingency, Complexity","Change and Continuity: what transforms vs. persists. Causality: why events occurred. Context: understanding the broader setting. Contingency: things could have gone differently (history is not inevitable). Complexity: avoiding simple explanations for complex events. Together these form the foundation of rigorous historical analysis."),
    ]),
  ],
]
print("G9 history complete")

P[9]["cs"] = [
  [
    s("Advanced programming concepts",[
      ("What is recursion?","Think: a function that calls itself","Recursion: a function that calls itself within its own definition. Every recursive function needs: (1) a base case that stops the recursion, (2) recursive case that moves toward the base case. Example: factorial(n) = n × factorial(n-1); base case: factorial(0) = 1."),
      ("What is the difference between recursion and iteration?","Think: self-referential vs. loop","Recursion: solves a problem by breaking it into smaller instances of itself. Iteration: repeats using loops. Both can solve the same problems. Recursion is often more elegant for problems that are naturally recursive (tree traversal, fractals); iteration is often more efficient (less memory overhead)."),
      ("What is a class in Python? Write a simple one.","Think: blueprint with __init__ and methods","class Dog: def __init__(self, name, age): self.name = name; self.age = age. def bark(self): return 'Woof!' myDog = Dog('Rex', 3). myDog.bark() returns 'Woof!'. __init__ is called when an object is created."),
      ("What is polymorphism in OOP?","Think: many forms — same interface, different behavior","Polymorphism: different classes sharing the same method name that behaves differently for each class. Example: both Dog and Cat classes have a make_sound() method — Dog returns 'Woof', Cat returns 'Meow'. Code can call make_sound() on any animal object without knowing the specific type."),
    ]),
    s("Data and databases",[
      ("What is a relational database?","Think: tables with rows and columns linked by relationships","Relational database: stores data in structured tables (relations) with rows (records) and columns (attributes). Tables are related to each other through shared keys. Examples: MySQL, PostgreSQL, SQLite. Used by virtually every business application."),
      ("What is SQL and what can it do?","Think: Structured Query Language for database interaction","SQL: the standard language for querying and managing relational databases. Key commands: SELECT (retrieve data), INSERT (add data), UPDATE (modify data), DELETE (remove data), CREATE TABLE (create structure), JOIN (combine tables). Example: SELECT name, age FROM users WHERE age > 18."),
      ("What is the difference between a primary key and a foreign key?","Think: unique identifier vs. reference to another table","Primary key: uniquely identifies each row in a table (user_id, product_id). Foreign key: a field in one table that references the primary key of another table — creates the relationship between tables. Example: an orders table has a user_id foreign key referencing the users table."),
      ("What is data normalization and why is it important?","Think: organizing database to reduce redundancy","Normalization: organizing database tables to reduce data redundancy and improve data integrity. If the same data is stored in multiple places, updating it requires changing multiple records — and inconsistencies can occur. Normalization puts each piece of data in one place."),
    ]),
    s("Web development",[
      ("What is the difference between front-end and back-end development?","Think: what the user sees vs. server-side logic","Front-end: code running in the browser that users see and interact with (HTML, CSS, JavaScript). Back-end: server-side code handling data storage, business logic, and security (Python, Java, Node.js, databases). Full-stack: both. APIs connect front and back ends."),
      ("What is JavaScript and what makes it unique?","Think: the language of the web browser","JavaScript: the only programming language that runs natively in web browsers. Makes web pages interactive (buttons that respond, animations, form validation, dynamic content updates). Can now also run server-side (Node.js). Asynchronous by nature — doesn't block the browser while waiting for data."),
      ("What is a framework and why do developers use them?","Think: pre-built structure to speed development","Framework: a pre-built structure of code providing common functionality so developers do not start from scratch. Examples: React/Vue/Angular (JavaScript front-end), Django/Flask (Python back-end), Ruby on Rails. Tradeoff: faster development, less flexibility; requires learning the framework's conventions."),
      ("What is the difference between GET and POST HTTP requests?","Think: retrieve vs. submit data","GET: retrieves data from server — data visible in URL, bookmarkable, should not change server state. POST: sends data to server (form submission) — data in request body, not visible in URL, can change server state. GET for reading; POST for creating or modifying data."),
    ]),
    s("Algorithms and complexity",[
      ("What is time complexity? Why does it matter?","Think: how runtime grows with input size","Time complexity describes how an algorithm's runtime scales with input size (n). Why it matters: an O(n^2) algorithm that takes 1 second for 1,000 inputs takes 1,000 seconds for 1,000,000 inputs. O(n log n) is much better. Choosing efficient algorithms is critical for large-scale systems."),
      ("What is the difference between O(n log n) and O(n^2) sorting?","Think: efficient vs. simple sorting algorithms","O(n^2): simple sorts like bubble sort or selection sort. O(n log n): efficient sorts like merge sort and quicksort. For 1 million elements: O(n^2) ≈ 10^12 operations; O(n log n) ≈ 20×10^6 operations. Efficient sorting is dramatically faster at scale."),
      ("What is a greedy algorithm?","Think: make locally optimal choice at each step","Greedy algorithm: at each step, make the choice that seems best at that moment without considering future consequences. Sometimes gives the globally optimal solution (Dijkstra's shortest path); sometimes does not (the 0/1 knapsack problem). Simple and fast, but not always optimal."),
      ("What is dynamic programming?","Think: break problem into subproblems, store solutions to avoid recomputation","Dynamic programming: solving complex problems by breaking them into overlapping subproblems and storing solutions (memoization) to avoid recomputing them. Fibonacci sequence is the classic example — computing F(n) naively recalculates the same values exponentially many times; DP computes each value once."),
    ]),
    s("Artificial intelligence",[
      ("What is the difference between AI, machine learning, and deep learning?","Think: nested subfields","AI (broadest): any technique enabling machines to mimic human intelligence. Machine Learning (subset): systems that learn from data. Deep Learning (subset of ML): uses artificial neural networks with many layers — responsible for most recent AI breakthroughs (image recognition, language models, AlphaGo)."),
      ("What is a neural network?","Think: loosely inspired by the brain; layers of interconnected nodes","Neural network: a computational model of interconnected nodes (neurons) organized in layers. Input layer → hidden layers (do the processing) → output layer. Connections have weights that are adjusted during training. Deep learning = neural networks with many hidden layers."),
      ("What is training data and why does its quality matter?","Think: garbage in, garbage out","Training data: the dataset used to teach a machine learning model. Model performance directly depends on data quality, diversity, and relevance. Biased data produces biased models. Insufficient data leads to overfitting. Data preparation (cleaning, labeling, balancing) is often 80% of the work in ML projects."),
      ("What are the ethical concerns about AI?","Think: bias, privacy, job displacement, autonomy, accountability","Algorithmic bias (AI perpetuates or amplifies human biases), privacy (surveillance, data collection), job displacement (automation of routine work), lack of transparency (black box decision-making), accountability (who is responsible when AI causes harm?), autonomous weapons, and existential risk. These concerns require technical and social/policy solutions."),
    ]),
  ],
  [
    s("Networking and security",[
      ("What is public key cryptography?","Think: asymmetric key pairs — public and private","Public key cryptography uses a key pair: a public key (shared openly) and a private key (kept secret). Anyone can encrypt a message using your public key, but only your private key can decrypt it. Also used for digital signatures: signing with private key, verifying with public key. Basis of HTTPS, email encryption, cryptocurrency."),
      ("What is a man-in-the-middle attack?","Think: attacker intercepts communications between two parties","Man-in-the-middle: an attacker secretly intercepts and potentially alters communications between two parties who believe they are communicating directly. Prevented by: encryption (attacker cannot read the content) and certificate authentication (verifying you are talking to the real server)."),
      ("What is the difference between authentication and authorization?","Think: who are you vs. what can you do","Authentication: verifying who you are (login with username/password, fingerprint, security token). Authorization: determining what an authenticated user is allowed to do (admin can delete accounts; regular user cannot). Both are essential components of access control."),
      ("What are the three factors of authentication?","Think: something you know, have, and are","Something you know: password, PIN, security question. Something you have: phone (authenticator app, SMS code), hardware token. Something you are: biometric (fingerprint, face, iris). Multi-factor authentication (MFA) requires two or more factors — dramatically more secure than single-factor."),
    ]),
    s("Software engineering",[
      ("What is version control with Git? Name three key commands.","Think: tracking changes; git add, commit, push","Git: distributed version control system. Key commands: git add (stage changes), git commit (save snapshot with message), git push (upload to remote), git pull (download from remote), git branch (create branch), git merge (combine branches). Essential for any professional software development."),
      ("What is a code review and why is it important?","Think: another developer reads your code before it is merged","Code review: a developer examines another developer's code before it is merged into the main codebase. Benefits: catches bugs, enforces coding standards, spreads knowledge of the codebase, identifies security vulnerabilities, and improves code quality. In most professional teams, no code is merged without at least one review."),
      ("What is documentation and why do developers often neglect it?","Think: written explanation of how code works","Documentation: written explanation of what code does, how to use it, and why design decisions were made. Often neglected because: writing code is more interesting, documentation becomes outdated, deadline pressure. Good documentation dramatically reduces onboarding time for new developers and makes code maintainable."),
      ("What is technical debt?","Think: shortcuts now that create extra work later","Technical debt: accumulated shortcuts, quick fixes, and suboptimal design decisions that must eventually be addressed. Like financial debt: fine in the short term but compounds over time — becoming increasingly expensive to fix. Good engineering practice pays off technical debt regularly rather than letting it accumulate."),
    ]),
    s("Computing and society",[
      ("What is net neutrality?","Think: internet service providers must treat all internet traffic equally","Net neutrality: the principle that internet service providers (ISPs) should treat all internet traffic equally — not prioritizing, throttling, or charging differently for different content or sources. Debate: proponents say it prevents ISPs from creating tiered internet access; opponents say it prevents investment and innovation in network infrastructure."),
      ("What are the privacy implications of the Internet of Things?","Think: internet-connected devices collecting data about your life","IoT (Internet of Things): everyday objects connected to the internet (smart speakers, thermostats, watches, appliances). Privacy implications: constant data collection about behaviors, locations, and routines. Who owns this data? How is it secured? Can it be subpoenaed or sold? Vulnerabilities in poorly secured IoT devices create large security risks."),
      ("What is open source vs. proprietary software and what are the tradeoffs?","Think: public code vs. secret code","Open source: source code publicly available — community can examine, improve, and distribute it (Linux, Python, Firefox). Proprietary: source code is secret (Windows, macOS, Adobe Photoshop). Tradeoffs: open source allows transparency (security audits) and collaboration; proprietary allows commercial profit protection and may have better user experience and support."),
      ("What is the impact of automation on employment?","Think: technological unemployment and economic transition","Historical precedent: mechanization displaced agricultural and manufacturing workers but created new jobs. Current concern: AI may displace cognitive workers (radiologists, lawyers, accountants) — jobs previously considered automation-resistant. Economists debate whether new jobs will replace old ones as fast as before. Policy responses: retraining programs, universal basic income, expanded education."),
    ]),
    s("Personal projects and portfolios",[
      ("What is a software portfolio and why is it important for tech careers?","Think: collection of projects demonstrating your abilities","Software portfolio: a collection of your projects (code repositories, deployed applications, contributions to open source) that demonstrates your skills to employers. Far more important than a resume in tech — employers want to see actual code, not just claims. Host on GitHub; deploy projects so they are publicly viewable."),
      ("What are good habits for writing maintainable code?","Think: clean code principles","(1) Meaningful variable and function names. (2) Single responsibility: each function does one thing. (3) DRY (Don't Repeat Yourself): avoid duplication. (4) Comments explaining WHY, not WHAT (code shows what; comments explain rationale). (5) Consistent formatting. (6) Tests that verify behavior."),
      ("How do you approach a new programming project?","Think: plan before coding; iterate","(1) Understand the problem completely. (2) Break into smaller sub-problems (decomposition). (3) Research: what libraries or tools exist? (4) Design the solution before coding. (5) Build a minimal working version first. (6) Test and refine. (7) Document. Starting to code immediately before understanding the problem wastes time."),
      ("What is pair programming and what are its benefits?","Think: two developers working on the same code simultaneously","Pair programming: two programmers work together at one computer — one types (driver), one reviews and thinks ahead (navigator). Benefits: reduces bugs (four eyes catch more errors), knowledge sharing, forces communication of thought process, faster onboarding of new developers. Used in many professional teams."),
    ]),
  ],
]
print("G9 CS complete")

P[9]["health"] = [
  [
    s("Emotional intelligence",[
      ("What are the five components of emotional intelligence (EI)?","Think: Goleman's model","(1) Self-awareness: recognizing your emotions. (2) Self-regulation: managing your emotions. (3) Motivation: inner drive beyond external rewards. (4) Empathy: understanding others' emotions. (5) Social skills: managing relationships. Higher EI correlates with better leadership, relationships, and mental health."),
      ("What is emotional regulation and what strategies support it?","Think: managing emotions rather than being controlled by them","Emotional regulation: the ability to manage and respond to emotional experiences effectively. Strategies: cognitive reappraisal (reinterpreting the situation), mindfulness (observing without reacting), emotional labeling (naming the emotion — activates prefrontal cortex, calms amygdala), and distress tolerance (accepting difficult feelings without acting on them)."),
      ("What is the difference between emotional suppression and emotional regulation?","Think: avoiding vs. managing","Suppression: pushing emotions down and not expressing them. Short-term: may work. Long-term: associated with increased stress, cardiovascular problems, and relationship difficulties. Regulation: acknowledging emotions and choosing how to respond — not the same as expressing every emotion immediately."),
      ("How does adolescent brain development affect emotional regulation?","Think: prefrontal cortex not fully developed until ~25","The adolescent prefrontal cortex (rational decision-making, impulse control, emotional regulation) is still developing, while the limbic system (emotional reactivity, reward-seeking) is fully active. This biological mismatch explains heightened emotional intensity, impulsivity, and risk-taking in adolescence — it is developmental, not a character flaw."),
    ]),
    s("Nutrition science",[
      ("What are micronutrients? Why are they important?","Think: vitamins and minerals needed in small amounts","Micronutrients: vitamins and minerals needed in small amounts for proper functioning. Examples: Vitamin D (bone health, immune function), Iron (oxygen transport in blood), Calcium (bones), Vitamin C (immune function, collagen), B vitamins (energy metabolism). Deficiencies can cause specific diseases (scurvy from Vitamin C deficiency, rickets from Vitamin D)."),
      ("What is the difference between complete and incomplete proteins?","Think: essential amino acids","Complete protein: contains all 9 essential amino acids (amino acids the body cannot make — must be obtained from food). Sources: meat, fish, eggs, dairy, soy. Incomplete protein: missing one or more essential amino acids. Sources: most plant proteins. Combine incomplete proteins (rice + beans) to get all essential amino acids."),
      ("What are antioxidants and what is their role?","Think: molecules that neutralize free radicals","Antioxidants: molecules that neutralize free radicals (unstable molecules that damage cells and DNA, contributing to aging and chronic disease). Found in: fruits (berries, citrus), vegetables (leafy greens, broccoli), nuts, tea. Diet rich in antioxidants is associated with reduced risk of cancer, heart disease, and inflammation."),
      ("What is the glycemic index?","Think: how quickly a food raises blood sugar","Glycemic index (GI): ranks foods by how quickly they raise blood sugar. High GI foods (white bread, sugary drinks): rapid spike followed by crash — can contribute to insulin resistance and type 2 diabetes over time. Low GI foods (whole grains, legumes, vegetables): slower, more sustained energy. Important for managing blood sugar."),
    ]),
    s("Exercise physiology",[
      ("What are the energy systems used during exercise?","Think: ATP-PC, glycolytic, oxidative — differ by duration and intensity","ATP-PC (phosphocreatine): immediate energy, 1-10 seconds (sprinting, weightlifting). Glycolytic (lactic acid): fast energy without oxygen, 10 seconds to 2 minutes (400m run). Oxidative (aerobic): sustained energy with oxygen, 2+ minutes (distance running, cycling). Most activities use a mix."),
      ("What is VO2 max and why is it a key fitness measure?","Think: maximum oxygen consumption during intense exercise","VO2 max: the maximum amount of oxygen the body can use during intense exercise. The best single predictor of cardiovascular fitness and aerobic endurance capacity. Higher VO2 max = better ability to deliver and use oxygen. Improved by aerobic training (especially high-intensity interval training)."),
      ("What happens to muscles during and after strength training?","Think: micro-tears heal stronger during recovery","During: resistance overload causes micro-tears in muscle fibers. After: during recovery, the body repairs and reinforces the fibers — making them thicker and stronger (hypertrophy). This is why rest days are essential — muscles grow during recovery, not during exercise."),
      ("What is the role of hormones in exercise and fitness?","Think: cortisol, testosterone, HGH, endorphins","Endorphins: released during exercise — reduce pain and elevate mood (runner's high). HGH (human growth hormone): released during sleep and intense exercise — drives muscle growth and fat metabolism. Cortisol: stress hormone — elevated by overtraining. Testosterone: supports muscle building. Hormonal balance supports optimal fitness."),
    ]),
    s("Health and technology",[
      ("How does screen time affect physical health?","Think: posture, vision, sleep, and sedentary behavior","Excessive screen time contributes to: poor posture (tech neck), eye strain (digital eye strain syndrome), disrupted sleep (blue light suppresses melatonin), sedentary behavior (reduced physical activity), and repetitive strain injuries (wrist, fingers). The key issue is not the screen itself but what replaces healthier behaviors."),
      ("What are the health risks of social media use for adolescents?","Think: comparison, cyberbullying, sleep, anxiety, FOMO","Research links heavy social media use to: increased anxiety and depression (social comparison), cyberbullying, sleep disruption (late-night use), fear of missing out (FOMO), and body image issues. Effects are stronger for passive consumption (scrolling) than active use (communicating with friends). Not inevitable — quality of use matters."),
      ("How can technology support health?","Think: fitness apps, telehealth, health monitoring","Health-supporting uses: fitness tracking apps and wearables (step counts, heart rate, sleep quality), telehealth (remote access to healthcare providers), medication reminders, mental health apps (CBT-based interventions), nutrition tracking. Technology can democratize health information and support — when used intentionally."),
      ("What is digital wellness?","Think: intentional, healthy relationship with technology","Digital wellness: using technology in a way that supports rather than undermines your mental, physical, and social well-being. Practices: digital boundaries (phone-free bedrooms, meal times), intentional consumption (purpose of each technology use), regular digital detoxes, and prioritizing in-person connection."),
    ]),
    s("Health advocacy",[
      ("What is health advocacy?","Think: speaking up for health needs — personal and community","Health advocacy: speaking up for health needs, both individually (navigating the healthcare system, asking questions) and at the community or policy level (supporting public health policies, raising awareness). Every person can advocate for better health in their community."),
      ("What is the difference between primary and urgent care?","Think: routine vs. time-sensitive","Primary care: long-term relationship with a provider for routine health maintenance, preventive care, and management of chronic conditions. Urgent care: facilities for illnesses and injuries needing prompt attention but not emergency care (minor cuts, sprains, infections). Emergency care: life-threatening situations. Using the right level of care avoids overcrowding ERs."),
      ("How does insurance work and why does it matter for health access?","Think: risk pooling; coverage determines access","Health insurance: pooling of risk — many people pay premiums so that costs are covered when anyone needs care. Uninsured individuals often delay or avoid care, leading to worse outcomes and higher long-term costs. Insurance terms: premium (monthly payment), deductible (amount paid before insurance covers), copay (fixed payment per visit)."),
      ("What is preventive care and why is it cost-effective?","Think: catching problems before they become expensive","Preventive care: health services aimed at preventing disease or detecting it early — screenings, vaccinations, counseling. Preventive care reduces long-term costs: treating early-stage cancer costs far less than advanced-stage cancer; preventing diabetes is far cheaper than managing it. Often covered at no cost by insurance because it saves money long-term."),
    ]),
  ],
  [
    s("Mental wellness",[
      ("What is mindfulness and what does research say about its benefits?","Think: non-judgmental present-moment awareness","Mindfulness: paying attention to the present moment without judgment. Well-researched benefits: reduces anxiety and depression symptoms, reduces chronic pain perception, improves emotional regulation, enhances focus and working memory. Practices: meditation, mindful breathing, body scan, mindful movement."),
      ("What is the difference between growth mindset and fixed mindset?","Think: Dweck's research","Fixed mindset: believing intelligence and ability are fixed traits — failure means you're not smart. Growth mindset: believing abilities can be developed through effort and learning — failure is information and part of growth. Growth mindset is associated with greater academic achievement, resilience, and well-being."),
      ("What is resilience and how can it be built?","Think: capacity to recover and adapt from adversity","Resilience: the ability to recover and adapt in the face of adversity, trauma, or stress. Built through: strong social connections, self-regulation skills, sense of purpose and meaning, realistic optimism, learning from failure, and previous experience overcoming challenges."),
      ("How is grief different from depression?","Think: normal response to loss vs. clinical condition","Grief: the normal emotional response to loss (death, divorce, major change). Involves: sadness, but also other emotions (anger, guilt, relief). Generally time-limited, responsive to support, does not involve persistent worthlessness or thoughts of self-harm. Depression: persistent, often involves hopelessness/worthlessness, not always triggered by loss, may require professional treatment."),
    ]),
    s("Sexual health education",[
      ("What are the key components of comprehensive sex education?","Think: beyond biology — includes relationships, consent, health","Comprehensive sex ed covers: reproductive anatomy and physiology, puberty, contraception and disease prevention, consent and healthy relationships, sexual orientation and gender identity, communication skills, and media literacy about sex and relationships. Evidence shows it does not increase sexual activity but does improve health outcomes."),
      ("What is the difference between gender identity, gender expression, and biological sex?","Think: three distinct but related concepts","Biological sex: physiological characteristics (chromosomes, hormones, anatomy). Gender identity: internal sense of being a man, woman, nonbinary, etc. — a psychological phenomenon. Gender expression: how one expresses gender through behavior, clothing, and presentation. These three can be congruent or diverge."),
      ("What is sexual orientation?","Think: pattern of emotional, romantic, and sexual attraction","Sexual orientation: a person's enduring pattern of emotional, romantic, and/or sexual attraction to others. Heterosexual (different gender), homosexual/gay/lesbian (same gender), bisexual (both/multiple genders), asexual (little/no sexual attraction). Sexual orientation is distinct from gender identity."),
      ("What are healthy vs. unhealthy sexual boundaries?","Think: consent, communication, respect, and safety","Healthy: both parties freely and enthusiastically consent, each feels respected and not pressured, communication is open, anyone can stop at any time, both feel safe. Unhealthy: pressure, coercion, guilt, manipulation, ignoring or overriding the other's stated wishes. Consent must be freely given, reversible, informed, enthusiastic, and specific."),
    ]),
    s("Community and global health",[
      ("What is a pandemic and how do they emerge?","Think: global spread of a novel or mutated infectious agent","Pandemic: a disease spreading across multiple countries and continents, affecting large numbers of people. How they emerge: a pathogen (often from animal reservoirs — zoonotic) mutates to infect and spread efficiently between humans. Global travel and trade spread pathogens rapidly. COVID-19 demonstrated the speed and scale of modern pandemic spread."),
      ("What is the role of the World Health Organization?","Think: global coordination of health standards and emergency response","WHO: the United Nations specialized agency for global health. Roles: sets international health standards, monitors global disease, coordinates response to health emergencies (pandemic declarations), provides technical assistance to developing countries, and promotes research and evidence-based health policy."),
      ("How do economic conditions affect population health?","Think: social determinants — poverty is the biggest risk factor for poor health","Poverty is the most powerful predictor of poor health outcomes. Mechanisms: less access to nutritious food, healthcare, safe housing, clean environment; more exposure to stress, violence, and hazardous conditions; less education about health. This is why addressing poverty is a public health intervention."),
      ("What is health equity and how is it different from health equality?","Think: giving everyone what they need vs. giving everyone the same","Equality: giving everyone the same resources (everyone gets the same size crate to stand on). Equity: giving people what they need based on their circumstances (shorter people get taller crates). Health equity aims to eliminate disparities by addressing the underlying conditions that cause them — not just treating everyone identically."),
    ]),
    s("Physical fitness advanced",[
      ("What is periodization in athletic training?","Think: systematically varying training to optimize performance","Periodization: organizing training into cycles with varying intensity and volume to optimize performance and prevent overtraining. Macrocycle (year), mesocycle (weeks to months), microcycle (days to week). Includes planned recovery periods. Used by elite athletes to peak at major competitions."),
      ("What are the principles of injury prevention in sport?","Think: warm-up, technique, progressive overload, recovery","(1) Proper warm-up: dynamic stretching prepares muscles and joints. (2) Correct technique: poor form causes overuse and acute injuries. (3) Progressive overload: gradual increase prevents stress injuries. (4) Adequate recovery: overtraining syndrome from insufficient rest. (5) Addressing imbalances: strengthen stabilizing muscles. (6) Listen to pain signals — pain is information."),
      ("What is the role of nutrition in athletic performance?","Think: fuel, repair, and hydration","Pre-exercise: complex carbs for sustained energy. During: quick carbs for activities over 60-90 minutes (sports drinks, gels). Post-exercise: protein (muscle repair) + carbs (glycogen replenishment) within 30-60 minutes (optimal window). Hydration: even 2% dehydration impairs performance significantly."),
      ("What is the female athlete triad?","Think: low energy availability, low bone density, menstrual disruption","Female athlete triad: a syndrome of three interrelated conditions in female athletes: (1) Low energy availability (often with disordered eating). (2) Low bone density (increased fracture risk). (3) Menstrual dysfunction (missed periods — amenorrhea). Caused by insufficient caloric intake relative to energy expenditure. Requires medical attention."),
    ]),
  ],
]
print("G9 health complete")

# ─── GRADE 10 ───
P[10] = {"math":[], "science":[], "ela":[], "history":[], "cs":[], "health":[]}

P[10]["math"] = [
  [  # Unit 0: Quadratic Functions
    s("Graphing Parabolas", [
      ("What is the vertex of y = (x-3)^2 + 5?", "Vertex form is y = a(x-h)^2 + k, vertex is (h,k)", "The vertex is (3, 5)."),
      ("Does y = -2x^2 + 4x open up or down? Why?", "The sign of 'a' determines direction", "It opens DOWN because a = -2, which is negative."),
      ("Find the axis of symmetry for y = x^2 - 6x + 8.", "Use x = -b/(2a) with a=1, b=-6", "x = -(-6)/(2*1) = 6/2 = 3. Axis of symmetry: x = 3."),
      ("What is the y-intercept of y = 3x^2 - 5x + 2?", "Set x = 0", "y = 3(0)^2 - 5(0) + 2 = 2. Y-intercept: (0, 2)."),
    ]),
    s("Solving Quadratics by Factoring", [
      ("Solve x^2 - 5x + 6 = 0 by factoring.", "Find two numbers that multiply to 6 and add to -5", "(x-2)(x-3) = 0, so x = 2 or x = 3."),
      ("Factor and solve x^2 + 7x + 12 = 0.", "Find two numbers that multiply to 12 and add to 7", "(x+3)(x+4) = 0, so x = -3 or x = -4."),
      ("Solve 2x^2 - 8 = 0.", "Factor out 2 first, then use difference of squares", "2(x^2 - 4) = 0 → 2(x-2)(x+2) = 0 → x = 2 or x = -2."),
      ("Solve x^2 - 9x = 0.", "Factor out x", "x(x-9) = 0 → x = 0 or x = 9."),
    ]),
    s("Quadratic Formula", [
      ("Use the quadratic formula to solve x^2 - 4x - 5 = 0.", "Formula: x = (-b ± sqrt(b^2-4ac)) / 2a", "a=1,b=-4,c=-5. Discriminant = 16+20 = 36. x = (4±6)/2 → x=5 or x=-1."),
      ("What is the discriminant of 2x^2 - 3x + 5 = 0, and what does it tell you?", "Discriminant = b^2 - 4ac", "Discriminant = 9 - 40 = -31. Since it's negative, there are NO real solutions."),
      ("Solve x^2 + 6x + 9 = 0 using the quadratic formula.", "Discriminant = b^2 - 4ac; if 0, one solution", "Discriminant = 36-36 = 0. x = -6/2 = -3. One solution: x = -3 (double root)."),
      ("Solve 3x^2 + 2x - 1 = 0.", "a=3, b=2, c=-1", "Discriminant = 4+12 = 16. x = (-2±4)/6 → x = 1/3 or x = -1."),
    ]),
    s("Completing the Square", [
      ("Complete the square: x^2 + 8x + ___ = (x + ___)^2", "Take half of 8, then square it", "x^2 + 8x + 16 = (x+4)^2. Fill in 16 and 4."),
      ("Rewrite y = x^2 - 6x + 11 in vertex form.", "Complete the square: take half of -6, square it, add and subtract", "y = (x^2 - 6x + 9) + 2 = (x-3)^2 + 2. Vertex form: y = (x-3)^2 + 2."),
      ("Solve x^2 + 4x - 3 = 0 by completing the square.", "Move constant, complete the square on left side", "x^2+4x = 3 → (x+2)^2 = 7 → x = -2 ± sqrt(7)."),
      ("What is the vertex of y = x^2 - 10x + 30?", "Complete the square to get vertex form", "y = (x-5)^2 + 5. Vertex is (5, 5)."),
    ]),
    s("Quadratic Word Problems", [
      ("A ball is thrown up with height h = -16t^2 + 64t + 5. When does it hit the ground?", "Set h = 0 and solve for t", "0 = -16t^2+64t+5. Using quadratic formula: t ≈ 4.08 seconds (taking the positive root)."),
      ("A rectangular garden has perimeter 40 ft and area 96 sq ft. Find the dimensions.", "Let l and w be dimensions. l+w=20, l*w=96", "l and w satisfy x^2-20x+96=0 → (x-8)(x-12)=0. Dimensions: 8 ft by 12 ft."),
      ("Profit P = -2x^2 + 120x - 1000 where x = units sold. Find max profit.", "Max profit at vertex: x = -b/(2a)", "x = -120/(2*-2) = 30 units. Max profit = -2(900)+3600-1000 = $800."),
      ("A ball reaches max height of 25 m at t=2 sec, and starts at h=5m. Write the height equation.", "Use vertex form h = a(t-h_t)^2 + k with vertex (2,25)", "h = a(t-2)^2+25. At t=0: 5=4a+25 → a=-5. Equation: h = -5(t-2)^2 + 25."),
    ]),
  ],
  [  # Unit 1: Polynomial Functions
    s("Polynomial Basics", [
      ("What is the degree and leading coefficient of 4x^5 - 3x^2 + 7?", "Degree = highest exponent; leading coefficient = coefficient of that term", "Degree = 5, leading coefficient = 4."),
      ("Classify: -8x^3 + 2x - 1. Name by degree and number of terms.", "Cubic = degree 3; three terms = trinomial", "Cubic trinomial."),
      ("What is (3x^2 + 2x - 1) + (x^2 - 5x + 4)?", "Combine like terms", "(3x^2+x^2) + (2x-5x) + (-1+4) = 4x^2 - 3x + 3."),
      ("Multiply: (x+2)(x^2 - 3x + 1).", "Distribute x and 2 to each term in the trinomial", "x^3 - 3x^2 + x + 2x^2 - 6x + 2 = x^3 - x^2 - 5x + 2."),
    ]),
    s("Dividing Polynomials", [
      ("Divide x^2 - 5x + 6 by (x-2) using long division.", "Set up polynomial long division", "(x^2-5x+6) / (x-2) = x-3. Check: (x-2)(x-3) = x^2-5x+6. Correct."),
      ("Use synthetic division to divide x^3 - 2x^2 - 5x + 6 by (x-3).", "Use 3 as the divisor in synthetic division", "Coefficients: 1,-2,-5,6. Bring down 1; 3*1=3; -2+3=1; 3*1=3; -5+3=-2; 3*-2=-6; 6-6=0. Quotient: x^2+x-2."),
      ("What does the Remainder Theorem say?", "When dividing f(x) by (x-c), the remainder equals f(c)", "The Remainder Theorem states that when polynomial f(x) is divided by (x-c), the remainder is f(c)."),
      ("Is (x+2) a factor of x^3 + 3x^2 - 4x - 12? Test using the Factor Theorem.", "If f(-2) = 0, then (x+2) is a factor", "f(-2) = -8+12+8-12 = 0. Yes, (x+2) is a factor."),
    ]),
    s("Polynomial Graphs and Zeros", [
      ("How many zeros can a degree-4 polynomial have at most?", "Fundamental Theorem of Algebra: degree = max number of roots", "At most 4 zeros (counting multiplicity)."),
      ("If (x-3)^2 is a factor of f(x), describe the graph behavior at x=3.", "Even multiplicity = touches and turns; odd multiplicity = crosses", "The graph TOUCHES the x-axis at x=3 but does NOT cross it (even multiplicity of 2)."),
      ("Describe the end behavior of f(x) = -3x^4 + 5x - 1.", "Even degree, negative leading coefficient", "Both ends go DOWN (as x→±∞, f(x)→-∞)."),
      ("Find all zeros of f(x) = x^3 - x^2 - 6x.", "Factor out x first", "x(x^2-x-6) = x(x-3)(x+2) = 0. Zeros: x = 0, 3, -2."),
    ]),
    s("Factoring Higher-Degree Polynomials", [
      ("Factor x^3 - 8 completely.", "Difference of cubes: a^3 - b^3 = (a-b)(a^2+ab+b^2)", "x^3-8 = (x-2)(x^2+2x+4)."),
      ("Factor x^4 - 16.", "Difference of squares twice", "x^4-16 = (x^2-4)(x^2+4) = (x-2)(x+2)(x^2+4)."),
      ("Factor 2x^3 + 6x^2 - 8x.", "Factor out GCF first, then factor trinomial", "2x(x^2+3x-4) = 2x(x+4)(x-1)."),
      ("Use the Rational Root Theorem to list possible rational zeros of x^3 - 2x^2 - 5x + 6.", "Possible roots = factors of constant / factors of leading coeff", "Factors of 6: ±1,±2,±3,±6. Leading coeff 1. Possible rational roots: ±1,±2,±3,±6."),
    ]),
    s("Rational Expressions", [
      ("Simplify (x^2-9)/(x+3).", "Factor numerator using difference of squares", "(x+3)(x-3)/(x+3) = x-3, where x ≠ -3."),
      ("Multiply: (x^2-4)/(x+3) * (x+3)/(x-2).", "Factor, cancel common factors", "(x+2)(x-2)/(x+3) * (x+3)/(x-2) = x+2, where x ≠ -3 and x ≠ 2."),
      ("Add: 3/(x+1) + 2/(x-1).", "Find common denominator (x+1)(x-1)", "3(x-1)/[(x+1)(x-1)] + 2(x+1)/[(x+1)(x-1)] = (3x-3+2x+2)/[(x+1)(x-1)] = (5x-1)/(x^2-1)."),
      ("Solve: 2/x + 1/3 = 5/6.", "Multiply through by LCD = 6x", "12 + 2x = 5x → 12 = 3x → x = 4."),
    ]),
  ],
  [  # Unit 2: Exponential and Logarithmic Functions
    s("Exponential Growth and Decay", [
      ("Write the exponential growth equation for a population of 500 growing at 3% per year.", "Use P = P0 * (1+r)^t", "P = 500 * (1.03)^t where t = years."),
      ("A car worth $20,000 depreciates at 15% per year. What is it worth after 5 years?", "Use V = V0 * (1-r)^t", "V = 20000 * (0.85)^5 = 20000 * 0.4437 ≈ $8,874."),
      ("Solve 2^x = 32.", "Rewrite 32 as a power of 2", "2^x = 2^5 → x = 5."),
      ("What is the y-intercept and horizontal asymptote of f(x) = 3 * 2^x - 4?", "Y-intercept: set x=0; asymptote: the shift value", "Y-intercept: f(0) = 3*1-4 = -1, so (0,-1). Horizontal asymptote: y = -4."),
    ]),
    s("Introduction to Logarithms", [
      ("Rewrite log_2(8) = 3 in exponential form.", "log_b(x) = y means b^y = x", "2^3 = 8."),
      ("Evaluate log_10(1000).", "What power of 10 gives 1000?", "10^3 = 1000, so log_10(1000) = 3."),
      ("Rewrite 5^3 = 125 in logarithmic form.", "a^b = c means log_a(c) = b", "log_5(125) = 3."),
      ("Evaluate ln(e^4).", "ln and e^ are inverse functions", "ln(e^4) = 4."),
    ]),
    s("Properties of Logarithms", [
      ("Expand log(x^2 * y / z).", "Use product, quotient, and power rules", "log(x^2) + log(y) - log(z) = 2log(x) + log(y) - log(z)."),
      ("Condense: 3log(x) - 2log(y) + log(z) into a single logarithm.", "Apply power rule first, then product/quotient rules", "log(x^3 * z / y^2)."),
      ("Solve log_3(x) + log_3(5) = log_3(20).", "Combine logs on left using product rule", "log_3(5x) = log_3(20) → 5x = 20 → x = 4."),
      ("What is the change of base formula? Use it to evaluate log_5(100).", "log_b(x) = log(x)/log(b)", "log_5(100) = log(100)/log(5) = 2/0.699 ≈ 2.86."),
    ]),
    s("Solving Exponential and Logarithmic Equations", [
      ("Solve 3^(2x) = 81.", "Rewrite 81 as a power of 3", "3^(2x) = 3^4 → 2x = 4 → x = 2."),
      ("Solve log_2(x+3) = 4.", "Convert to exponential form", "2^4 = x+3 → 16 = x+3 → x = 13."),
      ("Solve e^(2x) = 50 (round to nearest hundredth).", "Take natural log of both sides", "2x = ln(50) ≈ 3.912 → x ≈ 1.96."),
      ("Solve log(x) + log(x-3) = 1 (base 10).", "Combine logs, then convert to exponential form", "log(x(x-3)) = 1 → x(x-3) = 10 → x^2-3x-10=0 → (x-5)(x+2)=0. x=5 (reject x=-2, log undefined)."),
    ]),
  ],
  [  # Unit 3: Trigonometry Basics
    s("Trigonometric Ratios", [
      ("In a right triangle with opposite = 5, adjacent = 12, hypotenuse = 13, find sin, cos, tan of angle A.", "SOH-CAH-TOA: sin=opp/hyp, cos=adj/hyp, tan=opp/adj", "sin A = 5/13, cos A = 12/13, tan A = 5/12."),
      ("If sin(A) = 3/5 in a right triangle, find cos(A) and tan(A).", "Use Pythagorean identity: sin^2 + cos^2 = 1", "cos(A) = 4/5 (adj = 4, hyp = 5). tan(A) = 3/4."),
      ("Find the angle A if tan(A) = 1.", "tan(45°) = 1", "A = 45°."),
      ("A ladder 10 m long leans at 60° from the ground. How high does it reach on the wall?", "Use sin(60°) = opposite/hypotenuse", "sin(60°) = h/10 → h = 10 * sin(60°) = 10 * 0.866 ≈ 8.66 m."),
    ]),
    s("The Unit Circle", [
      ("What are the coordinates of the point on the unit circle at 90°?", "On unit circle, (cos θ, sin θ) gives the coordinates", "(cos 90°, sin 90°) = (0, 1)."),
      ("What is cos(180°) and sin(180°)?", "180° is at the left of the unit circle", "cos(180°) = -1, sin(180°) = 0."),
      ("What is the radian measure of 60°?", "Multiply degrees by pi/180", "60 * (pi/180) = pi/3 radians."),
      ("State the exact value of sin(pi/6).", "pi/6 radians = 30 degrees", "sin(30°) = 1/2."),
    ]),
    s("Graphing Trig Functions", [
      ("What is the period and amplitude of y = 3sin(2x)?", "Amplitude = |A|, Period = 2pi/B for y = A*sin(Bx)", "Amplitude = 3, Period = 2pi/2 = pi."),
      ("Describe the transformation: y = cos(x) - 4.", "The -4 shifts the graph vertically", "The graph of cos(x) is shifted DOWN 4 units."),
      ("What is the period of y = tan(x)?", "tan has a different period than sin/cos", "The period of tan(x) is pi."),
      ("Write the equation of a sine function with amplitude 5 and period 4pi.", "y = A*sin(Bx) where Period = 2pi/B", "Period 4pi means 4pi = 2pi/B → B = 1/2. Equation: y = 5sin(x/2)."),
    ]),
    s("Trigonometric Identities", [
      ("State the Pythagorean identity involving sin and cos.", "Comes from the unit circle equation", "sin^2(x) + cos^2(x) = 1."),
      ("If cos(x) = 4/5, find sin(x) using a Pythagorean identity.", "sin^2(x) = 1 - cos^2(x)", "sin^2(x) = 1 - 16/25 = 9/25 → sin(x) = 3/5 (assuming first quadrant)."),
      ("Simplify sin^2(x)/cos^2(x) + 1.", "Use identity sin^2/cos^2 = tan^2", "tan^2(x) + 1 = sec^2(x)."),
      ("Verify: (1-sin^2(x))/cos(x) = cos(x).", "Replace 1-sin^2(x) using Pythagorean identity", "(cos^2(x))/cos(x) = cos(x). Identity verified."),
    ]),
  ],
  [  # Unit 4: Statistics and Probability
    s("Measures of Central Tendency and Spread", [
      ("Find the mean, median, and mode of: 4, 7, 7, 9, 13.", "Mean=average, Median=middle, Mode=most frequent", "Mean = 40/5 = 8. Median = 7 (middle value). Mode = 7 (appears twice)."),
      ("What is the range and IQR of: 2, 5, 7, 8, 11, 14, 20?", "Range = max-min; IQR = Q3-Q1", "Range = 20-2 = 18. Q1 = 5, Q3 = 14. IQR = 14-5 = 9."),
      ("A data set has mean 50 and standard deviation 5. What range contains 95% of data (normal distribution)?", "95% of data falls within 2 standard deviations of mean", "Mean ± 2*SD = 50 ± 10. About 95% of data falls between 40 and 60."),
      ("What does a small standard deviation tell you about a data set?", "Standard deviation measures spread around the mean", "A small standard deviation means the data points are clustered closely around the mean (low variability)."),
    ]),
    s("Probability Fundamentals", [
      ("A bag has 4 red and 6 blue marbles. What is P(red)?", "Probability = favorable outcomes / total outcomes", "P(red) = 4/10 = 2/5 = 0.4."),
      ("What is the probability of rolling a 3 or 5 on a standard die?", "Events are mutually exclusive, so add probabilities", "P(3 or 5) = 1/6 + 1/6 = 2/6 = 1/3."),
      ("A and B are independent events. P(A)=0.4, P(B)=0.3. Find P(A and B).", "For independent events: P(A and B) = P(A)*P(B)", "P(A and B) = 0.4 * 0.3 = 0.12."),
      ("A deck of 52 cards: what is P(Jack or Heart)?", "Use P(A or B) = P(A)+P(B)-P(A and B)", "P(Jack)=4/52, P(Heart)=13/52, P(Jack of Hearts)=1/52. P = 4/52+13/52-1/52 = 16/52 = 4/13."),
    ]),
    s("Counting Methods", [
      ("How many ways can 5 books be arranged on a shelf?", "This is a permutation of 5 items", "5! = 5*4*3*2*1 = 120 ways."),
      ("A club has 10 members. How many ways can a president and vice president be chosen?", "Order matters — use permutation P(n,r) = n!/(n-r)!", "P(10,2) = 10*9 = 90 ways."),
      ("How many ways can a committee of 3 be chosen from 8 people?", "Order doesn't matter — use combination C(n,r)", "C(8,3) = 8!/(3!5!) = 56 ways."),
      ("What is the difference between a permutation and a combination? Give an example of each.", "Permutations: order matters. Combinations: order doesn't matter.", "Permutation: arranging 3 trophies on a shelf (order matters). Combination: choosing 3 pizza toppings (order doesn't matter)."),
    ]),
  ],
]
print("G10 math complete")

P[10]["science"] = [
  [  # Unit 0: Cell Biology
    s("Cell Structure and Function", [
      ("What is the main difference between prokaryotic and eukaryotic cells?", "Think: does it have a nucleus?", "Eukaryotic cells have a membrane-bound nucleus; prokaryotic cells do not. Eukaryotes also have membrane-bound organelles."),
      ("What is the function of the mitochondria?", "Think: energy currency of the cell", "Mitochondria produce ATP (energy) through cellular respiration. They are called the 'powerhouse of the cell.'"),
      ("What organelle is unique to plant cells and performs photosynthesis?", "Think green and food-making", "Chloroplasts. They contain chlorophyll and convert sunlight + CO2 + water into glucose and oxygen."),
      ("What is the function of the cell membrane?", "Think: selective barrier", "The cell membrane controls what enters and exits the cell. It is selectively permeable, regulating the cell's internal environment."),
    ]),
    s("Cell Transport", [
      ("What is the difference between active and passive transport?", "Think: does it require energy (ATP)?", "Passive transport requires NO energy (moves with concentration gradient). Active transport requires energy (moves against gradient)."),
      ("Define osmosis.", "Specific type of diffusion involving water", "Osmosis is the diffusion of water across a semipermeable membrane from an area of low solute concentration to high solute concentration."),
      ("If a cell is placed in a hypertonic solution, what happens?", "Hypertonic = more solutes outside; water moves out", "The cell shrinks (crenation) because water moves OUT of the cell into the higher-concentration solution by osmosis."),
      ("What is endocytosis?", "Think: cell engulfing material", "Endocytosis is the process by which a cell engulfs materials from outside by wrapping its membrane around them, forming a vesicle."),
    ]),
    s("DNA and Cell Division", [
      ("What is the relationship between DNA, genes, and chromosomes?", "Think: hierarchy from large to small", "Chromosomes are made of DNA coiled around proteins. Genes are specific segments of DNA that code for traits or proteins."),
      ("What happens in the S phase of the cell cycle?", "S stands for synthesis", "DNA replication (synthesis) occurs. Each chromosome is copied so the cell has double the DNA before dividing."),
      ("What is the difference between mitosis and cytokinesis?", "Two separate events in cell division", "Mitosis is the division of the nucleus (chromosomes separate). Cytokinesis is the division of the cytoplasm into two daughter cells."),
      ("How many chromosomes does a human cell have after mitosis?", "Mitosis preserves chromosome number", "46 chromosomes — the same as the parent cell. Mitosis produces genetically identical daughter cells."),
    ]),
    s("Cellular Respiration and Photosynthesis", [
      ("Write the overall equation for photosynthesis.", "Reactants: CO2 and water; Products: glucose and oxygen", "6CO2 + 6H2O + light energy → C6H12O6 + 6O2."),
      ("Write the overall equation for cellular respiration.", "Reverse-ish of photosynthesis; releases energy", "C6H12O6 + 6O2 → 6CO2 + 6H2O + ATP (energy)."),
      ("Where does glycolysis occur in the cell?", "First step of cellular respiration", "Glycolysis occurs in the cytoplasm (cytosol). It does not require oxygen."),
      ("How are photosynthesis and cellular respiration complementary?", "Products of one become reactants of the other", "The products of photosynthesis (glucose, O2) are the reactants of cellular respiration, and vice versa (CO2, H2O). They form a cycle."),
    ]),
  ],
  [  # Unit 1: Genetics
    s("Mendelian Genetics", [
      ("What is the difference between genotype and phenotype?", "Think: genetic code vs. physical appearance", "Genotype is the genetic makeup (allele combination, e.g., Bb). Phenotype is the observable trait (e.g., brown eyes)."),
      ("In a monohybrid cross of Bb x Bb, what is the phenotypic ratio?", "Use a Punnett square: BB, Bb, Bb, bb", "3:1 ratio — 3 dominant phenotype : 1 recessive phenotype."),
      ("What does it mean for an allele to be dominant?", "Only one copy is needed to express the trait", "A dominant allele is expressed whenever present (even in heterozygous form). It masks the recessive allele."),
      ("Two parents are both carriers (Aa) for a recessive disease. What is the probability their child has the disease?", "Carrier = Aa. Cross Aa x Aa", "Punnett square: AA, Aa, Aa, aa → 1/4 or 25% chance the child is aa and has the disease."),
    ]),
    s("Beyond Mendelian Genetics", [
      ("What is incomplete dominance? Give an example.", "Neither allele is fully dominant; blend occurs", "In incomplete dominance, neither allele is fully dominant. Example: red flower (RR) x white flower (WW) → pink flower (RW)."),
      ("What is codominance? How is it different from incomplete dominance?", "Both alleles fully expressed vs. blended", "In codominance, BOTH alleles are fully expressed simultaneously. Example: AB blood type shows both A and B antigens. Unlike incomplete dominance, no blending occurs."),
      ("A man who is X^B X^b (colorblind carrier) and a normal woman X^B X^B have children. Can their sons be colorblind?", "X-linked trait: sons get X from mom", "No. Sons get their X from mom (X^B) and Y from dad. All sons will have normal vision."),
      ("What is the difference between sex-linked and autosomal traits?", "Sex-linked = on X or Y chromosome; autosomal = on other chromosomes", "Autosomal traits are on chromosomes 1-22 (affect males and females equally). Sex-linked traits are on sex chromosomes (X-linked traits affect males more often)."),
    ]),
    s("DNA Structure and Protein Synthesis", [
      ("What is the structure of DNA? Describe the 'twisted ladder' model.", "Think: two strands, bases in the middle, sugar-phosphate outside", "DNA is a double helix: two strands of nucleotides held by hydrogen bonds between complementary bases (A-T, C-G). The backbone is made of sugar and phosphate."),
      ("What are the steps of protein synthesis in order?", "Think: DNA → mRNA → protein", "1. Transcription: DNA is copied into mRNA in the nucleus. 2. Translation: mRNA is read by ribosomes in the cytoplasm to build a protein."),
      ("If a DNA sequence is ATCGGA, what is the mRNA sequence transcribed from it?", "Complementary bases: A-U, T-A, G-C, C-G (RNA uses U instead of T)", "mRNA sequence: UAGCCU."),
      ("What is a codon and what does it code for?", "Codons are groups of 3 bases in mRNA", "A codon is a sequence of 3 mRNA bases that codes for a specific amino acid (or start/stop signal). 64 possible codons specify 20 amino acids."),
    ]),
    s("Mutation and Biotechnology", [
      ("What is a gene mutation? Give an example of a type.", "A change in the DNA sequence", "A gene mutation is a change in the nucleotide sequence of DNA. Example: point mutation (one base changed), insertion (base added), or deletion (base removed)."),
      ("What is the difference between a somatic mutation and a germline mutation?", "Think: body cells vs. reproductive cells", "Somatic mutations occur in body cells and are NOT passed to offspring. Germline mutations occur in egg/sperm cells and CAN be inherited."),
      ("What is CRISPR-Cas9 used for?", "Gene editing technology", "CRISPR-Cas9 is a gene-editing tool that allows scientists to cut and modify specific DNA sequences in an organism's genome with precision."),
      ("What is genetic engineering? Give one agricultural application.", "Modifying an organism's DNA intentionally", "Genetic engineering involves modifying an organism's DNA to introduce new traits. Example: Bt crops have a bacterial gene inserted to make them pest-resistant."),
    ]),
  ],
  [  # Unit 2: Evolution
    s("Evidence for Evolution", [
      ("Name four types of evidence that support evolution.", "Think: fossils, anatomy, DNA, and embryos", "1. Fossil record (shows changes over time). 2. Comparative anatomy (homologous structures). 3. Molecular/DNA evidence (shared sequences). 4. Embryology (similar embryo development across species)."),
      ("What are homologous structures? Give an example.", "Similar structure, different function", "Homologous structures are body parts with similar underlying structure but different functions, suggesting common ancestry. Example: human arm, whale flipper, bat wing — all have same bone arrangement."),
      ("What is a vestigial structure?", "Reduced or functionless remnant of an ancestral structure", "A vestigial structure is a body part that has lost its original function through evolution. Example: human appendix, tailbone (coccyx), wisdom teeth."),
      ("What does biogeography tell us about evolution?", "Distribution of species across geography", "Biogeography (the study of species distribution) provides evidence for evolution: similar environments with different species suggest common ancestors that diversified after geographic separation."),
    ]),
    s("Natural Selection", [
      ("State Darwin's four principles of natural selection.", "Variation, inheritance, overproduction, differential survival", "1. Variation: individuals differ. 2. Inheritance: traits pass to offspring. 3. Overproduction: more offspring than survive. 4. Differential survival: those with advantageous traits survive and reproduce more."),
      ("What is fitness in evolutionary terms?", "Not about physical strength", "Evolutionary fitness is an organism's ability to SURVIVE and REPRODUCE in its environment. It's measured by how many offspring survive to reproduce."),
      ("Explain how antibiotic resistance in bacteria is an example of natural selection.", "Random mutations exist; selection favors resistant bacteria", "Some bacteria randomly have mutations making them resistant. When antibiotics are used, non-resistant bacteria die, but resistant ones survive and reproduce. Over time, the population becomes resistant."),
      ("What is the difference between directional, stabilizing, and disruptive selection?", "Three types of natural selection based on which phenotype is favored", "Directional: one extreme phenotype is favored. Stabilizing: intermediate phenotype is favored (reduces variation). Disruptive: both extremes favored over the intermediate (can split populations)."),
    ]),
    s("Speciation and Macroevolution", [
      ("What is speciation and what usually causes it?", "Formation of new species", "Speciation is the formation of new, distinct species. It usually results from reproductive isolation — when populations can no longer interbreed."),
      ("What is allopatric speciation?", "Think: geographic separation", "Allopatric speciation occurs when a geographic barrier (mountain, river, distance) separates a population, leading to independent evolution and eventual reproductive isolation."),
      ("What does the fossil record show about the pace of evolution?", "Two models: gradual vs. punctuated", "The fossil record supports both gradualism (slow, continuous change) and punctuated equilibrium (long periods of stability interrupted by rapid change)."),
      ("What is adaptive radiation? Give an example.", "Rapid diversification from one ancestor", "Adaptive radiation is the rapid evolution of many species from one common ancestor to fill different ecological niches. Example: Darwin's finches on the Galapagos Islands."),
    ]),
    s("Ecology", [
      ("What is the difference between a food chain and a food web?", "Single path vs. interconnected network", "A food chain is a single linear sequence of energy transfer. A food web is a complex network of interconnected food chains that shows all feeding relationships in an ecosystem."),
      ("What is the 10% rule in ecology?", "Energy transfer between trophic levels", "Only about 10% of energy from one trophic level is transferred to the next. The rest is lost as heat. This is why food chains rarely exceed 4-5 levels."),
      ("Define carrying capacity.", "Maximum sustainable population size", "Carrying capacity (K) is the maximum population size an environment can sustainably support given available resources (food, space, water)."),
      ("What is the difference between primary and secondary succession?", "Think: starting from bare rock vs. disturbed community", "Primary succession starts on bare, lifeless substrate (no soil). Secondary succession occurs after a disturbance destroys an existing community but leaves soil intact (faster process)."),
    ]),
  ],
  [  # Unit 3: Chemistry of Life / Biochemistry
    s("Atoms and Chemical Bonding", [
      ("What is the difference between an ionic and a covalent bond?", "Think: electron transfer vs. electron sharing", "Ionic bonds form when electrons are transferred from one atom to another (forming ions). Covalent bonds form when atoms share electrons."),
      ("Why is water a polar molecule?", "Unequal sharing of electrons due to oxygen's electronegativity", "Oxygen is more electronegative than hydrogen, pulling electrons toward itself. This creates partial negative charge on O and partial positive on H, making water polar."),
      ("What are hydrogen bonds and why are they important in biology?", "Weak attraction between partial charges", "Hydrogen bonds are weak attractions between a partially positive hydrogen and a partially negative atom (like O or N). They are critical for DNA structure, water properties, and protein folding."),
      ("What makes carbon a unique atom for building life's molecules?", "Think: number of bonds carbon can form", "Carbon can form 4 covalent bonds, allowing it to bond with many elements and form long chains, rings, and branches — creating the vast diversity of organic molecules needed for life."),
    ]),
    s("Macromolecules", [
      ("What are the four main types of biological macromolecules?", "Think: carbs, fats, proteins, and nucleic acids", "1. Carbohydrates (energy, structure). 2. Lipids (energy storage, membranes). 3. Proteins (enzymes, structure, transport). 4. Nucleic acids (DNA, RNA — genetic information)."),
      ("What is the monomer of proteins? Of carbohydrates?", "Monomers are the building blocks of polymers", "Proteins: amino acids. Carbohydrates: monosaccharides (e.g., glucose)."),
      ("What is the difference between saturated and unsaturated fats?", "Think: single vs. double bonds in carbon chain", "Saturated fats have no double bonds between carbons (solid at room temp, from animals). Unsaturated fats have one or more double bonds (liquid at room temp, from plants)."),
      ("What do enzymes do and how do they work?", "Biological catalysts that lower activation energy", "Enzymes are biological catalysts that speed up reactions by lowering the activation energy. They have an active site that binds a specific substrate (lock-and-key model)."),
    ]),
    s("pH and Chemical Reactions", [
      ("What does pH measure? What is neutral pH?", "pH scale ranges from 0-14", "pH measures hydrogen ion concentration in a solution. Neutral pH = 7. Below 7 = acidic (more H+ ions). Above 7 = basic/alkaline (fewer H+ ions)."),
      ("What is a buffer and why is it important in the body?", "A substance that resists pH changes", "A buffer is a solution that resists changes in pH when acid or base is added. Blood uses a bicarbonate buffer to maintain pH ≈ 7.4, critical for enzyme function."),
      ("What is the difference between an endothermic and exothermic reaction?", "Think: absorbs heat vs. releases heat", "Endothermic reactions absorb energy (feel cold). Exothermic reactions release energy (feel warm). Cellular respiration is exothermic."),
      ("How does temperature affect enzyme activity?", "Think: optimal temperature and denaturation", "Enzymes work fastest at their optimal temperature (usually ~37°C for human enzymes). At too high a temperature, the enzyme denatures (loses its shape and stops working)."),
    ]),
  ],
]
print("G10 science complete")

P[10]["ela"] = [
  [  # Unit 0: Literary Analysis
    s("Theme and Central Idea", [
      ("What is the difference between a theme and a topic?", "Topic = subject; theme = message about that subject", "A topic is what a text is about (e.g., war). A theme is the author's insight or message about that topic (e.g., 'War destroys innocence')."),
      ("How do you identify theme in a story?", "Look for recurring ideas, character changes, and resolutions", "Identify what the main character learns or how they change. Look for repeated symbols or ideas. Ask: what is the author trying to say about human nature or life?"),
      ("What is a universal theme? Give an example.", "A theme that applies across cultures and time periods", "A universal theme is a message relevant to all humans across time and culture. Example: 'Love requires sacrifice' or 'Power corrupts.'"),
      ("How can two texts have the same topic but different themes?", "Authors convey different messages about the same subject", "Example: Two novels about war — one might argue war is honorable, another that it is pointless. Same topic (war), different themes (honor vs. futility)."),
    ]),
    s("Character Analysis", [
      ("What is the difference between a dynamic and a static character?", "Dynamic = changes; static = stays the same", "A dynamic character undergoes significant change during the story. A static character remains essentially the same throughout."),
      ("How do authors reveal character? List at least three methods.", "STEAL: Speech, Thoughts, Effect on others, Actions, Looks", "Authors reveal character through: (1) dialogue and speech, (2) actions and decisions, (3) thoughts and feelings, (4) how other characters react to them, (5) physical description."),
      ("What is a foil character and why do authors use them?", "A character who contrasts with another", "A foil is a character whose traits contrast with the protagonist's, highlighting the protagonist's qualities. Example: Draco Malfoy as a foil to Harry Potter."),
      ("Analyze how a character's flaw might drive the plot.", "Tragic heroes often have a fatal flaw (hamartia)", "A character's weakness or flaw (hamartia) creates conflict. Example: Macbeth's ambition leads him to murder, which causes his downfall. The flaw is both the cause and consequence."),
    ]),
    s("Literary Devices", [
      ("What is the difference between a simile and a metaphor? Give examples.", "Both compare; simile uses 'like' or 'as'", "Simile: 'Her smile is LIKE sunshine.' Metaphor: 'Her smile IS sunshine.' Similes use like/as; metaphors state equivalence directly."),
      ("What is dramatic irony? Give an example.", "Audience knows something the character doesn't", "Dramatic irony: the audience has knowledge that a character lacks. Example: In Romeo and Juliet, we know Juliet is alive when Romeo finds her, but he believes she is dead."),
      ("Explain how symbolism works in literature. Give an example.", "An object or element represents something beyond itself", "Symbolism is when an author uses something concrete to represent an abstract idea. Example: The green light in The Great Gatsby symbolizes Gatsby's dreams and the American Dream."),
      ("What is the effect of using imagery in a text?", "Imagery appeals to the senses", "Imagery creates vivid mental pictures by appealing to sight, sound, smell, taste, or touch. It helps readers experience what characters experience, creating emotional connection."),
    ]),
    s("Analyzing Narrative Structure", [
      ("What are the five parts of Freytag's Pyramid?", "Rising action leads to climax leads to resolution", "1. Exposition (introduction). 2. Rising Action (conflict builds). 3. Climax (turning point). 4. Falling Action (consequences). 5. Resolution/Denouement (outcome)."),
      ("What is a frame narrative? Give an example.", "A story within a story", "A frame narrative is an outer story that contains one or more inner stories. Example: In The Princess Bride, the grandfather reading to his grandson is the frame; the story of Westley is the inner narrative."),
      ("How does point of view affect how a story is told?", "Who is telling the story changes what we know", "First person (I/me) gives intimacy but limited perspective. Third person limited focuses on one character's thoughts. Third person omniscient knows all characters' inner thoughts."),
      ("What is in medias res and why do authors use it?", "Latin: 'in the middle of things'", "In medias res means starting the story in the middle of the action, then using flashbacks to fill in background. It creates immediate intrigue and engages readers faster."),
    ]),
  ],
  [  # Unit 1: Argumentative Writing
    s("Elements of an Argument", [
      ("What are the three main parts of a classical argument (Aristotle)?", "Ethos, pathos, logos", "Ethos (credibility/ethics), Pathos (emotion/audience connection), Logos (logic/evidence). Effective arguments use all three."),
      ("What is a claim in an argumentative essay?", "The main position or thesis", "A claim is the writer's central assertion — the position they are arguing for. It should be debatable, specific, and provable."),
      ("What is the difference between a claim and a counterclaim?", "Your position vs. the opposing position", "A claim is your position. A counterclaim is an opposing argument. Strong essays acknowledge and refute counterclaims to strengthen their own position."),
      ("What makes evidence 'strong' in an argument?", "Think: relevant, credible, sufficient", "Strong evidence is: (1) Relevant to the claim. (2) From a credible source. (3) Specific (statistics, expert testimony, examples). (4) Accurately cited."),
    ]),
    s("Logical Fallacies", [
      ("What is an ad hominem fallacy?", "Attacking the person instead of the argument", "An ad hominem fallacy attacks the character or motives of an opponent rather than addressing the argument itself. Example: 'You can't trust his views on climate change — he's not a scientist.'"),
      ("What is a straw man fallacy?", "Misrepresenting an opponent's argument", "A straw man fallacy involves misrepresenting or oversimplifying an opponent's position to make it easier to attack. Example: 'They want stricter gun laws — they want to take everyone's guns away!'"),
      ("What is a slippery slope fallacy?", "Assuming one event leads inevitably to extreme outcomes", "Slippery slope: claiming that one event will inevitably lead to a chain of extreme consequences. Example: 'If we allow this, next we'll be doing that, and then everything will fall apart.'"),
      ("What is circular reasoning (begging the question)?", "Using the conclusion as evidence for itself", "Circular reasoning uses the claim as its own evidence. Example: 'This book is the best because it is the greatest book ever written.' The conclusion ('best') is restated as the evidence."),
    ]),
    s("Writing and Revision", [
      ("What is the purpose of a thesis statement in an argumentative essay?", "The roadmap of your argument", "A thesis states your main claim and often previews your supporting reasons. It tells readers what you are arguing and why."),
      ("What is the PEEL paragraph structure?", "Point, Evidence, Explain, Link", "PEEL: (P)oint — state your argument. (E)vidence — provide support. (E)xplain — analyze how evidence supports your point. (L)ink — connect back to the thesis or transition to next point."),
      ("What is the difference between paraphrasing and quoting? When should you use each?", "Restate in own words vs. use exact words", "Paraphrasing restates the idea in your own words (better for integrating ideas smoothly). Direct quoting uses the author's exact words (better when the specific wording matters)."),
      ("What should you include in a rebuttal paragraph?", "Acknowledge the counterclaim, then refute it", "A rebuttal paragraph: (1) Acknowledges the opposing view fairly. (2) Explains why it is weaker than your position. (3) Reinforces your claim with additional evidence."),
    ]),
  ],
  [  # Unit 2: Research and Informational Texts
    s("Evaluating Sources", [
      ("What does CRAAP stand for in source evaluation?", "Criteria for evaluating source credibility", "Currency (how recent), Relevance (fits your topic), Authority (who wrote it), Accuracy (verifiable facts), Purpose (why it was written — bias?)."),
      ("What is the difference between a primary and secondary source?", "Firsthand vs. secondhand account", "Primary sources are firsthand accounts (diaries, original research, speeches). Secondary sources analyze or interpret primary sources (textbooks, articles, biographies)."),
      ("Why is it important to consult multiple sources?", "One source may be biased or incomplete", "Multiple sources help verify information, provide different perspectives, reduce the risk of relying on biased or incomplete information, and build a more complete understanding."),
      ("What is confirmation bias and how can it affect research?", "Seeking out information that confirms existing beliefs", "Confirmation bias is the tendency to favor information that supports what you already believe. It can cause researchers to overlook contradictory evidence and produce biased conclusions."),
    ]),
    s("Reading Informational Texts", [
      ("What is the difference between an implicit and explicit main idea?", "Stated vs. unstated", "Explicit main idea is directly stated in the text. Implicit main idea must be inferred from details, structure, and context."),
      ("What are text structures? List three.", "The organizational pattern of a nonfiction text", "Text structures include: (1) Cause and Effect. (2) Compare and Contrast. (3) Problem and Solution. (4) Sequence/Chronological. (5) Description. Signal words help identify each."),
      ("How do you distinguish fact from opinion in a text?", "Facts can be proven; opinions are beliefs or judgments", "A fact is verifiable and objective ('Water boils at 100°C'). An opinion expresses a belief, attitude, or judgment ('Water is the best drink'). Look for opinion signal words: believe, think, should, best."),
      ("What is the author's purpose (PIE) and how does it affect the content?", "PIE: Persuade, Inform, Entertain", "An author's purpose shapes their choices. To PERSUADE: uses argument and evidence. To INFORM: uses facts and explanations. To ENTERTAIN: uses narrative and emotional engagement."),
    ]),
    s("Research Process and Citation", [
      ("What are the steps of the research process in order?", "Think: question, search, evaluate, synthesize, cite", "1. Choose and narrow a topic. 2. Develop research questions. 3. Find and evaluate sources. 4. Take notes. 5. Organize and synthesize information. 6. Write and cite."),
      ("What information do you need for an MLA citation of a website?", "Author, title, site name, date, URL", "Author's last name, first name. 'Title of Page.' Name of Website, Day Month Year of publication, URL."),
      ("What is plagiarism and how can you avoid it?", "Using others' ideas/words without credit", "Plagiarism is presenting someone else's words or ideas as your own. Avoid it by: quoting and citing sources, paraphrasing accurately, using your own analysis, and tracking all sources."),
      ("What is the difference between a bibliography and an annotated bibliography?", "List of sources vs. list of sources with summaries", "A bibliography lists sources. An annotated bibliography includes a brief summary and evaluation of each source, explaining its relevance and credibility."),
    ]),
  ],
]
print("G10 ELA complete")

P[10]["history"] = [
  [  # Unit 0: Ancient Civilizations
    s("Mesopotamia and Egypt", [
      ("What was the significance of the Tigris and Euphrates rivers to Mesopotamia?", "Rivers provided water for farming in a dry region", "The rivers provided water for irrigation, fertile soil from flooding, trade routes, and transportation — allowing civilization to develop in an otherwise arid region."),
      ("What is a city-state and how were Mesopotamian city-states organized?", "An independent city with surrounding territory", "A city-state is a city that functions as an independent political unit. Mesopotamian city-states like Ur and Uruk had a ruler, priests, farmers, and artisans, with a ziggurat (temple) at the center."),
      ("Why is Hammurabi's Code historically significant?", "One of the earliest written law codes", "Hammurabi's Code (c. 1754 BCE) is one of the oldest written legal codes. It established that laws apply to all people, set punishments for crimes, and showed that government had responsibility for justice."),
      ("What are hieroglyphics and why were they important in ancient Egypt?", "Egyptian writing system using symbols", "Hieroglyphics were the Egyptian writing system using pictographic symbols. They were used to record religious texts, history, and administrative records, and were key to Egyptian culture and bureaucracy."),
    ]),
    s("Greece and Rome", [
      ("What were the main differences between Athens and Sparta?", "Democracy vs. military state", "Athens valued democracy, education, philosophy, and trade. Sparta was a militaristic oligarchy focused on military training, discipline, and conquest. Their values, governance, and daily life differed greatly."),
      ("What were the key contributions of ancient Greece to Western civilization?", "Philosophy, democracy, science, arts", "Democracy, philosophy (Socrates, Plato, Aristotle), drama, the Olympic Games, advances in mathematics and science, architecture (columns, Parthenon), and foundational ideas in logic."),
      ("How did Rome transition from Republic to Empire?", "Series of civil wars and power grabs", "Internal conflicts, civil wars, and the rise of Julius Caesar weakened the Republic. Augustus (Caesar's adopted heir) became the first Emperor in 27 BCE, beginning the Roman Empire while keeping some republican institutions."),
      ("What were the reasons for the fall of the Western Roman Empire?", "Multiple internal and external factors", "Causes include: political instability, economic decline, military pressure from Germanic tribes, overextension of the empire, moral/social decay, and eventually the sack of Rome by Visigoths (410 CE) and Odoacer (476 CE)."),
    ]),
    s("Asia and the Americas in the Ancient World", [
      ("What are the main teachings of Confucius and their impact on East Asia?", "Focus on relationships, hierarchy, and moral virtue", "Confucius taught respect for elders, loyalty, proper social roles, education, and virtue. Confucianism influenced Chinese government, family structure, and education for over 2,000 years and spread to Korea, Japan, and Vietnam."),
      ("What was the Silk Road and why was it important?", "Ancient trade network connecting East and West", "The Silk Road was a network of trade routes linking China, Central Asia, the Middle East, and Europe. It facilitated the exchange of silk, spices, ideas, religions, and technology between civilizations."),
      ("Describe the achievements of the Maya civilization.", "Think: astronomy, writing, architecture", "The Maya developed a sophisticated calendar, written hieroglyphic language, advanced mathematics (including the concept of zero), monumental architecture (pyramids), and complex city-states in Mesoamerica."),
      ("What geographic feature shaped early Indian civilizations?", "Think: rivers and monsoons", "The Indus and Ganges rivers provided fertile land for agriculture. Monsoon rains were crucial for crops. The Himalayas provided protection and resources. These features shaped where and how civilizations like the Indus Valley and later Vedic civilization developed."),
    ]),
    s("World Religions", [
      ("Compare the origins and core beliefs of Hinduism and Buddhism.", "Both originated in India; key differences in teachings", "Hinduism: polytheistic, emphasizes dharma, karma, reincarnation, caste system. Buddhism: founded by Siddhartha Gautama; emphasizes the Four Noble Truths and Eightfold Path to end suffering; rejected caste system."),
      ("What are the Five Pillars of Islam and why are they central to Muslim practice?", "Core obligations for every Muslim", "1. Shahada (declaration of faith). 2. Salat (5 daily prayers). 3. Zakat (charity). 4. Sawm (fasting during Ramadan). 5. Hajj (pilgrimage to Mecca). They define Muslim identity and practice."),
      ("How did Christianity spread throughout the Roman Empire?", "From small sect to official religion of Rome", "Christianity spread through missionary activity (especially Paul), appealing to the poor and enslaved with messages of equality and salvation. Emperor Constantine legalized it in 313 CE; Theodosius made it the state religion in 380 CE."),
      ("What was the impact of the spread of Islam on trade and culture?", "Islamic Golden Age and trade expansion", "The spread of Islam created a vast connected world from Spain to Southeast Asia. This facilitated trade, preserved and advanced Greek knowledge, and led to the Islamic Golden Age with advances in math, science, medicine, and philosophy."),
    ]),
  ],
  [  # Unit 1: Medieval World
    s("Feudalism and the Medieval Church", [
      ("How did feudalism work as a political and economic system?", "Hierarchy of lords, vassals, and serfs", "Feudalism was a hierarchical system: the king granted land (fiefs) to lords in exchange for military service. Lords granted land to knights; peasants/serfs worked the land. It provided protection but little social mobility."),
      ("What role did the Catholic Church play in medieval European life?", "Religious, political, and cultural authority", "The Church controlled education, hospitals, and influenced politics. Everyone from kings to peasants was affected. The Pope could excommunicate rulers. The Church also unified medieval Europe culturally and spiritually."),
      ("What was the Black Death and what were its effects on medieval society?", "Bubonic plague killed 1/3 of Europe", "The Black Death (1347-1353) killed 30-50% of Europe's population. Effects: labor shortages (empowered serfs), questioning of Church authority, economic disruption, and ultimately helped end feudalism and spark social change."),
      ("What were the Crusades and what were their long-term effects?", "Holy wars between Christian and Muslim forces for control of Jerusalem", "The Crusades were a series of religious wars (1096-1291) launched by European Christians to reclaim the Holy Land. Long-term effects: increased trade with the East, cultural exchange, weakened feudal lords, and lasting Christian-Muslim tensions."),
    ]),
    s("The Islamic World and Tang/Song China", [
      ("What was the Islamic Golden Age? Name two achievements.", "Period of scientific and cultural flourishing (8th-13th centuries)", "The Islamic Golden Age saw major advances in mathematics (algebra — al-Khwarizmi), medicine (Ibn Sina/Avicenna), astronomy, philosophy, and the preservation of ancient Greek texts that later influenced the European Renaissance."),
      ("What did the Tang Dynasty contribute to Chinese civilization?", "Think: trade, culture, technology", "The Tang Dynasty (618-907 CE) saw expansion of the Silk Road, advances in poetry and art, development of woodblock printing, and a merit-based civil service exam system that influenced East Asian governance for centuries."),
      ("What were the Four Great Inventions of ancient China and their global impact?", "Paper, printing, gunpowder, compass", "1. Paper (enabled writing and record-keeping). 2. Printing (spread of knowledge). 3. Gunpowder (changed warfare). 4. Magnetic compass (revolutionized navigation and exploration). All transformed world history."),
      ("How did the Mongol Empire facilitate or disrupt trade and cultural exchange?", "Pax Mongolica and the Silk Road", "The Mongol Empire at its peak created the Pax Mongolica — a period of relative stability that allowed trade along the Silk Road. However, Mongol conquests also destroyed cities and disrupted populations across Eurasia."),
    ]),
    s("The Renaissance and Reformation", [
      ("What was the Renaissance and where did it begin?", "Rebirth of art, culture, and learning", "The Renaissance (14th-17th centuries) was a cultural and intellectual movement that began in northern Italy (Florence). It featured renewed interest in classical Greek and Roman ideas, humanism, art, literature, and science."),
      ("What is humanism and how did it differ from medieval thinking?", "Focus on human potential vs. focus on God and afterlife", "Humanism emphasized human potential, reason, education, and achievement in this life. Medieval thinking focused heavily on God, the Church, and preparation for the afterlife. Humanism placed humans at the center of inquiry."),
      ("What were Martin Luther's main criticisms of the Catholic Church?", "Start with the 95 Theses (1517)", "Luther opposed the sale of indulgences (buying forgiveness), the Pope's absolute authority, and corruption in the Church. He argued salvation comes through faith alone (sola fide) and the Bible is the supreme authority (sola scriptura)."),
      ("What was the printing press's role in the Reformation?", "Gutenberg's press (1440s) spread ideas rapidly", "The printing press allowed Luther's ideas to spread rapidly across Europe. The 95 Theses were printed and distributed widely, making it impossible for the Church to suppress the Reformation as they had earlier movements."),
    ]),
  ],
  [  # Unit 2: Early Modern World
    s("Age of Exploration and Colonialism", [
      ("What motivated European exploration in the 15th-16th centuries?", "Think: God, Gold, Glory", "Motivations included: desire for direct trade routes to Asia (spices), spreading Christianity, national glory and competition, new technology (caravel ships, compass), and the profit motive."),
      ("What was the Columbian Exchange and what were its effects?", "Transfer of plants, animals, and diseases between Old and New Worlds", "The Columbian Exchange was the transfer of crops (tomatoes, potatoes, corn, tobacco), animals (horses, cattle), and diseases between Europe/Africa and the Americas. Europeans brought devastating diseases that killed up to 90% of Indigenous populations."),
      ("How did European colonization affect indigenous peoples of the Americas?", "Think: disease, forced labor, cultural destruction", "Indigenous populations suffered: (1) Massive population loss from disease (smallpox, measles). (2) Forced labor in encomienda and mita systems. (3) Destruction of cultures, religions, and political systems. (4) Land theft."),
      ("What was the triangular trade and who was involved?", "Three-way trade network between Europe, Africa, and Americas", "Europe sent manufactured goods to Africa; enslaved Africans were transported to the Americas (Middle Passage); the Americas sent raw materials (sugar, tobacco, cotton) to Europe. This fueled economic growth through exploitation."),
    ]),
    s("Scientific Revolution and Enlightenment", [
      ("What was the Scientific Revolution? Name two key figures.", "Shift from faith-based to evidence-based understanding of the natural world", "The Scientific Revolution (16th-17th centuries) was a transformation in how people understood nature — through observation, experimentation, and reason. Key figures: Copernicus (heliocentric model), Galileo (telescope, physics), Newton (gravity, laws of motion)."),
      ("What is the heliocentric model and why was it controversial?", "Sun-centered vs. Earth-centered view of the solar system", "The heliocentric model (Copernicus, 1543) proposed that the Earth and planets orbit the Sun. It was controversial because it contradicted the Church's geocentric (Earth-centered) view and challenged religious authority."),
      ("What were the core ideas of the Enlightenment?", "Think: reason, natural rights, progress", "The Enlightenment (18th century) promoted reason over tradition, natural rights (life, liberty, property — Locke), the social contract (Rousseau), separation of powers (Montesquieu), and progress through education and science."),
      ("How did Enlightenment ideas influence political revolutions?", "Influence on American and French Revolutions", "Enlightenment ideas about natural rights, consent of the governed, and the right to overthrow tyranny directly inspired the American Revolution (1776) and French Revolution (1789), reshaping concepts of government and citizenship."),
    ]),
    s("Revolutions and Their Impacts", [
      ("What were the main causes of the French Revolution?", "Think: social inequality, Enlightenment ideas, financial crisis", "Causes: rigid class system (Three Estates), financial crisis from war debt, Enlightenment ideas about rights and equality, food shortages, weak leadership of Louis XVI, and resentment of privilege."),
      ("What was the Reign of Terror and what caused it?", "Period of radical violence during the French Revolution (1793-1794)", "The Reign of Terror was a period when the Committee of Public Safety (led by Robespierre) executed tens of thousands as enemies of the Revolution. It resulted from fear of counterrevolution and foreign invasion, and ended with Robespierre's own execution."),
      ("How did the Haitian Revolution differ from other Atlantic revolutions?", "First successful slave revolt creating an independent nation", "The Haitian Revolution (1791-1804) was unique: it was the only successful slave rebellion in history, led by enslaved people who overthrew colonial rule. Haiti became the first Black republic and first Caribbean nation to gain independence."),
      ("What was Napoleon's impact on Europe?", "Military genius, legal reformer, conqueror", "Napoleon spread revolutionary ideals (Napoleonic Code), modernized French administration, and conquered much of Europe. He also provoked nationalist movements across Europe that reshaped the continent after his defeat at Waterloo (1815)."),
    ]),
  ],
]
print("G10 history complete")

P[10]["cs"] = [
  [  # Unit 0: Data Structures
    s("Lists and Arrays", [
      ("What is the difference between an array and a linked list?", "Contiguous memory vs. nodes with pointers", "An array stores elements in contiguous memory (fast random access). A linked list stores elements in nodes that point to the next node (faster insertion/deletion, slower access)."),
      ("How do you access the third element of a list in Python?", "Lists are zero-indexed", "my_list[2] — Python lists are zero-indexed, so index 2 gives the third element."),
      ("What does .append() vs .insert() do in Python lists?", "Add to end vs. add at specific position", ".append(x) adds x to the END of the list. .insert(i, x) inserts x at index i, shifting other elements right."),
      ("What is a 2D array (list of lists)? How do you access element at row 1, column 2?", "A list where each element is itself a list", "A 2D array is a list of lists. Access with matrix[1][2] — first index is the row, second is the column."),
    ]),
    s("Dictionaries and Sets", [
      ("What is a dictionary in Python and how is it different from a list?", "Key-value pairs vs. ordered indexed items", "A dictionary stores key-value pairs (e.g., {'name': 'Alice'}). Lists store ordered items accessed by index. Dictionaries allow fast lookup by key."),
      ("How do you add a new key-value pair to a dictionary?", "Assign to a new key", "my_dict['new_key'] = 'value'. If the key doesn't exist, Python creates it; if it does, the value is updated."),
      ("What is a set in Python? Name two properties.", "An unordered collection of unique elements", "A set is an unordered collection of unique items. Properties: (1) No duplicate elements. (2) No index (unordered). (3) Mutable (can add/remove items). Created with {} or set()."),
      ("When would you use a dictionary over a list?", "Think: lookup vs. sequence", "Use a dictionary when you need fast lookup by key (e.g., storing student grades by name). Use a list when order matters or you need sequential access."),
    ]),
    s("Stacks and Queues", [
      ("What is a stack and what principle does it follow?", "LIFO: Last In, First Out", "A stack is a data structure where the last item added is the first one removed (LIFO). Think of a stack of plates — you add and remove from the top."),
      ("How would you implement a stack in Python using a list?", "Use append() to push, pop() to pop", "Use a list: push = my_stack.append(item); pop = my_stack.pop(). The last appended item is the first popped."),
      ("What is a queue and what principle does it follow?", "FIFO: First In, First Out", "A queue is a data structure where the first item added is the first one removed (FIFO). Think of a line at a store — first person in line is served first."),
      ("Give a real-world example of where a queue is used in computing.", "Think: printer, CPU scheduling", "Print queues: documents are printed in the order they were submitted. Also: CPU task scheduling, handling web server requests, and breadth-first search algorithms."),
    ]),
    s("Searching and Sorting", [
      ("What is the difference between linear search and binary search?", "Check every element vs. divide and conquer", "Linear search checks each element one by one (O(n)). Binary search repeatedly halves the sorted search space (O(log n)) — much faster but requires sorted data."),
      ("Walk through binary search on [2,4,6,8,10] looking for 8.", "Start in the middle, compare, eliminate half", "Middle = 6. 8 > 6, so search right half [8,10]. Middle = 8. Found! Binary search took 2 steps instead of 4 for linear."),
      ("What is bubble sort? What is its time complexity?", "Repeatedly swap adjacent elements if out of order", "Bubble sort compares adjacent pairs and swaps them if out of order, repeating until the list is sorted. Time complexity: O(n^2) — inefficient for large lists."),
      ("What is the advantage of merge sort over bubble sort?", "Divide and conquer vs. repeated comparison", "Merge sort has O(n log n) time complexity vs. bubble sort's O(n^2). Merge sort is much faster for large datasets by recursively splitting and merging sorted halves."),
    ]),
  ],
  [  # Unit 1: Web Development Basics
    s("HTML Structure", [
      ("What does HTML stand for and what is its purpose?", "Markup language for web pages", "HyperText Markup Language. HTML defines the STRUCTURE and CONTENT of web pages using tags like <h1>, <p>, <div>, <img>, and <a>."),
      ("What is the difference between <div> and <span>?", "Block-level vs. inline element", "<div> is a block-level element (takes full width, starts on new line). <span> is an inline element (only takes needed width, stays within a line of text)."),
      ("What is the role of the <head> vs <body> in an HTML document?", "Metadata vs. visible content", "<head> contains metadata (title, links to CSS, charset) not shown to users. <body> contains all visible content (text, images, links, forms)."),
      ("How do you create a hyperlink in HTML?", "Use the <a> tag with href attribute", "<a href='https://example.com'>Link Text</a>. The href attribute specifies the destination URL."),
    ]),
    s("CSS Basics", [
      ("What does CSS stand for and what does it control?", "Styling language for web pages", "Cascading Style Sheets. CSS controls the VISUAL PRESENTATION of HTML: colors, fonts, spacing, layout, and responsiveness."),
      ("What is the CSS box model?", "How HTML elements are sized and spaced", "The box model describes each element as: content (innermost), surrounded by padding, then border, then margin (outermost). All four layers affect an element's total size and spacing."),
      ("What is the difference between a CSS class and an ID?", "Class can be reused; ID must be unique", "Classes (.) can be applied to multiple elements. IDs (#) should be unique on a page. Classes are preferred for styling; IDs are typically used for JavaScript targeting or unique elements."),
      ("What does 'cascading' mean in CSS?", "Styles from multiple sources are combined with a priority order", "Cascading means when multiple style rules apply to an element, they are combined using specificity rules: inline styles > IDs > classes > element selectors. The most specific rule wins."),
    ]),
    s("JavaScript Basics", [
      ("What is the difference between let, const, and var in JavaScript?", "Variable declaration with different scoping and mutability", "var: function-scoped, can be redeclared, hoisted. let: block-scoped, can be reassigned but not redeclared. const: block-scoped, cannot be reassigned. Prefer const and let over var."),
      ("What is a DOM and how does JavaScript interact with it?", "Document Object Model represents the HTML structure", "The DOM is a tree-like representation of an HTML document. JavaScript uses the DOM to select elements (document.getElementById()), change content, styles, and respond to user events."),
      ("Write a JavaScript function that takes a number and returns whether it is even or odd.", "Use the modulo operator %", "function evenOrOdd(n) { return n % 2 === 0 ? 'even' : 'odd'; }"),
      ("What is an event listener in JavaScript? Give an example.", "A function that responds to user actions", "An event listener waits for a specific event (like a click) and runs a function when it happens. Example: button.addEventListener('click', function() { alert('Clicked!'); });"),
    ]),
  ],
]
print("G10 CS complete")

P[10]["health"] = [
  [  # Unit 0: Mental Health
    s("Understanding Mental Health", [
      ("What is mental health and why is it as important as physical health?", "Mental health includes emotional, psychological, and social wellbeing", "Mental health affects how we think, feel, and act. It influences how we handle stress, relate to others, and make choices. Poor mental health can lead to physical illness, and vice versa — they are deeply connected."),
      ("What is the difference between stress, anxiety, and anxiety disorder?", "Normal responses vs. clinical condition", "Stress is a normal response to external pressure. Anxiety is excessive worry about future events. An anxiety disorder is when anxiety is persistent, disproportionate, and interferes with daily life — requiring professional support."),
      ("What are common signs of depression?", "Think: mood, energy, interest, and functioning", "Persistent sadness or emptiness, loss of interest in activities, fatigue, changes in sleep/appetite, difficulty concentrating, feelings of worthlessness, and in severe cases, thoughts of self-harm. Symptoms last 2+ weeks."),
      ("What healthy coping strategies can help manage stress?", "Think: physical, social, and cognitive strategies", "Healthy strategies include: exercise, adequate sleep, talking to a trusted person, journaling, deep breathing/meditation, time management, creative outlets, and knowing when to ask for professional help."),
    ]),
    s("Relationships and Communication", [
      ("What are the characteristics of a healthy vs. unhealthy relationship?", "Think: respect, trust, equality", "Healthy: mutual respect, trust, open communication, individuality, support. Unhealthy: control, jealousy, disrespect, pressure, dishonesty, or fear. Healthy relationships make both people feel valued and safe."),
      ("What is assertive communication? How is it different from passive or aggressive?", "Expressing your needs respectfully and confidently", "Assertive: clearly expressing needs/opinions while respecting others. Passive: avoiding conflict by not expressing needs. Aggressive: expressing needs by violating others' rights. Assertiveness is the healthiest approach."),
      ("What is consent and why is it important in all relationships?", "Voluntary, informed agreement", "Consent is a freely given, reversible, informed, enthusiastic, and specific agreement to any activity. It must be ongoing and can be withdrawn at any time. Consent is essential to respect and safety in any relationship."),
      ("What is the difference between conflict resolution and conflict avoidance?", "Solving the problem vs. avoiding it", "Conflict resolution addresses disagreements through communication, compromise, and empathy. Conflict avoidance ignores or sidesteps issues, which often makes them worse over time. Healthy relationships require resolution skills."),
    ]),
    s("Substance Use and Prevention", [
      ("What is the difference between physical and psychological dependence?", "Body need vs. mental craving", "Physical dependence: the body requires a substance to function normally; withdrawal causes physical symptoms. Psychological dependence: a strong mental craving or compulsion to use a substance for emotional reasons."),
      ("Why are teenagers at higher risk from substance use than adults?", "Brain development is not complete until mid-20s", "The adolescent brain (especially the prefrontal cortex, involved in decision-making) is still developing. Substances can cause long-term damage to developing brains, disrupt memory, learning, and increase addiction risk."),
      ("What are refusal skills and how can you use them?", "Strategies for saying no to peer pressure", "Refusal skills: directly saying 'no,' offering an excuse, suggesting an alternative activity, repeating 'no' if pressured (broken record), and leaving the situation. Practicing these helps resist peer pressure."),
      ("What are short-term and long-term effects of alcohol use?", "Think: impaired judgment vs. organ damage", "Short-term: impaired judgment, coordination, and memory; slowed reaction time; nausea. Long-term: liver damage (cirrhosis), brain damage, addiction, cardiovascular disease, and increased risk of cancer."),
    ]),
  ],
  [  # Unit 1: Physical Fitness and Nutrition
    s("Exercise Science", [
      ("What are the five components of physical fitness?", "Think: heart, muscles, flexibility, body composition", "1. Cardiovascular endurance. 2. Muscular strength. 3. Muscular endurance. 4. Flexibility. 5. Body composition. Together they represent overall physical fitness."),
      ("What is the FITT principle for exercise planning?", "FITT: Frequency, Intensity, Time, Type", "Frequency (how often), Intensity (how hard), Time (how long), Type (what kind of exercise). Using FITT helps create a balanced, progressive exercise plan that meets health goals."),
      ("What is the difference between aerobic and anaerobic exercise? Give examples.", "With oxygen vs. without oxygen", "Aerobic (with oxygen): sustained, moderate-intensity exercise using oxygen for energy (running, cycling, swimming). Anaerobic (without oxygen): short, intense bursts where the body can't supply enough oxygen (sprinting, weightlifting)."),
      ("What is overtraining and how can it be prevented?", "Too much exercise without enough recovery", "Overtraining occurs when exercise volume/intensity exceeds the body's ability to recover. Signs: fatigue, decreased performance, injury, mood changes. Prevention: rest days, adequate sleep, nutrition, and gradual increases in training."),
    ]),
    s("Nutrition and Health", [
      ("What are macronutrients and what are their roles?", "Carbs, proteins, fats — the main energy sources", "Carbohydrates: primary energy source. Proteins: build and repair tissues, enzymes, hormones. Fats: energy storage, cell membranes, fat-soluble vitamins. All three are needed in balance for health."),
      ("What is the difference between simple and complex carbohydrates?", "Sugar vs. starch/fiber", "Simple carbs (sugar): quickly digested, rapid energy spike (candy, white bread). Complex carbs (starch/fiber): slowly digested, sustained energy (whole grains, vegetables). Complex carbs are generally healthier."),
      ("What does BMI measure and what are its limitations?", "Body Mass Index = weight/height^2", "BMI estimates whether someone is underweight, normal, overweight, or obese based on height and weight. Limitations: doesn't account for muscle mass (athletes may have high BMI), age, sex, or fat distribution."),
      ("What are the effects of dehydration on athletic performance?", "Even mild dehydration impairs performance", "Effects: decreased endurance, strength, and coordination; impaired concentration; increased heart rate; muscle cramps; heat illness. Even 2% dehydration can reduce performance by 10-20%."),
    ]),
  ],
]
print("G10 health complete")

# ─── GRADE 11 ───
P[11] = {"math":[], "science":[], "ela":[], "history":[], "cs":[], "health":[]}

P[11]["math"] = [
  [  # Unit 0: Functions and Their Inverses
    s("Function Notation and Operations", [
      ("If f(x) = 2x + 3, evaluate f(5) and f(-2).", "Substitute the value in place of x", "f(5) = 2(5)+3 = 13. f(-2) = 2(-2)+3 = -1."),
      ("Given f(x) = x^2 and g(x) = x+1, find (f+g)(x) and (f*g)(x).", "Add/multiply the two function rules", "(f+g)(x) = x^2 + x + 1. (f*g)(x) = x^2(x+1) = x^3 + x^2."),
      ("Find the composition f(g(x)) if f(x) = 3x and g(x) = x - 2.", "Substitute g(x) into f", "f(g(x)) = f(x-2) = 3(x-2) = 3x - 6."),
      ("What is the domain of f(x) = sqrt(x - 4)?", "The expression under the square root must be >= 0", "x - 4 >= 0 → x >= 4. Domain: [4, ∞)."),
    ]),
    s("Inverse Functions", [
      ("What does it mean for two functions to be inverses?", "They 'undo' each other", "f and g are inverses if f(g(x)) = x and g(f(x)) = x for all x in their domains. They cancel each other out."),
      ("Find the inverse of f(x) = 2x - 6.", "Swap x and y, then solve for y", "y = 2x-6 → swap: x = 2y-6 → x+6 = 2y → y = (x+6)/2. Inverse: f^(-1)(x) = (x+6)/2."),
      ("How does the graph of a function relate to the graph of its inverse?", "Reflection about the line y = x", "The graph of f^(-1) is the reflection of f across the line y = x. Every point (a,b) on f corresponds to point (b,a) on f^(-1)."),
      ("Does every function have an inverse function? Explain.", "Must pass the horizontal line test", "No. A function has an inverse only if it is one-to-one (each y-value corresponds to exactly one x-value). It must pass the Horizontal Line Test."),
    ]),
    s("Piecewise and Absolute Value Functions", [
      ("Evaluate f(x) = {2x if x<0; x^2 if x>=0} at x=-3 and x=4.", "Check which piece applies for each input", "f(-3): use 2x since -3<0 → 2(-3) = -6. f(4): use x^2 since 4>=0 → 16."),
      ("Graph the key features of f(x) = |x - 3| + 2.", "Absolute value shifts: vertex at (h,k) for f(x)=|x-h|+k", "Vertex at (3, 2). The graph is V-shaped opening upward with vertex at (3,2)."),
      ("Solve |2x - 5| = 7.", "Split into two cases: positive and negative", "2x-5 = 7 → x = 6. Or 2x-5 = -7 → x = -1. Solutions: x = 6 or x = -1."),
      ("Solve |x + 1| < 4.", "Absolute value inequality: -4 < x+1 < 4", "-4 < x+1 < 4 → -5 < x < 3. Solution: (-5, 3)."),
    ]),
    s("Rational Functions", [
      ("What is a vertical asymptote? How do you find it for f(x) = 1/(x-3)?", "Value of x where denominator = 0", "A vertical asymptote is a vertical line the graph approaches but never crosses. For f(x) = 1/(x-3): set denominator = 0 → x = 3. Vertical asymptote: x = 3."),
      ("What is a horizontal asymptote? Find it for f(x) = (3x^2)/(x^2+1).", "Compare degrees of numerator and denominator", "Degrees are equal (both 2), so horizontal asymptote = ratio of leading coefficients = 3/1 = 3. Horizontal asymptote: y = 3."),
      ("Find the x-intercepts of f(x) = (x^2-4)/(x+5).", "Set numerator = 0 (where denominator ≠ 0)", "x^2-4 = 0 → (x-2)(x+2) = 0 → x = 2 or x = -2. (Neither makes denominator 0.) X-intercepts: (-2,0) and (2,0)."),
      ("What is a hole in a rational function graph? Find it for f(x) = (x^2-9)/(x-3).", "Hole occurs when factor cancels from numerator and denominator", "f(x) = (x+3)(x-3)/(x-3) = x+3 (with x≠3). There is a HOLE at x = 3 (not an asymptote). The hole is at the point (3, 6)."),
    ]),
    s("Conic Sections", [
      ("What is the standard form of a circle with center (h,k) and radius r?", "Circle equation from the distance formula", "(x-h)^2 + (y-k)^2 = r^2."),
      ("Find the center and radius of x^2 + y^2 - 6x + 4y - 3 = 0.", "Complete the square for x and y", "(x^2-6x+9) + (y^2+4y+4) = 3+9+4 → (x-3)^2 + (y+2)^2 = 16. Center (3,-2), radius 4."),
      ("What is the standard form of an ellipse? Describe what a and b represent.", "Stretched circle with two focal points", "(x^2/a^2) + (y^2/b^2) = 1 where a = semi-major axis (horizontal radius), b = semi-minor axis (vertical radius). If a > b, it's wider than tall."),
      ("What is the vertex form of a parabola that opens sideways (horizontal)?", "Horizontal parabola has y term squared", "x = a(y-k)^2 + h, where vertex is (h,k). If a > 0, opens right; if a < 0, opens left."),
    ]),
    s("Sequences and Series", [
      ("What is the difference between arithmetic and geometric sequences?", "Constant difference vs. constant ratio", "Arithmetic: each term is found by ADDING a constant difference. Geometric: each term is found by MULTIPLYING by a constant ratio."),
      ("Find the 10th term of the arithmetic sequence 3, 7, 11, 15, ...", "Use a_n = a_1 + (n-1)d", "d = 4, a_1 = 3. a_10 = 3 + 9*4 = 3 + 36 = 39."),
      ("Find the sum of the first 5 terms of geometric sequence 2, 6, 18, 54, ...", "S_n = a_1*(r^n - 1)/(r-1)", "r = 3, a_1 = 2. S_5 = 2*(3^5-1)/(3-1) = 2*(243-1)/2 = 242."),
      ("What is the difference between a sequence and a series?", "List of terms vs. sum of terms", "A sequence is an ordered list of numbers. A series is the SUM of the terms of a sequence."),
    ]),
  ],
  [  # Unit 1: Pre-Calculus (Trig and Limits intro)
    s("Advanced Trigonometry", [
      ("State the Law of Sines and when to use it.", "Relates angles and opposite sides", "Law of Sines: a/sin(A) = b/sin(B) = c/sin(C). Use when you know: two angles and a side (AAS/ASA), or two sides and an angle opposite one of them (SSA)."),
      ("State the Law of Cosines and when to use it.", "Extends the Pythagorean Theorem", "c^2 = a^2 + b^2 - 2ab*cos(C). Use when you know: three sides (SSS), or two sides and the included angle (SAS)."),
      ("What is the double angle formula for sin(2x)?", "Comes from the sum formula sin(A+B)", "sin(2x) = 2sin(x)cos(x)."),
      ("Solve sin(x) = sqrt(3)/2 for 0 <= x < 2pi.", "Find all angles in the given range with this sine value", "sin(x) = sqrt(3)/2 at x = pi/3 (60°) and x = 2pi/3 (120°). Two solutions in [0, 2pi)."),
    ]),
    s("Polar Coordinates", [
      ("What is the relationship between polar coordinates (r,theta) and Cartesian (x,y)?", "Conversion formulas", "x = r*cos(theta), y = r*sin(theta). Also: r = sqrt(x^2+y^2), tan(theta) = y/x."),
      ("Convert the polar point (4, pi/3) to Cartesian coordinates.", "Use x = r*cos(theta), y = r*sin(theta)", "x = 4*cos(pi/3) = 4*(1/2) = 2. y = 4*sin(pi/3) = 4*(sqrt(3)/2) = 2sqrt(3). Cartesian: (2, 2sqrt(3))."),
      ("What does the polar graph r = 3 look like?", "r is constant — all points at the same distance from origin", "It is a circle centered at the origin with radius 3."),
      ("Convert x^2 + y^2 = 25 to polar form.", "Replace x^2 + y^2 with r^2", "r^2 = 25 → r = 5. Polar equation: r = 5 (circle of radius 5)."),
    ]),
    s("Introduction to Limits", [
      ("What does lim(x→2) of (x^2-4)/(x-2) equal? Why can't you just plug in x=2?", "Factor and cancel to remove the discontinuity", "Plugging in gives 0/0 (indeterminate). Factor: (x+2)(x-2)/(x-2) = x+2. As x→2, limit = 2+2 = 4."),
      ("What does it mean for a limit to exist?", "Left-hand and right-hand limits must be equal", "A limit exists at x=c if the left-hand limit (x approaching c from the left) equals the right-hand limit (x approaching c from the right)."),
      ("Evaluate lim(x→∞) of (3x^2 + 1)/(x^2 - 5).", "Divide numerator and denominator by the highest power of x", "Divide by x^2: (3 + 1/x^2)/(1 - 5/x^2). As x→∞, 1/x^2→0. Limit = 3/1 = 3."),
      ("What is a continuous function? How can limits test continuity?", "No holes, jumps, or vertical asymptotes", "A function is continuous at x=c if: (1) f(c) exists, (2) the limit exists at c, (3) the limit equals f(c). If any condition fails, the function is discontinuous there."),
    ]),
    s("Vectors", [
      ("What is a vector and how does it differ from a scalar?", "Quantity with both magnitude and direction vs. magnitude only", "A vector has both magnitude (size) and direction (e.g., velocity: 60 mph north). A scalar has only magnitude (e.g., speed: 60 mph). Vectors are represented as arrows."),
      ("Find the magnitude of vector v = <3, 4>.", "Use the Pythagorean theorem", "|v| = sqrt(3^2 + 4^2) = sqrt(9+16) = sqrt(25) = 5."),
      ("Add vectors u = <2, -1> and v = <3, 5>.", "Add corresponding components", "u + v = <2+3, -1+5> = <5, 4>."),
      ("What is the dot product of u = <1, 3> and v = <4, -2>?", "Multiply corresponding components and add", "u · v = 1*4 + 3*(-2) = 4 - 6 = -2."),
    ]),
  ],
  [  # Unit 2: Probability and Statistics (Advanced)
    s("Probability Distributions", [
      ("What is a probability distribution?", "A function describing the probability of each outcome", "A probability distribution lists all possible outcomes and their probabilities. All probabilities must sum to 1."),
      ("What is the expected value (mean) of a discrete random variable?", "Weighted average of all outcomes", "E(X) = sum of [x * P(x)] for all values x. Multiply each outcome by its probability and add all products."),
      ("A die is rolled. X = payout: $10 for 6, -$2 for anything else. Find E(X).", "Use expected value formula", "E(X) = 10*(1/6) + (-2)*(5/6) = 10/6 - 10/6 = 0. This is a fair game."),
      ("What is the difference between a discrete and continuous random variable?", "Countable outcomes vs. any value in a range", "Discrete: takes countable values (e.g., number of heads in 10 flips). Continuous: can take any value in a range (e.g., height, temperature)."),
    ]),
    s("Normal Distribution", [
      ("What are the properties of a normal distribution?", "Bell curve characteristics", "A normal distribution is bell-shaped, symmetric about the mean, with mean = median = mode. Defined by mean (mu) and standard deviation (sigma)."),
      ("What is the Empirical Rule (68-95-99.7 Rule)?", "Percentages within standard deviations of the mean", "About 68% of data falls within 1 SD of the mean; 95% within 2 SD; 99.7% within 3 SD in a normal distribution."),
      ("What is a z-score and how do you calculate it?", "Number of standard deviations from the mean", "z = (x - mu) / sigma. It tells you how many standard deviations a value is above or below the mean."),
      ("A data set has mean = 70 and SD = 8. What percentage of data is between 54 and 86?", "Find how many SDs from mean each bound is", "54 = 70 - 2*8 (2 SDs below). 86 = 70 + 2*8 (2 SDs above). By the Empirical Rule, about 95% of data falls in this range."),
    ]),
    s("Statistical Inference", [
      ("What is the difference between a population and a sample?", "All individuals vs. a subset", "A population is the entire group being studied. A sample is a subset of the population used to make inferences. Samples are used because studying entire populations is often impractical."),
      ("What is sampling bias and how can it be avoided?", "When a sample does not represent the population", "Sampling bias occurs when some members of the population are more likely to be selected. Avoid it using random sampling methods where every member has an equal chance of selection."),
      ("What is a confidence interval and what does it mean?", "Range of values likely to contain the true population parameter", "A confidence interval gives a range of values within which the true population parameter likely falls. A 95% CI means if we repeated the study 100 times, about 95 of the intervals would contain the true value."),
      ("What is a p-value in hypothesis testing?", "Probability of getting results as extreme as observed, assuming null hypothesis is true", "The p-value is the probability of observing results as extreme as those seen if the null hypothesis (H0) is true. Small p-value (typically < 0.05) → reject H0 (results are statistically significant)."),
    ]),
    s("Regression and Correlation", [
      ("What does the correlation coefficient r tell you?", "Strength and direction of linear relationship between two variables", "r ranges from -1 to 1. r = 1: perfect positive linear relationship. r = -1: perfect negative. r = 0: no linear relationship. |r| > 0.7 is generally considered strong."),
      ("What is the difference between correlation and causation?", "Just because two variables are related doesn't mean one causes the other", "Correlation means two variables change together. Causation means one variable CAUSES the change in another. Establishing causation requires controlled experiments, not just correlation."),
      ("What is a least-squares regression line?", "Best-fit line that minimizes squared residuals", "The least-squares regression line (y = mx + b) minimizes the sum of squared differences between actual data points and the predicted values. It is the 'best fit' line through the data."),
      ("What is a residual in regression?", "Difference between actual and predicted values", "A residual = actual y-value - predicted y-value. Positive residuals: actual > predicted. Negative residuals: actual < predicted. Residuals help assess how well the model fits the data."),
    ]),
  ],
  [  # Unit 3: Financial Math
    s("Interest and Investments", [
      ("What is the formula for compound interest?", "A = P(1 + r/n)^(nt)", "A = P(1 + r/n)^(nt) where P = principal, r = annual interest rate, n = times compounded per year, t = years."),
      ("You invest $5,000 at 6% annual interest compounded monthly for 10 years. Find the final amount.", "Use A = P(1+r/n)^(nt) with n=12", "A = 5000(1+0.06/12)^(12*10) = 5000(1.005)^120 ≈ 5000 * 1.8194 ≈ $9,097."),
      ("What is the difference between APR and APY?", "Nominal rate vs. effective annual rate", "APR (Annual Percentage Rate) is the stated interest rate. APY (Annual Percentage Yield) accounts for compounding frequency, showing actual earnings. APY > APR when compounding more than once/year."),
      ("What is the rule of 72?", "Estimate time to double an investment", "Divide 72 by the annual interest rate to estimate years to double money. Example: at 6%, money doubles in ~72/6 = 12 years."),
    ]),
    s("Loans and Budgeting", [
      ("What factors affect monthly mortgage payments?", "Think: principal, rate, term", "Monthly payment depends on: loan amount (principal), interest rate, and loan term (number of years). Higher interest rate or larger principal = higher payment."),
      ("What is amortization?", "How a loan is paid off over time", "Amortization is the process of paying off a loan through regular payments. Early payments go mostly to interest; over time more goes to principal. An amortization schedule shows this breakdown."),
      ("Create a simple monthly budget. You earn $3,000/month. Rent=$900, Food=$400, Transportation=$300, Savings=$300. How much is left?", "Subtract all expenses from income", "Expenses = 900+400+300+300 = $1,900. Remaining: 3000-1900 = $1,100 for other expenses/discretionary spending."),
      ("What is the 50/30/20 budget rule?", "A simple budgeting guideline", "50% of after-tax income → needs (rent, food, utilities). 30% → wants (entertainment, dining out). 20% → savings and debt repayment."),
    ]),
    s("Taxes and Insurance", [
      ("What is the difference between gross income and net income?", "Before taxes vs. after taxes", "Gross income is total earnings before any deductions. Net income ('take-home pay') is what remains after taxes, Social Security, Medicare, and other deductions."),
      ("What is a progressive tax system?", "Tax rate increases as income increases", "In a progressive system, higher earners pay a higher percentage of income in taxes. The US uses this system with brackets — only the income in each bracket is taxed at that rate, not all income."),
      ("What is the purpose of insurance?", "Transferring financial risk", "Insurance protects against large financial losses by paying premiums for coverage. In exchange, the insurer pays out if the covered event occurs, spreading financial risk across many policyholders."),
      ("What is the difference between a deductible and a premium?", "Upfront cost vs. monthly payment", "Premium: regular payment (usually monthly) to maintain insurance coverage. Deductible: the amount YOU pay out-of-pocket before insurance covers costs. Higher deductible = lower premium."),
    ]),
    s("Economic Decision Making", [
      ("What is opportunity cost?", "Value of the next best alternative given up", "Opportunity cost is the value of the best alternative you give up when making a choice. Example: choosing to attend college means giving up income you could earn by working full-time."),
      ("What is the difference between needs and wants in economic decision-making?", "Necessities vs. desires", "Needs are things necessary for survival and basic wellbeing (food, shelter, healthcare). Wants are things that improve quality of life but aren't essential (luxury items, entertainment). Distinguishing helps in budgeting."),
      ("What is marginal thinking in economics?", "Analyzing the benefit of one more unit", "Marginal thinking evaluates whether the benefit of one additional unit exceeds its cost. Example: 'Should I work one more hour?' If the marginal benefit (wage) > marginal cost (fatigue, lost leisure), you should."),
      ("What is supply and demand? What happens when demand increases but supply stays the same?", "Core economic principle determining prices", "Supply = the amount producers offer; Demand = the amount consumers want. When demand increases but supply is constant, there is a shortage, driving prices UP until a new equilibrium is reached."),
    ]),
  ],
  [  # Unit 4: Calculus Preview
    s("Rates of Change", [
      ("What is the difference between average rate of change and instantaneous rate of change?", "Slope of secant line vs. slope of tangent line", "Average rate of change = (f(b)-f(a))/(b-a) — the slope between two points. Instantaneous rate = the slope at a single point — found using limits (the derivative)."),
      ("Find the average rate of change of f(x) = x^2 on [2, 5].", "Use (f(5)-f(2))/(5-2)", "(25-4)/3 = 21/3 = 7."),
      ("What does the derivative of a function represent graphically?", "Slope of the tangent line at a point", "The derivative f'(x) at a point gives the slope of the tangent line to the graph at that point, representing the instantaneous rate of change."),
      ("If a car's position is s(t) = t^2 - 3t, what does s'(t) represent?", "Derivative of position = velocity", "s'(t) represents the car's velocity at time t (rate of change of position with respect to time)."),
    ]),
    s("Basic Derivatives", [
      ("State the power rule for derivatives.", "d/dx of x^n", "Power rule: d/dx [x^n] = n*x^(n-1). Bring down the exponent as a coefficient and reduce the exponent by 1."),
      ("Find the derivative of f(x) = 3x^4 - 2x^2 + 5x - 7.", "Apply the power rule term by term", "f'(x) = 12x^3 - 4x + 5. (Constants disappear; apply power rule to each term.)"),
      ("Find the derivative of f(x) = x^3 at x = 2, and interpret its meaning.", "Find f'(x) first, then evaluate at x=2", "f'(x) = 3x^2. f'(2) = 12. This means the function is increasing at a rate of 12 units per unit of x at x = 2."),
      ("When is a function increasing or decreasing?", "Based on sign of the derivative", "A function is INCREASING where f'(x) > 0 (positive derivative) and DECREASING where f'(x) < 0 (negative derivative)."),
    ]),
    s("Applications of Derivatives", [
      ("How do you find the maximum or minimum of a function using derivatives?", "Critical points where f'(x) = 0 or undefined", "Find where f'(x) = 0 or f'(x) is undefined (critical points). Use the second derivative test or sign chart to classify as maximum, minimum, or neither."),
      ("Find the critical points of f(x) = x^3 - 6x^2 + 9x.", "Set f'(x) = 0 and solve", "f'(x) = 3x^2-12x+9 = 3(x^2-4x+3) = 3(x-1)(x-3) = 0. Critical points: x = 1 and x = 3."),
      ("What does the second derivative test tell us about critical points?", "Concavity at critical points", "If f''(c) > 0 at a critical point: local minimum (concave up). If f''(c) < 0: local maximum (concave down). If f''(c) = 0: inconclusive."),
      ("A company's profit is P(x) = -2x^2 + 80x - 500 where x = units sold. Find the production level that maximizes profit.", "Find x where P'(x) = 0", "P'(x) = -4x + 80 = 0 → x = 20. Maximum profit at 20 units. P(20) = -800+1600-500 = $300."),
    ]),
  ],
  [  # Unit 5: Introduction to Calculus (Integrals)
    s("Area Under a Curve", [
      ("What does the integral represent geometrically?", "Area between the curve and the x-axis", "The definite integral of f(x) from a to b represents the signed area between the curve and the x-axis. Area above x-axis is positive; below is negative."),
      ("What is a Riemann sum?", "An approximation of area using rectangles", "A Riemann sum approximates the area under a curve using n rectangles. As n→∞, the approximation approaches the exact integral."),
      ("State the Power Rule for integration.", "Reverse of the derivative power rule", "Integral of x^n dx = x^(n+1)/(n+1) + C (for n ≠ -1). Add 1 to the exponent and divide by the new exponent; add constant C."),
      ("Find the antiderivative of f(x) = 4x^3 - 6x + 2.", "Apply the power rule for integration term by term", "F(x) = x^4 - 3x^2 + 2x + C."),
    ]),
    s("The Fundamental Theorem of Calculus", [
      ("State the Fundamental Theorem of Calculus (Part 2).", "Connects definite integral to antiderivative", "If F is an antiderivative of f, then the integral from a to b of f(x)dx = F(b) - F(a). This allows exact calculation of definite integrals."),
      ("Evaluate the integral from 1 to 3 of (2x) dx.", "Find antiderivative, then evaluate F(3)-F(1)", "Antiderivative F(x) = x^2. F(3)-F(1) = 9-1 = 8."),
      ("Evaluate the integral from 0 to 2 of (3x^2 - 1) dx.", "Antiderivative then evaluate", "F(x) = x^3 - x. F(2)-F(0) = (8-2)-(0) = 6."),
      ("What is the connection between derivatives and integrals (briefly)?", "They are inverse operations", "Differentiation and integration are inverse operations. The derivative 'undoes' the integral, and the antiderivative 'undoes' the derivative. This is the essence of the Fundamental Theorem of Calculus."),
    ]),
  ],
]
print("G11 math complete")

P[11]["science"] = [
  [  # Unit 0: Atomic Structure and the Periodic Table
    s("Atomic Models", [
      ("Describe the development of the atomic model from Dalton to Bohr.", "Think: solid sphere → plum pudding → nuclear → electron cloud", "Dalton (solid sphere, 1803) → Thomson (plum pudding with electrons, 1897) → Rutherford (nuclear model, positive nucleus, 1911) → Bohr (electrons in fixed orbits, 1913) → Quantum model (electron probability clouds)."),
      ("What are protons, neutrons, and electrons and where are they located?", "Nucleus vs. electron cloud", "Protons (positive, in nucleus), Neutrons (neutral, in nucleus), Electrons (negative, in electron cloud outside nucleus). Protons determine the element; neutrons affect mass number."),
      ("What is an isotope? Give an example.", "Same element, different number of neutrons", "Isotopes are atoms of the same element with the same number of protons but different numbers of neutrons (different mass numbers). Example: Carbon-12 and Carbon-14 are both carbon but have 6 and 8 neutrons respectively."),
      ("How do you read the periodic table entry for an element to find its protons, neutrons, and electrons?", "Atomic number and mass number", "Atomic number = number of protons (and electrons in neutral atom). Mass number = protons + neutrons. Neutrons = mass number - atomic number."),
    ]),
    s("Periodic Trends", [
      ("What is electronegativity and how does it trend on the periodic table?", "Tendency to attract electrons in a bond", "Electronegativity increases going RIGHT across a period (more protons attract electrons more) and INCREASES going UP a group (electrons are closer to the nucleus). Fluorine is most electronegative."),
      ("How does atomic radius trend across a period and down a group?", "Size of atoms across the periodic table", "Across a period (left to right): atomic radius DECREASES (more protons pull electrons in). Down a group: atomic radius INCREASES (more electron shells are added)."),
      ("What is ionization energy and what is its periodic trend?", "Energy to remove an electron", "Ionization energy is the energy required to remove an electron from a neutral atom. It INCREASES left to right across a period and INCREASES up a group (same trends as electronegativity)."),
      ("What determines which group/family an element belongs to?", "Number of valence electrons", "An element's group is determined by its number of valence electrons (outermost shell electrons). Elements in the same group have the same number of valence electrons and similar chemical properties."),
    ]),
    s("Chemical Bonding", [
      ("What is the difference between ionic and covalent bonding?", "Electron transfer vs. electron sharing", "Ionic bonds: electrons are transferred from metal to nonmetal, forming oppositely charged ions that attract. Covalent bonds: electrons are shared between two nonmetals."),
      ("What is a polar covalent bond?", "Unequal sharing of electrons", "A polar covalent bond forms when electrons are shared unequally due to difference in electronegativity. The more electronegative atom gets partial negative charge (delta-). Example: H-F bond."),
      ("Draw the Lewis structure for water (H2O). How many bonding pairs and lone pairs does O have?", "O has 6 valence electrons", "O forms 2 bonds with H (2 bonding pairs) and has 2 lone pairs. Lewis structure: H-O-H with 2 dots on each side of O."),
      ("What is VSEPR theory and how is it used?", "Valence Shell Electron Pair Repulsion", "VSEPR theory predicts molecular geometry based on repulsion between electron pairs. Pairs (bonding and lone) arrange as far apart as possible. Water (2 bonds + 2 lone pairs) is bent (about 104.5°)."),
    ]),
    s("Intermolecular Forces", [
      ("What are the three types of intermolecular forces in order of strength?", "London dispersion < dipole-dipole < hydrogen bonding", "1. London dispersion forces (weakest) — all molecules. 2. Dipole-dipole forces — polar molecules. 3. Hydrogen bonding (strongest) — molecules with N-H, O-H, or F-H bonds."),
      ("Why does water have an unusually high boiling point compared to similar molecules?", "Hydrogen bonding between water molecules", "Water has extensive hydrogen bonding (O-H...O) between molecules. These strong IMFs require more energy to overcome, resulting in a boiling point of 100°C, much higher than similar-sized molecules."),
      ("What is the difference between intramolecular and intermolecular forces?", "Within a molecule vs. between molecules", "Intramolecular forces are bonds WITHIN a molecule (covalent/ionic bonds) — generally stronger. Intermolecular forces are attractions BETWEEN molecules — generally weaker and responsible for physical properties."),
      ("Why do noble gases have such low boiling points?", "Only London dispersion forces, which are very weak", "Noble gases are nonpolar monoatomic atoms with only London dispersion forces (the weakest IMFs). These weak forces mean very little energy is needed to overcome them, resulting in extremely low boiling/melting points."),
    ]),
  ],
  [  # Unit 1: Chemical Reactions and Stoichiometry
    s("Types of Chemical Reactions", [
      ("What are the five main types of chemical reactions?", "Think: synthesis, decomposition, single/double replacement, combustion", "1. Synthesis (A+B→AB). 2. Decomposition (AB→A+B). 3. Single replacement (A+BC→B+AC). 4. Double replacement (AB+CD→AD+CB). 5. Combustion (fuel+O2→CO2+H2O)."),
      ("Balance this equation: H2 + O2 → H2O.", "Add coefficients to balance atoms on each side", "2H2 + O2 → 2H2O. Check: Left = 4H, 2O. Right = 4H, 2O. Balanced."),
      ("What is an oxidation-reduction (redox) reaction?", "Transfer of electrons between reactants", "A redox reaction involves transfer of electrons. The substance losing electrons is OXIDIZED (oxidation state increases). The substance gaining electrons is REDUCED (oxidation state decreases). OIL RIG."),
      ("What is a precipitation reaction? Give an example.", "Two solutions react to form an insoluble solid", "A precipitation reaction forms an insoluble solid (precipitate) when two aqueous solutions are mixed. Example: AgNO3(aq) + NaCl(aq) → AgCl(s) + NaNO3(aq). AgCl is the precipitate."),
    ]),
    s("Stoichiometry", [
      ("What is a mole and why is it used in chemistry?", "6.022 x 10^23 particles", "A mole is 6.022 x 10^23 (Avogadro's number) of particles. It's used to count atoms/molecules in workable quantities, connecting the atomic scale to the lab scale."),
      ("How many grams are in 2 moles of water (H2O)? Molar mass of H=1, O=16.", "Grams = moles x molar mass", "Molar mass of H2O = 2(1)+16 = 18 g/mol. 2 moles * 18 g/mol = 36 grams."),
      ("In the reaction 2H2 + O2 → 2H2O, how many moles of H2O are produced from 4 moles of H2?", "Use mole ratio from balanced equation", "Mole ratio: 2 mol H2O / 2 mol H2 = 1:1. So 4 moles H2 → 4 moles H2O."),
      ("What is a limiting reagent? How do you identify it?", "The reactant that runs out first", "The limiting reagent is the reactant that is completely consumed first, limiting how much product can form. Compare moles of each reactant to stoichiometric ratios to identify which runs out first."),
    ]),
    s("Gas Laws", [
      ("State Boyle's Law. What relationship does it describe?", "Pressure and volume relationship at constant T", "Boyle's Law: P1V1 = P2V2. At constant temperature, pressure and volume of a gas are inversely proportional. If pressure doubles, volume halves."),
      ("State Charles's Law. What relationship does it describe?", "Volume and temperature relationship at constant P", "Charles's Law: V1/T1 = V2/T2. At constant pressure, volume is directly proportional to absolute temperature (in Kelvin). Heating a gas increases its volume."),
      ("What is the Ideal Gas Law equation?", "Combines all gas law variables", "PV = nRT, where P = pressure (atm), V = volume (L), n = moles, R = 0.0821 L·atm/mol·K, T = temperature (K)."),
      ("A gas occupies 4.0 L at 300 K. What volume does it occupy at 600 K at constant pressure?", "Use Charles's Law: V1/T1 = V2/T2", "4.0/300 = V2/600 → V2 = 4.0 * 600/300 = 8.0 L."),
    ]),
    s("Solutions and Acid-Base Chemistry", [
      ("What is molarity and how do you calculate it?", "Moles of solute per liter of solution", "Molarity (M) = moles of solute / liters of solution. Example: 2 moles of NaCl in 0.5 L = 2/0.5 = 4 M solution."),
      ("What is the difference between a strong and weak acid?", "Complete vs. partial ionization in water", "Strong acid (HCl, HNO3, H2SO4): completely ionizes in water. Weak acid (acetic acid, carbonic acid): only partially ionizes, establishing an equilibrium. Strong acids have lower pH at the same concentration."),
      ("What happens in a neutralization reaction?", "Acid + Base → Salt + Water", "An acid and a base react to form a salt and water. Example: HCl + NaOH → NaCl + H2O. The H+ from the acid combines with OH- from the base to form water."),
      ("What is a buffer and how does it resist pH changes?", "Contains both a weak acid and its conjugate base", "A buffer solution contains a weak acid and its conjugate base (or weak base and conjugate acid). It resists pH changes by absorbing H+ or OH- ions. Example: acetic acid/acetate buffer."),
    ]),
  ],
  [  # Unit 2: Thermodynamics and Kinetics
    s("Energy in Reactions", [
      ("What is the difference between endothermic and exothermic reactions?", "Absorbs vs. releases heat", "Exothermic: releases heat to surroundings (negative delta H); products have less energy than reactants. Examples: combustion, most oxidation. Endothermic: absorbs heat (positive delta H). Examples: photosynthesis, dissolving ammonium nitrate."),
      ("What is activation energy?", "Energy barrier to start a reaction", "Activation energy is the minimum energy required for reactants to transform into products. It represents the energy barrier that must be overcome for a reaction to proceed."),
      ("How do catalysts affect a reaction?", "Lower activation energy without being consumed", "Catalysts provide an alternative pathway with LOWER activation energy. This speeds up the reaction without being consumed or changing the overall energy released/absorbed."),
      ("What is Hess's Law?", "Enthalpy is a state function", "Hess's Law states that the total enthalpy change of a reaction is the same regardless of the path taken. You can add enthalpy changes of multiple reactions to find the enthalpy of a target reaction."),
    ]),
    s("Reaction Rates and Equilibrium", [
      ("Name three factors that affect the rate of a chemical reaction.", "Think: concentration, temperature, surface area, catalysts", "1. Concentration (more reactants = more collisions). 2. Temperature (higher temp = more energy/collisions). 3. Surface area (more surface = more contact). 4. Presence of a catalyst."),
      ("What does it mean for a reaction to be at equilibrium?", "Forward and reverse rates are equal", "At equilibrium, the rate of the forward reaction equals the rate of the reverse reaction. Concentrations of reactants and products remain constant (though NOT necessarily equal)."),
      ("What is Le Chatelier's Principle?", "A system in equilibrium responds to stress by shifting to reduce the stress", "Le Chatelier's Principle: if a stress (change in concentration, pressure, or temperature) is applied to a system at equilibrium, the system shifts to counteract the stress and re-establish equilibrium."),
      ("According to Le Chatelier's Principle, what happens if you increase temperature for an endothermic reaction?", "Temperature increase favors the endothermic (forward) direction", "For an endothermic reaction, heat is a 'reactant.' Increasing temperature shifts equilibrium to the RIGHT (forward), producing more products and consuming more heat."),
    ]),
    s("Nuclear Chemistry", [
      ("What is radioactive decay?", "Unstable nuclei emit particles/energy", "Radioactive decay is when an unstable atomic nucleus loses energy by emitting radiation (alpha, beta, gamma particles). This changes the nucleus into a different element."),
      ("What is the difference between alpha, beta, and gamma radiation?", "Three types of nuclear radiation", "Alpha (α): helium nucleus (2p+2n), low penetration. Beta (β): electron or positron, medium penetration. Gamma (γ): high-energy photon, highest penetration. Alpha is stopped by paper; beta by aluminum; gamma needs lead/concrete."),
      ("What is half-life and how is it used?", "Time for half of a radioactive sample to decay", "Half-life is the time for half of a radioactive substance to decay. After 1 half-life: 50% remains. After 2: 25%. After 3: 12.5%. Used in carbon-14 dating and medical applications."),
      ("What is the difference between nuclear fission and nuclear fusion?", "Splitting atoms vs. combining atoms", "Fission: a heavy nucleus splits into smaller nuclei, releasing energy (used in nuclear power plants and atomic bombs). Fusion: light nuclei combine to form a heavier nucleus, releasing more energy (powers the Sun)."),
    ]),
    s("Environmental Chemistry", [
      ("What causes the greenhouse effect and how does it lead to climate change?", "Greenhouse gases trap heat in the atmosphere", "Greenhouse gases (CO2, CH4, N2O, water vapor) absorb infrared radiation emitted by Earth's surface, trapping heat. Human activities (fossil fuels, deforestation) increase these gases, enhancing the greenhouse effect and warming the planet."),
      ("What is acid rain and what causes it?", "Rain with lower pH from air pollutants", "Acid rain forms when sulfur dioxide (SO2) and nitrogen oxides (NOx) — mainly from burning fossil fuels — react with water vapor to form sulfuric and nitric acids. This lowers rainfall pH, harming ecosystems."),
      ("What is ozone and why is the ozone layer important?", "O3 in the stratosphere filters UV radiation", "Ozone (O3) in the stratosphere absorbs harmful ultraviolet (UV) radiation from the Sun. Without the ozone layer, increased UV exposure would cause higher rates of skin cancer, cataracts, and damage to ecosystems."),
      ("What are CFCs and why were they banned?", "Chlorofluorocarbons destroy ozone", "CFCs (used in refrigerants and aerosols) rise to the stratosphere where UV radiation breaks them apart, releasing chlorine atoms that destroy ozone molecules. The Montreal Protocol (1987) banned CFCs globally."),
    ]),
  ],
  [  # Unit 3: Physics Fundamentals
    s("Motion and Forces", [
      ("What is the difference between speed and velocity?", "Magnitude vs. magnitude AND direction", "Speed is a scalar — only magnitude (e.g., 60 mph). Velocity is a vector — magnitude AND direction (e.g., 60 mph north). Velocity can change even if speed is constant (changing direction)."),
      ("State Newton's three laws of motion.", "Foundation of classical mechanics", "1st: Object stays at rest or in uniform motion unless a net force acts on it (inertia). 2nd: F = ma (net force = mass x acceleration). 3rd: For every action, there is an equal and opposite reaction."),
      ("A 5 kg object experiences a net force of 20 N. What is its acceleration?", "Use F = ma, solve for a", "a = F/m = 20/5 = 4 m/s^2."),
      ("What is friction and what are its two types?", "Force opposing relative motion between surfaces", "Friction is a force that opposes motion between surfaces in contact. Static friction: prevents motion from starting. Kinetic (sliding) friction: opposes motion already occurring. Static friction is usually greater."),
    ]),
    s("Energy and Momentum", [
      ("What is the difference between kinetic and potential energy?", "Energy of motion vs. stored energy", "Kinetic energy: energy of motion. KE = (1/2)mv^2. Potential energy: stored energy due to position. Gravitational PE = mgh. Energy converts between these forms."),
      ("A 2 kg ball is dropped from 10 m height. What is its speed just before hitting the ground?", "Use conservation of energy: PE = KE", "mgh = (1/2)mv^2 → gh = v^2/2 → v = sqrt(2gh) = sqrt(2*10*10) = sqrt(200) ≈ 14.1 m/s."),
      ("State the law of conservation of momentum.", "Total momentum in a closed system is constant", "In a closed system with no external forces, total momentum is conserved. p_before = p_after. p = mv (momentum = mass x velocity)."),
      ("What is the difference between elastic and inelastic collisions?", "Kinetic energy conserved vs. not conserved", "Elastic: both momentum AND kinetic energy conserved (billiard balls). Inelastic: momentum conserved but kinetic energy is lost to heat/deformation. Perfectly inelastic: objects stick together after collision."),
    ]),
  ],
]
print("G11 science complete")

P[11]["ela"] = [
  [  # Unit 0: American Literature
    s("Foundations of American Literature", [
      ("What themes are common in early American literature (Puritan and Revolutionary period)?", "Think: religion, nature, liberty, and identity", "Common themes: religious faith and divine providence (Puritan), the struggle for political freedom and rights (Revolutionary), and the relationship between humans and nature. These foundational concerns shaped American literary identity."),
      ("What is the Transcendentalist movement and who were its key figures?", "19th-century philosophical/literary movement emphasizing nature and individual spirit", "Transcendentalism (1830s-1850s) celebrated nature, individualism, and spiritual intuition over organized religion and rationalism. Key figures: Ralph Waldo Emerson ('Self-Reliance'), Henry David Thoreau ('Walden'), and Walt Whitman."),
      ("What is the American Dream and how do American authors challenge or celebrate it?", "The idea that anyone can succeed through hard work", "The American Dream is the belief that hard work leads to success and prosperity. Authors like F. Scott Fitzgerald (The Great Gatsby) critique it as illusory; others like Horatio Alger celebrate it. It remains a central, contested theme."),
      ("What is naturalism in American literature? How does it differ from realism?", "Both depict reality, but naturalism emphasizes forces beyond individual control", "Realism depicts life as it is, focusing on ordinary people. Naturalism (influenced by Darwin) depicts humans as shaped by forces — biology, environment, fate — largely beyond their control. Example: Jack London, Stephen Crane."),
    ]),
    s("The Harlem Renaissance", [
      ("What was the Harlem Renaissance and when did it occur?", "African American cultural flowering in New York in the 1920s", "The Harlem Renaissance was a cultural, artistic, and intellectual movement of African Americans centered in Harlem, New York in the 1920s. It celebrated Black identity and produced major works in literature, music, and art."),
      ("What were the major themes of Harlem Renaissance literature?", "Think: identity, racism, pride, migration", "Themes include: Black identity and pride, the experience of racial discrimination, the Great Migration (from South to North), urban life, jazz and blues culture, and the desire for social and political equality."),
      ("Who was Langston Hughes and what was his literary significance?", "Major poet of the Harlem Renaissance", "Langston Hughes (1902-1967) was a central figure of the Harlem Renaissance whose poetry celebrated Black life, incorporated jazz rhythms, and addressed racial inequality with both pride and protest. Key works: 'The Negro Speaks of Rivers,' 'Harlem.'"),
      ("What is the significance of the poem 'Harlem' (A Dream Deferred) by Hughes?", "Explores what happens to unfulfilled dreams", "The poem asks 'What happens to a dream deferred?' through a series of similes (raisin, sore, rotten meat, crust, heavy load). It suggests unrealized dreams of Black Americans may eventually 'explode' — pointing to social unrest if inequality persists."),
    ]),
    s("The Modern American Novel", [
      ("What are the major characteristics of modernist literature?", "Fragmented form, stream of consciousness, disillusionment", "Modernist literature features: stream of consciousness narration, fragmented structure, alienation and disillusionment, experimentation with form, and a break from traditional values following WWI."),
      ("What is the central theme of The Great Gatsby (Fitzgerald)?", "The hollow nature of the American Dream", "The Great Gatsby critiques the American Dream by showing Gatsby's wealth cannot overcome class barriers or win Daisy's love. The novel exposes the moral corruption, materialism, and illusion at the heart of 1920s prosperity."),
      ("What is To Kill a Mockingbird about and what themes does it explore?", "Harper Lee's novel about racial injustice in the American South", "Set in 1930s Alabama, it follows Scout Finch whose father Atticus defends a Black man falsely accused of assaulting a white woman. Themes: racial injustice, moral courage, empathy, loss of innocence, and social inequality."),
      ("What does Atticus Finch mean when he says 'You never really understand a person until you consider things from his point of view'?", "Lesson about empathy as moral foundation", "Atticus is teaching Scout to practice empathy — to suspend judgment and try to see the world through another person's experiences. This is the moral foundation of the novel and a counterforce to prejudice and injustice."),
    ]),
    s("Rhetorical Analysis of American Speeches", [
      ("Identify ethos, pathos, and logos in Martin Luther King Jr.'s 'I Have a Dream' speech.", "Three rhetorical appeals", "Ethos: MLK's moral authority as a civil rights leader and minister. Pathos: vivid imagery of injustice and dreams that evoke emotion. Logos: references to the Declaration of Independence and Constitution as logical foundation for civil rights claims."),
      ("What makes Abraham Lincoln's Gettysburg Address rhetorically powerful?", "Concision, elevated diction, and unifying purpose", "Its power comes from its brevity (272 words), elevated and biblical language, parallel structure ('of the people, by the people, for the people'), and its reframing of the Civil War as a test of democratic ideals, not just a battle over slavery."),
      ("What is antithesis as a rhetorical device? Find it in a famous speech.", "Contrasting ideas in parallel structure", "Antithesis places contrasting ideas side by side in similar grammatical structure. Example: JFK's 'Ask not what your country can do for you — ask what you can do for your country.' The contrast emphasizes the shift from receiving to giving."),
      ("What is anaphora and what effect does it create?", "Repetition of words/phrases at the beginning of successive clauses", "Anaphora is the repetition of a word or phrase at the start of successive clauses. Example: MLK's repeated 'I have a dream...' creates rhythm, emphasis, and emotional momentum, making the message memorable and powerful."),
    ]),
  ],
  [  # Unit 1: Writing for Purpose
    s("Research and Synthesis Writing", [
      ("What is synthesis in writing and how does it differ from summary?", "Combining multiple sources around your own idea", "Summary restates what one source says. Synthesis brings together ideas from multiple sources to support or develop YOUR own argument or analysis. Synthesis shows how sources relate to each other and to your thesis."),
      ("What is an annotated bibliography and when is it used?", "List of sources with evaluation notes", "An annotated bibliography lists each source in proper citation format followed by a brief paragraph describing: what the source is about, how it is useful to your research, and an assessment of its credibility and perspective."),
      ("How do you avoid plagiarism when using multiple sources?", "Cite all borrowed ideas and words; use your own analysis", "Always cite the source when using ideas, facts, or quotes — even when paraphrasing. Use quotation marks for direct quotes. Develop your own analysis around the sources. Keep detailed notes with source information while researching."),
      ("What is the difference between a primary and a secondary source? Give an example of each for a research paper on the Civil War.", "Firsthand vs. secondhand accounts", "Primary: a letter written by a Union soldier (firsthand account). Secondary: a history textbook chapter on the Civil War (analysis of primary sources). Both are valuable; primary sources provide direct evidence, secondary provide context and interpretation."),
    ]),
    s("Style and Voice", [
      ("What is tone in writing and how does a writer control it?", "The author's attitude toward the subject and audience", "Tone is the emotional quality or attitude conveyed in writing. Writers control tone through word choice (diction), sentence structure, imagery, and what details are emphasized or omitted. Tone can be formal, ironic, nostalgic, bitter, etc."),
      ("What is the difference between formal and informal writing? When is each appropriate?", "Register choice based on audience and purpose", "Formal writing: professional vocabulary, complete sentences, no contractions, objective tone (used for academic essays, business communications). Informal writing: conversational, uses contractions/slang, first person (used for personal essays, friendly correspondence)."),
      ("What is sentence variety and why is it important?", "Mixing sentence types and lengths improves readability", "Sentence variety means mixing short, punchy sentences with longer, complex ones. It prevents monotony, controls rhythm, and directs emphasis. A series of identical sentence structures becomes tedious; variation keeps readers engaged."),
      ("What is passive vs. active voice? Why prefer active voice?", "Who is doing the action?", "Active voice: the subject performs the action ('The dog bit the man'). Passive voice: the subject receives the action ('The man was bitten by the dog'). Active voice is usually clearer, more direct, and more engaging."),
    ]),
    s("Personal Essay and College Writing", [
      ("What makes a college application essay effective?", "Authenticity, specificity, and voice", "An effective college essay: reveals something genuine and specific about you, uses concrete details and storytelling (not generalizations), has a clear personal voice, and connects your experience to your character, growth, or values."),
      ("What is the difference between a narrative and a reflective essay?", "Telling a story vs. examining meaning", "A narrative essay tells a story with plot, characters, and setting. A reflective essay examines your own thoughts, feelings, and the significance of an experience. College essays often combine both: tell a story AND reflect on its meaning."),
      ("What is a 'show don't tell' approach in writing? Give an example.", "Specific details reveal meaning instead of stating it directly", "Instead of telling ('I was nervous'), show through specific details ('My hands were trembling; I kept re-reading the first sentence without absorbing a word'). Showing creates a vivid experience; telling is flat and abstract."),
      ("How do you write a strong opening for a personal essay?", "Hook readers immediately with specificity or action", "Start in the middle of the action (in medias res), with a vivid sensory detail, a surprising statement, or a compelling question. Avoid generic openings like 'I have always...' or 'From a young age...' Jump right into your specific story."),
    ]),
  ],
  [  # Unit 2: Literature and Society
    s("Social Issues in Literature", [
      ("How does literature reflect and shape social attitudes?", "Literature as a mirror and agent of social change", "Literature reflects the values and tensions of its time by depicting social realities. It also shapes attitudes — Uncle Tom's Cabin fueled abolitionism, 1984 shaped views on surveillance and authoritarianism. Literature makes abstract issues personal and urgent."),
      ("What is the difference between a social novel and propaganda?", "Authentic complexity vs. oversimplified message", "A social novel explores social issues with nuance, complex characters, and moral ambiguity (e.g., The Grapes of Wrath). Propaganda oversimplifies, distorts, and manipulates to promote an ideology, reducing complexity to a single message."),
      ("How do authors use satire to critique society?", "Using humor and irony to expose absurdity or injustice", "Satire uses irony, exaggeration, and humor to expose and mock social problems, hypocrisy, or folly. Example: Animal Farm uses talking animals to satirize the Soviet Union and authoritarian power more broadly."),
      ("Choose a social issue depicted in a novel you have read. How does the author present it?", "Connect text to broader social context", "Example: In The Kite Runner (Hosseini), the author depicts ethnic and class discrimination in Afghanistan through personal relationships. By showing prejudice affecting a friendship between Amir and Hassan, Hosseini makes systemic injustice deeply personal."),
    ]),
    s("Comparative Literature", [
      ("What does it mean to compare two texts? What elements can be compared?", "Systematic analysis across multiple texts", "Comparing texts involves analyzing how two or more works handle the same element differently. Elements: theme, character, setting, tone, structure, point of view, style, and historical/cultural context."),
      ("What is an archetype? Give an example of a hero archetype across two different texts.", "Universal patterns of character or story", "An archetype is a recurring pattern in literature (character type, theme, or plot). The Hero archetype appears as Odysseus in The Odyssey and Harry Potter — both face trials, receive supernatural help, and transform through their journey."),
      ("How can the same theme be explored differently in texts from different cultures?", "Cultural context shapes thematic treatment", "Example: 'Coming of age' in The Catcher in the Rye (Holden's alienation in 1950s America) vs. Things Fall Apart (Okonkwo's struggle with colonial disruption in Nigeria). Same theme (identity under pressure) but shaped by vastly different cultural forces."),
      ("What is world literature and why is it valuable?", "Literature from non-English or non-Western traditions", "World literature includes works from all languages and cultures. Reading it broadens perspective, challenges cultural assumptions, reveals universal human experiences across cultures, and helps understand global history and diversity."),
    ]),
    s("Media Literacy and Modern Texts", [
      ("What is media literacy and why is it important today?", "Ability to critically analyze and evaluate media messages", "Media literacy is the ability to access, analyze, evaluate, and create media. In an age of 24/7 news, social media, and misinformation, it helps people distinguish fact from opinion, identify bias, evaluate sources, and understand how messages are constructed."),
      ("How is reading a film different from reading a written text?", "Visual storytelling uses different techniques", "Film uses cinematography (camera angle, lighting, movement), editing (pacing, transitions), sound/music, and performance alongside dialogue and narrative. Analyzing film means attending to visual and auditory choices as you would word choice and syntax in writing."),
      ("What is a news article's inverted pyramid structure?", "Most important information comes first", "The inverted pyramid structure puts the most important information (who, what, when, where, why, how) in the first paragraph (lede), followed by supporting details in order of decreasing importance. This lets readers stop at any point and still get the main story."),
      ("What techniques do advertisers use to persuade consumers?", "Emotional appeals, repetition, celebrity endorsement, scarcity", "Advertisers use: emotional appeals (fear, desire, belonging), celebrity endorsements (ethos/aspirational), bandwagon appeals (everyone's doing it), scarcity (limited time!), and repetition. Identifying these techniques helps evaluate media messages critically."),
    ]),
  ],
]
print("G11 ELA complete")

P[11]["history"] = [
  [  # Unit 0: US History - Founding to Civil War
    s("The American Revolution and Constitution", [
      ("What were the main causes of the American Revolution?", "Think: taxation, Enlightenment ideas, colonial identity", "Causes: taxation without representation (Stamp Act, Townshend Acts), Enlightenment ideas about natural rights (Locke), British restrictions on colonial trade and self-governance, and growing sense of American identity distinct from Britain."),
      ("What is the significance of the Declaration of Independence?", "July 4, 1776 — formal break from Britain and statement of principles", "The Declaration (written primarily by Jefferson) declared independence from Britain, articulated Enlightenment principles (all men created equal; unalienable rights of life, liberty, and pursuit of happiness), and justified revolution by listing grievances against King George III."),
      ("What were the key compromises in the Constitutional Convention (1787)?", "Debate over representation, slavery, and federal power", "Key compromises: (1) Great Compromise: bicameral Congress (House by population, Senate equal). (2) Three-Fifths Compromise: enslaved people counted as 3/5 for representation. (3) Commerce/slave trade compromise."),
      ("What is the Bill of Rights and why was it added to the Constitution?", "First 10 amendments protecting individual rights", "The Bill of Rights (1791) was added to protect individual liberties and limit federal power — demanded by Anti-Federalists who feared a strong central government. Key rights: freedom of speech, religion, press, assembly, and protection from unreasonable searches."),
    ]),
    s("Westward Expansion and Manifest Destiny", [
      ("What was Manifest Destiny and how did it shape US expansion?", "Belief that US was destined to expand to the Pacific", "Manifest Destiny was the 19th-century belief that American expansion westward to the Pacific was divinely ordained and inevitable. It justified territorial acquisition (Louisiana Purchase, Texas annexation, Mexican-American War) and displacement of Indigenous peoples."),
      ("What was the Trail of Tears?", "Forced removal of Cherokee Nation, 1838-1839", "The Trail of Tears was the forced relocation of the Cherokee Nation (and other tribes) from their ancestral homelands in the Southeast to Indian Territory (present-day Oklahoma). About 4,000 Cherokee died from disease, starvation, and exposure."),
      ("What were the causes and results of the Mexican-American War (1846-1848)?", "US expansion into Mexican territory", "Causes: US annexation of Texas, disputed border, and desire for California. Result: Treaty of Guadalupe Hidalgo — Mexico ceded California, New Mexico, and other territories (525,000 sq miles) to the US, which intensified debates about slavery in new territories."),
      ("How did the concept of popular sovereignty contribute to conflict over slavery?", "Letting territories decide whether to allow slavery", "Popular sovereignty (proposed in Compromise of 1850 and Kansas-Nebraska Act) allowed territorial settlers to vote on slavery. This led to violent conflict in 'Bleeding Kansas' as pro- and anti-slavery groups rushed in to influence the vote."),
    ]),
    s("The Civil War", [
      ("What were the main causes of the Civil War?", "Think: slavery, states' rights, economic differences, political failure", "Primary cause: slavery — its expansion into new territories and the Southern economy's dependence on it. Also: political failure (party breakdown), economic differences (industrial North vs. agrarian South), and states' rights disputes."),
      ("What was the significance of the Emancipation Proclamation (1863)?", "Lincoln's executive order freeing enslaved people in Confederate states", "It declared enslaved people in Confederate states to be free (didn't apply to border states). It transformed the war's purpose (now explicitly about ending slavery), prevented European nations from supporting the Confederacy, and allowed Black men to enlist in the Union Army."),
      ("What were the key military turning points of the Civil War?", "Antietam, Gettysburg, Vicksburg", "Battle of Antietam (1862): bloodiest day; allowed Emancipation Proclamation. Gettysburg (1863): major Confederate defeat ending Lee's northern invasion. Vicksburg (1863): Union controls Mississippi River, splitting Confederacy. Sherman's March (1864) devastated the South."),
      ("What was Reconstruction and what were its main goals?", "Post-Civil War period rebuilding the South and integrating freed people", "Reconstruction (1865-1877) aimed to: rebuild the South, reintegrate Confederate states, and establish rights for formerly enslaved people. The 13th (abolition), 14th (citizenship/equal protection), and 15th (Black male voting) Amendments were passed."),
    ]),
    s("Industrialization and the Gilded Age", [
      ("What factors drove rapid industrialization in America after the Civil War?", "Think: railroads, technology, labor, and capital", "Key factors: transcontinental railroad network, technological innovations, abundant natural resources, large labor supply (immigration and migration), and concentrated capital from financiers. These created a massive industrial economy by the early 1900s."),
      ("Who were the 'robber barons' and what was controversial about them?", "Industrial tycoons of the late 19th century", "Robber barons like John D. Rockefeller (oil), Andrew Carnegie (steel), and J.P. Morgan (finance) built massive corporate empires. They were criticized for monopolistic practices, exploiting workers, and using ruthless tactics. Some gave back through philanthropy."),
      ("What were the conditions of workers in Gilded Age factories?", "Think: low wages, long hours, dangerous conditions", "Factory workers (including children) worked 12-16 hour days for low wages in dangerous, unsanitary conditions. There were no labor protections, workers' compensation, or safety regulations. This fueled the labor movement and calls for reform."),
      ("What was the Progressive Movement and what reforms did it seek?", "Early 20th century reform movement addressing industrialization's ills", "Progressives sought: government regulation of big business (antitrust laws), labor protections (8-hour day, child labor laws), direct democracy (direct election of senators, initiative, referendum), women's suffrage, and social welfare programs."),
    ]),
  ],
  [  # Unit 1: US History - 20th Century
    s("World Wars and Their Impact", [
      ("Why did the US initially resist entering WWI and what changed?", "Neutrality policy and the Zimmermann Telegram", "The US initially maintained neutrality (Wilson's policy). US entry in 1917 was triggered by: unrestricted German submarine warfare (sinking American ships), the Zimmermann Telegram (Germany proposing Mexico attack the US), and desire to make the world 'safe for democracy.'"),
      ("What was the significance of the 1920s (The Roaring Twenties)?", "Economic boom, social change, and cultural flowering", "The 1920s saw: economic prosperity and consumerism, the rise of jazz and popular culture, women's suffrage (19th Amendment, 1920), Prohibition (and organized crime), increased urbanization, and the Harlem Renaissance — alongside rising nativism and the KKK."),
      ("What caused the Great Depression?", "Multiple economic failures converging", "Causes: stock market crash (October 1929), overproduction and falling prices, bank failures, tight monetary policy (Federal Reserve), high tariffs (Smoot-Hawley) hurting international trade, and underlying weaknesses in the economy (agricultural decline, income inequality)."),
      ("What was the New Deal and how did it respond to the Great Depression?", "FDR's program of relief, recovery, and reform", "FDR's New Deal (1933-1939) provided: Relief (direct aid to unemployed — CCC, FERA), Recovery (economic stimulation — NRA, AAA), and Reform (permanent structural changes — Social Security, FDIC, SEC). It didn't end the Depression but reshaped the role of federal government."),
    ]),
    s("Cold War America", [
      ("What was the Cold War and what ideological conflict drove it?", "US-Soviet geopolitical rivalry after WWII", "The Cold War was a political, military, and ideological rivalry between the US (capitalism/democracy) and Soviet Union (communism) from 1947-1991. Direct military conflict was largely avoided due to nuclear deterrence, but proxy wars and competition defined the era."),
      ("What was the Truman Doctrine and how did it shape US foreign policy?", "US commitment to contain communism", "The Truman Doctrine (1947) committed the US to supporting free peoples resisting Soviet pressure or communist takeover. It led to the containment policy: using economic aid (Marshall Plan), military alliances (NATO), and military force to prevent communist expansion."),
      ("What was McCarthyism and how did it affect American society?", "Anti-communist witch hunts in the early 1950s", "McCarthyism refers to Senator Joseph McCarthy's aggressive investigation of alleged communist infiltration of US government and society. It led to blacklisting, destroyed careers without evidence, and created a climate of fear that suppressed dissent and civil liberties."),
      ("What were the main events of the Civil Rights Movement (1954-1968)?", "Organized struggle against racial segregation and discrimination", "Key events: Brown v. Board of Education (1954, desegregating schools), Montgomery Bus Boycott (1955-56), sit-ins and Freedom Rides, March on Washington and 'I Have a Dream' (1963), Civil Rights Act (1964), Voting Rights Act (1965), assassination of MLK (1968)."),
    ]),
    s("Contemporary America", [
      ("What were the causes and effects of the Vietnam War?", "US involvement in Southeast Asian Cold War conflict", "The US entered Vietnam to prevent communist takeover (domino theory). Effects: 58,000 American and millions of Vietnamese deaths, massive domestic protest, loss of public trust in government, end of military draft, and the War Powers Act limiting presidential military power."),
      ("What was Watergate and why was it historically significant?", "Nixon's political scandal and resignation", "The Watergate scandal involved the break-in at Democratic headquarters (1972) and Nixon's cover-up. Nixon resigned in 1974 (the only presidential resignation in US history). It led to deep public distrust of government and lasting scrutiny of executive power."),
      ("How did the Reagan Revolution reshape American politics?", "Conservative shift in the 1980s", "Reagan (1981-1989) championed: supply-side ('trickle-down') economics (tax cuts, deregulation), reduced government spending on social programs, anti-Soviet foreign policy ('Evil Empire'), and cultural conservatism. This reshaped the Republican Party and set the agenda for decades."),
      ("What were the causes of the September 11, 2001 attacks and their aftermath?", "Al-Qaeda terrorist attack and the War on Terror", "Al-Qaeda terrorists (under Osama bin Laden) hijacked four planes, attacking the World Trade Center and Pentagon. Response: US invaded Afghanistan (2001), then Iraq (2003). Domestically: Patriot Act, Department of Homeland Security, debates over security vs. civil liberties."),
    ]),
  ],
  [  # Unit 2: Global History and Current Issues
    s("Globalization", [
      ("What is globalization and what are its main drivers?", "Increasing interconnection of economies, cultures, and politics", "Globalization is the growing interdependence of countries through trade, communication, and technology. Drivers: internet and communication technology, free trade agreements (NAFTA, WTO), multinational corporations, and international migration."),
      ("What are the arguments for and against globalization?", "Both benefits and costs are widely debated", "For: economic growth, lower consumer prices, technology sharing, cultural exchange, poverty reduction. Against: job losses in manufacturing countries, cultural homogenization, exploitation of workers in developing countries, and growing inequality."),
      ("What is the difference between a developed and developing country?", "Level of economic and human development", "Developed countries (US, Germany, Japan) have high incomes, strong infrastructure, advanced healthcare and education. Developing countries have lower incomes, less infrastructure, and higher poverty rates. The gap has complex historical causes including colonialism."),
      ("What role do multinational corporations play in the global economy?", "Companies operating in multiple countries", "Multinationals operate across borders, often producing where labor is cheapest and selling where purchasing power is highest. They create jobs and transfer technology but are criticized for tax avoidance, exploiting weak labor/environmental regulations, and exerting political influence."),
    ]),
    s("Human Rights and International Law", [
      ("What is the Universal Declaration of Human Rights?", "UN document establishing fundamental rights for all people", "The UDHR (1948) was adopted by the UN after WWII. It establishes 30 fundamental rights for all people regardless of nationality: right to life, freedom from torture, freedom of expression, right to education, and equal treatment under the law."),
      ("What is genocide and what international mechanisms exist to prevent it?", "Deliberate destruction of a group", "Genocide is the deliberate killing of a large group of people based on ethnicity, religion, or nationality. The UN Genocide Convention (1948) criminalizes it. The International Criminal Court (ICC) prosecutes individuals. Prevention efforts have had mixed success (Rwanda 1994, Darfur)."),
      ("What is the difference between a refugee and an immigrant?", "Forced displacement vs. voluntary migration", "A refugee flees their home country due to persecution, war, or natural disaster and cannot safely return. An immigrant voluntarily moves to another country. Refugees have specific legal protections under international law (1951 Refugee Convention)."),
      ("What are human rights abuses and what challenges exist in addressing them?", "Violations of fundamental rights and dignity", "Human rights abuses include: torture, political imprisonment, slavery, discrimination, and denial of basic freedoms. Challenges in addressing them: national sovereignty (countries resist outside interference), lack of enforcement, geopolitical interests, and inconsistent international will."),
    ]),
    s("Political Systems and Democracy", [
      ("What are the key features that distinguish a democracy from an authoritarian state?", "Rule of law, elections, rights vs. concentrated power", "Democracy: free and fair elections, rule of law (applies equally to all), protection of civil liberties, independent judiciary, and peaceful transfer of power. Authoritarianism: power concentrated in one person/party, limited civil rights, state control of media, suppression of opposition."),
      ("What is a constitutional government and why is a constitution important?", "Government bound by supreme law", "A constitutional government operates within limits set by a constitution, which establishes the structure of government, defines powers, and protects rights. It prevents arbitrary rule and ensures consistent governance regardless of who holds power."),
      ("What is civil society and what role does it play in a democracy?", "Non-governmental organizations and citizen associations", "Civil society includes nonprofit organizations, religious groups, professional associations, and social movements that exist outside government and market. In a democracy, civil society holds government accountable, advocates for rights, and enables civic participation."),
      ("What are the main threats to democracy in the 21st century?", "Think: misinformation, erosion of norms, inequality, authoritarianism", "Threats include: spread of misinformation and propaganda, polarization and erosion of democratic norms, rising inequality (can undermine faith in democratic institutions), authoritarian leaders undermining checks and balances, and foreign interference in elections."),
    ]),
  ],
]
print("G11 history complete")

P[11]["cs"] = [
  [  # Unit 0: Object-Oriented Programming
    s("Classes and Objects", [
      ("What is a class in OOP? What is an object?", "Blueprint vs. instance", "A class is a blueprint that defines attributes (data) and methods (functions) for a type of object. An object is a specific instance of a class. Example: 'Dog' is a class; 'my_dog = Dog()' creates an object."),
      ("Write a basic Python class for a Rectangle with length and width.", "Use __init__ method to set attributes", "class Rectangle:\n    def __init__(self, length, width):\n        self.length = length\n        self.width = width\n    def area(self):\n        return self.length * self.width"),
      ("What is the __init__ method in Python?", "The constructor — called when an object is created", "__init__ is the constructor method, automatically called when a new object is created. It initializes the object's attributes. 'self' refers to the object being created."),
      ("What is the difference between an instance variable and a class variable?", "Belongs to one object vs. shared by all objects", "Instance variable (self.x): unique to each object. Class variable (defined outside __init__): shared by all instances of the class."),
    ]),
    s("Inheritance and Polymorphism", [
      ("What is inheritance in OOP?", "A class inheriting attributes and methods from a parent class", "Inheritance allows a child class to inherit attributes and methods from a parent class. It promotes code reuse. Example: class Dog(Animal) — Dog inherits from Animal."),
      ("What is method overriding?", "Child class provides its own version of a parent method", "Method overriding: a child class defines a method with the same name as in the parent class, replacing the parent's behavior for that method in instances of the child class."),
      ("What is polymorphism? Give an example.", "Different objects respond to the same method in different ways", "Polymorphism allows different classes to be treated as instances of the same parent class through a common interface. Example: both Dog and Cat have a speak() method, but dog.speak() returns 'Woof' and cat.speak() returns 'Meow'."),
      ("What is encapsulation and why is it important?", "Hiding internal data and implementation details", "Encapsulation bundles data (attributes) and methods together inside a class, and restricts direct access to internal data. It protects data integrity and hides implementation complexity. Achieved with public, protected, and private access modifiers."),
    ]),
    s("File I/O and Error Handling", [
      ("How do you open and read a file in Python?", "Use open() with 'r' mode and read()", "with open('file.txt', 'r') as f:\n    content = f.read()\nThe 'with' statement automatically closes the file when done."),
      ("What is the difference between read(), readline(), and readlines()?", "Different ways to read from a file", "read(): reads entire file as a single string. readline(): reads one line at a time. readlines(): reads all lines into a list, one line per element."),
      ("What is a try-except block used for in Python?", "Handling exceptions (errors) gracefully", "try-except catches and handles errors without crashing the program. Code that might fail goes in try; the except block handles specific errors. Example: except FileNotFoundError: print('File not found')"),
      ("What is the finally block in exception handling?", "Code that always runs regardless of exception", "The finally block always executes whether or not an exception occurred — useful for cleanup (closing files, releasing resources). Example: finally: f.close()"),
    ]),
    s("Recursion", [
      ("What is recursion?", "A function that calls itself", "Recursion is when a function calls itself as part of its own definition. Every recursive function needs: a base case (stopping condition) and a recursive case (calls itself with a smaller input)."),
      ("Write a recursive function to calculate factorial of n.", "n! = n * (n-1)!", "def factorial(n):\n    if n == 0: return 1  # base case\n    return n * factorial(n-1)  # recursive case"),
      ("What is the base case in recursion and why is it essential?", "Prevents infinite recursion", "The base case is the condition where the function returns a result WITHOUT calling itself. Without it, the function recurses infinitely, causing a stack overflow error."),
      ("Trace the call stack for factorial(3).", "Walk through each function call", "factorial(3) → 3 * factorial(2) → 3 * 2 * factorial(1) → 3 * 2 * 1 * factorial(0) → 3 * 2 * 1 * 1 = 6."),
    ]),
  ],
  [  # Unit 1: Algorithms and Complexity
    s("Algorithm Design", [
      ("What is an algorithm? What properties should a good algorithm have?", "Step-by-step problem-solving procedure", "An algorithm is a finite set of well-defined instructions to solve a problem. Good properties: correct (solves the problem), efficient (uses minimal time/space), unambiguous (each step is clear), and general (works for all valid inputs)."),
      ("What is the difference between a greedy algorithm and dynamic programming?", "Local optimal choices vs. solving subproblems", "Greedy: makes the locally optimal choice at each step, hoping to find a global optimum (may not always work). Dynamic programming: breaks a problem into overlapping subproblems, solves each once, and stores results (memoization) for efficiency."),
      ("What is a brute force algorithm? When might it be acceptable?", "Try all possible solutions", "Brute force tries every possible solution until one works. It's simple but usually inefficient. Acceptable when: the input size is small, speed is not critical, or no better algorithm exists."),
      ("What is the divide and conquer strategy? Give an example.", "Break problem into smaller subproblems, solve, combine", "Divide and conquer: split the problem into smaller subproblems, solve each recursively, and combine results. Example: merge sort (divide array in half, sort each half, merge)."),
    ]),
    s("Time and Space Complexity", [
      ("What is Big-O notation?", "A way to describe algorithm efficiency in the worst case", "Big-O notation describes how the runtime (or space) of an algorithm grows as input size (n) grows. It gives the worst-case performance. Common: O(1) constant, O(log n) logarithmic, O(n) linear, O(n^2) quadratic."),
      ("What is the time complexity of linear search vs. binary search?", "O(n) vs. O(log n)", "Linear search: O(n) — in the worst case, checks every element. Binary search: O(log n) — halves the search space each step. Binary search is much faster for large sorted datasets."),
      ("What does O(n^2) mean in terms of performance?", "Quadratic growth — doubles input, quadruples time", "An O(n^2) algorithm's runtime grows proportionally to the square of the input size. If n doubles, the time roughly quadruples. Common in nested loops. Generally avoided for large inputs."),
      ("Rank these complexities from best to worst: O(n^2), O(n log n), O(1), O(n), O(log n).", "From most efficient to least", "Best to worst: O(1) < O(log n) < O(n) < O(n log n) < O(n^2)."),
    ]),
    s("Graph Algorithms", [
      ("What is a graph in computer science?", "Nodes connected by edges", "A graph is a data structure of nodes (vertices) connected by edges. Graphs can be directed (edges have direction) or undirected. Examples: social networks, maps, the internet."),
      ("What is the difference between breadth-first search (BFS) and depth-first search (DFS)?", "Level by level vs. go as deep as possible", "BFS explores all neighbors at the current level before moving deeper (uses a queue). DFS goes as far as possible along each branch before backtracking (uses a stack or recursion). BFS finds shortest path; DFS is useful for exploring all paths."),
      ("What is Dijkstra's algorithm used for?", "Finding shortest paths in a weighted graph", "Dijkstra's algorithm finds the shortest path from a source node to all other nodes in a weighted graph (with non-negative weights). It greedily selects the closest unvisited node at each step."),
      ("What is a tree data structure and how does it relate to graphs?", "A connected graph with no cycles", "A tree is a special type of graph that is connected and has no cycles. It has a root node, with parent-child relationships. Binary trees have at most 2 children per node. Trees are used in file systems, DOM, databases."),
    ]),
  ],
]
print("G11 CS complete")

P[11]["health"] = [
  [  # Unit 0: Advanced Mental and Emotional Health
    s("Understanding Stress and Trauma", [
      ("What is the difference between acute and chronic stress?", "Short-term vs. long-term stress", "Acute stress is short-term, triggered by a specific event (exam, conflict). Chronic stress is long-term, ongoing stress (poverty, unhealthy relationship). Chronic stress has more severe health consequences: immune suppression, cardiovascular disease, mental health disorders."),
      ("What is PTSD and what causes it?", "Post-Traumatic Stress Disorder", "PTSD is a mental health condition triggered by experiencing or witnessing a traumatic event. Symptoms include: flashbacks, nightmares, hypervigilance, avoidance, and emotional numbing. Causes: combat, abuse, accidents, natural disasters. Treated with therapy and sometimes medication."),
      ("What are protective factors for mental health resilience?", "Factors that help people cope with adversity", "Protective factors include: strong social support, access to mental health care, physical health, sense of purpose and meaning, problem-solving skills, healthy coping strategies, and stable housing and financial resources."),
      ("What is cognitive behavioral therapy (CBT) and how does it work?", "Evidence-based therapy changing thought patterns", "CBT is a therapy that identifies and changes negative or distorted thought patterns and behaviors. It teaches that thoughts influence feelings, which influence behavior. By challenging unhelpful thoughts, CBT helps improve emotional wellbeing and behavioral responses."),
    ]),
    s("Chronic Disease Prevention", [
      ("What are the main risk factors for cardiovascular disease?", "Think: lifestyle and genetic factors", "Risk factors: high blood pressure (hypertension), high cholesterol, smoking, diabetes, obesity, physical inactivity, unhealthy diet, excessive alcohol, stress, and family history. Most are modifiable through lifestyle changes."),
      ("What is Type 2 diabetes and what lifestyle factors increase its risk?", "A metabolic disease affecting blood sugar regulation", "Type 2 diabetes occurs when the body becomes resistant to insulin or doesn't produce enough. Risk factors: obesity (especially abdominal), physical inactivity, poor diet (high in refined carbs/sugar), age, and family history. It's largely preventable."),
      ("What is cancer and what lifestyle factors affect cancer risk?", "Uncontrolled cell growth", "Cancer is uncontrolled cell division that can invade other tissues. Lifestyle factors that increase risk: tobacco use, excessive alcohol, UV radiation exposure, obesity, physical inactivity, and processed meat consumption. Screening and early detection save lives."),
      ("What is the role of preventive healthcare?", "Preventing disease before it develops", "Preventive healthcare includes: vaccinations, regular screenings (blood pressure, cholesterol, cancer), dental checkups, healthy lifestyle choices, and managing risk factors. Prevention is more effective and less costly than treating advanced disease."),
    ]),
  ],
  [  # Unit 1: Community and Environmental Health
    s("Environmental Health", [
      ("What is an environmental health hazard? Give two examples.", "Conditions in the environment that can harm health", "An environmental health hazard is any physical, chemical, biological, or social factor in the environment that can harm health. Examples: (1) Air pollution (PM2.5 particles) causing respiratory disease. (2) Lead in water supply causing neurological damage."),
      ("What is the relationship between poverty and health outcomes?", "Socioeconomic status is a major determinant of health", "People in poverty have higher rates of chronic disease, mental illness, and shorter life expectancy. Contributing factors: food insecurity, lack of healthcare access, exposure to environmental hazards, higher stress, and fewer safe recreational opportunities."),
      ("What are social determinants of health?", "Non-medical factors influencing health outcomes", "Social determinants include: education, income, housing, employment, access to healthy food, neighborhood safety, and social support. They account for 30-55% of health outcomes, often more impactful than medical care itself."),
      ("What is community health and how do communities promote it?", "Collective wellbeing of a defined population", "Community health addresses the health needs of defined populations. Communities promote health through: public health programs, access to parks and recreation, safe built environments, mental health services, and addressing social determinants."),
    ]),
    s("First Aid and Emergency Response", [
      ("What are the steps in basic CPR?", "Cardiopulmonary Resuscitation for cardiac arrest", "1. Check scene safety. 2. Check for responsiveness. 3. Call 911. 4. Begin chest compressions (30 compressions, 2 inches deep, 100-120/min). 5. Give 2 rescue breaths. 6. Repeat until help arrives or AED available."),
      ("What is the Heimlich maneuver used for?", "Dislodging a foreign object from the airway", "The Heimlich maneuver (abdominal thrusts) is used when someone is choking. Stand behind the person, place a fist above the navel, grasp with other hand, and give quick upward thrusts until the object is expelled."),
      ("What are the signs of a stroke and what is the FAST acronym?", "Time-critical medical emergency", "FAST: (F)ace drooping, (A)rm weakness, (S)peech difficulty, (T)ime to call 911. Stroke is a brain attack — every minute matters. Quick response can limit brain damage significantly."),
      ("What is the difference between a first-degree, second-degree, and third-degree burn?", "Burn severity classification", "1st degree: only outer skin (redness, pain) — minor. 2nd degree: dermis involved (blisters, intense pain) — serious. 3rd degree: full thickness, nerve damage (no pain, charred/white skin) — requires immediate emergency care."),
    ]),
  ],
]
print("G11 health complete")

# ─── GRADE 12 ───
P[12] = {"math":[], "science":[], "ela":[], "history":[], "cs":[], "health":[]}

P[12]["math"] = [
  [  # Unit 0: AP Calculus - Limits and Derivatives
    s("Limits", [
      ("Evaluate lim(x→3) of (x^2 - 9)/(x - 3).", "Factor the numerator", "(x-3)(x+3)/(x-3) = x+3. As x→3, limit = 6."),
      ("What is L'Hopital's Rule and when do you use it?", "For 0/0 or inf/inf indeterminate forms", "L'Hopital's Rule: if lim f(x)/g(x) gives 0/0 or ∞/∞, then lim f(x)/g(x) = lim f'(x)/g'(x). Differentiate numerator and denominator separately, then take the limit."),
      ("What does it mean for a function to be continuous at x=c?", "Three conditions must all hold", "f is continuous at c if: (1) f(c) is defined, (2) lim(x→c) f(x) exists, (3) lim(x→c) f(x) = f(c). All three must hold."),
      ("Evaluate lim(x→∞) of (5x^3 - 2x)/(2x^3 + 1).", "Divide by the highest power", "Divide numerator and denominator by x^3: (5 - 2/x^2)/(2 + 1/x^3) → 5/2 as x→∞."),
    ]),
    s("Differentiation Rules", [
      ("State the chain rule. Apply it to f(x) = (3x+1)^5.", "Derivative of outer times derivative of inner", "Chain rule: d/dx [f(g(x))] = f'(g(x)) * g'(x). For (3x+1)^5: 5(3x+1)^4 * 3 = 15(3x+1)^4."),
      ("Differentiate f(x) = x^2 * sin(x).", "Use the product rule: (uv)' = u'v + uv'", "u = x^2, u' = 2x. v = sin(x), v' = cos(x). f'(x) = 2x*sin(x) + x^2*cos(x)."),
      ("Differentiate f(x) = sin(x)/x^2.", "Use the quotient rule: (u/v)' = (u'v - uv')/v^2", "u = sin(x), u' = cos(x). v = x^2, v' = 2x. f'(x) = (cos(x)*x^2 - sin(x)*2x)/x^4 = (x*cos(x) - 2sin(x))/x^3."),
      ("Differentiate f(x) = e^(3x) and f(x) = ln(x^2).", "Derivatives of e^x and ln(x)", "d/dx [e^(3x)] = 3e^(3x). d/dx [ln(x^2)] = d/dx [2ln(x)] = 2/x."),
    ]),
    s("Applications of Derivatives", [
      ("Find the absolute maximum and minimum of f(x) = x^3 - 3x on [-2, 2].", "Evaluate at critical points and endpoints", "f'(x) = 3x^2-3 = 0 → x = ±1. f(-2)=-2, f(-1)=2, f(1)=-2, f(2)=2. Absolute max = 2 at x=-1 and x=2. Absolute min = -2 at x=1 and x=-2."),
      ("What is the Mean Value Theorem?", "There exists a point where instantaneous rate = average rate", "MVT: If f is continuous on [a,b] and differentiable on (a,b), there exists c in (a,b) where f'(c) = (f(b)-f(a))/(b-a). The tangent slope equals the secant slope at some point."),
      ("A 10 ft ladder leans against a wall. The bottom slides away at 2 ft/sec. How fast is the top sliding down when the bottom is 6 ft from the wall?", "Related rates problem using Pythagorean theorem", "x^2+y^2=100. Differentiate: 2x(dx/dt)+2y(dy/dt)=0. When x=6: y=8. 2(6)(2)+2(8)(dy/dt)=0 → dy/dt = -3/2 ft/sec (sliding down at 1.5 ft/sec)."),
      ("What does the second derivative test tell us?", "Classifying critical points as max or min", "At critical point c: if f''(c) > 0, it's a local minimum (concave up). If f''(c) < 0, it's a local maximum (concave down). If f''(c) = 0, test is inconclusive."),
    ]),
    s("Integration", [
      ("Evaluate the integral of sin(x) dx.", "Antiderivative of sin(x)", "Integral of sin(x) dx = -cos(x) + C."),
      ("Use u-substitution to evaluate the integral of x*e^(x^2) dx.", "Let u = x^2, du = 2x dx", "Let u = x^2, du = 2x dx → x dx = du/2. Integral becomes (1/2) integral of e^u du = (1/2)e^u + C = (1/2)e^(x^2) + C."),
      ("Evaluate the definite integral from 0 to pi of sin(x) dx.", "Apply FTC: F(pi) - F(0)", "F(x) = -cos(x). F(pi)-F(0) = -cos(pi)-(-cos(0)) = -(-1)-(-1) = 1+1 = 2."),
      ("Find the area between y = x^2 and y = x from x=0 to x=1.", "Area = integral of (top - bottom) dx", "Top: y=x, Bottom: y=x^2 on [0,1]. Area = integral from 0 to 1 of (x-x^2)dx = [x^2/2 - x^3/3] from 0 to 1 = 1/2 - 1/3 = 1/6."),
    ]),
  ],
  [  # Unit 1: Advanced Statistics
    s("Experimental Design", [
      ("What is the difference between an observational study and an experiment?", "No intervention vs. deliberate manipulation", "Observational study: researcher observes without intervening (can show correlation). Experiment: researcher deliberately applies a treatment to measure its effect (can show causation)."),
      ("What is a control group and a treatment group?", "Comparison groups in an experiment", "Control group: receives no treatment (or a placebo) — serves as the baseline. Treatment group: receives the experimental treatment. Comparing outcomes between groups isolates the effect of the treatment."),
      ("What is random assignment and why is it important?", "Randomly placing participants into groups", "Random assignment ensures that the control and treatment groups are similar in all respects (except the treatment), eliminating confounding variables. It allows researchers to attribute differences in outcomes to the treatment itself."),
      ("What is a double-blind experiment?", "Neither participants nor researchers know who gets what", "Double-blind: both participants and researchers are unaware of who is in the control vs. treatment group. This eliminates placebo effect and researcher bias, making results more reliable."),
    ]),
    s("Inference for Proportions and Means", [
      ("What is a hypothesis test and what are the two hypotheses?", "Test to determine if sample results are statistically significant", "Hypothesis test evaluates whether an observed result is due to chance. Null hypothesis (H0): no effect/no difference (the 'default'). Alternative hypothesis (Ha): there is an effect/difference."),
      ("What does 'statistically significant' mean?", "Results unlikely to be due to chance", "Statistically significant means the probability of getting results as extreme as observed, given H0 is true, is below the significance level (alpha, usually 0.05). We reject H0 when p-value < alpha."),
      ("What is a Type I error vs. a Type II error?", "False positive vs. false negative", "Type I error: rejecting H0 when it's actually true (false positive). Type II error: failing to reject H0 when it's actually false (false negative). Reducing Type I error risk increases Type II error risk."),
      ("A poll of 400 people shows 60% support a policy. Construct a 95% confidence interval.", "Use p ± z*sqrt(p(1-p)/n) with z=1.96 for 95%", "p=0.60, n=400, SE=sqrt(0.6*0.4/400)=sqrt(0.0006)=0.0245. CI: 0.60 ± 1.96*0.0245 = 0.60 ± 0.048. Interval: (0.552, 0.648)."),
    ]),
    s("Regression Analysis", [
      ("Interpret the slope of a regression line y = 2.5x + 10 where x = hours studied and y = test score.", "Slope tells you the change in y per unit change in x", "The slope 2.5 means for each additional hour studied, the predicted test score increases by 2.5 points."),
      ("What is r^2 (coefficient of determination) and what does it tell you?", "Proportion of variation in y explained by x", "r^2 = the proportion of the variation in y that is explained by the linear relationship with x. Example: r^2 = 0.80 means 80% of the variation in test scores is explained by hours studied."),
      ("What is extrapolation and why is it risky?", "Predicting y outside the range of x values used to build the model", "Extrapolation is using a regression model to predict y for x values outside the range of the data. It's risky because the linear relationship may not hold outside the observed data range."),
      ("A residual plot shows a curved pattern. What does this indicate?", "Curved residual plot = linear model is not appropriate", "A curved (non-random) pattern in a residual plot indicates that a linear model is NOT appropriate for the data — a curve or other model would fit better."),
    ]),
    s("Chi-Square Tests", [
      ("What does a chi-square test for goodness of fit test?", "Whether observed frequencies match expected frequencies", "A chi-square goodness of fit test evaluates whether observed data matches a hypothesized distribution. Example: testing whether a die is fair (each face should appear ~1/6 of the time)."),
      ("What is a chi-square test for independence?", "Tests whether two categorical variables are related", "A chi-square test of independence tests whether two categorical variables are associated (not independent). Example: Is there a relationship between gender and preferred news source?"),
      ("How do you calculate the chi-square test statistic?", "Sum of (observed - expected)^2 / expected", "Chi-square statistic = sum of [(O-E)^2/E] for all cells, where O = observed count and E = expected count."),
      ("What do degrees of freedom mean in a chi-square test?", "Determined by the number of categories", "For goodness of fit: df = number of categories - 1. For independence test: df = (rows - 1) * (columns - 1). Degrees of freedom determine the chi-square distribution used."),
    ]),
  ],
  [  # Unit 2: Discrete Mathematics
    s("Logic and Proof", [
      ("What is a conditional statement? Write it in if-then form.", "p → q: if p then q", "A conditional statement has the form 'If p, then q' (p → q). p is the hypothesis; q is the conclusion. Example: 'If it rains, then the ground is wet.'"),
      ("What is the contrapositive of 'If it rains, then the ground is wet'?", "Negate and swap hypothesis and conclusion", "Contrapositive: 'If the ground is NOT wet, then it did NOT rain.' A conditional and its contrapositive are logically equivalent."),
      ("What is a proof by contradiction?", "Assume the opposite is true, derive a contradiction", "Proof by contradiction: assume the statement is FALSE, then show this leads to a logical contradiction. This proves the original statement must be TRUE. Example: proof that sqrt(2) is irrational."),
      ("What is an indirect proof (proof by contrapositive)?", "Prove contrapositive instead of original statement", "Since p→q is equivalent to (not q)→(not p), you can prove the contrapositive instead. If it's easier to prove the contrapositive, do so to establish the original conditional."),
    ]),
    s("Combinatorics", [
      ("How many ways can 8 books be arranged on a shelf?", "Permutation of all 8 items", "8! = 40,320 ways."),
      ("A pizza restaurant offers 10 toppings. How many 3-topping pizzas are possible?", "Combination since order doesn't matter", "C(10,3) = 10!/(3!7!) = 120 pizzas."),
      ("What is Pascal's Triangle and how does it relate to combinations?", "Triangular array where each row gives binomial coefficients", "In Pascal's Triangle, each entry is the sum of the two above it. The nth row gives the binomial coefficients C(n,0), C(n,1), ... C(n,n). Row 4: 1, 4, 6, 4, 1 = C(4,0) through C(4,4)."),
      ("What is the Binomial Theorem? Use it to expand (x+y)^3.", "Expand a binomial raised to a power", "Binomial Theorem: (x+y)^n = sum of C(n,k)*x^(n-k)*y^k for k=0 to n. (x+y)^3 = C(3,0)x^3 + C(3,1)x^2y + C(3,2)xy^2 + C(3,3)y^3 = x^3 + 3x^2y + 3xy^2 + y^3."),
    ]),
    s("Number Theory", [
      ("What is a prime number? List the primes up to 30.", "A number divisible only by 1 and itself", "A prime has exactly two factors: 1 and itself. Primes up to 30: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29."),
      ("What is the Fundamental Theorem of Arithmetic?", "Every integer has a unique prime factorization", "Every integer greater than 1 can be expressed as a unique product of prime numbers (up to the order of factors). Example: 60 = 2^2 * 3 * 5."),
      ("What is modular arithmetic? Evaluate 17 mod 5.", "Remainder after division", "Modular arithmetic works with remainders. 17 mod 5 = 2 (because 17 = 3*5 + 2, remainder is 2). Used in cryptography, computer science, and calendars."),
      ("What is the Euclidean Algorithm used for?", "Finding the greatest common divisor (GCD)", "The Euclidean Algorithm finds the GCD of two integers by repeatedly dividing and taking remainders. Example: GCD(48,18): 48=2*18+12; 18=1*12+6; 12=2*6+0. GCD = 6."),
    ]),
    s("Graph Theory", [
      ("What is a graph? Define vertex, edge, and degree.", "Mathematical structure with nodes and connections", "A graph G = (V,E) consists of vertices (nodes) V and edges E (connections). The degree of a vertex is the number of edges connected to it."),
      ("What is the difference between a directed and undirected graph?", "Arrows vs. no arrows on edges", "Undirected graph: edges have no direction (friendship network). Directed graph (digraph): edges have direction, shown with arrows (web links, Twitter follows)."),
      ("What is the Handshaking Lemma?", "Sum of all degrees = twice the number of edges", "In any undirected graph, the sum of all vertex degrees equals twice the number of edges. This means the sum of degrees is always even."),
      ("What is the Four Color Theorem?", "Any map can be colored with at most 4 colors", "The Four Color Theorem states that any map (or planar graph) can be colored using at most 4 colors such that no two adjacent regions share the same color. First proven in 1976 using computers."),
    ]),
  ],
  [  # Unit 3: Senior Capstone / Financial Literacy
    s("College and Career Planning", [
      ("What is the difference between a college's sticker price and the net price?", "Published cost vs. actual cost after aid", "Sticker price: the full published tuition/fees/room and board. Net price: what you actually pay after grants and scholarships (not loans). Net price = sticker price - free aid."),
      ("What is the FAFSA and why is it important?", "Free Application for Federal Student Aid", "The FAFSA determines eligibility for federal grants, loans, and work-study. Nearly all colleges use it to award institutional aid as well. Filing early is important — some aid is first-come, first-served."),
      ("What is the difference between a subsidized and unsubsidized student loan?", "Government pays interest vs. you pay all interest", "Subsidized: federal government pays the interest while you're in school (for students with financial need). Unsubsidized: interest accrues from the day the loan is disbursed, whether you're in school or not."),
      ("What is a career pathway and how does it differ from a college pathway?", "Different routes to career goals", "College pathway: 2-4 year degree at a college/university. Career/vocational pathway: trade school, apprenticeship, certification programs leading directly to skilled trades (electrician, plumber, welder, medical technician). Both are valid routes to fulfilling careers."),
    ]),
    s("Personal Finance Mastery", [
      ("What is a credit score and what factors affect it?", "Numerical rating of creditworthiness", "Credit score (300-850) measures creditworthiness. Factors: payment history (35%), amounts owed (30%), length of credit history (15%), new credit (10%), credit mix (10%). Higher score = better loan rates."),
      ("What is the difference between a Roth IRA and a Traditional IRA?", "After-tax vs. pre-tax retirement accounts", "Traditional IRA: contributions may be tax-deductible; withdrawals in retirement are taxed. Roth IRA: contributions are made with after-tax money; qualified withdrawals in retirement are tax-FREE. Roth is generally better for young people in lower tax brackets."),
      ("What is compound interest and how does it work over time?", "Interest earning interest", "Compound interest earns interest on both the original principal AND the accumulated interest. Over long periods, this creates exponential growth. Starting at age 18 vs. 30 makes a dramatic difference due to more years of compounding."),
      ("Create a simple 3-category budget for a recent graduate earning $40,000/year ($3,333/month).", "Apply the 50/30/20 rule", "Needs (50%) = $1,667/month (rent, food, utilities, transportation). Wants (30%) = $1,000/month (entertainment, dining, hobbies). Savings/debt repayment (20%) = $667/month (emergency fund, student loans, retirement)."),
    ]),
    s("Civic Life and Democracy", [
      ("What are the three branches of the US federal government and their main functions?", "Separation of powers", "Legislative (Congress): makes laws. Executive (President): enforces laws. Judicial (courts/Supreme Court): interprets laws. Each has checks and balances on the others to prevent any one branch from becoming too powerful."),
      ("What is the process for a bill to become a law?", "From introduction to presidential signature", "A bill is introduced in Congress, reviewed in committee, debated and voted on by the full House and Senate (both must pass identical versions), then sent to the President. President can sign (becomes law), veto (Congress can override with 2/3 vote), or do nothing."),
      ("What are civil rights vs. civil liberties?", "Legal equality rights vs. freedoms from government", "Civil liberties: freedoms guaranteed to individuals limiting government action (free speech, religion, from unreasonable search — First, Fourth Amendments). Civil rights: freedom from discrimination; right to equal treatment under law (14th Amendment, Civil Rights Act)."),
      ("Why is voting important and what has historically limited access to it?", "Cornerstone of democratic participation", "Voting allows citizens to choose representatives and influence policy. Historical barriers to voting access: poll taxes, literacy tests, grandfather clauses (targeting Black Americans), property requirements, gender (women gained suffrage in 1920). The Voting Rights Act (1965) addressed many of these."),
    ]),
    s("Life Skills and Decision Making", [
      ("What is critical thinking and how can you apply it to decision making?", "Systematic, objective analysis and evaluation of information", "Critical thinking involves: identifying the question/problem, gathering relevant information, evaluating sources and evidence, considering multiple perspectives, identifying assumptions and biases, and making a reasoned conclusion. Apply it by slowing down before deciding."),
      ("What is an ethical dilemma and how do you navigate one?", "A situation where values or principles conflict", "An ethical dilemma presents two or more choices that conflict with different values. Navigate by: identifying stakeholders and their interests, considering consequences of each choice, applying ethical frameworks (fairness, harm reduction, duty), and making the most defensible choice."),
      ("What is time management and what strategies improve it?", "Using time effectively to achieve goals", "Good time management strategies: setting priorities (important vs. urgent), breaking goals into tasks, using a planner or calendar, setting deadlines, avoiding multitasking, taking breaks (Pomodoro technique), and eliminating distractions."),
      ("What is goal setting and what makes a goal effective (SMART goals)?", "Purposeful process of identifying objectives", "SMART goals are: (S)pecific — clearly defined. (M)easurable — you can track progress. (A)chievable — realistic. (R)elevant — connected to your values. (T)ime-bound — has a deadline. SMART goals are far more likely to be accomplished than vague goals."),
    ]),
  ],
]
print("G12 math complete")

P[12]["science"] = [
  [  # Unit 0: Physics - Mechanics
    s("Kinematics", [
      ("A car accelerates from rest at 3 m/s^2 for 5 seconds. Find its final velocity and distance traveled.", "Use kinematic equations: v=u+at and d=ut+0.5at^2", "v = 0 + 3*5 = 15 m/s. d = 0*5 + 0.5*3*25 = 37.5 m."),
      ("What is the difference between displacement and distance?", "Vector vs. scalar quantity", "Distance is the total path length traveled (scalar). Displacement is the change in position from start to end (vector — has direction). You can travel 10 m and have zero displacement (if you return to start)."),
      ("A ball is thrown horizontally at 20 m/s from a 45 m cliff. How long does it take to hit the ground?", "Vertical motion: d = 0.5*g*t^2 (g=10m/s^2)", "45 = 0.5*10*t^2 → t^2 = 9 → t = 3 seconds."),
      ("What is the equation for centripetal acceleration?", "Acceleration toward center for circular motion", "a_c = v^2/r where v is the speed and r is the radius of the circular path. Direction is always toward the center of the circle."),
    ]),
    s("Dynamics and Newton's Laws", [
      ("A 10 kg box is pushed with 50 N force on a surface with friction force 20 N. Find acceleration.", "Net force = F_applied - F_friction; then F=ma", "Net F = 50-20 = 30 N. a = F/m = 30/10 = 3 m/s^2."),
      ("What is the gravitational force between two objects?", "Newton's law of universal gravitation", "F = G*m1*m2/r^2, where G = 6.67x10^-11 N·m^2/kg^2, m1 and m2 are masses, r is the distance between them. Force decreases with the square of distance."),
      ("Explain why astronauts in the ISS appear weightless.", "They are in free fall — orbiting the Earth", "The ISS and astronauts are in continuous free fall toward Earth. Because they and the station fall together at the same rate, there is no normal force — creating the sensation of weightlessness (microgravity)."),
      ("State the law of conservation of energy.", "Total energy in a closed system is constant", "Energy cannot be created or destroyed, only converted from one form to another. In a closed system, the total mechanical energy (KE + PE) remains constant (ignoring friction)."),
    ]),
    s("Waves and Sound", [
      ("What is a wave? What is the difference between transverse and longitudinal waves?", "A disturbance that transfers energy", "A wave transfers energy through a medium without transferring matter. Transverse: particles oscillate perpendicular to wave travel (light, water waves). Longitudinal: particles oscillate parallel to wave travel (sound, seismic P-waves)."),
      ("What is the relationship between frequency, wavelength, and wave speed?", "v = f * lambda", "Wave speed = frequency * wavelength. v = f*lambda. If frequency increases and speed stays constant, wavelength decreases (and vice versa)."),
      ("What is the Doppler Effect?", "Apparent change in frequency due to relative motion", "The Doppler Effect is the change in perceived frequency when the source and observer are in relative motion. As the source approaches, frequency appears higher (higher pitch). As it moves away, frequency appears lower. Examples: ambulance siren, radar."),
      ("What is resonance?", "A system vibrating at its natural frequency", "Resonance occurs when a driving frequency matches an object's natural frequency, causing large amplitude vibrations. Examples: a singer breaking a glass, a bridge oscillating in wind (Tacoma Narrows), tuning a radio."),
    ]),
    s("Electricity and Magnetism", [
      ("What is Ohm's Law?", "Relationship between voltage, current, and resistance", "Ohm's Law: V = I*R. Voltage (V) = Current (I) * Resistance (R). Higher resistance means less current for the same voltage."),
      ("What is the difference between series and parallel circuits?", "Components in line vs. side by side", "Series: components in a single loop — same current flows through all; if one fails, all fail. Parallel: components in separate branches — same voltage across all; one failing doesn't affect others. Home wiring uses parallel circuits."),
      ("What is electromagnetic induction?", "Using a changing magnetic field to generate electricity", "Electromagnetic induction: a changing magnetic field induces an electric current in a conductor. This is the basis of generators, transformers, and electric motors. Discovered by Faraday."),
      ("How does a transformer work and what is it used for?", "Changes voltage using electromagnetic induction", "A transformer uses electromagnetic induction between two coils of wire. Step-up transformer: increases voltage (fewer primary turns → more secondary turns). Step-down: decreases voltage. Used to transmit electricity efficiently over long distances."),
    ]),
  ],
  [  # Unit 1: Environmental Science
    s("Earth Systems", [
      ("What are the four main Earth systems and how do they interact?", "Geosphere, hydrosphere, atmosphere, biosphere", "1. Geosphere (land/rock). 2. Hydrosphere (water). 3. Atmosphere (air). 4. Biosphere (living things). They interact constantly — e.g., water evaporates from hydrosphere into atmosphere, falls as rain, feeds biosphere, shapes geosphere through erosion."),
      ("What is the carbon cycle and why is it important?", "Movement of carbon through Earth's systems", "The carbon cycle tracks carbon as it moves through atmosphere (CO2), biosphere (photosynthesis/respiration), oceans, and geosphere (fossil fuels, rock). It regulates climate and supports life. Human activities are disrupting the natural balance."),
      ("What is the nitrogen cycle and why do organisms need nitrogen?", "Movement of nitrogen between air, soil, and organisms", "Nitrogen is essential for proteins and DNA. The cycle: nitrogen fixation (bacteria convert N2 to usable forms) → nitrification → plant uptake → animal consumption → decomposition → denitrification (returns N2 to air)."),
      ("What is the difference between weather and climate?", "Short-term vs. long-term atmospheric conditions", "Weather is the short-term atmospheric conditions at a specific place and time (today's temperature, rain). Climate is the average weather patterns over 30+ years for a region. 'Climate is what you expect; weather is what you get.'"),
    ]),
    s("Climate Change", [
      ("What is the greenhouse effect and how does human activity enhance it?", "Natural warming process intensified by human emissions", "The natural greenhouse effect traps enough heat to support life. Human activities (burning fossil fuels, deforestation) add CO2, methane, and N2O, trapping more heat. This enhanced greenhouse effect causes global temperatures to rise (global warming)."),
      ("What is the scientific consensus on human-caused climate change?", "97%+ of climate scientists agree it is real and human-caused", "The overwhelming scientific consensus (97%+ of climate scientists, supported by NASA, NOAA, IPCC) is that climate change is real, primarily caused by human activities (fossil fuel combustion), and poses serious risks to ecosystems and human civilization."),
      ("What are potential consequences of unchecked climate change?", "Think: sea level rise, extreme weather, ecosystem disruption", "Consequences include: rising sea levels (coastal flooding), more frequent/intense extreme weather events (hurricanes, droughts, wildfires), ocean acidification, ecosystem disruption and species extinction, threats to food and water security, and climate refugees."),
      ("What are mitigation vs. adaptation strategies for climate change?", "Reducing vs. adjusting to climate change", "Mitigation: reducing greenhouse gas emissions (renewable energy, efficiency, less deforestation). Adaptation: adjusting to current/future climate effects (sea walls, drought-resistant crops, early warning systems). Both are needed."),
    ]),
    s("Biodiversity and Conservation", [
      ("Why is biodiversity important?", "Benefits to ecosystems and human welfare", "Biodiversity supports: ecosystem stability (more resilient to disturbance), food security (genetic diversity in crops), medicines (many drugs come from plants/animals), ecosystem services (pollination, water purification), and intrinsic value of species."),
      ("What are the main causes of species extinction today?", "Think: HIPPO", "HIPPO: Habitat loss/destruction (biggest cause), Invasive species, Pollution, Population growth (human), Overexploitation (overhunting, overfishing). Climate change is increasingly a major driver as well."),
      ("What is a keystone species and why does its removal matter?", "A species with disproportionate impact on ecosystem structure", "A keystone species has an outsized role in maintaining ecosystem balance. Its removal causes dramatic changes. Example: sea otters control sea urchin populations; without them, urchins explode and destroy kelp forests, eliminating habitat for many species."),
      ("What is sustainable development?", "Meeting present needs without compromising future needs", "Sustainable development (Brundtland definition, 1987) meets the needs of the present without compromising future generations' ability to meet their own needs. It balances economic, social, and environmental goals."),
    ]),
    s("Energy Resources", [
      ("Compare renewable and nonrenewable energy sources.", "Can be replenished vs. finite supply", "Renewable: solar, wind, hydropower, geothermal, biomass — replenished naturally. Nonrenewable: coal, oil, natural gas, nuclear (uranium) — finite supply or very slow to form. Renewables produce less or no greenhouse gases."),
      ("How does a nuclear power plant generate electricity?", "Fission of uranium produces heat", "Nuclear plants use controlled nuclear fission (splitting uranium atoms) to produce heat. The heat boils water into steam, which drives turbines connected to generators, producing electricity. No CO2 emissions, but nuclear waste is radioactive."),
      ("What are the advantages and disadvantages of solar energy?", "Clean, renewable, but intermittent", "Advantages: no greenhouse emissions, no fuel costs, low maintenance, abundant resource. Disadvantages: intermittent (no sun at night or in clouds), land area requirements, manufacturing impacts, energy storage challenges."),
      ("What is the energy return on investment (EROI) and why does it matter?", "Energy gained vs. energy invested to get it", "EROI = energy output / energy input needed to obtain it. High EROI (oil historically ~25:1) means abundant net energy. Renewables have improving EROI. As fossil fuel EROI declines, understanding energy economics becomes critical for planning."),
    ]),
  ],
  [  # Unit 2: Anatomy and Human Health
    s("Body Systems Overview", [
      ("List the major organ systems and their primary functions.", "Human body has 11 major systems", "Integumentary (skin — protection), Skeletal (support), Muscular (movement), Nervous (control), Endocrine (hormones), Cardiovascular (transport), Lymphatic/Immune (defense), Respiratory (gas exchange), Digestive (nutrition), Urinary (waste), Reproductive."),
      ("How do the respiratory and circulatory systems work together?", "Gas exchange and transport", "Respiratory system: brings O2 into lungs, expels CO2. Circulatory system: carries O2-rich blood from lungs to cells via arteries, and returns CO2-rich blood to the lungs via veins. They work continuously together to supply cells with oxygen."),
      ("What is homeostasis and how does the body maintain it?", "Maintaining stable internal conditions", "Homeostasis is the body's maintenance of stable internal conditions (temperature ~37°C, blood pH ~7.4, blood glucose). Maintained through negative feedback loops: a change triggers a response that reverses the change. Example: body temperature regulation."),
      ("What is a negative feedback loop? Give an example from human physiology.", "Response that reverses a change — maintains balance", "Negative feedback: when a variable changes, a response reverses it. Example: blood glucose rises after eating → pancreas releases insulin → cells absorb glucose → blood glucose returns to normal. This keeps blood glucose within a narrow range."),
    ]),
    s("The Immune System", [
      ("What is the difference between innate and adaptive immunity?", "Non-specific vs. targeted response", "Innate immunity: fast, non-specific first defense (skin, fever, inflammation, natural killer cells). Adaptive immunity: slower but targeted — B and T lymphocytes recognize specific pathogens, create memory for faster future responses."),
      ("How do vaccines work?", "Training the immune system without causing disease", "Vaccines introduce a harmless form of a pathogen (killed/weakened pathogen, protein subunit, or mRNA). The immune system mounts a response and creates memory cells. Future exposure triggers a faster, stronger response that prevents or reduces disease."),
      ("What is the difference between an antigen and an antibody?", "Trigger vs. response", "Antigen: a molecule (usually on a pathogen) that triggers an immune response. Antibody: a protein produced by B cells that specifically binds to an antigen, marking it for destruction."),
      ("What is an autoimmune disease? Give an example.", "Immune system attacks the body's own tissues", "Autoimmune disease: the immune system mistakenly attacks healthy body cells/tissues. Examples: Type 1 diabetes (attacks insulin-producing cells), rheumatoid arthritis (attacks joints), multiple sclerosis (attacks myelin sheath of nerves)."),
    ]),
    s("Neuroscience and Behavior", [
      ("What are the main parts of a neuron and their functions?", "The nerve cell's structure", "Dendrites: receive signals. Cell body (soma): contains nucleus and processes signals. Axon: transmits electrical signal. Myelin sheath: insulates axon for faster transmission. Axon terminals: release neurotransmitters to next cell."),
      ("What is a synapse and how does synaptic transmission work?", "Gap between neurons where signals are transmitted", "A synapse is the tiny gap between neurons. The presynaptic neuron releases neurotransmitters into the synapse. Neurotransmitters bind to receptors on the postsynaptic neuron, either exciting or inhibiting the next neuron."),
      ("What is neuroplasticity?", "The brain's ability to change and reorganize", "Neuroplasticity is the brain's ability to form new neural connections and reorganize existing ones in response to learning, experience, or injury. It allows recovery from brain damage and underlies learning, memory, and skill development."),
      ("How does sleep affect brain function and learning?", "Sleep is critical for memory consolidation and brain health", "During sleep (especially deep sleep and REM), the brain consolidates memories, clears waste products (including amyloid plaques linked to Alzheimer's), repairs neurons, and processes emotions. Chronic sleep deprivation impairs cognition, mood, and physical health."),
    ]),
    s("Reproductive Health and Development", [
      ("What is the difference between mitosis and meiosis?", "Somatic cell division vs. gamete production", "Mitosis: produces 2 identical diploid daughter cells (for growth and repair). Meiosis: produces 4 genetically unique haploid gametes (sperm/eggs) with half the chromosomes. Meiosis involves two divisions."),
      ("What is fertilization and when does it occur?", "Union of egg and sperm", "Fertilization occurs when a sperm cell successfully penetrates and fuses with an egg cell (usually in the fallopian tube), forming a diploid zygote. The zygote begins dividing by mitosis and implants in the uterus."),
      ("What are the stages of fetal development?", "Zygote → embryo → fetus", "Zygote (0-2 weeks): fertilized egg divides and implants. Embryo (3-8 weeks): organs and major body structures form (organogenesis) — most vulnerable period. Fetus (9 weeks-birth): growth and refinement of organ systems."),
      ("What are sexually transmitted infections (STIs) and how are they prevented?", "Infections spread through sexual contact", "STIs include HIV, chlamydia, gonorrhea, syphilis, HPV, and herpes. Prevention: abstinence, consistent correct condom use, vaccination (HPV, hepatitis B), regular testing, limiting partners, and open communication with partners and healthcare providers."),
    ]),
  ],
  [  # Unit 3: Advanced CS / Computer Science
    s("Artificial Intelligence Basics", [
      ("What is artificial intelligence?", "Machines that simulate human intelligence", "AI is the simulation of human intelligence processes by computer systems: learning (machine learning), reasoning, problem-solving, perception, and language understanding. It ranges from narrow AI (specific tasks) to theoretical general AI."),
      ("What is machine learning and how does it differ from traditional programming?", "Learning from data vs. explicit instructions", "Traditional programming: programmer writes explicit rules. Machine learning: the algorithm LEARNS rules from data. Given enough examples, ML models can identify patterns and make predictions without being explicitly programmed for each scenario."),
      ("What is a neural network and how is it inspired by the brain?", "Layered network of artificial neurons", "A neural network is a system of interconnected nodes (artificial neurons) in layers. Input data flows through layers, which extract increasingly abstract features. Inspired by biological neurons; adjusts connection weights through training to minimize error."),
      ("What are ethical concerns about artificial intelligence?", "Bias, privacy, job displacement, accountability", "Key concerns: algorithmic bias (AI reflecting and amplifying human biases), privacy (facial recognition, data surveillance), job displacement (automation), lack of transparency ('black box' decisions), and accountability (who is responsible when AI makes harmful decisions)."),
    ]),
    s("Cybersecurity", [
      ("What is cybersecurity and why is it increasingly important?", "Protecting computer systems and data from attacks", "Cybersecurity protects computer systems, networks, and data from unauthorized access, theft, and damage. As society increasingly depends on digital infrastructure (banking, healthcare, government), security vulnerabilities have greater real-world consequences."),
      ("What is a phishing attack?", "Social engineering to steal credentials or install malware", "Phishing is a cyberattack where an attacker impersonates a trusted entity (bank, employer) to trick users into revealing sensitive information (passwords, credit card numbers) or clicking malicious links that install malware."),
      ("What is encryption and how does it protect data?", "Converting data into unreadable form without a key", "Encryption transforms data using an algorithm and key so only authorized parties can read it. HTTPS encrypts web traffic; end-to-end encryption protects messages. Without the key, intercepted data is unreadable."),
      ("What is two-factor authentication (2FA) and why does it improve security?", "Requiring two forms of identity verification", "2FA requires both something you KNOW (password) and something you HAVE (phone code) or ARE (biometric). Even if a password is stolen, attackers still can't access the account without the second factor, dramatically improving security."),
    ]),
    s("Databases", [
      ("What is a relational database and what is SQL?", "Structured data in tables with SQL for querying", "A relational database stores data in tables (rows and columns) with defined relationships between tables. SQL (Structured Query Language) is the standard language for querying and manipulating relational databases."),
      ("Write a basic SQL query to select all students with grade > 90.", "Use SELECT, FROM, WHERE", "SELECT * FROM students WHERE grade > 90;"),
      ("What is a primary key in a database?", "Unique identifier for each record", "A primary key is a column (or combination of columns) that uniquely identifies each row in a table. Primary keys must be unique and not null. They are used to link tables in a relational database."),
      ("What is a JOIN in SQL and what does it do?", "Combining rows from two tables based on related columns", "A JOIN combines rows from two or more tables based on a related column. INNER JOIN: only rows with matching values in both tables. LEFT JOIN: all rows from the left table + matched rows from right. Used to query data spread across multiple tables."),
    ]),
    s("Cloud Computing and the Future", [
      ("What is cloud computing?", "Delivering computing services over the internet", "Cloud computing provides computing services (storage, servers, databases, networking, software) over the internet on a pay-as-you-go basis. Examples: AWS, Google Cloud, Azure. Enables scalability without physical infrastructure."),
      ("What is the Internet of Things (IoT)?", "Physical devices connected to the internet", "IoT refers to the network of physical devices (cars, appliances, medical devices, sensors) embedded with software and connectivity, enabling them to collect and exchange data. Examples: smart home devices, fitness trackers, smart city sensors."),
      ("What is big data and what makes it challenging to work with?", "Extremely large datasets requiring special processing", "Big data refers to datasets so large and complex they cannot be processed with traditional tools. Characterized by Volume (amount), Velocity (speed), and Variety (types). Requires specialized tools (Hadoop, Spark) and raises privacy concerns."),
      ("What are the most promising areas of technology development in the next decade?", "Emerging technologies shaping the future", "Key areas: AI/machine learning, quantum computing, biotechnology (gene therapy, mRNA vaccines), renewable energy technology, augmented/virtual reality, autonomous vehicles, and cybersecurity. These will reshape healthcare, work, communication, and society."),
    ]),
  ],
]
print("G12 science complete")

P[12]["ela"] = [
  [  # Unit 0: British and World Literature
    s("Shakespeare and Early Modern Literature", [
      ("What are the major themes in Shakespeare's tragedies?", "Think: ambition, jealousy, love, fate, and power", "Shakespeare's tragedies explore: ambition and its consequences (Macbeth), jealousy and manipulation (Othello), the nature of family and loyalty (King Lear), and the struggle between love and social obligation (Romeo and Juliet). Characters contain their own destruction."),
      ("What is a Shakespearean sonnet? Describe its structure.", "14-line poem with specific rhyme scheme", "A Shakespearean sonnet has 14 lines: three quatrains (ABAB CDCD EFEF) and a final rhyming couplet (GG). The poem typically introduces a problem in the quatrains and offers a resolution or twist in the couplet (volta)."),
      ("What is dramatic irony in Shakespeare? Give an example from a play.", "When the audience knows more than the character", "Dramatic irony: audience has knowledge a character lacks. In Romeo and Juliet, the audience knows Juliet is alive when Romeo finds her in the tomb, but Romeo believes she is dead. The tragic mistake results from this gap in knowledge."),
      ("What is the significance of Shakespeare's contribution to the English language?", "Shakespeare invented or popularized hundreds of words and phrases", "Shakespeare contributed approximately 1,700 new words and countless phrases to English: 'bedroom,' 'lonely,' 'swagger,' 'break the ice,' 'all that glitters is not gold.' His plays also shaped how English speakers understand human psychology and motivation."),
    ]),
    s("20th Century World Literature", [
      ("What is magical realism? Name a work that exemplifies it.", "Realistic setting with magical elements presented matter-of-factly", "Magical realism blends realistic settings with fantastical or magical elements treated as ordinary. Example: Gabriel Garcia Marquez's One Hundred Years of Solitude — the Buendia family's magical events (insomnia plague, ghost of Prudencio) coexist with historical reality."),
      ("What are the major themes in Chinua Achebe's Things Fall Apart?", "Colonialism, tradition, masculinity, and change", "Things Fall Apart explores: the impact of British colonialism on Igbo culture, conflict between tradition and change, the rigid concept of masculinity (Okonkwo's fatal flaw), and the tragedy of cultural destruction when one civilization overrides another."),
      ("How does Albert Camus use The Stranger to explore existentialism?", "Meursault as an absurd hero detached from social norms", "Meursault's emotional detachment and refusal to perform expected social rituals exposes the arbitrariness of social conventions. Camus illustrates the absurdist idea that life has no inherent meaning — the universe is indifferent to human needs. Meursault's 'crime' is being honest about this."),
      ("What is postcolonial literature and what themes does it typically address?", "Literature from formerly colonized peoples", "Postcolonial literature: written by authors from countries that experienced colonization. Common themes: cultural identity and hybridity, trauma of colonial violence, resistance and liberation, the legacy of imperialism, and the struggle to reclaim native languages and traditions."),
    ]),
    s("Literary Criticism", [
      ("What are the main schools of literary criticism?", "Different frameworks for analyzing texts", "Major schools: New Criticism (close reading of the text itself), Historical/Biographical (context of author's life and era), Reader-Response (reader's experience), Feminist Criticism (gender roles and power), Marxist Criticism (class and economics), Psychoanalytic (unconscious symbolism)."),
      ("How does a feminist literary critique analyze a text?", "Examines gender representation and power dynamics", "Feminist criticism examines: how female characters are portrayed, what roles are assigned to women vs. men, whose perspective dominates, how the text reflects or challenges patriarchal power structures, and whose voices are silenced or marginalized."),
      ("What is a close reading and what does it involve?", "Careful, detailed analysis of a short passage", "Close reading is careful, detailed analysis of a specific passage: examining word choice (diction), figurative language, syntax, imagery, tone, and structure. It connects these micro-level choices to larger themes and meaning."),
      ("How does historical context change how we read a text?", "Historical knowledge informs interpretation", "Historical context — the time, place, and circumstances of a text's creation — shapes its meaning. Example: reading Huckleberry Finn knowing 19th-century racial dynamics helps understand both its radical challenge to racism and its use of offensive language. Context doesn't excuse but explains."),
    ]),
    s("Comparative Essay Writing", [
      ("What is a comparative essay and how do you structure one?", "Essay analyzing two or more texts together", "A comparative essay examines similarities and/or differences between texts in relation to a theme, technique, or question. Structure options: block (all of text A, then all of text B) or alternating/point-by-point (compare on each aspect). Alternating is usually more sophisticated."),
      ("How do you develop a strong thesis for a comparative essay?", "Your thesis must make a specific interpretive claim about both texts", "A strong comparative thesis: (1) names both texts, (2) identifies the point of comparison, (3) makes a specific claim about the relationship (not just 'they are similar/different'). Example: 'While both authors use nature as a symbol of freedom, Thoreau sees it as achievable while Cather treats it as ultimately elusive.'"),
      ("What is a transition sentence in a comparative essay?", "Bridge between paragraphs connecting both texts", "A transition sentence moves from one text/idea to the next while maintaining the thread of comparison. Example: 'While Fitzgerald depicts the American Dream as already corrupted, Steinbeck shows it being destroyed by economic forces outside individual control.'"),
      ("What makes a literary argument persuasive?", "Strong claim, textual evidence, and analysis", "A persuasive literary argument: (1) makes a specific, debatable claim. (2) supports it with direct textual evidence (quotes). (3) analyzes HOW the evidence supports the claim. (4) acknowledges and addresses counterarguments. (5) maintains a consistent, reasoned tone."),
    ]),
  ],
  [  # Unit 1: Senior Writing Portfolio
    s("Polishing Argumentative Writing", [
      ("What is the difference between a claim and an assertion?", "Assertion = statement; claim = debatable assertion", "An assertion is any statement. A claim is a debatable assertion that requires evidence and reasoning to support it. 'The sky is blue' is an assertion. 'Social media harms adolescent mental health' is a claim."),
      ("How do you integrate evidence without dropping quotes?", "Introduce, quote, explain (ICE)", "ICE method: (I)ntroduce the source/context, (C)ite the evidence (quote or paraphrase), (E)xplain how it supports your argument. Quotes should never stand alone; always analyze their significance."),
      ("What is hedging language and when should you use it in academic writing?", "Language that qualifies claims appropriately", "Hedging language (may, suggests, appears, often, tends to) qualifies claims that aren't absolute. Use when: evidence doesn't guarantee the conclusion, you're discussing patterns not rules, or claims may have exceptions. Avoids overstatement."),
      ("What are the most common errors in formal academic writing?", "Think: vague language, passive misuse, unsupported claims", "Common errors: vague language ('things,' 'stuff'), unnecessary passive voice, unsupported claims, logical fallacies, weak transitions, comma splices, inconsistent tense, and missing or incorrect citations."),
    ]),
    s("The College Application Essay", [
      ("What is the purpose of a college application essay?", "Reveal personality and voice beyond grades and test scores", "The essay humanizes your application — it tells admissions officers WHO you are, not just what you've achieved. It reveals voice, values, intellectual curiosity, resilience, or self-awareness that a transcript cannot show."),
      ("What makes a college essay topic too generic?", "Topics that could be written by thousands of applicants", "Generic topics: sports injury taught me perseverance, mission trip changed my worldview, a deceased relative I admired. These are cliché not because experiences are invalid, but because they're told without specific, unique personal insight. The story must be distinctly YOURS."),
      ("What is the revision process for a college essay?", "Multiple rounds addressing different levels of craft", "Revision stages: (1) Content revision — Does it reveal something meaningful? (2) Structure revision — Is the narrative arc clear? (3) Sentence-level revision — Is each sentence earning its place? (4) Proofreading — Grammar and mechanics. Get trusted feedback at each stage."),
      ("What should you do after receiving an essay prompt like 'Describe a challenge you faced'?", "Transform the expected into something specific and surprising", "Resist the predictable. Choose a specific, often small moment that reveals depth. Focus on internal journey (growth, complexity) not just external events. The most memorable essays are concrete and surprising, not heroic summaries."),
    ]),
    s("Career and Professional Writing", [
      ("What should a resume include and how should it be formatted?", "Key document for job applications", "A resume should include: contact information, education (reverse chronological), work/volunteer experience (reverse chronological, with bullet points using action verbs and quantifiable achievements), skills, and relevant activities. 1 page for students/entry-level."),
      ("How do you write a professional cover letter?", "Targeted letter accompanying job application", "Cover letter structure: (1) Opening — identify position and express enthusiasm. (2) Body — highlight 2-3 relevant skills/experiences with specific examples. (3) Closing — express interest in interview, thank the reader. Keep to one page; customize for each position."),
      ("What is professional email etiquette?", "Standards for workplace digital communication", "Professional email: clear subject line, appropriate greeting, concise and direct body, professional tone (no slang), proofread before sending, appropriate closing, full name signature. Respond within 24-48 hours to professional correspondence."),
      ("What is the difference between descriptive, narrative, expository, and persuasive writing?", "Four main writing modes", "Descriptive: creates a sensory picture. Narrative: tells a story with plot and characters. Expository: explains or informs using facts and analysis. Persuasive/argumentative: advocates for a position with evidence. Most professional writing blends modes."),
    ]),
  ],
  [  # Unit 2: Capstone Reading and Discussion
    s("Seminar Discussion Skills", [
      ("What is a Socratic seminar and how does it work?", "Student-led discussion exploring a central question", "A Socratic seminar is a collaborative discussion where students examine ideas from a text or question using dialogue, evidence, and reasoning. There is no single correct answer; the goal is to deepen understanding through open inquiry and respectful challenge."),
      ("What makes a strong contribution to a seminar discussion?", "Building on others, using evidence, asking good questions", "Strong contributions: respond directly to what was said, cite textual evidence, ask genuine questions that advance discussion, acknowledge other perspectives before offering your own, and challenge ideas respectfully with reasoning — not just opinion."),
      ("What is active listening and why is it critical in discussion?", "Full engagement with what others are saying", "Active listening means giving full attention to the speaker, not formulating your response while they talk, noting key claims and evidence, paraphrasing to confirm understanding, and building your contribution on what was actually said."),
      ("How can you respectfully challenge someone's idea in academic discussion?", "Disagree with the argument, not the person", "Use language like: 'That's interesting, but I'd push back on...', 'I see it differently — the text suggests...', 'Could that also be explained by...?'. Attack the argument with evidence, not the person. Model intellectual humility — you might be wrong too."),
    ]),
    s("Legacy and Synthesis", [
      ("What is the most important thing literature teaches us?", "A question worth genuinely thinking about", "Literature teaches empathy — the ability to inhabit another consciousness and understand experiences different from your own. It also teaches us to sit with ambiguity, think through moral complexity, and recognize the universal human experiences beneath surface differences."),
      ("How do the texts you have read in high school connect to your own life or the contemporary world?", "Personal synthesis across your reading", "Synthesis: identifying how a theme, idea, or question from literature recurs in your own experience or current events. Example: The Great Gatsby's critique of wealth inequality resonates with contemporary debates about economic mobility and the American Dream."),
      ("What is your responsibility as a reader when engaging with difficult or challenging texts?", "Ethical dimensions of reading", "As a reader you are responsible for: engaging seriously rather than dismissively, considering historical context before judging, distinguishing an author's views from a character's, and bringing critical awareness to texts that may perpetuate harmful views while still extracting their literary value."),
      ("If you could assign one book to everyone in your country to read, what would it be and why?", "A question requiring genuine literary argument", "Any defensible choice — the key is argumentation: What values does the book convey? What perspective does it offer that is broadly needed? Who would it help people understand? This synthesizes literary analysis with civic thinking."),
    ]),
    s("Independent Reading and Lifelong Literacy", [
      ("Why does reading for pleasure matter beyond school?", "Long-term cognitive and social benefits", "Regular reading builds: vocabulary and cognitive reserve (protecting against dementia), empathy and social intelligence, knowledge across domains, concentration in an attention-fractured world, and lifelong access to ideas and perspectives beyond personal experience."),
      ("How do you choose your next book? What makes something worth reading?", "Developing personal reading judgment", "Criteria for choosing: Does the premise interest me? Does the author have a distinctive perspective? Has it been recommended by someone with similar taste? Does it challenge me or offer a perspective I lack? Is it widely discussed for a reason I find compelling?"),
      ("How has your reading changed the way you think about something specific?", "Reflective connection between reading and thinking", "Reflective synthesis: identify a specific text and a specific belief, assumption, or behavior it challenged or changed. Trace the connection concretely. Strong readers are changed by what they read — they encounter ideas that don't let them think the same way afterward."),
      ("What is the relationship between reading widely and writing well?", "Reading is the foundation of writing", "Writers internalize sentence rhythms, vocabulary, argument structures, and narrative techniques from reading. Reading widely exposes you to different styles and genres. The best writing instruction is reading deeply and analyzing what makes effective writing work."),
    ]),
  ],
]
print("G12 ELA complete")

P[12]["history"] = [
  [  # Unit 0: Government and Political Science
    s("US Government Structure", [
      ("What is federalism and how does it work in the US?", "Division of power between national and state governments", "Federalism divides government powers between the federal (national) government and state governments. The Constitution grants specific powers to federal government (coining money, military); reserves others to states (education, most police powers); and shares some (taxation)."),
      ("What are the checks and balances built into the US government?", "Each branch limits the others", "Congress makes laws (legislative); President can veto them (executive); Courts can declare them unconstitutional (judicial). Congress can override vetoes with 2/3 vote. President appoints judges; Senate confirms. This prevents any branch from becoming too powerful."),
      ("What is the role of the Supreme Court and what is judicial review?", "Highest court; interprets the Constitution", "The Supreme Court is the final interpreter of the Constitution. Judicial review (established in Marbury v. Madison, 1803) gives courts the power to strike down laws that violate the Constitution. Justices serve lifetime appointments to ensure independence."),
      ("What is the difference between a democracy, a republic, and an oligarchy?", "Different systems of governance", "Democracy: citizens directly make decisions. Republic: citizens elect representatives to make decisions on their behalf (what the US is). Oligarchy: small group of powerful people (wealthy, military) rule. These categories often overlap in practice."),
    ]),
    s("Political Parties and Elections", [
      ("What are the main differences between the Democratic and Republican parties today?", "Core values and policy positions", "Democrats: tend to favor government programs for social welfare, environmental regulation, progressive taxation, and social liberalism. Republicans: tend to favor smaller government, lower taxes, less regulation, and social conservatism. Both parties contain diverse coalitions."),
      ("What is gerrymandering and how does it affect elections?", "Manipulating district boundaries for partisan advantage", "Gerrymandering is the manipulation of electoral district boundaries to favor one party. It can create 'packed' districts (concentrating opposition voters) and 'cracked' districts (diluting opposition). It can allow a party to win more seats than their vote share would proportionally warrant."),
      ("What is the Electoral College and why is it controversial?", "US system for electing the President", "The Electoral College: each state gets electors = its representatives + senators. A candidate needs 270 of 538 electoral votes to win. It's controversial because: (1) a candidate can win the popular vote but lose the election, (2) it gives smaller states disproportionate influence."),
      ("What is voter turnout and what factors affect it?", "Percentage of eligible voters who vote", "Voter turnout is the percentage of eligible citizens who actually vote. Factors: age (older people vote more), education, income (higher = more voting), voter registration requirements, geographic location, and competitive elections. US turnout is comparatively low among democracies."),
    ]),
    s("Constitutional Issues", [
      ("How has the First Amendment been interpreted by the courts?", "Freedom of religion, speech, press, assembly, and petition", "The First Amendment protects speech but not all speech — courts have ruled some speech unprotected (incitement to imminent lawless action, true threats, obscenity). Public school students have limited First Amendment rights; government employees more so than private employees."),
      ("What does the Fourth Amendment protect against?", "Unreasonable searches and seizures", "The Fourth Amendment protects against unreasonable searches and seizures and requires warrants based on probable cause. Courts have debated its application to digital data, cell phone searches, and surveillance in the digital age."),
      ("What is due process and what does it guarantee?", "Fair legal procedures", "Due process (Fifth and Fourteenth Amendments): the government must follow fair procedures before depriving citizens of life, liberty, or property. Includes: right to notice, right to be heard, and right to a fair and impartial decision-maker."),
      ("How does the 14th Amendment's Equal Protection Clause work?", "Government must treat similarly situated people equally", "Equal protection requires government to treat people equally under the law. Courts scrutinize laws that classify people by race (strict scrutiny) or sex (intermediate scrutiny). Key cases: Brown v. Board (desegregation), Obergefell v. Hodges (marriage equality)."),
    ]),
    s("Policy Making", [
      ("What is public policy and how is it made?", "Government actions to address public issues", "Public policy is what governments choose to do (or not do) about public issues. It's made through: identifying problems, agenda-setting, formulation (developing options), adoption (passing laws), implementation (carrying out), and evaluation (assessing effectiveness)."),
      ("What are interest groups and how do they influence policy?", "Organizations that advocate for specific causes", "Interest groups represent corporations, professions, causes, or ideologies and try to influence government policy through: lobbying (direct contact with legislators), campaign contributions, public advocacy, litigation, and grassroots organizing."),
      ("What is the role of the media in a democracy?", "The 'Fourth Estate' — checking power and informing citizens", "Media serves democracy by: informing citizens about government actions, setting the public agenda (what issues people think about), providing a forum for debate, and holding government accountable through investigative journalism. Media bias and misinformation are ongoing challenges."),
      ("What is the difference between fiscal policy and monetary policy?", "Two main economic policy tools", "Fiscal policy: government decisions about taxing and spending (controlled by Congress and President). Monetary policy: decisions about money supply and interest rates (controlled by the Federal Reserve/central bank). Both are used to stabilize the economy."),
    ]),
  ],
  [  # Unit 1: Economics
    s("Economic Principles", [
      ("What is economics and what are the two main branches?", "Study of scarcity and resource allocation", "Economics studies how individuals, businesses, and governments allocate scarce resources. Microeconomics: behavior of individuals and businesses. Macroeconomics: behavior of entire economies (inflation, unemployment, GDP)."),
      ("What is GDP and what does it measure?", "Gross Domestic Product", "GDP is the total market value of all goods and services produced within a country in a year. It measures economic output and is used to compare economic size and growth. GDP per capita adjusts for population size."),
      ("What is inflation and what causes it?", "General rise in prices over time", "Inflation is the general increase in prices (and decrease in purchasing power) over time. Causes: demand-pull (too much money chasing too few goods), cost-push (rising production costs), and money supply growth. Measured by CPI (Consumer Price Index)."),
      ("What is unemployment and what are its types?", "People able and willing to work but without jobs", "Types of unemployment: Frictional (between jobs, normal). Structural (skills don't match jobs available, often from technological change). Cyclical (from economic recession). Natural unemployment rate = frictional + structural. Zero unemployment is impossible and undesirable."),
    ]),
    s("Market Structures", [
      ("What is the difference between perfect competition and a monopoly?", "Many competitive firms vs. one dominant firm", "Perfect competition: many firms selling identical products, no pricing power (e.g., wheat markets). Monopoly: one firm dominates with no close substitutes, has significant pricing power (e.g., utilities). Most markets fall between these extremes."),
      ("What is a market failure and what can cause it?", "When markets fail to allocate resources efficiently", "Market failures occur when: externalities (costs/benefits not reflected in prices), public goods (non-excludable, non-rival — like national defense), information asymmetry (one party knows more), or monopoly power distort efficient allocation."),
      ("What is an externality? Give examples of positive and negative externalities.", "Side effects of economic activity affecting third parties", "Externalities are costs or benefits imposed on third parties not directly involved in a transaction. Negative: factory pollution harms nearby residents (not in the price). Positive: vaccination benefits the whole community beyond the individual who gets vaccinated."),
      ("What is the law of supply and demand?", "Core principle of market economics", "Law of Demand: as price increases, quantity demanded decreases (inverse relationship). Law of Supply: as price increases, quantity supplied increases (direct relationship). Equilibrium: the price where quantity demanded equals quantity supplied."),
    ]),
    s("Global Economics", [
      ("What is comparative advantage and how does it justify trade?", "Principle underlying international trade", "Comparative advantage: a country should produce and export goods it can produce at a LOWER OPPORTUNITY COST than other countries, even if it can produce everything more efficiently (absolute advantage). Trade based on comparative advantage benefits all parties."),
      ("What is the difference between free trade and protectionism?", "Open markets vs. protecting domestic industries", "Free trade: no barriers to international commerce (lower prices, greater choice, efficiency). Protectionism: tariffs, quotas, or subsidies to shield domestic industries from foreign competition (protects jobs and industries but raises prices for consumers)."),
      ("What is the role of the World Trade Organization (WTO)?", "International body regulating global trade", "The WTO provides a framework for international trade rules, facilitates trade negotiations, resolves trade disputes between member countries, and promotes free trade by reducing barriers. Critics argue it favors wealthy nations."),
      ("What is income inequality and how is it measured?", "Gap between high and low earners in an economy", "Income inequality is the unequal distribution of income across society. Measured by: the Gini coefficient (0 = perfect equality, 1 = perfect inequality), and income share ratios (top 1% vs. bottom 50%). Inequality has grown in most developed countries since the 1980s."),
    ]),
    s("Personal and Applied Economics", [
      ("What is the difference between needs and wants in economics?", "Necessities vs. desires", "Needs: goods and services necessary for survival and basic wellbeing (food, shelter, healthcare, clothing). Wants: goods and services desired but not essential (luxury goods, entertainment). Understanding this distinction is foundational for personal financial decision-making."),
      ("What is a market economy vs. a command economy?", "Decentralized vs. centralized economic decisions", "Market economy: individual buyers and sellers make economic decisions through prices (US, most developed nations). Command economy: government makes central decisions about production and distribution (North Korea, historical Soviet Union). Most economies are mixed."),
      ("What is behavioral economics?", "How psychology affects economic decision-making", "Behavioral economics combines psychology and economics to explain why people don't always make rational decisions. Key concepts: loss aversion (losses feel worse than equal gains feel good), anchoring (initial price influences decisions), and status quo bias (preferring the current state)."),
      ("How does the stock market work?", "Public market for buying and selling company shares", "Companies issue shares (stock) to raise capital. Investors buy shares, hoping to profit from company growth (price appreciation) or dividends. Stock prices reflect investors' expectations of future earnings. Major indices (S&P 500, Dow Jones) track overall market performance."),
    ]),
  ],
  [  # Unit 2: Contemporary Global Issues
    s("International Relations", [
      ("What are the main theories of international relations?", "Realism, liberalism, constructivism", "Realism: states pursue self-interest and power in an anarchic system; conflict is inevitable. Liberalism: cooperation is possible through international institutions, trade, and democracy. Constructivism: ideas, norms, and identities shape international behavior, not just material power."),
      ("What is deterrence theory in nuclear strategy?", "Preventing attack by threatening unbearable retaliation", "Nuclear deterrence (MAD — Mutually Assured Destruction): the threat that any nuclear attack will trigger devastating retaliation prevents first strikes. As long as both sides have second-strike capability, rational actors won't initiate nuclear war."),
      ("What is soft power vs. hard power?", "Attraction and persuasion vs. coercion and force", "Hard power: using military force or economic coercion to influence others. Soft power (Joseph Nye): using attraction — culture, values, institutions, diplomacy — to win influence without force. The US exercises both; China increasingly invests in soft power."),
      ("What are the main responsibilities of the United Nations?", "International organization promoting peace, human rights, development", "The UN's main bodies: Security Council (peace and security — 5 permanent veto members), General Assembly (forum for all nations), Secretariat (administrative), ICJ (international law). Functions: peacekeeping, humanitarian aid, human rights monitoring, sustainable development goals."),
    ]),
    s("21st Century Global Challenges", [
      ("What is terrorism and what distinguishes it from conventional warfare?", "Political violence targeting civilians to create fear", "Terrorism is the deliberate use of violence against civilians to advance political, ideological, or religious goals. Unlike conventional warfare (military vs. military), terrorism deliberately targets civilians. State and non-state actors can both engage in terrorism."),
      ("What drives international migration and refugee crises?", "Push and pull factors", "Push factors (leaving home): conflict, persecution, extreme poverty, climate change impacts, natural disasters. Pull factors (toward destination): economic opportunity, political stability, family connections, rule of law. Distinguishing economic migrants from refugees matters under international law."),
      ("What are the Sustainable Development Goals (SDGs)?", "17 global goals adopted by UN in 2015", "The 17 SDGs (2030 Agenda) address: poverty, hunger, health, education, gender equality, clean water, clean energy, economic growth, reduced inequalities, sustainable cities, climate action, and partnerships. They set targets for global development by 2030."),
      ("How does technology affect national security and international relations?", "Cyberwarfare, surveillance, and information warfare", "Technology has transformed security: cyberattacks can disrupt infrastructure without conventional warfare, surveillance technology enables authoritarianism, social media enables information warfare (disinformation campaigns), and autonomous weapons raise new ethical and legal questions."),
    ]),
    s("Social Justice and Human Rights", [
      ("What is systemic racism and how does it differ from individual racism?", "Racist policies and practices embedded in institutions vs. individual prejudice", "Individual racism: personal prejudice and discrimination. Systemic/institutional racism: policies, practices, and social structures that produce racial inequities regardless of individual intentions. Examples: disparities in lending, criminal justice, housing, and healthcare outcomes."),
      ("What is intersectionality?", "Multiple identities create overlapping experiences of privilege or oppression", "Intersectionality (Kimberle Crenshaw) recognizes that people have multiple identities (race, gender, class, sexuality) that intersect and create unique experiences. Someone who is both Black and a woman faces specific compounded forms of discrimination not captured by looking at race or gender alone."),
      ("What progress has been made on global poverty reduction, and what challenges remain?", "Dramatic gains and persistent inequalities", "Progress: extreme poverty (under $1.90/day) fell from 36% in 1990 to under 10% in 2019, largely due to growth in China and India. Challenges: COVID-19 reversed gains, climate change threatens progress, inequality WITHIN countries has often grown, and Sub-Saharan Africa lags."),
      ("What is environmental justice?", "The equitable distribution of environmental benefits and burdens", "Environmental justice addresses the disproportionate burden of environmental hazards (pollution, flooding, toxic waste) on low-income communities and communities of color. Environmental benefits (parks, clean air) are also unequally distributed. Both reflect structural inequality."),
    ]),
  ],
]
print("G12 history complete")

P[12]["cs"] = [
  [  # Unit 0: Capstone Projects and Software Engineering
    s("Software Development Process", [
      ("What are the stages of the software development lifecycle (SDLC)?", "Process of planning, creating, and maintaining software", "SDLC stages: 1. Planning. 2. Requirements analysis. 3. System design. 4. Implementation (coding). 5. Testing. 6. Deployment. 7. Maintenance. Different methodologies (Waterfall, Agile) approach these stages differently."),
      ("What is the difference between Waterfall and Agile development?", "Sequential vs. iterative development", "Waterfall: linear, sequential — complete each phase before moving to the next. Best for fixed requirements. Agile: iterative — work in short sprints, deliver working software frequently, adapt to changing requirements. Most modern software uses Agile."),
      ("What is version control and why is it important?", "Tracking changes to code over time", "Version control (e.g., Git) tracks every change to a codebase: who changed what and when. It allows: reverting to previous versions, working on features in branches without breaking main code, collaboration, and maintaining a history of the project."),
      ("What is the difference between unit testing and integration testing?", "Testing individual components vs. how they work together", "Unit testing: testing individual functions or components in isolation (does this function return the right value?). Integration testing: testing how multiple components work together (does the login system work end-to-end?). Both are essential."),
    ]),
    s("APIs and System Design", [
      ("What is an API (Application Programming Interface)?", "A way for different software systems to communicate", "An API defines how software components interact. Web APIs allow different applications to communicate over the internet. Example: a weather app uses a weather service's API to retrieve current data. APIs enable modular, scalable software development."),
      ("What is a REST API?", "A common web API architecture using HTTP", "REST (Representational State Transfer) APIs use HTTP methods: GET (retrieve data), POST (create), PUT (update), DELETE (remove). They return data (usually JSON) that can be used by any client. REST is the most common web API style."),
      ("What is the difference between a client and a server?", "The two sides of networked applications", "Client: the software that requests resources or services (your browser, a mobile app). Server: the software that receives requests and provides resources (a web server hosting a website, a database server). Communication happens over a network using protocols."),
      ("What is a microservices architecture?", "Building applications as small independent services", "Microservices: instead of one large application (monolith), functionality is split into small, independent services that communicate via APIs. Benefits: easier to scale, deploy, and maintain individual services. Used by Netflix, Amazon, Spotify."),
    ]),
    s("Capstone Project Planning", [
      ("What makes a good software project proposal?", "Clear problem, feasible solution, defined scope", "A good proposal: (1) identifies a real problem worth solving. (2) describes a specific, feasible solution. (3) defines the scope (what it will and won't do). (4) identifies users and their needs. (5) describes the technology stack and approach."),
      ("How do you decompose a large project into manageable tasks?", "Breaking down complex problems", "Decomposition: identify major features → break each into user stories ('As a user, I can...') → break user stories into specific coding tasks → estimate effort for each → prioritize based on importance and dependencies."),
      ("What is a minimum viable product (MVP)?", "The smallest version of a product that still provides value", "An MVP is the simplest version of a product with just enough features to satisfy early users and provide feedback. Building an MVP first avoids wasting time on features users don't want. Iterate based on feedback."),
      ("What documentation should accompany a software project?", "Making your project understandable to others", "Documentation should include: README (what the project does, how to install and run it), code comments (explaining complex logic), API documentation (for public APIs), user documentation (how to use it), and a description of design decisions made."),
    ]),
    s("Ethics in Computing", [
      ("What is the digital divide and why does it matter?", "Unequal access to technology", "The digital divide is the gap between those with access to digital technologies (computers, internet) and those without. It correlates with income, geography, age, and disability. As society and economy move online, those without access face growing disadvantages."),
      ("What are the ethical responsibilities of software developers?", "Professional obligations in building technology", "Software developers are responsible for: writing secure, accessible code, considering how software might be misused, protecting user data and privacy, avoiding building systems that discriminate, being transparent about limitations, and speaking up when asked to do something harmful."),
      ("What is data privacy and how do regulations like GDPR protect it?", "The right to control your own personal data", "Data privacy is the right to control how your personal information is collected, used, and shared. GDPR (Europe's General Data Protection Regulation, 2018): requires consent, right to access and delete data, mandatory breach notification, and significant fines for violations."),
      ("What is algorithmic bias and how can it be detected and reduced?", "When algorithms produce unfair outcomes for certain groups", "Algorithmic bias occurs when an AI or algorithm produces systematically unfair outcomes for some groups, often because training data reflects historical inequalities. Detect it by: auditing outcomes across demographic groups. Reduce it by: diverse training data, diverse development teams, ongoing monitoring."),
    ]),
  ],
  [  # Unit 1: Advanced Topics
    s("Machine Learning in Practice", [
      ("What is the difference between supervised and unsupervised learning?", "Labeled data vs. no labels", "Supervised: model learns from labeled training data (input-output pairs). Example: spam classifier trained on labeled emails. Unsupervised: model finds patterns in unlabeled data. Example: clustering customers into groups based on purchasing behavior."),
      ("What is overfitting in machine learning and how do you prevent it?", "Model too closely fits training data", "Overfitting: model learns the training data too specifically and fails to generalize to new data (high training accuracy, low test accuracy). Prevention: more training data, regularization, dropout (neural nets), cross-validation, and simpler models."),
      ("What is a training set, validation set, and test set?", "Three partitions of data for ML development", "Training set: data used to train the model (learn parameters). Validation set: used during development to tune hyperparameters and prevent overfitting. Test set: held completely aside until the end to evaluate final model performance on unseen data."),
      ("What are the steps to build a basic machine learning model?", "End-to-end ML workflow", "1. Define the problem. 2. Collect and prepare data. 3. Choose a model type. 4. Train the model on training data. 5. Evaluate on validation set and tune. 6. Test on test set. 7. Deploy. 8. Monitor and retrain as needed."),
    ]),
    s("Quantum Computing Introduction", [
      ("What is a qubit and how does it differ from a classical bit?", "Quantum vs. classical information unit", "A classical bit is either 0 or 1. A qubit can be 0, 1, or both simultaneously (superposition) until measured. This allows quantum computers to explore many solutions at once, giving them potential advantages for certain problems."),
      ("What is quantum superposition?", "A qubit existing in multiple states simultaneously", "Superposition means a qubit can represent 0 and 1 at the same time until observed/measured. When measured, it collapses to either 0 or 1 with certain probabilities. With n qubits, a quantum computer can represent 2^n states simultaneously."),
      ("What problems might quantum computers solve that classical computers cannot?", "Quantum advantage in specific domains", "Quantum computers show promise for: factoring large numbers (breaking RSA encryption — Shor's algorithm), searching unsorted databases faster (Grover's algorithm), simulating molecules (drug discovery, materials science), and optimization problems."),
      ("What is quantum entanglement?", "Correlated quantum states between particles", "Entanglement: two qubits become correlated so that measuring one instantly determines the state of the other, regardless of distance. Einstein called it 'spooky action at a distance.' It enables quantum cryptography and is a key resource for quantum computing."),
    ]),
    s("The Future of Computing", [
      ("What is edge computing?", "Processing data near its source rather than in the cloud", "Edge computing processes data at or near the source (on devices, local servers) rather than sending it to a central cloud. Benefits: lower latency, reduced bandwidth, better privacy, enables real-time decisions. Used in autonomous vehicles, IoT, industrial systems."),
      ("What is a distributed system?", "Computing across multiple machines that appear as one", "A distributed system is a collection of computers that work together and appear to users as a single system. Examples: the internet, cloud storage, blockchain. Challenges include: consistency (all nodes see same data), availability, and partition tolerance (CAP theorem)."),
      ("What is open source software and why does it matter?", "Software with publicly available source code", "Open source software has its source code publicly available, allowing anyone to view, modify, and distribute it. Examples: Linux, Python, Firefox. It fosters collaboration, innovation, and access to technology. Most of the internet's infrastructure runs on open source software."),
      ("How might computing change society in the next 20 years?", "Speculative but evidence-based forward-looking question", "Likely impacts: AI automating many cognitive jobs (requiring workforce retraining), quantum computing breaking current encryption (requiring post-quantum cryptography), neurotechnology (brain-computer interfaces), biocomputing, and increasing tension between surveillance capabilities and privacy rights."),
    ]),
  ],
]
print("G12 CS complete")

P[12]["health"] = [
  [  # Unit 0: Adult Health and Wellness
    s("Lifelong Wellness", [
      ("What are the eight dimensions of wellness?", "A holistic model of human wellbeing", "1. Physical. 2. Emotional. 3. Social. 4. Intellectual. 5. Spiritual. 6. Environmental. 7. Financial. 8. Occupational. True wellness requires balance across all dimensions, not just physical health."),
      ("What is the difference between intrinsic and extrinsic motivation for health behavior?", "Internal desire vs. external reward", "Intrinsic motivation: doing something for the internal reward (feeling good, genuine enjoyment). Extrinsic: doing it for external rewards (money, approval). Intrinsic motivation is more sustainable for long-term health behavior change."),
      ("What is self-efficacy and how does it affect health decisions?", "Belief in your ability to succeed", "Self-efficacy is confidence in your ability to perform a specific behavior. Higher self-efficacy → more likely to attempt and persist through challenges. It's built through: mastery experiences (success), vicarious learning, social encouragement, and managing stress states."),
      ("What is the difference between primary, secondary, and tertiary prevention?", "Before, detecting, and managing disease", "Primary prevention: stops disease before it starts (vaccination, healthy diet). Secondary prevention: early detection and treatment (cancer screening, blood pressure monitoring). Tertiary prevention: managing existing disease to prevent complications (rehabilitation, managing chronic conditions)."),
    ]),
    s("Healthcare Systems", [
      ("What is the difference between a GP, specialist, and emergency medicine?", "Different levels and types of medical care", "General Practitioner (GP/primary care): first contact, manages overall health. Specialist: focuses on a specific system or disease (cardiologist, neurologist). Emergency medicine: handles acute, life-threatening situations. The healthcare system works best as a coordinated team."),
      ("What is health insurance and how does it work?", "Risk pooling to cover healthcare costs", "Health insurance spreads financial risk across many people. Members pay premiums; the insurer pays covered costs above the deductible. Key terms: premium (monthly payment), deductible (amount you pay first), copay (fixed cost per visit), network (contracted providers)."),
      ("What is the difference between a cure and a treatment?", "Eliminating disease vs. managing it", "A cure eliminates the disease entirely (antibiotics for bacterial infection). A treatment manages symptoms or slows progression without eliminating the cause (most chronic disease management — insulin for diabetes doesn't cure it). Both have important roles."),
      ("What role does patient advocacy play in healthcare?", "Speaking up for your own or others' care", "Patient advocacy means actively participating in healthcare decisions: asking questions, understanding diagnoses and treatment options, seeking second opinions, understanding your rights, and communicating concerns clearly. Informed, engaged patients tend to get better care."),
    ]),
    s("Reproductive and Sexual Health", [
      ("What are the most reliable forms of contraception and how do they work?", "Methods to prevent pregnancy", "Most effective: hormonal methods (pill, patch, ring, shot, implant — 91-99% effective) and IUDs (99%+ effective). Less effective alone: condoms (85-98%), diaphragm. Condoms are the only method that also protects against STIs."),
      ("What are the symptoms and treatments for common STIs?", "Sexually transmitted infections", "Common STIs: Chlamydia (often asymptomatic, treated with antibiotics), Gonorrhea (discharge, burning, treated with antibiotics), HIV (progressive — antiretroviral therapy manages but doesn't cure), HPV (common — vaccine available, causes genital warts and some cancers), Herpes (lifelong, managed with antivirals)."),
      ("What is consent and what are its key components?", "Voluntary agreement to sexual activity", "Consent must be: Freely given (no pressure), Reversible (can be withdrawn at any time), Informed (all parties understand what they're agreeing to), Enthusiastic (genuine desire, not just absence of no), and Specific (consent to one activity doesn't mean all). Applies every time."),
      ("What is family planning and what resources are available?", "Making intentional decisions about reproduction", "Family planning involves decisions about if, when, and how many children to have. Resources: Planned Parenthood, OB/GYN offices, Title X funded clinics, health departments. Includes contraception counseling, fertility support, prenatal care, and STI testing."),
    ]),
  ],
  [  # Unit 1: Life Skills for Independent Living
    s("Mental Health in Adulthood", [
      ("What are the signs that someone might benefit from professional mental health support?", "Recognizing when to seek help", "Signs: persistent sadness, anxiety, or mood changes; difficulty functioning at work/school; relationship problems; substance use to cope; thoughts of self-harm; feeling overwhelmed consistently. Seeking help is a sign of strength, not weakness."),
      ("What is the difference between a psychologist, psychiatrist, and therapist?", "Different mental health professionals", "Psychiatrist: medical doctor (MD) who can prescribe medication; treats more complex conditions. Psychologist (PhD/PsyD): specializes in psychological testing and therapy; cannot prescribe (in most states). Therapist/counselor: provides talk therapy; various licensing levels."),
      ("What are healthy boundaries and why are they important in adult relationships?", "Limits protecting your wellbeing", "Healthy boundaries define what you will and won't accept in relationships. They protect your emotional, physical, and mental wellbeing. Setting them requires: knowing your values, communicating clearly, and following through consistently. Lack of boundaries often leads to resentment and burnout."),
      ("How can you support a friend who is struggling with mental health?", "Being a good support person", "Listen without judgment, take their concerns seriously, don't try to 'fix' it or minimize, ask how you can help, encourage professional support, check in regularly, and know the warning signs of crisis (talk of suicide). Take care of your own mental health too."),
    ]),
    s("Navigating Adulthood", [
      ("What are the key legal rights and responsibilities you gain at age 18?", "Transition to legal adulthood", "At 18: right to vote, sign legal contracts, join the military without parental consent, access your own medical records, be tried as an adult, be evicted by parents. Responsibilities: jury duty, selective service registration (men), full legal accountability for actions."),
      ("What is a living will and why might a young adult need one?", "Legal document specifying medical wishes", "A living will (advance directive) specifies your wishes for medical care if you become incapacitated (life support, CPR, feeding tubes). While young adults rarely need them, accidents can happen at any age. It relieves family from having to make agonizing decisions."),
      ("What are the health risks associated with recreational substance use in young adults?", "Age-specific impacts", "Young adults (18-25) are at higher risk because the prefrontal cortex (decision-making, impulse control) isn't fully developed until 25. Risks: higher addiction vulnerability, cognitive impairment, mental health exacerbation, legal consequences, and accidents."),
      ("What is work-life balance and why does it matter for long-term health?", "Managing professional and personal life demands", "Work-life balance is maintaining a sustainable equilibrium between career demands and personal life (relationships, health, hobbies, rest). Chronic imbalance leads to burnout, physical health problems (cardiovascular disease, immune suppression), and damaged relationships. Requires intentional boundaries."),
    ]),
  ],
]
print("G12 health complete")

# ─── SERIALIZE TO JSON AND INJECT INTO HTML ───
import re

def serialize_p(P):
    lines = ["const PRACTICE = {"]
    grades = sorted(P.keys())
    for gi, grade in enumerate(grades):
        lines.append(f"  {grade}: {{")
        subjects = list(P[grade].keys())
        for si, subj in enumerate(subjects):
            lines.append(f"    {subj}: [")
            units = P[grade][subj]
            for ui, unit in enumerate(units):
                lines.append("      [")
                for sheet in unit:
                    title = sheet["title"].replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
                    lines.append(f"        {{ title: `{title}`, problems: [")
                    for prob in sheet["problems"]:
                        q = prob["q"].replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
                        ex = prob["ex"].replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
                        a = prob["a"].replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
                        lines.append(f"          {{ q: `{q}`, ex: `{ex}`, a: `{a}` }},")
                    lines.append("        ]},")
                comma = "," if ui < len(units) - 1 else ""
                lines.append(f"      ]{comma}")
            comma = "," if si < len(subjects) - 1 else ""
            lines.append(f"    ]{comma}")
        comma = "," if gi < len(grades) - 1 else ""
        lines.append(f"  }}{comma}")
    lines.append("};")
    return "\n".join(lines)

js_practice = serialize_p(P)

# Read curriculum.html
with open("/sessions/admiring-stoic-pascal/mnt/outputs/curriculum.html", "r", encoding="utf-8") as f:
    html = f.read()

# Find and replace the PRACTICE block using brace counting
start_marker = "const PRACTICE = {"
start_idx = html.find(start_marker)
if start_idx == -1:
    print("ERROR: Could not find 'const PRACTICE = {' in HTML")
    exit(1)

# Count braces to find the end
depth = 0
i = start_idx
found_start = False
end_idx = -1
for i in range(start_idx, len(html)):
    if html[i] == '{':
        depth += 1
        found_start = True
    elif html[i] == '}':
        depth -= 1
        if found_start and depth == 0:
            end_idx = i + 1
            # consume trailing semicolon if present
            if end_idx < len(html) and html[end_idx] == ';':
                end_idx += 1
            break

if end_idx == -1:
    print("ERROR: Could not find end of PRACTICE block")
    exit(1)

new_html = html[:start_idx] + js_practice + html[end_idx:]

with open("/sessions/admiring-stoic-pascal/mnt/outputs/curriculum.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print(f"Injection complete. New file size: {len(new_html):,} bytes")
print("Done!")
