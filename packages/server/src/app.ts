import compression from "compression";
import express from "express";
import cors from "cors";
import { env } from "./config/env";
import cookieParser from "cookie-parser";
import { Request, Response } from "express";

const app = express();
app.use(compression());
app.use(
  cors({
    methods: ["GET", "POST", "PUT", "PATCH", "DELETE"],
    credentials: true,
    origin: env.NODE_ENV === "prod" ? env.ORIGIN : true,
  }),
);

app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/test", (_req: Request, res: Response) => {
  res.json({ message: "API fonctionne correctement" });
});

export default app;
