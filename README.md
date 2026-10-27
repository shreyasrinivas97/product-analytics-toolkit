# Product Feedback & Feature Prioritization Toolkit
**Portfolio project for a Product Management Intern role**

## Project summary
This portfolio case study demonstrates a practical product workflow: synthesize user feedback, identify user pain points, prioritize candidate features, draft a lightweight PRD, define success metrics, evaluate an A/B test, and prepare QA/UAT scenarios.

**Important:** all datasets in `data/` are synthetic and created for demonstration. Competitor scan entries are illustrative patterns, not verified claims about named companies. Do not present the findings as real company/user research.

## Business problem
A hypothetical consumer application receives feedback across onboarding, search, performance, notifications, payments, and content discovery. The product team needs a repeatable way to turn unstructured feedback into prioritized, measurable product work.

## What is included
- `data/user_feedback.csv` — 600 synthetic feedback records
- `data/ab_experiment.csv` — 1,200 synthetic users in a control/treatment experiment
- `data/competitor_scan.csv` — illustrative competitor-pattern comparison template
- `data/feature_prioritization.csv` — impact/confidence/effort scoring
- `sql/product_analytics_queries.sql` — queries for feedback themes, sentiment, segments, and experiment metrics
- `src/analyze_product_data.py` — Python analysis script using pandas and NumPy
- `docs/Product_Requirements_Document.docx` and `.md` — lightweight PRD
- `docs/User_Stories_and_Acceptance_Criteria.md` — backlog-ready stories
- `docs/Experiment_Plan_and_Readout.md` — experiment design and interpretation guardrails
- `docs/QA_UAT_Test_Cases.csv` — test cases and expected outcomes
- `docs/Product_Case_Study_Summary.md` — findings and portfolio presentation outline
- `Product_Analytics_Dashboard.xlsx` — workbook with KPI summary, source data, feature scoring and charts

## How to use
1. Open `Product_Analytics_Dashboard.xlsx` and review `Executive Summary`, `Feedback Data`, `A-B Test`, and `Prioritization`.
2. Install dependencies: `pip install pandas numpy`
3. From the project folder run: `python src/analyze_product_data.py`
4. Run the SQL in `sql/product_analytics_queries.sql` after importing the CSVs into tables named `user_feedback`, `ab_experiment`, and `feature_prioritization`.
5. Read the PRD and case study summary before discussing the project in an interview.

## Product process demonstrated
1. Define the user problem and target segment.
2. Quantify feedback themes and satisfaction.
3. Prioritize features using user impact, business impact, confidence, and effort.
4. Specify an MVP with user stories and acceptance criteria.
5. Define a measurable experiment and guardrails.
6. Prepare QA/UAT cases and post-launch metrics.

## Resume integrity
Use wording such as “Built a portfolio case study using synthetic data...” unless you later validate it with real users or deploy a working product. Never describe synthetic findings as actual customer research or claim that a live A/B test was run.
