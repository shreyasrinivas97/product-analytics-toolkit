# Experiment Plan and Readout
## Hypothesis
A simplified guided experience can improve the rate at which eligible users complete a meaningful action. The supplied synthetic A/B dataset is only a demonstration of analysis workflow; it is not evidence that the proposed onboarding feature works.

## Design
- **Control:** existing experience.
- **Treatment:** proposed guided onboarding concept.
- **Randomization unit:** user.
- **Primary metric:** conversion to a predefined meaningful action.
- **Secondary metric:** session duration (interpret cautiously; longer is not always better).
- **Guardrails:** crash/error rate, latency, support contacts, and opt-out/dismissal.
- **Analysis:** compare conversion rates, absolute percentage-point lift, relative lift, confidence interval, and significance using a preselected test.
- **Before launch:** calculate sample size using baseline conversion, minimum detectable effect, alpha, and power; define duration and stopping rules.

## Readout template
1. Experiment dates and eligible population
2. Assignment and sample-ratio checks
3. Primary metric: control rate, treatment rate, absolute lift, relative lift, confidence interval, p-value
4. Secondary metrics and segment cuts (pre-specified)
5. Guardrail results
6. Data quality issues and caveats
7. Decision: ship / iterate / stop, with rationale

## Synthetic sample readout
Run `python src/analyze_product_data.py` to calculate the results from `data/ab_experiment.csv`. Report the output as a **synthetic demonstration**. Do not state statistical significance without checking assumptions and an appropriate test; do not generalize to a real product population.
