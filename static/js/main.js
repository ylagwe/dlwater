// Nav toggle for mobile
const toggle = document.getElementById('navToggle');
const links = document.getElementById('navLinks');
if (toggle && links) {
  toggle.addEventListener('click', () => {
    links.classList.toggle('open');
  });
}

// Fade-in animation on scroll
const animEls = document.querySelectorAll('.animate');
if ('IntersectionObserver' in window) {
  const obs = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.style.animationPlayState = 'running'; obs.unobserve(e.target); }
    });
  }, { threshold: 0.1 });
  animEls.forEach(el => { el.style.animationPlayState = 'paused'; obs.observe(el); });
}
