-- Exported from QuickDBD: https://www.quickdatatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/WwRpT1
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Gym" (
    "Gym_ID" INTEGER   NOT NULL,
    "Gym_Name" VARCHAR   NOT NULL,
    "Address" VARCHAR   NOT NULL,
    "City" VARCHAR   NOT NULL,
    "Zipcode" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Gym" PRIMARY KEY (
        "Gym_ID"
     )
);

CREATE TABLE "Trainers" (
    "Trainer_ID" INTEGER   NOT NULL,
    "Gym_ID" INTEGER   NOT NULL,
    "First_Name" VARCHAR   NOT NULL,
    "Last_Name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Trainers" PRIMARY KEY (
        "Trainer_ID"
     )
);

CREATE TABLE "Members" (
    "Member_ID" INTEGER   NOT NULL,
    "Gym_ID" INTEGER   NOT NULL,
    "Trainer_ID" INTEGER   NOT NULL,
    "First_Name" VARCHAR   NOT NULL,
    "Last_Name" VARCHAR   NOT NULL,
    "Address" VARCHAR   NOT NULL,
    "CITY" VARCHAR   NOT NULL,
    CONSTRAINT "pk_Members" PRIMARY KEY (
        "Member_ID"
     )
);

CREATE TABLE "Payments" (
    "Payment_ID" INTEGER   NOT NULL,
    "Member_ID" INTEGER   NOT NULL,
    "CreditCard_Info" INTEGER   NOT NULL,
    "Billing_Zip" INTEGER   NOT NULL,
    CONSTRAINT "pk_Payments" PRIMARY KEY (
        "Payment_ID"
     )
);

ALTER TABLE "Trainers" ADD CONSTRAINT "fk_Trainers_Gym_ID" FOREIGN KEY("Gym_ID")
REFERENCES "Gym" ("Gym_ID");

ALTER TABLE "Members" ADD CONSTRAINT "fk_Members_Gym_ID" FOREIGN KEY("Gym_ID")
REFERENCES "Gym" ("Gym_ID");

ALTER TABLE "Members" ADD CONSTRAINT "fk_Members_Trainer_ID" FOREIGN KEY("Trainer_ID")
REFERENCES "Trainers" ("Trainer_ID");

ALTER TABLE "Payments" ADD CONSTRAINT "fk_Payments_Member_ID" FOREIGN KEY("Member_ID")
REFERENCES "Members" ("Member_ID");
