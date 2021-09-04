function verifValid() {
  // verify si le formulaire est completé
  var ok = true;
  $('.verify').each(function() {
    if (!$(this).hasClass("is-success")) {
      ok = false;
    }
  });

  if (ok) {
    generateRoom()
  }

  // verifie le nom de la salle si il faut l'enregistrer
  if ($('#saveRoom').is(':checked')){
    if (!$('#roomName').hasClass("is-success")) {
      ok = false;
    }
  }

  if (ok) {
    $("#submit button").removeAttr('disabled');
  } else {
    $("#submit button").attr('disabled', 'disabled');
  }
}

// buguer
function generateRoom(){
  // recupère les var des input
  tables = parseInt($('form select option:checked').val());
  cols = parseInt($('#colonne').val());
  rows = parseInt($('#rangee').val());

  // créé un tableau
  $('body').add('table').attr('id', 'rendu');
  $table = $('#rendu');

  // pour chaque ligne
  for (var i = 0; i < rows; i++){
    ligne = $table.add('tr');
    // pour chaque colonne
    for (var j = 0; j < cols; j++){
      // pour chaque table
      for (var k = 0; k < tables; k++){
        cell = ligne.add('td');
        cell.append('<i class="fas fa-user-graduate"></i>');
      }
      // ajout de la rangée de passage
      ligne.add('td');
    }
  }
}

$(document).ready(function() {
  // affiche ou cache l'input nom de la salle si la case est coché
  $('#saveRoom').on('change', function(e) {
    if ($(this).is(':checked')) {
      $('#inputName').show();
    } else {
      $('#inputName').hide();
    }
    verifValid();
  });

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

  // verifie la validité des select
  $('form select').on('blur change', function() {
    if ($('form select option:checked').val() == '') {
      $(this).parent().addClass("is-danger");
      $(this).parent().removeClass("is-success");
    } else {
      $(this).parent().addClass("is-success");
      $(this).parent().removeClass("is-danger");
    }
  });

  // enable le submit si besoin
  $('.verify').on('blur change', verifValid);
});
