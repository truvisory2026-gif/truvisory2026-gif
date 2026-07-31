import os
import re

# Supabase initialization code
supabase_script = """
<!-- Supabase -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
    const supabaseUrl = 'https://awpbuwzsszlwpsmjbbfq.supabase.co';
    const supabaseKey = 'sb_publishable_fIlhlf8ksuU_kVvphtctvw_2KxgynvE';
    const supabase = supabase.createClient(supabaseUrl, supabaseKey);
</script>
"""

def update_file(filename, replacement_script, old_script_pattern):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject Supabase initialization right before the custom script
    content = re.sub(old_script_pattern, supabase_script + r'\n' + replacement_script, content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

# --- UPDATE SIGNUP.HTML ---
signup_old_pattern = r'<script>\s*document\.getElementById\(\'createAccountBtn\'\)\.addEventListener.*?</script>'
signup_new_script = """<script>
    document.getElementById('createAccountBtn').addEventListener('click', async function() {
        var email = document.getElementById('signupEmail').value;
        if(email) {
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
                alert("OTP sent! Redirecting to verify your email...");
                window.location.href = 'verify-otp.html';
            }
        } else {
            alert("Please enter your email address.");
        }
    });
</script>"""

update_file('signup.html', signup_new_script, signup_old_pattern)

# --- UPDATE LOGIN.HTML ---
login_old_pattern = r'<script>\s*document\.getElementById\(\'loginBtn\'\)\.addEventListener.*?</script>'
login_new_script = """<script>
    // Hide password field as we are using OTP
    document.querySelector('#passwordInput').closest('.form-group').style.display = 'none';
    document.getElementById('loginBtn').innerText = 'Send OTP';

    document.getElementById('loginBtn').addEventListener('click', async function() {
        var email = document.getElementById('emailInput').value;
        if(email) {
            this.innerHTML = "Processing...";
            this.disabled = true;

            const { data, error } = await supabase.auth.signInWithOtp({
                email: email,
            });
            
            this.innerHTML = "Send OTP";
            this.disabled = false;

            if (error) {
                alert("Error: " + error.message);
            } else {
                localStorage.setItem('authEmail', email);
                alert("OTP sent! Redirecting to verify your email...");
                window.location.href = 'verify-otp.html';
            }
        } else {
            alert("Please enter your email address.");
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
                type: 'email'
            });
            
            this.innerHTML = "Verify & Login";
            this.disabled = false;

            if (error) {
                alert("Error: " + error.message);
            } else {
                localStorage.setItem('isLoggedIn', 'true');
                alert("Email verified successfully! You are now logged in.");
                window.location.href = 'index.html';
            }
        } else {
            alert("Please enter a valid 6-digit OTP.");
        }
    });
</script>"""

update_file('verify-otp.html', verify_new_script, verify_old_pattern)
