var studentList = [];

$(document).ready(function() {
  // verifie la validité des input
  $('form input').on('blur change', function() {
    if (!$(this).val()) {
      $(this).addClass("is-danger");
      $(this).removeClass("is-success");
    } else {
      $(this).addClass("is-success");
      $(this).removeClass("is-danger");
    }
  });

  $('#ajout').on('click', function(e){
    if (!$('#eleve').val()) {
      $('#eleve').addClass("is-danger");
      $('#eleve').removeClass("is-success");
      e.preventDefault();
      studentList.push($('#eleve').val());
    } else {
      $('#eleve').addClass("is-success");
      $('#eleve').removeClass("is-danger");
    }
  });
});
