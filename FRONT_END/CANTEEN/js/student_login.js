function togglePassword() {
  const pass = document.getElementById("password");
  pass.type = pass.type === "password" ? "text" : "password";
}

document.querySelector("form").addEventListener("submit", function (e) {
  const password = document.getElementById("password").value;

  if (password !== "hello") {
    e.preventDefault(); // only prevent if wrong password

    const loginBox = document.querySelector(".login-box");
    loginBox.classList.add("shake");

    setTimeout(() => {
      loginBox.classList.remove("shake");
    }, 400);
  }
  
});
