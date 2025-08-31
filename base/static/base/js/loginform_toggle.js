//<script>
    // function showForm(role) {
    //   document.getElementById('student').classList.add('hidden');
    //   document.getElementById('faculty').classList.add('hidden');
    //   document.getElementById(role).classList.remove('hidden');
    //   document.getElementById('studentSignup').classList.add('hidden');
      
      // document.getElementById('facultySignup').classList.add('hidden');
    // }

    // function toggleForm(formId) {
    //   document.getElementById('studentSignup').classList.add('hidden');
    //   document.getElementById('facultySignup').classList.add('hidden');
    //   if (formId) document.getElementById(formId).classList.remove('hidden');
    // }
  //   function toggleForm(formId) {
  // document.getElementById('student').classList.add('hidden');
  // document.getElementById('faculty').classList.add('hidden');
  // document.getElementById('studentSignup').classList.add('hidden');
  
 // document.getElementById('facultySignup').classList.add('hidden');

//   if (formId) document.getElementById(formId).classList.remove('hidden');
// }
//     function showForm(role) {
//   ['student','faculty','studentSignup','enterOtp','completeRegistration']
//     .forEach(id => document.getElementById(id).classList.add('hidden'));
//   document.getElementById(role).classList.remove('hidden');
// }

// Remove the auto-login showForm
// showForm('student');

// document.addEventListener("DOMContentLoaded", function() {
  // Read server-side step
  // var step = "{{ step|default:'' }}";
  // if (step === 'email') {
  //   showForm('studentSignup');
  // } else if (step === 'otp') {
  //   showForm('enterOtp');
  // } else if (step === 'register') {
  //   showForm('completeRegistration');
  // }
  // Otherwise, leave whatever the HTML/CSS default is (login visible).
// });
//     document.addEventListener("DOMContentLoaded", function() {
//   var step = "{{ step|default:'student' }}";  // default to login ('student')

//   toggleForm(step === 'email' ? 'studentSignup' : (step === 'otp' ? 'enterOtp' : (step === 'register' ? 'completeRegistration' : 'student')));
// });

function showForm(role) {
  ['student','faculty','studentSignup','enterOtp','completeRegistration'].forEach(id => {
    var el = document.getElementById(id);
    if (el) el.classList.add('hidden');
  });
  document.getElementById(role).classList.remove('hidden');
}

function toggleForm(formId) {
  ['student', 'faculty', 'studentSignup', 'enterOtp', 'completeRegistration'].forEach(id => {
    var el = document.getElementById(id);
    if (el) el.classList.add('hidden');
  });
  if (formId) document.getElementById(formId).classList.remove('hidden');
}

document.addEventListener("DOMContentLoaded", function() {
  var step = "{{ step|default:'' }}";
  if (step === 'email') {
    showForm('studentSignup');
  } else if (step === 'otp') {
    showForm('enterOtp');
  } else if (step === 'register') {
    showForm('completeRegistration');
  }
  // Default is what's in HTML (login shown).
});

