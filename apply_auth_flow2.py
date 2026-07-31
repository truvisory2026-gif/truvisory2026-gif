import re

def update_file(filename, replacement_script, old_script_pattern):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(old_script_pattern, replacement_script, content, flags=re.DOTALL)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

# --- UPDATE SIGNUP.HTML ---
signup_old_pattern = r'<script>\s*document\.getElementById\(\'createAccountBtn\'\)\.addEventListener.*?</script>'
signup_new_script = """<script>
    document.getElementById('createAccountBtn').addEventListener('click', async function() {
        var email = document.getElementById('signupEmail').value;
        var firstName = document.querySelector('input[placeholder="John"]').value;
        var lastName = document.querySelector('input[placeholder="Doe"]').value;
        var companyName = document.querySelector('input[placeholder="e.g. Acme Corp"]').value;
        var phone = document.querySelector('input[placeholder="+91 98765 43210"]').value;
        var password = document.querySelector('input[type="password"]').value;
        
        if(email && firstName && lastName && password) {
            this.innerHTML = "Processing...";
            this.disabled = true;
            
            const { data, error } = await supabase.auth.signUp({
                email: email,
                password: password,
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
                alert("Account created! Redirecting to verify your email...");
                window.location.href = 'verify-otp.html';
            }
        } else {
            alert("Please fill in First Name, Last Name, Email, and Password.");
        }
    });
</script>"""
update_file('signup.html', signup_new_script, signup_old_pattern)

# --- UPDATE LOGIN.HTML ---
login_old_pattern = r'<script>\s*// Hide password field.*?</script>'
login_new_script = """<script>
    document.getElementById('loginBtn').addEventListener('click', async function() {
        var email = document.getElementById('emailInput').value;
        var password = document.getElementById('passwordInput').value;
        
        if(email && password) {
            this.innerHTML = "Processing...";
            this.disabled = true;

            const { data, error } = await supabase.auth.signInWithPassword({
                email: email,
                password: password,
            });
            
            this.innerHTML = "Login";
            this.disabled = false;

            if (error) {
                alert("Error: " + error.message);
            } else {
                localStorage.setItem('isLoggedIn', 'true');
                alert("Login successful!");
                window.location.href = 'dashboard.html';
            }
        } else {
            alert("Please enter both email and password.");
        }
    });
</script>"""
update_file('login.html', login_new_script, login_old_pattern)

# --- UPDATE VERIFY-OTP.HTML ---
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
                type: 'signup'
            });
            
            this.innerHTML = "Verify & Login";
            this.disabled = false;

            if (error) {
                alert("Error: " + error.message);
            } else {
                // OTP verified successfully
                const user = data.user || (data.session && data.session.user);
                
                // Attempt to insert profile data if it exists in localStorage
                const firstName = localStorage.getItem('signup_firstName');
                const lastName = localStorage.getItem('signup_lastName');
                const company = localStorage.getItem('signup_company');
                const phone = localStorage.getItem('signup_phone');
                
                if (user && firstName && lastName) {
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
