-------------------------
-- BD Project 2 SQL code
-- Pedro Carmine 95493
-- Diogo Baptista 96733
-- Goncalo Veiga 96738
-------------------------
--CREATE SCHEMA IF NOT EXISTS supermarket_mgmt;
--SET SEARCH_PATH TO supermarket_mgmt;

DROP TABLE IF EXISTS replenish_event CASCADE;
DROP TABLE IF EXISTS planogram CASCADE;
DROP TABLE IF EXISTS displayed_in CASCADE;
DROP TABLE IF EXISTS consists_of CASCADE;
DROP TABLE IF EXISTS shelf CASCADE;
DROP TABLE IF EXISTS corridor CASCADE;
DROP TABLE IF EXISTS supermarket CASCADE;
DROP TABLE IF EXISTS simple_category CASCADE;
DROP TABLE IF EXISTS super_category CASCADE;
DROP TABLE IF EXISTS category CASCADE;
DROP TABLE IF EXISTS supplies_prim CASCADE;
DROP TABLE IF EXISTS supplies_sec CASCADE;
DROP TABLE IF EXISTS product CASCADE;
DROP TABLE IF EXISTS supplier CASCADE;

CREATE TABLE supermarket(
    NIF NUMERIC(9),
    name VARCHAR(80) NOT NULL,
    addr VARCHAR(255) NOT NULL,
    PRIMARY KEY(NIF),
    CHECK(LENGTH(NIF::text) = 9)
);

CREATE TABLE corridor(
    NIF NUMERIC(9),
    nr INTEGER,
    width NUMERIC(3,2) NOT NULL,
    PRIMARY KEY(NIF, nr),
    FOREIGN KEY(NIF) REFERENCES supermarket(NIF),
    CHECK(width > 0),
    CHECK(nr > 0)
);

CREATE TABLE shelf(
    NIF NUMERIC(9),
    nr INTEGER,
    side VARCHAR(5),
    height VARCHAR(6),
    PRIMARY KEY(NIF, nr, side, height),
    FOREIGN KEY(NIF, nr) REFERENCES corridor(NIF, nr),
    CHECK(side = 'left' OR side = 'right'),
    CHECK(height = 'floor' OR height = 'upper' OR height = 'middle')
);

CREATE TABLE supplier(
    nif NUMERIC(9),
    name VARCHAR(80) NOT NULL,
    PRIMARY KEY(nif)
    -- Every supplier cannot be simultaneously primary and secondary of the same product
);

CREATE TABLE category(
    name VARCHAR(80),
    PRIMARY KEY(name)
    -- Every category must exist in the table 'displayed_in'
    -- No category can exist at the same time in the table 'super_category' and in the table 'simple_category'
);

CREATE TABLE product(
    ean NUMERIC(13),
    descr VARCHAR(255) NOT NULL,
    associated_to VARCHAR(80) NOT NULL,
    PRIMARY KEY(ean),
    FOREIGN KEY(associated_to) REFERENCES category(name)
    -- A product can only be displayed in the shelf that it is designated to in the table 'planogram'
);

CREATE TABLE supplies_prim(
    nif NUMERIC(9),
    ean NUMERIC(13),
    date DATE NOT NULL,
    PRIMARY KEY(nif, ean),
    FOREIGN KEY(nif) REFERENCES supplier(nif),
    FOREIGN KEY(ean) REFERENCES product(ean),
    CHECK(date <= current_date)
);

CREATE TABLE supplies_sec(
    nif NUMERIC(9),
    ean NUMERIC(13),
    PRIMARY KEY(nif, ean),
    FOREIGN KEY(nif) REFERENCES supplier(nif),
    FOREIGN KEY(ean) REFERENCES product(ean)
    -- For each product (ean) it can only have atmost 3 suppliers
);

CREATE TABLE planogram(
    ean NUMERIC(13),
    NIF NUMERIC(9),
    nr INTEGER,
    side VARCHAR(5),
    height VARCHAR(6),
    facings NUMERIC(3) NOT NULL,
    loc NUMERIC(3) NOT NULL,
    units INTEGER NOT NULL,
    CHECK (units > 0),
    CHECK (loc > 0),
    PRIMARY KEY(ean, NIF, nr, side, height),
    FOREIGN KEY(ean) REFERENCES product(ean),
    FOREIGN KEY(NIF, nr, side, height) REFERENCES shelf(NIF, nr, side, height)
);

CREATE TABLE super_category(
    category_name VARCHAR(80),
    PRIMARY KEY(category_name),
    FOREIGN KEY(category_name) REFERENCES category(name)
    -- Every super_category must exist in the 'consists_of' table
);

CREATE TABLE simple_category(
    category_name VARCHAR(80),
    PRIMARY KEY(category_name),
    FOREIGN KEY(category_name) REFERENCES category(name)
);

CREATE TABLE consists_of(
    super_name VARCHAR(80),
    sub_name VARCHAR(80),
    PRIMARY KEY(super_name, sub_name),
    FOREIGN KEY(sub_name) REFERENCES category(name),
    FOREIGN KEY(super_name) REFERENCES category(name),
    CHECK (sub_name <> super_name)
    -- Categories cannot consist of one another cyclically
);

CREATE TABLE displayed_in(
    name VARCHAR(80),
    NIF NUMERIC(9),
    nr INTEGER,
    side VARCHAR(10),
    height VARCHAR(10),
    PRIMARY KEY(name, NIF, nr, side, height),
    FOREIGN KEY(name) REFERENCES category(name),
    FOREIGN KEY(NIF, nr, side, height) REFERENCES shelf(NIF, nr, side, height)
);

CREATE TABLE replenish_event(
    ean NUMERIC(13),
    NIF NUMERIC(9),
    nr INTEGER,
    side VARCHAR(5),
    height VARCHAR(6),
    instant DATE,
    units INTEGER NOT NULL,
    PRIMARY KEY(ean, NIF, nr, side, height, instant),
    FOREIGN KEY(ean, NIF, nr, side, height) REFERENCES planogram(ean, NIF, nr, side, height),
    CHECK(instant <= CURRENT_DATE),
    CHECK(units > 0)
);
