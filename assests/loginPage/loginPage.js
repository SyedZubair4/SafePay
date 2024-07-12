// Function to hide messages after 3 seconds
window.onload = function() {
    var messages = document.querySelectorAll('#message');
    messages.forEach(function(message) {
        setTimeout(function() {
            message.style.display = 'none';
        }, 3000); // Hide message after 3000 milliseconds (3 seconds)
    });
};


function validateEmail() {
    // Get the email input element
    var emailInput = document.getElementById("email");

    // Regular expressions for matching the organization addresses
    var gmailRegex = /@gmail\.com$/;
    var yahooRegex = /@yahoo\.com$/;
    var outlookRegex = /@outlook\.com$/;

    // Check if the email ends with one of the organization addresses
    if (gmailRegex.test(emailInput.value)) {
        alert("Email is valid - Gmail!");
    } else if (yahooRegex.test(emailInput.value)) {
        alert("Email is valid - Yahoo!");
    } else if (outlookRegex.test(emailInput.value)) {
        alert("Email is valid - Outlook!");
    } else {
        alert("Email must end with @gmail.com, @yahoo.com, or @outlook.com or @example.example");
    }
}