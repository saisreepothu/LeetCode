# Conditional Probability (FAANG DS Mastery)

Topic = conditional_probability  
Target Role = Data Scientist (Product / Experimentation / ML)  
Difficulty = Interview Level (FAANG/Google/Meta/Amazon)  
Goal = Deep Concept Mastery + Pattern Recognition + Unseen Question Handling

========================================
SECTION 1 — INTUITION (MULTI-LEVEL)
========================================

1) Explain like I am 10 years old (ELI10)
- Conditional probability is "the chance something happens after you learn something else already happened."
- If you know a clue (like it’s raining), you update how likely another thing is (like people carrying umbrellas).

2) Real-life daily life analogy
- You see wet sidewalks (B). That makes rain (A) more likely than it was before. You’re updating the chance of A using new information B.

3) Business/product analytics analogy (Google/Meta style)
- You want the probability a user purchases (A) given they started checkout (B): `P(purchase | started_checkout)`.
- This is how funnel steps work: each step conditions on the previous step having occurred.

4) Mathematical intuition (without heavy jargon)
- Start with the "overlap" of events A and B: `P(A and B)`.
- Then "zoom in" to only the world where B happened. Among that smaller world, ask what fraction also has A.
- That fraction is `P(A|B) = P(A ∩ B) / P(B)` (when `P(B) > 0`).

Core intuition (1 line)
- Conditional probability is probability after restricting attention to cases where the condition is true.

========================================
SECTION 2 — DEFINITIONS (INTERVIEW READY)
========================================

Formal definition (simple words)
- The conditional probability of A given B is the probability that A happens when we already know B happened.

Mathematical formulas
- `P(A|B) = P(A ∩ B) / P(B)` for `P(B) > 0`
- `P(A ∩ B) = P(A|B) P(B) = P(B|A) P(A)` (product rule)
- Bayes’ rule:
  - `P(A|B) = P(B|A) P(A) / P(B)` for `P(B) > 0`

Key related formulas (high ROI)
- Law of total probability (partition `{H_i}`):
  - `P(B) = Σ_i P(B|H_i) P(H_i)`
- Complement:
  - `P(A^c|B) = 1 - P(A|B)`
- Conditional independence:
  - `A ⟂ B | C` implies `P(A|B,C) = P(A|C)`

Common misconceptions
- Confusing `P(A|B)` with `P(B|A)` (classic Bayes trap).
- Ignoring base rates (prior `P(A)`) in rare-event problems (fraud, disease).
- Treating "given" as causal ("B causes A") rather than informational.
- Forgetting to normalize by `P(B)` or using the wrong denominator.

Difference vs similar concepts
- Conditional probability vs joint probability:
  - Joint: `P(A ∩ B)` is "both happen".
  - Conditional: `P(A|B)` is "A happens after restricting to B-happened cases".
- Conditional probability vs correlation:
  - Conditional probability is a probability statement; correlation is a numeric dependence summary (for numeric variables).

3 interview-ready one-liners
- "Conditional probability is probability restricted to the subset where the condition holds."
- "`P(A|B)` equals overlap `P(A∩B)` divided by how often the condition `B` occurs."
- "Bayes’ rule flips conditioning using priors and likelihoods; it’s essential for base-rate problems."

========================================
SECTION 3 — WHY THIS TOPIC MATTERS IN FAANG INTERVIEWS
========================================

Where it appears
- Product funnels: `P(purchase | impression)`, `P(purchase | click)`, drop-offs.
- Experimentation and metrics: segment-conditional effects, triggered analysis.
- ML: interpreting confusion matrices (precision/recall), Naive Bayes, calibration.
- Trust & safety/fraud: rare-event inference, alerting systems, priors.
- Data quality: selection bias, conditioning on observed data (missingness).

Interview rounds where it shows up
- Product sense + analytics deep dives (funnels, retention, segmentation).
- Experimentation/causal reasoning (conditioning on post-treatment variables).
- Applied stats / probability screens (Bayes, Monty Hall, balls/urns).
- ML system reasoning (precision vs recall vs base rate).

Real product examples
- YouTube: `P(watch >= 30s | clicked)` vs `P(click | impression)`; interpreting changes.
- Ads: `P(conversion | click)` vs `P(click | impression)`; attribution and funnel math.
- Search: `P(satisfied | reformulation)`; conditional evaluation by query type.
- Marketplace: `P(order | add_to_cart)`; conditional drop-offs by category.

========================================
SECTION 4 — COMPLETE PATTERN LIBRARY (EXHAUSTIVE)
========================================

