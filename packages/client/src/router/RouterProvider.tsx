import { Routes } from "react-router-dom";
import { publicRoutes } from "./routes";

export default function RouterProvider() {
  return <Routes>{publicRoutes}</Routes>;
}
