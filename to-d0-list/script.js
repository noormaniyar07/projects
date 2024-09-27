let subtotal = 0;
const itemList = [];

// Add item to the list
document.getElementById('add-item-btn').addEventListener('click', function() {
    const itemName = document.getElementById('item-name').value;
    const itemPrice = parseFloat(document.getElementById('item-price').value);
    const itemQuantity = parseInt(document.getElementById('item-quantity').value);
    
    if (itemName.trim() && itemPrice > 0 && itemQuantity > 0) {
        const itemTotal = itemPrice * itemQuantity;
        addItemToList(itemName, itemPrice, itemQuantity, itemTotal);
        updateSubtotal(itemTotal);
        
        clearInputFields();
    }
});

// Add item to the UI and store in memory
function addItemToList(name, price, quantity, total) {
    const listItem = document.createElement('li');
    listItem.innerHTML = `
        ${name} - ₹${price.toFixed(2)} x ${quantity} = ₹${total.toFixed(2)}
        <button class="edit-btn">Edit</button>
        <button class="delete-btn">Delete</button>
    `;
    
    // Edit button functionality
    listItem.querySelector('.edit-btn').addEventListener('click', function() {
        document.getElementById('item-name').value = name;
        document.getElementById('item-price').value = price;
        document.getElementById('item-quantity').value = quantity;
        listItem.remove();
        updateSubtotal(-total);
    });

    // Delete button functionality
    listItem.querySelector('.delete-btn').addEventListener('click', function() {
        listItem.remove();
        updateSubtotal(-total);
    });
    
    document.getElementById('bill-list').appendChild(listItem);
}

// Update subtotal amount
function updateSubtotal(amount) {
    subtotal += amount;
    document.getElementById('subtotal-amount').textContent = subtotal.toFixed(2);
}

// Calculate total with tax and discount
document.getElementById('calculate-total-btn').addEventListener('click', function() {
    const taxRate = parseFloat(document.getElementById('tax-rate').value) || 0;
    const discountRate = parseFloat(document.getElementById('discount-rate').value) || 0;

    const taxAmount = (subtotal * taxRate) / 100;
    const discountAmount = (subtotal * discountRate) / 100;
    const finalAmount = subtotal + taxAmount - discountAmount;
    
    document.getElementById('final-amount').textContent = finalAmount.toFixed(2);
});

// Clear input fields after adding an item
function clearInputFields() {
    document.getElementById('item-name').value = '';
    document.getElementById('item-price').value = '';
    document.getElementById('item-quantity').value = '';
}
