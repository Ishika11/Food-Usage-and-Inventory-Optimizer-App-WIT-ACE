DROP TABLE IF EXISTS "category";

CREATE TABLE "category" (
    "id" INTEGER PRIMARY KEY,
    "name" NVARCHAR(15) NOT NULL,
    "parent_category" NVARCHAR(15) NOT NULL 
);


DROP TABLE IF EXISTS "product";

CREATE TABLE "product" (
    "ID" INTEGER PRIMARY KEY,
    "Item" NVARCHAR(15) NOT NULL,
    "Price" INTEGER,
    "category" NVARCHAR(15) NOT NULL 
);

DROP TABLE IF EXISTS "user";

CREATE TABLE "user" (
    "ID" INTEGER PRIMARY KEY,
    "Item" NVARCHAR(15) NOT NULL,
    "Price" INTEGER,
    "category" NVARCHAR(15) NOT NULL 
);