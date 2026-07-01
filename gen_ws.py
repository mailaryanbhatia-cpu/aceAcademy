#!/usr/bin/env python3
"""Complete worksheet generator aligned 1:1 with curriculum.html"""
import json, re

# ── PROBLEMS: topic_key → list of problem dicts (2 easy, 2 medium, 2 hard) ──
# topic_key = lowercased topic name, spaces→underscores, stripped of punctuation
def k(s):
    return re.sub(r'[^a-z0-9_]','',s.lower().replace(' ','_').replace('/','_').replace('&','and').replace("'",'').replace(',',''))

P = {}

# ════ GRADE 6 MATH ════
P[k('Understanding ratios')] = [
  {'q':'Write the ratio of 3 cats to 7 dogs.','ex':'Use a colon or fraction.','a':'3:7','diff':'easy'},
  {'q':'A bag has 4 red and 6 blue marbles. What is the ratio of red to total?','ex':'Total = red + blue.','a':'4:10 or 2:5','diff':'easy'},
  {'q':'Is 2:3 equivalent to 4:6?','ex':'Cross-multiply or simplify.','a':'Yes — both simplify to 2:3.','diff':'medium'},
  {'q':'A recipe uses 2 cups flour for every 3 cups sugar. If you use 8 cups flour, how many cups sugar?','ex':'Set up a proportion.','a':'12 cups sugar','diff':'medium'},
  {'q':'Write three equivalent ratios to 5:2.','ex':'Multiply both parts by the same number.','a':'10:4, 15:6, 20:8','diff':'hard'},
  {'q':'In a class of 30 students, 18 are girls. Write the ratio of boys to girls in simplest form.','ex':'Find boys first.','a':'12:18 = 2:3','diff':'hard'},
]
P[k('Unit rates')] = [
  {'q':'A car travels 120 miles in 2 hours. What is the speed in miles per hour?','ex':'Divide miles by hours.','a':'60 mph','diff':'easy'},
  {'q':'You earn $45 for 9 hours of work. What is your hourly rate?','ex':'Divide total by hours.','a':'$5 per hour','diff':'easy'},
  {'q':'Store A sells 3 cans for $2.10. Store B sells 5 cans for $3.75. Which is cheaper per can?','ex':'Find each unit price.','a':'Store A: $0.70/can; Store B: $0.75/can → Store A is cheaper.','diff':'medium'},
  {'q':'A runner completes a 5-km race in 25 minutes. What is the unit rate in km per minute?','ex':'Divide distance by time.','a':'0.2 km per minute','diff':'medium'},
  {'q':'A factory makes 840 parts in 7 hours. How many parts does it make in one minute?','ex':'First find parts per hour, then per minute.','a':'2 parts per minute','diff':'hard'},
  {'q':'A faucet drips 15 mL every 5 minutes. How many liters drip in one day?','ex':'Find rate per minute, then scale to 1440 minutes.','a':'4.32 liters','diff':'hard'},
]
P[k('Ratio tables')] = [
  {'q':'Complete the ratio table: Miles 3, 6, ?, 12 | Hours 1, 2, 3, ?','ex':'The ratio is 3:1.','a':'Miles: 9; Hours: 4','diff':'easy'},
  {'q':'A ratio table shows 2 apples per 5 bananas. Fill in: 4 apples → ? bananas.','ex':'Multiply both by 2.','a':'10 bananas','diff':'easy'},
  {'q':'Fill in the table: Boys 3, 6, 9 | Girls 4, 8, ?','ex':'Find the pattern.','a':'12 girls','diff':'medium'},
  {'q':'A recipe uses 1 cup sugar for 4 cups flour. Complete: Sugar 2, 3 | Flour ?, ?','ex':'Multiply each sugar amount by 4.','a':'Flour: 8, 12','diff':'medium'},
  {'q':'The ratio of red to blue tiles is 5:3. If there are 40 red tiles, how many blue?','ex':'Set up 5:3 = 40:x.','a':'24 blue tiles','diff':'hard'},
  {'q':'A car uses 2 gallons of gas per 50 miles. Make a ratio table for 50, 100, 150, 200 miles and find total gallons.','ex':'Rate = 0.04 gal/mile.','a':'2, 4, 6, 8 gallons','diff':'hard'},
]
P[k('Proportional relationships')] = [
  {'q':'Is the table proportional? x: 1,2,3 | y: 4,8,12','ex':'Check if y/x is constant.','a':'Yes — y = 4x for each pair.','diff':'easy'},
  {'q':'y = 3x. What is y when x = 7?','ex':'Substitute x = 7.','a':'21','diff':'easy'},
  {'q':'A graph shows a straight line through the origin. Does it show a proportional relationship?','ex':'A proportional relationship passes through (0,0).','a':'Yes','diff':'medium'},
  {'q':'Write an equation for a proportional relationship where y = 15 when x = 3.','ex':'Find the constant of proportionality k = y/x.','a':'y = 5x','diff':'medium'},
  {'q':'Is the table proportional? x: 2,4,6 | y: 5,9,13','ex':'Check y/x for each.','a':'No — 5/2 ≠ 9/4.','diff':'hard'},
  {'q':'A proportional relationship has k = 2.5. Graph at least 3 points and describe the line.','ex':'Use x = 0,2,4.','a':'Points (0,0), (2,5), (4,10); straight line through origin with slope 2.5.','diff':'hard'},
]
P[k('Percent problems')] = [
  {'q':'What is 50% of 80?','ex':'50% = 1/2.','a':'40','diff':'easy'},
  {'q':'What is 10% of 250?','ex':'Move the decimal one place left.','a':'25','diff':'easy'},
  {'q':'A shirt costs $40 and is 25% off. What is the sale price?','ex':'Find 25% of $40, then subtract.','a':'$30','diff':'medium'},
  {'q':'18 out of 24 students passed. What percent passed?','ex':'Divide 18 by 24, then multiply by 100.','a':'75%','diff':'medium'},
  {'q':'A price increased from $50 to $65. What is the percent increase?','ex':'(New−Old)/Old × 100.','a':'30%','diff':'hard'},
  {'q':'After a 20% discount, a jacket costs $64. What was the original price?','ex':'$64 = 80% of original → divide by 0.80.','a':'$80','diff':'hard'},
]
# Number System
P[k('Division of fractions')] = [
  {'q':'What is 1/2 ÷ 1/4?','ex':'Keep-Change-Flip: 1/2 × 4/1.','a':'2','diff':'easy'},
  {'q':'Divide 3/4 ÷ 3.','ex':'Write 3 as 3/1 then KCF.','a':'1/4','diff':'easy'},
  {'q':'A ribbon 3/4 m long is cut into pieces of 1/8 m. How many pieces?','ex':'Divide 3/4 by 1/8.','a':'6 pieces','diff':'medium'},
  {'q':'Calculate 5/6 ÷ 2/3.','ex':'KCF: 5/6 × 3/2.','a':'5/4 or 1 and 1/4','diff':'medium'},
  {'q':'You have 2 1/2 cups of flour and each recipe needs 3/4 cup. How many recipes can you make?','ex':'Convert 2 1/2 to 5/2, then divide by 3/4.','a':'3 recipes (with 1/4 cup left over)','diff':'hard'},
  {'q':'Explain why dividing by 1/2 is the same as multiplying by 2. Give an example.','ex':'Think: how many halves fit in a whole?','a':'Dividing by 1/2 flips it to × 2/1 = × 2. Example: 6 ÷ 1/2 = 12 because 12 halves fit in 6 wholes.','diff':'hard'},
]
P[k('Multi-digit arithmetic')] = [
  {'q':'Calculate 4,523 + 1,879.','ex':'Add column by column, carrying.','a':'6,402','diff':'easy'},
  {'q':'Find 8,000 − 3,456.','ex':'Borrow across zeros.','a':'4,544','diff':'easy'},
  {'q':'Multiply 47 × 63.','ex':'Use the standard algorithm or area model.','a':'2,961','diff':'medium'},
  {'q':'Divide 2,496 ÷ 8.','ex':'Long division step by step.','a':'312','diff':'medium'},
  {'q':'A school orders 24 boxes of pencils. Each box has 144 pencils. How many pencils total?','ex':'Multiply 24 × 144.','a':'3,456 pencils','diff':'hard'},
  {'q':'A warehouse has 9,072 items. They are packed into crates of 36. How many crates are needed?','ex':'Divide 9,072 ÷ 36.','a':'252 crates','diff':'hard'},
]
P[k('Rational numbers on a number line')] = [
  {'q':'Plot −3 and 2 on a number line. Which is greater?','ex':'Numbers to the right are greater.','a':'2 is greater than −3.','diff':'easy'},
  {'q':'What rational number is exactly halfway between −1 and 1?','ex':'Find the midpoint.','a':'0','diff':'easy'},
  {'q':'Order these from least to greatest: −2, 1/2, −1/4, 0.','ex':'Place each on a number line.','a':'−2, −1/4, 0, 1/2','diff':'medium'},
  {'q':'What is the distance between −5 and 3 on a number line?','ex':'Subtract the smaller from the larger (or count).','a':'8 units','diff':'medium'},
  {'q':'A number is 4.5 units to the left of −1 on a number line. What is the number?','ex':'−1 − 4.5 = ?','a':'−5.5','diff':'hard'},
  {'q':'List all integers between −3.7 and 2.1.','ex':'List whole numbers only in that range.','a':'−3, −2, −1, 0, 1, 2','diff':'hard'},
]
P[k('Absolute value')] = [
  {'q':'What is |−7|?','ex':'Absolute value is the distance from 0.','a':'7','diff':'easy'},
  {'q':'What is |5|?','ex':'5 is already positive.','a':'5','diff':'easy'},
  {'q':'Solve: |x| = 9.','ex':'Two values are 9 from zero.','a':'x = 9 or x = −9','diff':'medium'},
  {'q':'Which is greater: |−8| or |6|?','ex':'Find the absolute value of each.','a':'|−8| = 8 is greater than |6| = 6.','diff':'medium'},
  {'q':'A submarine is at −340 m. A fish is at −120 m. How much closer to the surface is the fish?','ex':'Compare absolute values.','a':'220 m closer to the surface','diff':'hard'},
  {'q':'List all integers n where |n| < 4.','ex':'Include negatives and zero.','a':'−3, −2, −1, 0, 1, 2, 3','diff':'hard'},
]
P[k('Ordering integers')] = [
  {'q':'Order from least to greatest: 5, −3, 0, −7, 2.','ex':'Most negative is least.','a':'−7, −3, 0, 2, 5','diff':'easy'},
  {'q':'Which is greater: −10 or −3?','ex':'On a number line, right is greater.','a':'−3','diff':'easy'},
  {'q':'Place these temperatures in order from coldest to warmest: −12°, 4°, −1°, 0°, 8°.','ex':'Coldest = most negative.','a':'−12°, −1°, 0°, 4°, 8°','diff':'medium'},
  {'q':'Insert <, >, or = between −15 and −9.','ex':'Farther left on number line is smaller.','a':'−15 < −9','diff':'medium'},
  {'q':'A game shows scores: Player A −45, Player B −30, Player C −60. Rank from highest to lowest.','ex':'Least negative = highest score here.','a':'B (−30), A (−45), C (−60)','diff':'hard'},
  {'q':'You have these rational numbers: −3/2, −0.5, −5/4, −2. Order least to greatest.','ex':'Convert to decimals first.','a':'−2, −3/2 (−1.5), −5/4 (−1.25), −0.5','diff':'hard'},
]
# Expressions & Equations
P[k('Writing and evaluating expressions')] = [
  {'q':'Write an expression for "5 more than a number n."','ex':'More than = add.','a':'n + 5','diff':'easy'},
  {'q':'Evaluate 3x when x = 4.','ex':'Substitute 4 for x.','a':'12','diff':'easy'},
  {'q':'Write an expression for "a number divided by 6, then multiplied by 2."','ex':'Order of operations matters.','a':'(n ÷ 6) × 2','diff':'medium'},
  {'q':'Evaluate 2a + 3b when a = 5 and b = 4.','ex':'Substitute each variable.','a':'22','diff':'medium'},
  {'q':'Write and evaluate: "The product of 7 and a number, decreased by 4" when the number is 3.','ex':'Product = multiply.','a':'7 × 3 − 4 = 17','diff':'hard'},
  {'q':'Is 2(x + 3) the same as 2x + 6? Evaluate both when x = 5.','ex':'Use the distributive property.','a':'Yes. Both equal 16 when x = 5.','diff':'hard'},
]
P[k('Properties of operations')] = [
  {'q':'Name the property: 5 + 0 = 5.','ex':'What does adding zero do?','a':'Identity property of addition','diff':'easy'},
  {'q':'Name the property: 3 × 4 = 4 × 3.','ex':'Order does not matter.','a':'Commutative property of multiplication','diff':'easy'},
  {'q':'Rewrite using the distributive property: 4(x + 6).','ex':'Multiply 4 by each term.','a':'4x + 24','diff':'medium'},
  {'q':'Name the property: (2 + 3) + 7 = 2 + (3 + 7).','ex':'Grouping changes, result does not.','a':'Associative property of addition','diff':'medium'},
  {'q':'Use properties to simplify: 25 × 4 × 3 without a calculator.','ex':'Rearrange using commutative and associative.','a':'25 × 4 = 100; 100 × 3 = 300','diff':'hard'},
  {'q':'Explain how the distributive property justifies 6 × 53 = 6×50 + 6×3.','ex':'Break 53 into 50 + 3.','a':'6 × (50 + 3) = 6×50 + 6×3 = 300 + 18 = 318 — distributing multiplication over addition.','diff':'hard'},
]
P[k('Solving one-step equations')] = [
  {'q':'Solve: x + 7 = 12.','ex':'Subtract 7 from both sides.','a':'x = 5','diff':'easy'},
  {'q':'Solve: n − 4 = 9.','ex':'Add 4 to both sides.','a':'n = 13','diff':'easy'},
  {'q':'Solve: 3m = 18.','ex':'Divide both sides by 3.','a':'m = 6','diff':'medium'},
  {'q':'Solve: y/5 = 7.','ex':'Multiply both sides by 5.','a':'y = 35','diff':'medium'},
  {'q':'A book has p pages. After reading 45 pages you have 112 left. Write and solve an equation.','ex':'p − 45 = 112.','a':'p = 157 pages','diff':'hard'},
  {'q':'Solve and check: 2.5k = 17.5.','ex':'Divide both sides by 2.5, then verify.','a':'k = 7. Check: 2.5 × 7 = 17.5 ✓','diff':'hard'},
]
P[k('Inequalities')] = [
  {'q':'Is x = 5 a solution to x > 3?','ex':'Is 5 greater than 3?','a':'Yes','diff':'easy'},
  {'q':'Graph x ≥ 2 on a number line.','ex':'Closed circle at 2, arrow right.','a':'Closed dot at 2, shaded to the right.','diff':'easy'},
  {'q':'Solve: x + 4 < 10.','ex':'Subtract 4 from both sides.','a':'x < 6','diff':'medium'},
  {'q':'Solve: 3n ≥ 15.','ex':'Divide both sides by 3.','a':'n ≥ 5','diff':'medium'},
  {'q':'You need at least $50 to buy a game. You have $32. Write and solve an inequality for how much more you need.','ex':'32 + m ≥ 50.','a':'m ≥ 18; you need at least $18 more.','diff':'hard'},
  {'q':'Solve −2x < 8 and explain why the inequality sign flips when dividing by a negative.','ex':'Dividing by a negative reverses the order.','a':'x > −4. The inequality flips because dividing both sides by −2 reverses the comparison.','diff':'hard'},
]
# Geometry G6
P[k('Area of polygons')] = [
  {'q':'Find the area of a rectangle 8 cm wide and 5 cm tall.','ex':'A = length × width.','a':'40 cm²','diff':'easy'},
  {'q':'What is the area of a square with side 6 m?','ex':'A = s².','a':'36 m²','diff':'easy'},
  {'q':'Find the area of a triangle with base 10 ft and height 6 ft.','ex':'A = ½ × b × h.','a':'30 ft²','diff':'medium'},
  {'q':'A parallelogram has base 9 in and height 4 in. Find its area.','ex':'A = base × height.','a':'36 in²','diff':'medium'},
  {'q':'A composite shape is a rectangle (6×4) with a triangle on top (base 6, height 3). Find total area.','ex':'Add the two areas.','a':'24 + 9 = 33 units²','diff':'hard'},
  {'q':'A trapezoidal patio has parallel sides of 8 m and 12 m, and a height of 5 m. Find the area.','ex':'A = ½(b₁ + b₂)h.','a':'50 m²','diff':'hard'},
]
P[k('Surface area')] = [
  {'q':'How many faces does a rectangular prism have?','ex':'Count the flat surfaces.','a':'6 faces','diff':'easy'},
  {'q':'Find the surface area of a cube with side 3 cm.','ex':'SA = 6 × s².','a':'54 cm²','diff':'easy'},
  {'q':'Find the surface area of a rectangular box: length 5, width 4, height 3 (all in cm).','ex':'SA = 2(lw + lh + wh).','a':'94 cm²','diff':'medium'},
  {'q':'A can of soup is a cylinder (r = 4 cm, h = 10 cm). Estimate the surface area using π ≈ 3.14.','ex':'SA = 2πr² + 2πrh.','a':'≈ 351.68 cm²','diff':'medium'},
  {'q':'A triangular prism has rectangular faces 5×8, 5×6, 5×10 and two triangles (base 6, height 8). Find SA.','ex':'Add all five faces.','a':'(5×8) + (5×6) + (5×10) + 2×(½×6×8) = 40+30+50+48 = 168 units²','diff':'hard'},
  {'q':'You are wrapping a gift box: 12 in × 9 in × 4 in. How much paper do you need (SA)?','ex':'SA = 2(lw + lh + wh).','a':'2(108 + 48 + 36) = 384 in²','diff':'hard'},
]
P[k('Volume of rectangular prisms')] = [
  {'q':'Find the volume of a box: 4 cm × 3 cm × 2 cm.','ex':'V = l × w × h.','a':'24 cm³','diff':'easy'},
  {'q':'A fish tank is 10 in long, 8 in wide, 6 in tall. What is its volume?','ex':'V = lwh.','a':'480 in³','diff':'easy'},
  {'q':'A cube has volume 125 cm³. What is the length of each side?','ex':'s³ = 125.','a':'5 cm','diff':'medium'},
  {'q':'A box has volume 240 cm³, length 8 cm, and width 6 cm. Find the height.','ex':'240 = 8 × 6 × h.','a':'h = 5 cm','diff':'medium'},
  {'q':'How many 2 cm × 2 cm × 2 cm cubes fit in a 10 cm × 8 cm × 6 cm box?','ex':'Divide each dimension by 2, then multiply.','a':'5 × 4 × 3 = 60 cubes','diff':'hard'},
  {'q':'A swimming pool is 25 m long, 10 m wide, and 2 m deep. How many liters of water does it hold? (1 m³ = 1000 L)','ex':'V = 25 × 10 × 2 = 500 m³.','a':'500,000 liters','diff':'hard'},
]
P[k('Coordinate plane')] = [
  {'q':'Name the coordinates of a point 3 units right and 4 units up from the origin.','ex':'x is right, y is up.','a':'(3, 4)','diff':'easy'},
  {'q':'In which quadrant is the point (−2, 5)?','ex':'Negative x, positive y.','a':'Quadrant II','diff':'easy'},
  {'q':'Plot and label (−3, −4). Describe its location.','ex':'x = −3 (left), y = −4 (down).','a':'3 units left and 4 units down from the origin; Quadrant III.','diff':'medium'},
  {'q':'Find the distance between (1, 4) and (1, −2) on a coordinate plane.','ex':'Same x → count y units.','a':'6 units','diff':'medium'},
  {'q':'A rectangle has vertices at (2,1), (2,5), (7,1), and (7,5). Find its perimeter.','ex':'Find width and height from coordinates.','a':'Width = 5, Height = 4; P = 2(5+4) = 18 units','diff':'hard'},
  {'q':'Reflect the point (3, −2) over the y-axis and then over the x-axis. What are the final coordinates?','ex':'Over y-axis: negate x. Over x-axis: negate y.','a':'Over y-axis: (−3, −2). Over x-axis: (−3, 2).','diff':'hard'},
]
# Statistics & Probability G6
P[k('Statistical questions')] = [
  {'q':'Is "How tall are you?" a statistical question?','ex':'A statistical question expects varied answers.','a':'No — it has one specific answer.','diff':'easy'},
  {'q':'Give an example of a statistical question about students in your school.','ex':'Must anticipate variability.','a':'Example: "How many hours per week do students at our school exercise?"','diff':'easy'},
  {'q':'Why is "What is 5 × 6?" not a statistical question?','ex':'Think about variability.','a':'It has exactly one correct answer (30) — no variability expected.','diff':'medium'},
  {'q':'Survey question: "How many pets do students in 6th grade own?" Is this statistical? Why?','ex':'Will answers vary?','a':'Yes — different students have different numbers of pets, so answers will vary.','diff':'medium'},
  {'q':'Rewrite "What grade do I get on tests?" as a better statistical question.','ex':'Broaden to a group.','a':'Example: "What test grades do students in 6th grade typically receive?"','diff':'hard'},
  {'q':'You want to study sleep habits in your class. Write a good statistical question and identify the variable.','ex':'Variable = what you measure.','a':'Q: "How many hours of sleep do 6th graders get on school nights?" Variable: hours of sleep.','diff':'hard'},
]
P[k('Dot plots and histograms')] = [
  {'q':'What does each dot on a dot plot represent?','ex':'Think about data points.','a':'Each dot represents one data value (one observation).','diff':'easy'},
  {'q':'A histogram shows bars. What does the height of each bar tell you?','ex':'y-axis = frequency.','a':'The frequency (count) of data values in that interval.','diff':'easy'},
  {'q':'Dot plot data: 1,1,2,3,3,3,4,5. What is the most common value?','ex':'Look for the most dots stacked.','a':'3 (appears 3 times)','diff':'medium'},
  {'q':'Why would you use a histogram instead of a dot plot for 500 data points?','ex':'Think about legibility.','a':'A histogram groups data into intervals, making large data sets easier to read.','diff':'medium'},
  {'q':'A histogram has intervals 0–10, 10–20, 20–30 with frequencies 5, 12, 8. Describe the distribution shape.','ex':'Where is most of the data?','a':'Roughly bell-shaped (peaks in the middle interval 10–20).','diff':'hard'},
  {'q':'From a dot plot, how do you find the median? Give an example with: 2, 3, 3, 4, 5, 5, 6.','ex':'Middle value when ordered.','a':'7 values → middle is the 4th: median = 4.','diff':'hard'},
]
P[k('Box plots')] = [
  {'q':'What are the five values in a five-number summary?','ex':'Think min, max, and three others.','a':'Minimum, Q1, Median (Q2), Q3, Maximum','diff':'easy'},
  {'q':'In a box plot, what does the box itself represent?','ex':'Middle 50% of data.','a':'The interquartile range (IQR) — the middle 50% of the data.','diff':'easy'},
  {'q':'Data: 12, 15, 18, 20, 25, 30, 35. Find Q1, median, and Q3.','ex':'Median first, then split.','a':'Median = 20; Q1 = 15; Q3 = 30','diff':'medium'},
  {'q':'A box plot has Q1 = 40 and Q3 = 70. What is the IQR?','ex':'IQR = Q3 − Q1.','a':'30','diff':'medium'},
  {'q':'Two box plots show test scores: Class A median = 75, Class B median = 85. What can you conclude?','ex':'Compare centers and spreads.','a':'Class B typically scored higher. The median tells us the middle value; without more info, we cannot compare variability.','diff':'hard'},
  {'q':'A box plot has whiskers from 10 to 90, box from 30 to 70, and median at 55. Find the IQR and range.','ex':'Range = max − min; IQR = Q3 − Q1.','a':'IQR = 70 − 30 = 40; Range = 90 − 10 = 80','diff':'hard'},
]
P[k('Mean, median, mode, range')] = [
  {'q':'Find the mean of: 4, 7, 9, 6.','ex':'Add all, divide by count.','a':'(4+7+9+6)/4 = 26/4 = 6.5','diff':'easy'},
  {'q':'Find the median of: 3, 5, 8, 10, 12.','ex':'Middle value when ordered.','a':'8','diff':'easy'},
  {'q':'Data: 2, 4, 4, 5, 7, 8, 4. Find the mode.','ex':'Most frequent value.','a':'4','diff':'medium'},
  {'q':'Find the range of: 15, 22, 9, 31, 18.','ex':'Range = max − min.','a':'31 − 9 = 22','diff':'medium'},
  {'q':'Test scores: 70, 85, 90, 95, 100. A new score of 40 is added. How does the mean change?','ex':'Recalculate with the new score.','a':'Old mean = 88; new mean = (70+85+90+95+100+40)/6 = 480/6 = 80. It decreases by 8.','diff':'hard'},
  {'q':'When would the median be a better measure of center than the mean? Give an example.','ex':'Think about outliers.','a':'When data has outliers. Example: salaries $30k, $35k, $40k, $500k — mean = $151.25k (misleading); median = $37.5k (better).','diff':'hard'},
]
P[k('Data distributions')] = [
  {'q':'What does it mean for data to be symmetric?','ex':'Think mirror image.','a':'The left side mirrors the right side — most data is in the middle.','diff':'easy'},
  {'q':'A histogram is skewed right. Where is most of the data?','ex':'The tail points right (high values).','a':'Most data is on the left (low values); there are a few very high values pulling the tail right.','diff':'easy'},
  {'q':'Compare a distribution with mean 50 and range 10 to one with mean 50 and range 40.','ex':'Same center, different spread.','a':'Same center; the second is much more spread out (variable).','diff':'medium'},
  {'q':'What measures help you describe the center and spread of a distribution?','ex':'Name two for each.','a':'Center: mean, median. Spread: range, interquartile range (IQR).','diff':'medium'},
  {'q':'A data set has most values near 80 with a few values near 20. Describe the distribution shape.','ex':'Where is the tail?','a':'Left (negatively) skewed — tail extends toward lower values.','diff':'hard'},
  {'q':'Two classes both have median 75. Class A has IQR 10; Class B has IQR 30. Which class is more consistent?','ex':'Smaller spread = more consistent.','a':'Class A — its smaller IQR means scores are clustered closer to the median.','diff':'hard'},
]

print("Grade 6 Math problems loaded:", len([k for k in P if P[k]]))
