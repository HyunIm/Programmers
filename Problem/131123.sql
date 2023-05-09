SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
FROM (
    SELECT FOOD_TYPE, REST_ID, REST_NAME, FAVORITES,
        RANK () OVER (PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS `FOOD_TYPE_RANK`
    FROM REST_INFO RI
) RI
WHERE FOOD_TYPE_RANK = 1
ORDER BY FOOD_TYPE DESC
;
