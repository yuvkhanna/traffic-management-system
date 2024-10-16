fetch('/predict_congestion', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      location: { lat: 28.7041, lon: 77.1025 },
      time: '2024-10-15T08:00:00'
    }),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Congestion Level:', data.congestion_level);
  });
  
  fetch('/optimized_route', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      start: 'A',
      destination: 'C'
    }),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Optimal Route:', data.route);
  });
  