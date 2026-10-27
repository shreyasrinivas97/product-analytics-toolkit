-- Product feedback analysis (SQLite / PostgreSQL-compatible with minor date syntax changes)
-- 1. Feedback volume and average satisfaction by theme
SELECT theme,
       COUNT(*) AS feedback_count,
       ROUND(AVG(satisfaction_score_1_to_5), 2) AS avg_satisfaction
FROM user_feedback
GROUP BY theme
ORDER BY feedback_count DESC;

-- 2. Negative feedback rate by theme
SELECT theme,
       COUNT(*) AS total_feedback,
       SUM(CASE WHEN sentiment = 'Negative' THEN 1 ELSE 0 END) AS negative_feedback,
       ROUND(100.0 * SUM(CASE WHEN sentiment = 'Negative' THEN 1 ELSE 0 END) / COUNT(*), 1) AS negative_rate_pct
FROM user_feedback
GROUP BY theme
ORDER BY negative_rate_pct DESC;

-- 3. Satisfaction by user segment
SELECT user_segment,
       COUNT(*) AS responses,
       ROUND(AVG(satisfaction_score_1_to_5), 2) AS avg_satisfaction
FROM user_feedback
GROUP BY user_segment
ORDER BY avg_satisfaction ASC;

-- 4. A/B experiment conversion rate by variant
SELECT variant,
       COUNT(*) AS users,
       SUM(converted) AS conversions,
       ROUND(100.0 * AVG(converted), 2) AS conversion_rate_pct,
       ROUND(AVG(session_duration_seconds), 1) AS avg_session_seconds
FROM ab_experiment
GROUP BY variant;

-- 5. Feature prioritization table (precomputed score)
SELECT feature, user_impact_1_to_5, business_impact_1_to_5,
       confidence_1_to_5, effort_1_to_5, priority_score
FROM feature_prioritization
ORDER BY priority_score DESC;
