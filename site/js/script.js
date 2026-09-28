/* =========================================================
   John Doe - CV en ligne
   Script vanilla JS : navigation active, bouton retour en haut,
   validation Bootstrap du formulaire de contact, année du footer.
   ========================================================= */

document.addEventListener("DOMContentLoaded", function () {
  // ---- Année courante dans le footer -----------------------------------
  var yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  // ---- Mise en évidence du lien de navigation actif ---------------------
  // (déjà positionné côté serveur/génération, ce bloc sécurise le cas des
  // ancres et de la navigation via le clavier / retour arrière du navigateur)
  var currentPage = window.location.pathname.split("/").pop() || "index.html";
  var navLinks = document.querySelectorAll(".site-header .nav-link");
  navLinks.forEach(function (link) {
    var linkPage = link.getAttribute("href").split("#")[0] || "index.html";
    if (linkPage === currentPage) {
      link.classList.add("active");
    }
  });

  // ---- Bouton "retour en haut de la page" --------------------------------
  var backToTopBtn = document.getElementById("back-to-top");
  if (backToTopBtn) {
    var toggleBackToTop = function () {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add("show");
      } else {
        backToTopBtn.classList.remove("show");
      }
    };

    window.addEventListener("scroll", toggleBackToTop);
    toggleBackToTop();

    backToTopBtn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // ---- Validation Bootstrap du formulaire de contact ---------------------
  var contactForm = document.querySelector(".contact-form");
  if (contactForm) {
    contactForm.addEventListener("submit", function (event) {
      if (!contactForm.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      } else {
        event.preventDefault();
        contactForm.reset();
        contactForm.classList.remove("was-validated");
        window.alert("Merci pour votre message, je reviens vers vous rapidement !");
        return;
      }
      contactForm.classList.add("was-validated");
    });
  }
});