Pattern 1: Direct Conditional (Definition Pattern)
- Meaning: compute `P(A|B)` from counts or from `P(A∩B)` and `P(B)`.
- Identify in 5 seconds: "given", "among those who", "out of users who did X".
- Why interviewers use it: checks fundamentals and denominator discipline.
- Visual model: 2-set Venn or contingency table.
- Toolkit: `P(A|B)=P(A∩B)/P(B)`.
- Traps: using `P(A)` in denominator; mixing base population with conditioned subset.
- Strategy:
  1. Define A and B.
  2. Compute overlap (A and B).
  3. Divide by total B.
- Business angle: funnel step conversion rate.

Pattern 2: Contingency Table (2x2, Confusion Matrix)
- Meaning: compute conditional probabilities from TP/FP/TN/FN or a 2x2 table.
- Identify: "precision", "recall", "false positive rate", "given flagged".
- Visual: 2x2 table with totals.
- Toolkit:
  - Precision = `P(Y=1|Ŷ=1) = TP/(TP+FP)`
  - Recall = `P(Ŷ=1|Y=1) = TP/(TP+FN)`
- Traps: swapping precision and recall; ignoring prevalence.
- Strategy: label table first, then compute.
- Business: alert systems, moderation queues.

Pattern 3: Bayes Inversion (Flip the Conditioning)
- Meaning: compute `P(A|B)` from `P(B|A)`, `P(A)`, `P(B|A^c)`.
- Identify: "probability of disease given positive test", "fraud given alert".
- Visual: probability tree or odds table.
- Toolkit:
  - `P(A|B)=P(B|A)P(A)/P(B)` with `P(B)=P(B|A)P(A)+P(B|A^c)P(A^c)`
- Traps: ignoring base rate; using `P(B)` incorrectly.
- Strategy:
  1. Choose hypothesis A vs not A.
  2. Use total probability to compute `P(B)`.
  3. Apply Bayes.
- Business: base-rate correction for rare events.

Pattern 4: Total Probability via Partition (Mixtures)
- Meaning: overall rate is weighted average across segments/components.
- Identify: "overall", "across groups", "mixture", "from different sources".
- Visual: tree with branches `H_i`.
- Toolkit: `P(B)=Σ P(B|H_i)P(H_i)`.
- Traps: forgetting weights sum to 1; wrong segment weights.
- Strategy: compute per-branch then sum.
- Business: blended conversion across channels.

Pattern 5: Sequential Events / Chain Rule
- Meaning: probability of a sequence using `P(A∩B)=P(A)P(B|A)`.
- Identify: "first..., then...", "without replacement", "two draws".
- Visual: tree with sequential draws.
- Toolkit: chain rule, hypergeometric logic.
- Traps: treating dependent draws as independent.
- Strategy: multiply step-by-step, conditioning each step.
- Business: multi-step user journeys.

Pattern 6: "At Least One" / Complement Conditioning
- Meaning: condition on events like "at least one success" and compute something like `P(A|A ∪ B)`.
- Identify: "given at least one", "at least one is X".
- Visual: list of cases; complement.
- Toolkit: `P(A|C)=P(A∩C)/P(C)`; often compute `P(C)` via complement.
- Traps: double counting cases; missing overlap.
- Strategy: enumerate cases carefully or use complement.
- Business: conditional cohorts (e.g., users who interacted at least once).

Pattern 7: Odds / Likelihood Ratios (Bayes in Odds Form)
- Meaning: posterior odds = prior odds * likelihood ratio.
- Identify: "odds", "likelihood ratio", "diagnostic test", "calibration".
- Visual: odds table.
- Toolkit:
  - `odds(A|B) = odds(A) * LR`, where `LR = P(B|A)/P(B|A^c)`
- Traps: converting odds/prob incorrectly.
- Strategy: compute odds, update, convert back.
- Business: risk scoring, fraud.

Pattern 8: Conditional Independence / Naive Bayes
- Meaning: combine evidence assuming independence given class.
- Identify: "assume features independent given class".
- Visual: Naive Bayes graph.
- Toolkit: `P(A|x1,x2) ∝ P(A) Π P(xi|A)`.
- Traps: assuming marginal independence instead of conditional independence.
- Strategy: compute unnormalized posteriors then normalize.
- Business: simple classifiers, ranking signals.

Pattern 9: Selection Bias / Conditioning on a Collider (Interview Trap)
- Meaning: conditioning on an event affected by both A and B can induce dependence.
- Identify: "only among those who were selected/observed", "post-treatment conditioning".
- Visual: causal DAG with a collider.
- Toolkit: reasoning, not a single formula; watch `P(A|selected)` vs `P(A)`.
- Traps: concluding causality from conditioned correlations; triggered analysis pitfalls.
- Strategy:
  1. Ask what the condition depends on.
  2. Check if conditioning creates bias.
