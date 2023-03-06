



function barchart(labels1, values1) {

const ctx = document.getElementById('myChart');
    
new Chart(ctx, {
  type: 'bar',
  data: {
    labels: labels1,
    datasets: [{
      label: '$ Sales By Month',
      data:  values1,
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