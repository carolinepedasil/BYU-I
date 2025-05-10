const destinations = {
    beach: ["Copacabana", "Fernando de Noronha"],
    nature: ["Amazon Rainforest", "Pantanal"],
    history: ["Ouro Preto", "Salvador"]
  };
  
  function showSuggestion(interest) {
    const suggestion = document.getElementById("suggestion");
  
    if (destinations[interest]) {
      suggestion.textContent = `Recommended: ${destinations[interest].join(" or ")}`;
    } else {
      suggestion.textContent = "No suggestion available.";
    }
  }
  
  let wishlist = JSON.parse(localStorage.getItem("wishlist")) || [];
  
  function renderWishlist() {
    const listElement = document.getElementById("wishlistItems");
    listElement.innerHTML = "";
  
    wishlist.forEach(place => {
      const li = document.createElement("li");
      li.textContent = place;
      listElement.appendChild(li);
    });
  }
  
  document.getElementById("wishlistForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const placeInput = document.getElementById("place");
    const place = placeInput.value.trim();
  
    if (place) {
      wishlist.push(place);
      localStorage.setItem("wishlist", JSON.stringify(wishlist)); 
      renderWishlist();
      placeInput.value = "";
    }
  });
  
  renderWishlist();
  