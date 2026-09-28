#!/usr/bin/env python3
"""Génère les pages HTML statiques du site Fernando BILO à partir de gabarits communs
(header / footer) afin de garder une structure et une charte cohérentes."""

import os

ROOT = os.path.join(os.path.dirname(__file__), "site")

FA_CDN = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
BOOTSTRAP_CSS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
BOOTSTRAP_JS = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
GOOGLE_FONT = "https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600&amp;display=swap"


def nav_link(href, label, active_page, page_key):
    active = " active" if page_key == active_page else ""
    aria = ' aria-current="page"' if page_key == active_page else ""
    return f'<li class="nav-item"><a class="nav-link{active}" href="{href}"{aria}>{label}</a></li>'


NAV_ITEMS = [
    ("index.html", "Accueil", "accueil"),
    ("services.html", "Services", "services"),
    ("realisations.html", "Réalisations", "realisations"),
    ("blog.html", "Blog", "blog"),
    ("contact.html", "Me contacter", "contact"),
]


def build_head(title, description, robots="index, follow"):
    return f"""<!doctype html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="{robots}" />
  <link rel="icon" type="image/png" href="images/favicon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link href="{GOOGLE_FONT}" rel="stylesheet" />
  <link href="{BOOTSTRAP_CSS}" rel="stylesheet" />
  <link href="{FA_CDN}" rel="stylesheet" />
  <link href="css/style.css" rel="stylesheet" />
</head>
"""


def build_header(active_page):
    links = "\n        ".join(
        nav_link(href, label, active_page, key) for href, label, key in NAV_ITEMS
    )
    return f"""  <header class="site-header sticky-top">
    <nav class="navbar navbar-expand-lg navbar-dark py-3">
      <div class="container">
        <a class="navbar-brand" href="index.html">Fernando<strong>&nbsp;BILO</strong></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav"
          aria-controls="mainNav" aria-expanded="false" aria-label="Ouvrir la navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="mainNav">
          <ul class="navbar-nav ms-auto">
        {links}
          </ul>
        </div>
      </div>
    </nav>
  </header>
"""


FOOTER = """  <footer class="site-footer">
    <div class="container">
      <div class="row gy-4">
        <div class="col-md-3">
          <h5>Fernando BILO</h5>
          <p class="mb-1"><i class="fa-solid fa-location-dot me-2"></i>Paris, France</p>
          <p class="mb-1"><i class="fa-solid fa-phone me-2"></i>07 54 33 78 65</p>
          <p class="mb-3"><i class="fa-solid fa-envelope me-2"></i>dev-fernando@hotmail.fr</p>
          <div class="social-icons">
            <a href="https://github.com/github-john-doe" target="_blank" rel="noopener noreferrer nofollow" aria-label="Profil GitHub">
              <i class="fa-brands fa-github"></i>
            </a>
            <a href="https://twitter.com/" target="_blank" rel="noopener noreferrer nofollow" aria-label="Profil Twitter">
              <i class="fa-brands fa-twitter"></i>
            </a>
            <a href="https://linkedin.com/" target="_blank" rel="noopener noreferrer nofollow" aria-label="Profil LinkedIn">
              <i class="fa-brands fa-linkedin-in"></i>
            </a>
          </div>
        </div>
        <div class="col-md-3">
          <h5>Navigation</h5>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="index.html">Accueil</a></li>
            <li class="mb-2"><a href="index.html#about">À propos</a></li>
            <li class="mb-2"><a href="services.html">Services</a></li>
            <li class="mb-2"><a href="contact.html">Me contacter</a></li>
            <li class="mb-2"><a href="mentions-legales.html">Mentions légales</a></li>
          </ul>
        </div>
        <div class="col-md-3">
          <h5>Dernières réalisations</h5>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="realisations.html#projet-1">Fresh food</a></li>
            <li class="mb-2"><a href="realisations.html#projet-2">Restaurant Akira</a></li>
            <li class="mb-2"><a href="realisations.html#projet-3">Espace bien-être</a></li>
          </ul>
        </div>
        <div class="col-md-3">
          <h5>Derniers articles</h5>
          <ul class="list-unstyled">
            <li class="mb-2"><a href="blog.html#article-1">Coder son site en HTML/CSS</a></li>
            <li class="mb-2"><a href="blog.html#article-2">Vendre ses produits sur le web</a></li>
            <li class="mb-2"><a href="blog.html#article-3">Se positionner sur Google</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom text-center">
        &copy; <span id="year"></span> Fernando BILO. Tous droits réservés. &mdash;
        <a href="mentions-legales.html">Mentions légales</a>
      </div>
    </div>
  </footer>

  <button id="back-to-top" aria-label="Retour en haut de la page">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <script src="{bootstrap_js}"></script>
  <script src="js/script.js"></script>
</body>
</html>
""".replace("{bootstrap_js}", BOOTSTRAP_JS)


