# -*- coding: utf-8 -*-
import os
import re

# 1. Update Login HTML
login_main = '''
  <main style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center;">
    <style>
        .auth-container { max-width: 500px; margin: 0 auto; padding: 50px; }
        .auth-title { text-align: center; margin-bottom: 30px; }
        .auth-form .form-group { margin-bottom: 20px; }
        .auth-form label { display: block; color: #fff; margin-bottom: 8px; font-size: 0.9rem; }
        .auth-form input { width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); padding: 12px 15px; border-radius: 8px; color: #fff; font-family: inherit; transition: border-color 0.3s; }
        .auth-form input:focus { outline: none; border-color: var(--primary); }
        .auth-btn { width: 100%; padding: 12px; background: var(--primary); color: #fff; border: none; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; margin-top: 10px; transition: background 0.3s; }
        .auth-btn:hover { background: #0056b3; }
        .auth-links { text-align: center; margin-top: 25px; font-size: 0.9rem; }
        .auth-links a { color: var(--primary); text-decoration: none; font-weight: 500; }
        .auth-links a:hover { text-decoration: underline; }
    </style>
    <div class="container">
        <div class="glass-card auth-container reveal">
            <h2 class="auth-title gradient-text">Welcome Back</h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 30px;">Login to access your client portal</p>
            
            <form class="auth-form" id="loginForm">
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" id="emailInput" placeholder="name@company.com" required>
                </div>
                
                <div class="form-group">
                    <label style="display: flex; justify-content: space-between;">
                        <span>Password</span>
                        <a href="forgot-password.html" style="color: var(--primary); text-decoration: none;">Forgot?</a>
                    </label>
                    <input type="password" id="passwordInput" placeholder="Enter your password" required>
                </div>
                
                <button type="button" class="auth-btn" id="loginBtn">Login</button>
            </form>
            
            <div class="auth-links">
                <p style="color: var(--text-muted);">Don't have an account? <a href="signup.html">Sign Up</a></p>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('loginBtn').addEventListener('click', function() {
            var email = document.getElementById('emailInput').value;
            var password = document.getElementById('passwordInput').value;
            if(email && password) {
                // Simulate Supabase successful login
                localStorage.setItem('isLoggedIn', 'true');
                alert("Login successful!");
                window.location.href = 'index.html';
            } else {
                alert("Please enter your email and password.");
            }
        });
    </script>
  </main>
'''

