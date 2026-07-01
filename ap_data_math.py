"""AP Math data: 4 units x 7 topics"""

AP_MATH = [
  # Unit 1 - Limits and Continuity
  [
    {"title":"Introduction to Limits","problems":[
      {"q":"Evaluate lim(x→3) (x²−9)/(x−3).","ex":"Factor numerator as (x+3)(x−3).","a":"6","diff":"easy"},
      {"q":"Find lim(x→0) (sin x)/x.","ex":"Standard trigonometric limit — memorize this result.","a":"1","diff":"easy"},
      {"q":"Evaluate lim(x→2) (x³−8)/(x−2).","ex":"Factor x³−8=(x−2)(x²+2x+4).","a":"12","diff":"medium"},
      {"q":"Find lim(x→−1) (x²+3x+2)/(x+1).","ex":"Factor numerator.","a":"lim = x+2 evaluated at x=−1 → 1","diff":"medium"},
      {"q":"lim(x→4) (√x−2)/(x−4) = ?","ex":"Multiply numerator and denominator by (√x+2).","a":"1/4","diff":"hard"}
    ]},
    {"title":"One-Sided Limits","problems":[
      {"q":"Given f(x)={x+1 if x<2; x²−1 if x≥2}, find lim(x→2⁻) f(x) and lim(x→2⁺) f(x).","ex":"Substitute into the appropriate piece for each side.","a":"Left: 3; Right: 3. Two-sided limit = 3.","diff":"easy"},
      {"q":"Does lim(x→0) |x|/x exist? Explain.","ex":"Evaluate left and right limits separately.","a":"Left limit = −1; right limit = +1. Limits disagree, so the two-sided limit does not exist.","diff":"medium"},
      {"q":"Find lim(x→3⁺) (x−3)/(x²−9).","ex":"Factor denominator; approach from the right.","a":"lim = 1/(x+3) as x→3⁺ = 1/6","diff":"medium"},
      {"q":"For f(x)=1/(x−5), find lim(x→5⁻) f(x) and lim(x→5⁺) f(x).","ex":"As x approaches 5 from each side, what sign does the denominator have?","a":"Left: −∞; Right: +∞. Two-sided limit DNE.","diff":"medium"}
    ]},
    {"title":"Limit Laws and Computation","problems":[
      {"q":"If lim(x→a) f(x)=3 and lim(x→a) g(x)=−2, find lim(x→a) [f(x)·g(x)+f(x)].","ex":"Use product and sum limit laws.","a":"(3)(−2)+3 = −3","diff":"easy"},
      {"q":"Evaluate lim(x→∞) (5x³−2x)/(3x³+x²).","ex":"Divide every term by x³.","a":"5/3","diff":"medium"},
      {"q":"Find lim(x→∞) (√(x²+4x)−x).","ex":"Multiply by conjugate (√(x²+4x)+x)/(√(x²+4x)+x).","a":"2","diff":"hard"},
      {"q":"Evaluate lim(x→0) (1−cos x)/x.","ex":"Use known limit: lim(x→0)(1−cosx)/x=0.","a":"0","diff":"medium"}
    ]},
    {"title":"L'Hôpital's Rule","problems":[
      {"q":"Use L'Hôpital's Rule to evaluate lim(x→0) (eˣ−1)/x.","ex":"Check for 0/0 form, then differentiate top and bottom.","a":"lim = eˣ/1 at x=0 = 1","diff":"easy"},
      {"q":"Evaluate lim(x→∞) x/eˣ.","ex":"∞/∞ form — apply L'Hôpital.","a":"1/eˣ → 0 as x→∞","diff":"easy"},
      {"q":"Find lim(x→0) (sin x − x)/x³.","ex":"Apply L'Hôpital three times (0/0 each time).","a":"−1/6","diff":"hard"},
      {"q":"Evaluate lim(x→1) (ln x)/(x−1).","ex":"0/0 form — differentiate top and bottom.","a":"(1/x)/1 at x=1 = 1","diff":"medium"}
    ]},
    {"title":"Continuity and Discontinuities","problems":[
      {"q":"Is f(x)=(x²−4)/(x−2) continuous at x=2? What type of discontinuity exists?","ex":"Check all three continuity conditions.","a":"f(2) is undefined. Removable discontinuity (hole) at x=2 since the limit exists (=4) but f(2) is not defined.","diff":"easy"},
      {"q":"Classify the discontinuity of f(x)=1/(x−3)² at x=3.","ex":"Consider the one-sided limits.","a":"Infinite (essential) discontinuity — both one-sided limits approach +∞.","diff":"medium"},
      {"q":"Find k so f is continuous: f(x)={2x+k if x<1; 3x−1 if x≥1}.","ex":"Set lim(x→1⁻) f(x) = f(1).","a":"2(1)+k=3(1)−1=2 → k=0","diff":"medium"},
      {"q":"Explain why f(x)=tan x is discontinuous at x=π/2.","ex":"What happens to tan at odd multiples of π/2?","a":"cos(π/2)=0, so tan(π/2) is undefined. The left limit is +∞ and right limit is −∞ — an infinite (jump to ∞) discontinuity.","diff":"medium"}
    ]},
    {"title":"Limits at Infinity and Asymptotes","problems":[
      {"q":"Find the horizontal asymptote(s) of f(x)=(3x²+1)/(x²−4).","ex":"Evaluate lim(x→±∞) f(x).","a":"y=3 (both sides)","diff":"easy"},
      {"q":"Does f(x)=(2x+1)/(x²+1) have a horizontal asymptote? Find it.","ex":"Degree of denominator > numerator.","a":"lim(x→±∞)=0. HA: y=0","diff":"easy"},
      {"q":"Find all vertical asymptotes of f(x)=(x+1)/((x−2)(x+3)).","ex":"Set denominator=0, check numerator≠0.","a":"x=2 and x=−3","diff":"medium"},
      {"q":"Determine if f(x)=(x³−1)/(x²+1) has a slant asymptote and find it.","ex":"Perform polynomial long division.","a":"x³/(x²+1) → quotient x remainder −x−1; slant asymptote y=x","diff":"hard"}
    ]},
    {"title":"Intermediate Value Theorem","problems":[
      {"q":"Use the IVT to show f(x)=x³−x−1 has a root on (1,2).","ex":"Show f(1) and f(2) have opposite signs.","a":"f(1)=−1<0; f(2)=5>0. f is continuous; IVT guarantees c∈(1,2) where f(c)=0.","diff":"easy"},
      {"q":"Does f(x)=cos x have a fixed point on (0, π/2)? (A fixed point satisfies f(x)=x.) Justify.","ex":"Define g(x)=f(x)−x and apply IVT.","a":"g(0)=1>0; g(π/2)=cos(π/2)−π/2=−π/2<0. g is continuous → IVT guarantees g(c)=0, i.e., f(c)=c.","diff":"hard"},
      {"q":"A car travels 0 mph at t=0 and 60 mph at t=30 s. IVT guarantees what?","ex":"Speed is a continuous function of time.","a":"By IVT, the car reached every speed between 0 and 60 mph at some time in [0,30].","diff":"easy"},
      {"q":"Find an interval of length 1 where f(x)=x⁴−3x−1 must have a root.","ex":"Test integer values until sign change is found.","a":"f(1)=−3<0; f(2)=7>0 → root in (1,2) by IVT.","diff":"medium"}
    ]}
  ],
  # Unit 2 - Derivatives: Rules
  [
    {"title":"Definition of the Derivative","problems":[
      {"q":"Use the limit definition to find f′(x) for f(x)=x².","ex":"f′(x)=lim(h→0)[f(x+h)−f(x)]/h","a":"lim(h→0)[(x+h)²−x²]/h = lim(h→0)(2xh+h²)/h = 2x","diff":"easy"},
      {"q":"Use the definition to find the derivative of f(x)=3x+5.","ex":"Apply the difference quotient formula.","a":"lim(h→0)[(3(x+h)+5)−(3x+5)]/h = 3","diff":"easy"},
      {"q":"Find f′(2) using the definition if f(x)=x³.","ex":"Expand (2+h)³ then simplify.","a":"lim(h→0)[(2+h)³−8]/h = lim(h→0)(12h+6h²+h³)/h = 12","diff":"medium"},
      {"q":"Use the definition to show d/dx[c]=0 for any constant c.","ex":"f(x)=c, so f(x+h)=c.","a":"lim(h→0)[c−c]/h = lim(h→0) 0 = 0","diff":"easy"}
    ]},
    {"title":"Power Rule and Polynomial Differentiation","problems":[
      {"q":"Differentiate f(x)=7x⁵−3x³+2x−9.","ex":"Apply power rule to each term.","a":"f′(x)=35x⁴−9x²+2","diff":"easy"},
      {"q":"Find dy/dx for y=4√x−3/x².","ex":"Rewrite as 4x^(1/2)−3x^(−2).","a":"dy/dx=2x^(−1/2)+6x^(−3)=2/√x+6/x³","diff":"medium"},
      {"q":"Find the equation of the tangent line to f(x)=x³−2x at x=2.","ex":"Find slope via f′(2), then use point-slope form.","a":"f′(x)=3x²−2; f′(2)=10; f(2)=4; y−4=10(x−2) → y=10x−16","diff":"medium"},
      {"q":"At what x-values does f(x)=x³−3x have horizontal tangent lines?","ex":"Horizontal tangent ⟹ f′(x)=0.","a":"f′(x)=3x²−3=0 → x=±1","diff":"medium"}
    ]},
    {"title":"Product and Quotient Rules","problems":[
      {"q":"Differentiate h(x)=(x²+1)(3x−2).","ex":"(uv)′=u′v+uv′","a":"h′(x)=2x(3x−2)+(x²+1)(3)=9x²−4x+3","diff":"easy"},
      {"q":"Find f′(x) for f(x)=(2x+1)/(x²−3).","ex":"Quotient rule: (u/v)′=(u′v−uv′)/v²","a":"f′(x)=[(2)(x²−3)−(2x+1)(2x)]/(x²−3)²=(−2x²−2x−6)/(x²−3)²","diff":"medium"},
      {"q":"Differentiate g(x)=x²·sin x.","ex":"Product rule with u=x², v=sin x.","a":"g′(x)=2x sin x+x² cos x","diff":"medium"},
      {"q":"Find the derivative of h(x)=eˣ/x³.","ex":"Quotient rule with u=eˣ, v=x³.","a":"h′(x)=(eˣ·x³−eˣ·3x²)/x⁶=eˣ(x−3)/x⁴","diff":"medium"}
    ]},
    {"title":"Chain Rule","problems":[
      {"q":"Differentiate f(x)=(3x+1)⁵.","ex":"Outer function: u⁵; inner: u=3x+1.","a":"f′(x)=5(3x+1)⁴·3=15(3x+1)⁴","diff":"easy"},
      {"q":"Find dy/dx for y=sin(x²).","ex":"Outer: sin u; inner: u=x².","a":"dy/dx=cos(x²)·2x=2x cos(x²)","diff":"easy"},
      {"q":"Differentiate f(x)=e^(3x²−1).","ex":"Outer: eᵘ; inner: u=3x²−1.","a":"f′(x)=e^(3x²−1)·6x","diff":"medium"},
      {"q":"Find f′(x) for f(x)=ln(sin x).","ex":"d/dx[ln u]=u′/u; u=sin x.","a":"f′(x)=cos x/sin x=cot x","diff":"medium"},
      {"q":"Differentiate y=√(x²+4x+1).","ex":"Rewrite as (x²+4x+1)^(1/2), then chain rule.","a":"dy/dx=(2x+4)/(2√(x²+4x+1))=(x+2)/√(x²+4x+1)","diff":"hard"}
    ]},
    {"title":"Implicit Differentiation","problems":[
      {"q":"Find dy/dx for x²+y²=25.","ex":"Differentiate both sides w.r.t. x; d/dx[y²]=2y·dy/dx.","a":"2x+2y dy/dx=0 → dy/dx=−x/y","diff":"easy"},
      {"q":"Find dy/dx for x³+y³=6xy.","ex":"Differentiate both sides; collect dy/dx terms.","a":"3x²+3y²dy/dx=6y+6x dy/dx → dy/dx=(6y−3x²)/(3y²−6x)=(2y−x²)/(y²−2x)","diff":"hard"},
      {"q":"Find the slope of x²y+y³=2 at the point (1,1).","ex":"Differentiate implicitly, then substitute.","a":"2xy+x²dy/dx+3y²dy/dx=0 → dy/dx=−2xy/(x²+3y²); at (1,1): −2/4=−1/2","diff":"hard"},
      {"q":"If x sin y=1, find dy/dx.","ex":"Differentiate using product and chain rules.","a":"sin y+x cos y·dy/dx=0 → dy/dx=−sin y/(x cos y)=−tan y/x","diff":"medium"}
    ]},
    {"title":"Related Rates","problems":[
      {"q":"A ladder 10 ft long leans against a wall. The base slides away at 2 ft/s. How fast is the top sliding down when the base is 6 ft from the wall?","ex":"x²+y²=100; differentiate w.r.t. t.","a":"2x dx/dt+2y dy/dt=0; y=8; dy/dt=−2(6)(2)/(2·8)=−3/2 ft/s","diff":"hard"},
      {"q":"A spherical balloon is inflated at 10 cm³/s. How fast is the radius growing when r=5 cm?","ex":"V=(4/3)πr³; dV/dt=4πr² dr/dt.","a":"10=4π(25)dr/dt → dr/dt=10/(100π)=1/(10π) cm/s","diff":"medium"},
      {"q":"Water drains from a conical tank (r=4m, h=8m) at 2 m³/min. How fast is the water level dropping when h=4m?","ex":"V=(1/3)πr²h; use similar triangles: r=h/2.","a":"V=πh³/12; dV/dt=(π/4)h² dh/dt; −2=(π/4)(16)dh/dt → dh/dt=−1/(2π) m/min","diff":"hard"},
      {"q":"Two cars start from the same point. One drives east at 60 mph, the other north at 80 mph. How fast is the distance between them growing after 1 hour?","ex":"d²=x²+y²; differentiate and substitute x=60, y=80.","a":"d=100; 2d·dd/dt=2x·dx/dt+2y·dy/dt; dd/dt=(60·60+80·80)/100=100 mph","diff":"hard"}
    ]},
    {"title":"Higher-Order Derivatives and Motion","problems":[
      {"q":"Find f″(x) for f(x)=x⁴−3x²+2.","ex":"Differentiate f′(x) once more.","a":"f′(x)=4x³−6x; f″(x)=12x²−6","diff":"easy"},
      {"q":"If the position of a particle is s(t)=t³−6t²+9t, find velocity and acceleration at t=2.","ex":"v=s′(t), a=s″(t).","a":"v(t)=3t²−12t+9; v(2)=−3 m/s; a(t)=6t−12; a(2)=0 m/s²","diff":"medium"},
      {"q":"Find all values of t where the particle s(t)=t³−6t²+9t changes direction.","ex":"Particle changes direction when v=0 and v changes sign.","a":"v(t)=3(t−1)(t−3)=0 at t=1 and t=3. Check sign change: yes at both → changes direction at t=1 and t=3.","diff":"medium"},
      {"q":"For f(x)=sin x, find f⁽⁴⁾(x) (4th derivative).","ex":"sin→cos→−sin→−cos→sin...","a":"f⁽⁴⁾(x)=sin x (the 4th derivative returns to the original function)","diff":"easy"}
    ]}
  ],
  # Unit 3 - Applications of Derivatives
  [
    {"title":"Critical Points and Extrema","problems":[
      {"q":"Find all critical points of f(x)=2x³−9x²+12x−4.","ex":"Set f′(x)=0.","a":"f′(x)=6x²−18x+12=6(x−1)(x−2)=0 → x=1 and x=2","diff":"easy"},
      {"q":"Find the absolute maximum and minimum of f(x)=x³−3x on [−2,2].","ex":"Check critical points AND endpoints.","a":"f′(x)=3x²−3=0 → x=±1; f(−2)=−2, f(−1)=2, f(1)=−2, f(2)=2; absolute max=2, absolute min=−2","diff":"medium"},
      {"q":"Show that f(x)=eˣ has no critical points.","ex":"f′(x)=eˣ; when is this zero?","a":"eˣ>0 for all x, so f′(x) is never 0. No critical points exist.","diff":"easy"},
      {"q":"Find the local extrema of f(x)=x⁴−8x².","ex":"f′(x)=4x³−16x; factor and analyze sign.","a":"f′(x)=4x(x²−4)=0 → x=0,±2. Sign analysis: local max at x=0 (f=0), local min at x=±2 (f=−16)","diff":"medium"}
    ]},
    {"title":"First and Second Derivative Tests","problems":[
      {"q":"Use the second derivative test to classify the critical points of f(x)=x³−3x.","ex":"f′(x)=0 at x=±1; compute f″(x) at each.","a":"f″(x)=6x; f″(1)=6>0 → local min at x=1; f″(−1)=−6<0 → local max at x=−1","diff":"medium"},
      {"q":"Find intervals where g(x)=x³−6x²+9x is increasing and decreasing.","ex":"Analyze sign of g′(x).","a":"g′(x)=3x²−12x+9=3(x−1)(x−3); increasing on (−∞,1) and (3,∞); decreasing on (1,3)","diff":"medium"},
      {"q":"Find all inflection points of f(x)=x⁴−4x³.","ex":"Set f″(x)=0 and verify sign change.","a":"f″(x)=12x²−24x=12x(x−2)=0 → x=0,2. Inflection points at x=0 (f=0) and x=2 (f=−16)","diff":"medium"},
      {"q":"Determine concavity of f(x)=eˣ−x.","ex":"Find f″(x) and analyze its sign.","a":"f″(x)=eˣ>0 for all x → concave up everywhere, no inflection points","diff":"easy"}
    ]},
    {"title":"Curve Sketching","problems":[
      {"q":"Identify all key features for sketching f(x)=x³−3x²: domain, intercepts, critical points, inflection points.","ex":"Work through each feature systematically.","a":"Domain: all reals; x-intercepts: x=0,3; critical pts: x=0 (local max, f=0), x=2 (local min, f=−4); inflection pt: x=1; increasing: (−∞,0),(2,∞); decreasing: (0,2)","diff":"hard"},
      {"q":"Describe the end behavior of f(x)=−2x³+x.","ex":"Leading term determines end behavior.","a":"As x→+∞, f→−∞; as x→−∞, f→+∞ (negative leading coefficient, odd degree)","diff":"easy"},
      {"q":"Sketch key features of f(x)=(x²−1)/(x²−4): asymptotes, intercepts, symmetry.","ex":"Find VAs (denom=0), HA (degree comparison), x-intercepts (numer=0).","a":"VAs: x=±2; HA: y=1; x-intercepts: x=±1; y-intercept: 1/4; even function (symmetric about y-axis)","diff":"hard"},
      {"q":"For f(x)=xe^(−x), find max, asymptote, and concavity.","ex":"Apply product rule, then second derivative.","a":"f′(x)=e^(−x)(1−x)=0 → x=1 (max, f=1/e); HA: y=0 as x→∞; f″(x)=e^(−x)(x−2)=0 → inflection at x=2","diff":"hard"}
    ]},
    {"title":"Optimization Problems","problems":[
      {"q":"Find two positive numbers whose sum is 20 and whose product is maximized.","ex":"Let x and 20−x be the numbers; maximize P=x(20−x).","a":"P′=20−2x=0 → x=10. Numbers are 10 and 10; max product=100","diff":"easy"},
      {"q":"A farmer has 120 m of fencing to enclose a rectangular pen against a barn wall (one side free). Maximize area.","ex":"One side=barn wall (free); other three sides use fencing: 2w+l=120.","a":"A=lw=(120−2w)w; A′=120−4w=0 → w=30, l=60; max area=1800 m²","diff":"medium"},
      {"q":"A company's profit is P(x)=−2x²+80x−300 where x is units sold. Find the profit-maximizing quantity.","ex":"Maximize by setting P′(x)=0.","a":"P′(x)=−4x+80=0 → x=20 units; max profit=P(20)=−800+1600−300=500","diff":"medium"},
      {"q":"A box with square base and no top must hold 32 cm³. Minimize surface area.","ex":"V=x²h=32 → h=32/x²; SA=x²+4xh.","a":"SA=x²+128/x; SA′=2x−128/x²=0 → x³=64 → x=4; h=2; min SA=48 cm²","diff":"hard"}
    ]},
    {"title":"Mean Value Theorem","problems":[
      {"q":"Verify the MVT for f(x)=x²−2x on [1,4].","ex":"Find c where f′(c)=[f(4)−f(1)]/(4−1).","a":"Average rate=(8−(−1))/3=3; f′(x)=2x−2=3 → x=2.5 ∈ (1,4) ✓","diff":"medium"},
      {"q":"A car travels 180 miles in 3 hours. What does the MVT guarantee?","ex":"Apply MVT to position function.","a":"MVT guarantees the car was traveling at exactly 60 mph at some moment during the trip.","diff":"easy"},
      {"q":"Use Rolle's Theorem to show f(x)=x³−x has a point where f′(c)=0 on [0,1].","ex":"Check: continuous, differentiable, f(0)=f(1)?","a":"f(0)=0, f(1)=0; f is continuous and differentiable on [0,1]; by Rolle's, ∃c∈(0,1) with f′(c)=0; f′(x)=3x²−1=0 → c=1/√3 ≈ 0.577 ✓","diff":"medium"},
      {"q":"Why doesn't the MVT apply to f(x)=|x| on [−1,1]?","ex":"Check the conditions of the MVT.","a":"f is not differentiable at x=0 (sharp corner), violating the differentiability condition on the open interval (−1,1).","diff":"medium"}
    ]},
    {"title":"Linear Approximation and Differentials","problems":[
      {"q":"Use linear approximation to estimate √4.1.","ex":"f(x)=√x; linearize at x=4; L(x)=f(a)+f′(a)(x−a).","a":"f(4)=2; f′(4)=1/(2√4)=1/4; L(4.1)=2+(1/4)(0.1)=2.025","diff":"easy"},
      {"q":"Find the differential dy for y=x³−2x at x=3, dx=0.01.","ex":"dy=f′(x)dx","a":"dy=(3x²−2)dx=(27−2)(0.01)=0.25","diff":"easy"},
      {"q":"Use linearization to approximate sin(31°) without a calculator.","ex":"Convert 31°=π/6+π/180; linearize sin at π/6.","a":"L(x)=sin(π/6)+cos(π/6)(x−π/6); at π/6+π/180: ≈0.5+(√3/2)(π/180)≈0.515","diff":"hard"},
      {"q":"The radius of a sphere is measured as 10 cm with error ≤0.05 cm. Estimate the maximum error in volume.","ex":"V=(4/3)πr³; dV=4πr²dr.","a":"dV=4π(100)(0.05)=20π ≈ 62.8 cm³","diff":"medium"}
    ]},
    {"title":"Particle Motion Analysis","problems":[
      {"q":"s(t)=t³−9t²+24t gives position (meters) at time t (sec). Find when the particle is at rest.","ex":"Set v(t)=s′(t)=0.","a":"v(t)=3t²−18t+24=3(t−2)(t−4)=0 → t=2s and t=4s","diff":"easy"},
      {"q":"Using s(t)=t³−9t²+24t, find the total distance traveled from t=0 to t=5.","ex":"Track direction changes at t=2 and t=4.","a":"s(0)=0, s(2)=20, s(4)=16, s(5)=20; distance=|20−0|+|16−20|+|20−16|=20+4+4=28 m","diff":"hard"},
      {"q":"A particle's velocity is v(t)=6t²−18t. Find when it speeds up.","ex":"Particle speeds up when v and a have the same sign.","a":"a(t)=12t−18=0 at t=1.5; v(t)>0 for t>3; both positive for t>3 (speeds up); both negative for t<1.5 (also speeds up)","diff":"hard"},
      {"q":"If a(t)=4t−6 and v(0)=2, find v(t).","ex":"v(t)=∫a(t)dt+C; use initial condition.","a":"v(t)=2t²−6t+C; v(0)=C=2 → v(t)=2t²−6t+2","diff":"medium"}
    ]}
  ],
  # Unit 4 - Integrals and Statistics
  [
    {"title":"Antiderivatives and Indefinite Integrals","problems":[
      {"q":"Find ∫(5x⁴−3x²+2)dx.","ex":"Power rule in reverse: ∫xⁿdx=xⁿ⁺¹/(n+1)+C.","a":"x⁵−x³+2x+C","diff":"easy"},
      {"q":"Evaluate ∫(3/x + eˣ − cos x)dx.","ex":"Apply standard antiderivative rules.","a":"3ln|x|+eˣ−sin x+C","diff":"easy"},
      {"q":"Find ∫√(3x+1)dx using substitution.","ex":"Let u=3x+1.","a":"(2/9)(3x+1)^(3/2)+C","diff":"medium"},
      {"q":"Find ∫x·eˣ dx using integration by parts.","ex":"Let u=x, dv=eˣdx.","a":"xeˣ−eˣ+C=eˣ(x−1)+C","diff":"hard"}
    ]},
    {"title":"Definite Integrals and Riemann Sums","problems":[
      {"q":"Estimate ∫[0,4] x²dx using a left Riemann sum with n=4 rectangles.","ex":"Δx=1; left endpoints: 0,1,2,3.","a":"Δx(0²+1²+2²+3²)=1(0+1+4+9)=14","diff":"medium"},
      {"q":"Evaluate ∫[1,4] (2x+3)dx.","ex":"Find antiderivative F(x); compute F(4)−F(1).","a":"F(x)=x²+3x; F(4)−F(1)=(16+12)−(1+3)=24","diff":"easy"},
      {"q":"Evaluate ∫[0,π] sin x dx.","ex":"Antiderivative of sin x is −cos x.","a":"[−cos x]₀^π=(−cos π)−(−cos 0)=1+1=2","diff":"easy"},
      {"q":"Set up (don't evaluate) ∫[0,2] (4−x²)dx and describe what it represents geometrically.","ex":"Think about the region between the curve and x-axis.","a":"∫[0,2](4−x²)dx represents the area under y=4−x² and above the x-axis from x=0 to x=2.","diff":"medium"}
    ]},
    {"title":"Fundamental Theorem of Calculus","problems":[
      {"q":"State both parts of the Fundamental Theorem of Calculus.","ex":"Part 1 relates derivatives and integrals; Part 2 gives a way to evaluate definite integrals.","a":"Part 1: d/dx[∫[a,x] f(t)dt]=f(x). Part 2: ∫[a,b] f(x)dx=F(b)−F(a) where F′=f.","diff":"medium"},
      {"q":"Find d/dx[∫[1,x] (t³+1)dt].","ex":"Apply FTC Part 1 directly.","a":"x³+1","diff":"easy"},
      {"q":"Find d/dx[∫[x,x²] sin t dt].","ex":"Use FTC Part 1 with chain rule; split at a constant if needed.","a":"sin(x²)·2x−sin(x)·1=2x sin(x²)−sin x","diff":"hard"},
      {"q":"Evaluate ∫[0,3] (3x²−4x+1)dx and interpret the result.","ex":"FTC Part 2: find antiderivative, evaluate bounds.","a":"[x³−2x²+x]₀³=(27−18+3)−0=12","diff":"easy"}
    ]},
    {"title":"U-Substitution","problems":[
      {"q":"Evaluate ∫2x(x²+3)⁵dx.","ex":"Let u=x²+3; du=2x dx.","a":"∫u⁵du=u⁶/6+C=(x²+3)⁶/6+C","diff":"easy"},
      {"q":"Evaluate ∫[0,π/2] sin x·cos x dx.","ex":"Let u=sin x; du=cos x dx; change bounds.","a":"∫[0,1] u du=[u²/2]₀¹=1/2","diff":"medium"},
      {"q":"Evaluate ∫eˢⁱⁿ ˣ·cos x dx.","ex":"Let u=sin x.","a":"eˢⁱⁿ ˣ+C","diff":"medium"},
      {"q":"Evaluate ∫x/(x²+1) dx.","ex":"Let u=x²+1; du=2x dx.","a":"(1/2)ln(x²+1)+C","diff":"medium"}
    ]},
    {"title":"Area Between Curves","problems":[
      {"q":"Find the area between y=x² and y=x on [0,1].","ex":"Determine which function is on top; integrate the difference.","a":"x≥x² on [0,1]; A=∫[0,1](x−x²)dx=[x²/2−x³/3]₀¹=1/2−1/3=1/6","diff":"medium"},
      {"q":"Find the area enclosed by y=4−x² and y=x+2.","ex":"Find intersection points first, then integrate difference.","a":"4−x²=x+2 → x²+x−2=0 → x=1,−2; A=∫[−2,1]((4−x²)−(x+2))dx=∫[−2,1](2−x−x²)dx=9/2","diff":"hard"},
      {"q":"Set up the integral for the area between y=sin x and y=cos x from x=π/4 to x=5π/4.","ex":"Identify which is on top in the interval.","a":"sin x≥cos x on (π/4,5π/4); A=∫[π/4,5π/4](sin x−cos x)dx=2√2","diff":"hard"},
      {"q":"Find the area of the region bounded by y=eˣ, y=1, and x=2.","ex":"eˣ≥1 on [0,2].","a":"A=∫[0,2](eˣ−1)dx=[eˣ−x]₀²=(e²−2)−(1−0)=e²−3","diff":"medium"}
    ]},
    {"title":"Probability Distributions","problems":[
      {"q":"A Normal distribution has μ=70 and σ=10. What percentage of values lie between 60 and 80?","ex":"Apply the 68-95-99.7 rule.","a":"60 and 80 are each 1 SD from the mean → approximately 68% of values lie in this range.","diff":"easy"},
      {"q":"A random variable X is uniform on [2,8]. Find P(3≤X≤6).","ex":"P(a≤X≤b)=(b−a)/(total width) for uniform distributions.","a":"(6−3)/(8−2)=3/6=1/2","diff":"easy"},
      {"q":"For a standard normal distribution (μ=0, σ=1), P(Z<1.5)=0.9332. Find P(Z>1.5) and P(−1.5<Z<1.5).","ex":"Use symmetry and complement rule.","a":"P(Z>1.5)=1−0.9332=0.0668; P(−1.5<Z<1.5)=0.9332−0.0668=0.8664","diff":"medium"},
      {"q":"A binomial distribution has n=10, p=0.4. Find the expected value and standard deviation.","ex":"E(X)=np; SD=√(np(1−p)).","a":"E(X)=4; SD=√(10·0.4·0.6)=√2.4≈1.55","diff":"medium"}
    ]},
    {"title":"Statistical Inference and Hypothesis Testing","problems":[
      {"q":"A sample of 64 has mean 52 and SD 8. Construct a 95% CI for the population mean.","ex":"CI=x̄ ± z*(s/√n); z*=1.96 for 95%.","a":"52 ± 1.96(8/8) = 52 ± 1.96 = (50.04, 53.96)","diff":"medium"},
      {"q":"State H₀ and H₁ for: 'A new fertilizer increases average yield above 50 kg/plot.'","ex":"H₀ is the null (status quo); H₁ is the research claim.","a":"H₀: μ≤50; H₁: μ>50 (right-tailed test)","diff":"easy"},
      {"q":"A test gives z=2.3 for a two-tailed test with α=0.05. Critical values are ±1.96. What do you conclude?","ex":"Compare test statistic to critical values.","a":"|z|=2.3>1.96 → reject H₀. There is sufficient evidence at α=0.05 to reject the null hypothesis.","diff":"easy"},
      {"q":"What is a Type I error and a Type II error? Which is controlled by α?","ex":"Think about false positives and false negatives.","a":"Type I: rejecting a true H₀ (false positive); probability=α. Type II: failing to reject a false H₀ (false negative); probability=β. α controls Type I error.","diff":"medium"}
    ]}
  ]
]