def page(filename, title, description, active_page, body, robots="index, follow"):
    html = build_head(title, description, robots)
    html += "<body>\n"
    html += build_header(active_page)
    html += body
    html += FOOTER
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)


# ---------------------------------------------------------------------------
# Page d'accueil
# ---------------------------------------------------------------------------
BODY_INDEX = """
  <section class="hero" id="home">
    <div class="hero-content">
      <h1>Bonjour, je suis Fernando BILO</h1>
      <h2>Développeur Web &amp; futur alternant passionné par le front-end</h2>
      <a href="#about" class="btn btn-accent">En savoir plus</a>
    </div>
  </section>

  <section id="about" class="bg-page">
    <div class="container">
      <div class="row align-items-center gy-4">
        <div class="col-lg-4 text-center">
          <img src="https://images.unsplash.com/photo-1568602471122-7832951cc4c5?auto=format&amp;fit=crop&amp;w=600&amp;q=80" alt="Photo de Fernando BILO" class="about-photo" />
        </div>
        <div class="col-lg-8">
          <h2 class="section-title">À propos de moi</h2>
          <p>
            Je termine actuellement ma formation de développeur web au <strong>Centre Européen de
            Formation</strong> et je recherche une alternance pour poursuivre mon apprentissage.
            Curieux et rigoureux, j'aime concevoir des interfaces claires, accessibles et
            performantes, du prototypage jusqu'à la mise en production.
          </p>
          <p>
            Mon objectif : rejoindre une équipe où je pourrai continuer à apprendre tout en
            apportant une réelle valeur ajoutée sur des projets front-end comme back-end.
          </p>

          <h3 class="h5 mt-4 mb-3">Mes compétences</h3>
          <div class="skill-bar">
            <div class="d-flex justify-content-between"><span>HTML5</span><span>90%</span></div>
            <div class="progress"><div class="progress-bar skill-html" role="progressbar" style="width: 90%" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100"></div></div>
          </div>
          <div class="skill-bar">
            <div class="d-flex justify-content-between"><span>CSS3</span><span>80%</span></div>
            <div class="progress"><div class="progress-bar skill-css" role="progressbar" style="width: 80%" aria-valuenow="80" aria-valuemin="0" aria-valuemax="100"></div></div>
          </div>
          <div class="skill-bar">
            <div class="d-flex justify-content-between"><span>JavaScript</span><span>70%</span></div>
            <div class="progress"><div class="progress-bar skill-js" role="progressbar" style="width: 70%" aria-valuenow="70" aria-valuemin="0" aria-valuemax="100"></div></div>
          </div>
          <div class="skill-bar">
            <div class="d-flex justify-content-between"><span>PHP</span><span>60%</span></div>
            <div class="progress"><div class="progress-bar skill-php" role="progressbar" style="width: 60%" aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"></div></div>
          </div>
          <div class="skill-bar">
            <div class="d-flex justify-content-between"><span>React</span><span>50%</span></div>
            <div class="progress"><div class="progress-bar skill-react" role="progressbar" style="width: 50%" aria-valuenow="50" aria-valuemin="0" aria-valuemax="100"></div></div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

page(
    "index.html",
    "Fernando BILO — Développeur Web | CV en ligne",
    "Portfolio et CV en ligne de Fernando BILO, développeur web à la recherche d'une alternance.",
    "accueil",
    BODY_INDEX,
)

# ---------------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------------
SERVICES = [
    ("fa-solid fa-laptop-code", "Développement front-end", "Intégration HTML/CSS responsive, animations et interfaces accessibles avec Bootstrap."),
    ("fa-brands fa-react", "Applications React.js", "Création de composants réutilisables et gestion d'état avec les hooks React."),
    ("fa-solid fa-magnifying-glass-chart", "Référencement SEO", "Optimisation on-page, balisage sémantique et bonnes pratiques pour le référencement naturel."),
    ("fa-solid fa-mobile-screen-button", "Design responsive", "Sites adaptés à tous les écrans : mobile, tablette et desktop."),
    ("fa-solid fa-server", "Mise en ligne & hébergement", "Déploiement et hébergement d'applications web statiques et dynamiques."),
    ("fa-solid fa-code-compare", "Qualité & validation W3C", "Code propre, maintenable et conforme aux standards du web."),
]

cards = []
for icon, title, text in SERVICES:
    cards.append(f"""        <div class="col-md-6 col-lg-4">
          <div class="service-card">
            <i class="{icon} service-icon"></i>
            <h3 class="h5">{title}</h3>
            <p class="mb-0">{text}</p>
          </div>
        </div>""")

BODY_SERVICES = f"""
  <section class="bg-page">
    <div class="container">
      <h1 class="section-title text-center mx-auto" style="max-width: 600px;">Mes services</h1>
      <p class="text-center mb-5">Ce que je peux apporter à votre équipe ou votre projet.</p>
      <div class="row g-4">
{os.linesep.join(cards)}
      </div>
    </div>
  </section>