with open('login.html', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<main.*?</main>', login_main, content, flags=re.DOTALL)
with open('login.html', 'w', encoding='utf-8') as f:
    f.write(new_content)


# 2. Update Signup HTML
signup_main = '''
  <main style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center;">
    <style>
        .auth-container { max-width: 600px; margin: 0 auto; padding: 50px; }
        .auth-title { text-align: center; margin-bottom: 30px; }
        .auth-form .form-group { margin-bottom: 20px; }
        .auth-form label { display: block; color: #fff; margin-bottom: 8px; font-size: 0.9rem; }
        .auth-form input { width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); padding: 12px 15px; border-radius: 8px; color: #fff; font-family: inherit; transition: border-color 0.3s; }
        .auth-form input:focus { outline: none; border-color: var(--primary); }
        .auth-btn { width: 100%; padding: 12px; background: var(--primary); color: #fff; border: none; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; margin-top: 10px; transition: background 0.3s; }
        .auth-btn:hover { background: #0056b3; }
        .auth-links { text-align: center; margin-top: 25px; font-size: 0.9rem; }
        .auth-links a { color: var(--primary); text-decoration: none; font-weight: 500; }
        .auth-links a:hover { text-decoration: underline; }
    </style>
    <div class="container">
        <div class="glass-card auth-container reveal">
            <h2 class="auth-title gradient-text">Create an Account</h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 30px;">Join Truvisory to manage your compliance securely</p>
            
            <form class="auth-form" id="signupForm">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                    <div class="form-group">
                        <label>First Name</label>
                        <input type="text" placeholder="John" required>
                    </div>
                    <div class="form-group">
                        <label>Last Name</label>
                        <input type="text" placeholder="Doe" required>
                    </div>
                </div>
                <div class="form-group">
                    <label>Company Name (Optional)</label>
                    <input type="text" placeholder="e.g. Acme Corp">
                </div>
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" id="signupEmail" placeholder="name@company.com" required>
                </div>
                <div class="form-group">
                    <label>Phone Number</label>
                    <input type="tel" placeholder="+91 98765 43210" required>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <input type="password" placeholder="Create a strong password" required>
                </div>
                
                <button type="button" class="auth-btn" id="createAccountBtn" style="margin-top: 20px;">Sign Up</button>
            </form>
            
            <div class="auth-links">
                <p style="color: var(--text-muted);">Already have an account? <a href="login.html">Login</a></p>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('createAccountBtn').addEventListener('click', function() {
            var email = document.getElementById('signupEmail').value;
            if(email) {
                this.innerHTML = "Processing...";
                setTimeout(() => {
                    alert("Account created! Redirecting to verify your email...");
                    window.location.href = 'verify-otp.html';
                }, 1000);
            } else {
                alert("Please enter your email address.");
            }
        });
    </script>
  </main>
'''

with open('signup.html', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<main.*?</main>', signup_main, content, flags=re.DOTALL)
with open('signup.html', 'w', encoding='utf-8') as f:
    f.write(new_content)


# Extract header/footer from index.html to build the 3 new pages
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()
top_part = idx_content.split('<main>')[0]
bottom_part = idx_content.split('</main>')[1]

# 3. Create verify-otp.html
verify_main = '''
  <main style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center;">
    <style>
        .auth-container { max-width: 500px; margin: 0 auto; padding: 50px; }
        .auth-title { text-align: center; margin-bottom: 30px; }
        .auth-form .form-group { margin-bottom: 20px; }
        .auth-form label { display: block; color: #fff; margin-bottom: 8px; font-size: 0.9rem; text-align: center; }
        .auth-form input { width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; color: #fff; font-family: inherit; font-size: 1.5rem; text-align: center; letter-spacing: 5px; transition: border-color 0.3s; }
        .auth-form input:focus { outline: none; border-color: var(--primary); }
        .auth-btn { width: 100%; padding: 12px; background: var(--primary); color: #fff; border: none; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; margin-top: 10px; transition: background 0.3s; }
        .auth-btn:hover { background: #0056b3; }
    </style>
    <div class="container">
        <div class="glass-card auth-container reveal">
            <h2 class="auth-title gradient-text">Verify Email</h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 30px;">We've sent a 6-digit verification code to your email. Please enter it below.</p>
            
            <form class="auth-form">
                <div class="form-group">
                    <input type="text" id="otpInput" placeholder="------" maxlength="6" required>
                    <p style="font-size: 0.85rem; color: var(--primary); margin-top: 15px; text-align: center; cursor: pointer;">Resend Code</p>
                </div>
                
                <button type="button" class="auth-btn" id="verifyBtn">Verify & Login</button>
            </form>
        </div>
    </div>

    <script>
        document.getElementById('verifyBtn').addEventListener('click', function() {
            var otp = document.getElementById('otpInput').value;
            if(otp.length === 6) {
                localStorage.setItem('isLoggedIn', 'true');
                alert("Email verified successfully! You are now logged in.");
                window.location.href = 'index.html';
            } else {
                alert("Please enter a valid 6-digit OTP.");
            }
        });
    </script>
  </main>
'''

with open('verify-otp.html', 'w', encoding='utf-8') as f:
    f.write(top_part + verify_main + bottom_part)

# 4. Create forgot-password.html
forgot_main = '''
  <main style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center;">
    <style>
        .auth-container { max-width: 500px; margin: 0 auto; padding: 50px; }
        .auth-title { text-align: center; margin-bottom: 30px; }
        .auth-form .form-group { margin-bottom: 20px; }
        .auth-form label { display: block; color: #fff; margin-bottom: 8px; font-size: 0.9rem; }
        .auth-form input { width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); padding: 12px 15px; border-radius: 8px; color: #fff; font-family: inherit; transition: border-color 0.3s; }
        .auth-form input:focus { outline: none; border-color: var(--primary); }
        .auth-btn { width: 100%; padding: 12px; background: var(--primary); color: #fff; border: none; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; margin-top: 10px; transition: background 0.3s; }
        .auth-btn:hover { background: #0056b3; }
        .auth-links { text-align: center; margin-top: 25px; font-size: 0.9rem; }
        .auth-links a { color: var(--text-muted); text-decoration: none; font-weight: 500; }
        .auth-links a:hover { text-decoration: underline; color: #fff; }
    </style>
    <div class="container">
        <div class="glass-card auth-container reveal">
            <h2 class="auth-title gradient-text">Reset Password</h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 30px;">Enter your email address and we'll send you a link to reset your password.</p>
            
            <form class="auth-form">
                <div class="form-group">
                    <label>Email Address</label>
                    <input type="email" id="resetEmail" placeholder="name@company.com" required>
                </div>
                
                <button type="button" class="auth-btn" id="sendResetBtn">Send Reset Link</button>
            </form>
            
            <div class="auth-links">
                <p><a href="login.html"><i class="fa-solid fa-arrow-left"></i> Back to Login</a></p>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('sendResetBtn').addEventListener('click', function() {
            var email = document.getElementById('resetEmail').value;
            if(email) {
                this.innerHTML = "Sending...";
                setTimeout(() => {
                    alert("A password reset link has been sent to " + email);
                    // For simulation purposes, we redirect to change-password.html 
                    // to show the user what happens after clicking the email link.
                    window.location.href = 'change-password.html';
                }, 1500);
            } else {
                alert("Please enter your email address.");
            }
        });
    </script>
  </main>
'''
with open('forgot-password.html', 'w', encoding='utf-8') as f:
    f.write(top_part + forgot_main + bottom_part)

# 5. Create change-password.html
change_main = '''
  <main style="padding-top: 150px; padding-bottom: 80px; min-height: 80vh; display: flex; align-items: center;">
    <style>
        .auth-container { max-width: 500px; margin: 0 auto; padding: 50px; }
        .auth-title { text-align: center; margin-bottom: 30px; }
        .auth-form .form-group { margin-bottom: 20px; }
        .auth-form label { display: block; color: #fff; margin-bottom: 8px; font-size: 0.9rem; }
        .auth-form input { width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); padding: 12px 15px; border-radius: 8px; color: #fff; font-family: inherit; transition: border-color 0.3s; }
        .auth-form input:focus { outline: none; border-color: var(--primary); }
        .auth-btn { width: 100%; padding: 12px; background: var(--primary); color: #fff; border: none; border-radius: 8px; font-size: 1rem; font-weight: 600; cursor: pointer; margin-top: 10px; transition: background 0.3s; }
        .auth-btn:hover { background: #0056b3; }
    </style>
    <div class="container">
        <div class="glass-card auth-container reveal">
            <h2 class="auth-title gradient-text">Create New Password</h2>
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 30px;">Your new password must be different from previously used passwords.</p>
            
            <form class="auth-form">
                <div class="form-group">
                    <label>New Password</label>
                    <input type="password" id="newPass" placeholder="Enter new password" required>
                </div>
                <div class="form-group">
                    <label>Confirm Password</label>
                    <input type="password" id="confirmPass" placeholder="Confirm new password" required>
                </div>
                
                <button type="button" class="auth-btn" id="changePassBtn">Update Password</button>
            </form>
        </div>
    </div>

    <script>
        document.getElementById('changePassBtn').addEventListener('click', function() {
            var pass1 = document.getElementById('newPass').value;
            var pass2 = document.getElementById('confirmPass').value;
            if(pass1 && pass1 === pass2) {
                alert("Password successfully updated! You can now login with your new password.");
                window.location.href = 'login.html';
            } else if (!pass1) {
                alert("Please enter a password.");
            } else {
                alert("Passwords do not match.");
            }
        });
    </script>
  </main>
'''
with open('change-password.html', 'w', encoding='utf-8') as f:
    f.write(top_part + change_main + bottom_part)

print("Updated Auth Flow correctly.")
