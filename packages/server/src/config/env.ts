import { config } from "dotenv";
import { EnvConfig } from "@/types/env.js";
import process from "process";

config();

export const env: EnvConfig = {
  PORT: Number(process.env.PORT) || 8000,
  HOST:
    process.env.NODE_ENV === "dev"
      ? "localhost"
      : process.env.HOST || "localhost",
  ORIGIN: process.env.ORIGIN || "http://localhost:3000",
  NODE_ENV: (process.env.NODE_ENV || "dev") as "dev" | "prod" | "test",
  DATABASE_URL: process.env.DATABASE_URL || "mongodb://localhost:27017/myapp",
  JWT_SECRET: process.env.JWT_SECRET || "defaultsecret",
};
