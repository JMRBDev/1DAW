CREATE TABLE account(
	id int NOT NULL UNIQUE,
	control_code text PRIMARY KEY,
	description text NOT NULL
);

INSERT INTO account(id, control_code, description)
VALUES (1, '1500', 'Inventory'),
	   (2, '4500', 'Sales'),
	   (3, '5500', 'Purchase');
	   
CREATE TABLE inventory_item(
	id serial PRIMARY KEY,
	cogs_account_id int REFERENCES account(id),
	inv_account_id int REFERENCES account(id),
	income_account_id int REFERENCES account(id),
	sku text NOT NULL,
	description text,
	last_cost NUMERIC,
	sell_price NUMERIC NOT NULL,
	active BOOL NOT NULL DEFAULT TRUE);
	
CREATE UNIQUE INDEX inventory_item_sku_idx_u
ON inventory_item (sku) WHERE active IS TRUE;


CREATE FUNCTION markup(inventory_item) RETURNS NUMERIC AS
$$ SELECT CASE WHEN $1.last_cost = 0 THEN NULL
			   ELSE ($1.sell_price - $1.last_cost)
			   		/ $1.last_cost
		  END;
$$ LANGUAGE SQL IMMUTABLE;

SELECT sku, description, i.markup FROM inventory_item i;

SELECT sku, description
FROM inventory_item i
WHERE i.markup < 1.5;

CREATE INDEX inventory_item_markup_idx
ON inventory_item (markup(inventory_item));


CREATE OR REPLACE FUNCTION cogs_account(inventory_item)
RETURNS account
LANGUAGE SQL AS
$$ SELECT * FROM account
WHERE id = $1.cogs_account_id $$;

SELECT (i.cogs_account).* FROM inventory_item i;