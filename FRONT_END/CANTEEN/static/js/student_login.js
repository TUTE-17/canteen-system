function togglePassword() {
  const pass = document.getElementById("password");
  pass.type = pass.type === "password" ? "text" : "password";
}

document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault(); 

  const identifier = document.getElementById("identifier").value;
  const password = document.getElementById("password").value;

  fetch("/student/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ identifier, password })
})
    .then(res => res.json())
    .then(data => {
      if (data.success) {

        localStorage.setItem('student_regno',data.student_regno);
        window.location.href = "/dishes/menu";
      } else {
        
        const loginBox = document.querySelector(".login-box");
        loginBox.classList.add("shake");
        setTimeout(() => {
          loginBox.classList.remove("shake");
        }, 400);

        alert(data.message); 
      }
    })
    .catch(err => {
      console.error("Login error:", err);
      alert(err);
    });
});