- Business: experiment analysis only among clickers.

Pattern 10: Classic Puzzles (Monty Hall, Two Children, etc.)
- Meaning: the host/statement reveals information; update with conditional probability.
- Identify: "given that", "revealed", "host opens a door", "at least one is...".
- Visual: case enumeration tree.
- Toolkit: Bayes or careful conditioning.
- Traps: treating reveals as random when they’re conditional.
- Strategy: model the reveal process explicitly.
- Business: sanity check for modeling assumptions.

========================================
SECTION 5 — UNIVERSAL STEP-BY-STEP SOLVING FRAMEWORK
========================================

1) Decode the question
- Identify what is known (the condition) and what is asked (target probability).

2) Define events/variables precisely
- Use symbols: A = target, B = condition, H_i = hypotheses/segments.

3) Pick a diagram
- Venn (overlap), 2x2 table, probability tree (sequences/mixtures), or case list (puzzles).

4) Select the formula logically
- Direct conditional: `P(A|B)=P(A∩B)/P(B)`
- Bayes: if given `P(B|A)` and priors
- Total probability: if mixture/segments
- Chain rule: if multi-step

5) Compute in a stable order
- Compute denominators first (`P(B)`), then numerators (`P(A∩B)`), then divide.

6) Sanity check
- Is the answer between 0 and 1?
- Does it move in the right direction with base rates/sensitivity?
- Extreme cases: if base rate → 0, posterior should be small unless evidence is near-perfect.

7) Interview explanation template
- "Let A be ..., B be .... We want `P(A|B)`. I’ll compute `P(B)` via total probability and then apply Bayes/direct conditional. Finally I’ll sanity check with base rates."

========================================
SECTION 6 — DOMAIN-DIVERSE QUESTION BANK (MINIMUM 25)
========================================

Q1 (Easy) Pattern: Direct Conditional
- Tests: denominator discipline, overlap vs condition
- Relevance: funnels, segment metrics

Q2 (Easy) Pattern: Contingency Table (Precision)
- Tests: confusion-matrix probability
- Relevance: moderation queues, alerts

Q3 (Medium) Pattern: Bayes Inversion (Medical Test)
- Tests: base-rate reasoning
- Relevance: fraud/rare-event DS

Q4 (Medium) Pattern: Total Probability (Mixture + Bayes)
- Tests: partition, Bayes flip
- Relevance: multi-source pipelines

Q5 (Medium) Pattern: Sequential Draws (Without Replacement)
- Tests: chain rule with dependence
- Relevance: sampling reasoning

Q6 (Medium) Pattern: Complement Conditioning ("at least one")
- Tests: case enumeration, complement
- Relevance: cohort definition

Q7 (Easy) Pattern: Independence Check
- Tests: independence vs conditional
- Relevance: modeling assumptions

Q8 (Hard) Pattern: Monty Hall (Reveal Process)
- Tests: modeling of information
- Relevance: reasoning rigor

Q9 (Medium) Pattern: Funnel Conditional Rate
- Tests: conditional conversion math
- Relevance: product analytics

Q10 (Medium) Pattern: Fraud Base Rate + Alert
- Tests: Bayes with rare prevalence
- Relevance: trust & safety

Q11 (Medium) Pattern: A/B Triggered Analysis Trap (Collider)
- Tests: selection bias concept
- Relevance: experimentation rigor

Q12 (Medium) Pattern: Two Tests (Bayes sequential evidence)
- Tests: updating with multiple signals
- Relevance: risk scoring

Q13 (Easy) Pattern: Finance (Late payment -> default)
- Tests: conditional rate interpretation
- Relevance: risk analytics

Q14 (Medium) Pattern: Marketing channel mixture
- Tests: weighted averages
- Relevance: attribution/funnels

Q15 (Easy) Pattern: User retention conditional
- Tests: cohort conditioning
- Relevance: growth analytics

Q16 (Medium) Pattern: Dice given sum
- Tests: conditional sample space
- Relevance: classic screen

Q17 (Medium) Pattern: Cards given at least one ace
- Tests: complement/case enumeration
- Relevance: probability screen

Q18 (Medium) Pattern: Factory defects (Bayes)
- Tests: Bayes + total probability
- Relevance: quality analytics

Q19 (Hard) Pattern: Two children (information protocol)
- Tests: subtle conditioning
- Relevance: puzzle rigor

