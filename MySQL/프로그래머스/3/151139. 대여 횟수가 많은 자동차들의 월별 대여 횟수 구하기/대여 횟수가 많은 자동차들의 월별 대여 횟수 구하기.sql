WITH ANS AS
(
SELECT
    MONTH(START_DATE) MONTH,
    CAR_ID,
    COUNT(*) RECORDS
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    START_DATE >= STR_TO_DATE("2022-08-01", "%Y-%m-%d")
    AND START_DATE < STR_TO_DATE("2022-11-01", "%Y-%m-%d")
GROUP BY
    CAR_ID, MONTH
)
SELECT
    *
FROM
    ANS A
WHERE
    EXISTS (
        SELECT
            1
        FROM
            ANS B
        WHERE
            A.CAR_ID = B.CAR_ID
        GROUP BY
            B.CAR_ID
        HAVING
            SUM(RECORDS) > 4
    )
ORDER BY
    MONTH,
    CAR_ID DESC