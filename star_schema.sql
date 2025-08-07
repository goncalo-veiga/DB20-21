DROP TABLE IF EXISTS d_date CASCADE;
DROP TABLE IF EXISTS d_product CASCADE;
DROP TABLE IF EXISTS concerning_products CASCADE;


CREATE TABLE d_date (
    id_date INTEGER,
    day INTEGER NOT NULL,
    week_day VARCHAR(9) NOT NULL,
    week INTEGER NOT NULL,
    month VARCHAR(9) NOT NULL,
    year INTEGER NOT NULL,
    PRIMARY KEY(id_date)
);

CREATE TABLE d_product (
    id_product SERIAL NOT NULL,
    ean NUMERIC(13) NOT NULL,
    category VARCHAR(80) NOT NULL,
    PRIMARY KEY(id_product),
    FOREIGN KEY(ean) REFERENCES product(ean),
    FOREIGN KEY(category) REFERENCES category(name)
);

CREATE TABLE concerning_products(
    id_date INTEGER,
    id_product INTEGER,
    units_replenished INTEGER
);