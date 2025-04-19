// Cookie Consent functionality
document.addEventListener('DOMContentLoaded', function() {
    const cookieConsent = document.createElement('div');
    cookieConsent.id = 'cookie-consent';
    cookieConsent.innerHTML = `
        <div class="cookie-consent-content">
            <p>We use cookies to analyze website traffic and optimize your experience. Your data will be aggregated with all other user data. For more information, please read our <a href="about.html#privacy" style="color: #27ae60; text-decoration: underline;">Privacy Policy</a>.</p>
            <div class="cookie-buttons">
                <button id="accept-cookies" class="cookie-btn accept">Accept All</button>
                <button id="decline-cookies" class="cookie-btn decline">Decline</button>
            </div>
        </div>
    `;
    document.body.appendChild(cookieConsent);

    // Show the banner with animation
    setTimeout(() => {
        cookieConsent.classList.add('show');
    }, 500);

    // Check if user has already made a choice
    if (localStorage.getItem('cookieConsent') === 'accepted') {
        cookieConsent.style.display = 'none';
    } else if (localStorage.getItem('cookieConsent') === 'declined') {
        cookieConsent.style.display = 'none';
        // Disable Google Analytics
        window['ga-disable-G-BGX95TQC74'] = true;
    }

    // Handle accept button
    document.getElementById('accept-cookies').addEventListener('click', function() {
        cookieConsent.style.transform = 'translateY(100%)';
        setTimeout(() => {
            cookieConsent.style.display = 'none';
        }, 300);
        localStorage.setItem('cookieConsent', 'accepted');
        // Enable Google Analytics
        window['ga-disable-G-BGX95TQC74'] = false;
        gtag('consent', 'update', {
            'analytics_storage': 'granted'
        });
    });

    // Handle decline button
    document.getElementById('decline-cookies').addEventListener('click', function() {
        cookieConsent.style.transform = 'translateY(100%)';
        setTimeout(() => {
            cookieConsent.style.display = 'none';
        }, 300);
        localStorage.setItem('cookieConsent', 'declined');
        // Disable Google Analytics
        window['ga-disable-G-BGX95TQC74'] = true;
        gtag('consent', 'update', {
            'analytics_storage': 'denied'
        });
    });
}); 