"""

page(
    "services.html",
    "Services — Fernando BILO",
    "Les services proposés par Fernando BILO : développement front-end, React.js, SEO et responsive design.",
    "services",
    BODY_SERVICES,
)

# ---------------------------------------------------------------------------
# Réalisations
# ---------------------------------------------------------------------------
PROJECTS = [
    ("projet-1", "https://picsum.photos/seed/fernando-project-1/600/400", "Fresh food", "Réalisation d'un site avec commande en ligne.", "Site réalisé avec PHP et MySQL"),
    ("projet-2", "https://picsum.photos/seed/fernando-project-2/600/400", "Restaurant Akira", "Réalisation d'un site vitrine.", "Site réalisé avec WordPress"),
    ("projet-3", "https://picsum.photos/seed/fernando-project-3/600/400", "Espace bien-être", "Réalisation d'un site vitrine pour un patricien de bien-être.", "Site réalisé en HTML/CSS"),
]

proj_cards = []
for anchor, img, title, text, tech in PROJECTS:
    proj_cards.append(f"""        <div class="col-md-6 col-lg-4" id="{anchor}">
          <div class="card card-project h-100">
            <img src="{img}" class="card-img-top" alt="Aperçu du projet {title}" />
            <div class="card-body text-center">
              <h3 class="h5 card-title">{title}</h3>
              <p class="card-text">{text}</p>
              <a href="#" class="btn btn-outline-primary btn-sm">Voir</a>
            </div>
            <div class="card-footer text-center text-muted small">{tech}</div>
          </div>
        </div>""")

BODY_REALISATIONS = f"""
  <section class="bg-page">
    <div class="container">
      <h1 class="section-title text-center mx-auto" style="max-width: 600px;">Mes réalisations</h1>
      <p class="text-center mb-5">Une sélection de projets réalisés pendant ma formation.</p>
      <div class="row g-4">
{os.linesep.join(proj_cards)}
      </div>
    </div>
  </section>
