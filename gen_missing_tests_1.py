"""Missing tests part 1: G12 history unit 4, AP science units 5-7, AP history units 5-9"""

def mc(q, a, b, c, d, correct, exp):
    return {"type":"mc","q":q,"choices":[a,b,c,d],"correct":correct,"exp":exp}

# ── Grade 12 History Unit 4 ───────────────────────────────────────────────────
G12_HISTORY_U4 = {
  "title": "Philosophy & Ethics Intro",
  "questions": [
    mc("Which branch of philosophy asks 'What is real?'","Epistemology","Metaphysics","Ethics","Logic",1,"Metaphysics examines the nature of reality, existence, and being."),
    mc("Utilitarianism holds that the right action is the one that:","Follows universal moral rules","Produces the greatest good for the greatest number","Fulfills duties regardless of consequences","Expresses virtue of character",1,"Utilitarianism (Mill, Bentham) judges actions by their outcomes — maximize happiness."),
    mc("Kant's categorical imperative says you should:","Act to maximize utility","Act only on rules you could will to be universal laws","Follow natural law","Consult cultural norms",1,"The categorical imperative tests whether a maxim could be universalized without contradiction."),
    mc("Which ethical theory focuses on character and virtues rather than rules or outcomes?","Deontology","Consequentialism","Virtue ethics","Contractarianism",2,"Virtue ethics (Aristotle) focuses on developing excellent character traits (virtues)."),
    mc("John Rawls' 'veil of ignorance' is used to:","Argue for absolute property rights","Design fair principles of justice without knowing one's social position","Justify utilitarianism","Defend traditional values",1,"Behind the veil of ignorance, you don't know your place in society, so you design fair rules."),
    mc("The social contract theory (Hobbes, Locke, Rousseau) argues that:","Government is divinely ordained","Political authority derives from agreement among individuals","The strongest should rule","Morality is relative to culture",1,"Social contract theorists say legitimate government rests on consent of the governed."),
    mc("Hobbes described life without government as:","Peaceful and cooperative","Solitary, poor, nasty, brutish, and short","Naturally virtuous","Governed by natural law",1,"In Leviathan, Hobbes argues the state of nature is a war of all against all."),
    mc("Epistemology is the study of:","The nature of beauty","Knowledge — what it is and how we acquire it","Political authority","Moral duty",1,"Epistemology examines knowledge, belief, justification, and truth."),
    mc("A priori knowledge is knowledge that:","Comes from sensory experience","Is independent of experience and known through reason alone","Is culturally relative","Cannot be known with certainty",1,"A priori knowledge (e.g., math) is knowable through reason, not experience."),
    mc("Which philosopher argued that we can only know appearances (phenomena), not things-in-themselves (noumena)?","Descartes","Hume","Kant","Plato",2,"Kant distinguished phenomena (how things appear to us) from noumena (things as they are in themselves)."),
    mc("Moral relativism holds that:","There are universal moral truths","Moral judgments are relative to culture or individual","Reason alone determines morality","Nature dictates right action",1,"Moral relativism denies universal moral standards, saying morality varies by context."),
    mc("Plato's allegory of the cave illustrates:","The social contract","How sensory experience is the only path to knowledge","The difference between appearance and reality","The virtue of courage",2,"Prisoners see shadows (appearances); the philosopher escapes to see the real world (Forms)."),
    mc("Which philosopher argued that 'God is dead' and criticized herd morality?","Sartre","Nietzsche","Hegel","Schopenhauer",1,"Nietzsche declared 'God is dead' and critiqued conventional morality as slave morality."),
    mc("Existentialism holds that:","Essence precedes existence","Existence precedes essence — humans create their own meaning","Morality is fixed by nature","God determines human purpose",1,"Sartre's existentialism: we exist first, then define ourselves through choices."),
    mc("The trolley problem is a classic example of a conflict between:","Virtue ethics and natural law","Deontological and consequentialist reasoning","Existentialism and rationalism","Relativism and absolutism",1,"It pits the duty not to harm (deontology) against saving more lives (consequentialism)."),
    mc("Natural law theory holds that morality is:","Purely conventional","Derived from human nature and discoverable by reason","Whatever maximizes happiness","Relative to social agreements",1,"Natural law (Aquinas, Aristotle) grounds morality in human nature and reason."),
    mc("Which statement best describes the difference between ethics and morality?","They are completely unrelated","Ethics is the philosophical study; morality refers to actual beliefs/practices","Morality is objective; ethics is subjective","Ethics applies only to professionals",1,"Ethics is the systematic philosophical inquiry; morality is the lived practice of right and wrong."),
    mc("Socrates' method of inquiry (Socratic method) works by:","Lecturing students on fixed truths","Asking probing questions to expose contradictions in beliefs","Writing systematic treatises","Conducting empirical experiments",1,"The Socratic method uses dialectical questioning to examine assumptions and reach truth."),
    mc("Which position holds that morality is objective and binding regardless of opinion?","Moral relativism","Emotivism","Moral realism","Nihilism",2,"Moral realism says moral facts exist independently of what anyone believes."),
    mc("Aristotle's concept of eudaimonia is best translated as:","Pleasure","Duty","Flourishing or well-being","Social harmony",2,"Eudaimonia is the highest good — living and faring well, achieved through virtuous activity."),
  ]
}

