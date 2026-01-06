-- 코드를 입력하세요
SELECT FLAVOR
FROM
    (
        SELECT FLAVOR, F.TOTAL_ORDER + J.TOTAL_ORDER AS TOT
        FROM FIRST_HALF F JOIN 
            (
                SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
                FROM JULY
                GROUP BY FLAVOR
            ) J USING(FLAVOR)
    ) T
ORDER BY TOT DESC
LIMIT 3