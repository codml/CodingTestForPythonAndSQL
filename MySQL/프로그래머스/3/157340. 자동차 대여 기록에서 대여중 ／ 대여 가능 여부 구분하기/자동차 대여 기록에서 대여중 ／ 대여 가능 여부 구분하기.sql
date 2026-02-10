SELECT
    CAR_ID,
    MAX(AVAILABILITY)
FROM    
    (SELECT
        *,
        IF (
            START_DATE <= STR_TO_DATE("2022-10-16", "%Y-%m-%d")
            AND STR_TO_DATE("2022-10-16", "%Y-%m-%d") <= END_DATE,
            '대여중',
            '대여 가능'
        ) AVAILABILITY
    FROM
        CAR_RENTAL_COMPANY_RENTAL_HISTORY) C
GROUP BY
    CAR_ID
ORDER BY
    CAR_ID DESC