Q20 (Medium) Pattern: Continuous uniform (conditional interval)
- Tests: conditional on subrange
- Relevance: distribution intuition

Q21 (Medium) Pattern: ML score threshold -> class probability
- Tests: conditional interpretation
- Relevance: calibration thinking

Q22 (Medium) Pattern: Naive Bayes (conditional independence)
- Tests: combine evidence
- Relevance: simple ML interview

Q23 (Easy) Pattern: Healthcare improvement conditional
- Tests: conditional fraction
- Relevance: analysis framing

Q24 (Hard) Pattern: Posterior odds / likelihood ratio
- Tests: odds update
- Relevance: risk/ranking systems

Q25 (Medium) Pattern: Multi-step journey chain rule
- Tests: chain rule across steps
- Relevance: funnel decomposition

========================================
SECTION 7 — FULL STEP-BY-STEP SOLUTIONS (FOR ALL QUESTIONS)
========================================

Q1
1) Interpretation: Among users who saw an ad (B), what fraction purchased (A)?
2) Define: A=purchase, B=saw ad.
3) Pattern: Direct conditional.
4) Diagram: 2x2 table.
5) Formula reasoning: `P(A|B)=P(A∩B)/P(B)`.
6) Calculation: If 1,000 saw ad and 120 of them purchased, `P(A|B)=120/1000=0.12`.
7) Sanity: between 0 and 1; plausible.
8) Answer: 0.12

Q2
1) Interpretation: Probability email is spam given it was flagged by model.
2) Define: Y=spam, Ŷ=flagged.
3) Pattern: Contingency table (precision).
4) Diagram: confusion matrix.
5) Formula: `P(Y=1|Ŷ=1)=TP/(TP+FP)`.
6) Calculation: Suppose TP=90, FP=10. Precision=90/(90+10)=0.9.
7) Sanity: high precision means most flagged are truly spam.
8) Answer: 0.90

Q3
1) Interpretation: Probability patient has disease given positive test.
2) Define: D=disease, +=positive.
3) Pattern: Bayes inversion.
4) Diagram: tree on D vs not D then +/−.
5) Formula: `P(D|+)=P(+|D)P(D)/P(+)`.
6) Calculation: Let prevalence `P(D)=0.01`, sensitivity `P(+|D)=0.99`, specificity `P(-|~D)=0.95` so `P(+|~D)=0.05`.
   - `P(+)=0.99*0.01+0.05*0.99=0.0099+0.0495=0.0594`
   - `P(D|+)=0.0099/0.0594≈0.1667`
7) Sanity: despite strong test, rare disease keeps posterior modest.
8) Answer: ≈ 0.167

Q4
1) Interpretation: Probability a ticket came from system A given it was escalated.
2) Define: H=A-source, E=escalated.
3) Pattern: Total probability + Bayes.
4) Diagram: branches A vs B.
5) Formula: `P(A|E)=P(E|A)P(A)/[P(E|A)P(A)+P(E|B)P(B)]`.
6) Calculation: Suppose 60% from A, 40% from B. Escalation rates: 10% for A, 20% for B.
   - `P(A|E)=0.10*0.60/(0.10*0.60+0.20*0.40)=0.06/(0.06+0.08)=0.4286`
7) Sanity: escalations more likely from B, so posterior < prior (0.6).
8) Answer: ≈ 0.429

Q5
1) Interpretation: Probability second draw is red given first draw was red (without replacement).
2) Define: R1=first red, R2=second red.
3) Pattern: Sequential draws / conditional.
4) Diagram: tree with first draw then second.
5) Formula: `P(R2|R1)`.
6) Calculation: Urn has 5 red, 3 blue (8 total). Given first was red, remaining: 4 red, 3 blue (7 total).
   - `P(R2|R1)=4/7≈0.5714`
7) Sanity: slightly less than 5/8=0.625 due to removal.
8) Answer: ≈ 0.571

Q6
1) Interpretation: Two fair dice rolled. Probability at least one is a 6 given the sum is 8.
2) Define: A=at least one 6, B=sum=8.
3) Pattern: Conditional sample space.
4) Diagram: enumerate outcomes with sum 8.
5) Formula: `P(A|B)=|A∩B|/|B|` (equiprobable outcomes).
6) Calculation: Sum 8 outcomes: (2,6),(3,5),(4,4),(5,3),(6,2) => 5 outcomes.
   - Those with at least one 6: (2,6),(6,2) => 2 outcomes.
   - `P=2/5=0.4`
7) Sanity: plausible.
8) Answer: 0.4

