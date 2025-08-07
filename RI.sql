CREATE OR REPLACE FUNCTION new_secondary_suppliers()
RETURNS trigger
AS
$$
DECLARE ss_count INTEGER;
BEGIN
    SELECT COUNT(ss.ean) INTO ss_count
    FROM product p
    JOIN supplies_sec ss on p.ean = ss.ean
        WHERE ss.ean = NEW.ean;

    IF ss_count = 3
        THEN RAISE EXCEPTION 'Secondary supplier limit achieved on this product';
    END IF;

    RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_secondary_supplier
BEFORE INSERT ON supplies_sec
FOR EACH ROW
EXECUTE PROCEDURE new_secondary_suppliers();

CREATE OR REPLACE FUNCTION new_supplier()
RETURNS trigger
AS
$$
    DECLARE total_participation INTEGER;
BEGIN
    SELECT COUNT(*) INTO total_participation
    FROM (SELECT sp.ean
    FROM supplier s
    JOIN supplies_prim sp
    ON sp.nif = s.nif
    WHERE sp.ean = NEW.ean
    AND sp.nif = NEW.nif

    UNION

    SELECT sc.ean
    FROM supplier s
    JOIN supplies_sec sc
    ON s.nif = sc.nif
    WHERE sc.ean = NEW.ean
    AND sc.nif = NEW.nif) primary_secondary;

    IF total_participation = 1
        THEN RAISE EXCEPTION 'Supplier already supplies this product';
    END IF;

    RETURN NEW;
END
$$ LANGUAGE plpgsql;

CREATE TRIGGER already_supplying
BEFORE INSERT ON supplies_sec
FOR EACH ROW
EXECUTE PROCEDURE new_supplier();

CREATE TRIGGER already_supplying
BEFORE INSERT ON supplies_prim
FOR EACH ROW
EXECUTE PROCEDURE new_supplier();
