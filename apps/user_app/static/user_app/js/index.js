/* eslint-disable func-names */
/* eslint-disable prefer-arrow-callback */


$(document).ready(function () {
  $('#first_name').keyup(function (e) {
    if ($('#first_name').val().length < 2) {
      $('#fname_result').html("At least 2 characters");
    }
    else {
      $('#fname_result').html("");
    }
  })
  $('#last_name').keyup(function (e) {
    if ($('#last_name').val().length < 2) {
      $('#lname_result').html("At least 2 characters");
    }
    else {
      $('#lname_result').html("");
    }
  })
  $('#register_email').keyup(function (e) {
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if ( regex.test($('#register_email').val())) {
      $('#register_email_result').html("");
    }
    else {
      $('#register_email_result').html("Please enter a valid email");
    }
  })
  $('#confirm_password').keyup(function (e) {
    if ($('#password').val() != $('#confirm_password').val() ) {
      $('#password_result').html("Passwords must match");
    }
    else {
      $('#password_result').html("");
    }
  })

}


)




