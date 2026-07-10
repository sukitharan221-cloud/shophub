<<<<<<< HEAD
document.addEventListener('DOMContentLoaded', () => {
  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealItems.length) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('active'));
  }

  document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((element) => {
    if (window.bootstrap?.Tooltip) {
      new bootstrap.Tooltip(element);
    }
  });
});
=======
document.addEventListener('DOMContentLoaded', () => {
  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealItems.length) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    revealItems.forEach((item) => observer.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add('active'));
  }

  document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach((element) => {
    if (window.bootstrap?.Tooltip) {
      new bootstrap.Tooltip(element);
    }
  });
});
>>>>>>> 0ee8e68c256354465a0041cf1c3e350bde1c2534
