import os
import re

# 1. Create supabase_init.js
supabase_init_content = """
const supabaseUrl = 'https://awpbuwzsszlwpsmjbbfq.supabase.co';
const supabaseKey = 'sb_publishable_fIlhlf8ksuU_kVvphtctvw_2KxgynvE';
const supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
"""
os.makedirs('assets/js', exist_ok=True)
with open('assets/js/supabase_init.js', 'w', encoding='utf-8') as f:
    f.write(supabase_init_content.strip())
print("Created assets/js/supabase_init.js")

# 2. Create auth_nav.js
auth_nav_content = """
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
"""
with open('assets/js/auth_nav.js', 'w', encoding='utf-8') as f:
    f.write(auth_nav_content.strip())
print("Created assets/js/auth_nav.js")

# 3. Create dashboard.html (base template from index.html)
# Let's read index.html and replace its main content
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace <main>...</main> and inject auth protection script
dashboard_main = """
  <main style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh;">
    <div class="container">
        <div class="glass-card reveal" style="padding: 40px;">
            <h2 class="gradient-text">Welcome to Your Dashboard</h2>
            <p style="color: var(--text-muted); margin-top: 10px;" id="dashboardGreeting">Loading profile...</p>
            
            <div style="margin-top: 40px; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 25px;">
                    <h3 style="color: #fff; margin-bottom: 15px;"><i class="fa-solid fa-file-invoice" style="color: var(--primary); margin-right: 10px;"></i> Compliance Documents</h3>
                    <p style="color: #aaa; font-size: 0.9rem;">View and manage your compliance filings and reports.</p>
                    <button class="btn btn-outline" style="margin-top: 20px; padding: 10px 20px;">View Documents</button>
                </div>
                
                <div style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 8px; padding: 25px;">
                    <h3 style="color: #fff; margin-bottom: 15px;"><i class="fa-solid fa-credit-card" style="color: var(--primary); margin-right: 10px;"></i> Billing & Invoices</h3>
                    <p style="color: #aaa; font-size: 0.9rem;">Manage your subscription, payments, and view past invoices.</p>
                    <button class="btn btn-outline" style="margin-top: 20px; padding: 10px 20px;">View Billing</button>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        document.addEventListener('DOMContentLoaded', async () => {
            const { data: { session }, error } = await supabase.auth.getSession();
            if (!session) {
                // Not logged in, redirect to login
                window.location.href = 'login.html';
                return;
            }
            
            // Try fetching profile data
            const user = session.user;
            const { data: profile, error: profileError } = await supabase
                .from('profiles')
                .select('*')
                .eq('id', user.id)
                .single();
                
            if (profile) {
                document.getElementById('dashboardGreeting').innerText = `Hello, ${profile.first_name} ${profile.last_name}!`;
            } else {
                document.getElementById('dashboardGreeting').innerText = `Hello, ${user.email}!`;
            }
        });
    </script>
  </main>
"""
dashboard_html = re.sub(r'<main>.*?</main>', dashboard_main, index_html, flags=re.DOTALL)
dashboard_html = re.sub(r'<main .*?>.*?</main>', dashboard_main, dashboard_html, flags=re.DOTALL)

with open('dashboard.html', 'w', encoding='utf-8') as f:
    f.write(dashboard_html)
print("Created dashboard.html")

# 4. Modify signup.html script to save localStorage details
def update_file(filename, replacement_script, old_script_pattern):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(old_script_pattern, replacement_script, content, flags=re.DOTALL)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

