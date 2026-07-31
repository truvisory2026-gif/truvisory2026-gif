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
            <p style="text-align: center; color: var(--text-muted); margin-bottom: 30px;">Login with a secure OTP sent to your email.</p>
            
            <form class="auth-form" id="loginForm">
                <div class="form-group" id="emailGroup">
                    <label>Email Address</label>
                    <input type="email" id="emailInput" placeholder="name@company.com" required>
                </div>
                
                <div class="form-group" id="otpGroup" style="display: none;">
                    <label>Enter 6-digit OTP</label>
                    <input type="text" id="otpInput" placeholder="123456" maxlength="6">
                    <p style="font-size: 0.8rem; color: var(--primary); margin-top: 10px; cursor: pointer;">Resend OTP</p>
                </div>
                
                <button type="button" class="auth-btn" id="sendOtpBtn">Send OTP</button>
                <button type="button" class="auth-btn" id="loginBtn" style="display: none;">Login</button>
            </form>
            
            <div class="auth-links">
                <p style="color: var(--text-muted);">Don't have an account? <a href="signup.html">Sign Up</a></p>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('sendOtpBtn').addEventListener('click', function() {
            var email = document.getElementById('emailInput').value;
            if(email) {
                // Simulate sending OTP
                this.innerHTML = "Sending...";
                setTimeout(() => {
                    this.style.display = 'none';
                    document.getElementById('otpGroup').style.display = 'block';
                    document.getElementById('loginBtn').style.display = 'block';
                    alert("A secure OTP has been sent to " + email + " from truvisoryfinance@gmail.com!");
                }, 1000);
            } else {
                alert("Please enter your email address.");
            }
        });

        document.getElementById('loginBtn').addEventListener('click', function() {
            var otp = document.getElementById('otpInput').value;
            if(otp.length === 6) {
                // Simulate Supabase successful login
                localStorage.setItem('isLoggedIn', 'true');
                alert("Login successful!");
                window.location.href = 'index.html';
            } else {
                alert("Please enter a valid 6-digit OTP.");
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
                <div id="detailsGroup">
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
                </div>
                
                <div class="form-group" id="signupOtpGroup" style="display: none;">
                    <label>Enter 6-digit OTP sent to your email</label>
                    <input type="text" id="signupOtpInput" placeholder="123456" maxlength="6">
                    <p style="font-size: 0.8rem; color: var(--primary); margin-top: 10px; cursor: pointer;">Resend OTP</p>
                </div>
                
                <button type="button" class="auth-btn" id="verifyEmailBtn" style="margin-top: 20px;">Verify Email</button>
                <button type="button" class="auth-btn" id="createAccountBtn" style="display: none; margin-top: 20px;">Create Account</button>
            </form>
            
            <div class="auth-links">
                <p style="color: var(--text-muted);">Already have an account? <a href="login.html">Login</a></p>
            </div>
        </div>
    </div>

    <script>
        document.getElementById('verifyEmailBtn').addEventListener('click', function() {
            var email = document.getElementById('signupEmail').value;
            if(email) {
                this.innerHTML = "Sending OTP...";
                setTimeout(() => {
                    this.style.display = 'none';
                    document.getElementById('detailsGroup').style.display = 'none';
                    document.getElementById('signupOtpGroup').style.display = 'block';
                    document.getElementById('createAccountBtn').style.display = 'block';
                    alert("A secure OTP has been sent to " + email + " from truvisoryfinance@gmail.com!");
                }, 1000);
            } else {
                alert("Please enter your email address.");
            }
        });

        document.getElementById('createAccountBtn').addEventListener('click', function() {
            var otp = document.getElementById('signupOtpInput').value;
            if(otp.length === 6) {
                // Simulate Supabase successful signup
                localStorage.setItem('isLoggedIn', 'true');
                alert("Account created successfully!");
                window.location.href = 'index.html';
            } else {
                alert("Please enter a valid 6-digit OTP.");
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


# 3. Update Testimonials HTML
testimonials_main = '''
  <main id="main-content">
    <section class="page-header" style="padding-top: 150px; text-align: center; margin-bottom: 50px;">
        <div class="container reveal">
            <h1 class="gradient-text">Client Testimonials</h1>
            <h3 style="color: white; margin-top: 10px;">Hear From Businesses We've Helped Grow</h3>
        </div>
    </section>

    <section style="padding-bottom: 80px;">
        <div class="container">
            
            <!-- Real Testimonials Grid (Currently Empty awaiting original data) -->
            <div class="grid-2" id="testimonialsGrid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 40px; margin-bottom: 60px;">
                <!-- Real client data will be fetched and injected here by Supabase -->
                <div class="glass-card" style="padding: 40px; text-align: center; grid-column: 1 / -1;">
                    <i class="fa-solid fa-comments" style="font-size: 3rem; color: var(--text-muted); margin-bottom: 20px;"></i>
                    <h3 style="color: var(--text-muted);">No reviews yet.</h3>
                    <p style="color: var(--text-muted);">Be the first to share your experience with Truvisory!</p>
                </div>
            </div>

            <!-- Submit Review Section -->
            <div class="glass-card reveal" style="max-width: 800px; margin: 0 auto; padding: 40px; border-top: 4px solid var(--primary);">
                <h3 style="color: #fff; margin-bottom: 20px; font-size: 1.5rem; text-align: center;">Leave a Review</h3>
                
                <!-- Not Logged In State -->
                <div id="notLoggedInUI" style="text-align: center; padding: 30px 0;">
                    <p style="color: var(--text-muted); font-size: 1.1rem; margin-bottom: 20px;">You must be logged in to submit a review and help us maintain authenticity.</p>
                    <a href="login.html" class="btn btn-primary" style="padding: 12px 30px;">Login to Review</a>
                </div>

                <!-- Logged In State (Hidden by default) -->
                <div id="loggedInUI" style="display: none;">
                    <form id="reviewForm">
                        <div style="margin-bottom: 20px;">
                            <label style="display: block; color: #fff; margin-bottom: 10px;">Your Rating</label>
                            <div style="color: #FFD700; font-size: 1.5rem; cursor: pointer;">
                                <i class="fa-regular fa-star star-rating"></i>
                                <i class="fa-regular fa-star star-rating"></i>
                                <i class="fa-regular fa-star star-rating"></i>
                                <i class="fa-regular fa-star star-rating"></i>
                                <i class="fa-regular fa-star star-rating"></i>
                            </div>
                        </div>
                        <div style="margin-bottom: 20px;">
                            <label style="display: block; color: #fff; margin-bottom: 10px;">Your Review</label>
                            <textarea rows="5" placeholder="Share your experience working with Truvisory..." style="width: 100%; background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); padding: 15px; border-radius: 8px; color: #fff; font-family: inherit; resize: vertical;" required></textarea>
                        </div>
                        <button type="submit" class="btn btn-primary" style="width: 100%;">Submit Review</button>
                    </form>
                </div>
            </div>

        </div>
    </section>

    <script>
        // Check Login State
        document.addEventListener('DOMContentLoaded', function() {
            var isLoggedIn = localStorage.getItem('isLoggedIn');
            if (isLoggedIn === 'true') {
                document.getElementById('notLoggedInUI').style.display = 'none';
                document.getElementById('loggedInUI').style.display = 'block';
            }
        });

        // Handle Form Submission
        document.getElementById('reviewForm')?.addEventListener('submit', function(e) {
            e.preventDefault();
            alert("Thank you! Your review has been submitted securely.");
            this.reset();
        });
    </script>
  </main>
'''

with open('testimonials.html', 'r', encoding='utf-8') as f:
    content = f.read()
new_content = re.sub(r'<main.*?</main>', testimonials_main, content, flags=re.DOTALL)
with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated login.html, signup.html, testimonials.html")
