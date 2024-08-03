$(document).ready(function() {
    $('#uploadForm').submit(function(event) {
      event.preventDefault(); // Prevent default form submission
      var formData = new FormData(this);
  
      $.ajax({
        url: '{{ url_for("upload") }}',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
          $('#spinner').addClass('d-none'); // Hide spinner
          alert(response.message); // Show success message
        },
        error: function(xhr, status, error) {
          $('#spinner').addClass('d-none'); // Hide spinner
          alert(xhr.responseJSON.error); // Show error message
        }
      });
    });
  });
  