"""

page(
    "realisations.html",
    "Réalisations — Fernando BILO",
    "Portfolio des projets réalisés par Fernando BILO pendant sa formation de développeur web.",
    "realisations",
    BODY_REALISATIONS,
)

# ---------------------------------------------------------------------------
# Blog
# ---------------------------------------------------------------------------
ARTICLES = [
    ("article-1", "https://picsum.photos/seed/fernando-blog-1/600/400", "Coder son site en HTML/CSS", "Some quick example text to build on the card title and make up the bulk of the card's content.", "22 août 2026"),
    ("article-2", "https://picsum.photos/seed/fernando-blog-2/600/400", "Vendre ses produits sur le web", "Some quick example text to build on the card title and make up the bulk of the card's content.", "20 août 2026"),
    ("article-3", "https://picsum.photos/seed/fernando-blog-3/600/400", "Se positionner sur Google", "Some quick example text to build on the card title and make up the bulk of the card's content.", "1 août 2026"),
    ("article-4", "https://picsum.photos/seed/fernando-blog-4/600/400", "Coder en responsive design", "Some quick example text to build on the card title and make up the bulk of the card's content.", "31 juillet 2026"),
    ("article-5", "https://picsum.photos/seed/fernando-blog-5/600/400", "Techniques de référencement", "Some quick example text to build on the card title and make up the bulk of the card's content.", "30 juillet 2026"),
    ("article-6", "https://picsum.photos/seed/fernando-blog-6/600/400", "Apprendre à coder", "Some quick example text to build on the card title and make up the bulk of the card's content.", "12 juillet 2026"),
]

article_cards = []
for anchor, img, title, text, published in ARTICLES:
    article_cards.append(f"""        <div class="col-md-6 col-lg-4" id="{anchor}">
          <div class="card card-article h-100">
            <img src="{img}" class="card-img-top" alt="Illustration de l'article {title}" />
            <div class="card-body">
              <h3 class="h5 card-title">{title}</h3>
              <p class="card-text">{text}</p>
              <a href="#" class="btn btn-accent btn-sm">Lire la suite</a>
            </div>
            <div class="card-footer text-muted small">Publié le {published}</div>
          </div>
        </div>""")

BODY_BLOG = f"""
  <section class="bg-page">
    <div class="container">
      <h1 class="section-title text-center mx-auto" style="max-width: 600px;">Blog</h1>
      <p class="text-center mb-5">Mes notes et retours d'expérience sur le développement web.</p>
      <div class="row g-4">
{os.linesep.join(article_cards)}
      </div>
    </div>
  </section>
