import { BrowserRouter } from "react-router-dom";
import RouterProvider from "./router/RouterProvider";

export default function App() {
  return (
    <BrowserRouter>
      <RouterProvider />
    </BrowserRouter>
  );
}