Q7
1) Interpretation: If events A and B are independent with `P(A)=0.3`, does `P(A|B)` equal 0.3?
2) Define: independence.
3) Pattern: Independence.
4) Diagram: none.
5) Formula: if independent, `P(A|B)=P(A)`.
6) Calculation: `P(A|B)=0.3`.
7) Sanity: matches definition.
8) Answer: 0.3

Q8
1) Interpretation: Monty Hall. You pick 1 of 3 doors, host opens a goat door, offers switch. Probability you win if you switch.
2) Define: W=win, S=switch.
3) Pattern: Reveal process / Bayes reasoning.
4) Diagram: cases where car behind chosen door vs not.
5) Formula: reasoning by cases.
6) Calculation: Initially P(car behind your door)=1/3. Host action doesn’t change that. If you switch, you win when initial pick was wrong (2/3).
7) Sanity: classic result.
8) Answer: 2/3

Q9
1) Interpretation: Purchase given add-to-cart.
2) Define: A=purchase, C=add_to_cart.
3) Pattern: Funnel conditional.
4) Diagram: funnel.
5) Formula: `P(A|C)`.
6) Calculation: If 500 add-to-cart and 200 purchase, `P=200/500=0.4`.
7) Sanity: fine.
8) Answer: 0.4

Q10
1) Interpretation: Fraud probability given alert.
2) Define: F=fraud, A=alert.
3) Pattern: Bayes base-rate.
4) Diagram: tree.
5) Formula: Bayes with total probability.
6) Calculation: Suppose `P(F)=0.001`, `P(A|F)=0.95`, `P(A|~F)=0.02`.
   - `P(A)=0.95*0.001+0.02*0.999=0.00095+0.01998=0.02093`
   - `P(F|A)=0.00095/0.02093≈0.0454`
7) Sanity: even good detector yields low posterior when base rate is tiny.
8) Answer: ≈ 0.045

Q11
1) Interpretation: In an A/B test, you compute conversion rate only among users who clicked (post-treatment). Is that unbiased for treatment effect?
2) Define: T=treatment assignment, C=click, Y=conversion.
3) Pattern: Collider/selection bias.
4) Diagram: DAG `T -> C <- U -> Y` (simplified).
5) Formula reasoning: conditioning on C can induce dependence between T and unobserved factors; not generally unbiased.
6) Calculation: Not numeric; reasoning-based.
7) Sanity: triggered analysis can flip conclusions.
8) Answer: No; conditioning on a post-treatment variable (click) can bias estimates.

Q12
1) Interpretation: Disease posterior after two independent tests, both positive.
2) Define: D, +1, +2.
3) Pattern: Bayes with multiple evidence.
4) Diagram: tree or odds update.
5) Formula: `P(D|+,+) ∝ P(D)P(+|D)^2`, similarly for `~D`.
6) Calculation: `P(D)=0.01`, sensitivity 0.99, specificity 0.95 => `P(+|~D)=0.05`.
   - Unnormalized: D: `0.01*0.99^2=0.01*0.9801=0.009801`
   - ~D: `0.99*0.05^2=0.99*0.0025=0.002475`
   - Normalize: `0.009801/(0.009801+0.002475)=0.7984`
7) Sanity: two positives strongly increase posterior.
8) Answer: ≈ 0.798

Q13
1) Interpretation: Probability of default given 60+ days late.
2) Define: D=default, L=late.
3) Pattern: Direct conditional from portfolio data.
4) Diagram: table.
5) Formula: `P(D|L)=defaults among late / late total`.
6) Calculation: If 300 of 1,000 late accounts default, `P=0.3`.
7) Sanity: high but plausible.
8) Answer: 0.3

Q14
1) Interpretation: Overall conversion rate across channels.
2) Define: H=channel, C=convert.
3) Pattern: total probability mixture.
4) Diagram: tree by channel.
5) Formula: `P(C)=Σ P(C|H)P(H)`.
6) Calculation: 70% organic with 5% conversion, 30% paid with 2% conversion:
   - `P(C)=0.05*0.70+0.02*0.30=0.035+0.006=0.041`
7) Sanity: between 2% and 5%.
8) Answer: 0.041

Q15
1) Interpretation: Probability user is active in week 2 given active in week 1.
2) Define: W1, W2.
3) Pattern: retention conditional.
4) Diagram: cohort.
5) Formula: `P(W2|W1)=count(W1∩W2)/count(W1)`.
6) Calculation: If 8,000 active in W1 and 5,600 active in both, rate=0.7.
7) Sanity: plausible.
8) Answer: 0.7

