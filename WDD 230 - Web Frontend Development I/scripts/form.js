document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const username = document.getElementById("username");
    const password = document.getElementById("password");
    const confirm = document.getElementById("confirm");
    const email = document.getElementById("email");
    const rating = document.getElementById("rating");
    const ratingValue = document.getElementById("ratingValue");
  
    rating.addEventListener("input", () => {
      ratingValue.textContent = rating.value;
    });
  
    form.addEventListener("submit", (event) => {
  
      const passwordPattern = /^[A-Za-z0-9]{8,}$/;
      if (!passwordPattern.test(password.value)) {
        alert("Password must be at least 8 characters long and alphanumeric only.");
        password.value = "";
        confirm.value = "";
        password.focus();
        event.preventDefault();
        return;
      }
  
      if (password.value !== confirm.value) {
        alert("Passwords do not match. Please try again.");
        password.value = "";
        confirm.value = "";
        password.focus();
        event.preventDefault();
        return;
      }
  
      const emailPattern = /^[a-zA-Z0-9._%+\-]+@byui\.edu$/;
      if (!emailPattern.test(email.value)) {
        alert("Please enter a valid BYUI email address.");
        email.focus();
        event.preventDefault();
        return;
      }
    });
  });
  