# ── AP Science Unit 5: AP Physics 2 ──────────────────────────────────────────
AP_SCIENCE_U5 = {
  "title": "AP Physics 2: Algebra-Based",
  "questions": [
    mc("Pascal's principle states that pressure applied to an enclosed fluid:","Decreases with depth","Is transmitted equally throughout","Acts only at the point of application","Increases with temperature",1,"Pascal's principle: pressure change in a confined fluid is transmitted undiminished throughout."),
    mc("Archimedes' principle states that buoyant force equals:","Weight of the submerged object","Weight of fluid displaced by the object","Volume of the object times gravity","Mass of the object",1,"Buoyant force = weight of displaced fluid. If this exceeds object's weight, it floats."),
    mc("The first law of thermodynamics states that:","Entropy always increases","Energy cannot be created or destroyed — ΔU = Q - W","Heat flows from cold to hot","Entropy of a perfect crystal at 0 K is zero",1,"First law: change in internal energy = heat added minus work done by the system."),
    mc("Which process occurs at constant pressure?","Isochoric","Isothermal","Isobaric","Adiabatic",2,"Isobaric = constant pressure. Isochoric = constant volume. Isothermal = constant temperature."),
    mc("Coulomb's law states that electric force between two charges:","Is proportional to the sum of charges","Is inversely proportional to distance (not distance squared)","Is proportional to the product of charges and inversely proportional to distance squared","Acts only on positive charges",2,"F = kq₁q₂/r². Force is proportional to product of charges, inversely to square of distance."),
    mc("Electric field lines point:","From negative to positive","From positive to negative charge","Perpendicular to the field direction","In the direction of decreasing potential",1,"E-field lines point in the direction a positive test charge would move: away from + toward -."),
    mc("A capacitor stores energy in the form of:","Magnetic field","Electric field","Kinetic energy of electrons","Thermal energy",1,"Capacitors store energy in the electric field between their plates: U = ½CV²."),
    mc("Ohm's law states that current through a conductor is:","Proportional to resistance","Inversely proportional to voltage","Directly proportional to voltage and inversely to resistance","Proportional to resistance squared",2,"I = V/R. Current is proportional to voltage and inversely proportional to resistance."),
    mc("In a series circuit, which quantity is the same through all components?","Voltage","Current","Resistance","Power",1,"In series, the same current flows through all components. Voltage divides."),
    mc("Lenz's law states that induced current flows in a direction that:","Aids the change in flux that produced it","Opposes the change in magnetic flux","Flows with the magnetic field","Increases resistance",1,"Lenz's law: induced current creates a magnetic field opposing the change in flux (conservation of energy)."),
    mc("Which type of wave requires a medium to travel?","Electromagnetic","Mechanical","Light","Radio",1,"Mechanical waves (sound, water waves) need a medium. Electromagnetic waves do not."),
    mc("When light goes from a less dense to a more dense medium, it:","Speeds up and bends away from normal","Slows down and bends toward normal","Maintains the same speed","Is completely reflected",1,"Light slows in denser media and bends toward the normal (Snell's law: n₁sinθ₁ = n₂sinθ₂)."),
    mc("Total internal reflection occurs when:","Angle of incidence equals the critical angle or greater","Angle of incidence is zero","Light travels from dense to less dense and angle is below critical","Light hits a perfectly flat surface",0,"TIR occurs when light in a denser medium hits the boundary at or beyond the critical angle."),
    mc("The photoelectric effect demonstrated that light:","Is purely a wave","Comes in discrete packets (photons) with energy E=hf","Has infinite speed","Cannot transfer momentum",1,"Einstein's photoelectric effect showed light behaves as photons; E = hf. Won him the Nobel Prize."),
    mc("Which particle has no charge?","Proton","Electron","Neutron","Positron",2,"Neutrons are electrically neutral. Protons are positive, electrons negative."),
    mc("Alpha decay emits:","An electron","A helium nucleus (2 protons, 2 neutrons)","A high-energy photon","A neutron",1,"Alpha particle = ⁴He nucleus. Alpha decay decreases atomic number by 2, mass number by 4."),
    mc("What is the half-life of a radioactive sample?","Time for all atoms to decay","Time for half the atoms to decay","Time for activity to double","Time for energy to halve",1,"Half-life: time for half of a radioactive sample to decay. Activity decreases by half each half-life."),
    mc("Which lens converges parallel light to a focal point?","Concave (diverging)","Plane mirror","Convex (converging)","Flat lens",2,"Convex (converging) lenses bring parallel rays together at the focal point."),
    mc("Standing waves form when:","Two waves travel in the same direction","A wave reflects and interferes with itself, creating nodes and antinodes","Waves are absorbed by a surface","Frequency is below resonance",1,"Standing waves result from superposition of a wave and its reflection, creating fixed nodes."),
    mc("The entropy of an isolated system always:","Decreases over time","Remains constant","Increases or stays the same (second law)","Returns to its initial value",2,"Second law of thermodynamics: entropy of an isolated system never decreases."),
  ]
}

