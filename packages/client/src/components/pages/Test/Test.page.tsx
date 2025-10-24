import { TestTemplate } from "@/components/templates";
import { useTestManagement } from "@/hooks/useTestManagement";

export default function Test() {
  const { message, error, loading } = useTestManagement();
  return <TestTemplate message={message} error={error} loading={loading} />;
}
