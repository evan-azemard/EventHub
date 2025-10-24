import { Link } from "react-router-dom";

export default function AccueilTemplate() {
  return (
    <>
      <header>Page d'accueil</header>
      <h1>Bienvenue sur EventHub</h1>
      <nav>
        <Link to="/test">Aller à la page Test</Link>
      </nav>
      <footer>Footer Accueil</footer>
    </>
  );
}