Q16
1) Interpretation: Probability first die is 6 given sum is 7.
2) Define: A=die1=6, B=sum=7.
3) Pattern: conditional sample space.
4) Diagram: enumerate sum=7 outcomes.
5) Formula: `|A∩B|/|B|`.
6) Calculation: Sum 7 outcomes: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) => 6.
   - A∩B is (6,1) => 1.
   - Prob = 1/6 ≈ 0.1667.
7) Sanity: fine.
8) Answer: 1/6

Q17
1) Interpretation: Two cards drawn without replacement. Probability both are aces given at least one is an ace.
2) Define: A=both aces, B=at least one ace.
3) Pattern: at least one / complement.
4) Diagram: case ratio.
5) Formula: `P(A|B)=P(A)/P(B)` since A implies B.
6) Calculation: Standard deck, 4 aces, 52 cards.
   - `P(A)= (4/52)*(3/51)=12/2652=1/221`
   - `P(B)=1-P(no ace)=1- (48/52)*(47/51)=1- (2256/2652)=396/2652=33/221`
   - `P(A|B)=(1/221)/(33/221)=1/33≈0.0303`
7) Sanity: small.
8) Answer: 1/33

Q18
1) Interpretation: Probability a product came from Factory A given it’s defective.
2) Define: H=A, D=defective.
3) Pattern: Bayes.
4) Diagram: tree A/B then defect.
5) Formula: Bayes with total probability.
6) Calculation: A makes 40% with 3% defect; B makes 60% with 1% defect.
   - `P(D)=0.03*0.40+0.01*0.60=0.012+0.006=0.018`
   - `P(A|D)=0.012/0.018=2/3≈0.6667`
7) Sanity: defects overrepresent A.
8) Answer: 2/3

Q19
1) Interpretation: Two children puzzle: "At least one is a boy." Probability both are boys (assuming equally likely sexes, independent).
2) Define: B=boy, sample space for two children.
3) Pattern: information protocol (at least one).
4) Diagram: enumerate cases excluding (G,G).
5) Formula: conditional on event.
6) Calculation: Possible: (B,B),(B,G),(G,B),(G,G). Condition excludes (G,G).
   - Remaining 3 equally likely cases: (B,B),(B,G),(G,B). Only 1 is both boys.
   - Probability = 1/3.
7) Sanity: between 1/4 and 1/2.
8) Answer: 1/3

Q20
1) Interpretation: X ~ Uniform(0,1). Compute P(X > 0.7 | X > 0.4).
2) Define: A={X>0.7}, B={X>0.4}.
3) Pattern: direct conditional on interval.
4) Diagram: number line.
5) Formula: `P(A|B)=P(A)/P(B)` since A subset of B.
6) Calculation: `P(X>0.7)=0.3`, `P(X>0.4)=0.6`, ratio=0.3/0.6=0.5.
7) Sanity: should be 0.5 because interval lengths.
8) Answer: 0.5

Q21
1) Interpretation: P(Y=1 | score>t) from evaluation data.
2) Define: Y=positive, S=score>t.
3) Pattern: contingency table.
4) Diagram: thresholded confusion matrix.
5) Formula: `P(Y=1|S)=positives among selected / selected total` (precision at threshold).
6) Calculation: Suppose among 1,000 with score>t, 700 are truly positive. Then probability=0.7.
7) Sanity: ok.
8) Answer: 0.7

Q22
1) Interpretation: Naive Bayes with two binary features x1,x2 and class C∈{0,1}. Compute P(C=1|x1=1,x2=1).
2) Define: C, x1, x2.
3) Pattern: Naive Bayes.
4) Diagram: NB graph.
5) Formula: `P(C=1|x) ∝ P(C=1)P(x1|C=1)P(x2|C=1)`.
6) Calculation: Let `P(C=1)=0.2`, `P(x1=1|C=1)=0.8`, `P(x2=1|C=1)=0.7`,
   `P(x1=1|C=0)=0.1`, `P(x2=1|C=0)=0.2`.
   - Unnorm1 = 0.2*0.8*0.7 = 0.112
   - Unnorm0 = 0.8*0.1*0.2 = 0.016
   - Normalize: 0.112/(0.112+0.016)=0.875
7) Sanity: strong evidence for class 1.
8) Answer: 0.875

Q23
1) Interpretation: Among patients who completed therapy (B), probability their score improved (A).
2) Define: A=improved, B=completed.
3) Pattern: direct conditional from cohort.
4) Diagram: table.
5) Formula: `P(A|B)=improved&completed / completed`.
6) Calculation: If 180/300 completed improved => 0.6.
7) Sanity: ok.
8) Answer: 0.6

