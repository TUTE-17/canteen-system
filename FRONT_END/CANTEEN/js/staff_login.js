const togglePassword = document.getElementById("toggle-password"); 
const passwordField = document.getElementById("password"); 
 
togglePassword.addEventListener("click", () => { 
  if (passwordField.type === "password") { 
    passwordField.type = "text"; 
    togglePassword.textContent = "🙈"; 
  } else { 
    passwordField.type = "password"; 
    togglePassword.textContent = "👁"; 
  } 
}); 
 
  const loginBtn = document.querySelector('.login-btn'); 
  const successMessage = document.getElementById('successMessage'); 
 
  loginBtn.addEventListener('click', function (e) { 
    e.preventDefault(); // prevents actual form submission 
    successMessage.style.display = 'block'; 
}); 
function login() { 
  // Optional: validate username/password before redirecting 
  // For now, just redirect to success page 
 
  window.location.href = 'index1.html'; 
 
  document.getElementById('successPopup').style.display = 'block'; 
  document.getElementById('popupOverlay').style.display = 'block'; 
} 
 
function closePopup() { 
  document.getElementById('successPopup').style.display = 'none'; 
  document.getElementById('popupOverlay').style.display = 'none';
}