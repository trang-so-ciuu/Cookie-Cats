-- SQL Server queries for the validated Cookie Cats experiment dataset.

-- 1. Experiment sample and treatment allocation.
SELECT
    version,
    COUNT(*) AS players,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS player_share_pct
FROM dbo.gaming_data
GROUP BY version
ORDER BY version;

-- 2. Primary retention metrics by treatment.
SELECT
    version,
    COUNT(*) AS players,
    ROUND(100.0 * AVG(CAST(retention_1 AS float)), 2) AS day_1_retention_pct,
    ROUND(100.0 * AVG(CAST(retention_7 AS float)), 2) AS day_7_retention_pct
FROM dbo.gaming_data
GROUP BY version
ORDER BY version;

-- 3. Descriptive progress distribution. Missing rounds remain visible.
WITH player_progress AS (
    SELECT
        userid,
        version,
        retention_1,
        retention_7,
        CASE
            WHEN sum_gamerounds IS NULL THEN 'Missing'
            WHEN sum_gamerounds = 0 THEN '0'
            WHEN sum_gamerounds BETWEEN 1 AND 29 THEN '1-29'
            WHEN sum_gamerounds BETWEEN 30 AND 39 THEN '30-39'
            WHEN sum_gamerounds BETWEEN 40 AND 89 THEN '40-89'
            ELSE '90+'
        END AS rounds_bucket
    FROM dbo.gaming_data
)
SELECT
    rounds_bucket,
    COUNT(*) AS players,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) AS player_share_pct
FROM player_progress
GROUP BY rounds_bucket
ORDER BY
    CASE rounds_bucket
        WHEN '0' THEN 1
        WHEN '1-29' THEN 2
        WHEN '30-39' THEN 3
        WHEN '40-89' THEN 4
        WHEN '90+' THEN 5
        ELSE 6
    END;

-- 4. Descriptive retention by treatment and observed progress.
-- Rounds are measured after treatment, so this is not a causal subgroup estimate.
WITH player_progress AS (
    SELECT
        version,
        retention_1,
        retention_7,
        CASE
            WHEN sum_gamerounds = 0 THEN '0'
            WHEN sum_gamerounds BETWEEN 1 AND 29 THEN '1-29'
            WHEN sum_gamerounds BETWEEN 30 AND 39 THEN '30-39'
            WHEN sum_gamerounds BETWEEN 40 AND 89 THEN '40-89'
            ELSE '90+'
        END AS rounds_bucket
    FROM dbo.gaming_data
    WHERE sum_gamerounds IS NOT NULL
)
SELECT
    rounds_bucket,
    version,
    COUNT(*) AS players,
    ROUND(100.0 * AVG(CAST(retention_1 AS float)), 2) AS day_1_retention_pct,
    ROUND(100.0 * AVG(CAST(retention_7 AS float)), 2) AS day_7_retention_pct
FROM player_progress
GROUP BY rounds_bucket, version
ORDER BY rounds_bucket, version;
