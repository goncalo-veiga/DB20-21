--A.
SELECT p.ean, p.descr
FROM product p JOIN planogram pl
ON p.ean = pl.ean
JOIN replenish_event r
ON p.ean = r.ean
WHERE r.instant > '2021-03-25'
AND p.associated_to = 'Milk'
AND r.units > 15;

--B. In this query we used the EAN of the product 'Kitkat', DB manager must change the EAN in the query to search other products
SELECT s.name, s.nif
FROM supplier s
JOIN supplies_prim sp
ON sp.nif = s.nif
WHERE sp.ean = '9772328462672'
UNION
SELECT s.name, s.nif
FROM supplier s
JOIN supplies_sec sc
ON s.nif = sc.nif
WHERE sc.ean = '9772328462672';

--C.
SELECT count(*)
FROM consists_of
WHERE super_name = 'Milk';

--D.
SELECT s.name, s.nif
FROM supplier s
NATURAL JOIN(
    SELECT nif, COUNT(*)
    FROM (
        SELECT nif, ean FROM supplies_prim
        UNION
        SELECT nif, ean FROM supplies_sec
         ) u
    GROUP BY nif
    ORDER BY COUNT(*) DESC
    LIMIT 1
) result;

--E.
SELECT s.name, s.nif
FROM supplier s
WHERE s.nif IN (
    SELECT sp.nif
    FROM supplies_prim sp
    JOIN product p ON sp.ean = p.ean
    JOIN category c ON p.associated_to = c.name
    JOIN simple_category sc2 ON c.name = sc2.category_name
    )
AND s.nif IN (
    SELECT ss.nif
    FROM supplies_sec ss
    JOIN product p2 ON p2.ean = ss.ean
    JOIN category c2 ON p2.associated_to = c2.name
    JOIN simple_category sc ON c2.name = sc.category_name
);

--F.
SELECT d.nif, d.nr, d.side, d.height
FROM displayed_in d
JOIN category c
ON d.name = c.name
JOIN product p
ON d.name = p.associated_to
JOIN supplies_prim sp
ON p.ean = sp.ean
WHERE sp.nif NOT IN (
SELECT nif
FROM supplies_sec
);
