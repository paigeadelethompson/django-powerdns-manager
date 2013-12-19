-- Set engine to INNODB.
-- Alse see: https://docs.djangoproject.com/en/dev/ref/databases/#creating-your-tables
ALTER TABLE tsigkeys ENGINE=INNODB;

CREATE UNIQUE INDEX namealgoindex ON tsigkeys(name, algorithm);