signup_old_pattern = r'<script>\s*document\.getElementById\(\'createAccountBtn\'\)\.addEventListener.*?</script>'
signup_new_script = """<script>
    document.getElementById('createAccountBtn').addEventListener('click', async function() {
        var email = document.getElementById('signupEmail').value;
        var firstName = document.querySelector('input[placeholder="John"]').value;
        var lastName = document.querySelector('input[placeholder="Doe"]').value;
        var companyName = document.querySelector('input[placeholder="e.g. Acme Corp"]').value;
        var phone = document.querySelector('input[placeholder="+91 98765 43210"]').value;
        
        if(email && firstName && lastName) {
            this.innerHTML = "Processing...";
            this.disabled = true;
            
            const { data, error } = await supabase.auth.signInWithOtp({
                email: email,
            });
            
            this.innerHTML = "Sign Up";
            this.disabled = false;

            if (error) {
                alert("Error: " + error.message);
            } else {
                localStorage.setItem('authEmail', email);
                localStorage.setItem('signup_firstName', firstName);
                localStorage.setItem('signup_lastName', lastName);
                localStorage.setItem('signup_company', companyName);
                localStorage.setItem('signup_phone', phone);
                alert("OTP sent! Redirecting to verify your email...");
                window.location.href = 'verify-otp.html';
            }
        } else {
            alert("Please fill in at least First Name, Last Name, and Email.");
        }
    });
</script>"""

update_file('signup.html', signup_new_script, signup_old_pattern)

# 5. Modify verify-otp.html script to insert to profiles table
verify_old_pattern = r'<script>\s*document\.getElementById\(\'verifyBtn\'\)\.addEventListener.*?</script>'
verify_new_script = """<script>
    document.getElementById('verifyBtn').addEventListener('click', async function() {
        var otp = document.getElementById('otpInput').value;
        var email = localStorage.getItem('authEmail');
        
        if(!email) {
            alert("No email found. Please try logging in again.");
            window.location.href = 'login.html';
            return;
        }

        if(otp.length === 6) {
            this.innerHTML = "Verifying...";
            this.disabled = true;

            const { data, error } = await supabase.auth.verifyOtp({
                email: email,
                token: otp,
                type: 'email'
            });
            
            this.innerHTML = "Verify & Login";
            this.disabled = false;

            if (error) {
                alert("Error: " + error.message);
            } else {
                // OTP verified successfully
                const user = data.user;
                
                // Attempt to insert profile data if it exists in localStorage
                const firstName = localStorage.getItem('signup_firstName');
                const lastName = localStorage.getItem('signup_lastName');
                const company = localStorage.getItem('signup_company');
                const phone = localStorage.getItem('signup_phone');
                
                if (firstName && lastName) {
                    const { error: profileError } = await supabase
                        .from('profiles')
                        .insert([
                            {
                                id: user.id,
                                first_name: firstName,
                                last_name: lastName,
                                company_name: company,
                                phone_number: phone
                            }
                        ]);
                        
                    if (profileError) {
                        console.error("Profile insert error:", profileError);
                        // If error implies duplicate, we ignore as they might be logging in again
                    }
                    
                    // Clear local storage
                    localStorage.removeItem('signup_firstName');
                    localStorage.removeItem('signup_lastName');
                    localStorage.removeItem('signup_company');
                    localStorage.removeItem('signup_phone');
                }
                
                localStorage.setItem('isLoggedIn', 'true');
                alert("Email verified successfully! You are now logged in.");
                window.location.href = 'dashboard.html';
            }
        } else {
            alert("Please enter a valid 6-digit OTP.");
        }
    });
</script>"""

update_file('verify-otp.html', verify_new_script, verify_old_pattern)

# 6. Inject Supabase JS + auth_nav.js into all HTML files globally
def inject_global_scripts():
    script_injection = """
  <!-- Supabase & Auth Scripts -->
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script src="assets/js/supabase_init.js"></script>
  <script src="assets/js/auth_nav.js"></script>
"""
    for root, dirs, files in os.walk('.'):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if it already has Supabase globally injected
                if 'assets/js/supabase_init.js' not in content:
                    # Inject right before </body> or <script src="assets/js/main.js">
                    if '<script src="assets/js/main.js">' in content:
                        content = content.replace('<script src="assets/js/main.js">', script_injection + '\n  <script src="assets/js/main.js">')
                    else:
                        content = content.replace('</body>', script_injection + '\n</body>')
                    
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Injected scripts into {path}")

inject_global_scripts()

