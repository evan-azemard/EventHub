import axios from "axios";
import { useQuery } from "@tanstack/react-query";

export const useTestManagement = () => {
  const url = `${import.meta.env.VITE_API_URL}/test`;
  const { data, isLoading, error } = useQuery({
    queryKey: ["test"],
    queryFn: async () => {
      const response = await axios.get(url);
      return response.data.message;
    },
  });

  return {
    message: data,
    loading: isLoading,
    error: error?.message || null,
  };
};
