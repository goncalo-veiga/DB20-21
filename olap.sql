SELECT P.associated_to, DD.month, DD.week_day, SUM(units_replenished)
FROM concerning_products C
JOIN d_product DP
    on C.id_product = DP.id_product
JOIN product P on DP.ean = P.ean
JOIN d_date DD on C.id_date = DD.id_date
GROUP BY P.associated_to, ROLLUP(DD.month, DD.week_day);

SELECT p.associated_to, dd.month, dd.week_day, SUM(units_replenished)
FROM concerning_products c
JOIN d_product dp
    ON c.id_product = dp.id_product
JOIN product p 
    ON dp.ean = p.ean
JOIN d_date dd 
    ON c.id_date = dd.id_date
GROUP BY p.associated_to, CUBE(dd.month, dd.week_day);

SELECT p.associated_to, dd.month, dd.week_day, SUM(units_replenished)
FROM concerning_products c
JOIN d_product dp
    ON c.id_product = dp.id_product
JOIN product p 
    ON dp.ean = p.ean
JOIN d_date dd 
    ON c.id_date = dd.id_date
GROUP BY p.associated_to, GROUPING SETS (dd.month, dd.week_day);