# ── AP Science Unit 6: AP Physics C Mechanics ────────────────────────────────
AP_SCIENCE_U6 = {
  "title": "AP Physics C: Mechanics",
  "questions": [
    mc("In calculus-based kinematics, velocity is the:","Integral of acceleration with respect to time","Derivative of position with respect to time","Second derivative of position","Integral of position",1,"v = dx/dt. Velocity is the first derivative of position with respect to time."),
    mc("Newton's second law in calculus form is expressed as:","F = mv","F = dp/dt (rate of change of momentum)","F = ma only for constant mass","F = d²x/dt²",1,"F = dp/dt is the most general form; reduces to F = ma when mass is constant."),
    mc("The work-energy theorem states:","W = Fd cosθ only for constant force","Net work = change in kinetic energy: W_net = ΔKE","Work equals potential energy change","W = mgh always",1,"W_net = ΔKE = ½mv_f² − ½mv_i². This holds for variable forces via integration."),
    mc("For a conservative force, the relationship between force and potential energy is:","F = U","F = -dU/dx","F = dU/dt","F = ∫U dx",1,"Conservative force: F = -dU/dx. The force is the negative gradient of potential energy."),
    mc("Angular momentum L of a particle is defined as:","L = mv","L = r × p = r × mv","L = Iα","L = τt",1,"L = r × p. For a particle, angular momentum is the cross product of position and linear momentum."),
    mc("The rotational analog of Newton's second law is:","F = ma","τ_net = Iα","L = Iω","τ = Fr",1,"τ = Iα: net torque equals moment of inertia times angular acceleration."),
    mc("Which theorem relates the moment of inertia about the center of mass to another parallel axis?","Perpendicular axis theorem","Parallel axis theorem: I = I_cm + Md²","Conservation of angular momentum","Work-energy theorem",1,"Parallel axis theorem: I = I_cm + Md². d = distance between axes."),
    mc("For a rolling object without slipping, the relationship between v and ω is:","v = rω²","v = rω","ω = rv","v = r/ω",1,"No-slip condition: v_cm = rω. The contact point has zero velocity."),
    mc("Simple harmonic motion occurs when restoring force is:","Constant","Proportional to displacement: F = -kx","Proportional to velocity","Equal to gravity",1,"SHM: F = -kx. Acceleration is proportional to and opposite displacement."),
    mc("The period of a simple pendulum (small angles) depends on:","Mass of the bob","Length and gravitational acceleration: T = 2π√(L/g)","Amplitude of swing","Material of the string",1,"T = 2π√(L/g). Period is independent of mass and amplitude (for small angles)."),
    mc("Gravitational potential energy between two masses is:","U = mgh","U = -GMm/r","U = GMm/r","U = -mgh",1,"U = -GMm/r (negative because gravity is attractive). U → 0 as r → ∞."),
    mc("A satellite in circular orbit has speed determined by:","v = √(GM/r)","v = √(2GM/r)","v = √(gr)","v = GM/r²",0,"For circular orbit: gravitational force = centripetal force → v = √(GM/r)."),
    mc("Impulse is defined as:","Force times distance","Change in momentum: J = Δp = FΔt","Work done by force","Force times acceleration",1,"Impulse J = FΔt = Δp. Impulse equals change in momentum."),
    mc("In an elastic collision:","Only momentum is conserved","Both momentum and kinetic energy are conserved","Only kinetic energy is conserved","Neither is conserved",1,"Elastic collisions conserve both momentum and kinetic energy. Inelastic conserve only momentum."),
    mc("The center of mass of a system moves as if:","All forces act at each particle","All external forces act on the total mass at that point","Internal forces determine its motion","It is always at the geometric center",1,"r_cm = Σmᵢrᵢ/M. Net external force = Ma_cm; center of mass obeys Newton's 2nd law."),
    mc("For a spring-mass system, ω (angular frequency) equals:","√(m/k)","√(k/m)","k/m","2πk/m",1,"ω = √(k/m) for a spring-mass system. Period T = 2π/ω = 2π√(m/k)."),
    mc("Kepler's third law states that for planetary orbits:","T is proportional to r","T² is proportional to r³","T² is proportional to r²","T is proportional to r²",1,"T² ∝ r³ (or T² = 4π²r³/GM). Orbital period squared proportional to semi-major axis cubed."),
    mc("The moment of inertia of a solid sphere about its center is:","(1/2)MR²","(2/5)MR²","(2/3)MR²","MR²",1,"I = (2/5)MR² for a solid sphere. Hollow sphere: (2/3)MR². Disk: (1/2)MR²."),
    mc("Power delivered by a torque is:","P = τ/ω","P = τω","P = τ/α","P = τα",1,"P = τω (rotational analog of P = Fv). Power = torque times angular velocity."),
    mc("Which statement about escape velocity is correct?","It depends on the mass of the escaping object","v_esc = √(2GM/r); independent of escaping object's mass","v_esc = √(GM/r)","Escape velocity is infinite",1,"v_esc = √(2GM/r). Set KE = |PE|: ½mv² = GMm/r → v = √(2GM/r). Mass cancels."),
  ]
}

