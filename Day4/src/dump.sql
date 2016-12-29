BEGIN TRANSACTION;
CREATE TABLE PhoneBook (Name text, PhoneNumber text);
INSERT INTO "PhoneBook" VALUES('derick','010-222');
INSERT INTO "PhoneBook" VALUES('tom','010-333');
INSERT INTO "PhoneBook" VALUES('dep','010-444');
COMMIT;
