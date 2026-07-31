document.addEventListener('DOMContentLoaded', async () => {
    // Check if Supabase client is initialized
    if (typeof supabase === 'undefined') {
        console.warn('Supabase client not loaded, auth_nav skipped.');
        return;
    }

    const { data: { session }, error } = await supabase.auth.getSession();
    const navActions = document.querySelector('.nav-actions');

    if (navActions) {
        if (session) {
            // User is logged in
            navActions.innerHTML = `
                <a href="dashboard.html" class="btn btn-outline" style="padding: 12px 24px; font-weight: 500; border-color: rgba(255,255,255,0.2);">Dashboard</a>
                <button id="logoutBtn" class="btn btn-primary" style="padding: 12px 24px; font-weight: 500; border: none; background: #e74c3c; color: #fff; border-radius: 4px; cursor: pointer;">Logout</button>
            `;

            document.getElementById('logoutBtn').addEventListener('click', async () => {
                const { error } = await supabase.auth.signOut();
                if (!error) {
                    window.location.href = 'index.html';
                } else {
                    alert('Error logging out: ' + error.message);
                }
            });
        } else {
            // User is NOT logged in
            navActions.innerHTML = `
                <a href="login.html" class="btn btn-outline" style="padding: 12px 24px; font-weight: 500; border-color: rgba(255,255,255,0.2);">Login / Sign Up</a>
            `;
        }
    }
});