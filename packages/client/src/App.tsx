import { BrowserRouter } from "react-router-dom";
import RouterProvider from "./router/RouterProvider";
import { QueryClientProvider, QueryClient } from "@tanstack/react-query";

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      // staleTime: temps pendant lequel les données sont considérées fraîches
      staleTime: 1000 * 60 * 5, // 5 minutes

      // Si aucun composant n'utilise les données pendant ce temps, elles sont supprimées
      gcTime: 1000 * 60 * 10, // 10 minutes

      retry: 2,

      refetchOnWindowFocus: true,
    },
  },
});

export default function App() {
  return (
    <BrowserRouter>
      <QueryClientProvider client={queryClient}>
        <RouterProvider />
      </QueryClientProvider>
    </BrowserRouter>
  );
}
