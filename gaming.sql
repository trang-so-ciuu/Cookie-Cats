--1. Total player
SELECT COUNT(*) AS TotalPlayers
FROM [dbo].[gaming_data]

--2. Phân bố người chơi theo Version
SELECT
    version,
    COUNT(*) AS Players,
    ROUND(
        COUNT(*) * 100.0 /
        SUM(COUNT(*)) OVER(),
        2
    ) AS Percentage
FROM [dbo].[gaming_data]
GROUP BY version;

--3.D1 & D7 Retention theo Version
SELECT
    version,
    ROUND(
        AVG(CAST(retention_1 AS FLOAT))*100,
        2
    ) AS D1_Retention,
    ROUND(
        AVG(CAST(retention_7 AS FLOAT))*100,
        2
    ) AS D7_Retention

FROM [dbo].[gaming_data]
GROUP BY version;

--4. Player Distribution theo Rounds Bucket
WITH PlayerProgress AS (
    SELECT *,
        CASE
            WHEN sum_gamerounds = 0 THEN '0'
            WHEN sum_gamerounds BETWEEN 1 AND 29 THEN '1-29'
            WHEN sum_gamerounds BETWEEN 30 AND 39 THEN '30-39'
            WHEN sum_gamerounds BETWEEN 40 AND 89 THEN '40-89'
            ELSE '90+'
        END AS RoundsBucket
    FROM [dbo].[gaming_data]
)


SELECT pp.RoundsBucket ,COUNT(*) AS Players
FROM [dbo].[gaming_data] as gm , PlayerProgress as pp
where pp.userid = gm.userid
GROUP BY pp.RoundsBucket

-- 5.Retention theo Progress
SELECT pp.RoundsBucket,
    ROUND(AVG(CAST(gm.retention_1 AS FLOAT))*100,2) AS D1_Retention,
    ROUND(AVG(CAST(gm.retention_7 AS FLOAT))*100, 2) AS D7_Retention
FROM [dbo].[gaming_data] as gm , PlayerProgress as pp
where pp.userid = gm.userid
GROUP BY pp.RoundsBucket

--6. Gate30 và Gate40 khác nhau thế nào theo từng Progress Stage?
SELECT pp.RoundsBucket,
        gm.version,
        ROUND( AVG(CAST(gm.retention_1 AS FLOAT))*100, 2) AS D1,
        ROUND( AVG(CAST(gm.retention_7 AS FLOAT))*100,2) AS D7
FROM [dbo].[gaming_data] as gm, PlayerProgress as pp
where pp.userid = gm.userid
GROUP BY pp.RoundsBucket, gm.version;

--7. Người chơi rơi ở đâu?

SELECT pp.RoundsBucket,
        gm.version,
        COUNT(*) AS Installed,
    SUM(gm.retention_1) AS Day1Players,
    SUM(gm.retention_7) AS Day7Players,
    ROUND(AVG(CAST(retention_1 AS FLOAT))*100,2) AS Day1Retention,
    ROUND(AVG(CAST(retention_7 AS FLOAT))*100,2) AS Day7Retention
FROM [dbo].[gaming_data] as gm, PlayerProgress as pp
where pp.userid = gm.userid
GROUP BY pp.RoundsBucket, gm.version;

