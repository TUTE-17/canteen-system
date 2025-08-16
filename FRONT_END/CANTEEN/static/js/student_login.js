function togglePassword() {
  const pass = document.getElementById("password");
  pass.type = pass.type === "password" ? "text" : "password";
}

document.querySelector("form").addEventListener("submit", function (e) {
  e.preventDefault(); // prevent form's default submit

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
        // Save token if needed
        localStorage.setItem("token", data.token);
        // Redirect to menu page
        window.location.href = "/dishes/menu";
      } else {
        // Wrong credentials -> trigger shake
        const loginBox = document.querySelector(".login-box");
        loginBox.classList.add("shake");
        setTimeout(() => {
          loginBox.classList.remove("shake");
        }, 400);

        alert(data.message); // optional: show reason
      }
    })
    .catch(err => {
      console.error("Login error:", err);
      alert(err);
    });
});