"""

page(
    "blog.html",
    "Blog — Fernando BILO",
    "Articles et retours d'expérience de Fernando BILO sur le développement web front-end.",
    "blog",
    BODY_BLOG,
)

# ---------------------------------------------------------------------------
# Contact
# ---------------------------------------------------------------------------
BODY_CONTACT = """
  <section class="contact-hero">
    <div class="container text-center">
      <h1 class="mb-3">Contactez-moi</h1>
      <p class="mb-0">Une opportunité d'alternance ou une question ? N'hésitez pas à m'écrire.</p>
    </div>
  </section>

  <section class="bg-page">
    <div class="container">
      <div class="row gy-5">
        <div class="col-lg-7">
          <h2 class="section-title">Envoyer un message</h2>
          <form class="contact-form" novalidate>
            <div class="row g-3">
              <div class="col-md-6">
                <label for="name" class="form-label">Nom complet</label>
                <input type="text" class="form-control" id="name" name="name" required />
                <div class="invalid-feedback">Merci de renseigner votre nom.</div>
              </div>
              <div class="col-md-6">
                <label for="email" class="form-label">E-mail</label>
                <input type="email" class="form-control" id="email" name="email" required />
                <div class="invalid-feedback">Merci de renseigner un e-mail valide.</div>
              </div>
              <div class="col-md-6">
                <label for="phone" class="form-label">Téléphone</label>
                <input type="tel" class="form-control" id="phone" name="phone" required />
                <div class="invalid-feedback">Merci de renseigner votre numéro de téléphone.</div>
              </div>
              <div class="col-md-6">
                <label for="subject" class="form-label">Sujet</label>
                <input type="text" class="form-control" id="subject" name="subject" required />
                <div class="invalid-feedback">Merci de renseigner un sujet.</div>
              </div>
              <div class="col-12">
                <label for="message" class="form-label">Message</label>
                <textarea class="form-control" id="message" name="message" rows="5" required></textarea>
                <div class="invalid-feedback">Merci de renseigner votre message.</div>
              </div>
              <div class="col-12">
                <button type="submit" class="btn btn-accent">Envoyer le message</button>
              </div>
            </div>
          </form>
        </div>
        <div class="col-lg-5">
          <h2 class="section-title">Mes coordonnées</h2>
          <ul class="list-unstyled mb-4">
            <li class="mb-3"><i class="fa-solid fa-location-dot me-2 text-primary"></i>Paris, France</li>
            <li class="mb-3"><i class="fa-solid fa-phone me-2 text-primary"></i>07 54 33 78 65</li>
            <li class="mb-3"><i class="fa-solid fa-envelope me-2 text-primary"></i>dev-fernando@hotmail.fr</li>
          </ul>
          <div class="contact-map">
            <iframe
              src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2624.9!2d2.3488!3d48.8534!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47e66e1f06e2b70f%3A0x40b82c3688c9460!2sParis!5e0!3m2!1sfr!2sfr!4v1700000000000"
              title="Localisation de Fernando BILO sur Google Maps"
              loading="lazy"
              referrerpolicy="no-referrer-when-downgrade">
            </iframe>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

page(
    "contact.html",
    "Contact — Fernando BILO",
    "Contactez Fernando BILO, développeur web à la recherche d'une alternance.",
    "contact",
    BODY_CONTACT,
)

# ---------------------------------------------------------------------------
# Mentions légales (non indexée)
# ---------------------------------------------------------------------------
BODY_MENTIONS = """
  <section class="bg-page">
    <div class="container">
      <h1 class="section-title">Mentions légales</h1>
      <div class="accordion" id="legalAccordion">
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#editeur">
              Éditeur du site
            </button>
          </h2>
          <div id="editeur" class="accordion-collapse collapse show" data-bs-parent="#legalAccordion">
            <div class="accordion-body">
              <p>Le site <strong>fernandobilo-dev.fr</strong> est édité par Fernando BILO, développeur web, basé à
              Paris, France. Téléphone : 07 54 33 78 65. Contact : dev-fernando@hotmail.fr.</p>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#hebergeur">
              Hébergeur du site
            </button>
          </h2>
          <div id="hebergeur" class="accordion-collapse collapse" data-bs-parent="#legalAccordion">
            <div class="accordion-body">
              <p>Le site est hébergé par un prestataire d'hébergement web (nom, adresse et contact de
              l'hébergeur à compléter selon la solution retenue, par exemple GitHub Pages, Netlify ou
              Vercel). L'application React est hébergée sur CodeSandbox.</p>
            </div>
          </div>
        </div>
        <div class="accordion-item">
          <h2 class="accordion-header">
            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#credits">
              Crédits
            </button>
          </h2>
          <div id="credits" class="accordion-collapse collapse" data-bs-parent="#legalAccordion">
            <div class="accordion-body">
              <p>Les images utilisées sur ce site sont libres de droits et proviennent du site
              <a href="https://pixabay.com/" target="_blank" rel="noopener noreferrer">Pixabay</a>.
              Les icônes sont fournies par Font Awesome. La police utilisée est Nunito Sans (Google Fonts).</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

page(
    "mentions-legales.html",
    "Mentions légales — Fernando BILO",
    "Mentions légales du site de Fernando BILO.",
    None,
    BODY_MENTIONS,
    robots="noindex, nofollow",
)

print("Toutes les pages ont été générées.")
