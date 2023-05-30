var jQuery;
if (typeof window !== 'undefined') {
  jQuery = window.jQuery;
} else {
  jQuery = require('jquery');
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal
var modalImg = document.getElementById("img01");

// Create a new span element for the close button
var span = document.createElement("span");
span.className = "close";
span.innerHTML = "&times;";

// Append the close button to the modal
modal.appendChild(span);

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

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}


// Create Chart.js chart
var Chart = window.Chart; // Get the chart class from the window object

var ctx = document.getElementById('myChart');
if (ctx) { // Check if the element exists
  ctx = ctx.getContext('2d');
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10'], 
      datasets: [{
        label: 'Open-source',
        data: [8, 7.5, 7, 7.5, 9, 12, 16, 22, 28, 35],
        borderColor: 'blue',
        fill: false,
        tension: 0.4 // This will create a smooth line
      }, {
        label: 'Closed-source',
        data: [10, 12, 14, 16, 18, 20, 22, 24, 26, 28],
        borderColor: 'red',
        fill: false
      }]
    },
    options: {
      responsive: true,
      scales: {
        x: {
          display: true,
          title: {
            display: true,
            text: 'Time'
          },
          ticks: {
            display: false,
            drawTicks: false
          },
          grid: {
            drawBorder: true
          }
        },
        y: {
          display: true,
          beginAtZero: true,
          title: {
            display: false
          },
          ticks: {
            display: false,
            drawTicks: false
          },
          grid: {
            drawBorder: true
          }
        }
      }
    }
  });
}
