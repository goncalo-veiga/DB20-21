CREATE VIEW supplier_stats AS
SELECT total.ean, COUNT(*) total_suppliers
FROM (
    SELECT p.ean, sc.nif 
    FROM
    product p JOIN supplies_sec sc 
        ON p.ean = sc.ean
    UNION
    SELECT p.ean, sp.nif 
    FROM product p JOIN supplies_prim sp 
        ON p.ean = sp.ean) total
GROUP BY total.ean;