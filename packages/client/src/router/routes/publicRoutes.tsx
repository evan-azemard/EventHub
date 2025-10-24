import { Route } from "react-router-dom";
import * as Pages from "@pages";

export const publicRoutes = (
  <>
    <Route path="/" element={<Pages.Accueil />} />
    <Route path="/test" element={<Pages.Test />} />
  </>
);
