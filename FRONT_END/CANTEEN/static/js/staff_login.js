const togglePassword = document.getElementById("toggle-password"); 
const passwordField = document.getElementById("password"); 
 
togglePassword.addEventListener("click", () => { 
  if (passwordField.type === "password") { 
    passwordField.type = "text"; 
    togglePassword.textContent = "🙈"; 
  } else { 
    passwordField.type = "password"; 
    togglePassword.textContent = "👁️"; 
  } 
}); 
 
  const loginBtn = document.querySelector('.login-btn'); 
  const successMessage = document.getElementById('successMessage'); 
 
  loginBtn.addEventListener('click', function (e) { 
    e.preventDefault(); 
    successMessage.style.display = 'block'; 
}); 
function login() { 
 
  window.location.href = '/dishes/admin'; 
 
  document.getElementById('successPopup').style.display = 'block'; 
  document.getElementById('popupOverlay').style.display = 'block'; 
} 
 
function closePopup() { 
  document.getElementById('successPopup').style.display = 'none'; 
  document.getElementById('popupOverlay').style.display = 'none';
}