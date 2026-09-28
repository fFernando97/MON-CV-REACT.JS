import { useState, useEffect, useCallback } from "react";
import GithubProfile from "./components/GithubProfile.jsx";

// Profil GitHub par défaut proposé par le brief du devoir. Un champ de
// recherche permet aussi d'afficher n'importe quel autre profil GitHub réel.
const DEFAULT_USERNAME = "github-john-doe";

/**
 * App
 * Composant principal (fonctionnel). Gère l'état de l'application avec les
 * hooks useState / useEffect / useCallback : la recherche, le chargement,
 * les erreurs et les données du profil GitHub récupérées depuis l'API.
 */
function App() {
  const [username, setUsername] = useState(DEFAULT_USERNAME);
  const [searchValue, setSearchValue] = useState(DEFAULT_USERNAME);
  const [profile, setProfile] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchProfile = useCallback(async (githubUsername) => {
    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(
        `https://api.github.com/users/${encodeURIComponent(githubUsername)}`
      );

      if (!response.ok) {
        throw new Error(
          response.status === 404
            ? `Aucun profil GitHub trouvé pour "${githubUsername}".`
            : "Une erreur est survenue lors de la récupération du profil."
        );
      }

      const data = await response.json();
      setProfile(data);
    } catch (err) {
      setProfile(null);
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchProfile(username);
  }, [username, fetchProfile]);

  const handleSubmit = (event) => {
    event.preventDefault();
    const trimmed = searchValue.trim();
    if (trimmed) {
      setUsername(trimmed);
    }
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>Profil GitHub</h1>
        <p>Application React.js — Fernando BILO</p>
      </header>

      <form className="search-form" onSubmit={handleSubmit}>
        <input
          type="text"
          value={searchValue}
          onChange={(event) => setSearchValue(event.target.value)}
          placeholder="Identifiant GitHub (ex : github-john-doe)"
          aria-label="Identifiant GitHub"
        />
        <button type="submit">Rechercher</button>
      </form>

      {isLoading && <p className="state-message">Chargement du profil…</p>}

      {!isLoading && error && (
        <p className="state-message error" role="alert">
          {error}
        </p>
      )}

      {!isLoading && !error && profile && <GithubProfile profile={profile} />}
    </div>
  );
}

export default App;
