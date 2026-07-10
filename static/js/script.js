// ==========================================================================
// ShopHub Custom JavaScript
// Small, beginner-friendly UX enhancements (no frameworks needed).
// ==========================================================================

document.addEventListener('DOMContentLoaded', function () {

    // --------------------------------------------------------------------
    // 1. Auto-dismiss success/info alert messages after 4 seconds
    // --------------------------------------------------------------------
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            bsAlert.close();
        }, 4000);
    });

    // --------------------------------------------------------------------
    // 2. Add a subtle shadow to the navbar once the page is scrolled
    // --------------------------------------------------------------------
    const navbar = document.querySelector('.shophub-navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 10) {
                navbar.classList.add('shadow');
            } else {
                navbar.classList.remove('shadow');
            }
        });
    }

    // --------------------------------------------------------------------
    // 3. Reveal content as it scrolls into view
    // --------------------------------------------------------------------
    const revealTargets = document.querySelectorAll('.product-card, .category-card, .section-title');
    revealTargets.forEach(function (target) {
        target.classList.add('reveal');
    });

    if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver(function (entries, observer) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.18,
            rootMargin: '0px 0px -80px 0px'
        });

        revealTargets.forEach(function (target) {
            revealObserver.observe(target);
        });
    } else {
        revealTargets.forEach(function (target) {
            target.classList.add('active');
        });
    }

    // --------------------------------------------------------------------
    // 4. Confirm before removing an item from the cart or wishlist
    // --------------------------------------------------------------------
    document.querySelectorAll('form[action*="remove"]').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            if (!confirm('Are you sure you want to remove this item?')) {
                e.preventDefault();
            }
        });
    });

});
  
window.addEventListener("scroll", function () {

document.querySelectorAll(".reveal").forEach(function(el){

const top = el.getBoundingClientRect().top;

const height = window.innerHeight;

if(top < height-100){

el.classList.add("active");

}

});

});