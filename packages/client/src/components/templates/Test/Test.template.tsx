import { Link } from "react-router-dom";

interface TestTemplateProps {
  message: string;
  loading: boolean;
  error: string | null;
}

export default function TestTemplate({
  message,
  error,
  loading,
}: TestTemplateProps) {
  if (loading) return <h1>Chargement...</h1>;
  if (error) return <h1>{error}</h1>;

  return (
    <>
      <header>Test Page</header>
      <h1>{message}</h1>
      <nav>
        <Link to="/">Retour à l'accueil</Link>
      </nav>
      <footer>Footer Test Page</footer>
    </>
  );
}
