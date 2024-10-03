const events = [
  {
      title: 'Event 1',
      date: '2024-10-15',
      details: 'Detailed description about Event 1',
      imageUrl: '/public/event1.jpeg'
  },
  {
      title: 'Event 2',
      date: '2024-11-10',
      details: 'Detailed description about Event 2',
      imageUrl: '/public/event2.jpeg'
  },
  {
      title: 'Event 3',
      date: '2024-12-05',
      details: 'Detailed description about Event 3',
      imageUrl: '/public/event3.jpeg'
  },
];

let currentEventTitle = '';

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('load-events').addEventListener('click', () => {
      const eventList = document.getElementById('event-list');
      eventList.innerHTML = '';

      events.forEach(event => {
          const eventDiv = document.createElement('div');
          eventDiv.className = 'col-md-4 mb-4';
          eventDiv.innerHTML = `
              <div class="card">
                  <img src="${event.imageUrl}" class="card-img-top" alt="${event.title}">
                  <div class="card-body">
                      <h5 class="card-title">${event.title}</h5>
                      <p class="card-text">Date: ${event.date}</p>
                      <p class="card-text">${event.details}</p>
                      <button class="btn btn-success register-btn" data-toggle="modal" data-target="#registration-modal">Register</button>
                      <a href="components/event-details.html?title=${encodeURIComponent(event.title)}" class="btn btn-info">Get Details</a>
                  </div>
              </div>`;
          eventList.appendChild(eventDiv);

          eventDiv.querySelector('.register-btn').addEventListener('click', () => {
              currentEventTitle = event.title; 
          });
      });
  });

  document.getElementById('registration-form').onsubmit = function (e) {
      e.preventDefault();
      const name = document.getElementById('name').value;
      const email = document.getElementById('email').value;

      alert(`Thank you for registering for ${currentEventTitle}, ${name}!`);

      document.getElementById('registration-form').reset();
      $('#registration-modal').modal('hide');
  }

  $('.close').on('click', function () {
      $('#registration-modal').modal('hide');
  });
});
