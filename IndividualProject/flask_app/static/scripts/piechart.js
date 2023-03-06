


function piechart(labels, values) {

new Chart(document.getElementById('myChart2'), {
    type: 'pie',
    data: {
  
  
  
      
      labels: labels,
      
      
      //nombre 
      datasets: [{
        label: 'Year Sales By User',
        data: values,       // datooos
        backgroundColor: [
        'rgb(255, 99, 132)',
        'rgb(54, 162, 235)',
        'rgb(255, 205, 86)'],
  
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

}