Q24
1) Interpretation: Posterior probability using likelihood ratio.
2) Define: A=fraud, B=signal observed.
3) Pattern: odds / likelihood ratio.
4) Diagram: odds update.
5) Formula: `odds(A|B)=odds(A)*LR`, `LR=P(B|A)/P(B|~A)`.
6) Calculation: Prior `P(A)=0.01` => odds=0.01/0.99=0.010101.
   - Suppose `P(B|A)=0.6`, `P(B|~A)=0.1` => LR=6.
   - Posterior odds = 0.010101*6=0.060606.
   - Convert: `P=odds/(1+odds)=0.060606/1.060606≈0.0571`.
7) Sanity: increases from 1% to ~5.7%.
8) Answer: ≈ 0.057

Q25
1) Interpretation: Multi-step journey: probability a user purchases given they were exposed to an impression.
2) Define: I=impression, K=click, C=checkout, P=purchase.
3) Pattern: chain rule decomposition.
4) Diagram: funnel chain.
5) Formula: `P(P|I)=P(K|I)*P(C|K)*P(P|C)` (assuming the funnel sequence).
6) Calculation: If `P(K|I)=0.04`, `P(C|K)=0.25`, `P(P|C)=0.6`:
   - `P(P|I)=0.04*0.25*0.6=0.006`
7) Sanity: 0.6% purchase per impression, plausible.
8) Answer: 0.006

========================================
SECTION 8 — BUSINESS & INTERVIEW EXPLANATION (CRITICAL)
========================================

For each question Q1–Q25:

Q1
- PM explanation: "Among people who saw the ad, 12% purchased; that’s the ad-exposed conversion rate."
- Interview explanation: "Define A=purchase, B=exposure. Use `P(A|B)=count(A∩B)/count(B)`."
- Executive summary: "Conditional conversion rate is 12%."

Q2
- PM explanation: "When we flag an email, 90% are actually spam; that’s precision."
- Interview explanation: "Compute `P(spam|flagged)=TP/(TP+FP)` from the confusion matrix."
- Executive summary: "Precision is 0.90."

Q3
- PM explanation: "Even with a good test, because the disease is rare, only ~16.7% of positives truly have it."
- Interview explanation: "Use Bayes with prevalence + sensitivity/specificity to compute `P(D|+)`."
- Executive summary: "Posterior after one positive is ~0.167."

Q4
- PM explanation: "Escalated tickets are more likely from system B, so only ~43% of escalations come from A."
- Interview explanation: "Use total probability for `P(E)`, then Bayes for `P(A|E)`."
- Executive summary: "`P(A|escalated)≈0.429`."

Q5
- PM explanation: "If you already saw a red, the next draw is slightly less likely to be red due to depletion."
- Interview explanation: "Condition on the first draw and update remaining counts."
- Executive summary: "`P(R2|R1)=4/7`."

Q6
- PM explanation: "Given the sum is fixed, we restrict to the five equally likely sum=8 outcomes; 2 include a 6."
- Interview explanation: "Enumerate conditioned sample space then count favorable outcomes."
- Executive summary: "`P(at least one 6 | sum=8)=0.4`."

Q7
- PM explanation: "Independence means knowing B doesn’t change the chance of A."
- Interview explanation: "By definition, independence implies `P(A|B)=P(A)`."
- Executive summary: "Still 0.3."

Q8
- PM explanation: "Switching wins whenever your first pick was wrong, which happens 2/3 of the time."
- Interview explanation: "Model the host’s reveal; switching captures the 2/3 mass."
- Executive summary: "Switching wins with probability 2/3."

Q9
- PM explanation: "Add-to-cart users convert at 40% to purchase; that’s cart-to-purchase."
- Interview explanation: "Conditional conversion rate is `purchases among carts / carts`."
- Executive summary: "`P(purchase|cart)=0.4`."

Q10
- PM explanation: "Even with a strong alert, fraud is rare, so only ~4.5% of alerts are truly fraud."
- Interview explanation: "Bayes with base rate: posterior = (TP rate * prevalence) / alert rate."
- Executive summary: "`P(fraud|alert)≈0.045`."

Q11
- PM explanation: "Looking only at clickers can bias the effect because the treatment changes who clicks."
- Interview explanation: "Conditioning on a post-treatment variable can create selection bias (collider)."
- Executive summary: "Triggered-only conversion is not generally unbiased."

Q12
- PM explanation: "Two positive tests dramatically increase confidence to ~80%."
- Interview explanation: "Assuming conditional independence, multiply likelihoods then normalize."
- Executive summary: "`P(D|+,+)≈0.798`."

