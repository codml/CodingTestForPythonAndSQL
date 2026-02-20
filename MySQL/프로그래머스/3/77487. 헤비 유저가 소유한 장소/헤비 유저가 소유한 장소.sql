SELECT
    DISTINCT
    ID,
    NAME,
    HOST_ID
FROM
    PLACES A
WHERE
    HOST_ID IN
    (SELECT
        HOST_ID
    FROM
        PLACES B
    WHERE
        A.ID != B.ID)
ORDER BY
    ID