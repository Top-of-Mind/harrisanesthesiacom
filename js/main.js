document.getElementById('year').textContent = new Date().getFullYear();

const navToggle = document.getElementById('nav-toggle');
const siteNav = document.getElementById('site-nav');
navToggle.addEventListener('click', () => {
  const isOpen = siteNav.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
});
siteNav.querySelectorAll('a').forEach((link) => {
  link.addEventListener('click', () => {
    siteNav.classList.remove('open');
    navToggle.setAttribute('aria-expanded', 'false');
  });
});

const form = document.getElementById('contact-form');
const formNote = document.getElementById('form-note');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  formNote.textContent = 'Thanks for reaching out — this form is a placeholder until email delivery is connected.';
  form.reset();
});
