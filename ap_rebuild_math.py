"""AP Math: 4 units matching curriculum (Precalculus, Calc AB, Calc BC, Statistics)"""

AP_MATH = [
  # Unit 1 — AP Precalculus
  [
    {"title":"Polynomial and Rational Functions","problems":[
      {"q":"Find all zeros of f(x)=x³−6x²+11x−6.","ex":"Factor or use rational root theorem.","a":"Rational roots to test: ±1,±2,±3,±6. f(1)=0 ✓. Factor: (x−1)(x²−5x+6)=(x−1)(x−2)(x−3). Zeros: x=1,2,3.","diff":"medium"},
      {"q":"Identify vertical and horizontal asymptotes of f(x)=(2x²−1)/(x²−4).","ex":"Factor denominators; compare degrees for horizontal.","a":"VA: x²−4=0 → x=±2. HA: degrees equal → HA is ratio of leading coefficients = 2/1 = y=2.","diff":"medium"},
      {"q":"A rational function has zeros at x=1,3, a VA at x=−2, and HA at y=0. Write a possible formula.","ex":"HA=0 means numerator degree < denominator degree.","a":"f(x)=(x−1)(x−3)/((x+2)(x+something)) works; simplest: f(x)=(x−1)(x−3)/((x+2)·x) — numerator degree 2, denominator degree 2 would give HA≠0. For HA=0 need deg(num)<deg(den): f(x)=(x−1)(x−3)/(x+2)². Check: degree 2 numerator, degree 2 denominator — this gives HA=1/1=1, not 0. Adjust: f(x)=(x−1)(x−3)/(x+2)³. Now deg(num)=2 < deg(den)=3, so HA=y=0. ✓","diff":"hard"}
    ]},
    {"title":"Exponential and Logarithmic Functions","problems":[
      {"q":"Solve: 3^(2x−1)=27.","ex":"Express 27 as a power of 3.","a":"27=3³. So 2x−1=3 → 2x=4 → x=2.","diff":"easy"},
      {"q":"Evaluate log₂(64)−log₂(4).","ex":"Use quotient property of logarithms.","a":"log₂(64/4)=log₂(16)=4. (Since 2⁴=16.)","diff":"easy"},
      {"q":"The half-life of a substance is 12 years. Write an exponential decay model and find the percentage remaining after 30 years.","ex":"Use A(t)=A₀(1/2)^(t/half-life).","a":"A(t)=A₀(0.5)^(t/12). At t=30: A=A₀·(0.5)^(30/12)=A₀·(0.5)^2.5=A₀·0.177. About 17.7% remains.","diff":"medium"}
    ]},
    {"title":"Trigonometric Functions and Unit Circle","problems":[
      {"q":"Find sin(5π/6), cos(5π/6), and tan(5π/6).","ex":"5π/6 is in Q2; reference angle = π/6.","a":"Reference angle π/6: sin(π/6)=1/2, cos(π/6)=√3/2. In Q2: sin>0, cos<0. So sin(5π/6)=1/2, cos(5π/6)=−√3/2, tan(5π/6)=−1/√3=−√3/3.","diff":"medium"},
      {"q":"Convert 225° to radians and find its exact sine and cosine.","ex":"Multiply by π/180 for radians.","a":"225°×(π/180)=5π/4. Reference angle: π/4 (Q3, both negative). sin(5π/4)=−√2/2, cos(5π/4)=−√2/2.","diff":"medium"},
      {"q":"If sin θ=3/5 and θ is in Q2, find cos θ and tan θ.","ex":"Use Pythagorean identity; note signs in Q2.","a":"sin²θ+cos²θ=1 → cos²θ=1−9/25=16/25 → cosθ=±4/5. In Q2, cosθ<0 → cosθ=−4/5. tanθ=sinθ/cosθ=(3/5)/(−4/5)=−3/4.","diff":"medium"}
    ]},
    {"title":"Trigonometric Equations and Identities","problems":[
      {"q":"Verify the identity: sin²x+cos²x·tanx·cotx = 1.","ex":"cotx=cosx/sinx; tanx=sinx/cosx.","a":"tanx·cotx=(sinx/cosx)·(cosx/sinx)=1. So sin²x+cos²x·1=sin²x+cos²x=1. ✓","diff":"easy"},
      {"q":"Solve 2sin²x−sinx−1=0 on [0,2π).","ex":"Treat sinx as a variable; factor the quadratic.","a":"Let u=sinx: 2u²−u−1=0 → (2u+1)(u−1)=0 → u=−1/2 or u=1. sinx=−1/2: x=7π/6,11π/6. sinx=1: x=π/2. Solutions: {π/2, 7π/6, 11π/6}.","diff":"medium"},
      {"q":"Use the double-angle formula to find sin(2θ) if sinθ=5/13 and θ is in Q1.","ex":"sin(2θ)=2sinθcosθ","a":"cosθ=√(1−25/169)=12/13 (positive in Q1). sin(2θ)=2·(5/13)·(12/13)=120/169.","diff":"medium"}
    ]},
    {"title":"Conic Sections","problems":[
      {"q":"Write the equation of an ellipse centered at the origin with vertices at (±5,0) and co-vertices at (0,±3).","ex":"Standard form: x²/a²+y²/b²=1 with a>b.","a":"a=5, b=3. Equation: x²/25+y²/9=1.","diff":"easy"},
      {"q":"Find the vertex, focus, and directrix of the parabola y²=12x.","ex":"Compare to y²=4px.","a":"y²=4px=12x → p=3. Vertex: (0,0). Focus: (3,0). Directrix: x=−3.","diff":"medium"},
      {"q":"Write the equation of a hyperbola with vertices at (±4,0) and foci at (±5,0).","ex":"c²=a²+b²; standard form x²/a²−y²/b²=1.","a":"a=4, c=5 → b²=c²−a²=25−16=9. Equation: x²/16−y²/9=1.","diff":"medium"}
    ]},
    {"title":"Parametric Equations and Polar Coordinates","problems":[
      {"q":"Eliminate the parameter: x=3cosθ, y=3sinθ.","ex":"Use sin²θ+cos²θ=1.","a":"cosθ=x/3, sinθ=y/3. (x/3)²+(y/3)²=1 → x²+y²=9. A circle of radius 3 centered at origin.","diff":"easy"},
      {"q":"Convert the polar point (4, π/3) to rectangular coordinates.","ex":"x=rcosθ, y=rsinθ","a":"x=4cos(π/3)=4·(1/2)=2. y=4sin(π/3)=4·(√3/2)=2√3. Rectangular: (2, 2√3).","diff":"easy"},
      {"q":"Convert the rectangular equation x²+y²=6x to polar form.","ex":"x=rcosθ, y=rsinθ, x²+y²=r².","a":"r²=6rcosθ → r=6cosθ.","diff":"medium"}
    ]},
    {"title":"Limits and Continuity (Introduction)","problems":[
      {"q":"Estimate lim(x→2) (x²−4)/(x−2) numerically, then find it algebraically.","ex":"Factor the numerator.","a":"Factor: (x²−4)/(x−2)=(x+2)(x−2)/(x−2)=x+2 (for x≠2). So the limit = 2+2=4.","diff":"easy"},
      {"q":"Find lim(x→0) sinx/x.","ex":"This is a fundamental trigonometric limit.","a":"lim(x→0) sinx/x = 1. This is a standard limit proved using squeeze theorem; it appears throughout calculus.","diff":"easy"},
      {"q":"Is f(x)={x²−4)/(x−2) if x≠2; 3 if x=2} continuous at x=2? Explain.","ex":"Check all three conditions for continuity.","a":"(1) f(2)=3 ✓ (defined). (2) lim(x→2)(x²−4)/(x−2)=4 ✓ (exists). (3) lim≠f(2): 4≠3. NOT continuous at x=2 — the function has a removable discontinuity there (would be continuous if f(2)=4).","diff":"medium"}
    ]}
  ],
  # Unit 2 — AP Calculus AB
  [
    {"title":"Limits and Continuity","problems":[
      {"q":"Evaluate lim(x→3) (x²−9)/(x−3).","ex":"Factor and cancel.","a":"(x²−9)/(x−3)=(x+3)(x−3)/(x−3)=x+3 → as x→3, limit=6.","diff":"easy"},
      {"q":"Find lim(x→∞) (5x³−2x)/(3x³+x²−1).","ex":"Divide every term by the highest power of x.","a":"Divide by x³: (5−2/x²)/(3+1/x−1/x³) → as x→∞, limit=5/3.","diff":"medium"},
      {"q":"Where is f(x)=(x+2)/(x²−x−6) discontinuous, and what type of discontinuity?","ex":"Factor denominator.","a":"x²−x−6=(x−3)(x+2). At x=−2: numerator and denominator both =0 → removable discontinuity (hole). At x=3: denominator=0, numerator≠0 → infinite discontinuity (vertical asymptote).","diff":"medium"}
    ]},
    {"title":"Derivatives: Definition and Basic Rules","problems":[
      {"q":"Use the limit definition to find f'(x) for f(x)=x².","ex":"f'(x)=lim(h→0)[f(x+h)−f(x)]/h","a":"[(x+h)²−x²]/h=(x²+2xh+h²−x²)/h=(2xh+h²)/h=2x+h → as h→0, f'(x)=2x.","diff":"easy"},
      {"q":"Differentiate f(x)=5x⁴−3x²+7x−2.","ex":"Apply power rule to each term.","a":"f'(x)=20x³−6x+7.","diff":"easy"},
      {"q":"Find the equation of the tangent line to y=x³−2x at x=1.","ex":"Find slope (y'(1)) and point (1, y(1)).","a":"y(1)=1−2=−1. y'=3x²−2 → y'(1)=1. Tangent: y−(−1)=1(x−1) → y=x−2.","diff":"medium"}
    ]},
    {"title":"Derivatives: Composite, Implicit, and Inverse","problems":[
      {"q":"Differentiate f(x)=sin(3x²).","ex":"Use chain rule: d/dx[sin(u)]=cos(u)·u'","a":"f'(x)=cos(3x²)·6x=6xcos(3x²).","diff":"medium"},
      {"q":"Find dy/dx by implicit differentiation for x²+y²=25.","ex":"Differentiate both sides with respect to x; treat y as a function of x.","a":"2x+2y(dy/dx)=0 → dy/dx=−x/y.","diff":"medium"},
      {"q":"Find the derivative of f(x)=arctan(x).","ex":"Use the inverse derivative formula.","a":"d/dx[arctan(x)]=1/(1+x²). Derivation: let y=arctan(x), then x=tan(y). Differentiating: 1=sec²(y)·(dy/dx)=( 1+tan²y)(dy/dx)=(1+x²)(dy/dx). So dy/dx=1/(1+x²).","diff":"hard"}
    ]},
    {"title":"Contextual Applications of Differentiation","problems":[
      {"q":"A ladder 10 feet long leans against a wall. The bottom slides away at 2 ft/sec. How fast is the top sliding down when the bottom is 6 feet from the wall?","ex":"Related rates: use x²+y²=100.","a":"x²+y²=100. Differentiate: 2x(dx/dt)+2y(dy/dt)=0. At x=6: y=√(100−36)=8. 2(6)(2)+2(8)(dy/dt)=0 → 24+16(dy/dt)=0 → dy/dt=−3/2 ft/sec. (Top slides down at 1.5 ft/sec.)","diff":"hard"},
      {"q":"A particle's position is s(t)=t³−6t²+9t. Find when it is at rest and when it moves left.","ex":"Velocity = s'(t); at rest when v=0.","a":"v(t)=s'(t)=3t²−12t+9=3(t−1)(t−3). At rest: t=1 and t=3. Moving left (v<0): between t=1 and t=3.","diff":"medium"},
      {"q":"Use linear approximation to estimate √9.04.","ex":"f(x)=√x near x=9; L(x)=f(9)+f'(9)(x−9).","a":"f(9)=3. f'(x)=1/(2√x), f'(9)=1/6. L(9.04)=3+(1/6)(0.04)=3+0.00667≈3.00667.","diff":"medium"}
    ]},
    {"title":"Applying Derivatives to Analyze Functions","problems":[
      {"q":"For f(x)=x³−3x+2, find all critical points and classify each as local max, min, or neither.","ex":"Set f'=0; use second derivative test.","a":"f'(x)=3x²−3=3(x+1)(x−1)=0 → x=±1. f''(x)=6x. f''(−1)=−6<0 → local max at x=−1. f''(1)=6>0 → local min at x=1.","diff":"medium"},
      {"q":"A farmer has 200 meters of fence. Find the dimensions of the rectangle with maximum area.","ex":"Maximize A=lw subject to 2l+2w=200.","a":"w=100−l. A=l(100−l)=100l−l². A'=100−2l=0 → l=50. w=50. Maximum area is a square: 50×50=2500 m².","diff":"medium"},
      {"q":"State and apply the Mean Value Theorem to f(x)=x² on [1,3].","ex":"MVT: there exists c in (a,b) where f'(c)=(f(b)−f(a))/(b−a).","a":"f continuous and differentiable on [1,3]. Average rate = (9−1)/(3−1)=4. f'(c)=2c=4 → c=2. So at x=2, the instantaneous rate equals the average rate of change on [1,3]. ✓","diff":"medium"}
    ]},
    {"title":"Integration and Accumulation of Change","problems":[
      {"q":"Evaluate ∫(3x²−4x+1)dx.","ex":"Apply power rule for integration; add constant C.","a":"x³−2x²+x+C.","diff":"easy"},
      {"q":"Evaluate ∫₀³ (2x)dx using the Fundamental Theorem of Calculus.","ex":"Find antiderivative; evaluate from 0 to 3.","a":"∫2x dx = x². FTC: [x²]₀³ = 9−0 = 9.","diff":"easy"},
      {"q":"Use u-substitution to evaluate ∫ 2x·cos(x²)dx.","ex":"Let u=x².","a":"u=x², du=2x dx. ∫cos(u)du=sin(u)+C=sin(x²)+C.","diff":"medium"}
    ]},
    {"title":"Differential Equations","problems":[
      {"q":"Verify that y=Ce^(3x) is a solution to y'=3y.","ex":"Differentiate y and substitute into the equation.","a":"y'=3Ce^(3x)=3y. ✓ The equation is satisfied for any constant C.","diff":"easy"},
      {"q":"Solve the separable DE: dy/dx=2xy, y(0)=1.","ex":"Separate, integrate both sides.","a":"dy/y=2x dx → ln|y|=x²+C → y=Ae^(x²). Apply y(0)=1: 1=A. Solution: y=e^(x²).","diff":"medium"},
      {"q":"Sketch slope fields: describe the slope field for dy/dx=y.","ex":"The slope at each point depends only on the y-value.","a":"The slope at any point (x,y) equals y. Where y>0: positive slopes increasing with y. Where y<0: negative slopes. Along y=0: horizontal tangents. Integral curves are y=Ce^x — exponential growth/decay depending on sign of C.","diff":"hard"}
    ]},
    {"title":"Applications of Integration","problems":[
      {"q":"Find the area between f(x)=x² and g(x)=x on [0,1].","ex":"Area=∫₀¹|f−g|dx; determine which is on top.","a":"On [0,1]: x>x² (check x=0.5: 0.5>0.25). Area=∫₀¹(x−x²)dx=[x²/2−x³/3]₀¹=1/2−1/3=1/6.","diff":"medium"},
      {"q":"Set up (but don't evaluate) the integral for the area of the region bounded by y=√x, y=0, and x=4.","ex":"Identify the bounds and the function.","a":"Area=∫₀⁴ √x dx. (Alternatively by horizontal slices: ∫₀² (4−y²)dy — both give the same result of 16/3.)","diff":"easy"},
      {"q":"The velocity of a particle is v(t)=t²−2t on [0,4]. Find the total distance traveled.","ex":"Total distance = ∫|v(t)|dt; find where v changes sign.","a":"v(t)=t(t−2)=0 at t=0,2. On [0,2]: v<0 (moving left). On [2,4]: v>0. Total dist=∫₀²|t²−2t|dt+∫₂⁴(t²−2t)dt=∫₀²(2t−t²)dt+∫₂⁴(t²−2t)dt=[t²−t³/3]₀²+[t³/3−t²]₂⁴=(4−8/3)+(64/3−16−8/3+4)=4/3+28/3=32/3.","diff":"hard"}
    ]}
  ],
  # Unit 3 — AP Calculus BC (extends AB)
  [
    {"title":"Advanced Integration Techniques","problems":[
      {"q":"Evaluate ∫ x·e^x dx using integration by parts.","ex":"IBP: ∫u dv = uv − ∫v du; choose u=x, dv=e^x dx.","a":"u=x, dv=e^x dx → du=dx, v=e^x. IBP: xe^x−∫e^x dx=xe^x−e^x+C=e^x(x−1)+C.","diff":"medium"},
      {"q":"Evaluate ∫ 1/(x²−1) dx using partial fractions.","ex":"Factor x²−1=(x+1)(x−1); decompose.","a":"1/((x+1)(x−1))=A/(x+1)+B/(x−1). Multiply by (x+1)(x−1): 1=A(x−1)+B(x+1). x=1: 1=2B → B=1/2. x=−1: 1=−2A → A=−1/2. ∫=(1/2)ln|x−1|−(1/2)ln|x+1|+C=(1/2)ln|(x−1)/(x+1)|+C.","diff":"hard"},
      {"q":"Evaluate the improper integral ∫₁^∞ 1/x² dx.","ex":"Replace ∞ with t, take limit as t→∞.","a":"∫₁^t x⁻² dx=[−1/x]₁^t=−1/t+1. As t→∞: limit=0+1=1. The integral converges to 1.","diff":"medium"}
    ]},
    {"title":"Series: Taylor and Maclaurin Series","problems":[
      {"q":"Write the Maclaurin series for e^x and give the first four terms.","ex":"Maclaurin: f(x)=Σ f^(n)(0)/n! · xⁿ","a":"e^x=1+x+x²/2!+x³/3!+x⁴/4!+… = Σ(n=0 to ∞) xⁿ/n!. Converges for all x.","diff":"easy"},
      {"q":"Use the Maclaurin series for sin(x) to find the series for sin(x)/x.","ex":"sin(x)=x−x³/3!+x⁵/5!−…","a":"sin(x)/x=(x−x³/6+x⁵/120−…)/x=1−x²/6+x⁴/120−… = Σ(n=0 to ∞)(−1)ⁿx^(2n)/(2n+1)!","diff":"medium"},
      {"q":"Determine whether the series Σ(1/n²) converges or diverges and state the test used.","ex":"p-series test: Σ1/nᵖ converges if p>1.","a":"This is a p-series with p=2>1. By the p-series test, it converges. (Its sum is π²/6, Basel problem.)","diff":"medium"}
    ]},
    {"title":"Parametric Equations and Polar Curves","problems":[
      {"q":"Find dy/dx for the parametric curve x=t², y=t³−3t.","ex":"dy/dx=(dy/dt)/(dx/dt)","a":"dx/dt=2t, dy/dt=3t²−3. dy/dx=(3t²−3)/(2t)=3(t²−1)/(2t).","diff":"medium"},
      {"q":"Find the area enclosed by the polar curve r=3cos(θ).","ex":"Area=½∫r² dθ over appropriate interval.","a":"r=3cosθ is a circle. It completes from θ=−π/2 to π/2. A=½∫_{−π/2}^{π/2}(3cosθ)²dθ=½·9∫cos²θ dθ=9π/4. (Alternatively: circle of radius 3/2, so A=π(3/2)²=9π/4 ✓)","diff":"hard"},
      {"q":"A particle moves with x(t)=cos(t), y(t)=sin(t). Find the speed at t=π/4.","ex":"Speed=√((dx/dt)²+(dy/dt)²)","a":"dx/dt=−sin(t), dy/dt=cos(t). Speed=√(sin²t+cos²t)=√1=1. (Constant speed of 1 for uniform circular motion.)","diff":"medium"}
    ]},
    {"title":"Vector-Valued Functions","problems":[
      {"q":"Given r(t)=⟨t², 3t⟩, find the velocity and acceleration vectors at t=2.","ex":"v(t)=r'(t), a(t)=r''(t).","a":"v(t)=⟨2t,3⟩. a(t)=⟨2,0⟩. At t=2: v(2)=⟨4,3⟩, a(2)=⟨2,0⟩.","diff":"easy"},
      {"q":"Find the arc length of r(t)=⟨cos(t),sin(t)⟩ on [0,2π].","ex":"L=∫|r'(t)|dt","a":"r'(t)=⟨−sin(t),cos(t)⟩. |r'(t)|=√(sin²t+cos²t)=1. L=∫₀^{2π}1 dt=2π.","diff":"medium"},
      {"q":"A particle has velocity v(t)=⟨2t,3t²⟩ and initial position r(0)=⟨1,0⟩. Find r(t).","ex":"Integrate v(t), use initial condition.","a":"r(t)=⟨t²+C₁, t³+C₂⟩. r(0)=⟨1,0⟩ → C₁=1, C₂=0. r(t)=⟨t²+1, t³⟩.","diff":"medium"}
    ]},
    {"title":"Euler's Method and Logistic Differential Equations","problems":[
      {"q":"Use Euler's method with step h=0.5 to approximate y(1) for dy/dx=y, y(0)=1.","ex":"y_{n+1}=y_n+h·f(x_n,y_n)","a":"Step 1: y(0.5)=1+0.5·(1)=1.5. Step 2: y(1)=1.5+0.5·(1.5)=1.5+0.75=2.25. (Exact: e¹≈2.718; Euler underestimates for concave-up functions.)","diff":"medium"},
      {"q":"The logistic model is dP/dt=0.2P(1−P/500). Find the equilibrium values.","ex":"Set dP/dt=0.","a":"0.2P(1−P/500)=0 → P=0 or P=500. P=0 is unstable; P=500 (carrying capacity) is stable. Populations below 500 grow; above 500 decline.","diff":"easy"},
      {"q":"Solve the logistic equation dP/dt=kP(1−P/M) and describe the solution's behavior.","ex":"Separate variables; use partial fractions.","a":"Solution: P(t)=M/(1+Ae^{−kt}) where A=(M−P₀)/P₀. Behavior: S-shaped (sigmoidal) growth — exponential-like when P is small, decelerating as P approaches carrying capacity M, with an inflection point at P=M/2.","diff":"hard"}
    ]},
    {"title":"Infinite Sequences and Series Convergence","problems":[
      {"q":"Use the ratio test to determine if Σ n!/nⁿ converges.","ex":"L=lim|a_{n+1}/a_n|; converges if L<1.","a":"a_n=n!/nⁿ. a_{n+1}/a_n=(n+1)!/(n+1)^{n+1} ÷ n!/nⁿ = (n+1)·nⁿ/(n+1)^{n+1}=nⁿ/(n+1)ⁿ=(n/(n+1))ⁿ=(1−1/(n+1))ⁿ→e^{−1}<1. Series converges.","diff":"hard"},
      {"q":"Test ∑(n=1 to ∞)(−1)ⁿ/n for convergence; name the type of convergence.","ex":"Alternating series test and absolute convergence.","a":"Alternating series test: 1/n is decreasing → 0. Series converges (conditionally). Absolute convergence test: Σ1/n diverges (harmonic series). So convergent but NOT absolutely convergent — conditionally convergent.","diff":"medium"},
      {"q":"Find the radius of convergence of the power series Σ(n=0 to ∞) xⁿ/n!.","ex":"Use ratio test with general term a_n=xⁿ/n!","a":"L=lim|a_{n+1}/a_n|=lim|x^{n+1}/(n+1)!·n!/xⁿ|=lim|x/(n+1)|=0 for all x. Since L=0<1 for all x, radius of convergence R=∞ (series converges for all x). This is the series for e^x.","diff":"medium"}
    ]},
    {"title":"BC Exam Strategies","problems":[
      {"q":"What topics appear in BC but not AB? List at least 5.","ex":"Think about what was added in BC.","a":"BC-only topics: (1) Integration by parts, (2) Partial fractions, (3) Improper integrals, (4) Parametric and polar curves (arc length, area), (5) Vector-valued functions, (6) Power/Taylor/Maclaurin series, (7) Convergence tests (ratio, alternating, etc.), (8) Euler's method, (9) Logistic differential equations.","diff":"easy"},
      {"q":"Explain the difference between conditional and absolute convergence.","ex":"Think about what happens when you take absolute values of terms.","a":"Absolutely convergent: Σ|aₙ| converges → Σaₙ converges. Conditionally convergent: Σaₙ converges but Σ|aₙ| diverges. Example: Σ(−1)ⁿ/n converges conditionally; Σ|aₙ|=Σ1/n diverges. Absolute convergence is stronger — rearranging terms doesn't change the sum. With conditional convergence, rearranging can change or destroy convergence (Riemann rearrangement theorem).","diff":"hard"},
      {"q":"When should you use integration by parts vs. u-substitution?","ex":"Think about the forms each works best on.","a":"U-substitution: when you have a composite function f(g(x))·g'(x) — the derivative of the inside is present. IBP: when you have a product of two 'unlike' functions (polynomial × exponential, polynomial × trig, exponential × trig, ln or arctan alone). Mnemonic LIATE for choosing u: Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential — pick the first applicable type as u.","diff":"medium"}
    ]},
    {"title":"Applications of Series","problems":[
      {"q":"Use the first three terms of the Maclaurin series for cos(x) to approximate cos(0.1).","ex":"cos(x)=1−x²/2!+x⁴/4!−…","a":"cos(0.1)≈1−(0.01)/2+(0.0001)/24=1−0.005+0.00000417≈0.99500. (Actual: 0.99500 ✓, series converges very fast for small x.)","diff":"medium"},
      {"q":"Why does the Taylor series for f(x)=ln(x) centered at x=0 not exist?","ex":"Think about domain.","a":"ln(x) is undefined at x=0 (and for x<0). A Taylor series centered at a point requires the function and all its derivatives to be defined at that point. Since ln(0) is undefined (−∞), no Taylor series exists at x=0. The series for ln(1+x) (centered at x=0) is valid: ln(1+x)=x−x²/2+x³/3−… for |x|≤1, x≠−1.","diff":"hard"},
      {"q":"Show that the alternating series Σ(−1)ⁿ/(2n+1) = π/4.","ex":"Recognize this as the Leibniz formula.","a":"The Maclaurin series for arctan(x)=x−x³/3+x⁵/5−… is valid for |x|≤1. At x=1: arctan(1)=π/4=1−1/3+1/5−1/7+…=Σ(−1)ⁿ/(2n+1). This is the Leibniz formula for π. The series converges by the alternating series test (terms decrease to 0).","diff":"hard"}
    ]}
  ],
  # Unit 4 — AP Statistics
  [
    {"title":"Exploring One-Variable Data","problems":[
      {"q":"For the dataset {3,7,7,9,10,12,15}: find the mean, median, and mode.","ex":"Mean=sum/n; median=middle value; mode=most frequent.","a":"Mean=(3+7+7+9+10+12+15)/7=63/7=9. Median (7 values, middle is 4th)=9. Mode=7 (appears twice).","diff":"easy"},
      {"q":"What is the IQR and how is it used to identify outliers?","ex":"IQR=Q3−Q1; outlier rule.","a":"IQR=Q3−Q1 (middle 50% of data). Outlier: any value below Q1−1.5·IQR or above Q3+1.5·IQR. IQR is resistant to extreme values, making it better than range for describing spread when outliers are present.","diff":"medium"},
      {"q":"Compare the shapes: right-skewed, left-skewed, and symmetric distributions and their relationship between mean and median.","ex":"Think about where the tail pulls the mean.","a":"Symmetric: mean≈median. Right-skewed (positive skew): long tail to the right; mean>median (tail pulls mean right). Left-skewed (negative skew): long tail to the left; mean<median. The median is more resistant to skew and outliers, making it preferable for skewed distributions.","diff":"medium"}
    ]},
    {"title":"Exploring Two-Variable Data","problems":[
      {"q":"The correlation between hours studied and test scores is r=0.87. Interpret this value.","ex":"Think about direction, strength, and what r doesn't tell you.","a":"r=0.87 indicates a strong positive linear relationship — as hours studied increase, test scores tend to increase. However, correlation does not imply causation; a third variable could explain both. r only measures linear association; a strong non-linear relationship can have r close to 0.","diff":"easy"},
      {"q":"The LSRL for predicting test score (y) from hours studied (x) is ŷ=55+8x. Predict the score for 5 hours, and interpret the slope.","ex":"Substitute x=5; interpret slope as rate of change.","a":"ŷ=55+8(5)=95. Slope (8): for each additional hour studied, the predicted test score increases by 8 points, on average.","diff":"easy"},
      {"q":"What is the coefficient of determination (r²) and what does r²=0.64 mean?","ex":"Think about variance explained.","a":"r²=0.64 means that 64% of the variability in the response variable (y) is explained by the linear relationship with the explanatory variable (x). The remaining 36% of variability is unexplained (residual/error). r²=0.64 → r=±0.8 (direction from context).","diff":"medium"}
    ]},
    {"title":"Collecting Data: Sampling and Experiments","problems":[
      {"q":"Distinguish between observational study, survey, and experiment in terms of ability to establish causation.","ex":"Think about random assignment.","a":"Observational study: researcher observes without interfering; can show association but not causation. Survey: collects self-reported data; can show association but prone to response bias. Experiment: researcher randomly assigns subjects to treatments; random assignment controls for confounding variables and CAN establish causation. Only properly designed experiments can establish causal relationships.","diff":"medium"},
      {"q":"What are confounding variables and give an example?","ex":"Think about a third variable that affects both X and Y.","a":"A confounding variable is related to both the explanatory variable and the response variable, making it impossible to determine the true causal relationship. Example: a study finds firefighters have higher cancer rates than the general population. Confound: smoke exposure (correlated with being a firefighter AND with cancer). Without controlling for smoke, you can't attribute cancer to being a firefighter specifically.","diff":"medium"},
      {"q":"Explain the purpose of random assignment in an experiment and what it controls for.","ex":"Think about confounding and the scope of conclusions.","a":"Random assignment distributes subjects randomly among treatment groups. Purpose: balances both known and unknown confounding variables across groups by chance, so any difference in outcomes is more likely due to the treatment. It allows causal conclusions (not just associations). Without random assignment — a study is observational even if researcher makes decisions.","diff":"medium"}
    ]},
    {"title":"Probability and Random Variables","problems":[
      {"q":"A fair coin is flipped 3 times. What is the probability of getting exactly 2 heads?","ex":"Use combinations: P(X=k)=C(n,k)p^k(1−p)^(n−k)","a":"P(X=2)=C(3,2)(0.5)²(0.5)¹=3·0.25·0.5=0.375.","diff":"easy"},
      {"q":"X is a random variable with E(X)=10 and Var(X)=4. Find E(3X+5) and Var(3X+5).","ex":"E(aX+b)=aE(X)+b; Var(aX+b)=a²Var(X).","a":"E(3X+5)=3(10)+5=35. Var(3X+5)=9·4=36. SD=6.","diff":"medium"},
      {"q":"Events A and B are independent with P(A)=0.3, P(B)=0.5. Find P(A and B) and P(A or B).","ex":"Independence: P(A∩B)=P(A)·P(B).","a":"P(A∩B)=0.3·0.5=0.15. P(A∪B)=P(A)+P(B)−P(A∩B)=0.3+0.5−0.15=0.65.","diff":"easy"}
    ]},
    {"title":"Sampling Distributions","problems":[
      {"q":"A population has μ=50, σ=10. For samples of size n=25, describe the sampling distribution of x̄.","ex":"Apply Central Limit Theorem.","a":"By CLT: sampling distribution of x̄ is approximately Normal with mean μ_{x̄}=50 and standard error σ_{x̄}=σ/√n=10/5=2. So x̄ ~ N(50,2).","diff":"easy"},
      {"q":"What is the Central Limit Theorem and why is it important?","ex":"Think about what it says about sample means and why that matters.","a":"CLT: for random samples from any population with mean μ and finite standard deviation σ, the sampling distribution of x̄ approaches a Normal distribution as n increases, with mean μ and SD σ/√n. Importance: allows us to use z-scores and Normal tables for inference about means even when the original population is not Normal, provided n is large enough (typically n≥30).","diff":"medium"},
      {"q":"A population proportion is p=0.4. For samples of size 100, what is the SD of p̂ and the approximate shape of its distribution?","ex":"SD(p̂)=√(p(1−p)/n)","a":"SD(p̂)=√(0.4·0.6/100)=√(0.0024)≈0.049. Shape: approximately Normal because np=40≥10 and n(1−p)=60≥10. So p̂~N(0.4, 0.049).","diff":"medium"}
    ]},
    {"title":"Inference for Proportions","problems":[
      {"q":"In a sample of 200, 110 said yes. Construct a 95% confidence interval for the population proportion.","ex":"p̂±z*√(p̂(1−p̂)/n); z*=1.96 for 95%.","a":"p̂=110/200=0.55. SE=√(0.55·0.45/200)=√(0.0012375)≈0.0352. CI: 0.55±1.96(0.0352)=0.55±0.069=(0.481, 0.619). We are 95% confident the true proportion is between 48.1% and 61.9%.","diff":"medium"},
      {"q":"Interpret a 95% confidence interval in plain language.","ex":"What does '95% confident' actually mean?","a":"A 95% CI means: if we were to take many repeated samples and construct a CI from each, approximately 95% of those intervals would contain the true population parameter. It does NOT mean: 'there is a 95% chance the true proportion is in this interval' (the parameter is fixed; the interval either does or doesn't contain it).","diff":"medium"},
      {"q":"A researcher claims 60% of students support a policy. A sample of 100 gives p̂=0.54. Test H₀:p=0.6 at α=0.05 (two-tailed).","ex":"z=(p̂−p₀)/√(p₀(1−p₀)/n)","a":"z=(0.54−0.60)/√(0.60·0.40/100)=(−0.06)/0.049=−1.22. For two-tailed test at α=0.05: critical value=±1.96. |−1.22|<1.96 → fail to reject H₀. Insufficient evidence that the proportion differs from 0.60. (p-value≈0.222>0.05.)","diff":"hard"}
    ]},
    {"title":"Inference for Means","problems":[
      {"q":"A sample of 25 gives x̄=48, s=10. Construct a 90% CI for μ (population normal).","ex":"Use t-distribution with df=n−1=24; t*≈1.711.","a":"SE=s/√n=10/5=2. t*=1.711 (df=24, 90%). CI: 48±1.711(2)=48±3.42=(44.58, 51.42).","diff":"medium"},
      {"q":"What assumptions are needed for a one-sample t-test?","ex":"Think about randomness, normality, and independence.","a":"(1) Random sample from population. (2) Observations independent (n<10% of population if sampling without replacement). (3) Population normal OR n≥30 (CLT applies). The t-test is robust to mild non-normality, especially for larger samples.","diff":"easy"},
      {"q":"Two independent samples test: n₁=40, x̄₁=65, s₁=8; n₂=50, x̄₂=60, s₂=10. Test H₀: μ₁=μ₂ at α=0.05.","ex":"Two-sample t-test; compute t statistic.","a":"t=(65−60)/√(64/40+100/50)=5/√(1.6+2)=5/√3.6=5/1.897≈2.63. df≈min(39,49)=39 (conservative). Critical value≈2.023. |2.63|>2.023 → reject H₀. Evidence that μ₁≠μ₂.","diff":"hard"}
    ]},
    {"title":"Chi-Square Tests","problems":[
      {"q":"What does a chi-square goodness-of-fit test examine?","ex":"Think about observed vs. expected frequencies.","a":"It tests whether the observed distribution of a categorical variable matches a hypothesized (expected) distribution. H₀: the population follows the proposed distribution. Test statistic χ²=Σ(O−E)²/E. Reject H₀ if χ² is large (more discrepancy than chance).","diff":"easy"},
      {"q":"A die is rolled 60 times. Expected: 10 per face. Observed: 8,10,11,9,14,8. Calculate χ².","ex":"χ²=Σ(O−E)²/E","a":"χ²=(8−10)²/10+(10−10)²/10+(11−10)²/10+(9−10)²/10+(14−10)²/10+(8−10)²/10=4/10+0+1/10+1/10+16/10+4/10=26/10=2.6. df=5; critical value at α=0.05 is 11.07. 2.6<11.07 → fail to reject; no evidence the die is unfair.","diff":"medium"},
      {"q":"What is a chi-square test of independence and when is it used?","ex":"Think about two categorical variables.","a":"Used when you have two categorical variables measured on the same subjects and want to test whether they are associated (not independent). H₀: the two variables are independent. Set up a two-way contingency table; expected counts = (row total × column total)/grand total. χ²=Σ(O−E)²/E with df=(rows−1)(columns−1).","diff":"medium"}
    ]},
    {"title":"Inference for Regression","problems":[
      {"q":"What does inference for regression test, and what are the conditions?","ex":"Think about the slope parameter.","a":"Tests whether there is a significant linear relationship: H₀: β=0 (no linear relationship). Test statistic: t=b/SE_b with df=n−2. Conditions: (1) Linear relationship, (2) Independent observations, (3) Normal distribution of residuals, (4) Equal spread of residuals (constant variance/homoscedasticity) — check with residual plots.","diff":"medium"},
      {"q":"A regression of y on x gives b=3.2, SE_b=1.1, n=20. Test H₀: β=0 at α=0.05.","ex":"t=b/SE_b, df=n−2=18.","a":"t=3.2/1.1=2.91. df=18; critical value≈2.101. 2.91>2.101 → reject H₀. There is significant evidence of a linear relationship between x and y.","diff":"medium"},
      {"q":"Why should you look at residual plots after computing a regression?","ex":"Think about checking regression conditions.","a":"Residual plots reveal whether regression assumptions are met: (1) If residuals show a curve → relationship is not linear (model is misspecified). (2) If spread of residuals increases with x (fan shape) → variance is not constant. (3) Outliers or influential points distort the LSRL. A good residual plot shows random scatter around 0 with constant spread — confirming linearity and homoscedasticity.","diff":"medium"}
    ]}
  ]
]