Q13
- PM explanation: "30% of 60+ day late accounts default; that’s a conditional risk metric."
- Interview explanation: "Direct conditional from cohort counts."
- Executive summary: "`P(default|late)=0.3`."

Q14
- PM explanation: "Overall conversion is a weighted average across channels: 4.1% here."
- Interview explanation: "Use law of total probability with channel weights."
- Executive summary: "Blended conversion = 0.041."

Q15
- PM explanation: "Week-2 retention among week-1 actives is 70%."
- Interview explanation: "`P(W2|W1)=count(W1∩W2)/count(W1)`."
- Executive summary: "Retention is 0.7."

Q16
- PM explanation: "Given sum 7, each of 6 outcomes is equally likely; only one has first die 6."
- Interview explanation: "Condition on reduced sample space then count."
- Executive summary: "Probability is 1/6."

Q17
- PM explanation: "Among hands with at least one ace, only ~3% have two aces."
- Interview explanation: "Compute `P(two aces)/P(at least one ace)`."
- Executive summary: "Answer is 1/33."

Q18
- PM explanation: "Even though A makes 40% of items, it accounts for ~67% of defects due to higher defect rate."
- Interview explanation: "Bayes on factory given defect."
- Executive summary: "`P(A|defect)=2/3`."

Q19
- PM explanation: "Given at least one boy, we exclude (G,G); 1 of remaining 3 cases is (B,B)."
- Interview explanation: "Be explicit about conditioning statement; enumerate cases."
- Executive summary: "Probability is 1/3."

Q20
- PM explanation: "If you already know X>0.4, the remaining interval is [0.4,1]; half of that is >0.7."
- Interview explanation: "Subset ratio of interval lengths."
- Executive summary: "Answer is 0.5."

Q21
- PM explanation: "Among users above the score threshold, 70% are truly positive."
- Interview explanation: "It’s precision at the threshold: `P(Y=1|score>t)`."
- Executive summary: "Probability is 0.7."

Q22
- PM explanation: "We combine independent signals; both being present makes class 1 very likely (~87.5%)."
- Interview explanation: "Compute unnormalized posteriors via Naive Bayes then normalize."
- Executive summary: "Posterior is 0.875."

Q23
- PM explanation: "60% of completers improved; that’s the conditional improvement rate."
- Interview explanation: "Direct conditional from cohort counts."
- Executive summary: "Answer is 0.6."

Q24
- PM explanation: "This signal multiplies odds by 6, raising risk from 1% to ~5.7%."
- Interview explanation: "Use odds form to update quickly with likelihood ratios."
- Executive summary: "Posterior ≈ 0.057."

Q25
- PM explanation: "Impression-to-purchase is the product of step conversion rates; here 0.6%."
- Interview explanation: "Decompose with chain rule along funnel steps."
- Executive summary: "`P(purchase|impression)=0.006`."

========================================
SECTION 9 — COMMON INTERVIEW TRAPS & EDGE CASES
========================================

Top 10 traps
1) Swapping `P(A|B)` with `P(B|A)`.
2) Ignoring base rates in rare-event settings.
3) Wrong denominator (using total population instead of conditioned cohort).
4) Treating dependent draws as independent.
5) Not modeling the information/reveal process (Monty Hall).
6) Double counting overlapping cases when using "at least one".
7) Confusing precision vs recall.
8) Conditioning on post-treatment variables in experiments.
9) Assuming independence without stating/justifying it.
10) Forgetting to normalize when computing posteriors.

Trick variations
- "Given at least one is a boy born on Tuesday..." (changes conditioning protocol).
- Two-stage sampling: "Pick a random person from those who responded..." (selection bias).
- Multiple tests: "Two positives" vs "at least one positive".

How interviewers try to confuse candidates
- Provide `P(B|A)` and ask for `P(A|B)` without giving priors (you must ask or assume).
- Mix population-level and cohort-level rates.
- Hide that events are not independent (without replacement, conditional exposure).

========================================
SECTION 10 — MASTERY CHECKLIST
========================================

Concepts mastered
- Definition and denominator logic
- Bayes rule and total probability
- Confusion matrix probabilities
- Chain rule / sequential conditioning
- Complement and "at least one" logic
- Odds / likelihood ratio updates
- Conditional independence assumptions
- Selection bias awareness

Patterns mastered
- Direct conditional, Bayes inversion, mixtures, sequential draws, puzzles, collider traps

Interview readiness score
- If you can solve Q1–Q25 quickly and explain tradeoffs: FAANG Ready

Recommended next topic
- `conditional_expectation` (builds directly on conditioning mechanics)
