/**
 * GithubProfile
 * Composant séparé chargé uniquement de l'AFFICHAGE des informations
 * d'un profil GitHub. Il ne fait aucun appel réseau : il reçoit les
 * données déjà chargées par le composant principal (App) via ses props.
 */
function GithubProfile({ profile }) {
  const {
    avatar_url: avatarUrl,
    name,
    login,
    bio,
    public_repos: publicRepos,
    followers,
    following,
    location,
    blog,
    company,
    html_url: htmlUrl,
    created_at: createdAt,
  } = profile;

  const memberSince = createdAt
    ? new Date(createdAt).toLocaleDateString("fr-FR", {
        year: "numeric",
        month: "long",
      })
    : null;

  return (
    <article className="profile-card">
      <img src={avatarUrl} alt={`Avatar GitHub de ${name || login}`} />

      <div className="profile-info">
        <h2>{name || login}</h2>
        <a
          className="profile-username"
          href={htmlUrl}
          target="_blank"
          rel="noopener noreferrer"
        >
          @{login}
        </a>

        {bio && <p className="profile-bio">{bio}</p>}

        <div className="profile-stats">
          <div>
            <strong>{publicRepos}</strong>
            <span>Dépôts</span>
          </div>
          <div>
            <strong>{followers}</strong>
            <span>Followers</span>
          </div>
          <div>
            <strong>{following}</strong>
            <span>Following</span>
          </div>
        </div>

        <div className="profile-meta">
          {company && <span>🏢 {company}</span>}
          {location && <span>📍 {location}</span>}
          {blog && (
            <span>
              🔗{" "}
              <a href={blog} target="_blank" rel="noopener noreferrer">
                {blog}
              </a>
            </span>
          )}
          {memberSince && <span>📅 Membre GitHub depuis {memberSince}</span>}
        </div>
      </div>
    </article>
  );
}

export default GithubProfile;
