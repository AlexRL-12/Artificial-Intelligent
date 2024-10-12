-- Active: 1728745940946@@127.0.0.1@5433@facial_recognition
CREATE TABLE "house" (
  "id" serial PRIMARY KEY NOT NULL,
  "address" varchar NOT NULL
);

CREATE TABLE "user" (
  "id" serial PRIMARY KEY NOT NULL,
  "name" varchar NOT NULL,
  "username" varchar NOT NULL,
  "password" varchar NOT NULL,
  "file_path" varchar NOT NULL,
  "house_id" int NOT NULL,
  "created_at" TIMESTAMP DEFAULT now()
);

CREATE TABLE "entrance" (
  "id" serial PRIMARY KEY NOT NULL,
  "user_id" integer,
  "date" timestamp NOT NULL DEFAULT now(),
  "file_path" varchar NOT NULL,
  "allowed" boolean
);

ALTER TABLE "user" ADD FOREIGN KEY ("house_id") REFERENCES "house" ("id");

ALTER TABLE "entrance" ADD FOREIGN KEY ("user_id") REFERENCES "user" ("id");
