

var toastTrigger = document.getElementById('liveToastBtn')
var toastLiveExample = document.getElementById('liveToast')
// if (toastTrigger) {
//   console.log('hellow')
//   toastTrigger.addEventListener('click', function () {
//     var toast = new bootstrap.Toast(toastLiveExample)

//     toast.show()
//   })
// }

var form = document.getElementById('bookingForm');
form.addEventListener('submit', function (event) {
  event.preventDefault(); // Prevent the form from submitting the traditional way
  var formData = new FormData(form);
  fetch(form.action, {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value
    }
  })
  .then(response => {
    if (response.ok) {
      // Show the toast message
      var toast = new bootstrap.Toast(toastLiveExample);
      toast.show();

      // Clear the form
      form.reset();
      return true; // Assuming your Django view returns JSON response
    } else {
      throw new Error('Network response was not ok.');
    }
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
});

