/* Because i didnt set placeholder values in forms.py they will be set here using vanilla Javascript
//We start indexing at one because CSRF_token is considered and input field 
*/



document.getElementById("id_registration_status").checked = true


//Query All input fields
var form_fields = document.getElementsByTagName("input");
form_fields[4].placeholder = "Username..";
form_fields[5].placeholder = "Firstname..";
form_fields[6].placeholder = "Lastname..";
form_fields[7].placeholder = "Email..";
form_fields[8].placeholder = "Enter password...";
form_fields[9].placeholder = "Re-enter Password...";

for (var field in form_fields) {
  form_fields[field].className += " form-control";
}
