DROP TABLE IF EXISTS test_input;
CREATE TABLE test_input
(
  id serial NOT NULL,
  firstname VARCHAR(20),
  lastname VARCHAR(20),
  CONSTRAINT test_input_pkey PRIMARY KEY (id)
);
COMMIT;
