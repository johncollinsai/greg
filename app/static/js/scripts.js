var jQuery = require('jquery');

// Opens modal when user clicks on a row in the table - NOT WORKING YET, SEE CHATGPT "SHOW IMAGES"
// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal
var modalImg = document.getElementById("img01");

// Get the table rows
var rows = document.querySelectorAll(".table-hover tr");

// Loop through each row
rows.forEach(function(row) {
  // Add a click event listener to the row
  row.addEventListener('click', function() {
    // Get the image URL from the data-img attribute
    var imgSrc = this.getAttribute("data-img");

    // Set the image source for the modal image
    modalImg.src = imgSrc;

    // Display the modal
    modal.style.display = "block";
  });
});

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}
