export interface EnvConfig {
  PORT: number;
  HOST: string;
  NODE_ENV: "dev" | "prod" | "test";
  ORIGIN: string;
  DATABASE_URL: string;
  JWT_SECRET: string;
}
