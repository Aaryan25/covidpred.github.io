$(function() {
    "use strict";

     // chart 1
	 
		  var ctx = document.getElementById('chart1').getContext('2d');
		
			var myChart = new Chart(ctx, {
				type: 'line',
				data: {
					labels: JSON.parse(document.getElementById('data_india_active_date').textContent),
					datasets: [{
						label: 'Confirmed',
						data: JSON.parse(document.getElementById('data_india_active_data').textContent),
						borderColor: 'rgba(255, 0, 0, 0.5)',
						//borderColor: "transparent",
						pointRadius :"0",
						borderWidth: 3
					}, {
						label: 'Recovered',
						data: JSON.parse(document.getElementById('data_india_recover_data').textContent),
						borderColor: "rgba(0, 255, 0, 0.5)",
						//borderColor: "transparent",
						pointRadius :"0",
						borderWidth: 1
					},{
						label: 'Deaths',
						data: JSON.parse(document.getElementById('data_india_death_data').textContent),
						borderColor: 'rgba(255, 255, 255, 0.5)',
						//borderColor: "transparent",
						pointRadius :"0",
						borderWidth: 1,
						
					}]
				},
			options: {
				maintainAspectRatio: false,
				legend: {
				  display: false,
				  labels: {
					fontColor: '#ddd',  
					boxWidth:40
				  }
				},
				maintainAspectRatio: false,
				tooltips: {
				  displayColors:false,
					mode:'index',
					backgroundColor:'rgba(0,0,0,0.5)'
				},	
			  scales: {
				  xAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#ddd'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(221, 221, 221, 0.08)"
					},
				  }],
				   yAxes: [{
					ticks: {
						beginAtZero:true,
						fontColor: '#ddd'
					},
					gridLines: {
					  display: true ,
					  color: "rgba(221, 221, 221, 0.08)"
					},
				  }]
				 }

			 }
			}); 
		});		
		
   