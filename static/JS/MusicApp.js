// fade cards in
document.addEventListener("DOMContentLoaded", function () {
  const cards = document.querySelectorAll(".fade-card");

  cards.forEach((card, index) => {
    setTimeout(() => {
      card.classList.add("visible");
    }, index * 300);
  });
});

// typing effect
document.addEventListener('DOMContentLoaded', function () {
  if (document.querySelector('.typed-out')) {
    new Typed('.typed-out', {
      strings: ['Welcome!', 'Look at top tracks from around the world.', 'Add your own Tracks.'],
      typeSpeed: 30,
      backSpeed: 30,
      loop: true
    });
  }
});