# ── AP Science Unit 7: AP Physics C E&M ─────────────────────────────────────
AP_SCIENCE_U7 = {
  "title": "AP Physics C: Electricity & Magnetism",
  "questions": [
    mc("Gauss's law states that electric flux through a closed surface equals:","The total charge times ε₀","The enclosed charge divided by ε₀","The area times the electric field","The potential times charge",1,"Φ_E = Q_enc/ε₀. Gauss's law is useful when charge distributions have symmetry."),
    mc("The electric field inside a conductor in electrostatic equilibrium is:","Maximum at center","Equal to the surface field","Zero","Determined by Ohm's law",2,"In electrostatic equilibrium, E = 0 inside a conductor. All charge resides on the surface."),
    mc("For a spherical shell of charge, the field inside the shell is:","Proportional to r","Equal to kQ/R²","Zero","Proportional to 1/r²",2,"By Gauss's law, a spherical shell has zero field inside (no enclosed charge)."),
    mc("The capacitance of a parallel-plate capacitor is:","C = εA/d","C = Q/V and for parallel plates C = ε₀A/d","C = Vd/Q","C = Q²/2U",1,"C = ε₀A/d. Larger area or smaller separation increases capacitance."),
    mc("Kirchhoff's voltage law (KVL) states that:","Current at a junction sums to zero","The sum of potential differences around any closed loop is zero","Resistance increases with temperature","Power equals current squared times resistance",1,"KVL: ΣV = 0 around any closed loop. Follows from conservation of energy."),
    mc("Kirchhoff's current law (KCL) states that:","Voltage at a node sums to zero","Sum of currents entering a junction equals sum leaving","Resistance is constant","EMF equals IR",1,"KCL: ΣI_in = ΣI_out at any junction. Follows from conservation of charge."),
    mc("The time constant τ of an RC circuit is:","τ = R/C","τ = RC","τ = 1/(RC)","τ = L/R",1,"τ = RC. After one time constant, a capacitor charges to (1 - 1/e) ≈ 63% of maximum."),
    mc("Ampere's law relates the magnetic field around a closed loop to:","Electric flux through the surface","The enclosed current: ∮B·dl = μ₀I_enc","The charge enclosed","The potential difference",1,"Ampere's law: ∮B·dl = μ₀I_enc. Useful for symmetric current distributions."),
    mc("The magnetic force on a moving charge is:","F = qE","F = qv × B","F = qvB (always)","F = ma",1,"F = qv × B. The force is perpendicular to both velocity and magnetic field."),
    mc("A long straight wire carrying current I produces a magnetic field at distance r of:","B = μ₀I/(4πr²)","B = μ₀I/(2πr)","B = μ₀Ir/(2π)","B = μ₀I",1,"B = μ₀I/(2πr) for a long straight wire. Field circles the wire (right-hand rule)."),
    mc("Faraday's law states that induced EMF equals:","The magnetic flux","The negative rate of change of magnetic flux: EMF = -dΦ/dt","The current times resistance","The charge times velocity",1,"Faraday's law: EMF = -dΦ_B/dt. The negative sign reflects Lenz's law."),
    mc("The inductance L of a solenoid is:","L = μ₀N/l","L = μ₀N²A/l","L = NΦ/I only for uniform field","Both B and C are correct",3,"L = μ₀N²A/l for a solenoid. Also L = NΦ/I by definition. Both expressions are valid."),
    mc("The time constant of an RL circuit is:","τ = RL","τ = R/L","τ = L/R","τ = L²/R",2,"τ = L/R. Current rises to 63% of maximum after one time constant in an RL circuit."),
    mc("In an LC circuit, energy oscillates between:","Kinetic and potential energy of charges","Electric field of capacitor and magnetic field of inductor","Resistance and capacitance","EMF and current",1,"LC circuit: energy oscillates between E-field (capacitor) and B-field (inductor). ω = 1/√(LC)."),
    mc("Maxwell's addition to Ampere's law includes:","Displacement current","Magnetic monopoles","Lenz's law correction","Faraday induction",0,"Maxwell added displacement current ε₀(dΦ_E/dt) to Ampere's law, predicting EM waves."),
    mc("The speed of electromagnetic waves in vacuum is:","Determined by the source speed","c = 1/√(μ₀ε₀) ≈ 3×10⁸ m/s","Variable based on frequency","Equal to the speed of sound",1,"Maxwell derived c = 1/√(μ₀ε₀), confirming light is an electromagnetic wave."),
    mc("Electric potential V is related to electric field E by:","V = E/d","E = -dV/dr (E is negative gradient of V)","V = Ed","E = V/d only for uniform fields",1,"E = -∇V. For uniform field: E = -ΔV/d. The field points from high to low potential."),
    mc("Energy stored in an inductor carrying current I is:","U = ½LI","U = LI²","U = ½LI²","U = L²I/2",2,"U = ½LI². Analogous to ½mv² for kinetic energy and ½CV² for a capacitor."),
    mc("Which law relates a changing electric field to a magnetic field?","Faraday's law","Ampere-Maxwell law","Gauss's law for magnetism","Lenz's law",1,"The Ampere-Maxwell law includes displacement current, linking changing E-field to B-field."),
    mc("Gauss's law for magnetism states that:","Magnetic flux through any closed surface equals the enclosed pole strength","The magnetic flux through any closed surface is zero (no magnetic monopoles)","B field follows inverse square law","Magnetic field lines begin at north poles",1,"∮B·dA = 0. Magnetic field lines always close on themselves — no magnetic monopoles exist."),
  ]
}

if __name__ == '__main__':
    import json
    data = {
        "g12_history_u4": G12_HISTORY_U4,
        "ap_science_u5": AP_SCIENCE_U5,
        "ap_science_u6": AP_SCIENCE_U6,
        "ap_science_u7": AP_SCIENCE_U7,
    }
    for k, v in data.items():
        print(f"{k}: {len(v['questions'])} questions")
