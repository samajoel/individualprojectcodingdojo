



function linechart(values2, labels2) {

const ctx = document.getElementById('myChart');
    
new Chart(ctx, {
  type: 'line',
  data: {
    labels: labels2,
    datasets: [{
      label: '$ My Sales',
      data: values2,
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