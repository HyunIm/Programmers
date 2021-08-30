WITH TEMP AS
(
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME='Yogurt'
)

SELECT DISTINCT CART_ID
FROM CART_PRODUCTS C
INNER JOIN TEMP T
USING (CART_ID)
WHERE NAME='Milk'
ORDER BY CART_ID;