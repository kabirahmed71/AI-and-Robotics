let cart = [];
const filterButtons = document.querySelectorAll(".filter-btn");
const menuCards = document.querySelectorAll(".menu-items .item");

function addToCart(name, price) {
  cart.push({ name, price });
  displayCart();
}

function displayCart() {
  const cartItems = document.getElementById("cartItems");
  const totalElement = document.getElementById("total");
  let total = 0;

  cartItems.innerHTML = "";

  cart.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = `${item.name} - ৳${item.price}`;
    cartItems.appendChild(li);
    total += item.price;
  });

  totalElement.textContent = total;
}

function placeOrder() {
  if (cart.length === 0) {
    alert("No items selected!");
    return;
  }

  const paymentSelect = document.getElementById("paymentMethod");
  const payment = paymentSelect ? paymentSelect.value : "";

  if (!payment) {
    alert("Please select a payment method (Bkash, Nagad, Rocket, or Cash on Delivery).");
    return;
  }

  alert(`Order placed successfully!\nPayment method: ${payment}`);
  cart = [];
  displayCart();

  if (paymentSelect) {
    paymentSelect.value = "";
  }
}

filterButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const filter = btn.dataset.filter;

    filterButtons.forEach((button) => button.classList.remove("active"));
    btn.classList.add("active");

    menuCards.forEach((card) => {
      const mealType = card.dataset.meal;
      const shouldShow = filter === "all" || mealType === filter;
      card.style.display = shouldShow ? "block" : "none";
    });
  });
});
